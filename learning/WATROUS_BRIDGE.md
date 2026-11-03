# From Watrous to phase estimation and coherent-run necessity

A loop of unknown pure states contains a gauge-invariant phase. Coherent transport estimates it with nearly optimal total copies. A second question asks whether a processor can achieve the same copy order while repeatedly discarding every unknown quantum record. This bridge develops both questions from the single selected educational anchor, **Watrous (2018)**, and connects them to the project's authoritative proofs.

The [thirty-milestone map](MILESTONES.md) specifies common understanding targets. The explanations below are generally useful learning material; they are independent of any reader's assessment history. The sister project's root-fidelity theorem remains a different statistical problem. Its fixed-source transcript method is transferred only after a phase-specific information bound has been proved.

## 1. The task before the circuit

Imagine several labeled devices that each supply a quantum register. Repeated requests to device $`j`$ produce independent specimens of the same unknown pure state. The receiver can store these registers, apply known gates to them jointly and measure them. A specimen is quantum data: receiving it does not reveal its vector of amplitudes or provide a circuit that can prepare further specimens for free.

Write the state from device $`j`$ as a normalized vector $`|\psi_j\rangle`$. Its physical pure-state density operator is $`P_j=|\psi_j\rangle\langle\psi_j|`$. Multiplying the vector by any complex number of magnitude one leaves $`P_j`$ unchanged. Such an individual global phase is not observable.

The overlap $`\langle\psi_j|\psi_{j+1}\rangle`$ is a complex amplitude describing the alignment of two state vectors. Its squared magnitude is the probability that a projection onto the second ray accepts the first state. The problem promises that adjacent overlap amplitudes are at least a known $`c\gt0`$. It does not promise that every pair of devices has a substantial overlap.

Arrange the labels in a closed loop, with $`|\psi_{L+1}\rangle=|\psi_1\rangle`$. The target is

```math
B=\prod_{j=1}^{L}\langle\psi_j|\psi_{j+1}\rangle,
\qquad
\Phi=\arg B\pmod{2\pi}.
```

Changing one vector's phase changes its incoming and outgoing overlap by opposite phases. They cancel in the product. Thus $`\Phi`$ is a property of the supplied density operators, even though the phases of their individual vector representatives are arbitrary.

For $`L\ge4`$ and $`0\lt\epsilon\le\pi/16`$, the requested estimate must have circular error at most $`\epsilon`$ with probability at least $`2/3`$ on every admissible input. The resource is the total number of acquired copies, capped in the worst case.

A direct interference experiment can measure the real and imaginary parts of $`B`$. Its signal becomes weak if $`|B|`$ is small. The project asks whether that weak signal is an unavoidable limit on learning $`\Phi`$ from the sources. The answer depends on allowing coherent processing of their registers: local transports can retain each overlap's phase while removing its magnitude, with an explicit cost in fresh copies. The [model](../science/model.md) states exactly what is supplied and counted.

## 2. A focused route through Watrous

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the [author-hosted 2018 manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). Its chapter and section numbers agree with the author's [book page](https://jhwatrous.github.io/books-and-courses.html). Relevant foundations are selected below; reading the entire book is unnecessary.

