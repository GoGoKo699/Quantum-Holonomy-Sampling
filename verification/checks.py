"""Small deterministic checks of holonomy identities and coherent subroutines.

These are finite-dimensional numerical checks, not an implementation of the
QSVT compiler, a proof of an asymptotic bound, or evidence of originality.
Run with: python verification/checks.py
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import block_diag, expm


SEED = 20261031
TOL = 2e-10
RNG = np.random.default_rng(SEED)


def require(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def projector(v: np.ndarray) -> np.ndarray:
    return np.outer(v, v.conj())


def op_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, 2))


def trace_norm_hermitian(a: np.ndarray) -> float:
    return float(np.abs(np.linalg.eigvalsh((a + a.conj().T) / 2)).sum())


def circular_distance(a: float | np.ndarray, b: float) -> np.ndarray:
    return np.abs(np.angle(np.exp(1j * (a - b))))


def random_state(d: int) -> np.ndarray:
    v = RNG.normal(size=d) + 1j * RNG.normal(size=d)
    return v / np.linalg.norm(v)


def positive_sqrt(a: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(a)
    require(float(values.min()) > 0, "The tested Gram matrix must be positive.")
    return (vectors * np.sqrt(values)) @ vectors.conj().T


def transport(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    z = projector(x) + projector(y) - np.eye(x.size)
    values, vectors = np.linalg.eigh(z)
    result = (vectors * np.sign(values)) @ vectors.conj().T
    # Independent SVD polar calculation checks the whole operator, not only
    # its action on the occupied ray. Exploit Hermiticity numerically.
    left, singular_values, right = np.linalg.svd(z)
    require(float(singular_values.min()) > 1e-8, "A tested transport is singular.")
    require(op_norm(result - left @ right) < TOL,
            "The spectral sign and SVD polar factor disagree.")
    return result


def loop(states: np.ndarray) -> tuple[np.ndarray, complex, float]:
    d, length = states.shape
    w = np.eye(d, dtype=complex)
    bargmann = 1 + 0j
    local_residual = 0.0
    for j in range(length):
        x, y = states[:, j], states[:, (j + 1) % length]
        overlap = np.vdot(y, x)
        require(abs(overlap) > 1e-5, "No tested transport may have zero overlap.")
        t = transport(x, y)
        local_residual = max(
            local_residual,
            float(np.linalg.norm(t @ x - overlap / abs(overlap) * y)),
        )
        w = t @ w
        bargmann *= np.vdot(x, y)
    return w, bargmann, local_residual


def cyclic_family(length: int, c: float, phi: float):
    # Match science/lower-bound.md: S|j> = |j+1>, with cyclic indices.
    # Consequently G[j,j+1] = c exp(i phi/L).
    shift = np.roll(np.eye(length), 1, axis=0)
    phase = np.exp(1j * phi / length)
    gram = np.eye(length) + c * (phase.conjugate() * shift + phase * shift.T)
    return gram, positive_sqrt(gram), shift


def check_transport_and_symmetries() -> dict:
    pairs = []
    for r in (0.03, 0.4, 1.0):
        x = np.array([1, 0, 0], dtype=complex)
        y = np.exp(0.83j) * np.array([r, np.sqrt(1 - r * r), 0])
        t = transport(x, y)
        expected = np.vdot(y, x) / abs(np.vdot(y, x)) * y
        row = {
            "overlap": r,
            "mapping_residual": float(np.linalg.norm(t @ x - expected)),
            "unitarity_residual": op_norm(t.conj().T @ t - np.eye(3)),
        }
        require(max(row["mapping_residual"], row["unitarity_residual"]) < TOL,
                "The canonical transport failed, including the parallel-state case.")
        pairs.append(row)

    records = []
    for d, length in ((3, 4), (5, 7), (7, 9)):
        states = np.column_stack([random_state(d) for _ in range(length)])
        w, bargmann, residual = loop(states)
        phi = float(np.angle(bargmann))
        phases = np.exp(1j * RNG.uniform(-np.pi, np.pi, size=length))
        gauge_w, gauge_b, _ = loop(states * phases)
        q, _ = np.linalg.qr(RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d)))
        conjugated_w, _, _ = loop(q @ states)
        reverse_w, reverse_b, _ = loop(states[:, [0, *range(length - 1, 0, -1)]])
        row = {
            "dimension": d,
            "length": length,
            "local_mapping_residual": residual,
            "loop_eigenphase_residual": float(np.linalg.norm(
                w @ states[:, 0] - np.exp(-1j * phi) * states[:, 0])),
            "gauge_operator_residual": op_norm(gauge_w - w),
            "gauge_phase_residual": float(circular_distance(np.angle(gauge_b), phi)),
            "common_unitary_covariance_residual": op_norm(conjugated_w - q @ w @ q.conj().T),
            "reversed_loop_adjoint_residual": op_norm(reverse_w - w.conj().T),
            "reversed_phase_residual": float(circular_distance(np.angle(reverse_b), -phi)),
        }
        require(all(value < TOL for key, value in row.items() if key.endswith("residual")),
                "Loop phase, gauge, or reversal convention failed.")
        records.append(row)

    x, y = random_state(3), random_state(3)
    h = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    rx, ry = np.eye(3) - 2 * projector(x), np.eye(3) - 2 * projector(y)
    b = np.kron(h, np.eye(3)) @ block_diag(-rx, -ry) @ np.kron(h, np.eye(3))
    z = projector(x) + projector(y) - np.eye(3)
    lcu = {
        "top_block_residual": op_norm(b[:3, :3] - z),
        "unitarity_residual": op_norm(b.conj().T @ b - np.eye(6)),
    }
    require(max(lcu.values()) < TOL, "The LCU reflection signs are incorrect.")
    return {"explicit_pairs": pairs, "loops": records, "one_ancilla_lcu": lcu}


def qpe_distribution(w: np.ndarray, psi: np.ndarray, bits: int) -> np.ndarray:
    """State-vector circuit: Hadamards, controlled powers, inverse QFT."""
    count = 1 << bits
    indices = np.arange(count)
    amplitudes = np.tile(psi, (count, 1)) / np.sqrt(count)
    for bit in range(bits):
        power = np.linalg.matrix_power(w, 1 << bit)
        mask = (indices & (1 << bit)) != 0
        amplitudes[mask] = amplitudes[mask] @ power.T
    inverse_qft = np.exp(-2j * np.pi * np.outer(indices, indices) / count) / np.sqrt(count)
    amplitudes = inverse_qft @ amplitudes
    return np.sum(np.abs(amplitudes) ** 2, axis=1)


def check_coherent_phase_readout() -> list[dict]:
    records = []
    # Match the sufficient F >= 16*pi/epsilon convention in science/algorithm.md.
    bits = 8
    count = 1 << bits
    bins = np.arange(count)
    pauli_x = np.array([[0, 1], [1, 0]])
    pauli_y = np.array([[0, -1j], [1j, 0]])
    for length, phi in ((4, 0.73), (5, -3.08)):
        _, states, _ = cyclic_family(length, 0.2, phi)
        w, _, _ = loop(states)
        psi = states[:, 0]
        probabilities = qpe_distribution(w, psi, bits)
        # Independently predicted finite geometric-series distribution.
        frequencies = -phi - 2 * np.pi * bins / count
        predicted = np.abs(np.exp(1j * np.outer(frequencies, bins)).sum(axis=1) / count) ** 2
        epsilon = np.pi / 16
        good = circular_distance(-2 * np.pi * bins / count, phi) <= epsilon
        shifted = qpe_distribution(-w, psi, bits)
        ramsey = np.stack((psi, w @ psi)) / np.sqrt(2)
        control = ramsey @ ramsey.conj().T
        row = {
            "length": length,
            "phase": phi,
            "control_qubits": bits,
            "controlled_loop_uses": count - 1,
            "probability_normalization_residual": float(abs(probabilities.sum() - 1)),
            "distribution_residual": float(np.max(np.abs(probabilities - predicted))),
            "circular_error_tolerance": epsilon,
            "success_probability": float(probabilities[good].sum()),
            "ramsey_x_residual": float(abs(np.trace(pauli_x @ control).real - np.cos(phi))),
            "ramsey_y_residual": float(abs(np.trace(pauli_y @ control).real + np.sin(phi))),
            "negated_loop_distribution_total_variation": float(np.abs(shifted - probabilities).sum() / 2),
        }
        require(all(v < TOL for k, v in row.items() if k.endswith("residual")),
                "The controlled loop readout has a phase or orientation error.")
        require(row["success_probability"] > 0.9, "The finite QPE readout failed its tolerance.")
        require(row["negated_loop_distribution_total_variation"] > 0.85,
                "The readout must detect an otherwise invisible global sign.")
        records.append(row)
    return records


def check_cyclic_gram_lower_bound() -> dict:
    records = []
    for length in (4, 5, 8):
        for c in (0.08, 0.25):
            for phi in (-2.3, 0.4):
                g, states, shift = cyclic_family(length, c, phi)
                _, bargmann, _ = loop(states)
                phase = np.exp(1j * phi / length)
                dg = 1j * c / length * (phase * shift.T - phase.conjugate() * shift)
                derivative = 0.5 * np.linalg.solve(states, dg)
                fd_step = 1e-5
                _, plus, _ = cyclic_family(length, c, phi + fd_step)
                _, minus, _ = cyclic_family(length, c, phi - fd_step)
                finite_derivative = (plus - minus) / (2 * fd_step)
                h = 0.12
                _, nearby, _ = cyclic_family(length, c, phi + h)
                fidelity = float(abs(np.vdot(states[:, 0], nearby[:, 0])) ** 2)
                bound = c / (length * np.sqrt(1 - 2 * c))
                covariance = max(float(np.linalg.norm(
                    states[:, j] - np.linalg.matrix_power(shift, j) @ states[:, 0]))
                    for j in range(length))
                row = {
                    "length": length, "c": c, "phase": phi,
                    "gram_reconstruction_residual": op_norm(states.conj().T @ states - g),
                    "normalization_residual": float(np.max(np.abs(np.diag(g) - 1))),
                    "phase_identity_residual": float(circular_distance(np.angle(bargmann), phi)),
                    "magnitude_relative_residual": float(abs(abs(bargmann) / c ** length - 1)),
                    "covariance_residual": covariance,
                    "commuting_derivative_residual": op_norm(g @ dg - dg @ g),
                    "finite_derivative_relative_residual": op_norm(finite_derivative - derivative) / op_norm(derivative),
                    "derivative_bound_ratio": float(np.max(np.linalg.norm(derivative, axis=0)) / bound),
                    "finite_fidelity_bound_ratio": max(0.0, 1 - fidelity) / (h * h * bound * bound),
                }
                require(all(v < TOL for k, v in row.items()
                            if k.endswith("residual") and k != "finite_derivative_relative_residual"),
                        "The cyclic Gram family has an algebraic or covariance error.")
                require(row["finite_derivative_relative_residual"] < 2e-6,
                        "The analytic derivative disagrees with a central finite difference.")
                require(max(row["derivative_bound_ratio"], row["finite_fidelity_bound_ratio"]) < 1 + 1e-8,
                        "A tested lower-bound inequality failed.")
                records.append(row)

    # An actual two-copy density-matrix calculation, with distinct labels.
    length, c, phi, h = 4, 0.25, 0.4, 0.12
    _, a, _ = cyclic_family(length, c, phi)
    _, b, _ = cyclic_family(length, c, phi + h)
    va, vb = np.kron(a[:, 1], a[:, 3]), np.kron(b[:, 1], b[:, 3])
    single_fidelity = float(abs(np.vdot(a[:, 0], b[:, 0])) ** 2)
    trace_distance = trace_norm_hermitian(projector(va) - projector(vb)) / 2
    a_bound = h * h * c * c / (length * length * (1 - 2 * c))
    two_copy = {
        "product_fidelity_residual": float(abs(abs(np.vdot(va, vb)) ** 2 - single_fidelity ** 2)),
        "trace_distance": trace_distance,
        "pure_state_trace_distance_residual": float(abs(trace_distance - np.sqrt(1 - single_fidelity ** 2))),
        "bernoulli_trace_distance_bound": float(np.sqrt(2 * a_bound)),
    }
    require(two_copy["product_fidelity_residual"] < TOL and
            two_copy["pure_state_trace_distance_residual"] < TOL and
            trace_distance <= two_copy["bernoulli_trace_distance_bound"] + TOL,
            "The finite two-copy testing calculation failed.")
    return {"families": records, "two_copy_testing": two_copy}


def swap_matrix(d: int) -> np.ndarray:
    swap = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            swap[j * d + i, i * d + j] = 1
    return swap


def controlled_partial_swap(d: int, delta: float) -> np.ndarray:
    return expm(-1j * delta * np.kron(np.diag([0, 1]), swap_matrix(d)))


def partial_swap_circuit_residuals(d: int, delta: float) -> tuple[float, float]:
    """Explicit clean-ancilla phase-kickback circuit, order C,a,T,P."""
    identity = np.eye(d * d)
    hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    h = np.kron(hadamard, identity)
    compute_swap_eigenvalue = h @ block_diag(identity, swap_matrix(d)) @ h
    compute = np.kron(np.eye(2), compute_swap_eigenvalue)
    phase = np.diag([1, 1, np.exp(-1j * delta), np.exp(1j * delta)])
    circuit = compute @ np.kron(phase, identity) @ compute
    base = np.arange(d * d)
    clean = np.concatenate((base, 2 * d * d + base))
    dirty = np.concatenate((d * d + base, 3 * d * d + base))
    return (
        op_norm(circuit[np.ix_(clean, clean)] - controlled_partial_swap(d, delta)),
        op_norm(circuit[np.ix_(dirty, clean)]),
    )


def dme_kraus(rho: np.ndarray, delta: float) -> list[np.ndarray]:
    """Contract the explicit unitary with program input, then trace program."""
    d = rho.shape[0]
    u = controlled_partial_swap(d, delta).reshape(2 * d, d, 2 * d, d)
    values, vectors = np.linalg.eigh(rho)
    kraus = []
    for value, vector in zip(values, vectors.T):
        if value > 1e-14:
            for outcome in range(d):
                kraus.append(np.sqrt(value) * np.einsum("aip,p->ai", u[:, outcome, :, :], vector))
    return kraus


def apply_channel(x: np.ndarray, kraus: list[np.ndarray]) -> np.ndarray:
    return sum((k @ x @ k.conj().T for k in kraus), np.zeros_like(x, dtype=complex))


def dme_block_formula(x: np.ndarray, rho: np.ndarray, delta: float) -> np.ndarray:
    d = rho.shape[0]
    co, si = np.cos(delta), np.sin(delta)
    x00, x01 = x[:d, :d], x[:d, d:]
    x10, x11 = x[d:, :d], x[d:, d:]
    return np.block([
        [x00, co * x01 + 1j * si * x01 @ rho],
        [co * x10 - 1j * si * rho @ x10,
         co * co * x11 + si * si * np.trace(x11) * rho
         - 1j * co * si * (rho @ x11 - x11 @ rho)],
    ])


def check_controlled_dme() -> dict:
    one_step = []
    convergence = []
    for d in (2, 3):
        psi = random_state(d)
        pure = projector(psi)
        for name, rho in (("pure", pure), ("mixed", 0.7 * pure + 0.3 * np.eye(d) / d)):
            for delta in (0.17, -0.13):
                kraus = dme_kraus(rho, delta)
                dim = 2 * d
                formula_residual = 0.0
                for i in range(dim):
                    for j in range(dim):
                        unit = np.zeros((dim, dim), dtype=complex)
                        unit[i, j] = 1
                        formula_residual = max(formula_residual, op_norm(
                            apply_channel(unit, kraus) - dme_block_formula(unit, rho, delta)))
                phi = np.eye(dim).reshape(-1) / np.sqrt(dim)
                omega = projector(phi)
                extended = [np.kron(k, np.eye(dim)) for k in kraus]
                actual = apply_channel(omega, extended)
                ideal_unitary = expm(-1j * delta * np.kron(np.diag([0, 1]), rho))
                ideal = np.kron(ideal_unitary, np.eye(dim)) @ phi
                choi_error = trace_norm_hermitian(actual - projector(ideal))
                circuit_error, leakage = partial_swap_circuit_residuals(d, delta)
                row = {
                    "dimension": d, "program": name, "step": delta,
                    "all_matrix_units_formula_residual": formula_residual,
                    "trace_preservation_residual": op_norm(sum(k.conj().T @ k for k in kraus) - np.eye(dim)),
                    "clean_ancilla_circuit_residual": circuit_error,
                    "ancilla_leakage_residual": leakage,
                    "normalized_choi_trace_norm_error": choi_error,
                    "diamond_upper_bound": 4 * delta * delta,
                }
                require(all(v < TOL for k, v in row.items() if k.endswith("residual")),
                        "The physical partial-swap circuit disagrees with its reduced channel.")
                require(choi_error <= row["diamond_upper_bound"] + TOL,
                        "A tested entangled input exceeds the analytical local diamond bound.")
                one_step.append(row)

        dim = 2 * d
        entangled = np.eye(dim).reshape(-1) / np.sqrt(dim)
        omega = projector(entangled)
        reflection = np.eye(d) - 2 * pure
        controlled_reflection = block_diag(np.eye(d), reflection)
        ideal_vector = np.kron(controlled_reflection, np.eye(dim)) @ entangled
        plus = np.array([1, 1]) / np.sqrt(2)
        occupied_input = projector(np.kron(plus, psi))
        mixed_target_input = np.kron(projector(plus), np.eye(d) / d)
        for copies in (16, 64, 256):
            delta = np.pi / copies
            kraus = dme_kraus(pure, delta)
            extended = [np.kron(k, np.eye(dim)) for k in kraus]
            actual = omega.copy()
            occupied = occupied_input.copy()
            mixed_target = mixed_target_input.copy()
            for _ in range(copies):
                actual = apply_channel(actual, extended)
                occupied = apply_channel(occupied, kraus)
                mixed_target = apply_channel(mixed_target, kraus)
            choi_error = trace_norm_hermitian(actual - projector(ideal_vector))
            control = np.einsum("aibi->ab", occupied.reshape(2, d, 2, d))
            off_diagonal_factor = np.cos(delta) ** copies * (np.eye(d) - pure) - pure
            row = {
                "dimension": d, "fresh_program_copies": copies,
                "normalized_choi_trace_norm_error": choi_error,
                "diamond_upper_bound": min(2.0, 4 * np.pi * np.pi / copies),
                "occupied_branch_minus_phase_residual": float(abs(2 * control[0, 1] + 1)),
                "control_coherence_formula_residual": op_norm(
                    mixed_target[:d, d:] - off_diagonal_factor / (2 * d)),
                "trace_residual": float(abs(np.trace(actual) - 1)),
            }
            require(all(v < TOL for k, v in row.items() if k.endswith("residual")),
                    "Repeated controlled DME lost the fixed reflection phase.")
            require(choi_error <= row["diamond_upper_bound"] + TOL,
                    "A tested entangled input exceeds the analytical repeated diamond bound.")
            convergence.append(row)

    # Negative control: uncontrolled channels cannot distinguish R from -R.
    psi = np.array([1, 1j]) / np.sqrt(2)
    r = np.eye(2) - 2 * projector(psi)
    state = projector(np.array([1, 2j]) / np.sqrt(5))
    uncontrolled = op_norm(r @ state @ r.conj().T - (-r) @ state @ (-r).conj().T)
    input_vector = np.kron(np.array([1, 1]) / np.sqrt(2), psi)
    v1 = block_diag(np.eye(2), r) @ input_vector
    v2 = block_diag(np.eye(2), -r) @ input_vector
    controlled_distance = trace_norm_hermitian(projector(v1) - projector(v2)) / 2
    require(uncontrolled < TOL and abs(controlled_distance - 1) < TOL,
            "The global-phase negative control failed.")
    return {
        "one_step_channels": one_step,
        "fresh_copy_reflection_channels": convergence,
        "global_phase_negative_control": {
            "uncontrolled_channel_residual": uncontrolled,
            "controlled_output_trace_distance": controlled_distance,
        },
    }


def main() -> None:
    results = {
        "status": "passed",
        "seed": SEED,
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": (
            "Deterministic finite-matrix, state-vector, and consumed-program channel checks. "
            "No full QSVT compilation, asymptotic proof, empirical diamond-norm optimization, "
            "experimental implementation, or novelty certification."
        ),
        "transport": check_transport_and_symmetries(),
        "coherent_phase_readout": check_coherent_phase_readout(),
        "cyclic_gram_lower_bound": check_cyclic_gram_lower_bound(),
        "controlled_dme": check_controlled_dme(),
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(results, indent=2, allow_nan=False) + "\n")
    print(json.dumps({
        "status": results["status"],
        "output": str(path),
        "transport_loops": len(results["transport"]["loops"]),
        "coherent_readouts": len(results["coherent_phase_readout"]),
        "cyclic_gram_families": len(results["cyclic_gram_lower_bound"]["families"]),
        "controlled_dme_one_step_channels": len(results["controlled_dme"]["one_step_channels"]),
        "controlled_dme_reflection_channels": len(results["controlled_dme"]["fresh_copy_reflection_channels"]),
    }, indent=2))


if __name__ == "__main__":
    main()
