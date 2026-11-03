# Thirty milestones for phase estimation and coherent runs

The project asks how many copies of unknown pure states are needed to estimate the phase around a specified loop, then asks whether the best copy order can survive frequent complete quantum resets. The constructive transport algorithm, unrestricted copy converse, optimal four-copy information, and fixed-source adaptive transcript argument form one connected story.

The map contains exactly **30 project-defined understanding targets**. **Background/preliminaries has 12 milestones, M01–M12**: individual rays and operations become a complete statistical experiment with symmetry, a total-copy cap, and a precise reset boundary. **Narrative/innovation has 18 milestones, M13–M30**: local transport builds the upper endpoint, while phase-specific block information and the adaptive comparison establish its necessary coherent-run size. Each phase proceeds from local objects to a global account. The allocation gives both the algorithm and the information argument room without turning specialist lemmas into separate milestones.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the [author-hosted 2018 manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). All section numbers below refer to this source. The [Watrous bridge](WATROUS_BRIDGE.md) supplies notation translations, missing algorithmic explanations, two complete four-state examples, and the route to the phase/coherence theorem. Primary research papers remain attribution and proof dependencies, not extra educational anchors. Watrous supplies information-theoretic foundations; the particular transport and transcript theorems are supplied by the linked scientific accounts.

Dependencies refer to earlier targets. They are conceptual requirements, not a reader's assessment record. The map does not claim to cover every technical lemma or neighboring topic.

## Phase I — Background/preliminaries

### M01 — Rays and source density operators

**Central question:** What does a pure-state source specify when the phase of its vector is arbitrary?

**Understanding target:** Explain a normalized vector, its ray, and $`P=|\psi\rangle\langle\psi|`$. Rephasing a vector leaves the source unchanged, but relationships between several projectors can retain observable phase information.

**Dependencies and story role:** None. This establishes the local physical object used by the algorithm and the statistical hard family.

**Conceptual connection:** The target must be a function of supplied density operators, rather than the unobservable global phase of one vector.

