# Phase information in a coherent block

The visibility of a specified cycle test does not bound the performance of every measurement on the same copies. This page optimizes the four-copy experiment and then proves a bound uniform in the number of copies in a block. The latter is needed when coherent runs grow as the neighboring overlaps become small. The [complete-reset converse](coherent-runs.md) combines this phase-specific information bound with a fixed-source adaptive transcript comparison.

## 1. Sparse four-state cycle and block experiment

Let $`S|j\rangle=|j+1\rangle`$ on four labels, with cyclic indices, and set

```math
G_\phi=I+c\left(e^{-i\phi/4}S+e^{i\phi/4}S^\dagger\right),
\qquad 0\lt c\le\frac14.
\qquad\text{(1)}
```

Its diagonal entries are one, its opposite-label entries vanish, and

```math
(1-2c)I\preceq G_\phi\preceq(1+2c)I.
```

Embed $`\mathbb C^4`$ isometrically into $`\mathbb C^d`$, where $`d\ge4`$, and take $`|\psi_j(\phi)\rangle=G_\phi^{1/2}|j\rangle`$ in that subspace. The forward overlaps and target are

```math
\langle\psi_j(\phi)|\psi_{j+1}(\phi)\rangle
=ce^{i\phi/4},
\qquad
B(\phi)=c^4e^{i\phi},
\qquad \Phi=\phi\pmod{2\pi}.
\qquad\text{(2)}
```

A fixed stock contains $`r_j`$ copies of source $`j`$, in a known order, with $`t=\sum_jr_j`$. Write its tensor vector as $`|v_\phi\rangle`$. The invariant stock experiment is the common-unitary Haar average

```math
\omega_\phi
=\int_{\mathrm U(d)}
U^{\otimes t}|v_\phi\rangle\langle v_\phi|
(U^\dagger)^{\otimes t}\,dU.
\qquad\text{(3)}
```

One unknown orientation is shared by all copies in this stock. Equation (3) is a statistical experiment for an invariant measurement or a Haar prior over unknown orientations. It does not authorize independently averaging successive runs from stationary sources. That additional comparison is proved separately in [Coherent runs](coherent-runs.md).

Throughout this page $`D(\rho\|\sigma)`$ is quantum relative entropy with natural logarithms. Quantum Fisher information uses the symmetric logarithmic derivative convention: if $`\dot\rho=(L\rho+\rho L)/2`$, then $`F_Q=\mathrm{Tr}(\rho L^2)`$.

## 2. A finite Gram representation

Let $`\mathcal W_r`$ be the set of words of length $`t`$ having exactly $`r_j`$ occurrences of label $`j`$, and put

```math
K=|\mathcal W_r|=\frac{t!}{r_1!r_2!r_3!r_4!}.
```

Use an orthonormal abstract basis indexed by these words. The tensor-word Gram operator is

```math
C_\phi(w,z)
=\prod_{k=1}^{t}G_\phi[w_k,z_k],
\qquad w,z\in\mathcal W_r.
\qquad\text{(4)}
```

It is positive definite and $`\mathrm{Tr}C_\phi=K`$. If $`P_r`$ projects onto the fixed-type word subspace of $`(\mathbb C^4)^{\otimes t}`$, then

```math
C_\phi
=\left.P_rG_\phi^{\otimes t}P_r\right|_{\mathcal W_r}.
\qquad\text{(5)}
```

The following identification makes this finite matrix useful for optimal block measurements:

```math
\begin{aligned}
D(\omega_\phi\|\omega_\theta)
&=D(C_\phi/K\|C_\theta/K),\\
F_Q(\omega_\phi)&=F_Q(C_\phi/K).
\end{aligned}
\qquad\text{(6)}
```

These identities hold for every multiplicity vector and every $`d\ge4`$, including $`t\gt d`$.

### Schur decomposition and the transpose

Let $`H=S_{r_1}\times\cdots\times S_{r_4}`$ be the stabilizer of the chosen stock word. Its permutation module decomposes as

