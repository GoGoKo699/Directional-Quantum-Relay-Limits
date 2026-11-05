# Thirty milestones for directional quantum relay limits

This map connects the local physics of an oscillator and its environment to the complete design limit for static directional paths. It contains exactly 30 understanding targets in two phases. Specialist calculations remain in the linked scientific pages.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background joins oscillator states, composite-system channels, Markovian loss, linear dynamics, and performance measures into the physical optimization contract. The narrative then follows one mechanism from a two-mode response through the all-path converse, physical constructions, loss optimization, communication consequences, and a counterexample that fixes the result's scope. Each phase ends by assembling its preceding components.

## Educational anchor and notation

The single educational anchor is H. M. Wiseman and G. J. Milburn, *Quantum Measurement and Control* (2010), denoted **WM10**. The [source-to-project bridge](WISEMAN_MILBURN_BRIDGE.md) supplies the reading route, notation translation, and a worked two-mode example.

The section and starting-page pointers below follow the publisher's table of contents. They orient the background; the linked project pages supply the specialized proofs and identify imported research-level results. The numerical-radius extremum, bidiagonal response identity, absorption benchmark, and pure-loss capacity formula retain their primary attributions in [related work](../references/related_work.md).

| Anchor location | Starting page | Role in this project |
|---|---:|---|
| Appendix A.4 | 410 | Harmonic oscillator states, operators, and vacuum |
| Appendix A.2 | 404 | Composite systems and reduced states |
| §3.2 | 99 | Born–Markov description of open dynamics |
| §3.6 | 119 | Lindblad evolution and positivity |
| §3.11 | 141 | Heisenberg-picture equations |
| §6.6 | 312 | Linear quantum systems |

