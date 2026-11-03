# Copy-optimal phase estimation and coherent runs

For a sparse four-state cycle at fixed small phase accuracy, the unrestricted copy complexity is $`\Theta(c^{-2})`$. In a sufficient large-dimension regime, attaining that copy order requires a coherent run consuming $`\Omega(c^{-2})`$ copies. A run may stream program specimens and discard them after use; its size counts all copies consumed before the entire input-dependent quantum state is reset.

The proof has two distinct components. The [phase-block information bound](block-information.md) is specific to the loop phase. A fixed-source Haar comparison, inherited from the method developed in [Quantum Fidelity Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence/blob/2fcb88fd734f0235ab83fe2ce628bf8b99c85118/science/haar_comparison.md), controls the information that classical history can retain about a single stationary source orientation. The root-fidelity resource law itself is not used as a phase theorem.

## 1. Complete-reset consumed-copy model

Use the [labeled pure-state source interface](model.md), with four stationary sources and the sparse family

```math
G_\phi=I+c\left(e^{-i\phi/4}S+e^{i\phi/4}S^\dagger\right),
\qquad
|\psi_j(\phi)\rangle=G_\phi^{1/2}|j\rangle,
\qquad 0\lt c\le\frac14.
\qquad\text{(1)}
```

Embed these states in $`\mathbb C^d`$ and apply one unknown $`U\in\mathrm U(d)`$ to all four sources. The sources remain fixed for the whole experiment. Copies are independent conditional on this tuple. Their adjacent overlap amplitudes are $`c`$, their opposite overlaps vanish, and their loop phase is $`\phi`$.

The receiver obeys two worst-case caps:

- $`N`$ is the total number of source copies consumed on every execution history.
- $`b`$ is the number consumed within any one coherent run, including copies already measured or discarded during that run.

At a run boundary, all retained input-dependent information is classical history. Conditional on that full history, the joint state of all retained quantum systems and reserved ancillary aids must be known independently of the unknown sources. Known individual marginals do not suffice when unknown conditional correlations remain. No specimen, unknown program or input-dependent quantum memory may cross a boundary; known joint entangled ancillas may be recreated from the history. Source labels, measurements, stopping and known operations may depend arbitrarily on the classical history. Within a run, arbitrary allowed quantum processing and intermediate measurements are permitted.

This is a complete-reset restriction on consumed copies. It is not a bound on live qubits or on circuit depth. Discarding a program copy while retaining a coherent target does not complete a reset. Conversely, retaining an unbounded classical tomography record between one-copy measurements is allowed.

For the lower bound, average $`U`$ once under Haar measure. This is a prior over legal fixed inputs, not a physical change to the sources. Let $`P_\phi`$ denote the resulting complete classical transcript law. Any estimator succeeding for every legal tuple also succeeds under each such prior.

## 2. Finite adaptive transcript theorem

**Theorem.** In the complete-reset model above, put $`\beta=\min\{b,N\}`$. For positive integer caps, $`d\ge32N`$, and arbitrary phases $`\phi,\theta`$,

```math
\begin{aligned}
\mathrm{TV}(P_\phi,P_\theta)
&\le
\sqrt{\frac{32768}{3}}\,
c^4\sqrt{N\beta^3}\,e^{16\beta c^2}
+\frac{768N^2}{d}\\
&\le
\sqrt{\frac{32768}{3}}\,
c^4\sqrt{Nb^3}\,e^{16bc^2}
+\frac{768N^2}{d}.
\end{aligned}
\qquad\text{(2)}
```