```math
\mathbb C[S_t/H]
\cong\bigoplus_\lambda W_\lambda\otimes M_\lambda,
\qquad
d_\lambda=\dim W_\lambda,
\qquad
m_\lambda=\dim M_\lambda=\dim W_\lambda^H.
\qquad\text{(7)}
```

The tensor-word orbit map $`A_\phi`$ sends the abstract word $`w`$ to $`\bigotimes_k|\psi_{w_k}(\phi)\rangle`$. It intertwines the $`S_t`$ actions, and $`A_\phi^\dagger A_\phi=C_\phi`$. With the physical Schur decomposition ordered as $`\bigoplus_\lambda W_\lambda\otimes V_\lambda^{(d)}`$, it therefore has blocks

```math
A_\phi=\bigoplus_\lambda I_{W_\lambda}\otimes A_{\phi,\lambda},
\qquad
C_\phi=\bigoplus_\lambda I_{W_\lambda}\otimes C_{\phi,\lambda},
\qquad
C_{\phi,\lambda}=A_{\phi,\lambda}^\dagger A_{\phi,\lambda}.
\qquad\text{(8)}
```

Only partitions with at most four rows occur in this four-label permutation module. All corresponding physical sectors exist when $`d\ge4`$.

Choose orthonormal $`H`$-invariant vectors $`\eta_{\lambda,a}\in W_\lambda`$ and an orthonormal basis $`e_{\lambda,a}\in M_\lambda`$. The component of the distinguished stock word in (7) can be written

```math
\sqrt{\frac{d_\lambda}{K}}
\sum_{a=1}^{m_\lambda}
\eta_{\lambda,a}\otimes e_{\lambda,a}.
\qquad\text{(9)}
```

Applying the orbit map and Haar twirling the $`V_\lambda^{(d)}`$ factor gives, up to fixed factor ordering, the block

```math
\frac{I_{V_\lambda^{(d)}}}{D_\lambda}
\otimes
\frac{d_\lambda}{K}C_{\phi,\lambda}^{\mathsf T},
\qquad D_\lambda=\dim V_\lambda^{(d)}.
\qquad\text{(10)}
```

The second factor is embedded in the span of the $`\eta_{\lambda,a}`$; its orthogonal zero subspace is fixed and may be removed. In contrast, $`C_\phi/K`$ has block $`I_{W_\lambda}\otimes C_{\phi,\lambda}/K`$. Both descriptions assign the same sector weight $`d_\lambda\mathrm{Tr}C_{\phi,\lambda}/K`$. Adding or discarding a known maximally mixed representation factor preserves relative entropy and Fisher information. Simultaneous transposition preserves them as well. This proves (6), including varying sector probabilities.

The transpose is material: it does not define a completely positive map on arbitrary ancillary extensions. Equation (6) asserts equality of the stated information quantities. For ordinary measurement probabilities, blockwise transposition sends positive effects to positive effects and gives the corresponding measurement directly. In the four-copy commuting family below, a common classical eigenvalue experiment suffices.

## 3. Exact optimal four-copy information

Take one copy of each label, so $`t=4`$, $`K=24`$, and the word module is the regular representation of $`S_4`$. Choose regular permutation operators $`R_\pi`$ consistently with (4), and let

```math
\begin{aligned}
g&=(1234),\\
A&=R_{(12)}+R_{(23)}+R_{(34)}+R_{(41)},\\
B_0&=R_{(12)(34)}+R_{(14)(23)}.
\end{aligned}
```

Here $`B_0`$ is a permutation sum, distinct from the Bargmann invariant $`B(\phi)`$. The only nonzero Gram coefficients are the identity, these four transpositions, these two double swaps, and the two oriented four-cycles. Hence

```math
C_\phi
=I+c^2A+c^4\left(
B_0+e^{i\phi}R_g+e^{-i\phi}R_g^{-1}
\right).
\qquad\text{(11)}
```

Reversing the regular-action convention exchanges $`g`$ and $`g^{-1}`$ and reverses the phase sign, without changing any information quantity below.

