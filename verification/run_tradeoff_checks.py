"""Finite checks for the four-state copy/run tradeoff.

Checks the complex Bargmann expectation, second moments, addressed register
permutations, both quadrature block encodings and their QPE distributions.
The winding check samples the finite-stock matrix bound. None of these
calculations proves the minimax or asymptotic resource theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import numpy as np


TOLERANCE = 2e-12


def direct_cycle_axes(copies, addresses):
    axes = list(range(4 * copies))
    slots = [j * copies + address for j, address in enumerate(addresses)]
    for output, source in zip(slots, slots[1:] + slots[:1]):
        axes[output] = source
    return axes


def routed_cycle_axes(copies, addresses):
    """Move each chosen copy to its bank's first slot, cycle, and unroute."""
    axes = list(range(4 * copies))
    queue = [(j * copies, j * copies + address)
             for j, address in enumerate(addresses)]
    for first, selected in queue:
        axes[first], axes[selected] = axes[selected], axes[first]
    for bank in range(3):
        first, second = bank * copies, (bank + 1) * copies
        axes[first], axes[second] = axes[second], axes[first]
    for first, selected in reversed(queue):
        axes[first], axes[selected] = axes[selected], axes[first]
    return axes


def sparse_gram(overlap, phase):
    gram = np.eye(4, dtype=complex)
    for index in range(4):
        next_index = (index + 1) % 4
        gram[index, next_index] = overlap * np.exp(1j * phase / 4)
        gram[next_index, index] = gram[index, next_index].conjugate()
    return gram


def states_from_gram(gram):
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    return (eigenvectors * np.sqrt(eigenvalues)) @ eigenvectors.conj().T


def stock_vector(states, copies):
    vector = np.array([1.0 + 0j])
    for state in states.T:
        for _ in range(copies):
            vector = np.kron(vector, state)
    return vector


def check_moments(states, copies):
    dimension = states.shape[0]
    stock = stock_vector(states, copies)
    tensor = stock.reshape((dimension,) * (4 * copies))
    forward = np.zeros_like(stock)
    reverse = np.zeros_like(stock)
    for addresses in itertools.product(range(copies), repeat=4):
        axes = direct_cycle_axes(copies, addresses)
        assert axes == routed_cycle_axes(copies, addresses)
        forward += tensor.transpose(axes).reshape(-1)
        reverse += tensor.transpose(np.argsort(axes)).reshape(-1)
    forward /= copies**4
    reverse /= copies**4
    edge = np.sum(states.conj() * np.roll(states, -1, axis=1), axis=0)
    bargmann = np.prod(edge)
    probability = np.abs(edge)**2
    second_moment = float(np.prod(probability + (1 - probability) / copies))
    real_quadrature = (forward + reverse) / 2
    imag_quadrature = (forward - reverse) / (2j)
    variance = sum(np.vdot(item, item).real - abs(np.vdot(stock, item))**2
                   for item in (real_quadrature, imag_quadrature))
    errors = {
        "bargmann_mean_error": float(abs(np.vdot(stock, forward) - bargmann)),
        "forward_second_moment_error": float(abs(np.vdot(forward, forward) - second_moment)),
        "reverse_second_moment_error": float(abs(np.vdot(reverse, reverse) - second_moment)),
        "variance_sum_error": float(abs(variance - (second_moment - abs(bargmann)**2))),
    }
    assert max(errors.values()) < TOLERANCE, errors
    return {
        "dimension": dimension,
        "copies_per_label": copies,
        "adjacent_overlap_amplitudes": np.abs(edge).tolist(),
        "predicted_second_moment": second_moment,
        **errors,
    }


def prepare_addresses(copies, orientation):
    if orientation == "real":
        phase = 1
    elif orientation == "imaginary":
        phase = -1j
    else:
        raise ValueError(f"Unknown quadrature {orientation}")
    return np.repeat(np.array([1, phase]) / np.sqrt(2), copies**4) / copies**2


