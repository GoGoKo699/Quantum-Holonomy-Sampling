# Learning Quantum Holonomy Sampling

A collection of sources repeatedly prepares unknown quantum states. Each source has a classical label, and a receiver can process the supplied quantum registers together. The question is how many copies the receiver must consume to learn the geometric phase around a specified loop of those sources.

The loop's phase is a relational property: changing the arbitrary phase used to write any one state vector leaves the target unchanged. A direct interference experiment reads a complex product of overlaps, whose magnitude can become very small as the loop grows. This project instead builds a coherent transport around the loop, reads its phase, and accounts for the copies needed to implement that transport. A separate family of statistically close sources proves the scale that every permitted procedure must pay.

## The single anchor

The educational anchor is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms***, using the **17 April 2025** version linked from the [author's page](https://www.cs.umd.edu/~amchilds/qa/) and available as the [author-hosted PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf).

The [Childs bridge](CHILDS_BRIDGE.md) selects the relevant material on circuits, error accumulation, phase estimation, interference, simulation and signal processing. It translates the source's conventions and explains the additional geometric and statistical steps supplied by this project. Primary research papers support the imported technical theorems and their attribution in the [related-work account](../references/related-work.md).

## Routes through the material

| Aim | Route | What it connects |
|---|---|---|
| Build a complete conceptual understanding | [M01–M30](MILESTONES.md), with the [bridge](CHILDS_BRIDGE.md) alongside | States and operations, the coherent construction, its complete resource budget, and the finite converse |
| See a small loop before following the proof | [The bridge's worked example](CHILDS_BRIDGE.md), then [model](../science/model.md) and [transport](../science/transport.md) | Gauge-independent phase, orientation of the transport, and what a Fourier readout estimates |
| Check the constructive algorithm | [Transport](../science/transport.md) → [algorithm](../science/algorithm.md) → [resources](../science/resources.md) | Exact ray transport, approximate controlled implementation, fresh program copies, and accumulated error |
| Understand why the copy scale is unavoidable | [Lower bound](../science/lower-bound.md), then [examples](../science/examples.md) | Positive Gram matrices, adaptive source selection, finite fidelity, and discrimination |
| Understand the result's operational meaning | [Interpretation](../science/interpretation.md) and [related work](../references/related-work.md) | Intrinsic statistical difficulty, direct-cycle visibility, and the role of the supplied access |
| Reproduce the finite evidence | [Verification guide](../verification/README.md) | Which identities and finite circuits are checked, and which general statements depend on the written proofs |

The map has **11 background/preliminaries milestones** and **19 narrative/innovation milestones**. The background phase progresses from individual states and copies to the full access, loss and resource model. The narrative phase progresses from adjacent-ray transport to a complete algorithm and then from one slowly varying source family to a general lower bound. Its final milestones combine the construction, converse, comparison and scope.

Each milestone has a central question, an understanding target, earlier dependencies, a conceptual connection and source pointers. The map is defined by the scientific story and gives a common understanding route for readers. Detailed calculations remain in their authoritative scientific files.

## Conventions that carry through every route

The target uses the forward ordered product of neighboring overlaps. The controlled transport loop has the opposite eigenphase, so the Fourier readout is negated. The overlap promise concerns an **amplitude**; its squared magnitude is a different quantity. A labeled source supplies independent state copies, while a unitary oracle supplies an operation. Converting the required reflections into operations built from copies is part of the resource proof.

The upper copy count is independent of Hilbert-space dimension. Gates and live memory still depend on the register size, and classical compilation is accounted for separately. The matching lower bound applies when the dimension is at least the loop length and the overlap floor is at most one quarter. The [model](../science/model.md) owns the precise parameter ranges and success guarantee.

The comparison with exponentially weak visibility concerns the specified direct-cycle experiment. The coherent construction requires control of the supplied registers. Pure-state sources, stationary independent sampling, and a specified discrete loop remain part of the result throughout the learning route.
