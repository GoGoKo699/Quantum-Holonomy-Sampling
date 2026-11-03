"""Finite checks of uniform fixed-type sparse-cycle Gram information bounds.

Relative entropy is evaluated by eight-point Gauss-Legendre integration of
its Hessian, avoiding direct cancellation of a quantity of order c**8.
This is numerical quadrature, not a certified interval bound or a proof of
the asymptotic theorem. A separately computed Petz chi-square bound is also
checked in every case.
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
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh, solve


def words(counts):
    labels = sum(([j] * r for j, r in enumerate(counts)), [])
    return np.array(sorted(set(itertools.permutations(labels))), dtype=int)


def gram(c, phi):
    matrix = np.eye(4, dtype=complex)
    for j in range(4):
        k = (j + 1) % 4
        matrix[j, k] = c * np.exp(1j * phi / 4)
        matrix[k, j] = np.conj(matrix[j, k])
    return matrix


def compressed(counts, c, phi):
    stock_words = words(counts)
    matrix = gram(c, phi)
    return np.prod(matrix[stock_words[:, None, :], stock_words[None, :, :]], axis=2)


def stable_relative_entropy(a, b):
    """Numerical D(a/K||b/K) through the exact Hessian integral identity."""
    delta = a - b
    nodes, weights = leggauss(8)
    result = 0.0
    for node, weight in zip(nodes, weights):
        s = (node + 1) / 2
        values, vectors = eigh(b + s * delta, check_finite=False)
        transformed = vectors.conj().T @ delta @ vectors
        difference = values[:, None] - values[None, :]
        baseline = np.broadcast_to(values[None, :], difference.shape)
        kernel = np.empty_like(difference)
        separated = np.abs(difference) > 1e-11 * baseline
        kernel[separated] = np.log1p(
            difference[separated] / baseline[separated]) / difference[separated]
        kernel[~separated] = 1 / baseline[~separated]
        hessian = float(np.sum(np.abs(transformed) ** 2 * kernel))
        result += weight / 2 * (1 - s) * hessian
    return result / len(a)


def source_metadata():
    directory = Path(__file__).resolve().parent
    paths = [Path(__file__).resolve(), directory / "requirements-phase.txt",
             directory.parent / "science" / "block-information.md",
             directory.parent / "science" / "coherent-runs.md"]
    return {
        "python": platform.python_version(), "numpy": np.__version__,
        "scipy": scipy.__version__, "hessian_quadrature_nodes": 8,
        "sha256": {str(p.relative_to(directory.parent)):
                   hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("stock_information_results.json"))
    args = parser.parse_args()
    records = []
    for counts in [(1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1)]:
        t = sum(counts)
        for c in [0.01, 0.1, 0.25]:
            for phi in [0.0, 0.37, np.pi / 2]:
                theta = phi + np.pi / 8
                a = compressed(counts, c, phi)
                b = compressed(counts, c, theta)
                eigen_min = float(eigh(a, eigvals_only=True, check_finite=False)[0])
                eigen_bound = float(np.exp(-2 * t * c * c))
                delta = a - b
                hs = float(np.linalg.norm(delta, "fro") ** 2 / len(a))
                hs_bound = float((8 / 3) * t**4 * c**8 * np.exp(2 * t * c * c))
                divergence = stable_relative_entropy(a, b)
                chi_square = float(np.trace(
                    delta @ solve(b, delta, assume_a="pos", check_finite=False)
                ).real / len(a))
                divergence_bound = float((8 / 3) * t**4 * c**8 * np.exp(4 * t * c * c))
                assert np.isclose(np.trace(a).real, len(a))
                assert eigen_min >= eigen_bound - 1e-11
                assert hs <= hs_bound * (1 + 1e-9)
                assert divergence >= -1e-30
                assert divergence <= chi_square * (1 + 1e-9)
                assert chi_square <= divergence_bound * (1 + 1e-9)
                records.append({
                    "counts": counts, "stock_size": t, "orbit_dimension": len(a),
                    "c": c, "phi": float(phi), "theta": float(theta),
                    "lambda_min": eigen_min, "lambda_lower_bound": eigen_bound,
                    "hs_squared_per_row": hs, "hs_upper_bound": hs_bound,
                    "relative_entropy_quadrature": divergence,
                    "petz_chi_square": chi_square,
                    "relative_entropy_upper_bound": divergence_bound,
                    "relative_entropy_over_c8": divergence / c**8,
                })
    output = {"status": "all assertions passed", "cases": len(records),
              "metadata": source_metadata(), "records": records}
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "status": output["status"], "cases": len(records),
        "orbit_dimensions": sorted({r["orbit_dimension"] for r in records}),
        "minimum_eigenvalue_margin": min(
            r["lambda_min"] - r["lambda_lower_bound"] for r in records),
        "max_divergence_bound_ratio": max(
            r["relative_entropy_quadrature"] / r["relative_entropy_upper_bound"]
            for r in records),
        "output": args.output.name,
    }))


if __name__ == "__main__":
    main()
