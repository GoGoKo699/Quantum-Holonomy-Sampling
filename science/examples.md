# Sparse rings and the cost of direct phase readout

The sparse-ring family makes the distinction between phase and interference visibility explicit. It also gives a comparison in which raw measurement shots and total supplied state copies can be counted separately.

Throughout, the target is

```math
B=\prod_{j=1}^{L}\langle\psi_j|\psi_{j+1}\rangle,
\qquad
\Phi=\arg B\pmod{2\pi}.
```

## 1. A phase-bearing ring with constant local overlaps

Let $`S|j\rangle=|j+1\rangle`$ cyclically on $`\mathbb C^L`$, and choose

```math
G_\phi
=I+c\left(e^{-i\phi/L}S+e^{i\phi/L}S^\dagger\right),
\qquad
|\psi_j(\phi)\rangle=G_\phi^{1/2}|j\rangle,
\tag{1}
```

with $`L\geq4`$ and $`0<c\leq1/4`$. The construction and its normalization are proved in [the lower-bound note](lower-bound.md). It has

```math
\langle\psi_j|\psi_{j+1}\rangle=c e^{i\phi/L},
\qquad
B=c^L e^{i\phi}.
\tag{2}
```

Every pairwise overlap magnitude is independent of $`\phi`$. Non-neighboring vectors are orthogonal. Thus pairwise SWAP tests reveal no phase information, and every triangle of distinct labels has zero Bargmann invariant. More generally, any simple cycle of length between three and $`L-1`$ contains a zero-overlap edge. A decomposition into nonzero triangle invariants is unavailable for this family.

The Gram eigenvalues lie in $`[1-2c,1+2c]`$, so every value of $`\phi`$ is allowed while the Gram matrix remains uniformly positive definite. The phase can vary around the full circle even though the magnitude $`|B|=c^L`$ is exponentially small in $`L`$. Independent rephasing of the vector representatives leaves $`B`$ invariant; this is relational information in the source density operators, not the unobservable global phase of one supplied vector.

## 2. What one direct cycle-test shot measures

Define the left cyclic permutation on the $`L`$ data registers by

```math
C\bigl(|v_1\rangle\otimes\cdots\otimes|v_L\rangle\bigr)
=|v_2\rangle\otimes\cdots\otimes|v_L\rangle\otimes|v_1\rangle.
\tag{3}
```

On one independent copy of each labeled source,

```math
\langle\psi_1\otimes\cdots\otimes\psi_L|
C
|\psi_1\otimes\cdots\otimes\psi_L\rangle=B.
\tag{4}
```

A controlled-$`C`$ Hadamard test followed by an ancilla $`X`$ measurement produces a random variable in $`\{-1,+1\}`$ with mean $`\mathrm{Re}B`$. An ancilla $`Y`$ measurement has mean $`\mathrm{Im}B`$. Equivalently, an ancilla quadrature at a chosen angle $`t`$ has mean

```math
\mu_t=\mathrm{Re}(e^{-it}B)
=r\cos(\Phi-t),
\qquad r=|B|.
\tag{5}
```

