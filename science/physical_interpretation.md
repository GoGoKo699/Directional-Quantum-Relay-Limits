# Local directed relays as a physical architecture

The path theorem concerns transfer between **initially occupied and finally retained internal modes**. This operational choice matters as much as the topology. A directional device can have excellent transmission for an incoming traveling field while failing to transfer an arbitrary state initially stored in one cavity perfectly to another cavity at one time.

## How local directionality is realized

For two neighboring modes, a shared vacuum loss operator creates a dissipative cross term in both drift directions. A coherent hopping term contributes with opposite phases to those directions. Matching their magnitudes cancels the upstream drift and reinforces the downstream drift. This coherent–dissipative interference mechanism is established reservoir engineering; see [MetelmannClerk15] and [Wanjura20] in the [references](../references/related_work.md#references).

The construction in [Attainable designs](attainable_designs.md) uses one loss channel for each edge. In the interior its jump is

```math
L_j=\sqrt{\Gamma}(a_j-a_{j+1}),
```

and the matched Hamiltonian matrix elements are

```math
h_{j+1,j}=\frac{i\Gamma}{2},
\qquad
h_{j,j+1}=-\frac{i\Gamma}{2}.
```

Each interior mode participates in two edge loss operators. Their diagonal contributions produce amplitude damping $`\Gamma`$. The upper drift cancels and the lower drift is $`\Gamma`$. Modified edge weights match slower sender and receiver modes to the same interior. The full construction, including boundary cases, is given in the authoritative design proof.

These are passive linear dynamics: the Hamiltonian conserves total excitation number, and the loss operators contain annihilation operators only. Complex relative phases implement directional interference without supplying a creation-operator gain channel in the effective model. The theorem does not equate a rate cap with total laboratory power or the cost of setting up a reservoir.

The array interpretation is local. Independent engineered edge reservoirs give a tridiagonal damping matrix and, after interference, a bidiagonal drift. The known cavity-array framework supplies physical context for these local coherent and dissipative bonds. Results about actively pumped amplification in that framework are distinct from the passive state-transfer task analyzed here.

## Why a common waveguide is different

Several emitters coupled to one chiral Markovian waveguide generally interact with all downstream emitters through the same traveling field. Ordering the sites makes the drift lower triangular, but not lower bidiagonal. The field can pass through an intermediate site without being stored there, producing multiple coherent routes between the endpoint modes.

The distinction is explicit in the [bypass example](bypass.md): one direct first-to-last coupling interferes with the route through the middle mode and raises the arrival probability above $`4/e^2`$. Thus a geometrical drawing of atoms along a line does not by itself place their effective generator in the local path class. One must inspect the complete drift after the environmental degrees of freedom have been treated.

Similarly, hybrid nodes with internally reciprocal resonators, giant atoms with retarded multiple coupling points, and dispersion-engineered propagating fields have different impulse responses. Their high-transfer results are compatible with the local path ceiling. The [model-by-model comparison](../references/related_work.md) states what each relevant source establishes.

## Stored-state transfer and scattering

In the stored-state task the sender starts occupied at time zero and emits according to its fixed local dynamics. The receiver retains one physical mode at a declared time. There is no freely selected incident temporal waveform, and the emitted field is not subsequently collected as an additional output.

A scattering experiment instead prescribes an incoming traveling mode and measures the outgoing field. A unit scattering amplitude over a suitable frequency range does not mean that a spontaneously emitted decaying pulse will be captured perfectly by one stationary receiver. Capturing it requires the appropriate temporal mode. Static relays on the strict path contribute positive first-order response kernels, so they can delay and broaden the response without increasing its peak beyond the endpoint ceiling.

This explains both sides of the result. The relays do not repair the endpoint pulse mismatch. Yet a suitable endpoint timescale can average over fluctuations in the total interior transit delay, preventing the arrival probability from vanishing with the number of ideal relays.

## The time and tuning costs

For $`n\ge3`$, write $`m=n-2\ge1`$ for the number of interior modes, all at rate $`\Gamma`$. Their positive convolution acts like a sum of $`m`$ independent exponential waiting times. Its mean is $`m/\Gamma`$ and standard deviation is $`\sqrt m/\Gamma`$. An endpoint timescale $`1/a`$ long compared with this spread makes the pulse insensitive to the arrival-time fluctuations.

For a relative amplitude deficit at most $`\varepsilon`$, the explicit design chooses

```math
a=\Gamma\sqrt{\frac{\varepsilon}{m}},
\qquad
t=\frac{m+\sqrt{m/\varepsilon}}{\Gamma},
```

subject to the construction's boundary-rate condition. At fixed $`\varepsilon`$, the leading time is proportional to chain length. At fixed length, approaching the exact zero-extra-loss supremum sends the endpoint rate to zero and the readout time to infinity.

Unavoidable loss penalizes this waiting. In the weak-loss regime $`n\kappa_n/\Gamma\to x`$, an endpoint choice $`a_n=\Gamma n^{-\alpha}`$ with $`1/2\lt \alpha\lt 1`$ resolves the transit spread while adding only a subleading delay. The propagation time then accumulates a limiting amplitude attenuation $`e^{-x}`$, and the probability acquires $`e^{-2x}`$. The [loss proof](loss_frontier.md) establishes both this construction and the converse over every allowed design.

## What the resource conventions measure

All rates in the bounds are **amplitude damping rates**. A jump $`\sqrt{2\kappa}\,a_j`$ produces drift $`-\kappa a_j`$ and population decay rate $`2\kappa`$. Confusing the two conventions changes the exponent in the transmission law.

The cap $`\nu_j\leq\Gamma`$ applies to engineered diagonal amplitude damping before the additional loss is added. Complete positivity ties the off-diagonal drift entries to those dampings. It does not permit arbitrary independent choices of a non-Hermitian hopping matrix and a smaller physical loss budget. Nor does it impose the separate constraint $`|w_j|\leq\Gamma`$: product-saturating equal-damping endpoint links have magnitude $`\sqrt2\Gamma`$ for $`n\ge3`$, while the two-mode link has magnitude $`2\Gamma`$.

Every channel use begins with the other modes and environmental inputs in vacuum. The capacity statements assume independent such uses. A reset schedule, loading/readout overhead and fixed spatial spacing would be needed to turn them into qubits per second or a distance in meters. The mode-count threshold itself is determined without those additional assumptions.