The network has $`n`$ modes and $`m=n-2`$ internal relays. Its endpoint amplitude is $`G(t)=[e^{At}]_{n1}`$ and its transmissivity is $`\eta(t)=|G(t)|^2`$. Engineered diagonal amplitude rates are bounded by $`\Gamma`$; unavoidable additional amplitude loss is $`\kappa`$. This map uses $`\delta=\kappa/\Gamma`$ for the loss ratio and $`\varepsilon`$ for an amplitude-accuracy parameter. The [bridge's rate conventions](WISEMAN_MILBURN_BRIDGE.md#notation-and-rate-conventions) and the [canonical model](../science/model.md) fix their meanings.

## Phase I — Background and preliminaries: M01–M12

The first phase moves from one local mode to the complete quantum channel and admissible architecture.

### M01: Oscillator states and vacuum

**Central question.** What is carried by one oscillator, and what does it mean for every other mode to start empty?

**Understanding target.** Identify the annihilation operator, number operator, vacuum, and arbitrary oscillator state. Distinguish a number-conserving interaction from a restriction to a single-photon input: the physical model acts on the full oscillator Hilbert space.

**Earlier dependencies and story role.** None. Introduces the local quantum object from which the network is assembled.

**Conceptual connection.** Vacuum is a specified environmental resource, while the input can contain an arbitrary state. This distinction later makes the output channel quantum limited.

**Source pointers.** Background anchor: [WM10, Appendix A.4 (p. 410)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Passive Markovian dynamics](../science/model.md#passive-markovian-dynamics) and [operational contract](../science/model.md#operational-contract).

### M02: Composite systems and reference-preserving transfer

**Central question.** How is transfer defined when the input is entangled with a system outside the device?

**Understanding target.** Explain the product initialization of the relay modes and bath inputs, the retained external reference, and the partial trace defining the output channel. Successful state transfer must preserve correlations with that reference as well as reproduce local expectation values.

**Earlier dependencies and story role.** [M01](#m01-oscillator-states-and-vacuum). Extends one oscillator to the composite input–network–environment setting.

**Conceptual connection.** The channel viewpoint turns an excitation calculation into a statement about arbitrary inputs and entanglement.

**Source pointers.** Background anchor: [WM10, Appendix A.2 (p. 404)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Operational contract](../science/model.md#operational-contract) and [reduction to a pure-loss channel](../science/model.md#reduction-to-a-pure-loss-channel).

### M03: The Markovian description and its physical boundary

**Central question.** Which environmental assumptions are encoded in a time-local, time-independent generator?

**Understanding target.** Identify the Markovian approximation underlying the model and the role of vacuum bath inputs. Distinguish this assumed reduced description from a microscopic device whose delays or frequency dependence remain dynamically important.

**Earlier dependencies and story role.** [M01](#m01-oscillator-states-and-vacuum), [M02](#m02-composite-systems-and-reference-preserving-transfer). Places the elementary modes in the open-system setting used throughout the project.

**Conceptual connection.** A memoryless generator permits a matrix exponential; retarded waveguide dynamics can have a different response and belong to a different architectural class.

**Source pointers.** Background anchor: [WM10, §3.2 (p. 99)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Passive Markovian dynamics](../science/model.md#passive-markovian-dynamics) and [why a common waveguide is different](../science/physical_interpretation.md#why-a-common-waveguide-is-different).

### M04: Lindblad loss and the two damping conventions

**Central question.** Why do amplitude and occupation decay carry different rates?

**Understanding target.** Interpret the dissipator $`\mathcal D[L]`$ and explain why $`L=\sqrt{2\nu}\,a`$ produces amplitude decay $`e^{-\nu t}`$ and occupation decay $`e^{-2\nu t}`$. Keep bath coupling coefficients, amplitude damping rates, and population damping rates distinct.

**Earlier dependencies and story role.** [M01](#m01-oscillator-states-and-vacuum), [M03](#m03-the-markovian-description-and-its-physical-boundary). Fixes the local dissipative convention before rates enter bounds or limits.

**Conceptual connection.** The same factor of two controls the final attenuation exponent and the physical meaning of the unavoidable-loss parameter.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Passive Markovian dynamics](../science/model.md#passive-markovian-dynamics) and [resource conventions](../science/physical_interpretation.md#what-the-resource-conventions-measure).

### M05: From the adjoint generator to a closed drift equation

**Central question.** Why can the relevant amplitudes be propagated by a finite matrix?

**Understanding target.** Connect a quadratic, number-conserving Hamiltonian and linear annihilation-only jumps to $`\frac{d}{dt}\langle a\rangle=A\langle a\rangle`$, with $`A=-ih-K^\dagger K/2`$. Explain why closure of this equation is a property of the dynamics rather than an assumption that the input is Gaussian.

**Earlier dependencies and story role.** [M02](#m02-composite-systems-and-reference-preserving-transfer), [M04](#m04-lindblad-loss-and-the-two-damping-conventions). Connects the microscopic operators to the linear system used in every proof.

**Conceptual connection.** The Heisenberg description supplies the input–output amplitude whose physical channel meaning is established later.

**Source pointers.** Background anchor: [WM10, §3.11 (p. 141)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Passive Markovian dynamics](../science/model.md#passive-markovian-dynamics) and [pure-loss reduction](../science/model.md#reduction-to-a-pure-loss-channel).

### M06: Passivity as a constraint on the full drift

**Central question.** What prevents directional hopping from being chosen independently of its physical damping?

**Understanding target.** Explain $`A+A^\dagger=-K^\dagger K\preceq0`$ and its implication that $`e^{At}`$ is a contraction. Recognize that this constraint concerns the complete physical drift, including coherent and dissipative terms, and that a general non-Hermitian hopping matrix need not satisfy it.

**Earlier dependencies and story role.** [M04](#m04-lindblad-loss-and-the-two-damping-conventions), [M05](#m05-from-the-adjoint-generator-to-a-closed-drift-equation). Adds the physical admissibility condition to the linear-system description.

**Conceptual connection.** Complete positivity and vacuum loss become a matrix inequality that later bounds the product of all path couplings.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Passive Markovian dynamics](../science/model.md#passive-markovian-dynamics) and [rate budget](../science/model.md#additional-unavoidable-loss-and-the-rate-budget).

### M07: Directional interference on one bond

**Central question.** How can reciprocal coherent and dissipative terms produce a one-way drift?

**Understanding target.** Explain the cancellation of the upstream drift and reinforcement of the downstream drift when a shared vacuum loss operator is matched to a coherent hopping term. Keep the Hamiltonian's Hermiticity and the complete drift's directionality distinct.

**Earlier dependencies and story role.** [M04](#m04-lindblad-loss-and-the-two-damping-conventions), [M05](#m05-from-the-adjoint-generator-to-a-closed-drift-equation), [M06](#m06-passivity-as-a-constraint-on-the-full-drift). Builds the local physical mechanism from which a directional path is constructed.

**Conceptual connection.** Reservoir engineering realizes the admissible matrix structure without introducing a gain channel into the effective model.

**Source pointers.** Background anchor: [WM10, §3.11 (p. 141)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [How local directionality is realized](../science/physical_interpretation.md#how-local-directionality-is-realized) and [local realization](../science/attainable_designs.md#a-local-realization-of-the-sharp-product-profile).

### M08: The drift graph and the communication geometry

**Central question.** When does a line of physical components actually define one directed path?

**Understanding target.** Distinguish a lower-bidiagonal drift from a general lower-triangular drift, and identify bypass couplings in the latter. Explain why internal-mode state transfer and traveling-field scattering use different inputs and outputs even in the same device.

**Earlier dependencies and story role.** [M03](#m03-the-markovian-description-and-its-physical-boundary), [M05](#m05-from-the-adjoint-generator-to-a-closed-drift-equation), [M07](#m07-directional-interference-on-one-bond). Moves from one directional bond to the full architecture and operational task.

**Conceptual connection.** The theorem's unique route is a property of the reduced drift, not merely the spatial arrangement of modes.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Strictly directional scalar paths](../science/model.md#strictly-directional-scalar-paths) and [stored-state transfer and scattering](../science/physical_interpretation.md#stored-state-transfer-and-scattering).

### M09: Causal responses and positive convolutions

**Central question.** How does a sequence of scalar first-order equations combine into a transfer response?

**Understanding target.** Relate variation of constants to convolution of causal exponential responses. For $`\nu>0`$, distinguish $`e^{-\nu t}`$ on nonnegative times from the normalized density $`k_\nu(t)=\nu e^{-\nu t}`$, and explain why convolution with a positive unit-mass kernel cannot increase a peak.

**Earlier dependencies and story role.** [M05](#m05-from-the-adjoint-generator-to-a-closed-drift-equation), [M08](#m08-the-drift-graph-and-the-communication-geometry). Supplies the mathematical language connecting local relaxations to a network response.

**Conceptual connection.** Serial relay dynamics can be interpreted as averaging over positive delays, which is the central mechanism of both the upper bound and the construction.

**Source pointers.** Background anchor: [WM10, §3.11 (p. 141)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [The propagator as a convolution](../science/path_ceiling.md#3-the-propagator-is-a-single-convolution) and [random-delay representation](../science/attainable_designs.md#exact-random-delay-representation).

### M10: From a transfer amplitude to the complete quantum channel

**Central question.** Why does one matrix element determine the retained-mode channel for arbitrary inputs?

**Understanding target.** Explain the vacuum dilation $`a_{\mathrm{out}}=G a_{\mathrm{in}}+\sqrt{1-|G|^2}\,e`$ and the role of the output commutator. Identify $`\eta=|G|^2`$ as the transmissivity of a pure-loss channel, including when the input is non-Gaussian or reference entangled.

**Earlier dependencies and story role.** [M02](#m02-composite-systems-and-reference-preserving-transfer), [M05](#m05-from-the-adjoint-generator-to-a-closed-drift-equation), [M06](#m06-passivity-as-a-constraint-on-the-full-drift). Connects the network calculation to a state-transfer statement.

**Conceptual connection.** Passivity determines the allowed amplitudes, while vacuum environmental modes determine the noise accompanying those amplitudes.

**Source pointers.** Background anchor: [WM10, Appendix A.2 (p. 404)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Reduction to a pure-loss channel](../science/model.md#reduction-to-a-pure-loss-channel) and [operational contract](../science/model.md#operational-contract).

### M11: Transfer probability, fidelity, and communication capacity

**Central question.** Which quantity is bounded when a transfer probability is reported?

**Understanding target.** Distinguish single-excitation arrival probability, bosonic transmissivity, average qubit-state fidelity, ordinary quantum capacity, and capacity with two-way assistance. Identify the separate roles of an input-energy budget and a fresh-use convention.

**Earlier dependencies and story role.** [M02](#m02-composite-systems-and-reference-preserving-transfer), [M10](#m10-from-a-transfer-amplitude-to-the-complete-quantum-channel). Establishes the interpretation of performance before any architecture is optimized.

**Conceptual connection.** A physical transmissivity bound becomes a communication statement only after the input encoding and allowed assistance are specified.

**Source pointers.** Background anchor: [WM10, Appendix A.2 (p. 404)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Transmissivity and fidelity](../science/channel_consequences.md#transmissivity-and-state-fidelity-are-different-quantities), [ordinary bosonic capacity](../science/channel_consequences.md#ordinary-unassisted-bosonic-quantum-capacity), and [assistance boundaries](../science/channel_consequences.md#assistance-and-resource-boundaries).

### M12: The complete physical optimization contract

**Central question.** What is being optimized, and which resources remain charged?

**Understanding target.** Assemble the static passive scalar path, arbitrary single-mode input, vacuum relays, one retained output mode, and freely chosen readout time into one problem. Separate the engineered diagonal-rate cap $`\Gamma`$ from added amplitude loss $`\kappa`$, endpoint tuning, elapsed time, and initialization between uses.

**Earlier dependencies and story role.** [M03](#m03-the-markovian-description-and-its-physical-boundary), [M06](#m06-passivity-as-a-constraint-on-the-full-drift), [M08](#m08-the-drift-graph-and-the-communication-geometry), [M09](#m09-causal-responses-and-positive-convolutions), [M10](#m10-from-a-transfer-amplitude-to-the-complete-quantum-channel), [M11](#m11-transfer-probability-fidelity-and-communication-capacity). Integrates the background into the exact framework needed for the research narrative.

**Conceptual connection.** The admissible generator, the channel task, and the resource budget jointly determine which optimization claims have physical meaning.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Operational contract](../science/model.md#operational-contract), [additional loss and budget](../science/model.md#additional-unavoidable-loss-and-the-rate-budget), and [resource conventions](../science/physical_interpretation.md#what-the-resource-conventions-measure).

## Phase II — Narrative and innovation: M13–M30

The second phase builds the global result from its local response and coupling constraints. Imported ingredients remain explicitly attributed; the final milestones integrate the optimized channel, charged resources, and architectural boundary.

### M13: The inherited two-endpoint response

**Central question.** Where does the familiar two-emitter ceiling come from?

**Understanding target.** Explain the matched-pair response $`G(t)=2at\,e^{-at}`$ and its peak $`2/e`$, then relate the unequal-rate response to the same upper bound. Distinguish the amplitude ceiling from the probability $`4/e^2`$ and identify this endpoint benchmark as established absorption physics.

**Earlier dependencies and story role.** [M07](#m07-directional-interference-on-one-bond), [M09](#m09-causal-responses-and-positive-convolutions), [M10](#m10-from-a-transfer-amplitude-to-the-complete-quantum-channel), [M12](#m12-the-complete-physical-optimization-contract). Starts the narrative with the smallest physical instance and the inherited benchmark that relays must confront.

**Conceptual connection.** A decaying emitter waveform and a stationary receiver define the local pulse mismatch that survives throughout the path.

**Source pointers.** Background anchor: [WM10, §3.11 (p. 141)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Two-endpoint response](../science/path_ceiling.md#4-the-two-endpoint-response-has-peak-2e) and [optical absorption attribution](../references/related_work.md#optical-absorption-and-passive-pulse-shaping).

### M14: Normalizing the complete-positivity constraint

**Central question.** How does passivity constrain an entire connected path of unequal rates?

**Understanding target.** Explain why a zero diagonal damping rate or a zero edge breaks transfer. For positive rates, remove edge phases and normalize the damping matrix to $`I-B\succeq0`$, where $`B`$ is a nonnegative weighted path with $`b_j=|w_j|/(2\sqrt{\nu_j\nu_{j+1}})`$.

**Earlier dependencies and story role.** [M06](#m06-passivity-as-a-constraint-on-the-full-drift), [M08](#m08-the-drift-graph-and-the-communication-geometry), [M12](#m12-the-complete-physical-optimization-contract). Turns local physical admissibility into a common matrix constraint for all designs.

**Conceptual connection.** The normalization isolates the geometry and dimensionless edge strengths from the individual decay times.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Degenerate rates](../science/path_ceiling.md#1-degenerate-rates-break-the-path) and [sharp path-product inequality](../science/path_ceiling.md#2-the-sharp-path-product-inequality).

### M15: The classical extremum for the edge product

**Central question.** Why is the product of all forward couplings bounded more strongly than separate bondwise estimates suggest?

**Understanding target.** Follow the Perron-vector product argument and its equality conditions. Connect it to the numerical-radius power inequality and the Crabb weighted shift, keeping a numerical-radius bound distinct from an operator-norm contraction and recognizing both the extremum and its profile as classical.

**Earlier dependencies and story role.** [M06](#m06-passivity-as-a-constraint-on-the-full-drift), [M14](#m14-normalizing-the-complete-positivity-constraint). Supplies the global coupling constraint required by the path theorem.

**Conceptual connection.** A physical complete-positivity condition invokes an inherited operator-theoretic extremum; its new role is to constrain a realizable quantum transfer amplitude.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Product proof](../science/path_ceiling.md#2-the-sharp-path-product-inequality), [operator-theory interpretation](../science/path_ceiling.md#classical-operator-theory-interpretation), and [classical attribution](../references/related_work.md#classical-operator-theory).

### M16: The unique-path transfer formula

**Central question.** How do the edge-product bound and the scalar responses combine for an arbitrary chain?

**Understanding target.** Explain why the endpoint propagator is one product of edge couplings times one convolution. Use the triangle inequality to remove detunings and the product bound to separate a two-endpoint response from normalized internal delay kernels.

**Earlier dependencies and story role.** [M09](#m09-causal-responses-and-positive-convolutions), [M13](#m13-the-inherited-two-endpoint-response), [M15](#m15-the-classical-extremum-for-the-edge-product). Joins the operator constraint and the dynamical response into the load-bearing upper-bound mechanism.

**Conceptual connection.** Uniqueness of the directed route prevents a sum over interfering paths; positivity then turns the relay action into averaging.

**Source pointers.** Background anchor: [WM10, §3.11 (p. 141)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [The propagator is a single convolution](../science/path_ceiling.md#3-the-propagator-is-a-single-convolution) and [serial-filter attribution](../references/related_work.md#serial-filters-and-the-time-domain-step).

### M17: The universal ceiling and its exact quantifiers

**Central question.** What does the relay-independent ceiling establish, and when can equality occur?

**Understanding target.** Combine the two-endpoint peak and positive-kernel contraction to obtain $`\eta(t)\le4/e^2`$ for every allowed design and time. Distinguish finite-time equality for two modes from the sharp but unattained finite-rate supremum for $`n\ge3`$.

**Earlier dependencies and story role.** [M13](#m13-the-inherited-two-endpoint-response), [M16](#m16-the-unique-path-transfer-formula). Completes the converse for the zero-extra-loss path problem.

**Conceptual connection.** The theorem extends the known endpoint limit through every admissible static relay without assuming equal rates or resonant parameters in the original design.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Path theorem](../science/path_ceiling.md#theorem) and [attainment and strictness](../science/path_ceiling.md#5-attainment-and-strictness).

### M18: Realizing the extremal profile with local reservoirs

**Central question.** Can the sharp mathematical edge profile be implemented by the stated physical model?

**Understanding target.** Explain the adjacent-pair loss operators and matched current Hamiltonian that realize product saturation for arbitrary positive diagonal rates. Account for the different two-mode endpoint coefficient and the bounded coefficients of the oscillator operators.

**Earlier dependencies and story role.** [M07](#m07-directional-interference-on-one-bond), [M15](#m15-the-classical-extremum-for-the-edge-product), [M17](#m17-the-universal-ceiling-and-its-exact-quantifiers). Connects the converse to a constructive physical design.

**Conceptual connection.** An extremal matrix is useful for quantum transfer only when its coherent and dissipative contributions satisfy the same local realization and rate contract.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Local realization of the product profile](../science/attainable_designs.md#a-local-realization-of-the-sharp-product-profile) and [directionality mechanism](../science/physical_interpretation.md#how-local-directionality-is-realized).

### M19: Relay-delay fluctuations and endpoint response width

**Central question.** Which feature of many relays degrades a sharply timed endpoint response?

**Understanding target.** For $`m=n-2\ge1`$ internal rates equal to $`\Gamma`$, interpret the amplitude as an average over $`S\sim\mathrm{Gamma}(m,\text{ rate }\Gamma)`$. Distinguish the mean delay $`m/\Gamma`$, its spread $`\sqrt m/\Gamma`$, and the endpoint timescale $`1/a`$.

**Earlier dependencies and story role.** [M09](#m09-causal-responses-and-positive-convolutions), [M18](#m18-realizing-the-extremal-profile-with-local-reservoirs). Identifies the physical timescale separation behind near-attainment.

**Conceptual connection.** Slow endpoints average over fluctuations in relay transit time while the leading propagation delay still grows with chain length.

**Source pointers.** Background anchor: [WM10, §3.11 (p. 141)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Random-delay representation](../science/attainable_designs.md#exact-random-delay-representation) and [time and tuning costs](../science/physical_interpretation.md#the-time-and-tuning-costs).

### M20: Sharpness with bounded coefficients and an explicit time cost

**Central question.** How can a long path approach the ceiling without increasing its local rates?

**Understanding target.** Connect the finite lower bound to the choice $`a=\Gamma\sqrt{\varepsilon/m}`$ and readout $`t=(m+\sqrt{m/\varepsilon})/\Gamma`$, with the stated boundary-rate condition. Explain both fixed-accuracy ballistic scaling and the diverging readout time needed for exact sharpness at fixed $`n\ge3`$.

**Earlier dependencies and story role.** [M12](#m12-the-complete-physical-optimization-contract), [M17](#m17-the-universal-ceiling-and-its-exact-quantifiers), [M19](#m19-relay-delay-fluctuations-and-endpoint-response-width). Completes the zero-extra-loss result by matching its upper bound with a charged construction.

**Conceptual connection.** Endpoint engineering removes the equal-rate family's algebraic dilution, while the endpoint pulse-mismatch ceiling remains.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Finite lower bound](../science/attainable_designs.md#a-finite-size-lower-bound), [accuracy and rate hierarchy](../science/attainable_designs.md#accuracy-waiting-time-and-rate-hierarchy), and [equal-rate comparison](../science/attainable_designs.md#comparison-with-equal-diagonal-damping).

### M21: The finite bound with unavoidable loss

**Central question.** How does loss that cannot be engineered away enter an all-design converse?

**Understanding target.** Keep $`A_0`$ passive separately from $`-\kappa I`$, shift every decay rate to $`\nu_j+\kappa`$, and explain the internal mass factors and endpoint square roots. Count their combined $`n-1`$ powers to obtain the finite bound under $`\nu_j\le\Gamma`$.

**Earlier dependencies and story role.** [M04](#m04-lindblad-loss-and-the-two-damping-conventions), [M12](#m12-the-complete-physical-optimization-contract), [M15](#m15-the-classical-extremum-for-the-edge-product), [M16](#m16-the-unique-path-transfer-formula), [M20](#m20-sharpness-with-bounded-coefficients-and-an-explicit-time-cost). Introduces the new optimization regime while preserving the physical resource constraint.

**Conceptual connection.** Extra loss changes both the kernel normalization and the waiting-time penalty; complete positivity still constrains only the engineered transfer couplings.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Uniform-loss setup](../science/loss_frontier.md) and [universal finite-size bound](../science/loss_frontier.md#1-universal-finite-size-bound).

### M22: Why every internal rate can saturate its budget

**Central question.** Which part of the finite design optimization can be solved exactly before choosing the endpoints?

**Understanding target.** Explain the factorization $`h_\nu=h_\Gamma*q_{\nu,\Gamma}`$ with a nonnegative measure of total mass at most one. Use peak contraction to justify replacing internal rates by $`\Gamma`$, then identify the exact remaining optimization over two endpoint rates and time without assuming equal endpoints.

**Earlier dependencies and story role.** [M09](#m09-causal-responses-and-positive-convolutions), [M18](#m18-realizing-the-extremal-profile-with-local-reservoirs), [M21](#m21-the-finite-bound-with-unavoidable-loss). Reduces the all-generator optimization to its remaining physical degrees of freedom.

**Conceptual connection.** The same positive-convolution mechanism now compares designs; the comparison concerns an optimized peak and need not hold at a fixed time.

**Source pointers.** Background anchor: [WM10, §3.11 (p. 141)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Exact finite-size reduction](../science/loss_frontier.md#2-exact-reduction-of-the-finite-size-optimization).

### M23: The exact attenuation exponent at fixed positive loss

**Central question.** What part of the long-chain optimum is fixed even when its finite-size formula is unknown?

**Understanding target.** Connect the equal-diagonal, product-saturating design to its factorial transfer expression and Stirling scaling. Compare it with the universal upper bound to identify $`2\ln(1+\kappa/\Gamma)`$ as the exact attenuation exponent, while leaving the optimized polynomial prefactor unresolved.

**Earlier dependencies and story role.** [M18](#m18-realizing-the-extremal-profile-with-local-reservoirs), [M21](#m21-the-finite-bound-with-unavoidable-loss), [M22](#m22-why-every-internal-rate-can-saturate-its-budget). Extracts a global asymptotic statement from upper and lower constructions.

**Conceptual connection.** Matching exponential rates can be exact even when the benchmark's algebraic prefactor is not optimal.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Fixed-loss exponent](../science/loss_frontier.md#3-equal-diagonal-rates-attain-the-fixed-loss-exponent) and [fixed-loss finite examples](../science/finite_examples.md#fixed-additional-loss).

### M24: The complete optimized weak-loss frontier

**Central question.** How can the full limiting transfer probability be matched when accumulated loss stays finite?

**Understanding target.** For $`n\kappa_n/\Gamma\to x`$, connect the finite upper bound to the slow-endpoint choice $`a_n=\Gamma n^{-\alpha}`$, $`1/2<\alpha<1`$. Explain why relay-delay fluctuations vanish relative to the endpoint response, endpoint waiting loss becomes subleading, and the optimized probability tends to $`(4/e^2)e^{-2x}`$.

**Earlier dependencies and story role.** [M19](#m19-relay-delay-fluctuations-and-endpoint-response-width), [M20](#m20-sharpness-with-bounded-coefficients-and-an-explicit-time-cost), [M21](#m21-the-finite-bound-with-unavoidable-loss), [M23](#m23-the-exact-attenuation-exponent-at-fixed-positive-loss). Matches the full asymptotic value, not only its exponential rate.

**Conceptual connection.** The two inequalities on the endpoint exponent separate delay spread from propagation time and charge unavoidable loss throughout both.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Exact weak-loss frontier](../science/loss_frontier.md#4-exact-optimized-weak-loss-frontier) and [time and tuning costs](../science/physical_interpretation.md#the-time-and-tuning-costs).

### M25: Finite designs, rigorous brackets, and asymptotic evidence

**Central question.** What can a computed finite chain establish about the proved optimum?

**Understanding target.** Distinguish the lower-bound-maximizing endpoint rule, exact evaluation of that selected family, the all-design upper bound, and the limiting frontier. Interpret the finite examples without treating the chosen equal endpoints, declared readout time, or numerical trend as a global optimizer.

**Earlier dependencies and story role.** [M20](#m20-sharpness-with-bounded-coefficients-and-an-explicit-time-cost), [M22](#m22-why-every-internal-rate-can-saturate-its-budget), [M23](#m23-the-exact-attenuation-exponent-at-fixed-positive-loss), [M24](#m24-the-complete-optimized-weak-loss-frontier). Connects the analytical classification to concrete finite devices.

**Conceptual connection.** Finite evaluations reveal convergence and physical timescales, while the converse and attaining sequence supply the universal conclusions.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Explicit finite endpoint choice](../science/finite_examples.md#an-explicit-finite-endpoint-choice), [exact selected-design evaluation](../science/finite_examples.md#exact-evaluation-of-the-selected-design), and [approach to the frontier](../science/finite_examples.md#approach-to-the-weak-loss-frontier).

### M26: Applying the inherited pure-loss capacity threshold

**Central question.** Which communication consequence follows from the optimized physical transmissivity?

**Understanding target.** Apply the established ordinary bosonic capacity formula to the weak-loss frontier and identify $`x_{\mathrm c}=(\ln 8-2)/2`$. Explain why the positivity threshold is unchanged by any fixed positive photon-number budget and why the numerical unconstrained bosonic capacity is distinct from a qubit-encoding capacity.

**Earlier dependencies and story role.** [M10](#m10-from-a-transfer-amplitude-to-the-complete-quantum-channel), [M11](#m11-transfer-probability-fidelity-and-communication-capacity), [M12](#m12-the-complete-physical-optimization-contract), [M24](#m24-the-complete-optimized-weak-loss-frontier). Connects the solved transfer law to a specified information task.

**Conceptual connection.** The capacity theorem is imported channel theory; the architecture result determines which channel parameters are achievable.

**Source pointers.** Background anchor: [WM10, Appendix A.2 (p. 404)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Ordinary bosonic capacity](../science/channel_consequences.md#ordinary-unassisted-bosonic-quantum-capacity), [finite-energy positivity](../science/channel_consequences.md#a-finite-energy-budget-preserves-the-positivity-threshold), and [optimized capacity](../science/channel_consequences.md#optimized-weak-loss-capacity).

### M27: The maximum-length law and its operational meaning

**Central question.** How do matching transfer bounds determine the longest path with positive unassisted capacity?

**Understanding target.** Explain the upper bound on $`n_{\max}`$ and the lower construction at any scaled loss below $`x_{\mathrm c}`$. Obtain $`(\kappa/\Gamma)n_{\max}\to x_{\mathrm c}`$ without assuming finite-size monotonicity, and distinguish mode count per fresh use from throughput, physical distance, and a sharp finite-size cutoff.

**Earlier dependencies and story role.** [M12](#m12-the-complete-physical-optimization-contract), [M21](#m21-the-finite-bound-with-unavoidable-loss), [M24](#m24-the-complete-optimized-weak-loss-frontier), [M26](#m26-applying-the-inherited-pure-loss-capacity-threshold). Completes the communication consequence with both directions of its asymptotic claim.

**Conceptual connection.** A channel threshold becomes a length law only after an all-design converse and a realizable family are combined under the same rate budget.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, Appendix A.2 (p. 404)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Asymptotic maximum length](../science/channel_consequences.md#the-asymptotic-maximum-length), [assistance boundaries](../science/channel_consequences.md#assistance-and-resource-boundaries), and [resource conventions](../science/physical_interpretation.md#what-the-resource-conventions-measure).

### M28: The bypass counterexample and the architectural boundary

**Central question.** Which broader claim is ruled out by a passive three-mode bypass?

**Understanding target.** Explain how a common loss channel and a Hermitian Hamiltonian produce a one-way triangular drift with two forward routes. Connect its exact value $`(4/e^2)(1+1/\pi^2)`$ to the failure of the single-convolution proof, while passivity and the single-mode channel task remain intact.

**Earlier dependencies and story role.** [M07](#m07-directional-interference-on-one-bond), [M08](#m08-the-drift-graph-and-the-communication-geometry), [M10](#m10-from-a-transfer-amplitude-to-the-complete-quantum-channel), [M16](#m16-the-unique-path-transfer-formula), [M17](#m17-the-universal-ceiling-and-its-exact-quantifiers), [M24](#m24-the-complete-optimized-weak-loss-frontier). Determines the scope of the whole optimization result through an explicit counterexample.

**Conceptual connection.** Directionality, passivity, and Markovianity alone do not impose the ceiling; the unique-path structure carries an independent physical restriction.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Bypass realization](../science/bypass.md#physical-realization), [exact amplitude](../science/bypass.md#exact-transfer-amplitude), and [why the proof no longer applies](../science/bypass.md#why-the-path-proof-no-longer-applies).

### M29: Inherited ingredients and the physical design conclusion

**Central question.** What remains of the contribution after its prior ingredients and full resource costs are made explicit?

**Understanding target.** Separate the established two-emitter constant, classical product extremum, bidiagonal response identity, directional reservoir construction, and capacity formula from the all-design physical transfer classification. Explain how bounded-rate endpoint engineering, exact loss optimization, and the bypass boundary fit together.

**Earlier dependencies and story role.** [M15](#m15-the-classical-extremum-for-the-edge-product), [M17](#m17-the-universal-ceiling-and-its-exact-quantifiers), [M20](#m20-sharpness-with-bounded-coefficients-and-an-explicit-time-cost), [M22](#m22-why-every-internal-rate-can-saturate-its-budget), [M24](#m24-the-complete-optimized-weak-loss-frontier), [M27](#m27-the-maximum-length-law-and-its-operational-meaning), [M28](#m28-the-bypass-counterexample-and-the-architectural-boundary). Synthesizes attribution, mechanism, and scope before the final global account.

**Conceptual connection.** The consequential statement is about which static scalar relay architectures can realize a quantum channel under a rate and loss budget, not a new numerical constant or a new pure-loss capacity theorem.

**Source pointers.** Background anchor: [WM10, §3.6 (p. 119)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Attribution map](../references/related_work.md#attribution-map), [physical interpretation](../science/physical_interpretation.md), and [loss-result boundaries](../science/loss_frontier.md#boundaries-of-the-result).

### M30: The complete design-limit picture

**Central question.** How do the ceiling, constructions, loss limits, communication law, and bypass form one coherent result?

**Understanding target.** Give a connected account of the exact physical contract, the sharp zero-extra-loss supremum, its bounded-rate approach, the endpoint-and-time reduction, both matched loss limits, and the unassisted length consequence. Preserve the distinction between proved optima, finite construction bounds, and the unresolved finite endpoint choice and general multipath problem.

**Earlier dependencies and story role.** [M12](#m12-the-complete-physical-optimization-contract), [M25](#m25-finite-designs-rigorous-brackets-and-asymptotic-evidence), [M26](#m26-applying-the-inherited-pure-loss-capacity-threshold), [M27](#m27-the-maximum-length-law-and-its-operational-meaning), [M28](#m28-the-bypass-counterexample-and-the-architectural-boundary), [M29](#m29-inherited-ingredients-and-the-physical-design-conclusion). Integrates the narrative into the complete project-level understanding target.

**Conceptual connection.** Local coherent–dissipative interference leads to a globally constrained response; changing endpoint timescales exploits that response, while an added forward route changes the class of possible responses.

**Source pointers.** Background anchor: [WM10, §6.6 (p. 312)](WISEMAN_MILBURN_BRIDGE.md#reading-route); [WM10, §3.2 (p. 99)](WISEMAN_MILBURN_BRIDGE.md#reading-route). Canonical account: [Scientific account](../science/README.md), [loss frontier](../science/loss_frontier.md), [channel consequences](../science/channel_consequences.md), and [architectural boundary](../science/bypass.md#why-the-path-proof-no-longer-applies).