| Project connection | Anchor sections | Project continuation |
|---|---|---|
| States, phases, registers, tensor copies | §§2.1.1–2.1.3 | [Model §§1–3](../science/model.md#1-independent-labeled-sources) |
| Spectral functions, norms, singular values | §1.1.3 | [Transport §§1–2](../science/transport.md#1-a-projector-defined-transport) |
| Channels, discarding, and measurements | §§2.2.1–2.2.3, 2.3.1–2.3.2 | [Controlled sample simulation](../science/resources.md#controlled-density-matrix-exponentiation) |
| Finite testing and fidelity | §§3.1.1, 3.2.1–3.2.3 | [Unrestricted copy lower bound](../science/lower-bound.md) |
| Error with an entangled reference | §§3.3.1–3.3.3 | [Diamond-norm error](../science/resources.md#diamond-norm-bound) |
| Classical and quantum relative entropy | §§5.1.1–5.1.2, 5.2.1–5.2.3 | [Block information](../science/block-information.md), [adaptive runs](../science/coherent-runs.md) |
| Permutation representations and Haar averaging | §§7.1.1–7.1.2, 7.2.1–7.2.2 | [Four-copy invariant experiment](../science/block-information.md) |

Watrous provides states, measurements, information, symmetry, and the language of the converse. The particular controlled-interference and Fourier circuits, projector transport, polar compilation, sample simulation, four-cycle information, and adaptive transcript transfer are supplied in the project. Research-level sign and polar compiler theorems retain their primary citations in [Transport](../science/transport.md); they are proof dependencies rather than additional educational anchors. In particular, the book is not being credited with the new phase/coherence theorem.

## 3. Conventions that matter

### Radians, Fourier fractions and the loop sign

The project's local Fourier derivation writes a unitary eigenvalue as $`e^{i\varphi}`$, with $`\varphi`$ in radians, and reads its fraction of a full turn through $`\varphi/(2\pi)`$. We use $`\Phi`$ for the desired overlap-product phase and $`\theta`$ for the normalized Fourier fraction. Watrous §§2.1 and 2.3 supply the state and measurement language; [Algorithm §1](../science/algorithm.md#1-an-ideal-phase-estimation-circuit) gives the circuit and finite tail bound.

For adjacent projectors, define

```math
T_j=\mathrm{sign}(P_j+P_{j+1}-I),
\qquad
W=T_L\cdots T_1.
```

The matrix sign sends positive eigenvalues to $`+1`$ and negative eigenvalues to $`-1`$. The [transport identity](../science/transport.md#1-a-projector-defined-transport) gives

```math
\begin{aligned}
T_j|\psi_j\rangle
&=\frac{\langle\psi_{j+1}|\psi_j\rangle}
 {|\langle\psi_{j+1}|\psi_j\rangle|}
 |\psi_{j+1}\rangle,\\
W|\psi_1\rangle&=e^{-i\Phi}|\psi_1\rangle.
\end{aligned}
```

The transport contains the reverse overlap, the complex conjugate of the factor used in $`B`$. That is the origin of the minus sign. The three conventions are therefore

```math
\varphi=-\Phi\pmod{2\pi},
\qquad
\theta=-\frac{\Phi}{2\pi}\pmod1,
\qquad
e^{i\varphi}=e^{2\pi i\theta}.
```

With a Fourier grid of size $`F`$, the measured integer $`y`$ estimates $`F\theta`$ modulo $`F`$. The output is the exact pair $`(y,F)`$ interpreted as

```math
\widehat\Phi=-\frac{2\pi y}{F}\pmod{2\pi}.
```

No decimal angle need be rounded. Accuracy is circular: angles on opposite sides of a chosen branch cut may be close on the circle.

### Overlap amplitude, probability and the singular-value gap

Use $`r_j=|\langle\psi_j|\psi_{j+1}\rangle|`$. The promise is $`r_j\ge c`$, whereas a projective acceptance probability or pure-state **squared fidelity** is $`r_j^2\ge c^2`$. For example, an overlap amplitude $`1/\sqrt2`$ corresponds to probability $`1/2`$. A swap test's symmetric outcome has probability $`(1+r_j^2)/2`$; it does not directly report the complex overlap phase.

The same amplitude controls the local matrix

```math
Z_j=P_j+P_{j+1}-I,
\qquad
\|Z_j\|\le1,
\qquad
\sigma_{\min}(Z_j)=r_j\ge c.
```

Its singular values stay away from zero at the scale of the chosen block encoding, whose normalization is one. A polynomial can therefore approximate its sign with cost proportional to $`1/c`$, up to logarithms. This is the relevant condition parameter. It need not equal the intrinsic ratio $`\sigma_{\max}(Z_j)/\sigma_{\min}(Z_j)`$: in a two-dimensional span filling the whole register, both singular values can equal $`r_j`$ even when $`r_j\lt1`$.

There is no required gap between eigenphases of $`W`$. The initial specimen $`|\psi_1\rangle`$ is already an exact eigenvector of the ideal loop. The theorem also assumes no physical Hamiltonian path or adiabatic gap.

### Source calls and intermediate oracles

A source call acquires one specimen. In the upper-bound proof, a reflection $`R_j=I-2P_j`$ is temporarily treated as a query gate so that the transport circuit can be counted. It is subsequently implemented from fresh specimens. Stopping at the reflection-query count would omit the main statistical cost.

The selector within a block encoding coherently chooses whether to apply one of two **fixed-label gates**. Source acquisition still follows a classical schedule. This does not supply a source on a superposition of labels, a preparation unitary, or its inverse. Likewise, a controlled power $`W^{2^k}`$ is implemented by $`2^k`$ loop applications; it is not a unit-cost input operation.

### Four error quantities with different jobs

| Quantity | Operational role here |
|---|---|
| Vector error $`\lVert \lvert v\rangle-\lvert w\rangle\rVert`$ | Keeps the phase of a coherent branch fixed; it controls the clean-ancilla transport approximation. |
| Operator error $`\lVert A-B\rVert`$ | The largest vector error over normalized inputs; used for the selected matrix block and known-gate synthesis. |
| State trace distance $`D(\rho,\sigma)=\tfrac12\lVert\rho-\sigma\rVert_1`$ | Bounds the change in any measurement-event probability; used in the discrimination converse. |
| Channel diamond norm $`\lVert\mathcal E-\mathcal F\rVert_\diamond`$ | Bounds channel error even with a retained entangled reference; used when program copies are discarded. |

The project uses an **unhalved** diamond norm. A diamond error $`\delta`$ gives state trace distance at most $`\delta/2`$; the success calculation safely uses the looser bound $`\delta`$. For normalized pure states, trace distance is $`\sqrt{1-|\langle v|w\rangle|^2}`$ and is at most their vector distance.

Phase-sensitive vector error is essential before putting a gate under control. The operators $`I`$ and $`-I`$ act identically on an isolated density operator, but their controlled versions differ by a phase flip on the control. Merely producing the correct endpoint ray would therefore not establish the coherent-loop guarantee. The [clean lift and hybrid proof](../science/transport.md#5-the-inherited-polar-compiler-and-its-clean-ancilla-guarantee) addresses exactly this issue.

## 4. A complete four-state loop

Consider four labels producing qubit states

```math
\begin{aligned}
|\psi_1\rangle&=|0\rangle,\\
|\psi_2\rangle&=\frac{|0\rangle+|1\rangle}{\sqrt2},\\
|\psi_3\rangle&=\frac{|0\rangle+i|1\rangle}{\sqrt2},\\
|\psi_4\rangle&=|0\rangle.
\end{aligned}
```

Distinct labels are allowed to produce the same ray. The formulas specify an instance for analysis; the receiver's input remains copies, not these classical coordinates.

The forward overlaps, including the closing edge, are

```math
\begin{aligned}
\langle\psi_1|\psi_2\rangle&=\frac1{\sqrt2},\\
\langle\psi_2|\psi_3\rangle&=\frac{1+i}{2},\\
\langle\psi_3|\psi_4\rangle&=\frac1{\sqrt2},\\
\langle\psi_4|\psi_1\rangle&=1.
\end{aligned}
```

Consequently

```math
\begin{aligned}
c&=\frac1{\sqrt2},&
B&=\frac{1+i}{4},\\
|B|&=\frac1{2\sqrt2},&
\Phi&=\frac\pi4.
\end{aligned}
```

A direct cycle test uses a fresh specimen from each of the four labels. Its ancilla has $`X`$ expectation $`\mathrm{Re}\,B=1/4`$ and $`Y`$ expectation $`\mathrm{Im}\,B=1/4`$, with the cycle orientation fixed as in [Examples](../science/examples.md). Thus a measurement of either quadrature returns its $`+1`$ outcome with probability $`5/8`$. Each such shot consumes four copies. Repeating the shots estimates two small biases and then their angle.

For the coherent route, the exact transport matrices in the computational basis are

```math
\begin{aligned}
T_1&=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},\\
T_2&=\frac1{\sqrt2}
\begin{pmatrix}0&1-i\\1+i&0\end{pmatrix},
\end{aligned}
```

```math
\begin{aligned}
T_3&=\frac1{\sqrt2}
\begin{pmatrix}1&-i\\i&-1\end{pmatrix},\\
T_4&=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\end{aligned}
```

The first transport takes $`|0\rangle`$ to $`|\psi_2\rangle`$. The second takes that state to $`e^{-i\pi/4}|\psi_3\rangle`$. The third returns it to $`e^{-i\pi/4}|0\rangle`$, and the fourth leaves that vector unchanged. In fact,

```math
W=T_4T_3T_2T_1
=\begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix}.
```

The starting specimen is an eigenvector with eigenvalue of magnitude one. Under controlled loop applications, its phase becomes a relative phase between control branches and is measurable.

Here $`\theta=7/8`$. For any power-of-two grid $`F`$ divisible by eight, the ideal control register just before the inverse Fourier transform is

```math
\frac1{\sqrt F}\sum_{s=0}^{F-1}
e^{2\pi i(7/8)s}|s\rangle.
```

The inverse transform returns $`y=7F/8`$ with certainty. Interpreting the pair $`(y,F)`$ gives $`-2\pi(7/8)\equiv\pi/4`$, the desired phase.

A three-qubit grid $`F=8`$ illustrates this exact-grid calculation. For the repository's uniform algorithm at $`\epsilon=\pi/16`$, the prescribed grid is instead $`F=256`$; the ideal outcome is $`y=224`$. That circuit has $`255`$ loop applications and $`1020`$ transport occurrences. If the common transport compiler uses $`K`$ block calls, it contains $`Q=2040K`$ reflection calls. Each receives the fresh-copy budget specified in the next section. The matrices above explain the ideal action; using their entries as supplied gates would bypass the unknown-source task.

This instance satisfies the upper-bound model with $`L=4`$ and $`d=2`$. It illustrates phase orientation and readout, not the worst-case converse. The matching lower bound requires $`d\ge L`$ and $`c\le1/4`$, neither of which holds for the displayed value of $`c`$ and dimension.

## 5. From the loop to a copy budget

The construction has three costs that must be combined: implementing one transport, using enough loop powers to resolve an angle, and simulating all reflections from copies.

The local matrix $`Z_j=P_j+P_{j+1}-I`$ satisfies

```math
Z_j|\psi_j\rangle
=\langle\psi_{j+1}|\psi_j\rangle|\psi_{j+1}\rangle.
```

It has the right phase but an attenuated amplitude. Its sign removes that attenuation. A selector qubit and the two reflections give a block encoding because

```math
-\frac{R_j+R_{j+1}}2=Z_j.
```

Polynomial transformation then implements the sign coherently. The precise clean-ancilla guarantee, rather than a measurement of the selected block, is needed: repeated postselection would reintroduce small success probabilities. The [transport proof](../science/transport.md) shows why work qubits can be reused without resetting them, by comparing each actual operation against an ideal prefix with clean workspace.

Choose $`F`$ as in the [algorithm](../science/algorithm.md), so that $`F=O(1/\epsilon)`$. The exact accounting is

```math
\begin{aligned}
q&=F-1,& M&=Lq,\\
\eta&=\frac1{100M},&
K&=O\!\left(c^{-1}\log(1/\eta)\right),\\
Q&=2KM.
\end{aligned}
```

Here $`q`$ counts full loops, $`M`$ counts local transports, $`\eta`$ is the vector-error allowance per transport, $`K`$ counts block-encoding calls per compiled transport, and $`Q`$ counts controlled reflections. The phase register has only logarithmically many qubits, but its powered operations require $`F-1`$ loop applications.

The remaining primitive is a controlled reflection about an unknown state. Since a projector has eigenvalues zero and one,

```math
e^{-i\pi P_j}=I-2P_j=R_j.
```

A fresh specimen of $`P_j`$ acts as a program for a short controlled partial swap with the target. After that program register is discarded, the target and its control approximately undergo a short evolution generated by the controlled projector. Repeating this with $`m`$ independent fresh program copies and step angle $`\pi/m`$ approximates the controlled reflection. The [resource proof](../science/resources.md#controlled-density-matrix-exponentiation) bounds its unhalved diamond error by $`4\pi^2/m`$, including coherent control and retained entanglement.

To bound the error of all $`Q`$ calls, choose

```math
m=\left\lceil400\pi^2Q\right\rceil,
\qquad
N=1+Qm.
```

The initial one is the target specimen. Every programmed reflection consumes $`m`$ additional copies, including copies acquired when a control branch is inactive. The total simulation error is at most $`1/100`$. Combining the counts gives

```math
N=O\!\left(
\frac{L^2}{c^2\epsilon^2}
\log^2\frac{L}{\epsilon}
\right).
```

This explains why the inverse-accuracy cost of coherent phase estimation becomes an inverse-square-accuracy cost in copies. More reflection calls also require more accurate individual reflection simulations, which consume more program copies.

Copy count is only one resource. With $`n=\lceil\log_2 d\rceil`$, a register swap takes $`O(n)`$ elementary gates. Program copies can be streamed, keeping one target and one program register plus control workspace. Classical synthesis of the common polynomial-transformation phase sequence is also charged; it can dominate quantum processing in some regimes. The [resource account](../science/resources.md) gives the complete gate, memory and preprocessing statements.

## 6. Why the lower bound is a different argument

Counting this algorithm's operations proves sufficiency. To prove necessity, one must consider receivers that use a different construction, retain all their copies and perform an arbitrary joint measurement. A lower bound for a particular reflection simulator would not answer that question.

The [finite converse](../science/lower-bound.md) chooses a family of physical sources whose total loop phase changes appreciably while every individual specimen changes only slightly. For $`L\ge4`$ and $`d\ge L`$, use an $`L`$-dimensional subspace. Let $`S|j\rangle=|j+1\pmod L\rangle`$ be the known cyclic shift and set

```math
\begin{aligned}
G_\phi&=I+c\left(e^{-i\phi/L}S+e^{i\phi/L}S^\dagger\right),\\
|\psi_j(\phi)\rangle&=\sqrt{G_\phi}\,|j\rangle,
\qquad
0\lt c\le\frac14.
\end{aligned}
```

This is a Gram-matrix construction: its diagonal entries are one, so the source vectors are normalized; its eigenvalues lie between $`1-2c`$ and $`1+2c`$, so its positive square root exists. For $`L\ge4`$, the only nonzero off-diagonal overlaps are the ring neighbors. Their forward phases are $`\phi/L`$, and hence $`B=c^Le^{i\phi}`$.

The factor $`1/L`$ spreads the unknown angle across the sources. Comparing phases $`0`$ and $`4\epsilon`$, the squared overlap $`f`$ of the two states from any fixed label obeys

```math
1-f\le
\frac{16c^2\epsilon^2}{L^2(1-2c)}.
```

The source labels do not provide independent ways around this bound: all are related by known cyclic shifts, $`|\psi_j(\phi)\rangle=S^{j-1}|\psi_1(\phi)\rangle`$. A receiver with $`N`$ copies from source one can therefore simulate any adaptive classical label schedule with the same cap. Subsequent processing cannot increase trace distance.

The trace distance between the two pure tensor-power inputs is

```math
D_N=\sqrt{1-f^N}
\le\sqrt{N(1-f)}.
```

An estimate accurate to $`\epsilon`$ would distinguish phases $`0`$ and $`4\epsilon`$ with success at least $`2/3`$, because their allowed output arcs are disjoint. Optimal binary discrimination then requires $`D_N\ge1/3`$. Combining the two inequalities yields

```math
N\ge\frac{(1-2c)L^2}{144c^2\epsilon^2}.
```

This is a finite distinguishability calculation, including adaptive source choice. Its ingredients and the gauge subtlety in choosing representatives are proved in the canonical converse. Watrous §3.1.1 supplies binary discrimination and §3.2 supplies fidelity. The source-family construction and finite copy reduction are local arguments; a general information inequality alone does not establish the theorem's dependence on the loop geometry.

## 7. Reading the unrestricted result

On the sparse ring above, direct cycle interference has magnitude $`r=c^L`$. To infer an angle to error $`\epsilon`$ from its quadratures requires raw-expectation accuracy of order $`r\epsilon`$. The specified direct test consequently needs order $`c^{-2L}\epsilon^{-2}`$ fresh full-cycle shots, with $`L`$ copies in every shot. The [benchmark proof](../science/examples.md) includes both an estimator and a converse for that restricted measurement strategy.

The coherent algorithm has polynomial copy cost, and the general converse matches its powers of $`L`$, $`1/c`$ and $`1/\epsilon`$ up to logarithms in the stated lower-bound regime. The exponential comparison concerns the specified direct-cycle readout. It does not establish a separation against all separate-copy measurements, all classical processing or all optical experiments.

The model assumes pure, stationary sources and coherent access to their registers. The target is the phase of a specified discrete loop. A mixed-state extension, source drift, inaccessible internal photon states or a continuous Berry-phase limit needs additional assumptions and analysis. At $`c=1`$, all rays coincide and the target is zero, illustrating why the matching lower bound is restricted to a different overlap regime.

The complete route is [model](../science/model.md) → [transport](../science/transport.md) → [algorithm](../science/algorithm.md) → [resources](../science/resources.md) → [lower bound](../science/lower-bound.md). The [milestone map](MILESTONES.md) connects those components into the common understanding map, while [related work](../references/related-work.md) separates established primitives from the task-specific resource statement. The following sections address the additional complete-reset question shared with [Quantum-Fidelity-Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence).


## 8. What survives a complete reset

A coherent run consumes at most $`b`$ copies, including copies already measured or discarded. At its end, the complete classical history is the only input-dependent resource available later. Conditioned on that history, every retained quantum register must be a known state the protocol can prepare without the sources. An unmeasured target, a quantum posterior, or correlations with a set-aside ancilla would continue the same coherent run.

This is a channel restriction in the sense of Watrous §§2.2–2.3, not a bound on the number of live qubits. The algorithm above streams program copies through a small workspace while retaining its target and control coherence. It can consume $`N`$ specimens in one run with $`b=N`$, despite storing only one live target and program. Program discards do not reset that target.

Repeated measurements may leave an unlimited classical notebook, and later measurements may use it. The sources themselves remain fixed. A lower bound must include that learning of their orientation. Independently averaging the orientation anew at every reset would remove correlations that the physical notebook can exploit and would analyze a different experiment.

The new question fixes $`L=4`$ and a small accuracy $`0\lt\epsilon\le\pi/16`$, then takes $`c\to0`$. For this limit the upper budget is $`N=O_\epsilon(c^{-2})`$: $`F,M,\eta`$ depend on the fixed accuracy, so the compiler has $`K=O_\epsilon(c^{-1})`$ and no additional overlap logarithm appears in copies. Classical compilation and finite-gate synthesis remain separately charged.

## 9. A sparse four-state experiment with an optimal block measurement

The qubit example in §4 shows transport and readout. The reset converse uses a different, four-dimensional sparse family. Let $`S|j\rangle=|j+1\pmod4\rangle`$ and set

```math
G_\phi=I+c(e^{-i\phi/4}S+e^{i\phi/4}S^\dagger),
\qquad |\psi_j(\phi)\rangle=\sqrt{G_\phi}|j\rangle.
```

The diagonal is one; neighboring overlaps are $`ce^{i\phi/4}`$, opposite overlaps vanish, and $`G_\phi\succeq(1-2c)I`$. Therefore for $`0\lt c\le1/4`$ these are normalized physical states with

```math
B=c^4e^{i\phi}.
```

Apply one unknown common unitary $`U`$ to all four rays. First consider a single block containing exactly one copy of every label. Averaging its common orientation is legitimate for an invariant one-block experiment. Watrous §§7.1–7.2 explain the symmetry and Haar measure; the local proof identifies the particular sufficient matrix.

Permute the four tensor positions in all $`24`$ ways, and let $`C_\phi`$ be their orbit Gram matrix. It has trace $`24`$. The physical averaged state and $`C_\phi/24`$ have identical relative entropy and quantum Fisher information after the Schur decomposition. Parameter-independent maximally mixed representation factors can be discarded. A transpose enters the identification; it preserves these quantities but is not an arbitrary completely positive channel on entangled extensions.

For this one-each block, every phase-dependent entry comes from one of the two oriented four-cycles. Identity, adjacent transpositions, and pairs of disjoint adjacent swaps contribute only real, phase-independent terms. These permutation operators commute in this family. One common spectral measurement is therefore optimal for every $`\phi`$; it is unnecessary to know the unknown phase to choose it.

To see its outputs concretely, write $`g=(1234)`$, let $`A`$ be the sum of the four adjacent swaps, and let $`D`$ be the sum of the two disjoint adjacent swap pairs. A simultaneous eigenspace with eigenvalues $`z,a,d_0`$ has probability $`m k_\phi/24`$, where $`m`$ is its multiplicity and

```math
k_\phi=1+ac^2+d_0c^4+2c^4\cos(\phi+\arg z).
```

The [exact spectrum and probabilities](../science/block-information.md) give a fully specified finite experiment. Its optimal information is

```math
\mathcal F_4(\phi)=2c^8[1+O(c^4)],
\qquad
\mathcal F_4(0)=\frac{2c^8}{1-4c^4}.
```

The phase is encoded in changes of order $`c^4`$ on a probability distribution with order-one background, so its information starts at order $`c^8`$. This explanation follows the optimized experiment, rather than assuming that every possible POVM must behave like a chosen ancilla cycle test. A spectral measurement of the cycle already reaches the leading coefficient; the known cycle tests deserve that credit.

For finite separation $`h=\phi-\theta`$, the same common eigenbasis gives

```math
D(\omega_\phi\|\omega_\theta)
\le\frac{8c^8\sin^2(h/2)}{1-4c^2-4c^4}.
```

Here $`D`$ is quantum relative entropy with natural logarithms, not trace distance. Its finite bound, combined with data processing and binary testing from Watrous Chapters 3 and 5, proves a statistical limitation without assuming an unbiased estimator. Independent invariant four-copy blocks need order $`c^{-8}`$ copies for fixed phase accuracy. This is still a one-block or independently refreshed conclusion; it has not yet handled a fixed physical orientation across many adaptive runs.

## 10. Why the block estimate must be uniform in run length

An endpoint theorem must cover runs whose size grows as $`c`$ decreases. A Taylor expansion with fixed multiplicities cannot be extrapolated into that regime. For a stock with $`r_j`$ copies of label $`j`$, total $`t=\sum_jr_j`$, use the distinct words with these exact label counts as an orthonormal indexing basis. Its dimension is

```math
K_r=\frac{t!}{r_1!r_2!r_3!r_4!}.
```

The stock's orbit Gram matrix is the compression of $`G_\phi^{\otimes t}`$ to this fixed-type space. A naive lower bound $`(1-2c)^t`$ deteriorates at scale $`tc`$, too early to reach the desired $`t\asymp c^{-2}`$ endpoint.

The improvement comes from keeping the exact type constraint. Put $`E=G_\phi-I`$ and $`H=\sum_k(\log G_\phi)^{(k)}`$. Every off-diagonal one-site term changes label counts and maps this space outside itself. Since $`E_{jj}=0`$ and $`(E^2)_{jj}=2c^2`$, the spectral inequality for $`\log(I+E)`$ gives, for every unit vector $`x`$ of fixed type,

```math
\langle x|H|x\rangle\ge-2tc^2.
```

Ordinary scalar Jensen applied to the spectral probability distribution of $`H`$ in $`x`$ gives

```math
\langle x|e^H|x\rangle
\ge e^{\langle x|H|x\rangle}\ge e^{-2tc^2}.
```

This uses a scalar inequality for each vector, not an assertion that the exponential is operator convex. Consequently the compressed Gram matrix obeys

```math
C_\phi\succeq e^{-2tc^2}I.
```

A nonzero phase winding requires at least four changed sites. Counting possible changed labels bounds the squared matrix difference, while the eigenvalue bound controls the inverse matrix in the relative-entropy comparison. Together,

```math
D(\omega_\phi\|\omega_\theta)
\le\frac83t^4c^8e^{4tc^2}.
```

The [uniform proof](../science/coherent-runs.md) supplies the exact combinatorial and Schur steps. Watrous §§1.1.3, 5.2, and 7.1–7.2 provide the language. The fixed-type Jensen argument and its phase-specific use are supplied here, rather than being consequences of the sister's root-fidelity resource formula.

## 11. From stocks to the actual adaptive transcript

There are two separate obstacles. First, source labels and stopping decisions may depend on measurements inside a run. Group complete runs into superblocks and give each superblock $`2\beta`$ copies of every label, where $`\beta=\min(b,N)`$. Selecting unused stock registers simulates every original request. Each stock has $`8\beta`$ copies, the number of stocks is at most $`\lceil N/\beta\rceil`$, and at most $`16N`$ padded copies suffice. Unused stock specimens are charged in this lower-bound comparison, not supplied to the original algorithm for free.

Second, the actual orientation $`U`$ stays fixed. Conditioned on one complete classical transcript leaf, a rank-one refinement of each stock measurement gives a homogeneous polynomial amplitude in the entries of $`U`$. Its coefficients may depend on the specified earlier outcomes. The comparison uses the **unnormalized likelihood of the whole leaf**. A normalized quantum posterior need not have a polynomial form.

The Haar/Gaussian homogeneous-norm comparison and polynomial product inequality, already established as a method in [Quantum-Fidelity-Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence), apply to these four-source stock vectors. They bound the difference between the fixed-orientation transcript $`P_\phi`$ and an auxiliary independently refreshed transcript $`Q_\phi`$:

```math
\mathrm{TV}(P_\phi,Q_\phi)\le\frac{384N^2}{d},
\qquad d\ge32N.
```

The uniform phase-block divergence bounds every conditional refreshed measurement, so data processing and the classical relative-entropy chain rule control the entire refreshed transcript. Pinsker's inequality and two fixed/fresh comparisons then give

```math
\mathrm{TV}(P_\phi,P_\theta)
\le\sqrt{\frac{32768}{3}}\,c^4\sqrt{Nb^3}\,e^{16bc^2}
+\frac{768N^2}{d}.
```

All outcomes, classical histories, within-run adaptation, and random stopping under the deterministic cap are included. A small block signal alone would not justify this inequality. The complete-reset condition is what allows a transcript leaf to factor into history-dependent stock measurements; the comparison then accounts for the common unknown orientation instead of pretending that the sources physically refresh.

## 12. The endpoint and its dimension boundary

Take $`\phi_0=0`$ and $`\phi_1=4\epsilon`$. A uniformly successful circular estimator distinguishes them with transcript total variation at least $`1/3`$. If

```math
N\le C_0c^{-2},\qquad C_0\ge1,
\qquad d\ge9216C_0^2c^{-4},
```

the dimension correction in §11 is at most $`1/12`$. Its remaining term cannot be large enough when

```math
b\lt\frac{c^{-2}}{128C_0^{1/3}}.
```

Thus copy-optimal weak-overlap phase estimation requires $`b=\Omega(c^{-2})`$ in this sufficient high-dimensional regime. The existing algorithm, run as one coherent experiment, has both $`N=O_\epsilon(c^{-2})`$ and $`b=O_\epsilon(c^{-2})`$. Together these statements identify the threshold at the copy-optimal endpoint. They do not claim a matched formula for every $`N,b,c,d`$, nor joint optimality when phase accuracy also tends to zero.

The dimension condition matters. At fixed finite $`d`$, measure each source separately in a tomographically complete set of bases. Classical reconstruction can produce unit vectors whose ray-aligned errors are at most $`\delta=c\epsilon/32`$ with $`O_d(c^{-2}\epsilon^{-2})`$ copies. Adjacent complex overlaps then change by at most $`2\delta`$. Since each true overlap has magnitude at least $`c`$, each argument changes by at most $`4\delta/c`$ and the four arguments change by at most $`\epsilon/2`$. The aligning representative phases cancel in the cyclic product; the algorithm never needs to learn them. Every acquisition can be its own complete-reset run, so $`b=1`$ is possible. [The scope argument](../science/coherent-runs.md) gives an explicit reconstruction and finite-output budget.

The two facts coexist: dimension-uniform processing has a high-dimensional coherent-run requirement, while fixed-dimensional tomography can use a classical notebook efficiently. The joint result supplies the phase-specific information argument behind that requirement. Existing replica hierarchies, invariant cycle tests, polar compilation, and the sister's transcript method remain separately credited foundations.

The specialist route is [model](../science/model.md) → [block information](../science/block-information.md) → [coherent runs](../science/coherent-runs.md). The constructive route remains [transport](../science/transport.md) → [algorithm](../science/algorithm.md) → [resources](../science/resources.md). The [milestone map](MILESTONES.md) joins both routes and the unrestricted [copy lower bound](../science/lower-bound.md) into one scientific account.
