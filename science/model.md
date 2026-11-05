# Model and communication task

We study the transfer of a state initially stored in one physical oscillator to a second physical oscillator through a static sequence of directional relays. The input and output are internal modes of the device. The performance measure is the resulting quantum channel at a chosen time, rather than a stationary scattering coefficient.

The architecture has one oscillator per site, vacuum environments, and a strictly one-way nearest-neighbor drift. These restrictions are essential: [a three-mode passive network with a bypass](bypass.md) already exceeds the path ceiling.

## Passive Markovian dynamics

Let $`a=(a_1,\ldots,a_n)^T`$ collect the annihilation operators of $`n\ge2`$ bosonic modes. Set $`\hbar=1`$ and use the Lindblad convention

```math
\frac{d\rho}{dt}
=
-i[H,\rho]
+\sum_\mu \mathcal D[L_\mu]\rho,
\qquad
\mathcal D[L]\rho
=
L\rho L^\dagger
-\frac12\{L^\dagger L,\rho\}.
```

The Hamiltonian and coupling operators are

```math
H=a^\dagger h a,
\qquad h=h^\dagger,
\qquad
L_\mu=\sum_{j=1}^{n}K_{\mu j}a_j.
```

All coefficients are finite and time independent. The Hamiltonian conserves excitation number, the coupling operators contain annihilation operators only, and every input field is in vacuum. Thus the network has no amplification, squeezing interaction, coherent drive, or supplied excitation outside the input state.

The first moments obey

```math
\frac{d}{dt}\langle a\rangle=A\langle a\rangle,
\qquad
A=-ih-\frac12K^\dagger K,
\qquad
A+A^\dagger=-K^\dagger K\preceq0.
```

This last inequality is the passivity constraint used throughout. Conversely, every finite matrix satisfying $`A+A^\dagger\preceq0`$ has a realization of this form: take

```math
K^\dagger K=-(A+A^\dagger),
\qquad
h=\frac{i}{2}(A-A^\dagger).
```

The bath factorization need not be unique. The [attaining designs](attainable_designs.md) have an explicit realization using only jumps supported on adjacent pairs.

