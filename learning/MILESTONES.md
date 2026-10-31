# Thirty milestones for quantum holonomy sampling

The project asks how many independently supplied copies of unknown pure states are needed to estimate the geometric phase of a specified discrete loop. Its scientific story has two complementary parts: a coherent algorithm that preserves local overlap phases without multiplying their attenuation, and a finite statistical argument that limits every protocol in the same copy model.

This map contains exactly thirty understanding targets. The targets follow the project's assumptions, mechanism, proof structure, and operational meaning. Specialist details remain in the linked scientific accounts; the map does not claim to cover every lemma or every neighboring subject.

## One anchor and the role of the sources

The single educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), the author PDF dated **17 April 2025**. All Childs section numbers below refer to that edition. The [Childs bridge](CHILDS_BRIDGE.md) translates its conventions and connects the selected sections to this project.

Childs supplies the circuit, interference, phase-estimation, error-composition, and polynomial-transformation foundations. The local scientific files supply the particular source model, phase-preserving transport, controlled sample simulation, and finite converse. Primary research citations in those files remain proof dependencies and attribution; they are not additional educational anchors. Where Childs provides only context, the source entry says so rather than attributing the project's theorem to the notes.

## Allocation and progression

**Background/preliminaries has eleven milestones, M01–M11.** They move from individual rays and supplied specimens to relations between states, coherent operations, approximation, and statistical inference. M11 combines those objects into the complete estimation problem. Eleven are needed because understanding a copy theorem requires both quantum-algorithm and quantum-information concepts; a circuit-only introduction would leave its access assumptions and converse unexplained.

**Narrative/innovation has nineteen milestones, M12–M30.** M12–M20 connect local transport to an executable algorithm and its complete resource budget. M21–M25 build the independent lower-bound argument from physical source states to a bound against adaptive collective protocols. M26–M30 connect those proofs to the direct-cycle benchmark, the near-optimal theorem, its intellectual context, and its limits. The extra space belongs to the project's two proof arguments and their connection, not to an extended survey of quantum algorithms. “Narrative/innovation” names the contribution-building phase; established primitives within it are explicitly credited.

Dependencies name earlier milestones needed for the stated target. Each phase progresses from local objects to a global explanation, and each ends with synthesis. The canonical conventions are those of [the model](../science/model.md): overlap **amplitude** is bounded below by $`c`$, the target is the argument of the forward cyclic product, total consumed copies are counted, and accuracy is circular.

## Phase I — Background/preliminaries

### M01 — Rays, projectors, and an unknown pure state

**Central question:** What physical information does a pure-state source specify when the phase of its state vector is arbitrary?

**Understanding target:** Distinguish a normalized vector, its ray, and the density operator $`P=|\psi\rangle\langle\psi|`$. Explain why rephasing a representative leaves the supplied state unchanged, while relations between several projectors can contain observable phase information.

**Dependencies and story role:** No earlier milestone. This establishes the individual object from which both the algorithm and the hard family are built.

**Conceptual connection:** The project must define its phase through source density operators; it cannot ask a receiver to measure the global phase of one unknown vector.

