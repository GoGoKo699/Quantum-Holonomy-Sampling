# A finite copy lower bound

This note proves a lower bound for estimating the phase of a cyclic product of pure-state overlaps. The proof allows arbitrary quantum memory, collective measurements, and adaptive choices of which labeled source to sample. It counts every independent state copy supplied by those sources.

The phase convention throughout is

```math
B=\prod_{j=1}^{L}\langle\psi_j|\psi_{j+1}\rangle,
\qquad
\Phi=\arg B\pmod{2\pi},
\qquad
\psi_{L+1}=\psi_1.
```

For real angles, write

```math
d_{\mathrm{circ}}(x,y)
=\min_{k\in\mathbb Z}|x-y+2\pi k|.
```

## Theorem

Fix an integer $`L\geq4`$, a register dimension $`d\geq L`$, and parameters

```math
0\lt c\leq\frac14,
\qquad
0\lt \epsilon\leq\frac{\pi}{16}.
```

Suppose an algorithm receives independent copies from $`L`$ labeled, unknown, pure-state sources. Each requested label is a classical choice, which may depend on all previous measurement outcomes. The algorithm may otherwise use arbitrary known operations, ancillas, quantum memory, randomness, and collective measurements. Its total number of source copies is capped by $`N`$ on every run.

Assume that, for every source tuple satisfying

```math
|\langle\psi_j|\psi_{j+1}\rangle|\geq c
\quad\text{for every }j,
```

the algorithm outputs an angle $`\widehat\Phi`$ with

```math
\Pr\!\left[
d_{\mathrm{circ}}(\widehat\Phi,\Phi)\leq\epsilon
\right]\geq\frac23.
```

Then

```math
\boxed{
N\geq
\frac{(1-2c)L^2}{144c^2\epsilon^2}
\geq
\frac{L^2}{288c^2\epsilon^2}.
}
```

The hard instances have adjacent overlap magnitude exactly $`c`$, all other off-diagonal overlaps zero, and Gram-matrix eigenvalues in $`[1-2c,1+2c]`$. In particular, the bound does not depend on an ill-conditioned or nearly singular Gram matrix.

## 1. A normalized family of sources

Work first in $`\mathbb C^L`$ with the fixed computational basis $`|1\rangle,\ldots,|L\rangle`$. Define the known cyclic shift by

```math
S|j\rangle=|j+1\rangle\quad(1\leq j\lt L),
\qquad
S|L\rangle=|1\rangle.
```

For a real parameter $`\phi`$, set

```math
G_\phi
=I+c\left(e^{-i\phi/L}S+e^{i\phi/L}S^\dagger\right),
\qquad
|\psi_j(\phi)\rangle=G_\phi^{1/2}|j\rangle.
\qquad\text{(1)}
```

The square root is the positive square root in this fixed basis. Since the eigenvalues of $`S`$ lie on the unit circle,

```math
(1-2c)I\preceq G_\phi\preceq(1+2c)I.
\qquad\text{(2)}
```

Thus $`G_\phi`$ is positive definite for every $`\phi`$ in the theorem's range. Its diagonal entries equal one, so each source vector is normalized:

```math
\langle\psi_j(\phi)|\psi_j(\phi)\rangle
=\langle j|G_\phi|j\rangle=1.
\qquad\text{(3)}
```

The Gram matrix of these vectors is exactly $`G_\phi`$:

```math
\langle\psi_j(\phi)|\psi_k(\phi)\rangle
=\langle j|G_\phi|k\rangle.
\qquad\text{(4)}
```

With the specified orientation of $`S`$, the forward adjacent entries, including the closing entry, are

```math
\langle\psi_j(\phi)|\psi_{j+1}(\phi)\rangle
=c e^{i\phi/L}
\qquad(1\leq j\leq L),
\qquad\text{(5)}
```

where the index is cyclic. Therefore

```math
B(\phi)=c^L e^{i\phi},
\qquad
\Phi(\phi)=\phi\pmod{2\pi}.
\qquad\text{(6)}
```

This sign follows from the fact that the matrix element $`\langle j|S^\dagger|j+1\rangle`$ is one. Reversing the definition of the shift or the cyclic product reverses the phase; neither reversal is made here.

For $`d\gt L`$, embed these vectors into any fixed $`L`$-dimensional subspace of the register. Their norms, overlaps, and distinguishability remain unchanged.

