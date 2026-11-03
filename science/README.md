# Scientific account

The central question is how many independent copies of unknown quantum states are needed to learn the geometric phase around a discrete loop. The [model and main theorem](model.md) give the complete input, error and resource conventions.

| Topic | Account |
|---|---|
| Exact target, source promises and near-optimal copy law | [Model](model.md) |
| Canonical transport and its phase convention | [Transport](transport.md) |
| Controlled loop construction and accumulated error | [Algorithm](algorithm.md) |
| Consumed copies, gates, memory and classical preprocessing | [Resources](resources.md) |
| Finite lower bound against collective and adaptive protocols | [Lower bound](lower-bound.md) |
| Exact four-copy information and a uniform growing-stock bound | [Block information](block-information.md) |
| Complete-reset model, adaptive transcript comparison and necessary run length | [Coherent runs](coherent-runs.md) |
| Sparse rings and the direct-cycle benchmark | [Examples](examples.md) |
| Meaning of visibility, local conditioning and operational access | [Interpretation](interpretation.md) |
| Imported results and the closest competing models | [Related work](../references/related-work.md) |
| Reproducible finite checks and their limits | [Verification](../verification/README.md) |

For a proof-first route, read model → transport → algorithm → resources → lower bound. For the operational consequence, read model → examples → interpretation, returning to the proofs for the exact assumptions. The verification checks signs, coherent phases and finite instances; the general asymptotic guarantees are analytical.

For the coherence question, continue from the sparse-ring example to block information and coherent runs. [Quantum Fidelity Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence) owns the general fixed-source transcript method; this repository owns the phase-specific block theorem and its application. The fixed-dimension tomography exception is part of the coherent-run statement.

For a guided route through the prerequisites and the complete argument, use the [30-milestone map](../learning/MILESTONES.md) alongside the [Watrous bridge](../learning/WATROUS_BRIDGE.md). The [learning overview](../learning/README.md) distinguishes those study routes from the direct proof route.