Coherent and dissipative couplings can cancel in one propagation direction while adding in the other. This mechanism and its relation to cascaded quantum systems are established ingredients of reservoir engineering [[MetelmannClerk15]](../references/related_work.md#references).

## Strictly directional scalar paths

The required drift is lower bidiagonal:

```math
A=
\begin{pmatrix}
-\nu_1-i\omega_1 & 0 & \cdots & 0\\
w_1 & -\nu_2-i\omega_2 & \ddots & \vdots\\
0 & w_2 & \ddots & 0\\
\vdots & \ddots & w_{n-1} & -\nu_n-i\omega_n
\end{pmatrix}.
```

Here $`\nu_j\ge0`$, $`\omega_j\in\mathbb R`$, and $`w_j\in\mathbb C`$. More explicitly, the only allowed off-diagonal entries are $`A_{j+1,j}=w_j`$ for $`1\le j<n`$. The equation for mode $`j+1`$ can depend on mode $`j`$, while the reverse dependence vanishes. There is exactly one directed route from site $`1`$ to site $`n`$.

The condition applies to the complete drift, including the coherent and dissipative contributions. It does not require either contribution to be directional separately. It is also stronger than one-way transmission at a selected scattering frequency.

The numbers $`\nu_j`$ are **amplitude damping rates**. An isolated mode with drift $`-\nu_j-i\omega_j`$ has amplitude decay $`e^{-\nu_jt}`$ and occupation decay $`e^{-2\nu_jt}`$. Frequencies, damping rates, and hopping coefficients have units of inverse time.

## Operational contract

| Component | Assumption |
|---|---|
| Input | An arbitrary state of physical mode $`1`$, possibly entangled with an external reference. |
| Other modes | Physical modes $`2,\ldots,n`$ begin in vacuum. |
| Environments | All input bath fields begin in vacuum and are inaccessible during and after transmission. |
| Propagation | One fixed passive Lindblad generator acts for a chosen duration $`t\ge0`$. |
| Output | Retain physical mode $`n`$ at time $`t`$ and trace out every other mode and field. |
| Design optimization | The allowed rates, frequencies, couplings, and readout time can be chosen before the use. |
| Relay operations | No time modulation, measurements, feedback, postselection, or intermediate reset is performed during a use. |

A known output phase is a deterministic local unitary and does not affect the transmissivity or quantum capacities considered here. Selecting an output time does not make the output a permanent memory: the receiving oscillator generally continues to decay if it remains coupled to the network.

The [capacity consequences](channel_consequences.md) concern independent repetitions of this channel. Each repetition starts with fresh vacuum modes and bath inputs. Coding across repetitions and terminal decoding are allowed when defining a capacity; they do not change the static propagation rule inside an individual use.

## Reduction to a pure-loss channel

Write $`M(t)=e^{At}`$. The passive vacuum dilation gives the Heisenberg evolution of the retained mode in the form

```math
a_n(t)
=
M_{n1}(t)a_1(0)
+\sum_{j=2}^{n}M_{nj}(t)a_j(0)
+\text{bath annihilation operators}.
```

The environmental terms contain no creation operators. They act on vacuum degrees of freedom that are independent of the input and its reference. Preservation of the output commutator implies that the total squared coefficient of these terms is

```math
1-|M_{n1}(t)|^2.
```

In particular, $`0\le |M_{n1}(t)|^2\le1`$. If this quantity is less than one, the environmental linear combination can be normalized to a single vacuum mode $`e`$. Therefore

```math
a_{\mathrm{out}}
=
G(t)a_{\mathrm{in}}
+\sqrt{1-|G(t)|^2}\,e,
\qquad
G(t)=[e^{At}]_{n1}.
```

Up to the phase of $`G(t)`$, this is the quantum-limited pure-loss channel

```math
\mathcal N_t=\mathcal L_{\eta(t)},
\qquad
\eta(t)=|G(t)|^2.
```

The reduction holds for arbitrary input states and reference systems, not only for coherent states, Gaussian inputs, or single excitations. The Gaussian description characterizes the channel itself. The capacity formulas used later are standard properties of this channel class [[Wolf07]](../references/related_work.md#references).

For a one-photon input, $`\eta(t)`$ is the probability of finding that photon in the output oscillator. For a general quantum state, transmissivity is a channel parameter and should not be identified with state fidelity.

## Additional unavoidable loss and the rate budget

The [loss frontier](loss_frontier.md) separates the engineered path drift $`A_0`$ from independent unavoidable loss:

```math
A=A_0-\kappa I,
\qquad
A_0+A_0^\dagger\preceq0,
\qquad
0\le\nu_j=-\operatorname{Re}(A_0)_{jj}\le\Gamma.
```

Here $`\Gamma>0`$ bounds the engineered diagonal amplitude damping, and $`\kappa\ge0`$ is an additional amplitude damping rate on every mode. The added jumps are $`\sqrt{2\kappa}\,a_j`$. Passivity is imposed on $`A_0`$ separately, so the unavoidable loss cannot be canceled by gain.

This is a bound on diagonal damping rather than a separate restriction $`|w_j|\le\Gamma`$. Complete positivity already limits the edge couplings; the constructions use coefficients bounded by constants times $`\Gamma`$. The near-ceiling family in [attainable designs](attainable_designs.md) satisfies the stronger edge bound $`|w_j|\le\Gamma`$.

## Scope

The conclusions apply to this single-mode input, single-mode output, scalar path contract. They do not assert a bound on reciprocal chains, general directed graphs, internal multimode nodes, time-dependent control, monitored or postselected evolution, nonlinear couplings, or non-Markovian waveguides. A standard cascade through one shared field can generate drift couplings between nonadjacent modes and therefore need not belong to this path class.

The [path ceiling](path_ceiling.md) proves the universal upper bound; [attainable designs](attainable_designs.md) identify its resource costs; [loss frontier](loss_frontier.md) treats uniform extra loss; and [bypass](bypass.md) gives an exact boundary example.

