"""Finite checks of optimal invariant four-copy loop-phase information.

The orbit Gram and its winding derivative are built entry by entry, then
compared with the independently stated exact spectrum and QFI formula.
These finite calculations do not prove an adaptive transcript lower bound.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import numpy as np
import scipy


PERMUTATIONS = list(itertools.permutations(range(4)))
EXACT_SPECTRUM = [
    (1, -2, 2, 2), (1, 0, -2, 3), (1, 4, 2, 1),
    (-1, -4, 2, 1), (-1, 0, -2, 3), (-1, 2, 2, 2),
    (1j, -2, 0, 3), (1j, 2, 0, 3),
    (-1j, -2, 0, 3), (-1j, 2, 0, 3),
]


def gram(c, phi):
    matrix = np.eye(4, dtype=complex)
    for j in range(4):
        matrix[j, (j + 1) % 4] = c * np.exp(1j * phi / 4)
        matrix[(j + 1) % 4, j] = c * np.exp(-1j * phi / 4)
    return matrix


def orbit_gram(c, phi):
    matrix = gram(c, phi)
    return np.array([
        [np.prod([matrix[p[k], q[k]] for k in range(4)])
         for q in PERMUTATIONS]
        for p in PERMUTATIONS
    ])


def winding_derivative(c, phi):
    matrix = gram(c, phi)
    result = np.zeros((24, 24), complex)
    for a, p in enumerate(PERMUTATIONS):
        for b, q in enumerate(PERMUTATIONS):
            steps = []
            for k in range(4):
                displacement = (q[k] - p[k]) % 4
                if displacement == 2:
                    break
                steps.append({0: 0, 1: 1, 3: -1}[displacement])
            else:
                result[a, b] = 1j * sum(steps) / 4 * np.prod(
                    [matrix[p[k], q[k]] for k in range(4)])
    return result


def matrix_qfi(matrix, derivative):
    values, vectors = np.linalg.eigh(matrix)
    derivative = vectors.conj().T @ derivative @ vectors
    return float((2 / 24 * np.sum(
        np.abs(derivative) ** 2 / (values[:, None] + values[None, :])
    )).real)


def spectral_formula(c, phi):
    eigenvalues = []
    information = 0.0
    for z, a, u, multiplicity in EXACT_SPECTRUM:
        angle = phi + np.angle(z)
        value = 1 + a * c**2 + u * c**4 + 2 * c**4 * np.cos(angle)
        eigenvalues.extend([float(value)] * multiplicity)
        information += multiplicity * 4 * c**8 * np.sin(angle)**2 / value / 24
    return np.sort(eigenvalues), float(information)


def regular_operator(permutation):
    indices = {p: i for i, p in enumerate(PERMUTATIONS)}
    matrix = np.zeros((24, 24), dtype=np.int64)
    for column, q in enumerate(PERMUTATIONS):
        composed = tuple(q[permutation[k]] for k in range(4))
        matrix[indices[composed], column] = 1
    return matrix


def check_group_identities():
    identity = np.eye(24, dtype=np.int64)
    a = sum(regular_operator(p) for p in [
        (1, 0, 2, 3), (0, 2, 1, 3), (0, 1, 3, 2), (3, 1, 2, 0)
    ])
    b = regular_operator((1, 0, 3, 2)) + regular_operator((3, 2, 1, 0))
    g = regular_operator((1, 2, 3, 0))
    assert np.array_equal(b @ b, 2 * identity + 2 * g @ g)
    assert np.array_equal(b @ a, (identity + g @ g) @ a)
    assert np.array_equal(a @ a, (g + g.T) @ a + 4 * identity + 2 * b)


def source_metadata():
    directory = Path(__file__).resolve().parent
    paths = [Path(__file__).resolve(), directory / "requirements-phase.txt",
             directory.parent / "science" / "block-information.md"]
    return {
        "python": platform.python_version(), "numpy": np.__version__,
        "scipy": scipy.__version__,
        "sha256": {str(p.relative_to(directory.parent)):
                   hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("block_phase_results.json"))
    args = parser.parse_args()
    check_group_identities()
    records = []
    for phi in (0.0, 0.37, np.pi / 2, np.pi):
        for c in (0.25, 0.1, 0.03, 0.01):
            matrix = orbit_gram(c, phi)
            derivative = winding_derivative(c, phi)
            values, formula = spectral_formula(c, phi)
            information = matrix_qfi(matrix, derivative)
            delta = 4 * c**2 + 4 * c**4
            lower = 2 * c**8
            upper = lower * (1 + delta**2 / (1 - delta))
            assert np.allclose(np.linalg.eigvalsh(matrix), values,
                               rtol=1e-12, atol=1e-12)
            assert np.isclose(information, formula, rtol=1e-11, atol=0)
            assert lower * (1 - 1e-11) <= information <= upper * (1 + 1e-11)
            assert np.isclose(np.trace(derivative @ derivative).real,
                              48 * c**8, rtol=1e-11, atol=0)
            commutator = np.linalg.norm(matrix @ derivative - derivative @ matrix)
            assert commutator <= 1e-12 * np.linalg.norm(derivative)
            if phi == 0:
                assert np.isclose(information, 2 * c**8 / (1 - 4 * c**4),
                                  rtol=1e-11, atol=0)
            records.append({
                "c": c, "phi": float(phi), "qfi": information,
                "exact_spectrum_qfi": formula,
                "qfi_over_c8": information / c**8,
                "qfi_lower_bound": lower, "qfi_upper_bound": upper,
                "commutator_norm": float(commutator),
            })
    output = {"status": "all assertions passed", "cases": len(records),
              "exact_integer_group_identities": 3,
              "metadata": source_metadata(), "records": records}
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "cases": len(records),
                      "exact_integer_group_identities": 3,
                      "output": args.output.name}))


if __name__ == "__main__":
    main()