**Sources:** Watrous §§2.1.1–2.1.3. [Model §§1–2](../science/model.md#1-independent-labeled-sources); [bridge §1](WATROUS_BRIDGE.md#1-the-task-before-the-circuit).

### M02 — Supplied specimens and classical source labels

**Central question:** Which computational access is provided by an independent quantum copy?

**Understanding target:** Distinguish copies from a classical state description, preparation circuit, inverse preparation, conjugated specimen, and coherent source-index oracle. Explain how known gates act jointly on supplied registers while their acquisition labels remain classical.

**Dependencies and story role:** M01. It turns a state into a charged input interface and identifies what later protocols must simulate.

**Conceptual connection:** Controlled processing of register contents does not supply controlled state preparation. Every fresh target or program specimen counts toward the deterministic cap.

**Sources:** Watrous §§2.1, 2.2. [Model §§1 and 3](../science/model.md#1-independent-labeled-sources); [algorithm access model](../science/algorithm.md#access-model-and-target).

### M03 — Complex overlaps and physical Gram matrices

**Central question:** When can prescribed local overlaps describe a physical collection of states?

**Understanding target:** Distinguish overlap amplitude, its magnitude, and squared fidelity. Explain how a positive semidefinite Gram matrix with unit diagonal produces normalized source vectors and why pairwise magnitudes omit phase information.

**Dependencies and story role:** M01–M02. Local relations become matrix data that can specify an entire sparse family.

**Conceptual connection:** The promise is amplitude at least $`c`$, so squared fidelity is at least $`c^2`$. Gram positivity must hold before a formal phase pattern becomes a legal lower-bound input.

**Sources:** Watrous §§1.1.3, 3.2.1. [Model §1](../science/model.md#1-independent-labeled-sources); [lower bound §1](../science/lower-bound.md#1-a-normalized-family-of-sources).

### M04 — Channels, discarded programs, and coherent references

**Central question:** What remains of an operation after an auxiliary specimen is discarded?

**Understanding target:** Connect unitary evolution on a larger system to a channel on retained registers. Explain why an approximation must preserve correlations with controls and arbitrary references, including off-diagonal control blocks.

**Dependencies and story role:** M01–M03. It extends the local description from state vectors to the operations required for sample-based simulation.

**Conceptual connection:** A program can be consumed while an unknown target remains coherent. Correct output rays on isolated inputs do not alone imply the correct controlled channel.

**Sources:** Watrous §§2.2.1–2.2.3, 3.3.1–3.3.3. [Controlled density-matrix exponentiation](../science/resources.md#controlled-density-matrix-exponentiation); [diamond bound](../science/resources.md#diamond-norm-bound).

### M05 — Measurable relative phase and cycle interference

**Central question:** How does a cyclic product become an observable interference signal?

**Understanding target:** Explain how controlling a permutation turns its expectation into a control-qubit bias. Connect real and imaginary readout to the gauge-invariant product $`B`$, and distinguish an isolated state-vector phase from a controlled operation's relative phase.

**Dependencies and story role:** M01, M03–M04. Local phase conventions become a complete measurable quantity.

**Conceptual connection:** A scalar phase that is irrelevant to an uncontrolled channel matters after coherent control. The orientation of the permutation fixes which sign of the imaginary part is measured.

**Sources:** Watrous §§2.2–2.3 for channels and measurement; the interference derivation is local. [Examples §2](../science/examples.md#2-what-one-direct-cycle-test-shot-measures); [bridge §§3–4](WATROUS_BRIDGE.md#3-conventions-that-matter).

### M06 — Reflections, spectral sign, and matrix blocks

**Central question:** How can projectors specify a reversible transport despite a small overlap?

**Understanding target:** Relate $`R_P=I-2P`$ to projector eigenvalues; explain spectral sign, polar factor, and a selected matrix block of a larger unitary. Distinguish normalization-relative singular-value gap from an intrinsic condition number.

**Dependencies and story role:** M03–M05. It supplies the operator language that will remove local attenuation coherently.

**Conceptual connection:** The local sign gap is at least $`c`$ under normalization one. It is not an assumed eigenphase gap of the eventual loop.

**Sources:** Watrous §1.1.3 and §2.2. The particular block-encoding compiler is a primary research dependency. [Transport §§1–2 and 4–5](../science/transport.md#1-a-projector-defined-transport); [bridge §5](WATROUS_BRIDGE.md#5-from-the-loop-to-a-copy-budget).

### M07 — Errors that compose through a computation

**Central question:** Which notion of closeness controls the final classical experiment?

**Understanding target:** Distinguish vector, operator, trace-distance, and unhalved diamond error. Explain telescoping composition, and why a clean-input guarantee can be applied on ideal clean prefixes without assuming that actual workspace stays perfectly clean.

**Dependencies and story role:** M04–M06. Approximate local operations become usable components of a reliable global algorithm.

**Conceptual connection:** Polar leakage and discarded-program error have different mathematical forms, but both must ultimately bound changes in final outcome probabilities.

**Sources:** Watrous §§1.1.3, 3.2–3.3. [Transport clean lift and workspace reuse](../science/transport.md#5-the-inherited-polar-compiler-and-its-clean-ancilla-guarantee); [algorithm §4](../science/algorithm.md#4-finite-gate-errors-and-the-final-success-bound).

### M08 — An eigenphase and a finite Fourier output

**Central question:** How can coherent evolution reveal an angle at a charged finite cost?

**Understanding target:** Connect a unitary eigenvalue, controlled powers, finite Fourier interference, and its measured integer. Distinguish radians from a fraction of a turn, phase-qubit count from expanded unitary calls, and circular accuracy from ordinary real-line error.

**Dependencies and story role:** M02, M05–M07. It supplies the readout mechanism before the project builds the required loop eigenvalue.

**Conceptual connection:** Fine resolution comes from actual repeated coherent applications. The exact pair $`(y,F)`$ describes an output angle without numerical rounding ambiguity.

**Sources:** Watrous §§2.1–2.3 supply state/measurement foundations; the Fourier circuit is explained locally. [Algorithm §1](../science/algorithm.md#1-an-ideal-phase-estimation-circuit); [bridge §§3–4](WATROUS_BRIDGE.md#3-conventions-that-matter).

### M09 — Estimation, finite testing, and information

**Central question:** How can two source tuples constrain every estimator?

**Understanding target:** Connect disjoint accuracy regions to binary discrimination, trace distance to optimal success, and relative entropy to classical data processing. Distinguish a finite testing bound from asymptotic Fisher information or a lower bound for one chosen measurement.

**Dependencies and story role:** M02–M04, M07. It supplies the statistical language common to both lower-bound branches.

**Conceptual connection:** A task lower bound must include receivers that avoid the proposed transport or any particular cycle readout. Information bounds must concern the actual experiment whose outputs are retained.

**Sources:** Watrous §§3.1.1, 3.2, 5.1–5.2. [Lower bound §§4–5](../science/lower-bound.md#4-phase-estimation-implies-binary-discrimination); [block information](../science/block-information.md).

### M10 — Permutations, common orientation, and Haar averaging

**Central question:** What remains measurable when the joint orientation of the sources is unknown?

**Understanding target:** Explain invariant measurements and common-unitary averaging. Connect tensor-position permutations, Schur sectors, and orbit Gram matrices; recognize why known maximally mixed factors do not change distinguishability and why transposition is not generally a physical channel on extensions.

**Dependencies and story role:** M03–M04, M09. It builds the symmetry framework used to optimize a block measurement.

**Conceptual connection:** A common Haar rotation preserves the promised Gram matrix. Independent rotations of the four labels would destroy that relation; independent rotations between runs would change the stationary-source experiment.

**Sources:** Watrous §§7.1–7.2, 3.1–3.2. [Block-information representation argument](../science/block-information.md); [bridge §9](WATROUS_BRIDGE.md#9-a-sparse-four-state-experiment-with-an-optimal-block-measurement).

### M11 — Complete resets and a classical adaptive notebook

**Central question:** What information may survive a boundary between coherent runs?

**Understanding target:** State the conditional complete-reset rule for all retained quantum registers jointly. Explain arbitrary classical histories and feedback, consumed-copy run cap $`b`$, total worst-case cap $`N`$, and why a target carried through streamed acquisitions is still inside one run.

**Dependencies and story role:** M02, M04, M09–M10. It assembles the operational restriction needed for a meaningful adaptive converse.

**Conceptual connection:** Consumed copies before reset are neither simultaneous storage width, elementary-gate count, circuit depth, nor physical elapsed time. A marginally unknown-free register can still carry prohibited conditional correlations.

**Sources:** Watrous §§2.1–2.3 for registers, conditioning, and instruments. [Coherent-run model](../science/coherent-runs.md); [bridge §8](WATROUS_BRIDGE.md#8-what-survives-a-complete-reset).

### M12 — The two resource questions in one model

**Central question:** What does copy-optimal phase estimation mean, and which extra question does the run constraint ask?

**Understanding target:** Assemble pure stationary sources, adjacent amplitude promise, forward loop phase, circular error, constant success, total consumed copies, and complete resets. Explain the general-$`L`$ copy theorem and the additional fixed-$`L=4`$, fixed-accuracy, weak-overlap endpoint question.

**Dependencies and story role:** M01–M11. This completes the background phase by joining objects, operations, symmetry, and statistical quantifiers.

**Conceptual connection:** A weak raw invariant motivates the question but does not optimize block information. Root fidelity is a different target; only a method with verified assumptions may transfer from the sister project.

**Sources:** Watrous Chapters 2–3, §§5.1–5.2, 7.1–7.2 as assembled above. [Model](../science/model.md); [coherent runs](../science/coherent-runs.md); [bridge §§1 and 8](WATROUS_BRIDGE.md#1-the-task-before-the-circuit).

## Phase II — Narrative/innovation

### M13 — Compiling the local phase-preserving transport

**Central question:** How does a pair of nonorthogonal projectors yield a usable controlled transport?

**Understanding target:** Derive the normalized-overlap action of $`\mathrm{sign}(P+Q-I)`$, relate it to the established direct rotation, and connect its two-reflection block encoding to the inherited polar compiler. Explain the block-error-to-clean-vector guarantee and inverse-$`c`$ query cost.

**Dependencies and story role:** M03, M05–M07, M12. The narrative starts with the local mechanism and its executable interface.

**Conceptual connection:** The transport depends only on projectors, keeps the overlap phase, and removes its magnitude. Fixed control phases and a coherent clean lift replace repeated postselection.

**Sources:** Watrous §§1.1.3, 2.2, 3.3. [Transport §§1–5](../science/transport.md), with primary direct-rotation/QSVT/polar citations; [bridge §§3 and 5](WATROUS_BRIDGE.md#3-conventions-that-matter).

### M14 — Closing the coherent loop

**Central question:** Why does sequential local transport produce the desired global phase?

**Understanding target:** Follow the ordered product $`W=T_L\cdots T_1`$ and show $`W|\psi_1\rangle=e^{-i\Phi}|\psi_1\rangle`$. Explain the minus sign, cancellation of vector gauges, and the clean-prefix hybrid permitting work-qubit reuse.

**Dependencies and story role:** M05, M07–M08, M13. It joins local transfers into the global object measured by the algorithm.

**Conceptual connection:** A supplied initial specimen already has the ideal eigenphase. No eigenstate-preparation routine, isolated eigenvalue, or Hamiltonian path is assumed. The full qubit loop makes orientation and output concrete.

**Sources:** Watrous §§2.1–2.2 and 3.3 for state evolution and error. [Transport §3 and workspace reuse](../science/transport.md#3-the-loop-and-its-orientation); [worked bridge §4](WATROUS_BRIDGE.md#4-a-complete-four-state-loop).

### M15 — Fourier readout and reflections from specimens

**Central question:** How does an ideal loop become a charged copy algorithm?

**Understanding target:** Connect the finite grid, $`q=F-1`$ expanded loops, $`M=Lq`$ transports, and $`Q=2KM`$ reflections. Explain how fresh controlled partial swaps approximate each fixed-phase reflection with unhalved diamond error at most $`4\pi^2/m`$, including inactive control branches.

**Dependencies and story role:** M04, M07–M08, M13–M14. It joins the readout circuit to the actual source interface.

**Conceptual connection:** Discarding program specimens does not supply inverse preparation or end the target's coherent run. The first-order channel calculation must include off-diagonal control coherence.

**Sources:** Watrous §§2.2–2.3, 3.3. [Algorithm §§1–3](../science/algorithm.md#1-an-ideal-phase-estimation-circuit); [resources controlled simulation](../science/resources.md#controlled-density-matrix-exponentiation); [bridge §5](WATROUS_BRIDGE.md#5-from-the-loop-to-a-copy-budget).

### M16 — A complete upper endpoint with separated resources

**Central question:** What is the actual cost and success probability of the construction?

**Understanding target:** Combine $`m=\lceil400\pi^2Q\rceil`$, $`N=1+Qm`$, and the separate polar, sample, and gate-error budgets. Explain the general copy bound and why fixed $`L=4`$, fixed accuracy gives $`O_\epsilon(c^{-2})`$ copies without an overlap logarithm.

**Dependencies and story role:** M07, M11, M13–M15. This integrates the constructive branch into a complete operational endpoint.

**Conceptual connection:** Streaming uses $`2\lceil\log_2d\rceil+O(\log(1/\epsilon))`$ live qubits, while one run may consume all $`N`$ copies. Quantum gates and classical phase compilation remain separately charged.

**Sources:** Watrous §§3.2–3.3 provide error language. [Algorithm §§2–4](../science/algorithm.md#2-compile-every-transport-coherently); [resources](../science/resources.md); [bridge §§5 and 8](WATROUS_BRIDGE.md#5-from-the-loop-to-a-copy-budget).

### M17 — The sparse physical family and unrestricted copy converse

**Central question:** Why can no collective receiver improve the general copy powers beyond the stated law?

**Understanding target:** Build the positive circulant Gram family, distribute phase over its edges, and use cyclic covariance to simulate adaptive source labels from source-one copies. Connect a finite source-vector difference to tensor-power trace distance and an accurate phase estimate to binary testing.

**Dependencies and story role:** M03, M07, M09, M12. It supplies an independent necessity argument alongside the completed algorithm.

**Conceptual connection:** The hard Gram matrix is uniformly well conditioned. Weak phase sensitivity of each specimen forces $`\Omega(L^2c^{-2}\epsilon^{-2})`$ copies without restricting the receiver to a reflection compiler.

**Sources:** Watrous §§1.1.3, 3.1.1–3.2. [Lower bound §§1–5 and scope](../science/lower-bound.md); [bridge §6](WATROUS_BRIDGE.md#6-why-the-lower-bound-is-a-different-argument).

### M18 — What raw-cycle visibility does establish

**Central question:** Why is a direct cyclic readout costly, and which receivers does that comparison cover?

**Understanding target:** Connect $`B=c^Le^{i\phi}`$, quadrature accuracy of order $`c^L\epsilon`$, and $`L`$ specimens per fresh shot. Explain the restricted readout's $`\Theta(Lc^{-2L}\epsilon^{-2})`$ copy count and why it is not a converse for arbitrary block measurements or classical histories.

**Dependencies and story role:** M05, M09, M16–M17. It makes the motivating benchmark precise before a stronger measurement-independent block analysis.

**Conceptual connection:** The sparse graph has no nonzero triangles that recover its phase. Cycle/Bargmann tests are established useful protocols; their visibility alone cannot prove long-run necessity.

**Sources:** Watrous §§2.3, 3.1, 5.1. [Examples §§1–4](../science/examples.md); [related work](../references/related-work.md); [bridge §7](WATROUS_BRIDGE.md#7-reading-the-unrestricted-result).

### M19 — The invariant stock and its orbit Gram matrix

**Central question:** How can every measurement of a common-orientation block be studied in a finite symmetry model?

**Understanding target:** Construct the tensor-word orbit Gram matrix for a fixed stock. Connect its Schur blocks to the physical common-Haar twirl, with parameter-independent representation factors and a simultaneous transpose. Explain equality of relative entropy and QFI without asserting unrestricted CPTP equivalence.

**Dependencies and story role:** M03, M09–M10, M17–M18. It begins the phase-specific information branch with a sufficient mathematical experiment.

**Conceptual connection:** The one-each stock has a $`24\times24`$ regular model. General multiplicities use distinct words of one exact type; the dimension restriction of the later transcript theorem is a separate requirement.

**Sources:** Watrous §§7.1–7.2, 3.1–3.2. [Block-information representation](../science/block-information.md); [coherent-run stock proof](../science/coherent-runs.md); [bridge §§9–10](WATROUS_BRIDGE.md#9-a-sparse-four-state-experiment-with-an-optimal-block-measurement).

### M20 — Optimal information in four consumed copies

**Central question:** How much phase information can the best four-copy block measurement extract?

**Understanding target:** Identify the identity, adjacent swaps, disjoint swap pairs, and oriented four-cycle terms of the orbit Gram matrix. Explain their common spectral measurement, its exact probabilities, and optimal QFI $`2c^8[1+O(c^4)]`$, including $`\mathcal F_4(0)=2c^8/(1-4c^4)`$.

**Dependencies and story role:** M05, M09–M10, M19. It replaces raw visibility intuition by an optimized measurement calculation.

**Conceptual connection:** Phase dependence first appears at fourth order, and distinguishability at eighth order. A known cycle spectral test already attains the leading coefficient; the exponent is not merely a weakness of one ancilla readout.

**Sources:** Watrous §§2.3, 7.1–7.2 for measurements/symmetry; the QFI calculation is local. [Exact spectrum and QFI](../science/block-information.md); [bridge §9](WATROUS_BRIDGE.md#9-a-sparse-four-state-experiment-with-an-optimal-block-measurement).

### M21 — Finite four-copy testing without asymptotic assumptions

**Central question:** How does local information become a finite bound on phase discrimination?

**Understanding target:** Use the commuting spectrum to compute relative entropy between separated phases and bound it by order $`c^8\sin^2((\phi-\theta)/2)`$. Distinguish finite binary testing from an unbiased-estimator Cramér–Rao statement and explain the scope of optimizing one adaptive four-copy run.

**Dependencies and story role:** M09–M11, M19–M20. It turns a differential diagnostic into a rigorous one-block comparison.

**Conceptual connection:** Independent invariant four-copy blocks need order $`c^{-8}`$ copies at fixed phase accuracy. A single fixed orientation across adaptive runs has additional correlations, which this calculation alone has not removed.

**Sources:** Watrous §§3.1.1, 5.1–5.2. [Finite block information and four-copy scope](../science/block-information.md); [bridge §9](WATROUS_BRIDGE.md#9-a-sparse-four-state-experiment-with-an-optimal-block-measurement).

### M22 — Growing stocks and the first phase-carrying winding

**Central question:** What survives the four-cycle mechanism when a run may consume many copies of each label?

**Understanding target:** Define exact multiplicities, distinct-word dimension $`t!/(\prod_jr_j!)`$, and the fixed-type compression of $`G_\phi^{\otimes t}`$. Explain balanced label flow, integer winding, and why a nonzero winding requires at least four changed sites.

**Dependencies and story role:** M03, M10–M11, M19–M21. It generalizes the local block mechanism to run lengths that may grow as overlap weakens.

**Conceptual connection:** The leading fixed-multiplicity expansion is informative but nonuniform. A threshold at $`b\asymp c^{-2}`$ needs bounds valid when the multiplicities themselves diverge.

**Sources:** Watrous §§1.1.3, 7.1–7.2. [Coherent runs: stock compression and phase difference](../science/coherent-runs.md); [bridge §10](WATROUS_BRIDGE.md#10-why-the-block-estimate-must-be-uniform-in-run-length).

### M23 — A fixed-type Jensen bound at the correct scale

**Central question:** Why does the stock remain controllable up to order $`c^{-2}`$ copies?

**Understanding target:** Explain why off-diagonal one-site terms leave a fixed-type subspace, leaving a quadratic diagonal contribution in $`\log G_\phi`$. Apply scalar spectral Jensen to obtain $`C_\phi\succeq e^{-2tc^2}I`$ and distinguish it from a claim of operator convexity of the exponential.

**Dependencies and story role:** M06, M19, M22. It gives the uniform eigenvalue control needed for large runs.

**Conceptual connection:** The naive $`(1-2c)^t`$ bound decays at scale $`tc`$ and would miss the endpoint. Exact label counts reveal the useful scale $`tc^2`$.

**Sources:** Watrous §§1.1.3, 1.2.1 for spectral calculus/convexity; the compression estimate is local. [Coherent-run uniform eigenvalue proof](../science/coherent-runs.md); [bridge §10](WATROUS_BRIDGE.md#10-why-the-block-estimate-must-be-uniform-in-run-length).

### M24 — Uniform phase-specific stock divergence

**Central question:** How does phase winding bound every measurement of a growing stock?

**Understanding target:** Combine the changed-site count, squared entry weights, and the minimum-eigenvalue estimate with the quantum relative-entropy/chi-square comparison. Explain the bound $`D(\omega_\phi\|\omega_\theta)\le(8/3)t^4c^8e^{4tc^2}`$ and its uniformity in multiplicities.

**Dependencies and story role:** M09, M19, M22–M23. It completes the crucial information input for the adaptive lower bound.

**Conceptual connection:** This is a phase theorem. Neither the raw-cycle bias nor the sister's root-fidelity divergence can be substituted for the winding and fixed-type calculation.

**Sources:** Watrous §§5.1–5.2, 7.1–7.2. [Coherent-run divergence proof](../science/coherent-runs.md); [bridge §10](WATROUS_BRIDGE.md#10-why-the-block-estimate-must-be-uniform-in-run-length).

### M25 — Fixed stocks simulate adaptive source requests

**Central question:** How can a block information bound handle unknown run lengths and measurement-dependent labels?

**Understanding target:** Group complete original runs into superblocks and simulate each with $`2\beta`$ specimens of every label, $`\beta=\min(b,N)`$. Explain $`8\beta`$ copies per stock, at most $`\lceil N/\beta\rceil`$ stocks, and at most $`16N`$ padded copies, including early termination.

**Dependencies and story role:** M02, M11, M24. It converts the operational protocol into fixed-size experiments without restricting its choices.

**Conceptual connection:** Inner resets are part of each stock's instrument; no unknown quantum resource crosses its boundary. The padded specimens are charged to the comparison, not hidden inside the original resource count.

**Sources:** Watrous §§2.2–2.3 for instruments and composition. [Coherent-run padding proof](../science/coherent-runs.md); [bridge §11](WATROUS_BRIDGE.md#11-from-stocks-to-the-actual-adaptive-transcript).

### M26 — Comparing fixed and refreshed orientations honestly

**Central question:** Why does an auxiliary refreshed calculation say anything about fixed physical sources?

**Understanding target:** Explain whole-leaf likelihoods under rank-one measurement refinement as homogeneous polynomials in one Haar unitary. Connect the inherited Haar/Gaussian norm and product comparison to $`\mathrm{TV}(P_\phi,Q_\phi)\le384N^2/d`$ for $`d\ge32N`$.

**Dependencies and story role:** M09–M11, M19, M25. It transfers the stock analysis while accounting for correlations learned in classical history.

**Conceptual connection:** Coefficients may depend on the specified history, but normalized quantum posteriors need not be polynomial. The common orientation is sampled once in the actual experiment; refreshing belongs only to the compared auxiliary model.

**Sources:** Watrous §§5.1–5.2, 7.2. [Coherent-run transcript transfer](../science/coherent-runs.md), with its pinned sister-method reference; [bridge §11](WATROUS_BRIDGE.md#11-from-stocks-to-the-actual-adaptive-transcript).

### M27 — The complete fixed-source adaptive testing bound

**Central question:** What limits the information in all the classical records together?

**Understanding target:** Apply data processing to each refreshed stock and the classical relative-entropy chain rule across history-dependent measurements. Combine Pinsker and two fixed/fresh comparisons into the phase-specific transcript bound, identifying the block-information term and dimension correction separately.

**Dependencies and story role:** M09, M11, M24–M26. It joins the local stock theorem and correlation comparison into a bound for every permitted protocol.

**Conceptual connection:** Arbitrary classical computation, within-run measurements, source allocation, and stopping remain allowed. Complete reset is load bearing because it makes the quantum experiments factor conditional on the classical transcript.

**Sources:** Watrous §§3.1, 5.1–5.2, 7.2. [Coherent-run transcript theorem](../science/coherent-runs.md); [bridge §11](WATROUS_BRIDGE.md#11-from-stocks-to-the-actual-adaptive-transcript).

### M28 — Necessary coherent runs at the copy-optimal endpoint

**Central question:** Which run size is required to retain $`O(c^{-2})`$ total copies?

**Understanding target:** Compare phases $`0`$ and $`4\epsilon`$, require transcript total variation at least $`1/3`$, and derive $`b\ge c^{-2}/(128C_0^{1/3})`$ from $`N\le C_0c^{-2}`$ and $`d\ge9216C_0^2c^{-4}`$. Join this necessity with the one-run upper algorithm.

**Dependencies and story role:** M12, M16–M17, M27. It integrates both proof branches into the sharp high-dimensional endpoint $`b=\Theta(c^{-2})`$ at fixed small accuracy.

**Conceptual connection:** Fixed $`b\ge4`$ instead gives a $`c^{-8}`$ regime when the dimension correction is small. Neither statement is a matched full tradeoff in all parameters or a theorem for vanishing phase accuracy.

**Sources:** Watrous §§3.1 and 5.1 for testing. [Coherent-run endpoint and scope](../science/coherent-runs.md); [algorithm upper bound](../science/algorithm.md#upper-bound); [bridge §12](WATROUS_BRIDGE.md#12-the-endpoint-and-its-dimension-boundary).

### M29 — Dimension, attribution, and the physical boundary

**Central question:** Which apparently similar claims does the theorem leave separate?

**Understanding target:** Explain fixed-dimensional single-copy tomography with $`O_d(c^{-2}\epsilon^{-2})`$ copies by stabilizing each adjacent overlap, showing why dimension-unqualified run necessity is false. Attribute cycle tests, replica hierarchies, polar compilation, sample simulation, and the sister's transcript method separately from the new phase-specific bound.

**Dependencies and story role:** M02–M03, M11–M12, M18–M28. It connects the established endpoint to its operational uses and limits.

**Conceptual connection:** Purity, stationary independent specimens, accessible controlled registers, a discrete loop, and complete conditional reset matter. Simultaneous width, passive optics, noisy sources, mixed states, a continuum Berry phase, and root fidelity require their own statements.

**Sources:** Watrous §§2.3, 3.1–3.2, 7.2. [Coherent-run fixed-d scope](../science/coherent-runs.md); [interpretation](../science/interpretation.md); [related work](../references/related-work.md); [bridge §12](WATROUS_BRIDGE.md#12-the-endpoint-and-its-dimension-boundary).

### M30 — One explanation of geometric phase and coherent access

**Central question:** Why does efficient phase access demand long coherent consumption in the stated regime?

**Understanding target:** Connect projector transport, charged compilation, loop readout, and unrestricted copy necessity to the optimal four-copy experiment, uniform winding/Jensen estimate, fixed-source transcript comparison, and dimension-qualified run endpoint. Explain the substantive sister relationship and each project's distinct target without duplicating the root-fidelity theorem as a phase claim.

**Dependencies and story role:** M12–M29. This completes the narrative by joining mechanism, resources, necessity, attribution, and scope into one account.

**Conceptual connection:** Coherence removes attenuation constructively, while short complete-reset runs discard quantum relations before they accumulate enough information. The classical notebook remains fully available; the theorem quantifies when it still cannot replace those relations.

**Sources:** Watrous Chapters 2–3, §§5.1–5.2, 7.1–7.2 as connected by the bridge. [Model](../science/model.md), [block information](../science/block-information.md), [coherent runs](../science/coherent-runs.md), [interpretation](../science/interpretation.md), and [Watrous bridge](WATROUS_BRIDGE.md).
