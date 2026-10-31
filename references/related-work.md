# Related work and attribution

This project studies the number of independently supplied pure-state copies required to estimate one specified discrete geometric phase. The promise concerns adjacent overlap amplitudes, and the receiver may coherently process the supplied registers. The [model](../science/model.md) makes those assumptions precise. The distinction between estimating a complex invariant to additive error and estimating its argument is central to the comparisons below.

The result established here combines a coherent loop construction with a matching finite discrimination lower bound. For $`L\ge4`$ and $`0\lt \epsilon\le\pi/16`$, the upper copy cost is

```math
O\!\left(\frac{L^2}{c^2\epsilon^2}\log^2\frac{L}{\epsilon}\right).
```

The lower bound has order $`L^2/(c^2\epsilon^2)`$ for $`d\ge L`$ and $`0\lt c\le1/4`$. It allows arbitrary collective processing and adaptive classical choices of source label. The local transport, polynomial transformation, phase estimation and conversion from reflection queries to copies are established ingredients; the claim is a resource law for this particular statistical task.

Bibliographic records are in [references.bib](references.bib). The account below identifies the versions used for the closest comparisons. It does not assert that every possible algorithm in the broader geometric-phase literature has been excluded.

## 1. Established ingredients used by the algorithm

| Ingredient | Primary source and relevant statement | Role in this project |
|---|---|---|
| Canonical transport between nonorthogonal rays | Bravyi, DiVincenzo and Loss, [Sec. 2.1, Definition 2.1 and Lemma 2.1](https://arxiv.org/html/1105.0675v1) | Their direct rotation is the principal square root of a product of reflections. The [transport proof](../science/transport.md) relates it to the sign of $`P+Q-I`$ and fixes the orientation of the accumulated phase. Canonical ray transport is not a new primitive. |
| Polar-factor implementation | Lloyd et al., [quantum polar decomposition](https://arxiv.org/abs/2006.00841v1); Quek and Rebentrost, [Corollary 1, Eqs. (7)–(8)](https://arxiv.org/html/2106.07634v1) | Polar decomposition removes the attenuation of an overlap. Quek and Rebentrost give the clean-ancilla isometry guarantee used to compile a transport, with inverse singular-value dependence and logarithmic precision dependence. |
| Quantum singular value transformation | Gilyén, Su, Low and Wiebe, [STOC 2019 / arXiv:1806.01838](https://arxiv.org/abs/1806.01838) | Bounded polynomial transformation implements the gapped sign function. Here the gap is at least $`c`$, so the transport degree is $`O(c^{-1}\log(L/\epsilon))`$. |
| Simulation from state copies | Lloyd, Mohseni and Rebentrost, [density-matrix exponentiation](https://doi.org/10.1038/nphys3029); Kimmel et al., [optimal sample complexity for Hamiltonian simulation](https://doi.org/10.1038/s41534-017-0013-7) | Fresh program copies and controlled partial swaps implement a reflection with a fixed phase relative to the control. The [resource proof](../science/resources.md) gives a direct error bound that includes off-diagonal control coherence. |
| Multiple-source query-to-copy conversion | Wang and Zhang, [Definition 12 and Theorem 13](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.154/LIPIcs.ICALP.2026.154.html) | Their multisource samplizer gives total sample cost $`O(Q^2/\delta)`$ for $`Q`$ controlled-reflection queries and simulation error $`\delta`$. This is the established conversion underlying the upper bound's quadratic dependence. |
| Finite-precision phase compilation | Haah, [product decomposition for quantum signal processing](https://quantum-journal.org/papers/q-2019-10-07-190/) | A constructive classical procedure supplies the signal-processing phases. The [resource account](../science/resources.md) charges this preprocessing separately from source copies and quantum gates. |

Fourier phase estimation and the two-state Helstrom discrimination formula are also standard. The [algorithm](../science/algorithm.md) supplies the particular Fourier tail bound and error allocation needed here; the [converse](../science/lower-bound.md) supplies the finite two-hypothesis calculation. Neither routine is claimed as a new method.

The samplizer's generic optimality theorem does not establish the present lower bound. A compiler lower bound limits simulation of arbitrary query algorithms; a task lower bound must also rule out procedures that avoid that compiler. The circulant Gram family and cyclic-covariance reduction in this repository address the latter question directly.

## 2. Relational invariants and Gram reconstruction

**Oszmaniec, Brod and Galvão, arXiv:2109.10006v1.** Their [relational-information paper](https://arxiv.org/pdf/2109.10006v1) characterizes pure-state tuples using Bargmann invariants. Theorem 1 gives a complete set with degrees up to the number of states. A spanning-tree gauge makes selected overlaps positive, and remaining edge phases are recovered from corresponding cycle invariants. Figure 1 gives the direct cycle test.

This establishes both the invariant language and a reconstruction route. On a sparse ring, the phase-carrying fundamental cycle can have length $`L`$ and magnitude $`c^L`$. Estimating its raw real and imaginary parts therefore does not directly give a phase guarantee whose sample cost is polynomial under the adjacent-only promise. This conclusion is the conditioning calculation in [examples](../science/examples.md), rather than a claim that their completeness theorem is incorrect.

**Kotowski et al., arXiv:2610.06736v1.** [Gram-matrix tomography for photonic partial distinguishability](https://arxiv.org/pdf/2610.06736v1), submitted 5 October 2026, is a particularly close comparison. It reconstructs relational information with explicit sampling and prediction guarantees. Its polynomial regimes require control of the relevant cycle magnitudes; the dependence on these magnitudes appears in Theorem 1, Proposition 2 and Appendix B. Good pairwise overlaps can permit reconstruction through triangles, which is a stronger condition than nonzero adjacent overlaps alone.

Section V and Figure 6 discuss a sparse ring with neighboring overlap amplitude $`1/2`$ and zero non-neighbor overlaps. They explicitly identify the exponentially weak full-cycle signal as an obstacle to that protocol. The present ring family has the same overlap-graph obstruction, with $`c\le1/4`$ chosen to keep its Gram matrix uniformly positive. The receiver here can perform controlled swaps on the state registers. The photonic protocol instead addresses internal states inaccessible to direct control through spatial interferometry and photon counting. The present algorithm is consequently not a solution within that restricted optical interface.

## 3. Direct multivariate-trace and discrete-phase measurements

**Quek, Kaur and Wilde, Quantum 8, 1220 (2024).** Their [constant-depth multivariate-trace estimator](https://quantum-journal.org/papers/q-2024-01-10-1220/) reduces quantum circuit depth for estimating $`\mathrm{Tr}(\rho_1\cdots\rho_L)`$. Reduced circuit depth and precision of the argument are different resource questions. If the raw complex expectation has magnitude $`r`$, extracting its phase to error $`\epsilon`$ by estimating its quadratures requires absolute precision of order $`r\epsilon`$. The [direct-cycle comparison](../science/examples.md) gives this calculation and separately counts repetitions and consumed copies.

**Simonov, Wagner and Galvão, Physical Review A 112, 062435 (2025).** Their [multivariate-trace estimator with partial classical information](https://journals.aps.org/pra/pdf/10.1103/mrpz-xq28) uses known classical descriptions of some input states to reduce quantum registers and controlled-swap resources. It also discusses geometric-phase applications and sparse overlap patterns. Our input supplies every state as an unknown quantum source. The present theorem concerns phase precision under that source model, whereas their resource reductions concern raw-trace estimation with additional classical information.

**The 2023 Bhowmick–Liu–Sengupta–Tan preprint and the 2025 Tan et al. article.** The inspected [author preprint, version 1](https://www.researchgate.net/publication/371272465_Probing_quantum_phase_transitions_via_short_depth_quantum_circuits_for_estimating_quantum_coherence_and_discrete_Berry_phases), DOI 10.21203/rs.3.rs-2922743/v1, defines a discrete phase through a cyclic overlap product in Eq. (8). Equations (11)–(13) express the product through a cyclic permutation, with the conjugation depending on orientation, and Eqs. (17)–(19) give ancilla quadrature readout. This is a direct raw-cycle route; its circuit-depth improvement does not itself normalize exponentially small visibility.

The corresponding [published article](https://journals.aps.org/prb/abstract/10.1103/gydb-9jt2) is Physical Review B 112, 014108 (2025), with author list Kok Chuan Tan, Deren Liu, Kishor Bharti, Dhiman Bhowmick and Pinaki Sengupta. Its final metadata and abstract were checked, but the final full text was not accessible in this review. The equation-level comparison above therefore applies to the inspected 2023 preprint; it must not be read as a verification that the final article has identical equations or assumptions. Both versions have separate bibliography entries.

## 4. Adaptive relational learning

**Jastrzebski, Yu, Patel and Kyriienko, arXiv:2609.17352v1.** The full text of [Adaptive Relational Learning on Multi-instance Quantum Data with Photonic Processors](https://arxiv.org/pdf/2609.17352v1), submitted 15 September 2026, was inspected. Section II, Eqs. (1) and (3), measures a cycle expectation after local trainable transformations; Eq. (7) relates an invariant's argument to a geometric phase with that paper's sign convention. The work includes geometric-phase classification examples.

The precision in Section IV, Eq. (25), is additive precision of a raw observable estimated by the cycle test, giving $`O(\log(1/\delta)/\varepsilon^2)`$ measurements for that observable. It is not a general guarantee of circular phase error $`\varepsilon`$ for an arbitrary original loop whose invariant is exponentially small. Training local transformations and performing a learned classification task also differ from estimating the specified original invariant under only an adjacent-overlap promise. This comparison does not exclude the usefulness of learned transformations; it identifies which guarantee Eq. (25) actually supplies.

## 5. Hamiltonian access and emulation of unknown operations

**Hamiltonian-based Berry-phase algorithms.** Hayakawa, Sakamoto and Kiumi's [arXiv:2509.13423v3](https://arxiv.org/pdf/2509.13423v3), revised 4 August 2026, treats Berry-phase estimation for Hamiltonian paths, with algorithmic and complexity results under specified access and guiding-state assumptions. Kiumi's [arXiv:2604.20952v3](https://arxiv.org/pdf/2604.20952v3), revised 16 September 2026, controls adiabatic error in Berry-phase estimation using structured evolutions and cancellation. These works receive dynamical information that is absent from a collection of independent unknown snapshots. Conversely, this repository estimates a specified discrete phase and does not prove an adiabatic approximation or a continuum limit. Their Hamiltonian costs and our copy costs cannot be identified without an additional reduction.

**Marvian and Lloyd, PRX Quantum 6, 030346 (2025).** Their [universal quantum emulator](https://doi.org/10.1103/PRXQuantum.6.030346) already demonstrates dimension-independent sample access to transformations specified through quantum examples. It is relevant prior work on coherent processing of quantum data, including controlled reflections and possible use within larger algorithms.

The final published [open full text](https://www.researchgate.net/publication/395491319_Efficient_Quantum_Emulation_of_Unknown_Unitaries), Section IV, subsection 2, explicitly distinguishes ordinary emulation from controlled emulation. Independent input-output density operators determine an unknown unitary only up to global phase; a controlled version requires additional resources that fix that phase. Their example supplies coherent control input-output samples. Our input supplies no such pairs. Instead, the controlled transport is specified by an explicit projector formula and implemented through known controlled gates. The emulator is therefore an important precursor, but its uncontrolled input-output guarantee cannot simply be substituted for the phase-referenced loop construction.

## 6. Scope of the comparison

The exponential benchmark in this repository is the specified full-cycle measurement that retains its noisy ancilla outcome and consumes a fresh complete tuple on each repetition. The finite lower bound for that benchmark appears alongside the matching direct estimator in [examples](../science/examples.md). It is not a lower bound for all separate-copy measurements, all classical data analysis, or all photonic protocols.

The general converse is instead polynomial and applies to every protocol in the stated independent-source model. It is this converse, together with the explicit upper construction and full resource accounting, that supports the near-optimal copy claim. Further improvements could remove logarithms, improve finite constants or preprocessing, or exploit additional overlap structure without contradicting either theorem.

### Version and access record

This account was checked against the cited sources on 31 October 2026. Comparisons to the 2026 Gram-tomography and adaptive-learning papers use their version-1 full texts. The Hamiltonian comparisons use the explicit version-3 texts linked above. The universal-emulator comparison uses its final published text. The discrete-phase circuit comparison preserves the separate 2023-preprint and 2025-final-metadata limitation described above.
