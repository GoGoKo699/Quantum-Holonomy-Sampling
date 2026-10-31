# Question, input model, and resource law

A cyclic collection of quantum states has a geometric phase that is unchanged by arbitrary phase choices for the individual state vectors. Directly measuring the corresponding Bargmann invariant can produce an exponentially small signal. The question here is how many supplied state copies are actually necessary when the receiver can process them coherently.

## 1. Independent labeled sources

Fix an integer $`L\ge4`$ and a Hilbert space $`\mathcal H=\mathbb C^d`$, represented in $`n=\lceil\log_2 d\rceil`$ qubits. The input consists of sources for the unknown pure density operators

```math
P_j=|\psi_j\rangle\langle\psi_j|,
\qquad j=1,\ldots,L,
\qquad P_{L+1}=P_1.
```

A request for label $`j`$ returns one fresh register in state $`P_j`$, independent of all previous copies. Labels are classical and may be chosen adaptively. The receiver may keep quantum memory, use known gates and clean ancillas, and perform joint or adaptive measurements. The sources supply density operators; an arbitrary global phase attached to a representative vector has no operational meaning.

The promise is a known lower bound on **overlap amplitude**:

```math
r_j=|\langle\psi_j|\psi_{j+1}\rangle|\ge c,
\qquad 0\lt c\le1.
```

Thus the corresponding pure-state squared fidelity is at least $`c^2`$. There is no promise of a nonzero overlap between nonadjacent states, a common reference state, or a lower bound on the full cyclic product independent of $`L`$.

The receiver is given copies as quantum data. A state-preparation unitary, its inverse, a coherent source-index oracle, and QRAM are not part of the input. Known controlled swaps between accessible registers are allowed and their gates are counted. The algorithm's requests follow a fixed classical schedule; the converse allows the more general adaptive schedule just described.

## 2. Target and error convention

Define

```math
B=\mathrm{Tr}(P_1P_2\cdots P_L)
=\prod_{j=1}^{L}\langle\psi_j|\psi_{j+1}\rangle,
\qquad \Phi=\arg B\pmod{2\pi}.
```

Under $`|\psi_j\rangle\mapsto e^{i\alpha_j}|\psi_j\rangle`$, the adjacent factors acquire phases that cancel around the loop. Therefore $`B`$ and $`\Phi`$ are well-defined functions of the density operators. The overlap promise ensures $`B\ne0`$.

For real angles, use circular distance

```math
\mathrm{dist}_{2\pi}(x,y)
=\min_{k\in\mathbb Z}|x-y+2\pi k|.
```

Given $`0\lt \epsilon\le\pi/16`$, the algorithm must output an angle $`\widehat\Phi`$ satisfying

```math
\Pr\!\left[
\mathrm{dist}_{2\pi}(\widehat\Phi,\Phi)\le\epsilon
\right]\ge\frac23
```

for every admissible input tuple. The algorithm returns a discrete Fourier outcome together with its grid-angle formula. This is an exact finite output description, so the statistical guarantee requires no numerical angle rounding.

This is the discrete Bargmann, or Pancharatnam, phase of the specified loop. Identifying it with a continuum Berry phase additionally requires a path, a discretization rule and an error estimate. Those are separate inputs and are not assumed here.

## 3. What is counted

The primary resource $`N`$ is the **total number of source copies**, summed over all labels. It includes the initial target specimen and every program copy consumed while implementing a reflection, including on an inactive control branch. A repetition of an ordinary full-cycle test consumes $`L`$ copies, so repetitions and copies must be distinguished.

The minimax copy complexity $`N^*_{L,d}(c,\epsilon)`$ is the smallest worst-case cap on the total number of requests sufficient for the guarantee above. A protocol with a random stopping time is covered when it obeys that cap. A bound only on the expected stopping time defines a different convention.

Quantum gates, simultaneously retained registers, and classical preprocessing are reported separately. In particular, swapping two $`n`$-qubit state registers costs $`O(n)`$ elementary gates. Dimension-independent copy complexity does not make all processing independent of $`d`$. The [resource account](resources.md) also charges the classical synthesis of a reusable polar-transformation circuit.

## 4. Main theorem

**Theorem (copy complexity of a discrete geometric phase).** In the stated input model, there is an algorithm with

```math
N^*_{L,d}(c,\epsilon)
\le
C\frac{L^2}{c^2\epsilon^2}
\log^2\!\left(\frac{L}{\epsilon}\right)
```

for an absolute constant $`C`$, every $`L\ge4`$, every represented dimension, and $`0\lt c\le1`$. For $`d\ge L`$ and $`0\lt c\le1/4`$, every algorithm in the model satisfies

```math
N^*_{L,d}(c,\epsilon)
\ge
\frac{(1-2c)L^2}{144c^2\epsilon^2}.
```

Consequently the dependence on $`L`$, $`c`$ and $`\epsilon`$ is optimal up to logarithms in that lower-bound regime. The upper theorem is dimension independent as a copy bound. The converse is a worst-case statement for dimensions at least $`L`$; it does not assert the same uniform small-$`c`$ law at a fixed smaller dimension or near $`c=1`$.

At $`c=1`$, all adjacent rays coincide, hence $`\Phi=0`$. This endpoint illustrates why the restricted range of the matching lower bound is substantive.

### Proof route

1. [Canonical transport](transport.md) gives a projector-defined unitary that transfers each ray to the next while preserving its geometric phase.
2. [The complete algorithm](algorithm.md) implements that transport coherently, applies phase estimation to the loop, and controls all approximation errors.
3. [Resources](resources.md) converts the reflection circuit into independently supplied copies using controlled partial swaps, with explicit counts and charged preprocessing.
4. [The lower bound](lower-bound.md) constructs a positive circulant Gram family and reduces every adaptive protocol to finite discrimination of two tensor-power pure states.

## 5. Consequence and inherited ingredients

The [sparse-ring example](examples.md) has $`|B|=c^L`$, although each local overlap remains nonzero and bounded below. Direct raw-cycle measurements require exponentially many shots for fixed phase accuracy on this family. The upper theorem gives polynomial total-copy cost with general coherent processing, and the converse identifies its intrinsic polynomial scale.

The exact local rotation, polar compilation, phase estimation and sample-based simulation are established tools. The [related-work account](../references/related-work.md) identifies their source statements and distinguishes the present task-specific copy law from raw-trace estimation, Hamiltonian-oracle Berry-phase algorithms, and photonic protocols with more restricted operations.