**Sources:** Childs §1.1 for state-vector notation. [Model §1](../science/model.md#1-independent-labeled-sources) and [§2](../science/model.md#2-target-and-error-convention) give the source and rephasing conventions.

### M02 — Copies, registers, and the supplied interface

**Central question:** Which operations follow from receiving a quantum specimen, and which require an additional access assumption?

**Understanding target:** Distinguish independent copies, a classical state description, a preparation unitary, its inverse, and a coherent source-index oracle. Explain how known gates can act jointly on supplied registers even though their unknown states cannot be prepared or queried through an assumed oracle.

**Dependencies and story role:** M01. It turns the abstract state into a computational input and fixes the resource that the theorem counts.

**Conceptual connection:** Classical source labels and coherent processing of register contents coexist. The algorithm's controlled operations do not imply coherent access to the label-selection interface.

**Sources:** Childs §§1.2 and 21.1–21.2 for circuits and query models. [Model §1](../science/model.md#1-independent-labeled-sources), [§3](../science/model.md#3-what-is-counted), and [Algorithm: access model](../science/algorithm.md#access-model-and-target) define the particular copy interface.

### M03 — Overlaps, squared fidelity, and physical Gram matrices

**Central question:** What can pairwise overlaps tell us, and when can a proposed set of overlaps describe actual states?

**Understanding target:** Distinguish the complex overlap, its magnitude, and its squared magnitude. Understand a Gram matrix as the collection of overlaps, with unit diagonal and positive semidefiniteness ensuring a realization by normalized vectors. Recognize that pairwise magnitudes omit phase information.

**Dependencies and story role:** M01–M02. This introduces local relations between inputs and the matrix language later used to construct an entire hard instance.

**Conceptual connection:** The promise is $`|\langle\psi_j|\psi_{j+1}\rangle|\ge c`$, not squared fidelity at least $`c`$. Gram positivity constrains which sparse phase patterns are physical.

**Sources:** Childs §15.3 for the SWAP test and squared-overlap information. [Model §1](../science/model.md#1-independent-labeled-sources) and [Lower bound §1, equations (1)–(6)](../science/lower-bound.md#1-a-normalized-family-of-sources) supply the amplitude convention and Gram realization.

### M04 — Measurements, discarded registers, and coherent references

**Central question:** How should an operation be described when its target is entangled with another register or an auxiliary specimen is discarded?

**Understanding target:** Connect unitary evolution of a larger system to a channel on retained registers. Distinguish a measurement outcome distribution from the complete output state, and understand why an approximation must preserve correlations with controls and reference registers used later in the computation.

**Dependencies and story role:** M01–M03. It extends the description from isolated pure vectors to the operational setting required for sample simulation and collective lower bounds.

**Conceptual connection:** A program copy can be consumed while the target remains coherent. Checking only the active and inactive control branches separately would miss their relative coherence.

**Sources:** Childs §§1.1–1.2 provide state and circuit vocabulary. The channel and reference-system treatment used here is supplied locally in [Resources: controlled density-matrix exponentiation](../science/resources.md#controlled-density-matrix-exponentiation) and [its diamond-norm bound](../science/resources.md#diamond-norm-bound).

### M05 — Controlled interference and a measurable operation phase

**Central question:** Why can an overall phase of an operation matter once that operation is coherently controlled?

**Understanding target:** Explain how a controlled unitary converts its action into interference on a control qubit, and how the Hadamard test accesses real and imaginary expectation values. Distinguish an unobservable phase of an isolated state vector from a relative phase between two controlled circuit branches.

**Dependencies and story role:** M01, M02, and M04. It establishes the phase reference needed by every later transport and simulation claim.

**Conceptual connection:** A transport correct only up to an unspecified scalar phase is insufficient for reading the loop phase. Known scalar phases in explicit circuits must be retained.

**Sources:** Childs §16.1. [Examples §2, equations (3)–(5)](../science/examples.md#2-what-one-direct-cycle-test-shot-measures) fixes the direct-readout orientation; [Transport §4](../science/transport.md#4-a-block-encoding-with-a-fixed-phase) explains the controlled block's scalar sign.

### M06 — Reflections, spectral functions, and normalization

**Central question:** How does a projector define a reversible operation, and what does applying a function to a Hermitian matrix mean?

**Understanding target:** Relate a projector's eigenvalues to the reflection $`R_P=I-2P=e^{-i\pi P}`$. Understand spectral sign and polar factors as operations on eigenvalues or singular values, and distinguish a spectral gap relative to a specified normalization from an intrinsic condition number.

**Dependencies and story role:** M01, M03, and M05. It supplies the local operator language for turning overlap geometry into a coherent transformation.

**Conceptual connection:** The compiler uses a sign gap relative to block normalization one. This is not a promised eigenphase gap of the eventual loop operator.

**Sources:** Childs §§27.1 and 29.3 for evolution and spectral transformations. [Transport §§1–2](../science/transport.md#1-a-projector-defined-transport) and [Resources, equation (5)](../science/resources.md#diamond-norm-bound) supply the exact reflection and transport conventions.

### M07 — Fourier phase estimation and the cost of powers

**Central question:** How can an eigenvalue become a classical angle estimate, and what determines its resolution?

**Understanding target:** Connect a unitary eigenphase, controlled powers, a finite Fourier grid, and the measured output. Distinguish angle in radians from phase divided by $`2\pi`$, and distinguish the number of phase qubits from the number of unitary calls needed to implement their controlled powers.

**Dependencies and story role:** M02, M05, and M06. It supplies the global readout primitive before the project constructs the appropriate loop eigenvalue.

**Conceptual connection:** Fine phase resolution comes from repeated coherent evolution. The powers are expanded and charged; they are not supplied at unit cost.

**Sources:** Childs §§4.1–4.3. [Algorithm §1, equations (4)–(7)](../science/algorithm.md#1-an-ideal-phase-estimation-circuit) and [the bridge's conventions](CHILDS_BRIDGE.md#3-conventions-that-matter) translate the notes to the project's phase and output.

### M08 — A matrix inside a unitary circuit

**Central question:** How can a circuit act on a matrix that is not itself unitary?

**Understanding target:** Explain a block encoding as a selected matrix block of a larger unitary, including its normalization. Connect a bounded polynomial of that block to a sequence of known phase rotations and block-encoding calls. Keep the selected-block guarantee distinct from the action of the entire circuit on its ancillas.

**Dependencies and story role:** M02, M04, and M06. It introduces the compiler interface that links spectral functions to executable circuits.

**Conceptual connection:** The project needs a near-unitary sign transform with a coherent clean-ancilla guarantee; the general polynomial viewpoint alone does not yet provide that stronger guarantee.

**Sources:** Childs §§29.1–29.3. [Transport §§4–5](../science/transport.md#4-a-block-encoding-with-a-fixed-phase) specifies the actual block encoding and separately credits the inherited research-level polar theorem.

### M09 — Approximation errors that compose

**Central question:** Which notion of closeness remains useful when an approximate operation is inserted into a long coherent computation?

**Understanding target:** Distinguish vector error, operator error, trace distance, and unhalved diamond error by what each controls. Understand the telescoping argument that adds local errors, including why a clean-input guarantee must be applied on ideal clean prefixes rather than assumed on arbitrary dirty workspace.

**Dependencies and story role:** M04–M08. It turns separate approximate primitives into ingredients of a reliable complete algorithm.

**Conceptual connection:** The polar circuit and the consumed-copy simulator require different guarantees. Their errors ultimately bound changes in the same final measurement probability.

**Sources:** Childs §2.1. [Transport §5, equations (10)–(11)](../science/transport.md#5-the-inherited-polar-compiler-and-its-clean-ancilla-guarantee), [Resources: diamond-norm bound](../science/resources.md#diamond-norm-bound), and [Algorithm §4](../science/algorithm.md#4-finite-gate-errors-and-the-final-success-bound) give the local extensions.

### M10 — Finite estimation, discrimination, and resource lower bounds

**Central question:** How can two difficult-to-distinguish inputs limit every estimator, including one using collective measurements?

**Understanding target:** Relate separated target values to a binary decision problem, trace distance to optimal decision success, and independent copies to tensor powers. Distinguish a lower bound for a restricted measurement strategy, a generic query simulator, and the actual estimation task under a total-copy cap.

**Dependencies and story role:** M02–M04 and M09. It introduces the statistical reasoning needed to assess necessity as well as algorithmic sufficiency.

**Conceptual connection:** The converse must constrain all allowed processing of the sources, including protocols that never implement the proposed transport circuit.

**Sources:** Childs §§21.1–21.2 provide resource-model context, not the copy converse. The finite discrimination identities and reduction are supplied in [Lower bound §§4–5, equations (15)–(20)](../science/lower-bound.md#4-phase-estimation-implies-binary-discrimination); [Related work §1](../references/related-work.md#1-established-ingredients-used-by-the-algorithm) distinguishes compiler and task lower bounds.

### M11 — The complete discrete-phase estimation problem

**Central question:** What precisely must a successful algorithm learn, from which inputs, at which cost?

**Understanding target:** Assemble the pure independent sources, known adjacent amplitude bound, gauge-invariant forward product, circular error, constant success probability, and worst-case total-copy count into one problem statement. Explain why a small raw invariant and a difficult phase-estimation task are related but not identical claims.

**Dependencies and story role:** M01–M10. This completes the background phase by connecting its objects, operations, error notions, and statistical objective.

**Conceptual connection:** The target is $`\Phi=\arg\prod_j\langle\psi_j|\psi_{j+1}\rangle`$. The central question is whether the exponentially small product magnitude is an unavoidable copy cost under the stated coherent access.

**Sources:** [Model §§1–3](../science/model.md#1-independent-labeled-sources) and [Interpretation: why the direct signal can be small](../science/interpretation.md#why-the-direct-signal-can-be-small). Childs §§4.3, 16.1, and 21.1 supply the readout and resource language assembled here; the particular statistical problem is defined locally.

## Phase II — Narrative/innovation

### M12 — Local transport that retains phase and removes attenuation

**Central question:** How can two nonorthogonal projectors specify a unitary transfer with the correct overlap phase?

**Understanding target:** Explain the action of $`Z=P+Q-I`$ on the two-ray span and its orthogonal complement, then connect its spectral sign to the normalized overlap transfer. Relate this sign transport to the established principal direct rotation, including the reflection convention and the coincident-ray endpoint.

**Dependencies and story role:** M03, M06, and M11. This is the local mechanism from which the narrative builds the global algorithm.

**Conceptual connection:** The transport is determined by projectors, so removing overlap attenuation does not require choosing or learning the phases of source-vector representatives.

**Sources:** [Transport §§1–2, equations (1)–(4)](../science/transport.md#1-a-projector-defined-transport); its reference [1] credits Bravyi, DiVincenzo, and Loss. Childs §§27.1 and 29.3 provide spectral-operation background; the rank-one derivation is local.

### M13 — A fixed-phase block encoding from two labeled reflections

**Central question:** How is the local matrix made available to a polynomial circuit without a coherent source-index oracle?

**Understanding target:** Follow the selector qubit through the two controlled reflections and Hadamard gates, obtaining the block $`Z=P+Q-I`$ with normalization one. Explain why the leading minus sign must become a known phase on an external control and why both source labels remain classical circuit data.

**Dependencies and story role:** M02, M05, M08, and M12. It converts the geometric mechanism into a concrete circuit interface.

**Conceptual connection:** An explicit circuit supplies a controlled operation with a fixed phase. Merely knowing its uncontrolled channel or endpoint-state action would not supply that information.

**Sources:** [Transport §4, equations (7)–(8)](../science/transport.md#4-a-block-encoding-with-a-fixed-phase). Childs §§16.1 and 29.1 provide the control and selected-block concepts.

### M14 — The polar compiler and a coherent clean-ancilla guarantee

**Central question:** What additional guarantee makes a polynomial approximation usable as a controlled transport?

**Understanding target:** Connect the bounded sign approximation to its inverse-$`c`$ query cost and logarithmic precision cost. Explain why block error at most $`\eta^2/2`$ yields clean-input isometry error at most $`\eta`$, and why invertibility makes the inherited row-space condition apply to every input.

**Dependencies and story role:** M08–M09 and M12–M13. It closes the gap between an approximate matrix block and a coherent transformation suitable for a larger algorithm.

**Conceptual connection:** Here $`c`$ bounds the smallest singular value relative to normalization one. It is neither an assumed eigenphase gap of the loop nor necessarily the reciprocal intrinsic condition number of the two-dimensional operator.

**Sources:** [Transport §5, equations (9)–(10)](../science/transport.md#5-the-inherited-polar-compiler-and-its-clean-ancilla-guarantee), including Gilyén et al. and Quek–Rebentrost Corollary 1. Childs §§29.1–29.3 supply foundations; the clean polar theorem is a separately cited research dependency.

### M15 — Closing the loop while preserving control coherence

**Central question:** Why does a sequence of local transports return a specimen with the required global phase?

**Understanding target:** Explain the ordered product $`W=T_L\cdots T_1`$ and its eigenvalue $`e^{-i\Phi}`$ on the initial source state. Connect this phase calculation to the hybrid argument that permits reuse of approximate compiler workspace without postselection or an assumed perfect reset.

**Dependencies and story role:** M05, M09, and M12–M14. It assembles local transfers into the coherent global object that the readout will probe.

**Conceptual connection:** The starting specimen is already an eigenvector of the ideal loop. The proof needs neither a separate eigenstate-preparation routine nor an eigenvalue-isolation promise.

**Sources:** [Transport §3, equations (5)–(6)](../science/transport.md#3-the-loop-and-its-orientation) and [reusing work qubits, equation (11)](../science/transport.md#reusing-work-qubits). Childs §§4.3 and 2.1 provide the eigenphase and composition foundations. The [four-state bridge example](CHILDS_BRIDGE.md#4-a-complete-four-state-loop) illustrates the orientation.

### M16 — A finite Fourier readout with charged loop powers

**Central question:** How does the ideal loop give the required circular estimate at a known finite query cost?

**Understanding target:** Relate $`F=2^{\lceil\log_2(16\pi/\epsilon)\rceil}`$, $`q=F-1`$ expanded loop calls, and $`M=Lq`$ transport occurrences to the measurement distribution. Explain the wrapped Fourier-tail guarantee and the output sign $`\widehat\Phi=-2\pi y/F`$; the pair $`(y,F)`$ is an exact finite description.

**Dependencies and story role:** M07, M11, and M15. It turns the coherent global phase into the specified statistical output and fixes the number of operations the later budgets must cover.

**Conceptual connection:** Precision is built into the ideal circuit's grid and total coherent evolution. It is not obtained by ignoring the cost of controlled powers.

**Sources:** Childs §§4.2–4.3. [Algorithm §1, equations (4)–(7)](../science/algorithm.md#1-an-ideal-phase-estimation-circuit) gives the finite grid and tail bound; [the bridge's conventions](CHILDS_BRIDGE.md#3-conventions-that-matter) explains radians and normalized phase.

### M17 — Controlled reflections from consumed copies

**Central question:** How can fresh specimens simulate the fixed-phase reflection that the query circuit assumes?

**Understanding target:** Explain how controlled partial swaps with a fresh program register reproduce evolution generated by the source projector to first order. Connect the off-diagonal control blocks, the diamond bound $`4\tau^2`$, and $`m`$ independent steps to reflection error at most $`4\pi^2/m`$.

**Dependencies and story role:** M02, M04–M06, M09, and M13. It replaces the temporary reflection-query interface by the actual supplied-copy interface.

**Conceptual connection:** Density-matrix exponentiation must preserve phase relative to the inactive control branch. Fresh programs are consumed; an inverse block-encoding call does not reverse a previously discarded program.

**Sources:** [Resources: controlled density-matrix exponentiation and diamond bound, equations (1)–(5)](../science/resources.md#controlled-density-matrix-exponentiation), with the cited Lloyd–Mohseni–Rebentrost and Kimmel et al. results. Childs §§27.1–27.2 provide evolution and simulation context, not this sample-access lemma.

### M18 — Why the whole query count is squared in copies

**Central question:** How does a local sample simulation guarantee turn into a bound for the complete controlled circuit?

**Understanding target:** Explain the channel hybrid over all $`Q`$ reflection occurrences and the uniform allocation of program copies. Recognize why a constant total simulation error requires order $`Q`$ copies per reflection and order $`Q^2`$ program copies overall, with every inactive control branch still charged.

**Dependencies and story role:** M09, M16, and M17. It connects local sample consumption to the algorithm's global copy resource.

**Conceptual connection:** The Fourier grid has already set angle accuracy. The simulation only needs to preserve a constant success margin, so its total diamond tolerance is not additionally set to $`\epsilon`$.

**Sources:** [Resources: query circuit to copy circuit, equation (6)](../science/resources.md#from-the-query-circuit-to-the-copy-circuit) and [Algorithm §3, equations (11)–(13)](../science/algorithm.md#3-replace-queries-by-supplied-copies). Wang–Zhang Definition 12 and Theorem 13 are the inherited multisource conversion. Childs §2.1 supplies the elementary composition principle.

### M19 — The complete upper bound and its finite error budget

**Central question:** How do the phase resolution, polar approximation, sample simulation, and gate errors fit into one successful algorithm?

**Understanding target:** Combine $`\eta=1/(100M)`$, the actual polar query count $`K`$, $`Q=2KM`$, and $`m=\lceil400\pi^2Q\rceil`$ into $`N=1+Qm`$. Explain the separate error margins and the resulting success at least $`87/100`$, including the initial target copy and the per-source allocation.

**Dependencies and story role:** M14–M18. This integrates the algorithmic branch into the claimed upper theorem rather than leaving a collection of ideal primitives.

**Conceptual connection:** Substituting the charged query count gives $`O(L^2c^{-2}\epsilon^{-2}\log^2(L/\epsilon))`$ total copies. No tomography, individual overlap estimate, or inverse preparation access is hidden in that count.

**Sources:** [Algorithm §§2–4, equations (8)–(14)](../science/algorithm.md#2-compile-every-transport-coherently) and [Resources: parameter table](../science/resources.md#resource-conventions). Childs §§2.1 and 4.3 supply the composition and readout ideas combined by the local budget.

### M20 — Streaming memory, quantum gates, and classical compilation

**Central question:** What computational resources accompany the copy bound, and which costs remain distinct?

**Understanding target:** Explain the persistent target, one live program register, phase register, and constant workspace. Distinguish the known-angle quantum gate bound, finite-gate synthesis overhead, and one-time classical phase-sequence computation; understand why dimension-independent copies do not imply dimension-independent processing or optimal total runtime.

**Dependencies and story role:** M02, M08–M09, and M17–M19. It completes the operational description of the upper construction.

**Conceptual connection:** With $`n=\lceil\log_2d\rceil`$, streaming uses $`2n+O(\log(1/\epsilon))`$ qubits and known-angle processing uses $`O(nN)`$ gates for $`d\ge2`$. Classical compilation can dominate in some parameter regimes.

**Sources:** [Resources: gate implementation and live memory, equations (7)–(9)](../science/resources.md#gate-implementation-and-live-memory) and [classical preprocessing and synthesis, equations (10)–(13)](../science/resources.md#classical-preprocessing-and-gate-synthesis), including Haah's attributed factorization cost. Childs §§1.3, 1.5, 2.1, and 3.4 supply universality, uniformity, and synthesis context.

### M21 — A physical source family with a distributed loop phase

**Central question:** How can a full loop phase vary while each source changes only weakly?

**Understanding target:** Explain the positive circulant Gram matrix built from the cyclic shift, its unit diagonal, its eigenvalue bounds, and the state vectors obtained from its positive square root in a fixed basis. Relate the distributed edge phase to $`B=c^Le^{i\phi}`$.

**Dependencies and story role:** M03, M06, M10, and M11. It begins the converse with actual normalized sources rather than a formal list of unconstrained overlaps.

**Conceptual connection:** For $`c\le1/4`$, the Gram spectrum stays in $`[1-2c,1+2c]`$. The hard family is well conditioned even when the raw full-cycle invariant is tiny.

**Sources:** [Lower bound §1, equations (1)–(6)](../science/lower-bound.md#1-a-normalized-family-of-sources) and [Examples §1](../science/examples.md#1-a-phase-bearing-ring-with-constant-local-overlaps). Childs §4.1 supplies Fourier-basis background; the Gram construction and its fixed embedding are derived locally.

### M22 — Sparse relations, missing triangles, and gauge choice

**Central question:** Why does this family retain a global phase that cannot be recovered from its pairwise magnitudes or shorter nonzero cycles?

**Understanding target:** Connect the ring overlap graph to vanishing non-neighbor overlaps and vanishing simple-cycle invariants of lengths three through $`L-1`$. Distinguish rephasing source-vector representatives from changing their physical embedding by a parameter-dependent common unitary; understand why the latter cannot be substituted into a distinguishability proof.

**Dependencies and story role:** M01, M03, M05, and M21. It explains the global information encoded by the hard family and the gauge discipline needed for its statistical analysis.

**Conceptual connection:** A triangle reconstruction route needs overlap structure absent from this input family. Moving the displayed edge phases by a gauge choice does not move the information between physical specimens.

**Sources:** [Examples §1](../science/examples.md#1-a-phase-bearing-ring-with-constant-local-overlaps) and [Lower bound: moving the edge phases](../science/lower-bound.md#moving-the-edge-phases-does-not-change-the-source-states). Childs §15.3 explains the pairwise statistic; the cycle obstruction and gauge distinction are supplied locally.

### M23 — Cyclic covariance and adaptive source selection

**Central question:** Why can an adaptive choice of source label not evade the lower bound on this family?

**Understanding target:** Use the common known cyclic shift relating every source to the first to explain a simulation from a capped supply of iid first-source specimens. Recognize that adaptive operations, classical records, unused copies, and final measurements can all be included in one parameter-independent channel.

**Dependencies and story role:** M02, M04, M10, and M21–M22. It reduces the full allowed input interface to a single tensor-power discrimination problem.

**Conceptual connection:** The algorithm may choose labels adaptively; the lower-bound family is covariant enough that those choices create no additional parameter access.

**Sources:** [Lower bound §2, equations (7)–(8)](../science/lower-bound.md#2-cyclic-covariance-removes-the-advantage-of-adaptive-label-choices). Childs §§21.1–21.2 provide access-model context; this source-simulation reduction is local.

### M24 — Weak single-copy sensitivity as a finite fidelity bound

**Central question:** How does distributing phase over the ring limit the distinguishability of individual specimens?

**Understanding target:** Connect the common Fourier eigenbasis to differentiation of the Gram square root, then connect the derivative bound to a finite difference between normalized source vectors and a squared-fidelity bound. Identify the scale $`c/L`$ without assuming an unbiased estimator or replacing the proof by an asymptotic Fisher-information argument.

**Dependencies and story role:** M03, M06, M09–M10, and M21–M23. It quantifies the local statistical weakness that the collective lower bound will amplify.

**Conceptual connection:** The finite bound concerns two actual source tuples separated in target phase. Its validity does not depend on how an estimator parametrizes or processes its outputs.

**Sources:** [Lower bound §3, equations (9)–(14)](../science/lower-bound.md#3-each-supplied-copy-changes-slowly-with-the-target-phase). Childs §4.1 supplies only Fourier-basis background; the matrix derivative and finite-fidelity reasoning are given in the local proof.

### M25 — From an accurate phase estimate to the copy lower bound

**Central question:** How do the weak specimens force a quadratic copy cost for every permitted estimator?

**Understanding target:** Connect target phases separated by $`4\epsilon`$, disjoint circular accuracy regions, a binary decision with success at least $`2/3`$, and trace distance of tensor-power pure states. Explain how this yields the finite bound with constant $`(1-2c)/144`$.

**Dependencies and story role:** M10–M11 and M23–M24. It completes the converse branch, including collective measurements and adaptive classical label selection.

**Conceptual connection:** The result is a task lower bound under a worst-case copy cap, independent of whether a protocol uses reflections, phase estimation, or any other proposed algorithmic primitive.

**Sources:** [Lower bound §§4–5, equations (15)–(20)](../science/lower-bound.md#4-phase-estimation-implies-binary-discrimination) and [its theorem](../science/lower-bound.md#theorem). Childs §§21.1–21.2 supply lower-bound modeling context; the finite two-state argument is supplied locally.

### M26 — The direct-cycle benchmark and its actual resource count

**Central question:** What exactly is exponentially costly about measuring the raw cyclic interference signal?

**Understanding target:** Connect the full-cycle Hadamard-test mean to quadrature estimation, angle conditioning, and the direct-readout shot count. Explain why the restricted adaptive-quadrature lower bound matches that scaling and why each shot consumes $`L`$ copies, giving total cost $`\Theta(Lc^{-2L}\epsilon^{-2})`$ on the ring at fixed confidence.

**Dependencies and story role:** M03, M05, M10–M11, M21–M22, and M25. It turns the motivating visibility problem into a precise comparison with the proved copy theorem.

**Conceptual connection:** This comparator retains only each fresh full-cycle ancilla outcome. Its lower bound does not cover all separate-copy measurements, all photonic protocols, or arbitrary collective processing.

**Sources:** Childs §§15.3 and 16.1. [Examples §§2–3, equations (3)–(13)](../science/examples.md#2-what-one-direct-cycle-test-shot-measures), especially [the restricted lower bound](../science/examples.md#the-visibility-dependence-is-unavoidable-for-this-direct-readout-family), gives the estimator, finite converse, and shot-to-copy conversion.

### M27 — Joining sufficiency and necessity in the minimax theorem

**Central question:** Which parameter dependences are established as nearly optimal, and over which inputs?

**Understanding target:** Combine the algorithmic upper bound and task lower bound under the same total-copy and success conventions. Identify the matching powers of $`L`$, $`c^{-1}`$, and $`\epsilon^{-1}`$, the remaining logarithms, and the lower-bound restrictions $`0\lt c\le1/4`$ and $`d\ge L`$.

**Dependencies and story role:** M11, M19–M20, and M25–M26. It joins the two proof branches into the principal theorem and its sparse-cycle consequence.

**Conceptual connection:** Dimension independence is an upper copy guarantee. The converse is a worst-case statement in sufficiently large dimension, not the same uniform small-overlap law for every fixed dimension.

**Sources:** [Model §4](../science/model.md#4-main-theorem), [Algorithm: upper bound](../science/algorithm.md#upper-bound), and [Lower bound: theorem and scope](../science/lower-bound.md#scope-of-optimality). Childs §§21.1–21.2 provide the language of resource bounds; the minimax copy law is the project result.

### M28 — Established ingredients and the task-specific contribution

**Central question:** What has been imported from prior work, and what does their combination establish for this problem?

**Understanding target:** Attribute direct rotation, polar compilation, Fourier phase estimation, density-matrix exponentiation, multisource simulation, and phase synthesis to their established sources. Distinguish a raw-trace or Gram-reconstruction guarantee from precision of its argument, and an uncontrolled emulator guarantee from the fixed-phase controlled operation required here.

**Dependencies and story role:** M12–M20 and M25–M27. It places the complete theorem in its scientific context without identifying newness with a familiar primitive.

**Conceptual connection:** The contribution is the explicit phase-estimation construction and corresponding finite copy law for the adjacent-overlap source model. Similar algebra or an earlier polynomial simulation primitive does not alone settle that statistical task.

**Sources:** [Related work §§1–6](../references/related-work.md#1-established-ingredients-used-by-the-algorithm) and the primary references identified there. Childs §§4.3 and 29.1–29.3 are the educational foundation for established algorithmic ideas, not a substitute for research attribution or the task-specific converse.

### M29 — Assumptions, endpoints, and additional structure

**Central question:** Which changes to the input or physical interface would require a new scientific statement?

**Understanding target:** Explain the roles of purity, independent stationary sources, accessible controlled swaps, nonzero adjacent overlaps, and a specified discrete loop. Interpret $`c=1`$, the excluded zero-overlap endpoint, dimensions below the lower-bound regime, and possible extra overlap structure without extending the theorem to mixed states, passive optical control, noisy sources, or a continuum Berry phase.

**Dependencies and story role:** M02, M11, M20–M22, and M27–M28. It connects the theorem's quantifiers to physical and computational uses.

**Conceptual connection:** Additional information can change the problem, while less coherent access can remove operations used by the upper construction. A discrete geometric-phase theorem supplies no automatic adiabatic or source-noise guarantee.

**Sources:** [Interpretation: operational meaning and geometric scope](../science/interpretation.md#operational-meaning-of-the-input), [Lower bound: endpoints](../science/lower-bound.md#gauge-choice-and-endpoints), and [Resources: what the bound establishes](../science/resources.md#what-the-bound-establishes). Childs §§27.1–27.2 give simulation context; §30.1 is relevant only for distinguishing an adiabatic-path setting from the present discrete input.

### M30 — The complete explanation of phase access beyond raw visibility

**Central question:** Why can an exponentially weak cyclic signal coexist with a nearly optimal polynomial copy algorithm?

**Understanding target:** Connect the whole chain: projector-defined phase transport, its controlled compiler, the loop eigenphase, the Fourier query count, the quadratic sample conversion, and the matching finite discrimination argument. Explain why the direct visibility is a property of one experiment while the minimax copy law concerns all allowed processing, and identify the proved scope and remaining logarithmic or compilation improvements without turning them into established results.

**Dependencies and story role:** M11–M29. This concludes the narrative phase by integrating mechanism, implementation, necessity, comparison, attribution, and operational meaning.

**Conceptual connection:** The local overlap controls both the cost of coherent normalization and how weakly the hard specimens encode phase. The two independent arguments meet at the same powers of loop length, reciprocal overlap, and accuracy in the stated regime.

**Sources:** [Model §4](../science/model.md#4-main-theorem), [Interpretation](../science/interpretation.md), [Examples §4](../science/examples.md#4-coherent-transport-removes-the-full-cycle-visibility-factor), and [Related work §6](../references/related-work.md#6-scope-of-the-comparison). Childs §§4.3, 21.1–21.2, and 29.1–29.3 provide the algorithmic language synthesized by the project; the [Childs bridge](CHILDS_BRIDGE.md#7-reading-the-result-with-its-limits) connects that language to the full result.