def check_qubiterate(states, copies, quadrature, grid):
    """Simulate the walk and inverse QFT on the stock and all address states."""
    stock = stock_vector(states, copies)
    data_dimension = len(stock)
    addresses = list(itertools.product(range(copies), repeat=4))
    basis = np.arange(data_dimension).reshape((2,) * (4 * copies))
    forward = np.array([
        basis.transpose(routed_cycle_axes(copies, address)).reshape(-1)
        for address in addresses
    ])
    reverse = np.argsort(forward, axis=1)
    assert np.array_equal(np.take_along_axis(forward, reverse, axis=1),
                          np.broadcast_to(np.arange(data_dimension), forward.shape))

    rows = np.arange(len(addresses))
    data_columns = np.arange(data_dimension)

    def select(vector):
        selected = np.empty_like(vector)
        selected[0] = np.take_along_axis(vector[1], forward, axis=1)
        selected[1] = np.take_along_axis(vector[0], reverse, axis=1)
        return selected

    amplitude = prepare_addresses(copies, quadrature).reshape(2, -1)

    def inject(data):
        return amplitude[:, :, None] * data

    def project(vector):
        return np.einsum("oa,oaj->j", amplitude.conj(), vector)

    def step(vector):
        selected = select(vector)
        return 2 * inject(project(selected)) - selected

    def readout(vector):
        powers = np.empty((grid, *vector.shape), dtype=complex)
        powers[0] = vector
        for power in range(1, grid):
            powers[power] = step(powers[power - 1])
        return np.fft.fft(powers, axis=0) / grid

    average_cycle = np.zeros((data_dimension, data_dimension), dtype=complex)
    for address in rows:
        average_cycle[data_columns, forward[address]] += 1 / len(addresses)
    if quadrature == "real":
        observable = (average_cycle + average_cycle.conj().T) / 2
    else:
        observable = (average_cycle - average_cycle.conj().T) / (2j)

    # Compare the entire compressed action on computational basis vectors.
    compressed = np.empty_like(observable)
    for index in data_columns:
        data = np.zeros(data_dimension, dtype=complex)
        data[index] = 1
        compressed[:, index] = project(select(inject(data)))
    block_error = float(np.max(np.abs(compressed - observable)))
    initial = inject(stock)
    select_error = float(np.linalg.norm(select(select(initial)) - initial))
    recovered = readout(initial)
    measured = np.sum(np.abs(recovered)**2, axis=(1, 2, 3))

    eigenvalues, eigenvectors = np.linalg.eigh(observable)
    phases = np.arccos(np.clip(eigenvalues, -1, 1))
    weights = np.abs(eigenvectors.conj().T @ stock)**2
    powers_index = np.arange(grid)[:, None]
    expected = np.zeros(grid)
    branch = int(np.argsort(measured)[-2])
    expected_joint = np.zeros(grid)
    for sign in (-1, 1):
        fourier = np.fft.fft(np.exp(sign * 1j * powers_index * phases), axis=0) / grid
        probabilities = np.abs(fourier)**2
        expected += probabilities @ weights / 2
        expected_joint += probabilities @ (weights * probabilities[branch]) / 2
    # Keep the unnormalized postmeasurement stock to audit a repeat on the same copies.
    repeated = np.sum(np.abs(readout(recovered[branch]))**2, axis=(1, 2, 3))
    distribution_error = float(np.max(np.abs(measured - expected)))
    normalization_error = float(abs(np.sum(measured) - 1))
    errors = {
        "compressed_operator_max_error": block_error,
        "select_involution_vector_error": select_error,
        "qpe_probability_max_error": distribution_error,
        "qpe_probability_normalization_error": normalization_error,
        "repeat_qpe_joint_probability_max_error": float(
            np.max(np.abs(repeated - expected_joint))),
    }
    assert max(errors.values()) < TOLERANCE, errors
    return {
        "quadrature": quadrature,
        "copies_per_label": copies,
        "qpe_grid": grid,
        "controlled_walk_uses": grid - 1,
        "first_outcome_for_repeat_check": branch,
        **errors,
    }


def check_winding(counts):
    labels = tuple(itertools.chain.from_iterable(
        itertools.repeat(j, count) for j, count in enumerate(counts)))
    words = np.array(sorted(set(itertools.permutations(labels))))
    overlap, phase, separation = 0.19, 0.37, 0.007
    first = np.prod(sparse_gram(overlap, phase)[labels, words], axis=1)
    second = np.prod(sparse_gram(overlap, phase + separation)[labels, words], axis=1)
    changed = np.count_nonzero(words != labels, axis=1)
    step = (words - labels) % 4
    winding = (np.count_nonzero(step == 1, axis=1)
               - np.count_nonzero(step == 3, axis=1)) / 4
    supported = np.all(step != 2, axis=1)
    assert np.all(winding[supported] == np.round(winding[supported]))
    assert np.all(np.abs(winding[supported]) <= changed[supported] / 4)
    maximum_winding = int(np.max(np.abs(winding[supported])))
    squared_difference = float(np.sum(np.abs(first - second)**2))
    # Every row has the same squared norm because words differ by slot relabeling.
    size = len(labels)
    bound = (2 / 3) * separation**2 * size**4 * overlap**8 * np.exp(2 * size * overlap**2)
    assert 0 < squared_difference <= bound
    return {
        "label_counts": counts,
        "orbit_dimension": len(words),
        "maximum_winding": maximum_winding,
        "squared_hilbert_schmidt_per_row": squared_difference,
        "upper_bound": bound,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("run_tradeoff_results.json"))
    parser.add_argument("--source-root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    random = np.random.default_rng(20261118)
    moments = []
    for dimension, copies in ((2, 1), (2, 2), (2, 3), (3, 2), (4, 2)):
        states = (random.normal(size=(dimension, 4))
                  + 1j * random.normal(size=(dimension, 4)))
        states /= np.linalg.norm(states, axis=0)
        moments.append(check_moments(states, copies))
    for overlap, phase in ((0.2, 0.43), (0.1, -1.1)):
        moments.append(check_moments(states_from_gram(sparse_gram(overlap, phase)), 2))
    circuit_states = np.array([[1, 1, 1, 1], [0, 1, 1j, 0.4 - 0.3j]], dtype=complex)
    circuit_states /= np.linalg.norm(circuit_states, axis=0)
    circuits = [check_qubiterate(circuit_states, 2, quadrature, 64)
                for quadrature in ("real", "imaginary")]
    winding = [check_winding(counts) for counts in (
        (1, 1, 1, 1), (2, 2, 1, 1), (2, 2, 2, 2))]
    assert winding[-1]["maximum_winding"] == 2

    script = Path(__file__).resolve()
    hashes = {"verification/run_tradeoff_checks.py":
              hashlib.sha256(script.read_bytes()).hexdigest()}
    for name in ("verification/requirements.txt", "science/run-tradeoff.md"):
        path = args.source_root / name
        if path.is_file():
            hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    output = {
        "status": "all assertions passed",
        "metadata": {
            "python": platform.python_version(), "numpy": np.__version__,
            "random_seed": 20261118, "sha256": hashes,
        },
        "moment_checks": moments,
        "circuit_checks": circuits,
        "winding_checks": winding,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "moment_cases": len(moments),
                      "circuit_cases": len(circuits), "winding_cases": len(winding),
                      "output": args.output.name}))


if __name__ == "__main__":
    main()
