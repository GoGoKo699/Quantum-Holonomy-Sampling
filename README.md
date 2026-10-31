# Quantum Holonomy Sampling

**How many copies of unknown quantum states are needed to learn the geometric phase around a loop?** This project gives a coherent algorithm and a nearly matching statistical lower bound. The copy cost depends polynomially on the loop length and local overlap, even when direct cyclic interference has exponentially small visibility.

There are $`L`$ classically labeled sources of independent pure states $`|\psi_j\rangle`$. Neighboring overlap amplitudes obey $`|\langle\psi_j|\psi_{j+1}\rangle|\ge c\gt 0`$, with $`|\psi_{L+1}\rangle=|\psi_1\rangle`$. The target is

```math
\Phi=\arg B\pmod{2\pi},
\qquad
B=\prod_{j=1}^{L}\langle\psi_j|\psi_{j+1}\rangle.
```

The receiver gets quantum copies and can process their registers coherently. State-preparation unitaries, inverse preparation circuits and a coherent source-index oracle are not supplied.

## Principal result

For circular accuracy $`0\lt \epsilon\le\pi/16`$ and success probability at least $`2/3`$:

| Result | Total source copies | Scope |
|---|---|---|
| Coherent upper bound | $`O\!\left(L^2c^{-2}\epsilon^{-2}\log^2(L/\epsilon)\right)`$ | $`L\ge4`$, all $`0\lt c\le1`$; independent of Hilbert-space dimension $`d`$ |
| Minimax lower bound | $`\Omega\!\left(L^2c^{-2}\epsilon^{-2}\right)`$ | $`L\ge4`$, $`d\ge L`$, $`0\lt c\le1/4`$; arbitrary collective and adaptive protocols |

The powers of loop length, reciprocal overlap and accuracy therefore match up to logarithms in the lower-bound regime. The theorem counts every consumed copy. The [precise model](science/model.md) defines the worst-case copy cap and distinguishes overlap amplitude from squared fidelity.

## Why weak visibility is avoidable

For adjacent pure-state projectors $`P,Q`$, the unitary $`\mathrm{sign}(P+Q-I)`$ transports one ray to the other with the phase of their overlap. Composing these transports around the loop returns the starting state with eigenvalue $`e^{-i\Phi}`$. Phase estimation reads that eigenvalue.

The transport is implemented using established polar-decomposition machinery. Controlled partial swaps then simulate every required reflection from fresh copies, with a fixed control phase and an explicit error budget. The [related-work account](references/related-work.md) credits the direct-rotation, QSVT, phase-estimation and sample-simulation ingredients.

The lower-bound family has

```math
B=c^Le^{i\phi},
```

with nonzero overlaps only between neighbors on a ring. Direct full-cycle measurements require order $`c^{-2L}\epsilon^{-2}`$ repetitions on this family, each consuming $`L`$ copies. The coherent algorithm uses polynomially many copies, while the finite discrimination argument establishes its intrinsic polynomial scale. This is a comparison with the specified direct-cycle measurement strategy; no general classical-versus-quantum separation is asserted.

## Read the science

| Question | Account |
|---|---|
| What exactly is supplied, estimated and counted? | [Model and main theorem](science/model.md) |
| How is the geometric phase preserved locally? | [Canonical transport](science/transport.md) |
| How do the controlled loop and error budgets fit together? | [Complete algorithm](science/algorithm.md) |
| What are the copy, gate, memory and compilation costs? | [Resource accounting](science/resources.md) |
| Why can no collective or adaptive protocol beat the stated scale? | [Finite lower bound](science/lower-bound.md) |
| What happens on a sparse loop, and what does the direct test cost? | [Worked examples and comparison](science/examples.md) |
| What does the result change operationally? | [Physical interpretation](science/interpretation.md) |
| Which results are inherited, and which models differ? | [Related work](references/related-work.md) and [bibliography](references/references.bib) |

The [scientific overview](science/README.md) gives proof and interpretation routes. The [LLM reading guide](llms.txt) maps specific questions to authoritative files.

## Processing resources

Writing $`n=\lceil\log_2 d\rceil`$, the known-angle quantum gate count is $`O(nN)`$, where $`N`$ is the explicit copy budget. Program copies can be streamed using $`2n+O(\log(1/\epsilon))`$ live qubits. A finite universal gate set adds synthesis logarithms. Classical phase-sequence compilation is charged separately and can dominate quantum processing in some parameter regimes; copy optimality is not a claim of universally optimal end-to-end runtime.

## Reproduce the finite checks

With the dependencies in [verification/requirements.txt](verification/requirements.txt), run from the repository root:

```bash
python verification/checks.py
```

The [verification guide](verification/README.md) and [recorded results](verification/results.json) cover transport and gauge identities, sparse Gram families, coherent Fourier readout, and controlled sample simulation with entangled references. The numerical checks inspect finite circuits and algebraic identities. General complexity guarantees follow from the analytical proofs and their cited dependencies; the suite does not compile a complete QSVT instance or numerically optimize a diamond norm.

## Operational scope

The sources are pure, stationary and independently sampled. The quantity is a specified discrete geometric phase. Mixed-state targets, a continuum Berry-phase limit and source-noise robustness require additional analysis.

The receiver can coherently address the supplied state registers and perform controlled swaps. This is stronger than passive optical access to inaccessible internal photon states. Producing the quantum data remains a source cost; applying the theorem to a classical input also requires accounting for preparation.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The repository retains its [MIT license](LICENSE).