## 2. Cyclic covariance removes the advantage of adaptive label choices

Every $`G_\phi`$ commutes with $`S`$, and so does its positive square root. Consequently,

```math
|\psi_j(\phi)\rangle
=S^{j-1}|\psi_1(\phi)\rangle.
\qquad\text{(7)}
```

Consider an arbitrary algorithm in the theorem. Supply its simulator with $`N`$ independent copies of $`|\psi_1(\phi)\rangle`$ in advance. When the algorithm requests a copy with label $`j`$, the simulator takes one unused copy and applies the known unitary $`S^{j-1}`$. Equation (7) produces exactly the requested state. The simulator then continues the algorithm's operations and measurements.

This construction works when labels depend on previous outcomes: it follows the same classical decision rule and applies the corresponding known shift. Any unused copies are discarded if the algorithm stops early. All randomness and all measurement records can be included in a single quantum channel. Thus there is a parameter-independent completely positive, trace-preserving map $`\mathcal A`$ such that the algorithm's final output on this family is

```math
\mathcal A\!\left(P_\phi^{\otimes N}\right),
\qquad
P_\phi=|\psi_1(\phi)\rangle\langle\psi_1(\phi)|.
\qquad\text{(8)}
```

The simulator does not need to know $`\phi`$. The known shifts are independent of the parameter. Equation (8) is why neither adaptive source selection nor arbitrary collective processing evades the bound below.

## 3. Each supplied copy changes slowly with the target phase

The family $`G_\phi`$ has a common Fourier eigenbasis. Its derivative therefore commutes with $`G_\phi`$, and scalar differentiation in that basis gives

```math
\frac{d}{d\phi}G_\phi^{1/2}
=\frac12G_\phi^{-1/2}G_\phi'.
\qquad\text{(9)}
```

Direct differentiation of (1) yields

```math
G_\phi'
=\frac{c}{L}
\left(-i e^{-i\phi/L}S+i e^{i\phi/L}S^\dagger\right),
\qquad
\|G_\phi'\|\leq\frac{2c}{L}.
\qquad\text{(10)}
```

Here and below, the norm of an operator without a subscript is its operator norm. Combining (2), (9), and (10),

```math
\left\|\frac{d}{d\phi}G_\phi^{1/2}\right\|
\leq\frac{c}{L\sqrt{1-2c}},
\qquad
\left\|\frac{d}{d\phi}|\psi_1(\phi)\rangle\right\|
\leq\frac{c}{L\sqrt{1-2c}}.
\qquad\text{(11)}
```

Integrating along an interval of length $`h`$ gives

```math
\bigl\||\psi_1(\phi+h)\rangle-|\psi_1(\phi)\rangle\bigr\|
\leq\frac{|h|c}{L\sqrt{1-2c}}.
\qquad\text{(12)}
```

For normalized vectors $`|u\rangle,|v\rangle`$,

```math
1-|\langle u|v\rangle|^2
\leq\bigl\||u\rangle-|v\rangle\bigr\|^2.
\qquad\text{(13)}
```

Indeed, subtracting the left side from the right side gives $`|1-\langle u|v\rangle|^2\geq0`$. It follows that the single-copy squared fidelity obeys

```math
f(\phi,h)
:=|\langle\psi_1(\phi)|\psi_1(\phi+h)\rangle|^2
\geq1-\frac{h^2c^2}{L^2(1-2c)}.
\qquad\text{(14)}
```

This is a finite-distance bound. No asymptotic unbiasedness assumption, differentiability of the estimator, or quantum Fisher information approximation is used.

## 4. Phase estimation implies binary discrimination

Choose the two parameters

```math
\phi_0=0,
\qquad
\phi_1=4\epsilon.
\qquad\text{(15)}
```

Their circular distance is $`4\epsilon`$, because $`4\epsilon\leq\pi/4`$. The circular balls of radius $`\epsilon`$ around the two target phases are disjoint.

Turn the hypothesized estimator into a binary test: output hypothesis zero when its estimate lies within circular distance $`\epsilon`$ of zero, and output hypothesis one otherwise. On the first source tuple it succeeds with probability at least $`2/3`$. On the second tuple every $`\epsilon`$-accurate estimate lies outside the first ball, so it also succeeds with probability at least $`2/3`$.