The normal operators $`A,B_0,R_g`$ commute. Conjugation by $`g`$ preserves the edge set in $`A`$, and the two double swaps preserve it as well. The double swaps commute with each other and their product is $`g^2`$. Thus the whole family $`C_\phi`$ has one phase-independent eigenbasis. Measuring that basis, with the representation-sector factors in (10), attains its quantum Fisher information for every phase.

The exact joint spectrum in the regular model is:

| Eigenvalue $`z`$ of $`R_g`$ | Eigenvalue $`a`$ of $`A`$ | Eigenvalue $`u`$ of $`B_0`$ | Multiplicity $`m`$ |
|---|---:|---:|---:|
| $`1`$ | $`-2`$ | $`2`$ | $`2`$ |
| $`1`$ | $`0`$ | $`-2`$ | $`3`$ |
| $`1`$ | $`4`$ | $`2`$ | $`1`$ |
| $`-1`$ | $`-4`$ | $`2`$ | $`1`$ |
| $`-1`$ | $`0`$ | $`-2`$ | $`3`$ |
| $`-1`$ | $`2`$ | $`2`$ | $`2`$ |
| $`i`$ | $`-2`$ | $`0`$ | $`3`$ |
| $`i`$ | $`2`$ | $`0`$ | $`3`$ |
| $`-i`$ | $`-2`$ | $`0`$ | $`3`$ |
| $`-i`$ | $`2`$ | $`0`$ | $`3`$ |

For a row $`(z,a,u;m)`$, define

```math
k_\phi(z,a,u)
=1+ac^2+uc^4+2c^4\cos(\phi+\arg z).
\qquad\text{(12)}
```

The corresponding eigenvalue probability is $`k_\phi/24`$, repeated $`m`$ times. The exact optimal four-copy Fisher information and finite relative entropy are therefore

```math
\begin{aligned}
F_4(\phi)
&=\frac1{24}\sum_{\mathrm{rows}}
\frac{4mc^8\sin^2(\phi+\arg z)}{k_\phi(z,a,u)},\\
D(\omega_\phi\|\omega_\theta)
&=\frac1{24}\sum_{\mathrm{rows}}
mk_\phi(z,a,u)
\log\frac{k_\phi(z,a,u)}{k_\theta(z,a,u)}.
\end{aligned}
\qquad\text{(13)}
```

These are optima over all measurements on the invariant four-copy experiment, rather than the information of one prescribed interferometer.

### Proof of the spectrum

Multiplication of the listed permutations gives

```math
\begin{aligned}
B_0^2&=2I+2R_g^2,\\
B_0A&=(I+R_g^2)A,\\
A^2&=(R_g+R_g^{-1})A+4I+2B_0.
\end{aligned}
\qquad\text{(14)}
```

Each $`g`$-eigenspace has dimension six: the trace of every nonidentity regular permutation is zero. When $`z=\pm1`$, the first identity gives $`u=\pm2`$; the trace of $`B_0`$ on that eigenspace is zero, so each sign has multiplicity three. On $`u=-2`$, the second identity forces $`A=0`$. On $`u=2`$, the last identity gives roots $`\{-2,4\}`$ for $`z=1`$ and $`\{-4,2\}`$ for $`z=-1`$. The trace of $`A`$ on each relevant subspace is zero, fixing the multiplicities in the table. When $`z=\pm i`$, $`B_0=0`$ and $`A^2=4I`$; its zero trace gives multiplicity three for each sign of $`A`$. This proves the full table.

### Weak-overlap limit and finite discrimination

Put $`\delta=4c^2+4c^4\lt1`$. Equation (11) implies

```math
(1-\delta)I\preceq C_\phi\preceq(1+\delta)I,
\qquad
\frac1{24}\mathrm{Tr}\bigl[(C_\phi')^2\bigr]=2c^8.
\qquad\text{(15)}
```

There is no vanishing background eigenvalue that could convert the small phase coefficient into a larger rare-event Fisher information. In fact,

```math
2c^8\le F_4(\phi)
\le2c^8\left(1+\frac{\delta^2}{1-\delta}\right),
\qquad
F_4(\phi)=2c^8\bigl[1+O(c^4)\bigr]
\qquad\text{(16)}
```

