# Copies, coherent processing, and compilation costs

The copy bound counts every specimen consumed by the algorithm, rather than treating reflections about unknown states as supplied gates. This section derives the controlled sample simulation with a finite constant, explains its streaming implementation, and separates quantum processing from classical circuit synthesis. The notation and error budgets agree with the [algorithm](algorithm.md).

## Resource conventions

Each source returns a pure state in a common register encoding. Let $`n=\lceil\log_2 d\rceil`$; unused computational basis states may pad the register to dimension $`2^n`$. The operators $`P_j+P_{j+1}-I`$ act as $`-I`$ on unused states, so this padding does not reduce the sign gap.

The main parameters of the explicit construction are:

| Symbol | Meaning | Value or bound |
|---|---|---|
| $`F`$ | Fourier grid size | $`2^{\lceil\log_2(16\pi/\epsilon)\rceil}`$ |
| $`t`$ | Phase-register qubits | $`\log_2 F`$ |
| $`q`$ | Expanded loop calls | $`F-1<32\pi/\epsilon`$ |
| $`M`$ | Transport occurrences | $`Lq`$ |
| $`\eta`$ | Local coherent transport error | $`1/(100M)`$ |
| $`K`$ | Block-encoding calls in one polar lift | $`O(c^{-1}\log(1/\eta))`$ |
| $`Q`$ | Fixed-label reflection calls | $`2KM`$ |
| $`m`$ | Program copies per reflection call | $`\lceil400\pi^2 Q\rceil`$ |
| $`N`$ | Total source copies | $`1+Qm`$ |

The exact finite copy budget uses the actual compiled value of $`K`$. Its asymptotic estimate uses the inherited QSVT degree bound. The constants displayed here are sufficient error margins, not optimized resource estimates.

## Controlled density-matrix exponentiation

Density-matrix exponentiation is the established conversion from copies of a state to Hamiltonian evolution under that state. Its original construction and optimal sample analysis are due to Lloyd, Mohseni and Rebentrost [1] and Kimmel et al. [2]. Wang and Zhang's pure-state multi-samplizer packages the same controlled-reflection conversion for an arbitrary query circuit [3]. The following derivation records the precise controlled channel and a sufficient finite error bound.

Let $`S`$ denote the target register, $`B`$ a fresh program register containing the density operator $`P`$, and $`C=|1\rangle\langle1|`$ an external control projector. Additional reference registers are allowed and are left implicit. Put

```math
H=C\otimes\mathrm{SWAP}_{SB},\qquad
h=C\otimes P_S.
```

For a short time $`\tau`$, use the known joint unitary and then discard the program:

```math
\mathcal E_\tau(X)
=\mathrm{Tr}_B\!\left[
e^{-i\tau H}(X\otimes P_B)e^{i\tau H}
\right].
\tag{1}
```

The intended target-control channel is

```math
\mathcal U_\tau(X)=e^{-i\tau h}Xe^{i\tau h}.
```

The swap identities

```math
\mathrm{Tr}_B[\mathrm{SWAP}(A\otimes P)]=PA,
\qquad
\mathrm{Tr}_B[(A\otimes P)\mathrm{SWAP}]=AP
```

show that $`\mathcal E_0=\mathcal U_0`$ and

```math
\left.\frac{d\mathcal E_\tau}{d\tau}\right|_{\tau=0}
=-i[h,\,\cdot\,]
=\left.\frac{d\mathcal U_\tau}{d\tau}\right|_{\tau=0}.
\tag{2}
```

This equality includes the coherence between the inactive and active control branches. For example, if $`X_{01}`$ denotes a control off-diagonal block, (1) maps it to

```math
\cos\tau\,X_{01}+i\sin\tau\,X_{01}P,
```

whose first derivative is $`iX_{01}P`$, exactly as in (2). It is not sufficient to check only the two diagonal control blocks.

### Diamond-norm bound

We use the unhalved diamond norm. For a Hermitian operator $`A`$ of norm at most one, the commutator superoperator $`\mathcal L_A=-i[A,\,\cdot\,]`$ has diamond norm at most two. Therefore the second derivatives of both channels above have diamond norm at most four: conjugation, appending $`P`$, and partial trace are channels of diamond norm one, and $`\|H\|,\|h\|\le1`$.