Total variation uses $`\mathrm{TV}(P,Q)=\tfrac12\|P-Q\|_1`$. The theorem includes adaptive source allocation within and between runs, random stopping under the worst-case cap, and arbitrary classical computation. Its phase dependence comes from the uniform stock divergence in [Block information](block-information.md#4-information-bound-uniform-in-stock-size).

### Padding adaptive requests by a fixed stock

Concatenate whole original runs until at least $`\beta`$ copies have been consumed or the protocol terminates. Since each original run consumes at most $`\beta`$, each resulting nonempty superblock consumes fewer than $`2\beta`$ copies. The number of superblocks is at most

```math
R=\lceil N/\beta\rceil\le2N/\beta.
```

Give each superblock $`2\beta`$ copies of each of the four labels in advance, in a known order. Its stock has

```math
t=8\beta,
\qquad
M=tR\le16N
\qquad\text{(3)}
```

padded copies across the experiment. Every adaptive request can be answered from an unused register of the required label; at most $`2\beta`$ requests occur in that superblock. Unused copies are discarded, and dummy superblocks are appended after early termination. This is a comparison construction: it does not assert that the physical protocol paid for unused padding.

The reset boundaries internal to a superblock are part of its instrument. At the next superblock boundary, the retained input-dependent state is still classical. Thus each stock undergoes a history-dependent POVM with a known initial ancilla state, exactly the interface needed below.

### Fixed orientation versus independently refreshed stocks

Let $`Q_\phi`$ be the transcript law of the auxiliary experiment in which each padded stock has its own independently sampled common Haar orientation. All copies and labels within that stock retain the same Gram matrix (1). The following comparison does not assume that these two experiments are identical:

```math
\mathrm{TV}(P_\phi,Q_\phi)
\le\frac{3M^2}{2d}
\le\frac{384N^2}{d},
\qquad M\le d/2.
\qquad\text{(4)}
```

For clarity, the generic comparison applies to any fixed normalized stock vector $`v_\phi`$ appearing as $`U^{\otimes t}v_\phi`$; the copies need not come from independent Haar-distributed species. After rank-one refinement of each conditional POVM, the likelihood amplitude at a fixed transcript leaf is holomorphic homogeneous of degree $`t`$ in the entries of $`U`$. Its coefficients may depend on the specified previous classical history. Multiplying these unnormalized amplitudes is legitimate even when normalized conditional quantum states are not polynomial functions of $`U`$.

The Haar/Gaussian homogeneous norm comparison and the Gaussian product inequality give the pointwise domination

```math
P_\phi(\mathrm{leaf})
\ge\kappa Q_\phi(\mathrm{leaf}),
\qquad
\kappa=\frac{(d)_{\downarrow t}^{\,R}}{(d)_{\uparrow M}},
\qquad\text{(5)}
```

where $`(d)_{\downarrow t}=d(d-1)\cdots(d-t+1)`$ and $`(d)_{\uparrow M}=d(d+1)\cdots(d+M-1)`$. For $`M\le d/2`$, the elementary product bounds give $`1-\kappa\le3M^2/(2d)`$. Pointwise domination between normalized laws then implies (4). A measurable rank-one refinement covers general standard-Borel outcomes.

The full generic proof, including the homogeneous inequalities and outcome refinement, is the authoritative [fixed-source comparison in Quantum Fidelity Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence/blob/2fcb88fd734f0235ab83fe2ce628bf8b99c85118/science/haar_comparison.md). The transfer here changes the stock vector to correlated four-state columns with prescribed Gram matrix and uses the four-source padding (3). No step assumes that independent orientation refreshes occur in the actual experiment. The condition $`d\ge32N`$ ensures $`M\le d/2`$.

### Phase information in each refreshed stock

In the auxiliary experiment the next stock is independent of all previous history. The [uniform phase-specific block bound](block-information.md#4-information-bound-uniform-in-stock-size), evaluated at $`t=8\beta`$, gives

```math
D(\omega_\phi\|\omega_\theta)
\le\frac{32768}{3}\beta^4c^8e^{32\beta c^2}.
\qquad\text{(6)}
```

Condition on the same earlier history under the two hypotheses. The receiver's POVM at that history is the same known instrument. Quantum-to-classical data processing bounds its conditional output divergence by (6). The classical relative-entropy chain rule and $`R\le2N/\beta`$ therefore imply

```math
D(Q_\phi\|Q_\theta)
\le\frac{65536}{3}N\beta^3c^8e^{32\beta c^2}.
\qquad\text{(7)}
```

Pinsker's inequality, $`\mathrm{TV}(Q_\phi,Q_\theta)\le\sqrt{D(Q_\phi\|Q_\theta)/2}`$, bounds the refreshed-phase comparison. The triangle inequality pays (4) once for each hypothesis. This proves (2).

The fixed-source comparison is essential: applying the chain rule directly to independently twirled runs would remove the orientation information in their common classical history without a bound on the error. The stock information theorem and (4) justify exactly that step.

## 3. Copy-optimality forces a long consumed-copy run

Fix $`0\lt\epsilon\le\pi/16`$, independent of $`c`$. Suppose the receiver estimates the four-state phase within circular error $`\epsilon`$, with probability at least $`2/3`$ for every legal source tuple. Let $`C_0\ge1`$ and suppose

```math
N\le C_0c^{-2},
\qquad
d\ge9216C_0^2c^{-4}.
\qquad\text{(8)}
```

Then necessarily

```math
\boxed{\displaystyle
b\ge\frac{c^{-2}}{128C_0^{1/3}}.}
\qquad\text{(9)}
```

To prove this, choose phases $`\phi_0=0`$ and $`\phi_1=4\epsilon`$. Their circular $`\epsilon`$-balls are disjoint. Mapping an estimate inside the first ball to hypothesis zero and every other estimate to hypothesis one produces a binary test with success at least $`2/3`$ under either Haar prior. Thus

```math
\mathrm{TV}(P_{\phi_0},P_{\phi_1})\ge\frac13.
\qquad\text{(10)}
```

Condition (8) implies $`d\ge32N`$ and makes the dimension correction in (2) at most $`1/12`$. If (9) were false, put $`y=bc^2\lt1/(128C_0^{1/3})`$. The first term of (2) would be at most

```math
\sqrt{\frac{32768}{3}C_0y^3e^{32y}}
\lt\sqrt{\frac{e^{1/4}}{192}}
\lt0.082.
```

Together with $`1/12`$, this is strictly less than $`1/3`$, contradicting (10). The numerical constants are conservative sufficient bounds; optimizing them is not needed for the scaling statement.

### Matching sufficient run size

At $`L=4`$ and fixed $`\epsilon`$, the existing [coherent algorithm](algorithm.md) consumes $`N=O_\epsilon(c^{-2})`$ copies. There is no hidden $`\log(1/c)`$ in this copy count: its Fourier grid, number of transports and local error tolerance depend only on $`L,\epsilon`$; the polar degree is $`O_\epsilon(c^{-1})`$, and the total consumed-copy budget is quadratic in that degree. Classical phase compilation and finite gate synthesis have their separately charged costs in [Resources](resources.md).

Execute the whole sample circuit in one run. It supplies the upper endpoint $`b=O_\epsilon(c^{-2})`$. Program copies may be streamed and discarded while the target and phase workspace remain coherent. Therefore, in the sufficient large-dimension regime (8), the consumed-copy run threshold for copy-optimal weak-overlap phase estimation is

```math
b=\Theta_\epsilon(c^{-2}),
\qquad N=O_\epsilon(c^{-2}).
\qquad\text{(11)}
```

This is a sharp endpoint in the run resource, not a matched formula for the full joint tradeoff in $`N,b,c,d,\epsilon`$. It imposes no matching lower bound on simultaneous quantum width. The streaming algorithm uses $`2\lceil\log_2d\rceil+O(\log(1/\epsilon))`$ live qubits.

## 4. Fixed run caps and the four-copy exponent

For any fixed $`b`$, (2) gives an $`\Omega_b(c^{-8})`$ consumed-copy lower bound when $`N^2/d`$ is sufficiently small. A finite-dimension version avoids an implicit condition on $`N`$. For $`c\le1/4`$, define

```math
K_b=\sqrt{\frac{32768b^3}{3}}e^b,
\qquad
a_b=\min\left\{\frac1{36K_b^2},\frac1{96},\frac1{32}\right\}.
```

Then every successful estimator in the model satisfies

```math
N\ge a_b\min\{c^{-8},\sqrt d\}.
\qquad\text{(12)}
```

Indeed, if $`N`$ were smaller than the right side and positive, then $`d\ge32N`$ and (2) would be at most $`K_bc^4\sqrt N+768N^2/d\lt1/6+1/12\lt1/3`$. If the right side is at most one, the integer copy cap makes the same lower statement immediate for a nontrivial estimator.

For fixed $`b\ge4`$, ordinary real and imaginary four-cycle tests fit within one run and give the matching $`O_\epsilon(c^{-8})`$ copy upper bound at fixed accuracy. The [optimal four-copy calculation](block-information.md#3-exact-optimal-four-copy-information) confirms that this exponent persists even after optimizing the invariant four-copy measurement. No matching upper bound is asserted here for run caps below four.

## 5. Why the dimension qualification is necessary

At every fixed finite $`d`$, separate-copy tomography gives a counterexample to an unqualified long-run necessity statement. It estimates all four pure rays with $`b=1`$ using $`O_d(c^{-2}\epsilon^{-2})`$ copies, then computes the loop phase from the classical reconstruction. The constants can depend strongly on dimension.

Here is an explicit conservative construction. For each source, estimate the probabilities of the $`d^2`$ rank-one tests

```math
|a\rangle,\qquad
\frac{|a\rangle+|b\rangle}{\sqrt2},\qquad
\frac{|a\rangle+i|b\rangle}{\sqrt2},
\qquad a\lt b.
```

Each test uses one fresh copy and leaves only a classical outcome. If every probability estimate has error at most $`\zeta`$, the reconstructed Hermitian matrix $`A`$ obeys $`\|A-P\|_{\mathrm{op}}\le\|A-P\|_F\le3d\zeta`$. Put $`\eta_T=c\epsilon/96`$ and $`\zeta=\eta_T/(3d)`$. Hoeffding's inequality and a union bound over the $`4d^2`$ tests make these bounds simultaneous with probability at least $`2/3`$ using

```math
O\!\left(d^4c^{-2}\epsilon^{-2}\log(2d)\right)
\qquad\text{(13)}
```

copies, with no quantum information retained between copies.

Let $`v`$ be a normalized top eigenvector of $`A=P+E`$, with $`\|E\|\le\eta_T\lt1/4`$. Its eigenvalue is at least $`1-\eta_T`$. Projecting its eigenvector equation orthogonally to the true ray gives

```math
\|(I-P)v\|
\le\frac{\eta_T}{1-2\eta_T}\le2\eta_T.
```

After a representative phase choice used only in this analysis, $`v`$ is within vector distance $`3\eta_T=c\epsilon/32`$ of the true source vector. Set this distance to $`\delta_T`$. Each reconstructed adjacent overlap differs from its true value by at most $`2\delta_T`$. Since the true magnitude is at least $`c`$,

```math
\left|\arg\frac{\widehat z_j}{z_j}\right|
\le\arcsin(2\delta_T/c)
\le4\delta_T/c.
```

Summing the four argument errors gives at most $`16\delta_T/c=\epsilon/2`$. Vector gauges cancel around the loop, so the numerical algorithm never needs the unknown aligning phases from this proof. A finite output grid absorbs the remaining error margin.

This construction applies in particular at $`d=4`$, where the sparse family exists. It shows why (9) is a high-dimensional minimax statement: classical history can learn a finite-dimensional orientation from many short runs. The dimension condition in (8) suppresses that possibility at the copy-optimal budget.

## 6. Scientific scope and attribution

The decisive exchange with [Quantum Fidelity Coherence](https://github.com/GoGoKo699/Quantum-Fidelity-Coherence) is methodological. That project supplies the complete-reset accounting and the generic fixed-versus-refreshed Haar transcript comparison. This project owns the sparse-cycle phase information theorem and the resulting loop-phase run threshold. Its [block proof](block-information.md) supplies the new phase-dependent divergence, including the uniform control required when the run cap grows.

Replica hierarchies, optimal collective overlap measurements, Bargmann invariants and cycle tests are prior foundations, credited in [Related work](../references/related-work.md). Raw cycle visibility alone is not a converse for arbitrary block measurements. A root-fidelity copy/run formula is not a theorem for a four-state phase. The valid conclusion here uses the phase-specific Gram calculation, the fixed-source transcript comparison, and the complete-reset restriction together.