uniformly in $`\phi`$. To obtain the sharper remainder, write $`C_\phi=I+E`$ and $`C_\phi'=c^4H`$. All these matrices commute. Here $`H=i(e^{i\phi}R_g-e^{-i\phi}R_g^{-1})`$ and $`H^2=2I-2\cos(2\phi)R_g^2`$. Neither the identity nor $`g^2`$ occurs in the permutation support of $`E`$. The regular trace therefore gives $`\mathrm{Tr}(H^2E)=0`$ and $`\mathrm{Tr}(H^2)/24=2`$. Using

```math
(I+E)^{-1}=I-E+E^2(I+E)^{-1}
```

in $`F_4=c^8\mathrm{Tr}[H^2(I+E)^{-1}]/24`$ yields (16): the remaining term is nonnegative and at most $`2c^8\delta^2/(1-\delta)`$. At zero phase the exact formula reduces to

```math
F_4(0)=\frac{2c^8}{1-4c^4}.
\qquad\text{(17)}
```

For a finite phase separation $`h=\phi-\theta`$,

```math
\frac{\|C_\phi-C_\theta\|_{\mathrm{HS}}^2}{24}
=8c^8\sin^2(h/2).
```

The classical relative-entropy/chi-square inequality in the common eigenbasis gives

```math
D(\omega_\phi\|\omega_\theta)
\le\frac{8c^8\sin^2(h/2)}{1-\delta}
\le\frac{2c^8h^2}{1-\delta}.
\qquad\text{(18)}
```

The exact leading finite-separation value is $`4c^8\sin^2(h/2)[1+O(c^2)]`$. Its small-$`h`$ limit is $`c^8h^2`$, consistent with the factor $`F_4/2`$ in a local relative-entropy expansion. The finite bound (18) supports binary testing without imposing an unbiasedness assumption on a phase estimator.

### Relation to cycle tests

Measuring the eigenvalue of the four-cycle already gives the four probabilities

```math
p_k(\phi)=\frac{1+2c^4\cos(\phi-\vartheta_k)}4,
\qquad
\vartheta_k\in\{0,\pi/2,\pi,3\pi/2\}.
\qquad\text{(19)}
```

Its Fisher information is $`2c^8+O(c^{16})`$. Thus the standard cycle measurement attains the leading optimal information; the full measurement in (13) improves higher-order terms. Independent four-copy blocks need and suffice $`\Theta(c^{-8})`$ copies at fixed small phase accuracy. The lower statement follows from (18), the classical chain rule and binary testing; the upper statement follows by estimating the real and imaginary cycle expectations to absolute error $`O(c^4\epsilon)`$. The usual cycle tests and Bargmann-invariant measurements are inherited ingredients, as detailed in [Related work](../references/related-work.md).

This one-block conclusion is not yet a lower bound for arbitrary fixed-source complete-reset protocols. Classical records can retain information about a fixed orientation across runs. The next bound supplies the phase calculation required by the separate transcript comparison.

## 4. Information bound uniform in stock size

**Proposition.** For every nonnegative integer multiplicity vector $`r`$, $`t=\sum_jr_j`$, $`d\ge4`$, and arbitrary phases $`\phi,\theta`$,

```math
D(\omega_\phi\|\omega_\theta)
\le\frac83t^4c^8e^{4tc^2}.
\qquad\text{(20)}
```

The estimate is uniform when $`t`$ grows with $`1/c`$. In particular, it remains useful for $`t=O(c^{-2})`$; extrapolating a fixed-$`t`$ Fisher expansion would not establish this.

### A fixed-type minimum eigenvalue bound

Write $`E_\phi=G_\phi-I`$, so $`\|E_\phi\|\le2c`$. The scalar inequality

```math
\log(1+y)\ge y-\frac{y^2}{2(1-2c)},
\qquad |y|\le2c,
```

follows by bounding the tail of the logarithm series. Functional calculus applies it to $`E_\phi`$. Its diagonal entries obey