Taylor's formula with an integral remainder gives

```math
\|\mathcal E_\tau-I-\tau\mathcal L_h\|_\diamond\le2\tau^2,
\qquad
\|\mathcal U_\tau-I-\tau\mathcal L_h\|_\diamond\le2\tau^2.
```

Consequently,

```math
\|\mathcal E_\tau-\mathcal U_\tau\|_\diamond\le4\tau^2.
\tag{3}
```

These bounds are completely bounded and therefore hold with an arbitrary entangled reference. They do not depend on $`d`$.

Use $`m`$ fresh independent program states and set $`\tau=u/m`$. Composition of channels and the telescoping inequality give

```math
\|\mathcal E_{u/m}^{\,m}-\mathcal U_u\|_\diamond
\le m\,4(u/m)^2
=\frac{4u^2}{m}.
\tag{4}
```

For a pure projector $`P`$ and $`u=\pi`$,

```math
e^{-i\pi C\otimes P}
=(I-C)\otimes I+C\otimes(I-2P).
\tag{5}
```

Thus $`m`$ copies implement the required **fixed-phase controlled reflection**, with error at most $`4\pi^2/m`$. Extra control conditions in a compiled SELECT gate can be computed into a single flag and uncomputed using a constant number of ancillas and known gates. Equation (4) applies to that flag even when it is entangled with the other registers.

## From the query circuit to the copy circuit

Write the compiled reflection-query circuit as a sequence of known gates interspersed with $`Q`$ controlled reflections. The source label of each reflection is a fixed classical part of the circuit description. Replacing one occurrence by its simulated channel changes the whole channel by at most the simulation error of that occurrence, because preceding and succeeding channels have diamond norm one. Hence

```math
\|\mathcal A_{\mathrm{copies}}-\mathcal A_{\mathrm{queries}}\|_\diamond
\le\sum_{s=1}^{Q}\frac{4\pi^2}{m_s}.
\tag{6}
```

For a desired total error $`\delta_D`$, the uniform choice

```math
m_s=m=\left\lceil\frac{4\pi^2Q}{\delta_D}\right\rceil
```

therefore consumes

```math
N_j^{\mathrm{program}}=Q_jm,
\qquad
N^{\mathrm{program}}=Qm
```

copies of the respective sources, where $`\sum_jQ_j=Q`$. This is the $`O(Q_jQ/\delta_D)`$ per-source bound in Wang and Zhang's Theorem 13 [3], now with the explicit sufficient constant from (3). Taking $`\delta_D=1/100`$ gives the table above.

There is no coherent source query in (6). A controlled reflection still consumes its allocated program states when its quantum control happens to be inactive. A later call, including one arising from an inverse block encoding, receives fresh programs; the algorithm never tries to reverse a discarded sample register.

The constant **total** simulation error in (6) is the relevant one. Phase estimation's fine resolution comes from the total number of coherent loop calls. Approximate simulation only needs to preserve its constant success probability, so its global diamond error is not set equal to the final angle accuracy.

## Gate implementation and live memory

Each short-time unitary in (1) can be implemented using $`O(n)`$ elementary gates and one reusable ancilla, rather than storing all $`m`$ program copies.

To see this explicitly, let $`V`$ be a known Hermitian involution, and define

```math
A=(H_b\otimes I)\,\mathrm{C}_bV\,(H_b\otimes I).
```

On an eigenvector of $`V`$ with eigenvalue $`+1`$ or $`-1`$, $`A`$ records that sign in the ancilla $`b`$, initially zero. As $`A=A^\dagger`$,

```math
A\,e^{-i\tau Z_b}\,A
\bigl(|0\rangle_b\otimes|v\rangle\bigr)
=|0\rangle_b\otimes e^{-i\tau V}|v\rangle.
\tag{7}
```

