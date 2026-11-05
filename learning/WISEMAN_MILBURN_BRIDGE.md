# From open quantum systems to directional relay limits

Consider two cavities. A state is loaded into the first cavity, all other modes begin empty, and a fixed device couples them for a chosen time. The receiver keeps the second cavity and discards everything else. The question is how well the device transfers the state, including coherence with a distant reference.

This setting leads from the open-system foundations in **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control* (Cambridge University Press, 2010)** to this project's limits on static directional paths. This is the single educational anchor, identified as **WM10** in the [structured bibliography](../references/references.bib). The [30-milestone map](MILESTONES.md) organizes the complete scientific story; the bridge below supplies a continuous route into it.

[Official book page](https://www.cambridge.org/core/books/quantum-measurement-and-control/F78F445CD9AF00B10593405E9BAC6B9F) · [Official front matter](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) · [Official contents](https://assets.cambridge.org/97805218/04424/toc/9780521804424_toc.pdf)

The section numbers and starting pages below are verified against the official contents. The front matter confirms first publication in 2010. Full chapter text was not inspected for this bridge, so no textbook equation numbers or exact symbol-by-symbol correspondence are asserted. The equations and examples below are supplied locally in the repository's conventions, with their authoritative scientific homes linked.

## Reading route

The anchor supplies foundations for describing an open quantum device. The path optimization requires further arguments developed in the scientific account.

| Anchor location | Concept needed here | Connection to the project |
|---|---|---|
| Appendix A.4, p. 410 | A bosonic mode, its annihilation operator, vacuum, and number states | Defines the physical input, relays, and retained output. |
| Appendix A.2, p. 404 | Composite systems and entanglement | Explains why transfer must work when the input has an external reference, and why discarded modes form an environment. |
| Section 3.2, p. 99: *The Born–Markov master equation* | Replacing bath dynamics by a time-local equation under appropriate approximations | Introduces the setting for one fixed Markovian generator. |
| Section 3.6, p. 119: *The Lindblad form and positivity* | A physically valid dissipative evolution | Leads to the constraint tying directional hopping to damping. |
| Section 3.11, p. 141: *Heisenberg-picture dynamics* | Evolution of observables rather than density matrices | Gives the closed equation for oscillator amplitudes. |
| Section 6.6, p. 312: *Linear quantum systems* | Linear drift and quantum fluctuations | Connects a finite drift matrix to a quantum channel with vacuum noise. |
| Appendix B.1, p. 418; B.2, p. 420; B.4, p. 423 | White-noise increments, stochastic calculus, and solutions of stochastic equations | Supports a bath-noise formulation. The finite matrix and master-equation derivations below can be followed without first developing that machinery. |

The selected sections are entry points, not an instruction to read the entire book. The relevant background ends with the [precise operational contract](../science/model.md). Measurement records, adaptive feedback, and conditional trajectories are not resources in that contract.

## Notation and rate conventions

The following map connects the source's subject matter to notation fixed for this project. It does not assume that every chapter uses identical symbols.

| Object | Project notation and meaning |
|---|---|
| State | $`\rho`$ is the density operator of the retained device modes. |
| Bosonic mode | $`a_j`$ lowers the excitation number of mode $`j`$; $`[a_j,a_k^\dagger]=\delta_{jk}`$. |
| Passive Hamiltonian | $`H=a^\dagger h a`$, where $`a=(a_1,\ldots,a_n)^T`$ and $`h=h^\dagger`$. It conserves total excitation number. |
| Loss coupling | $`L_\mu=\sum_jK_{\mu j}a_j`$. Each row of $`K`$ specifies a vacuum loss channel. |
| Drift | $`A=-ih-K^\dagger K/2`$ determines the evolution of first moments. It is not the full density-operator generator. |
| Local damping | $`\nu_j=-\mathrm{Re}\,(A_0)_{jj}`$ is the engineered amplitude decay rate. Before additional loss, $`A_0=A`$; with it, $`A=A_0-\kappa I`$. |
| Budget and additional loss | $`\Gamma`$ caps engineered diagonal amplitude damping; $`\kappa`$ is an independent additional amplitude decay rate. |
| Transfer | $`G(t)=[e^{At}]_{n1}`$ is the input-to-output amplitude coefficient; $`\eta(t)=|G(t)|^2`$ is the transmissivity. |

We set $`\hbar=1`$ and use

```math
\dot\rho=-i[H,\rho]+\sum_\mu\mathcal D[L_\mu]\rho,
\qquad
\mathcal D[L]\rho=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The rate is absorbed into the jump operator. For one isolated mode, a term $`\gamma\mathcal D[a]\rho`$ is equivalent to the jump $`L=\sqrt{\gamma}\,a`$. It gives

```math
\frac{d}{dt}\langle a\rangle=-\frac{\gamma}{2}\langle a\rangle,
\qquad
\frac{d}{dt}\langle a^\dagger a\rangle=-\gamma\langle a^\dagger a\rangle.
```

Thus a population decay rate $`\gamma`$ corresponds to the amplitude rate $`\nu=\gamma/2`$. In particular, the extra loss $`\kappa`$ used here is implemented by $`L=\sqrt{2\kappa}\,a`$. Its amplitude factor is $`e^{-\kappa t}`$ and its population factor is $`e^{-2\kappa t}`$. The factor of two in the loss frontier follows from this convention.

The entries of $`h`$ and $`A`$ have units of inverse time; entries of $`K`$ have units of inverse square root of time. The cap $`\nu_j\le\Gamma`$ is not a separate cap $`|w_j|\le\Gamma`$ on every hopping.

### From the master equation to the drift

The adjoint master equation gives, for an operator $`O`$,

```math
\frac{d}{dt}\langle O\rangle
=i\langle[H,O]\rangle
+\frac12\sum_\mu
\left\langle
L_\mu^\dagger[O,L_\mu]+[L_\mu^\dagger,O]L_\mu
\right\rangle.
```

For $`O=a_j`$, annihilation operators commute with each other, while $`[L_\mu^\dagger,a_j]=-K_{\mu j}^*`$. The Hamiltonian and loss contributions therefore close on the vector of annihilation operators:

```math
\frac{d}{dt}\langle a\rangle=A\langle a\rangle,
\qquad
A=-ih-\frac12K^\dagger K,
\qquad
A+A^\dagger=-K^\dagger K\preceq0.
```

The last inequality means that the Hermitian part of $`A`$ is negative semidefinite. It is the passivity constraint used in the proof. It couples the permitted off-diagonal drift to the diagonal losses; one cannot specify large directional hoppings and independently remove the loss required by the same quantum realization.

Conversely, a finite matrix satisfying this inequality admits the passive realization

```math
K^\dagger K=-(A+A^\dagger),
\qquad
h=\frac{i}{2}(A-A^\dagger).
```

Taking a positive-semidefinite matrix square root supplies a suitable $`K`$. The project uses more local adjacent-pair factorizations when constructing paths. The [model](../science/model.md) and [attainable designs](../science/attainable_designs.md) give the complete statements.

## Physical assumptions

The textbook framework permits many open-system models. The following restrictions select the one whose optimization is solved here.

| Assumption | Where it matters |
|---|---|
| Time-independent passive Hamiltonian and annihilation-only loss jumps | Excludes gain, squeezing, and time-dependent waveform control during propagation. |
| Markovian dynamics | Together with time-independent coefficients, makes one constant drift matrix govern the entire use. Retarded giant-atom couplings and dispersion-engineered traveling fields need a different description. |
| One scalar oscillator per site and a lower-bidiagonal drift | Leaves exactly one route from input to output: each site influences only its immediate downstream neighbor. |
| Vacuum auxiliaries and vacuum input fields | Makes the retained single-mode channel quantum-limited pure loss rather than a thermal or amplified channel. |
| One physical input mode and one physical output mode at a chosen time | Defines a stored-state task, distinct from continuous-wave port scattering or joint recovery from several outputs. |
| Other modes and fields are discarded, without monitoring or postselection | The reported probability is unconditional. |
| Additional loss acts on every mode, including the slow endpoints | Charges the complete propagation and waiting time in the loss frontier. |

A matrix equation for first moments alone does not establish a quantum-state transfer claim. A one-photon number state, for example, has zero mean amplitude both before and after transfer. The quantum interpretation also needs the environmental noise.

For the passive vacuum model, the retained annihilation operator has the form

```math
a_{\mathrm{out}}
=G(t)a_{\mathrm{in}}
+\sqrt{1-|G(t)|^2}\,e,
```

up to a known output phase. Here $`e`$ is a normalized environmental annihilation operator in the vacuum, independent of the input and its reference. Preservation of the output commutator fixes its coefficient. This is a statement about the entire pure-loss channel, so it applies to non-Gaussian inputs and reference-entangled states as well as to first moments. The derivation is in [model](../science/model.md#reduction-to-a-pure-loss-channel).

## A complete two-mode example

This example connects a master equation, a physical directional coupling, a transfer amplitude, and an observed output. It is a local derivation of the established two-mode response, whose optical antecedents are [Stobinska09 and Wang11](../references/related_work.md#references).

### Device and initialization

Let $`\nu>0`$ and take two modes with zero onsite frequency. Choose

```math
H=i\nu(a_2^\dagger a_1-a_1^\dagger a_2),
\qquad
L=\sqrt{2\nu}\,(a_1-a_2).
```

The Hamiltonian transfers excitations between the two modes without creating them. The jump describes one common vacuum loss channel. In matrix form,

```math
h=
\begin{pmatrix}0&-i\nu\\i\nu&0\end{pmatrix},
\qquad
K=\sqrt{2\nu}\begin{pmatrix}1&-1\end{pmatrix}.
```

Combining their contributions gives

```math
A=-ih-\frac12K^\dagger K
=
\begin{pmatrix}-\nu&0\\2\nu&-\nu\end{pmatrix},
\qquad
A+A^\dagger=
-2\nu
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\preceq0.
```

The coherent and dissipative contributions cancel from the upper off-diagonal entry and add in the lower one. Mode 1 influences mode 2; mode 2 does not influence mode 1. This interference mechanism is established reservoir engineering [MetelmannClerk15](../references/related_work.md#references), specialized here to a simple choice of phases.

Load the state into mode 1 at time zero. Mode 2 and the bath begin in vacuum. Evolve with this fixed generator and retain mode 2 at time $`t`$.

### Propagation and readout

The nilpotent off-diagonal part of $`A`$ squares to zero, so its exponential is

```math
e^{At}
=e^{-\nu t}
\begin{pmatrix}1&0\\2\nu t&1\end{pmatrix},
\qquad
G(t)=2\nu t\,e^{-\nu t}.
```

For a single photon initially in mode 1, the unnormalized one-excitation component inside the two cavities is

```math
|\widetilde\psi(t)\rangle
=e^{-\nu t}|1,0\rangle
+2\nu t\,e^{-\nu t}|0,1\rangle.
```

Any photon lost to the bath leaves both cavities in vacuum. Consequently the complete unconditional device state is

```math
\rho_{12}(t)
=|\widetilde\psi(t)\rangle\langle\widetilde\psi(t)|
+\left(1-\langle\widetilde\psi(t)|\widetilde\psi(t)\rangle\right)
|0,0\rangle\langle0,0|.
```

The probabilities for a photon in the sender, a photon in the receiver, and a photon lost to the bath are

```math
p_1=e^{-2\nu t},
\qquad
p_2=4\nu^2t^2e^{-2\nu t},
\qquad
p_{\mathrm{loss}}=1-p_1-p_2.
```

These probabilities include every outcome. No successful detection is selected in defining the channel. Tracing out the sender gives

```math
\rho_2(t)
=(1-\eta(t))|0\rangle\langle0|
+\eta(t)|1\rangle\langle1|,
\qquad
\eta(t)=4\nu^2t^2e^{-2\nu t}.
```

For $`t>0`$,

```math
\frac{d}{dt}\log\eta(t)=\frac2t-2\nu.
```

The unique peak occurs at $`t_*=1/\nu`$, with

```math
\eta(t_*)=\frac4{e^2},
\qquad
p_1(t_*)=e^{-2},
\qquad
p_{\mathrm{loss}}(t_*)=1-5e^{-2}.
```

The receiver holds approximately 54.13% of the initial one-photon probability at that time. It continues to decay afterwards; the device has not created permanent storage.

### Coherence and arbitrary input states

The experiment is not limited to photon counting. For the vacuum/one-photon input $`|\psi\rangle=\alpha|0\rangle+\beta|1\rangle`$, with $`|\alpha|^2+|\beta|^2=1`$, the receiver's density matrix in that basis is

```math
\rho_2(t)=
\begin{pmatrix}
|\alpha|^2+(1-\eta)|\beta|^2&
\sqrt{\eta}\,\alpha\beta^*\\
\sqrt{\eta}\,\alpha^*\beta&
\eta|\beta|^2
\end{pmatrix}.
```

Here $`G(t)\ge0`$, so $`G=\sqrt\eta`$. The off-diagonal entries show the surviving coherence. Loss affects an unknown superposition differently from a photon-number probability, so $`\eta`$ is not a general state fidelity. The [channel consequences](../science/channel_consequences.md#transmissivity-and-state-fidelity-are-different-quantities) make that distinction quantitative.

For arbitrary bosonic inputs, including inputs entangled with a reference, use the vacuum-noise channel relation above. The two-dimensional example illustrates it without restricting the full theorem to a qubit encoding.

### The same example with unavoidable loss

Add independent jumps $`\sqrt{2\kappa}\,a_1`$ and $`\sqrt{2\kappa}\,a_2`$. The engineered Hamiltonian and shared jump remain fixed, while $`A`$ changes to $`A-\kappa I`$. Therefore

```math
G_\kappa(t)=2\nu t\,e^{-(\nu+\kappa)t},
\qquad
t_*=\frac1{\nu+\kappa},
\qquad
\eta_{\max}=\frac4{e^2}
\left(\frac{\nu}{\nu+\kappa}\right)^2.
```

Under the engineered damping cap $`0<\nu\le\Gamma`$, the best matched pair uses $`\nu=\Gamma`$. This realizes the exact two-mode optimum proved in [loss frontier](../science/loss_frontier.md#1-universal-finite-size-bound). The longer-path problem needs a converse over unequal rates and every admissible coupling, not just this symmetric example.

## From two modes to the full path

Four additional steps connect the example to the all-design theorem. The anchor's open-system foundations make the model meaningful; they do not replace these proof steps.

### 1. Bound the whole path product

For the strict path, $`A_{jj}=-\nu_j-i\omega_j`$ and $`A_{j+1,j}=w_j`$. Complete positivity constrains all the edges together:

```math
\prod_{j=1}^{n-1}|w_j|
\le
2\sqrt{\nu_1\nu_n}\prod_{j=2}^{n-1}\nu_j.
```

Applying only a two-by-two positivity bound independently to each edge misses this stronger global restriction. The sharp inequality is a weighted-shift consequence of the classical Berger/Pearcy numerical-radius bound; its saturating normalized edge profile is the Crabb matrix. These are imported primary ingredients [Pearcy1966, Crabb1971, LewisOverton2020](../references/related_work.md#classical-operator-theory), not textbook results newly proved by this project. The [path proof](../science/path_ceiling.md#2-the-sharp-path-product-inequality) also gives a self-contained Perron-vector derivation.

### 2. Use the unique directed route

Successive variation of constants expresses the endpoint coefficient as one product times one causal convolution:

```math
[e^{At}]_{n1}
=\left(\prod_jw_j\right)
(f_{\nu_1+i\omega_1}*\cdots*f_{\nu_n+i\omega_n})(t),
\qquad
f_z(t)=e^{-zt}\mathbf1_{\{t\ge0\}}.
```

Convolution combines responses whose nonnegative time intervals sum to the total elapsed time. This identity is standard linear-system algebra, also covered by the bidiagonal divided-difference formula [Higham2024](../references/related_work.md#references).

If any $`\nu_j=0`$, passivity forces the incident path couplings to vanish, so endpoint transfer is zero. The remaining argument takes all $`\nu_j>0`$.

Taking the absolute value shows that onsite detunings cannot improve the response beyond the resonant path with the same rates and coupling magnitudes. Applying the sharp product bound leaves the two-endpoint response $`F_{a,b}=2\sqrt{ab}\,(f_a*f_b)`$ convolved with normalized internal kernels:

```math
|[e^{At}]_{n1}|
\le(F_{\nu_1,\nu_n}*k_2*\cdots*k_{n-1})(t),
\qquad
k_j(s)=\nu_je^{-\nu_js}\mathbf1_{\{s\ge0\}}.
```

Each internal kernel integrates to one. Its probability-density interpretation is an analytical representation of the impulse response, not an environmental measurement record or a claim that the quantum device follows a measured classical trajectory.

### 3. Take the peak and keep the quantifiers

The unequal-endpoint calculation gives $`\sup_tF_{\nu_1,\nu_n}(t)\le2/e`$. Averaging a function over positive normalized delays cannot raise its maximum. Consequently every admissible path obeys

```math
|[e^{At}]_{n1}|\le\frac2e,
\qquad
\eta(t)\le\frac4{e^2}.
```

The quantifier includes every finite number of relays, every allowed static rate and coupling, every onsite frequency, and every readout time. With at least one relay, each finite-rate design has strict inequality at finite time because the positive internal delay has an unbounded tail. This is why attainment for two modes and a supremum for longer paths are different statements.

### 4. Construct paths that approach the bound

Set the internal rates to $`\Gamma`$ and the two endpoint rates to $`a`$. With the physically realizable product-saturating couplings, the internal delay has mean $`(n-2)/\Gamma`$ and variance $`(n-2)/\Gamma^2`$. Making the endpoint response width $`1/a`$ large compared with the delay spread preserves the two-endpoint peak.

The [explicit construction](../science/attainable_designs.md) supplies both the local jumps and a finite lower bound. A useful asymptotic choice is

```math
a_n=\Gamma n^{-\alpha},
\qquad
\frac12<\alpha<1,
\qquad
t_n=\frac{n-2+n^\alpha}{\Gamma}.
```

The first inequality on $`\alpha`$ suppresses delay fluctuations relative to the endpoint width. The second makes endpoint waiting subleading to the transit time. Local coefficients remain bounded, while endpoint rates decrease. This removes the equal-diagonal family's algebraic dilution, but does not raise the ceiling.

## Loss and communication consequences

The long-path result cannot be inferred by simply attaching a loss factor to an arbitrarily chosen ideal readout time. Extra loss changes which rates and times are useful. The [loss proof](../science/loss_frontier.md) supplies both a converse and attaining designs.

For $`\delta=\kappa/\Gamma`$, every design satisfies

```math
\eta(t)\le\frac4{e^2}(1+\delta)^{-2(n-1)}.
```

This is an exact upper bound, not generally the exact finite-size optimum. At fixed positive $`\delta`$, a matching lower construction determines the optimal exponential attenuation rate; it does not settle the optimum's polynomial prefactor.

There is also an exact finite-size reduction. An internal factor $`\nu e^{-(\nu+\kappa)t}`$ can be written as the corresponding factor at rate $`\Gamma`$ convolved with a positive measure of mass at most one. Replacing each internal rate by $`\Gamma`$, and readjusting the product-saturating physical couplings, therefore cannot lower the best peak over time. The remaining exact optimization is over the two endpoint rates and readout time. Equal optimal endpoints are not assumed or proved by that reduction.

When $`n\delta_n\to x`$ with $`0\le x<\infty`$, the slow-endpoint family above matches the converse:

```math
\lim_{n\to\infty}\eta_n^*(\delta_n)
=\frac4{e^2}e^{-2x}.
```

Its total added amplitude loss is governed by $`\kappa_nt_n=\delta_n(n-2+n^\alpha)\to x`$. This charges loss during endpoint waiting as well as propagation.

The conversion from transmissivity to capacity then uses primary channel theory [Wolf07, PLOB17](../references/related_work.md#references), not an assumed theorem from the educational anchor. Ordinary unassisted pure-loss quantum capacity is positive exactly when $`\eta>1/2`$. Combining this inherited threshold with the optimized physical frontier gives

```math
\lim_{\delta\downarrow0}\delta\,n_{\max}(\delta)
=\frac{\ln8-2}{2}.
```

The logarithm here is natural. This limit concerns existence of a positive rate per independent, freshly initialized channel use. It is not a fixed finite-size threshold, a transmission speed, or a cutoff for two-way-assisted entanglement distribution. The precise channel formulas and order of limits are in [channel consequences](../science/channel_consequences.md).

## Where the path assumption enters

Passivity and one-way propagation alone are insufficient for the ceiling. The [bypass example](../science/bypass.md) adds one direct input-to-output edge to a three-mode directional network. Its drift remains passive and lower triangular, but is no longer lower bidiagonal. At a specified time it has

```math
\eta=\frac4{e^2}\left(1+\frac1{\pi^2}\right)
>\frac4{e^2}.
```

There are now two coherent routes. The propagator is a sum of route contributions, so the single-product, single-positive-convolution proof no longer applies. A common waveguide or a composite reciprocal node must therefore be assessed from its actual drift and retained outputs, not from a drawing of sites in a line.

The [physical interpretation](../science/physical_interpretation.md) connects this boundary to known reservoir-engineered arrays. The [related-work account](../references/related_work.md) distinguishes giant atoms, dispersion shaping, autonomous dark-state transfer, and reciprocal multimode schemes from this scalar path task.

## Foundations, imported ingredients, and project results

| Layer | What it supplies | Authoritative location |
|---|---|---|
| Educational anchor WM10 | Open-system, positivity, Heisenberg, oscillator, and linear-system foundations | The verified section pointers in [reading route](#reading-route). |
| Local explanatory derivation | The rate convention, drift calculation, physical matched pair, and its unconditional output | The worked example here, consistent with [model](../science/model.md) and [attainable designs](../science/attainable_designs.md). |
| Imported primary mathematics and physics | Numerical-radius product extremum, Crabb profile, bidiagonal function identity, two-mode absorption peak, directionality mechanism, and capacity formulas | [Related work](../references/related_work.md) and [structured bibliography](../references/references.bib). |
| Project-specific analysis | Complete scalar-path ceiling, bounded-rate approach, finite optimization reduction, matched loss laws, and architectural boundary | [Science index](../science/README.md), leading to the exact statements and proofs. |

The [finite examples](../science/finite_examples.md) show how the proven bounds constrain concrete designs. Their reproduced curves illustrate the analytical results and distinguish an explicit family from the all-design optimum. [Reproducibility](../REPRODUCIBILITY.md) gives the commands and verification scope.
