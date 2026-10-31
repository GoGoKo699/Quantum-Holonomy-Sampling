# Estimating the discrete loop phase from copies

The algorithm estimates the phase of a cyclic product of overlaps by coherently transporting one specimen around the loop and reading the resulting eigenphase. It consumes only independent, classically labelled state copies. This section states the access model, gives a finite error budget, and proves the upper bound. The local unitary and its controlled compiler are proved in [Transport](transport.md); the conversion from reflection queries to copies is proved in [Resources](resources.md).

## Access model and target

There are $`L\ge4`$ sources of pure states $`P_j=|\psi_j\rangle\langle\psi_j|`$ on a common $`d`$-dimensional register type. A source call specifies a classical label $`j`$ and returns a fresh independent copy of $`P_j`$. Supplied copies may be processed jointly with clean ancillas and known one- and two-qubit gates. This processing includes coherent controlled swaps between registers in the common encoding.

The input does not supply a state-preparation unitary, its inverse, a coherent source-label oracle, or a classical description of any $`|\psi_j\rangle`$. Preparation of each requested copy is the charged input operation; no complexity guarantee is made for manufacturing the physical sources themselves.

A known number $`0\lt c\le1`$ is a lower bound on every adjacent overlap:

```math
|\langle\psi_j|\psi_{j+1}\rangle|\ge c,
\qquad |\psi_{L+1}\rangle=|\psi_1\rangle.
```

Define

```math
B=\prod_{j=1}^{L}\langle\psi_j|\psi_{j+1}\rangle,
\qquad \Phi=\arg B\pmod{2\pi},
\qquad
\mathrm{dist}_{2\pi}(x,y)
=\min_{k\in\mathbb Z}|x-y+2\pi k|.
```

For $`0\lt \epsilon\le\pi/16`$, the output must satisfy

```math
\Pr\!\left[
\mathrm{dist}_{2\pi}(\widehat\Phi,\Phi)\le\epsilon
\right]\ge\frac23.
\qquad\text{(1)}
```

Every acquired specimen is counted, including the initial target. The bounds below are deterministic upper bounds on the total number acquired. They are independent of $`d`$ in copies, but the gate and memory costs include the register size. When $`c=1`$, all projectors coincide and $`\Phi=0`$; outputting zero without a source call is valid. The general construction also remains well-defined in this case.

## Upper bound

**Theorem.** In this model there is an algorithm satisfying (1) with

```math
N=O\!\left(
\frac{L^2}{c^2\epsilon^2}
\log^2\frac{L}{\epsilon}
\right)
\qquad\text{(2)}
```

total source copies. Let $`n=\lceil\log_2 d\rceil`$. In the model of known-angle elementary gates, its quantum gate count is

```math
O\!\left(
n\frac{L^2}{c^2\epsilon^2}
\log^2\frac{L}{\epsilon}
\right)
\qquad\text{(3)}
```

