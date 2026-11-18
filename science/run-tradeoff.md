# How the coherent-run limit changes the sample cost

Four weakly overlapping states carry a loop phase in their cyclic overlap product. In sufficiently large dimension, if a receiver can use only four copies before resetting, the optimal total copy cost scales as the inverse eighth power of the overlap. Larger coherent runs let the receiver measure a lower-variance observable. This account gives the attainable tradeoff, an explicit circuit, and the matching converse in the stated dimension regime.

## Model and theorem

Use the [labeled pure-state model](model.md) with four sources and $`0\lt c\le 1/4`$. The neighboring overlap amplitudes are at least $`c`$, and the target $`\Phi`$ is the argument of the cyclic product $`B`$. At a [complete reset](coherent-runs.md#1-complete-reset-consumed-copy-model), only the classical history retains information about the sources. Each run consumes at most $`b`$ specimens on every history, including specimens discarded within the run. Let $`N^*(d,c,b,\epsilon)`$ be the minimum worst-case total consumed copies for circular error $`0\lt\epsilon\le\pi/16`$ with probability at least $`2/3`$. The four source states are stationary. Their copies are independent, and no source-preparation unitaries are supplied.

For integer $`b\ge4`$, put

```math
T=\epsilon^{-2}\max\left\{c^{-2},\,c^{-8}b^{-3}\right\}.
\qquad\text{(1)}
```

There is a dimension-independent $`O(T)`$ protocol. The matching $`\Omega(T)`$ bound holds for $`4\le b\lt c^{-2}`$ and $`d\ge9216T^2`$, and for $`b\ge c^{-2}`$ and $`d\ge4`$. The constants in these order bounds are absolute. The short-run dimension condition is sufficient for the fixed-source comparison, and a sharp dimension threshold remains open. Run caps below four fall outside the matched theorem.

## A collective average of cycles

Take $`m`$ specimens per label, in four separately addressed banks. For a tuple $`a`$ of one address in each bank, let $`C_a`$ cycle the selected registers so that the old state from bank $`j+1`$ lands in bank $`j`$. Other registers are fixed. On the product input $`v`$, each $`C_a`$ has expectation $`B`$. Define

```math
A=\frac{1}{m^4}\sum_a C_a,\qquad
H=\frac{A+A^\dagger}{2},\qquad K=\frac{A-A^\dagger}{2i}.
\qquad\text{(2)}
```

Measure $`H`$ or $`K`$ spectrally, using a fresh bank for each outcome. Their means are the real and imaginary parts of $`B`$. Measuring the spectrum of this coherent average is the operation that reduces variance. Choosing a random tuple and recording its usual binary cycle-test outcome would still give a binary variable with variance near one when the invariant is small.

Let $`q_j=|\langle\psi_j|\psi_{j+1}\rangle|^2`$. For two independent uniform address tuples, compare their two permuted product states. Bank $`j`$ contributes overlap one if their selected addresses agree. Otherwise, at two slots the original and incoming states exchange roles in the bra and ket, contributing $`q_j`$. The inner product factors over the banks. Using inverse cycles replaces successor by predecessor and only reorders the resulting factors. Hence

```math
\begin{aligned}
\langle A^\dagger A\rangle
 &=\langle AA^\dagger\rangle
 =\prod_{j=1}^4\left(q_j+\frac{1-q_j}{m}\right),\\
\operatorname{Var}(H)+\operatorname{Var}(K)
 &=\prod_{j=1}^4\left(q_j+\frac{1-q_j}{m}\right)-|B|^2 .
\end{aligned}
\qquad\text{(3)}
```

In the second line, $`H^2+K^2=(A^\dagger A+AA^\dagger)/2`$. The identity applies to unequal overlaps, with arbitrary phases and no sparsity assumption.

Choose $`m`$ as the largest power of two at most $`\min\{\lfloor b/4\rfloor,c^{-2}\}`$. This is at least one, and $`4m\le b`$. After dividing (3) by $`|B|^2=\prod_jq_j`$, the relative variance sum is bounded by

```math
V_m=\left(1+\frac{1}{mc^2}\right)^4-1
\le \frac{15}{(mc^2)^4}.
\qquad\text{(4)}
```

The inequality uses $`mc^2\le1`$. Average $`r=\lceil192V_m/\epsilon^2\rceil`$ independent outcomes per quadrature. The expected squared complex error is at most $`|B|^2 V_m/r`$. Markov's inequality bounds the probability of complex error greater than $`\epsilon|B|/4`$ by $`1/12`$. Such relative complex error bounds the angular error: within a disk of radius $`a|B|`$ about $`B`$, the maximum argument error equals $`\arcsin a`$ for $`a\le1`$. The implementation below leaves room to round the final angle.

The deterministic total is $`8mr=O(\epsilon^{-2}c^{-8}/m^3)=O(T)`$. For a fixed cap below the crossover, more copies in each run reduce the number of runs faster than they increase the copies used in each run. At caps above the crossover it suffices to use order $`c^{-2}`$ copies per run.

## Finite-precision implementation

Write $`n=\lceil\log_2d\rceil`$. Prepare a uniform superposition over the four address registers and an orientation qubit. For tuple $`a`$, apply the Hermitian involution

```math
S_a=|0\rangle\langle1|\otimes C_a
    +|1\rangle\langle0|\otimes C_a^\dagger.
\qquad\text{(5)}
```

The address-controlled version $`S`$ is unitary and Hermitian. An orientation state $`|+\rangle`$ selects $`H`$ on compression to the prepared address and orientation state $`g`$. The state $`(|0\rangle-i|1\rangle)/\sqrt2`$ instead selects $`K`$. The switch of orientation in (5) is part of the operation.

For either quadrature, let $`\Pi=|g\rangle\langle g|\otimes I`$ and $`W=(2\Pi-I)S`$. If the compressed observable has eigenvector $`u`$ with eigenvalue $`\lambda`$, then $`v_u=|g\rangle u`$ and the component of $`Sv_u`$ orthogonal to $`\Pi`$ span a plane invariant under $`W`$. For $`|\lambda|\lt1`$, the latter component has norm $`\sqrt{1-\lambda^2}`$. In the resulting orthonormal basis the matrix is

```math
\begin{pmatrix}\lambda & \sqrt{1-\lambda^2}\\
-\sqrt{1-\lambda^2} & \lambda\end{pmatrix}.
\qquad\text{(6)}
```

Both eigenphases have cosine $`\lambda`$. At $`\lambda=\pm1`$, $`v_u`$ itself has eigenvalue $`\lambda`$ under $`W`$. Thus phase estimation followed by taking a cosine approximates a spectral measurement of the desired quadrature.

To implement (5), route each selected register to slot zero by an addressed swap. For every nonzero slot, compute its address-equality flag, apply the flagged register swap, and uncompute the flag. Apply the cycle or inverse on the four routed registers according to the orientation, flip orientation, and reverse the routing. This uses gates on the available specimen registers and known ancillas. There is no external address oracle. Including the reflection, one controlled $`W`$ uses $`O(m(n+\log m+1))`$ gates and a reusable $`O(\log m+1)`$ routing workspace. The controlled reflection implements the sign in (6), including the overall phase relative to the inactive control.

Put $`\delta=\epsilon c^4/20`$. A Fourier phase-estimation grid with $`M=O(1/\delta)`$ points, rounded up to a power of two, suffices to approximate the eigenphase cosine within $`\delta`$ with probability at least $`5/6`$ after allocating part of the accuracy to numerical cosine evaluation. Indeed, at circular distance $`u/M`$ from the true phase in turns, the squared Fourier amplitude is bounded by $`1/(4u^2)`$ for $`u\le M/2`$. There are at most two grid points per distance bin. Discarding the tail beyond eight bins incurs probability less than $`1/6`$, and cosine is $`2\pi`$-Lipschitz in turns. A constant multiple of $`1/\delta`$ in the grid size pays both discretization and evaluation error.

Repeat phase estimation $`O(\log(2r))`$ times within the same run, using fresh phase bits and returning the median of the cosines. This reuses the same address, orientation and specimen bank. Each phase-readout Kraus operator is a function of $`W`$. The joint classical probabilities are the mixture obtained by first drawing one eigenphase from the original spectral distribution, then applying independent phase readouts to that eigenphase. This gives a per-run error probability at most $`1/(24r)`$, without multiplying the specimen cost. It also provides a coupling to the exact spectral outcome within $`\delta`$. All $`2r`$ outcomes satisfy this error bound simultaneously with failure probability at most $`1/12`$. Their complex mean error due to digitization is at most $`\sqrt2\delta`$. Together with the statistical error, this is less than $`\epsilon|B|/2`$. Returning a nearest point on a circular grid with angular mesh at most $`\epsilon/4`$ stays within $`\epsilon`$ on the good event.

Per sample there are $`O(\delta^{-1}\log(2r))`$ controlled walks and $`O(\log^2(1/\delta)\log(2r))`$ Fourier gates. Live quantum width is $`O(mn+\log m+\log(1/\delta))`$. Multiply the per-sample gate count by $`2r`$ to obtain the full cost. In a finite universal gate set, approximate the ideal sequence of $`G`$ gates to operator error at most $`1/(24G)`$ per gate. A hybrid bound gives at most $`1/24`$ change in full-experiment total variation, with polylogarithmic gate synthesis overhead. The three failure budgets together are below $`1/3`$. Classical arithmetic can approximate the quadrature sums and central phase to within the stated digitization and final-grid margins. These width and gate costs apply to this collective circuit. The [streaming transport circuit](resources.md) uses less simultaneous width at the copy-optimal endpoint for fixed accuracy.

## Matching adaptive converse

Use the [sparse four-cycle family](coherent-runs.md#1-complete-reset-consumed-copy-model), embedded at one fixed unknown common Haar orientation. Two phases $`\phi,\theta`$ with separation $`h=4\epsilon`$ have disjoint $`\epsilon`$-balls. A successful estimator therefore gives transcript total variation at least $`1/3`$ between the two phase priors.

The [stock Gram calculation](block-information.md#4-information-bound-uniform-in-stock-size) gives entries of the form $`c^k e^{iw\phi}`$, with at most $`\binom tk2^k`$ entries per row at changed-site count $`k`$ for a stock of $`t`$ specimens. Nonzero winding has $`k\ge4`$ and $`|w|\le k/4`$. Use the phase difference rather than a uniform bound of two on the amplitude difference:

```math
\left|e^{iw\phi}-e^{iw\theta}\right|^2
\le h^2(k/4)^2,
\qquad
\frac{(k/4)^2}{k!}\le\frac{1}{24(k-4)!}.
\qquad\text{(7)}
```

The second inequality follows from $`(k-1)(k-2)(k-3)\ge3k/2`$ for $`k\ge4`$. With $`x=2tc^2`$, the normalized squared Hilbert–Schmidt difference of the fixed-type Gram matrices is at most $`h^2x^4 e^x/24`$. The existing minimum-eigenvalue estimate $`e^{-2tc^2}`$ and the Petz order-two comparison then give the uniform stock bound

```math
D(\omega_\phi\|\omega_\theta)
\le\frac23 h^2 t^4 c^8 e^{4tc^2}.
\qquad\text{(8)}
```

Apply the [fixed-source transcript transfer](coherent-runs.md#2-finite-adaptive-transcript-theorem). For $`\beta=\min\{b,N\}`$, it compares with at most $`2N/\beta`$ refreshed stocks of $`t=8\beta`$ specimens. Conditional data processing and Pinsker's inequality bound the refreshed experiment. The cost of changing from a single physical orientation to the refreshed auxiliary experiment is paid once for each phase prior. For $`d\ge32N`$, this yields

```math
\mathrm{TV}(P_\phi,P_\theta)
\le \sqrt{8192/3}\, h c^4\sqrt{N\beta^3}\,e^{16\beta c^2}
     +\frac{768N^2}{d}.
\qquad\text{(9)}
```

When $`b\lt c^{-2}`$, the exponential is bounded by an absolute constant, and $`T=\epsilon^{-2}c^{-8}b^{-3}`$. If $`N<T`$ and $`d\ge9216T^2`$, then $`d\ge32N`$ and the last term is at most $`1/12`$. With $`h=4\epsilon`$, reaching total variation $`1/3`$ therefore requires $`N=\Omega(T)`$. If $`N\ge T`$, the conclusion already holds. For $`b\ge c^{-2}`$, the [unrestricted sparse-cycle lower bound](lower-bound.md) gives $`\Omega(\epsilon^{-2}c^{-2})`$ at every $`d\ge4`$. This completes the stated minimax law.

The small-dimension regime can behave differently. At each fixed finite $`d`$, [separate-copy tomography](coherent-runs.md#5-why-the-dimension-qualification-is-necessary) attains overlap and accuracy exponents $`O_d(c^{-2}\epsilon^{-2})`$ with $`b=1`$. The new converse makes no simultaneous-width claim. Unknown mixed states, changing source orientations, passive-only optical access and preparation costs are outside the theorem.

## Attribution and reproduction

[Guţă and Butucea](../references/related-work.md#collective-four-bank-measurement) introduced quantum U-statistics based on symmetrized kernels. The cycle observable comes from prior multivariate-trace measurements. The four labeled banks give the exact second moment (3) and hence the relative-variance gain for weak phases. The companion project supplies the generic Haar transcript comparison. The winding refinement (7) and the use of the four-bank observable in the reset tradeoff are specific to this account.

The [verification guide](../verification/README.md) describes the finite variance, permutation and spectral-circuit checks. The analytical argument establishes the uniform scaling; finite experiments check the stated identities and implementation conventions.