One such shot consumes **$`L`$ source copies**. The cycle-test construction and its real/imaginary readout are established in Oszmaniec, Brod, and Galvao, [arXiv:2109.10006v1, Fig. 1](https://arxiv.org/pdf/2109.10006). The finite-shot phase estimates below follow directly from (5).

## 3. Raw shots needed for a phase estimate

Suppose a known lower bound $`r_*\leq r`$ is available. From the adjacent-overlap promise one may always use $`r_*=c^L`$; knowing the actual magnitude is unnecessary.

Take $`m`$ independent $`X`$ shots and $`m`$ independent $`Y`$ shots and denote their sample means by $`\widehat x`$ and $`\widehat y`$. For a mean of $`m`$ independent variables in $`\{-1,+1\}`$, Hoeffding's inequality gives

```math
\Pr[|\widehat x-\mathrm{Re}B|>a]
\leq2e^{-ma^2/2},
\tag{6}
```

and the same bound holds for $`\widehat y`$. Set

```math
a=\frac{r_*\sin\epsilon}{\sqrt2}.
```

If both component errors are at most $`a`$, then

```math
|\widehat x+i\widehat y-B|
\leq r_*\sin\epsilon\leq r\sin\epsilon.
\tag{7}
```

For $`0<\epsilon<\pi/2`$, the disk of radius $`r\sin\epsilon`$ about $`B`$ lies within angular distance $`\epsilon`$ of $`B`$ and does not contain the origin. This follows by drawing the two tangent lines from the origin to that disk, or by minimizing the distance to a ray of prescribed angle. Hence (7) implies that $`\arg(\widehat x+i\widehat y)`$ is an $`\epsilon`$-accurate circular phase estimate.

A union bound in (6) shows that failure probability at most $`\delta`$ is ensured by

```math
m\geq
\frac{4\log(4/\delta)}{r_*^2\sin^2\epsilon}.
\tag{8}
```

The number of **raw cycle-test shots** and the number of **total source copies** are therefore

```math
M_{\mathrm{cycle}}=2m
=O\!\left(\frac{\log(1/\delta)}{r_*^2\epsilon^2}\right),
\qquad
N_{\mathrm{cycle}}=L M_{\mathrm{cycle}}.
\tag{9}
```

On the ring, $`r=r_*=c^L`$. At fixed confidence this gives

```math
M_{\mathrm{cycle}}=O\!\left(c^{-2L}\epsilon^{-2}\right),
\qquad
N_{\mathrm{cycle}}=O\!\left(Lc^{-2L}\epsilon^{-2}\right).
\tag{10}
```

The extra factor $`L`$ in the second expression is essential when comparing with an algorithm whose resource count is total supplied copies.

### The visibility dependence is unavoidable for this direct-readout family

Here the comparator is specifically a sequence of fresh full-cycle Hadamard tests, retaining only each ancilla quadrature outcome. The quadrature angle may be chosen adaptively. This is a restricted measurement protocol, not the most general operation on the supplied copies.

For fixed $`0<r<1`$ and $`0<\epsilon\leq\pi/16`$, compare phases zero and $`h=4\epsilon`$. A quadrature outcome is Bernoulli with probability

```math
p_\phi(t)=\frac{1+r\cos(\phi-t)}2
```

for the outcome $`+1`$. For every chosen quadrature,

```math
|p_0(t)-p_h(t)|\leq\frac{r|h|}{2},
\qquad
p_h(t)(1-p_h(t))\geq\frac{1-r^2}{4}.
\tag{11}
```

The elementary Bernoulli relative-entropy bound

```math
D_{\mathrm{KL}}(\mathrm{Ber}(p)\|\mathrm{Ber}(q))
\leq\frac{(p-q)^2}{q(1-q)}
```

therefore bounds the information in one shot by $`r^2h^2/(1-r^2)`$. The chain rule gives the same per-shot bound conditionally on any previous transcript, so adaptive quadrature selection does not change it. With at most $`M`$ shots, the transcript relative entropy is at most $`Mr^2h^2/(1-r^2)`$.

Success at least $`2/3`$ in estimating each phase to error $`\epsilon`$ implies binary discrimination success at least $`2/3`$, by the disjoint-interval argument in [the lower-bound proof](lower-bound.md). The two transcript distributions must therefore have total variation distance at least $`1/3`$. Pinsker's inequality, with natural logarithms, requires relative entropy at least $`2/9`$. Thus

```math
M\geq\frac{1-r^2}{72r^2\epsilon^2}.
\tag{12}
```

For the ring in (1), $`r=c^L\leq1/256`$, so $`1-r^2`$ is bounded below by a constant. Equations (8) and (12) establish the precise fixed-confidence scaling

```math
\boxed{
M_{\mathrm{cycle}}=\Theta(c^{-2L}\epsilon^{-2}),
\qquad
N_{\mathrm{cycle}}=\Theta(Lc^{-2L}\epsilon^{-2})
}
\tag{13}
```

for this direct-readout family. Access to other measurements, retained data registers, or collective processing of many runs is outside this restricted lower bound.

## 4. Coherent transport removes the full-cycle visibility factor

For adjacent source projectors $`P_j`$ and $`P_{j+1}`$, the canonical local operation is

```math
T_j=\mathrm{sign}(P_j+P_{j+1}-I).
```

It obeys

```math
T_j|\psi_j\rangle
=\frac{\langle\psi_{j+1}|\psi_j\rangle}
{|\langle\psi_{j+1}|\psi_j\rangle|}
|\psi_{j+1}\rangle.
\tag{14}
```

The loop $`W=T_L\cdots T_1`$ therefore satisfies

```math
W|\psi_1\rangle=e^{-i\Phi}|\psi_1\rangle.
\tag{15}
```

The loop eigenvalue has unit magnitude. The small local overlaps enter the cost of implementing each transport, rather than multiplying into the readout visibility. The [transport construction](transport.md), [algorithm](algorithm.md), and [resource accounting](resources.md) show how copies implement these controlled operations with total cost

```math
N_{\mathrm{transport}}
=\widetilde O\!\left(\frac{L^2}{c^2\epsilon^2}\right).
\tag{16}
```

The matching lower bound applies to this same sparse-ring family and to arbitrary protocols in the copy model. Exponentially small $`|B|`$ consequently does not imply an exponentially large number of copies for estimating its phase.

### Illustrative scaling factors

For $`c=1/4`$, the following table compares the factors multiplying $`\epsilon^{-2}`$ in the two copy scalings. These are asymptotic factors, **not predicted experimental copy counts**: constants and the transport algorithm's logarithmic factors are omitted.

| Number of sources $`L`$ | Full-cycle magnitude $`c^L`$ | Direct cycle factor $`Lc^{-2L}`$ | Transport factor $`L^2/c^2`$ |
|---:|---:|---:|---:|
| 4 | $`1/256`$ | $`262\,144`$ | $`256`$ |
| 8 | $`1/65\,536`$ | $`34\,359\,738\,368`$ | $`1\,024`$ |
| 16 | $`1/4\,294\,967\,296`$ | approximately $`2.95\times10^{20}`$ | $`4\,096`$ |

## 5. Operational comparison and literature context

Both procedures above are quantum protocols. Their difference is how they process the same supplied quantum data. Direct cycle readout uses a full-cycle permutation and measures a small expectation value. The transport algorithm uses long coherent sequences of controlled partial swaps and polynomial transformations to normalize each local transfer before reading a loop eigenphase. It requires those known controlled operations on accessible quantum registers; independent source copies alone do not provide them as free black-box gates.

The comparison does not establish a general classical-versus-quantum separation, nor a lower bound for every protocol that might be called incoherent. It also does not claim that the transport circuit can be implemented using passive optics when the relevant photon internal degrees of freedom cannot be manipulated.

The ring obstruction appears explicitly in Kotowski et al., [*Characterizing Photonic Partial Distinguishability Through Gram-Matrix Tomography*, arXiv:2610.06736v1](https://arxiv.org/pdf/2610.06736), Section V and Fig. 6. Their circle-dance example has zero non-neighbor overlaps and a full-cycle invariant that decays exponentially. Their polynomial reconstruction guarantees require appropriate lower bounds on the magnitudes of the invariants used, while their physical access consists of spatial-mode interference and photon counting with unresolved internal states. The present copy-model calculation addresses phase estimation with more general controlled register operations and should be compared on that basis.