for $`d\ge2`$, and its live quantum memory is $`2n+O(\log(1/\epsilon))`$ qubits. Classical phase-sequence synthesis is a separate, charged polynomial preprocessing cost, described in [Resources](resources.md#classical-preprocessing-and-gate-synthesis). A finite universal gate set adds gate-synthesis logarithms to (3).

The upper bound holds throughout the stated range of $`c`$. The matching worst-case lower bound is established in [Lower bound](lower-bound.md) for $`0\lt c\le1/4`$ and $`d\ge L`$. No matching claim near $`c=1`$ is implied.

## 1. An ideal phase-estimation circuit

For the moment suppose the transports are exact. From [Transport, equation (6)](transport.md#3-the-loop-and-its-orientation),

```math
W=T_L\cdots T_1,\qquad W|\psi_1\rangle=e^{-i\Phi}|\psi_1\rangle.
```

Choose the Fourier grid size

```math
t=\left\lceil\log_2\frac{16\pi}{\epsilon}\right\rceil,
\qquad F=2^t,
\qquad q=F-1.
\qquad\text{(4)}
```

Then $`16\pi/\epsilon\le F\lt 32\pi/\epsilon`$. Acquire one copy of $`P_1`$ as the target. Prepare a uniform superposition on the $`t`$ phase qubits, apply controlled powers $`W^{2^0},\ldots,W^{2^{t-1}}`$, perform the inverse Fourier transform, and measure $`y\in\{0,\ldots,F-1\}`$. Each power is implemented by repeated loop calls, so the total number of loop calls is exactly $`q=F-1`$. There is no free powered-unitary oracle.

The classical output is

```math
\widehat\Phi=-\frac{2\pi y}{F}\pmod{2\pi}.
\qquad\text{(5)}
```

This output can be represented exactly by the pair $`(y,F)`$ together with the convention (5), so no numerical rounding of an angle is needed for the statistical guarantee.

### Explicit ideal success probability

Write $`e^{-i\Phi}=e^{2\pi i\theta}`$ with $`\theta\in[0,1)`$. Standard Fourier phase estimation gives

```math
p(y)=\left|
\frac1F\sum_{s=0}^{F-1}e^{2\pi i s(\theta-y/F)}
\right|^2.
\qquad\text{(6)}
```

Let $`\Delta_y`$ be the representative of $`F\theta-y`$ in $`[-F/2,F/2]`$. When $`\Delta_y\ne0`$, the geometric-sum formula and $`|\sin(\pi\Delta_y/F)|\ge2|\Delta_y|/F`$ give

```math
p(y)\le\frac1{4\Delta_y^2}.
```

Failure in (1) requires $`|\Delta_y|\gt a`$, where $`a=F\epsilon/(2\pi)\ge8`$. There are at most two outcomes in each unit interval of $`|\Delta_y|`$. Therefore

```math
\Pr[\text{ideal failure}]
\le\frac12\sum_{k=\lfloor a\rfloor}^{\infty}\frac1{k^2}
\le\frac1{2(\lfloor a\rfloor-1)}
\le\frac1{14}\lt \frac1{10}.
\qquad\text{(7)}
```

If $`\theta`$ lies exactly on the Fourier grid, the circuit returns it with certainty. The estimate is circular, so the argument also applies across the branch cut at $`\pm\pi`$.

## 2. Compile every transport coherently

There are exactly

```math
M=Lq
```

local transport occurrences in the expanded phase-estimation circuit. Set

```math
\eta=\frac1{100M}.
\qquad\text{(8)}
```

For each occurrence use the common polar compiler from [Transport](transport.md#5-the-inherited-polar-compiler-and-its-clean-ancilla-guarantee), with total block error at most $`\eta^2/2`$. Its clean-ancilla isometry error is at most $`\eta`$. The compiler's classical numerical precision is included in this block tolerance.

All work qubits are initialized once and reused. The hybrid proof in Transport, equation (11), compares the actual lifts to ideal prefixes that always keep them clean. It gives final state-vector error at most

```math
M\eta=\frac1{100}.
\qquad\text{(9)}
```

There is no intermediate ancilla postselection or reset. In particular, successful endpoint-state preparation with an unspecified environmental phase would not suffice here; the compiler supplies the fixed-phase vector guarantee needed for a controlled loop.

Let $`K`$ be the actual total number of block-encoding or inverse-block-encoding calls in this common compiler. The inherited singular-vector transformation guarantees

```math
K=O\!\left(c^{-1}\log(1/\eta)\right)
=O\!\left(c^{-1}\log(L/\epsilon)\right).
```

Each block-encoding call consists of two fixed-label controlled reflection calls. The expanded circuit consequently contains exactly

```math
Q=2KM
=O\!\left(\frac{L}{c\epsilon}\log\frac{L}{\epsilon}\right)
\qquad\text{(10)}
```

such calls. If a chosen compiler has redundant identity calls, counting them in $`K`$ only enlarges this upper bound. Every label appears in its two adjacent edge compilers, so the uniform circuit uses $`Q_j=2Kq`$ reflection calls to source $`j`$.

## 3. Replace queries by supplied copies

The exact controlled-reflection phase is

```math
e^{-i\pi |1\rangle\langle1|\otimes P_j}
=|0\rangle\langle0|\otimes I
 +|1\rangle\langle1|\otimes R_j.
```

Controlled density-matrix exponentiation implements this channel from $`m`$ fresh copies of $`P_j`$ with unhalved diamond error at most $`4\pi^2/m`$. The bound applies with arbitrary reference entanglement, including the phase and QSVT control registers. A self-contained derivation is given in [Resources](resources.md#controlled-density-matrix-exponentiation).

Use the same integer budget for every reflection call:

```math
m=\left\lceil400\pi^2 Q\right\rceil.
\qquad\text{(11)}
```

The full circuit's accumulated diamond error is at most

```math
Q\frac{4\pi^2}{m}\le\frac1{100}.
\qquad\text{(12)}
```

This is the pure-state multi-samplizer conversion of Wang and Zhang [1], with an explicit nonoptimized constant. The sum is over all reflection occurrences in the entire phase-estimation circuit. The required simulation tolerance is constant: the target precision $`\epsilon`$ has already been set by the ideal Fourier grid. Demanding an additional global diamond tolerance of order $`\epsilon`$ would unnecessarily multiply the copy bound by another inverse power of $`\epsilon`$.

The total number of copies is now the explicit finite budget

```math
N=1+Qm
=1+Q\left\lceil400\pi^2 Q\right\rceil
\le1+400\pi^2 Q^2+Q.
\qquad\text{(13)}
```

The first copy is the target. The other copies are independent programs consumed by the reflection simulations. Substituting (10) proves (2). Individual source counts are $`mQ_j+\mathbf1_{\{j=1\}}`$ for this uniform circuit.

## 4. Finite-gate errors and the final success bound

If arbitrary known-angle gates are not taken as exact, synthesize the known gates of the complete circuit to total state-vector error at most $`1/100`$, as detailed in [Resources](resources.md#classical-preprocessing-and-gate-synthesis). This budget includes the partial-swap rotations, QSVT rotations and inverse Fourier transform. It is separate from the sample-simulation error in (12).

For normalized pure states, their trace distance is at most the norm of their vector difference. Thus (9) changes every measurement-event probability by at most $`1/100`$. The sample-simulation channel in (12) changes it by at most $`1/100`$ as a conservative bound; the exact unhalved-diamond conversion would give half that value. Gate synthesis changes it by at most another $`1/100`$.

Combining these bounds with the weaker ideal guarantee $`9/10`$ from (7) gives

```math
\Pr\!\left[
\mathrm{dist}_{2\pi}(\widehat\Phi,\Phi)\le\epsilon
\right]
\ge\frac9{10}-\frac1{100}-\frac1{100}-\frac1{100}
=\frac{87}{100}\gt \frac23.
\qquad\text{(14)}
```

All compilation and simulation costs are deterministic functions of $`L,c,\epsilon`$. The algorithm never needs to estimate the overlap magnitudes $`r_j`$ individually. It also does not need to reconstruct the source states, or to prepare an eigenvector of the compiled loop from a classical description: the initial source specimen is already an eigenvector of the ideal loop used in the error comparison.

## References

1. Q. Wang and Z. Zhang, *Sample-Optimal Quantum Estimators for Pure-State Trace Distance and Fidelity via Samplizer*, ICALP 2026, LIPIcs 374, Article 154, [DOI:10.4230/LIPIcs.ICALP.2026.154](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.154/LIPIcs.ICALP.2026.154.html). Definition 12 and Theorem 13 give the multisource reflection-to-copy conversion, explicitly including controlled reflections.
2. Y. Quek and P. Rebentrost, *Fast algorithm for quantum polar decomposition, pretty-good measurements, and the Procrustes problem*, [arXiv:2106.07634](https://arxiv.org/html/2106.07634v1). Corollary 1 supplies the coherent polar lift used in step 2.
