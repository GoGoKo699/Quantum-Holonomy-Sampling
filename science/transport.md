# Phase-preserving transport from two projectors

The algorithm uses a unitary determined by two pure-state projectors to carry the phase of their overlap without its magnitude. This section proves the transport identity, relates it to the established direct rotation between subspaces, and gives the precise coherent compilation guarantee used by the [estimation algorithm](algorithm.md).

The matrix identity and the polar-decomposition compiler are established tools. The role of this section is to fix their phase conventions and show that their guarantees are sufficient for a controlled loop built from copies of unknown states.

## 1. A projector-defined transport

Let $`|\psi\rangle,|\phi\rangle\in\mathbb C^d`$ be unit vectors, and write

```math
\begin{gathered}
P=|\psi\rangle\langle\psi|,\qquad
Q=|\phi\rangle\langle\phi|,\\
z=\langle\phi|\psi\rangle,\qquad r=|z|\gt 0.
\end{gathered}
```

Define

```math
Z=P+Q-I,\qquad T_{Q\leftarrow P}=\mathrm{sign}(Z).
```

Here the sign is defined by spectral calculus: it is $`+1`$ on the positive spectrum and $`-1`$ on the negative spectrum. There is no zero eigenvalue under the nonorthogonality assumption.

**Transport identity.** The operator $`T_{Q\leftarrow P}`$ is a Hermitian unitary and satisfies

```math
T_{Q\leftarrow P}|\psi\rangle
=\frac{\langle\phi|\psi\rangle}{|\langle\phi|\psi\rangle|}
 |\phi\rangle.
\qquad\text{(1)}
```

To prove this when $`r\lt 1`$, restrict to the two-dimensional subspace $`\mathcal S=\mathrm{span}\{|\psi\rangle,|\phi\rangle\}`$. Direct calculation gives

```math
Z|\psi\rangle=z|\phi\rangle,\qquad
Z|\phi\rangle=\overline z|\psi\rangle.
```

Consequently $`Z^2=r^2 I`$ on $`\mathcal S`$, and the two eigenvalues of $`Z|_{\mathcal S}`$ are $`r`$ and $`-r`$. On $`\mathcal S^\perp`$, $`Z=-I`$. Thus

```math
\|Z\|\le 1,\qquad
\sigma_{\min}(Z)=r,\qquad
T_{Q\leftarrow P}|_{\mathcal S}=Z/r.
```

Equation (1) follows. If $`r=1`$, then $`P=Q`$ and $`Z=2P-I`$ is already a Hermitian unitary. Equation (1) still holds, including arbitrary choices of vector phases. This also covers $`d=1`$.

The construction depends only on $`P,Q`$. Replacing either representative vector by a phase multiple changes the two sides of (1) consistently and does not change the operator. For any common unitary change of basis $`V`$,

```math
T_{VQV^\dagger\leftarrow VPV^\dagger}
=V T_{Q\leftarrow P}V^\dagger.
\qquad\text{(2)}
```

The transport therefore requires neither a choice of phase for an unknown source nor a classical description of its coordinates.

## 2. Relation to the direct rotation

Use the reflection convention

```math
R_P=I-2P,\qquad R_Q=I-2Q.
```

The principal direct rotation is

```math
U_{P\to Q}=\sqrt{R_QR_P},
\qquad\text{(3)}
```

where the square root has its branch cut on the negative real axis and $`\sqrt 1=1`$. Nonorthogonality ensures that $`R_QR_P`$ has no eigenvalue on that cut. This construction and its positive-overlap phase convention are given explicitly in Bravyi, DiVincenzo and Loss, Section 2.1, Definition 2.1 and Lemma 2.1 [1].

The sign transport is related to it by

```math
U_{P\to Q}=-T_{Q\leftarrow P}R_P.
\qquad\text{(4)}
```

For example, choose representatives with positive overlap and an orthonormal basis of their span in which $`|\psi\rangle=(1,0)^{\mathsf T}`$ and $`|\phi\rangle=(r,s)^{\mathsf T}`$, with $`s=\sqrt{1-r^2}`$. On this span,

```math
T_{Q\leftarrow P}
=\begin{pmatrix}r&s\\s&-r\end{pmatrix},\qquad
-T_{Q\leftarrow P}R_P
=\begin{pmatrix}r&-s\\s&r\end{pmatrix}.
```

