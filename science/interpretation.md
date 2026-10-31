# Visibility, phase, and coherent access

The [main theorem](model.md#4-main-theorem) separates two resources that are easy to conflate: the visibility of one particular interference experiment, and the information available in a supply of quantum states.

## Why the direct signal can be small

The cyclic Bargmann invariant multiplies neighboring overlap amplitudes. If each amplitude is $`c`$, its magnitude is $`c^L`$. An ancilla in a direct cycle test consequently carries only a small bias about the phase. Repeating that experiment estimates its real and imaginary parts, with phase accuracy requiring absolute accuracy proportional to $`|B|`$.

The [explicit comparison](examples.md) gives the shot and total-copy costs, and states exactly which measurement strategy the exponential benchmark describes. It does not provide a lower bound against every quantum protocol or every receiver who measures copies separately.

## What coherent transport changes

For neighboring projectors $`P,Q`$, the operator $`P+Q-I`$ sends the source ray toward the next ray with an amplitude proportional to their overlap. Taking its polar factor retains the phase of that overlap and removes the attenuation. Repeating this operation around the loop produces a unit-modulus eigenvalue carrying the desired phase.

This normalization has a cost. The smallest relevant singular value is the local overlap, so the polar compiler uses order $`1/c`$ queries per transport, up to logarithms. Phase estimation adds inverse accuracy, and simulating all reflection queries with fresh copies squares their total count. The result is polynomial in the loop length and the reciprocal local overlap.

The normalization is implemented coherently with an explicitly controlled circuit. Postselecting successive projections instead would retain the product of success probabilities and would not establish the stated resource law.

## Why sparse overlap graphs matter

With a well-overlapping common reference, one can sometimes reconstruct loop information using triangles. The hard family here has a ring as its graph of nonzero overlaps. Every proper simple cycle of length at least three has a missing edge; adjacent two-cycles are real and carry no phase. The global cyclic phase therefore cannot be obtained by multiplying nonzero triangle invariants within the supplied state set.

Nevertheless, the Gram matrix remains uniformly positive in the lower-bound regime. Its columns give physical normalized states, and the total phase changes only weakly in each individual specimen. The [finite-testing converse](lower-bound.md) shows that this weak local distinguishability forces the quadratic copy cost even for an unrestricted collective receiver.

## Operational meaning of the input

The states are quantum data already supplied by sources. Their physical production remains a source cost; the theorem counts how many such data items the receiver needs. Applying it to a classically specified input requires separately accounting for state preparation.

The receiver has coherent access to the contents of each state register and can perform known controlled swaps. This is compatible with the circuit model. It is stronger than a photonic interface in which internal degrees of freedom are inaccessible and only spatial-mode interferometers and photon counting are allowed. The existing photonic sparse-cycle example is a useful diagnosis of raw visibility, but the present algorithm is not an implementation under that restricted apparatus.

The [resource account](resources.md) reports quantum gates, streaming registers, precision synthesis and classical preprocessing. Optimal copy scaling does not imply that the algorithm is currently the fastest implementation at every finite parameter value.

## Scope of the geometric quantity

All input sources are pure and stationary across requests. For mixed states, the phase of $`\operatorname{Tr}(\rho_1\cdots\rho_L)`$ and the phase of the dominant eigenvector loop are different targets. The rank-one transport identity does not prove either mixed-state extension.

The result concerns the specified discrete loop. A continuous adiabatic path or a topological invariant introduces additional structure. No automatic continuum limit, quantization, or noise tolerance follows from the discrete copy theorem alone.

The outcome is a statistical resource characterization: coherent processing can access a geometric phase despite exponentially weak raw-cycle visibility, and the local overlap and loop length set the nearly optimal worst-case copy scale.
