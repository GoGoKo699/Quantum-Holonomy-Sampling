# Learning phase estimation and coherent runs

Several labeled sources supply independent specimens of their fixed unknown pure states. A receiver wants the geometric phase around their specified loop. Coherent transport estimates it with nearly optimal total copies. The shared question with [Quantum-Fidelity-Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence) asks how many copies the receiver must process before completely resetting its unknown quantum information.

The distinction is operational. A processor can stream many specimens through a small target register while remaining in one long coherent run. A complete reset instead leaves only classical history. That notebook is unlimited and may guide every later operation; the lower bound must account for what it learns about fixed source states.

## One anchor and thirty targets

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the [author-hosted 2018 manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). The [Watrous bridge](WATROUS_BRIDGE.md) selects relevant sections, translates conventions, and supplies the connections from those foundations to the project's actual proofs. It includes a complete qubit loop showing transport and readout, followed by a sparse four-state experiment showing optimal block information and the dimension-qualified coherence theorem.

The [thirty-milestone map](MILESTONES.md) has **12 background/preliminaries targets** and **18 narrative/innovation targets**. This allocation follows the science: the background connects states, operations, inference, symmetry, and reset rules; the narrative joins the coherent algorithm to the phase-specific adaptive converse. The map is common scientific learning material, independent of any reader's assessment history.

| Milestones | Organizing question | Scientific connection |
|---|---|---|
| M01–M06 | What are the states, relations, and permitted operations? | Rays, Gram matrices, controlled interference, and spectral transformations. |
| M07–M12 | What constitutes the complete statistical experiment? | Error composition, finite testing, symmetry, complete resets, and the two resource questions. |
| M13–M18 | How does the coherent algorithm meet the general copy scale? | Transport, readout, sample simulation, the unrestricted converse, and the direct-cycle benchmark. |
| M19–M24 | What can an optimal short block reveal about phase? | Orbit Gram representation, exact four-copy information, and the uniform winding/Jensen estimate. |
| M25–M28 | Why does the block bound constrain fixed adaptive sources? | Stock padding, fixed-versus-refreshed likelihood comparison, transcript information, and the endpoint. |
| M29–M30 | Where does the result apply, and how do the sister methods connect? | Fixed-dimensional tomography, accurate attribution, operational boundaries, and synthesis. |

Watrous supplies states, channels, measurements, distinguishability, information, permutation symmetry, and Haar averaging. The projector transport, Fourier circuit, polar compilation, sample simulator, and phase-specific transcript argument are developed in the project. Primary research citations remain necessary for inherited ingredients; they are not additional educational anchors.

## Start with a complete example

[Bridge §4](WATROUS_BRIDGE.md#4-a-complete-four-state-loop) gives four labeled qubit rays, every adjacent overlap, the product $`B=(1+i)/4`$, the transport matrices, and the Fourier outcome recovering $`\Phi=\pi/4`$. It makes the orientation, coherent control, specimens, and output explicit. This small example illustrates the algorithm rather than the worst-case converse.

[Bridge §9](WATROUS_BRIDGE.md#9-a-sparse-four-state-experiment-with-an-optimal-block-measurement) then uses a sparse four-dimensional cycle with $`B=c^4e^{i\phi}`$. One specimen per label has optimal invariant information $`2c^8[1+O(c^4)]`$. The [canonical block account](../science/block-information.md) specifies its exact optimal spectral measurement and finite divergence. This establishes a measurement-independent block limitation rather than inferring one from raw visibility alone.

## Follow the constructive route

The [transport](../science/transport.md) retains each local overlap phase while removing attenuation. The [algorithm](../science/algorithm.md) closes the loop, reads its eigenphase, and allocates finite errors. The [resources](../science/resources.md) replace reflection queries with consumed specimen programs and charge gates, live memory, and classical compilation separately.

The [unrestricted lower bound](../science/lower-bound.md) uses a physical sparse Gram family and finite discrimination. For general loop length, it matches the upper theorem's powers up to logarithms in the stated regime. At four states and fixed small accuracy the upper budget is $`O(c^{-2})`$ copies, with no overlap logarithm in the copy count.

## Follow the complete-reset converse

The new [coherent-run account](../science/coherent-runs.md) first proves a stock-information bound uniform in growing run length. Fixed-type compression and scalar Jensen keep its inverse Gram matrix under control at the useful scale $`tc^2`$. Counting the first possible phase winding yields the phase-specific divergence.

Actual sources stay fixed, so independently refreshing their orientation after every run would change the experiment. Four-source stock padding simulates adaptive labels and stopping. A transferred homogeneous-polynomial likelihood comparison bounds the difference between the actual fixed-source transcript and an auxiliary refreshed transcript. The classical chain rule then joins all retained outcomes without restricting the notebook.

At fixed small phase accuracy, $`N\le C_0c^{-2}`$ and the sufficient dimension condition $`d\ge9216C_0^2c^{-4}`$ force runs of order $`c^{-2}`$ consumed copies. The coherent algorithm supplies matching sufficient order. This is a threshold at the copy-optimal endpoint; a full matching law for every dimension and every run budget is not asserted.

## Read the boundary with the theorem

At fixed finite dimension, separate-copy tomography reaches $`O_d(c^{-2}\epsilon^{-2})`$ copies and permits $`b=1`$. The dimension condition is therefore part of the operational conclusion. Consumed copies per complete reset also remain distinct from simultaneous quantum width, circuit depth, and elapsed time.

The sister's root-fidelity theorem concerns a different target. Its reset model and fixed-source comparison method transfer after their assumptions are checked; its numerical fidelity tradeoff is not substituted for a phase theorem. [Related work](../references/related-work.md) credits replica hierarchies, cycle tests, collective overlap measurements, polar compilation, and sample simulation. The [verification guide](../verification/README.md) separates finite algebraic/circuit checks from the analytical universal proofs.

Direct routes: [milestone map](MILESTONES.md), [Watrous bridge](WATROUS_BRIDGE.md), [scientific overview](../science/README.md), and [reproduction](../verification/README.md).