The latter is the principal square root of $`R_QR_P`$. Both sides of (4) are the identity on the orthogonal complement. The two transports agree on $`|\psi\rangle`$, because $`R_P|\psi\rangle=-|\psi\rangle`$. The algorithm uses the Hermitian sign transport because its block encoding is particularly simple; a new direct-rotation identity is not claimed.

## 3. The loop and its orientation

For $`L`$ projectors $`P_j=|\psi_j\rangle\langle\psi_j|`$, set $`P_{L+1}=P_1`$ and $`|\psi_{L+1}\rangle=|\psi_1\rangle`$. The target convention throughout this repository is

```math
B=\prod_{j=1}^{L}\langle\psi_j|\psi_{j+1}\rangle,
\qquad \Phi=\arg B\pmod{2\pi}.
\qquad\text{(5)}
```

Assume $`r_j=|\langle\psi_{j+1}|\psi_j\rangle|\gt 0`$, and define

```math
T_j=\mathrm{sign}(P_j+P_{j+1}-I),\qquad
W=T_L T_{L-1}\cdots T_1.
```

Applying (1) successively gives

```math
\begin{aligned}
W|\psi_1\rangle
&=\left(\prod_{j=1}^{L}
\frac{\langle\psi_{j+1}|\psi_j\rangle}{r_j}\right)
|\psi_1\rangle\\
&=\frac{\overline B}{|B|}|\psi_1\rangle
=e^{-i\Phi}|\psi_1\rangle.
\end{aligned}
\qquad\text{(6)}
```

The minus sign in this eigenphase is part of the convention. The final classical output negates the phase measured by phase estimation. Equation (6) needs no eigenvalue gap for $`W`$: the initial specimen is already an exact eigenvector, whether or not that eigenvalue is degenerate. The phase is that of the discrete loop in (5); no continuum interpolation or Berry-phase discretization estimate is assumed.

## 4. A block encoding with a fixed phase

Temporarily regard the reflections $`R_j=I-2P_j`$ as query gates. The [resource analysis](resources.md) replaces every such query by a channel consuming source copies.

With one selector qubit $`a`$, define

```math
\begin{aligned}
D_j&=|0\rangle\langle0|_a\otimes R_j
    +|1\rangle\langle1|_a\otimes R_{j+1},
\\
U_j^{\mathrm{be}}&=-(H_a\otimes I)D_j(H_a\otimes I).
\end{aligned}
\qquad\text{(7)}
```

This is a Hermitian unitary. Its top block is exactly

```math
\begin{gathered}
(\langle0|_a\otimes I)U_j^{\mathrm{be}}(|0\rangle_a\otimes I)\\
=-\frac{R_j+R_{j+1}}{2}
=P_j+P_{j+1}-I=Z_j.
\end{gathered}
\qquad\text{(8)}
```

The selector is implemented by one reflection controlled on $`a=0`$ and another controlled on $`a=1`$. Both source labels are known from the circuit position. The coherent selector chooses between applying two fixed-label gates; it does not query a source on a superposition of labels.

The leading minus sign in (7) must be retained. When $`U_j^{\mathrm{be}}`$ is externally controlled, that sign becomes a known phase gate on the external control. Controlling the entire explicit circuit, including such known phase gates, fixes the convention needed by (6).

## 5. The inherited polar compiler and its clean-ancilla guarantee

Suppose $`r_j\ge c\gt 0`$. Then $`Z_j`$ is invertible, $`\|Z_j\|\le1`$, and $`\sigma_{\min}(Z_j)\ge c`$. Its unitary polar factor is $`T_j=\mathrm{sign}(Z_j)`$.

Quantum singular value transformation supplies a bounded odd sign approximation on $`[-1,-c]\cup[c,1]`$ with degree

```math
K=O\!\left(c^{-1}\log(1/\delta)\right).
\qquad\text{(9)}
```

Applied to (8), the singular-vector transformation gives a unitary lift whose selected block approximates $`T_j`$ to operator error $`\delta`$. This is the standard QSVT primitive [2]. Quek and Rebentrost's Corollary 1, equations (7)–(8), states its corresponding clean-ancilla vector guarantee explicitly [3]. Their row-space hypothesis holds for every input here because $`Z_j`$ is invertible. No amplitude amplification is needed.

