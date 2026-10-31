# Verification scope and resource audit

This directory checks the identities and coherent phase conventions used by the
holonomy argument. The checks are small deterministic calculations with NumPy
and SciPy. They include an actual state-vector phase-estimation readout and an
explicit consumed-program density-matrix-exponentiation (DME) circuit.

Requirements: Python 3.10 or newer and the packages in requirements.txt.

Run from the repository root:

~~~bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
~~~

The second command writes verification/results.json and exits with a nonzero
status if a check fails. The output records the random seed, package versions,
and the SHA-256 digest of the checked script. Randomly generated test inputs are
reproducible from the fixed seed. Last-bit differences across numerical-library
versions are expected.

## What is checked

| Check | Error it can expose |
| --- | --- |
| Spectral matrix-sign transport cross-checked by the SVD polar factor, including overlap one | Incorrect transport phase, sign, or handling of coincident rays |
| Independent state gauges, common unitary changes, reversed loops | A gauge-dependent answer, basis dependence, or wrong orientation |
| Explicit one-ancilla reflection LCU | Dropping the minus signs in the block encoding of $P+Q-I$ |
| Controlled powers followed by inverse QFT | Wrong loop eigenphase or readout sign, including near the circular branch cut |
| Ramsey $X/Y$ expectations and deliberately negated loop | Treating uncontrolled density-matrix correctness as controlled-unitary correctness |
| Cyclic Gram square roots, finite-difference derivatives, covariance, and fidelity | Missing factors of $L$, an invalid source-shift reduction, or inconsistent phase orientation |
| Explicit two-copy density matrices | Incorrect fidelity multiplication or trace-distance convention |
| Clean-ancilla controlled partial-swap circuit | A missing control phase or ancilla that was silently discarded |
| Reduced DME action on every matrix unit, including off-diagonal control blocks | A channel formula that works only on classical control branches |
| Fresh-copy DME on an input entangled with a reference | Correlation or coherence errors hidden by testing only product inputs |

The QPE checks use eight control qubits and count $2^8-1=255$ loop uses, with
$\epsilon=\pi/16$ and $F=256=16\pi/\epsilon$, matching the sufficient grid
convention in [the algorithm](../science/algorithm.md). The controlled-DME
checks use target dimensions two and three and at most 256 sequential program
copies. No many-copy tensor-product circuit is materialized. Each program
register is traced out before the next fresh copy is consumed.

## What is not checked

The exact sign matrices are computed classically for these small examples.
They stand in for the ideal transport gates. This script does **not** synthesize
or simulate a full QSVT sign compiler, establish its degree bound, or provide a
practical implementation of the complete sampling algorithm. The explicit
partial-swap circuit checks its own phase and ancilla behavior; it does not
substitute for the manuscript's QSVT clean-ancilla argument.

The reported normalized-Choi trace-norm errors are errors on one particular
entangled input. They are lower bounds on the diamond norm, **not numerical
computations of that norm**. The dimension-independent upper bound below is
analytical. Its comparison with finite inputs can expose contradictions but
cannot prove it.

Finite examples do not prove asymptotic sample complexity, rule out better
algorithms, certify novelty, validate hardware noise robustness, or extend the
theorem beyond its promises. In particular, the sparse-Gram lower construction
uses $d\ge L\ge4$, $0\lt c\le1/4$, and a bounded total copy budget. The examples
do not establish a lower bound near $c=1$ or at fixed $d$.

## Controlled DME: phase and channel audit

Let $C=|1\rangle\langle1|$ be the external control projector, $S$ the SWAP
between target and program, and $\rho$ the density matrix of one fresh program
copy. Use the known unitary

~~~math
U_\delta=\exp(-i\delta C\otimes S).
~~~

For a control-target operator $`X=[X_{ab}]_{a,b=0,1}`$, tracing out the program
gives a channel $`\mathcal E_\delta`$ with blocks

~~~math
\begin{aligned}
(\mathcal E_\delta X)_{00}&=X_{00},\\
(\mathcal E_\delta X)_{01}&=\cos\delta\,X_{01}
  +i\sin\delta\,X_{01}\rho,\\
(\mathcal E_\delta X)_{10}&=\cos\delta\,X_{10}
  -i\sin\delta\,\rho X_{10},\\
(\mathcal E_\delta X)_{11}&=\cos^2\delta\,X_{11}
  +\sin^2\delta\,\rho\mathrm{Tr}X_{11}
  -i\cos\delta\sin\delta\,[\rho,X_{11}].
\end{aligned}
~~~

Thus the first-order generator on the **whole control-target system** is

~~~math
\left.\frac{d}{d\delta}\mathcal E_\delta\right|_{\delta=0}
=-i[C\otimes\rho,\,\cdot\,].
~~~