```math
(E_\phi)_{jj}=0,
\qquad (E_\phi^2)_{jj}=2c^2,
\qquad
(\log G_\phi)_{jj}
\ge-\frac{c^2}{1-2c}\ge-2c^2.
\qquad\text{(21)}
```

Define $`T_\phi=\sum_{k=1}^t(\log G_\phi)^{(k)}`$, so $`e^{T_\phi}=G_\phi^{\otimes t}`$. For any unit vector $`x`$ in the fixed-type subspace, a one-site off-diagonal matrix element changes the label counts and maps that subspace into its orthogonal complement. Therefore

```math
\langle x|T_\phi|x\rangle
=\sum_jr_j(\log G_\phi)_{jj}
\ge-2tc^2.
```

Scalar Jensen applied to the spectral measure of $`T_\phi`$ in this vector gives

```math
\langle x|e^{T_\phi}|x\rangle
\ge e^{\langle x|T_\phi|x\rangle}
\ge e^{-2tc^2}.
```

Together with the compression (5), this proves

```math
C_\phi\succeq e^{-2tc^2}I_K.
\qquad\text{(22)}
```

Only scalar Jensen is used here; the exponential is not being asserted to be operator convex. The cruder bound $`C_\phi\succeq(1-2c)^tI`$ would lose the needed control when $`t`$ grows as $`c^{-2}`$.

### Counting phase-dependent matrix entries

A nonzero entry in (4) has the form $`c^ke^{iw\phi}`$, where $`k`$ is the number of positions at which the two words differ. Every changed label moves to one of its two neighbors. Because the words have identical counts, the net directed flow is equal along all four cycle edges. Its common value $`w`$ is an integer, and a nonzero winding requires $`k\ge4`$. Zero-winding entries are independent of phase. Hence

```math
|C_\phi(w_1,w_2)-C_\theta(w_1,w_2)|^2
\le4c^{2k}\,\mathbf1_{\{k\ge4\}}.
```

For each fixed row there are at most $`\binom tk2^k`$ nonzero columns with $`k`$ changed positions: choose the positions, then one neighboring label at each. Ignoring the requirement that these assignments preserve the type only overcounts. Summing the squared entries gives

```math
\begin{aligned}
\frac{\|C_\phi-C_\theta\|_{\mathrm{HS}}^2}{K}
&\le4\sum_{k=4}^t\binom tk(2c^2)^k\\
&\le4\sum_{k=4}^{\infty}\frac{(2tc^2)^k}{k!}\\
&\le\frac83t^4c^8e^{2tc^2}.
\end{aligned}
\qquad\text{(23)}
```

The last line uses $`k!\ge4!(k-4)!`$. This bound is uniform in the phase separation, as appropriate to fixed small accuracy; it does not claim the sharp accuracy dependence as $`\epsilon\to0`$.

### Relative entropy

For a density operator $`\rho`$ and positive $`\sigma`$, the Petz order-two bound and $`\log x\le x-1`$ give

```math
\begin{aligned}
D(\rho\|\sigma)
&\le\log\mathrm{Tr}(\rho^2\sigma^{-1})\\
&\le\mathrm{Tr}\bigl[(\rho-\sigma)\sigma^{-1}(\rho-\sigma)\bigr].
\end{aligned}
\qquad\text{(24)}
```

Apply this to $`C_\phi/K`$ and $`C_\theta/K`$. Equation (22) bounds $`C_\theta^{-1}`$ by $`e^{2tc^2}I`$, while (23) bounds the squared Hilbert–Schmidt difference. The identity (6) then proves (20).

The result concerns a phase, rather than a two-state fidelity. Its proof uses the first nonzero winding on the four-cycle and a bound uniform in the exact source multiplicities. The generic Haar transcript comparison is an independent ingredient; its authoritative account is in [Quantum Fidelity Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence/blob/2fcb88fd734f0235ab83fe2ce628bf8b99c85118/science/haar_comparison.md). The [complete-reset theorem](coherent-runs.md) specifies precisely how the two ingredients compose.