For equal prior probabilities, binary discrimination of density operators $`\rho`$ and $`\sigma`$ has optimal success probability

```math
p_{\mathrm{succ}}^*
=\frac{1+D(\rho,\sigma)}{2},
\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\qquad\text{(16)}
```

For completeness, if the first outcome of a binary measurement is represented by $`0\preceq M\preceq I`$, its success probability is $`1/2+\mathrm{Tr}(M(\rho-\sigma))/2`$. The largest value of the trace term is the sum of positive eigenvalues of the trace-zero Hermitian matrix $`\rho-\sigma`$, namely $`\|\rho-\sigma\|_1/2`$. This proves (16).

Equation (8) means that the estimator and the subsequent binary decision together form a measurement on the $`N`$ iid input copies. Hence success at least $`2/3`$ requires

```math
D\!\left(P_{\phi_0}^{\otimes N},P_{\phi_1}^{\otimes N}\right)
\geq\frac13.
\qquad\text{(17)}
```

## 5. Tensor powers give the announced constant

The difference of two pure-state density operators has nonzero eigenvalues $`\pm\sqrt{1-|\langle u|v\rangle|^2}`$. Applying this identity to the two tensor powers gives

```math
D\!\left(P_{\phi_0}^{\otimes N},P_{\phi_1}^{\otimes N}\right)
=\sqrt{1-f^N},
\qquad
f=f(0,4\epsilon).
\qquad\text{(18)}
```

For $`0\leq f\leq1`$, the identity $`1-f^N=(1-f)\sum_{k=0}^{N-1}f^k`$ implies $`1-f^N\leq N(1-f)`$. Equation (14) therefore yields

```math
D\!\left(P_{\phi_0}^{\otimes N},P_{\phi_1}^{\otimes N}\right)
\leq
\sqrt{
\frac{16Nc^2\epsilon^2}{L^2(1-2c)}
}.
\qquad\text{(19)}
```

Combining (17) and (19) proves

```math
N\geq\frac{(1-2c)L^2}{144c^2\epsilon^2}.
\qquad\text{(20)}
```

Finally, $`c\leq1/4`$ implies $`1-2c\geq1/2`$, giving the second inequality in the theorem.

## Gauge choice and endpoints

### Moving the edge phases does not change the source states

The equally distributed phase in (5) is a convenient Gram-matrix gauge. Replacing the representative vectors by

```math
|\widetilde\psi_j(\phi)\rangle
=e^{-i(j-1)\phi/L}|\psi_j(\phi)\rangle
\qquad\text{(21)}
```

leaves every density operator unchanged. In this representation the first $`L-1`$ forward overlaps equal the positive number $`c`$, while the closing overlap equals $`c e^{i\phi}`$. Their product remains $`c^L e^{i\phi}`$.

Equation (21) is only a choice of vector representatives; it is not a parameter-dependent operation supplied to the algorithm. Likewise, the construction in (1) uses the positive square root in a fixed basis. Taking the positive square root of a differently gauged Gram matrix would generally also change the embedding by a parameter-dependent common unitary, so that alternative family must not be substituted silently in the distinguishability argument.

### The smallest allowed loop

At $`L=4`$, the two neighbors of each vertex are distinct. The nonzero off-diagonal entries in (1) are exactly the four ring edges and their conjugates; opposite vertices are orthogonal. There is no double counting of an edge, and all triangles of distinct labels have zero overlap product. Equations (2)–(20) apply without modification.

### Small overlap

As $`c`$ decreases toward zero, the normalized sources approach orthogonal basis states while their Gram spectrum approaches one. The phase remains well-defined for every positive $`c`$, but its imprint on each source becomes proportional to $`c/L`$, as (11) quantifies. The factor $`c^{-2}`$ in the lower bound therefore reflects weak statistical information, not loss of normalization or spectral conditioning. At $`c=0`$ the cyclic product vanishes and its phase is undefined, which is why zero is excluded.

### Scope of optimality

Together with the copy upper bound in [the algorithm](algorithm.md) and [resource accounting](resources.md), this proves optimality up to logarithmic factors in the stated regime. The theorem counts a worst-case cap on supplied copies; an expected stopping-time formulation is a different statement. It also does not assert the same uniform lower bound as $`c`$ tends to one. In particular, at $`c=1`$ all adjacent rays coincide and the cyclic phase is zero.