This identifies the phase of the implemented controlled operation. An
uncontrolled simulation of a density-matrix channel alone would not do so:
$R$ and $-R$ induce identical uncontrolled channels, but their controlled
versions can give orthogonal outputs. The negative-control check demonstrates
this explicitly.

For a pure program $P=|\psi\rangle\langle\psi|$, the $01$ block can also be
written

~~~math
X_{01}\bigl[\cos\delta(I-P)+e^{i\delta}P\bigr].
~~~

After $n$ fresh steps with $\delta=\pi/n$, its factor is

~~~math
(\cos(\pi/n))^n(I-P)-P.
~~~

The minus phase on the occupied ray is exact for every $n$; the orthogonal
component converges to $I-P$. This is checked in addition to the full channel.

### A dimension-independent error bound

Use the full diamond norm, without a factor of one half. Write
$\mathcal L_H=-i[H,\cdot]$, so
$\|\mathcal L_H\|_\diamond\le2\|H\|$.

The program-appending and program-tracing maps are channels with diamond norm
one. For $H=C\otimes S$ and $H_{\rm eff}=C\otimes\rho$, both Hamiltonian
norms are at most one. The exact and reduced evolutions have the same value and
first derivative at zero. Each second derivative has diamond norm at most four
because it is a composition of two commutator generators and channels. The
integral Taylor remainder therefore gives

~~~math
\|\mathcal E_\delta
-\mathrm{Ad}_{e^{-i\delta C\otimes\rho}}\|_\diamond
\le 4\delta^2.
~~~

Telescoping $n$ fresh steps, with $\delta=t/n$, yields

~~~math
\|\mathcal E_{t/n}^{\,n}
-\mathrm{Ad}_{e^{-itC\otimes\rho}}\|_\diamond
\le \frac{4t^2}{n}.
~~~

This argument allows an arbitrary reference system and a mixed program state.
The application to a reflection uses purity: for $\rho=P$ and $t=\pi$,
$e^{-i\pi P}=I-2P$. Reusing the same physical program copy is not licensed by
this derivation; the checks consume a fresh copy at every step.

### Explicit clean-ancilla implementation

Let $a$ be one clean ancilla. The known circuit

~~~math
D=(H_a\otimes I)\,\mathrm{controlled}_a(S)\,(H_a\otimes I)
~~~

records the SWAP eigenvalue in $a$. Applying the known controlled phase
$\exp(-i\delta C\otimes Z_a)$, then $D^\dagger=D$, implements
$U_\delta$ and returns $a$ to zero. The phase gate is the exact matrix
$\mathrm{diag}(1,1,e^{-i\delta},e^{i\delta})$ on $C,a$.
The checks compare its clean block and leakage with the matrix exponential.
There are two controlled SWAPs per step, plus a constant number of known
single- and two-qubit gates. On a $\lceil\log_2d\rceil$-qubit encoding, the
SWAP cost is $O(\log d)$; dimension padding does not require state access.

## Consequence for resource accounting

For an ideal circuit containing $Q$ fixed-label, phase-defined controlled
reflection calls, allocate

~~~math
n=\left\lceil \frac{4\pi^2 Q}{\delta_{\rm tot}}\right\rceil
~~~

fresh copies to each reflection call. The whole circuit's diamond error is at
most $\delta_{\rm tot}$, its total copy count is at most $Qn$, and source $j$
contributes $Q_jn$ copies. This is $O(Q^2/\delta_{\rm tot})$ copies, with no
extra factor of the number of sources. Inactive control branches still consume
their allocated samples. Multiply controlled calls reduce to computing their
known control condition into a clean bit, using the same primitive, then
uncomputing that bit.

The manuscript chooses $\delta_{\rm tot}=1/100$, giving
$n=\lceil400\pi^2Q\rceil$, in agreement with
[the resource accounting](../science/resources.md). Here $n$ denotes copies per
reflection; that section denotes this quantity by $m$.

With constant total simulation error, the manuscript's reflection query bound
$Q=O((L/(c\epsilon))\log(L/\epsilon))$ therefore leads to the stated copy
upper bound. The initial target specimen must be counted separately. Choosing
simulation error proportional to $\epsilon$ is unnecessary: the ideal
readout sets precision, while a constant total channel error reduces its
constant success probability by a constant amount.

The DME implementation requires the persistent target, one current program
register, one clean phase ancilla, and the circuit's controls. Its copies are
sequential; its memory does not grow with $Qn$. The gate bound counts known
rotations as elementary gates. Restricting to a fixed finite universal gate
set adds synthesis costs, which these numerical checks do not estimate.

The sample-to-reflection conversion is inherited. A relevant primary reference
is Wang and Zhang, [*Sample-Optimal Quantum Estimators for Pure-State Trace
Distance and Fidelity via Samplizer*, Theorem 13 (ICALP 2026)](https://doi.org/10.4230/LIPIcs.ICALP.2026.154).
The explicit argument here audits the phase and conservative constants needed
for this application; it is not a claim of a new samplizer.