For completeness, the implication from a block guarantee to a coherent lift follows directly from unitarity. Let $`J|v\rangle=|0^b\rangle\otimes|v\rangle`$ embed a system into the clean work space, and let $`V_j`$ be a unitary such that

```math
A_j=J^\dagger V_j J,\qquad \|A_j-T_j\|\le\delta.
```

For any unit vector $`|v\rangle`$,

```math
\begin{aligned}
\|V_jJ|v\rangle-JT_j|v\rangle\|^2
&=2-2\mathrm{Re}\langle v|T_j^\dagger A_j|v\rangle\\
&\le2\delta.
\end{aligned}
\qquad\text{(10)}
```

Thus, to obtain an isometry error at most $`\eta`$, it is sufficient to choose $`\delta\le\eta^2/2`$. The query count is still $`K=O(c^{-1}\log(1/\eta))`$. We use $`K`$ for the **total** number of calls to $`U_j^{\mathrm{be}}`$ or its adjoint in one lift. The same coefficient sequence works for every edge because $`c`$ and $`\eta`$ are common. The work size $`b`$ is constant for this one-ancilla block encoding.

Equation (10) bounds $`\|V_jJ-JT_j\|`$, so it continues to hold when the target is entangled with arbitrary other registers. It is stronger than agreement of the output density matrices up to an unspecified phase.

### Controlled use

For an additional control qubit, compare

```math
\mathrm{C}V_j=|0\rangle\langle0|\otimes I
             +|1\rangle\langle1|\otimes V_j
```

to the controlled ideal transport. Their difference is zero on the inactive branch and is bounded by $`\eta`$ on the active clean-ancilla branch. This proves the same isometry bound for controlled use, including a superposed or entangled control.

This control is implemented by controlling known gates of the polar circuit. The only unknown gates appearing in it are fixed-phase reflections, supplied in the next stage as approximations to $`e^{-i\pi P_j}=R_j`$. An inverse block-encoding call requires no inverse state-preparation operation: its reflection gates are self-inverse, and the other gates are known.

### Reusing work qubits

The clean work register can be reused without measurement or resetting. Let $`A_s`$ denote the implemented controlled lift at occurrence $`s`$, and let $`B_s`$ be its ideal controlled $`T_j`$, extended by the identity on the work register. In a circuit with $`M`$ occurrences,

```math
\begin{gathered}
A_M\cdots A_1-B_M\cdots B_1\\
=\sum_{s=1}^{M}
A_M\cdots A_{s+1}(A_s-B_s)B_{s-1}\cdots B_1.
\end{gathered}
\qquad\text{(11)}
```

Every ideal prefix keeps the work register in $`|0^b\rangle`$. Therefore each summand, when applied to the initial state, has norm at most $`\eta`$. The total error is at most $`M\eta`$. The proof makes no claim that $`A_s`$ is close to $`B_s`$ on arbitrary dirty work states. Actual leakage is simply carried through later unitaries, whose norms are one.

The finite-precision synthesis of the common phase sequence is charged in [Resources](resources.md#classical-preprocessing-and-gate-synthesis). Its error is included in the block tolerance used in (10).

## References

1. S. Bravyi, D. P. DiVincenzo and D. Loss, *Schrieffer-Wolff transformation for quantum many-body systems*, Annals of Physics 326, 2793–2826 (2011), [arXiv:1105.0675](https://arxiv.org/html/1105.0675v1). Section 2.1 gives the direct rotation and its phase convention.
2. A. Gilyén, Y. Su, G. H. Low and N. Wiebe, *Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics*, STOC 2019, 193–204, [arXiv:1806.01838](https://arxiv.org/abs/1806.01838). The singular-vector transformation and bounded sign approximation are inherited.
3. Y. Quek and P. Rebentrost, *Fast algorithm for quantum polar decomposition, pretty-good measurements, and the Procrustes problem*, [arXiv:2106.07634](https://arxiv.org/html/2106.07634v1). Corollary 1, equations (7)–(8), gives the clean-ancilla polar guarantee.
4. S. Lloyd et al., *Quantum polar decomposition algorithm*, [arXiv:2006.00841](https://arxiv.org/pdf/2006.00841). This is an earlier sign-filtering implementation of the polar transformation.