For an external control $`C`$, replace the middle gate by $`e^{-i\tau C\otimes Z_b}`$. On the inactive branch the two copies of $`A`$ cancel; on the active branch they give (7). With $`V=\mathrm{SWAP}_{SB}`$, this realizes (1)'s joint unitary and returns $`b`$ to zero. A controlled swap of two $`n`$-qubit registers is a product of $`n`$ controlled swaps of qubit pairs, each having constant elementary gate cost. The number of further controls in this construction is constant.

After each short-time interaction, discard the current program register and request the next one. The target remains coherent throughout. The polar compiler needs constant work space because its block encoding has one selector qubit. Its work space can also be reused, by the hybrid argument in [Transport](transport.md#reusing-work-qubits).

The largest live quantum space therefore contains:

- the persistent $`n`$-qubit target;
- one fresh $`n`$-qubit program;
- the $`t=O(\log(1/\epsilon))`$ phase qubits;
- a constant number of selector, polar, swap-simulation and control-flag qubits.

In total,

```math
S_{\mathrm{quantum}}=2n+O(\log(1/\epsilon)).
\tag{8}
```

This counts coherent live memory, not a requirement to hold all source copies simultaneously. It assumes a streaming source interface that can deliver fresh labelled programs when requested. It is an upper bound on memory, with no memory-optimality claim.

There are $`Qm`$ short-time program interactions. Apart from them, the polar circuit uses $`O(Q)`$ known elementary gates and an exact inverse Fourier transform uses $`O(t^2)`$ gates. Thus, for $`d\ge2`$,

```math
G_0=O(nQm+Q+t^2)
=O(nQ^2+t^2)
=O\!\left(
n\frac{L^2}{c^2\epsilon^2}\log^2\frac{L}{\epsilon}
\right).
\tag{9}
```

Here $`G_0`$ counts known-angle one- and two-qubit gates. The case $`d=1`$ is trivial and can output zero directly. Sequential execution has depth at most $`G_0`$; no small-depth claim is made.

## Classical preprocessing and gate synthesis

### The phase sequence is computed once

The promise bound $`c`$ and target $`\epsilon`$ are classical numerical parameters. In a uniform finite-input implementation, supply rational bounds of sufficient precision; replacing either by a conservative value within a factor of two changes only constants. The input bit lengths are charged to classical preprocessing.

The bounded sign approximant and its QSVT phase sequence depend on $`c,\eta`$, not on the unknown source vectors, their overlaps, or $`d`$. One common sequence is reused for every edge and every controlled loop occurrence. Computing this sequence is a classical task; it is not an additional state-access oracle.

A sufficient numerical convention is to require the **final** selected block of the finite-precision polar circuit to obey

```math
\|J^\dagger V_jJ-T_j\|\le\eta^2/2.
\tag{10}
```

For example, divide this tolerance among the bounded sign approximation, coefficient rounding, phase-factorization error, and rounding of the returned rotation parameters. Coefficient errors can be bounded in coefficient $`\ell_1`$ norm, which bounds the polynomial error on $`[-1,1]`$. Rounding each of the $`O(K)`$ rotation parameters to $`O(\eta^2/K)`$ changes the entire corresponding unitary by $`O(\eta^2)`$, by a product hybrid bound. These choices need $`O(\log(K/\eta))`$ output bits per rotation parameter; sufficiently small fixed constants in the tolerances ensure (10).

The sign-polynomial and singular-vector constructions are constructive QSVT results [4,5]. Rigorous phase factorization with finite-precision arithmetic is available: Haah gives a sufficient classical running time of

```math
O\!\left(K^3\mathrm{polylog}(K/\xi)\right)
\tag{11}
```

for a degree-$`K`$ QSP function at functional tolerance $`\xi`$, with $`O(K\log(K/\xi))`$ bits of working arithmetic precision [6]. The corresponding QSP/QSVT convention conversions add known single-qubit gates and at most constant factors in degree. Taking $`\xi`$ to be a sufficiently small constant multiple of $`\eta^2`$ is a sufficient polynomial-time preprocessing route. The cost of constructing the sign polynomial and reading the rational parameter descriptions must be added; both are polynomial in the degree and required bit precision. No optimal classical preprocessing bound is claimed.

This one-time cost is independent of $`d`$, but it can dominate the quantum gate count in some parameter regimes, for example at very small $`c`$. Consequently (9) is a **quantum gate bound**, not a claim that the complete classical-plus-quantum running time is always $`O(nN)`$. A conservative end-to-end description adds (11), the polynomial coefficient-generation cost, and the classical circuit-scheduling cost to the quantum processing time.

Known global phases are retained during conversion between phase conventions. In particular, a scalar phase on a controlled block becomes a phase on its control; it cannot be silently dropped. The selected-block criterion (10) fixes the intended matrix phase.

### Finite universal gate sets

Let $`G_0`$ be the actual known-angle gate count of the complete sample circuit, including the inverse Fourier transform and every short-time partial swap. Compile each approximated elementary gate to operator-norm error at most

```math
\zeta=\frac1{100G_0}.
\tag{12}
```

The product hybrid inequality then bounds the error of a unitary dilation of the full computation by $`1/100`$. Subsequent discarding of programs and measurement cannot increase the induced trace distance. This gives the separate gate-synthesis budget used in the algorithm's final success calculation.

Any standard finite universal gate synthesis with polylogarithmic dependence on $`1/\zeta`$ yields a total finite-set gate count

```math
G_{\mathrm{finite}}
=O\!\left(G_0\mathrm{polylog}G_0\right).
\tag{13}
```

The same approximation parameters can be reused for repeated gate types, but their errors are still charged at every occurrence. Equation (12) is a sufficient uniform allocation and makes no assumption of exact arbitrary-angle physical rotations. It leaves the copy count unchanged and needs no additional quantum data registers. Classical control can stream the gate list using counters and the stored common phase sequence; no quantum random-access memory is used.

## What the bound establishes

With the displayed conventions,

```math
N=O\!\left(
\frac{L^2}{c^2\epsilon^2}\log^2\frac{L}{\epsilon}
\right)
```

is a dimension-independent copy bound for a general coherent processor receiving pure-state copies. Gate and memory dependence on the number of qubits is explicit. The compiler, density-matrix exponentiation, and multisource conversion are inherited primitives; their full costs are included. Nothing in this resource analysis gives the processor direct access to a photon degree of freedom that an experiment does not control, or guarantees robustness to impure source copies.

## References

1. S. Lloyd, M. Mohseni and P. Rebentrost, *Quantum principal component analysis*, Nature Physics 10, 631–633 (2014), [arXiv:1307.0401](https://arxiv.org/abs/1307.0401).
2. S. Kimmel, C. Y.-Y. Lin, G. H. Low, M. Ozols and T. J. Yoder, *Hamiltonian Simulation with Optimal Sample Complexity*, npj Quantum Information 3, 13 (2017), [arXiv:1608.00281](https://arxiv.org/abs/1608.00281), [DOI:10.1038/s41534-017-0013-7](https://doi.org/10.1038/s41534-017-0013-7).
3. Q. Wang and Z. Zhang, *Sample-Optimal Quantum Estimators for Pure-State Trace Distance and Fidelity via Samplizer*, ICALP 2026, [DOI:10.4230/LIPIcs.ICALP.2026.154](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.154/LIPIcs.ICALP.2026.154.html). Theorem 13 and equations (59)–(67) state the controlled multisource conversion.
4. A. Gilyén, Y. Su, G. H. Low and N. Wiebe, *Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics*, STOC 2019, [arXiv:1806.01838](https://arxiv.org/abs/1806.01838).
5. Y. Quek and P. Rebentrost, *Fast algorithm for quantum polar decomposition, pretty-good measurements, and the Procrustes problem*, [arXiv:2106.07634](https://arxiv.org/html/2106.07634v1). Corollary 1 specifies the clean-ancilla polar guarantee.
6. J. Haah, *Product Decomposition of Periodic Functions in Quantum Signal Processing*, Quantum 3, 190 (2019), [arXiv:1806.10236](https://arxiv.org/pdf/1806.10236), [DOI:10.22331/q-2019-10-07-190](https://doi.org/10.22331/q-2019-10-07-190). The finite-precision classical factorization cost is inherited from this work.
