# Quantum-channel consequences

The physical transfer problem determines a transmissivity $`\eta`$. The resulting channel is the [pure-loss channel](model.md), so its communication properties follow from established channel theory. The capacity formulas and the half-transmission threshold below are inherited; the [loss frontier](loss_frontier.md) supplies the optimization over the allowed physical architectures.

## Transmissivity and state fidelity are different quantities

For a single-photon input, $`\eta`$ is the probability that the photon reaches the retained output oscillator. It is also the transmissivity of the full bosonic pure-loss channel. It is not the average fidelity for transferring an unknown qubit or an arbitrary bosonic state.

For example, restrict the input to the vacuum/one-photon qubit and correct the known output phase. The channel has amplitude-damping Kraus operators

```math
K_0=
\begin{pmatrix}
1&0\\
0&\sqrt\eta
\end{pmatrix},
\qquad
K_1=
\begin{pmatrix}
0&\sqrt{1-\eta}\\
0&0
\end{pmatrix}.
```

Its entanglement fidelity for a maximally mixed qubit input is

```math
F_{\mathrm e}
=
\frac14\sum_{\ell=0}^{1}
|\mathrm{Tr}K_\ell|^2
=
\frac{(1+\sqrt\eta)^2}{4}.
```

The uniform average over pure qubit inputs is

```math
F_{\mathrm{avg}}
=
\frac{2F_{\mathrm e}+1}{3}
=
\frac12+\frac{\sqrt\eta}{3}+\frac{\eta}{6}.
```

The relation follows by averaging two copies of a pure qubit projector, whose average is $`(I+\mathrm{Swap})/6`$. Thus the path transmissivity ceiling implies

```math
F_{\mathrm{avg}}
\le
\frac12+\frac{2}{3e}+\frac{2}{3e^2}
=
0.8354764829\ldots.
```

The value $`4/e^2\simeq54.13\%`$ should therefore be called a transfer-probability or transmissivity ceiling. In this qubit example its corresponding average state fidelity is about $`83.55\%`$. This conversion is standard channel algebra, not an additional transport bound.

## Ordinary unassisted bosonic quantum capacity

For a memoryless pure-loss bosonic channel with no input-energy constraint, the ordinary unassisted quantum capacity is [[Wolf07]](../references/related_work.md#references)

```math
Q(\eta)=
\begin{cases}
0,&0\le\eta\le\frac12,\\
\displaystyle\log_2\frac{\eta}{1-\eta},
&\frac12\lt \eta\lt 1.
\end{cases}
```

The units are qubits per channel use. The formula allows arbitrary bosonic encodings across independent uses. It is not the capacity formula for the two-dimensional vacuum/one-photon restriction discussed above.

The [operational contract](model.md) requires each use to start with vacuum relay modes and vacuum bath inputs. The network generator remains fixed during that use. The capacity includes terminal coding and decoding, but no intervention at intermediate relays, environmental monitoring, postselection, or classical feedback assistance.

Since the transmissivity of every allowed path is at most $`4/e^2\lt 1`$,

```math
Q\le
Q\!\left(\frac4{e^2}\right)
=
\log_2\frac4{e^2-4}
=
0.2391164821\ldots.
```

For each number of modes, this is the supremum of the **unconstrained bosonic** capacity in the zero-extra-loss model. Exact attainment occurs for two modes; with relays it is approached by the slow-endpoint construction.

This numerical ceiling assumes no bound on input photon number. It is not a throughput per unit time, and it does not account for the duration or resource cost of resetting the network between uses.

## A finite energy budget preserves the positivity threshold

A fixed positive input photon-number budget changes achievable rates, but does not change the zero-versus-positive threshold at $`\eta=1/2`$.

For $`\eta\le1/2`$, the pure-loss channel is antidegradable and its unassisted quantum capacity vanishes under any input constraint. For $`\eta>1/2`$, choose a thermal input with mean photon number $`0\lt N\le\overline N`$, where $`\overline N>0`$ is the budget. Its coherent information is

```math
I_{\mathrm c}(N,\eta)
=
g(\eta N)-g((1-\eta)N),
\qquad
g(y)=(y+1)\log_2(y+1)-y\log_2y,
```

with $`g(0)=0`$. Since $`g`$ is strictly increasing, this is positive whenever $`\eta>1/2`$. The standard coding result for the degradable pure-loss channel makes it an achievable positive rate [[Wolf07]](../references/related_work.md#references).

The length threshold below therefore does not rely on an unlimited photon supply merely to obtain a nonzero rate. The unconstrained capacity formula should still not be used as a finite-energy rate estimate.

## Optimized weak-loss capacity

Let

```math
Q_n^*(\delta)
=
\sup_{A_0,t}Q(\eta(t)),
\qquad
\delta=\frac{\kappa}{\Gamma}.
```

The function $`Q`$ is continuous and nondecreasing on the interval $`[0,4/e^2]`$. Thus

```math
Q_n^*(\delta)=Q(\eta_n^*(\delta)).
```

When $`n\delta_n\to x\in[0,\infty)`$, the exact physical frontier gives

```math
\lim_{n\to\infty}Q_n^*(\delta_n)
=
Q_*(x)
=
\max\!\left\{
0,\,
\log_2
\frac{4e^{-2-2x}}{1-4e^{-2-2x}}
\right\}.
```

Its positivity interval ends at

```math
\boxed{
x_{\mathrm c}
=
\frac{\log8-2}{2}
=
0.03972077084\ldots.
}
```

Here and in the attenuation exponents, $`\log`$ denotes the natural logarithm; capacities use $`\log_2`$.

At $`x=x_{\mathrm c}`$, the limiting transmissivity is $`1/2`$ and the limiting capacity is zero. This does not assert that every finite chain with $`n\delta=x_{\mathrm c}`$ has exactly zero capacity. A small positive finite-size capacity could still tend to zero at the limiting boundary.

## The asymptotic maximum length

For $`\delta>0`$, define

```math
n_{\max}(\delta)
=
\max\left(
\{n\ge2:\eta_n^*(\delta)>1/2\}\cup\{0\}
\right).
```

The value is zero if no chain with at least two modes has positive unassisted capacity. The finite-size upper bound makes this maximum finite. No monotonicity of the exact finite-size optimum in $`n`$ is assumed.

Positive capacity requires

```math
\frac4{e^2}(1+\delta)^{-2(n-1)}>\frac12,
```

or equivalently

```math
n-1\lt \frac{x_{\mathrm c}}{\log(1+\delta)}.
```

It follows that

```math
\limsup_{\delta\downarrow0}
\delta\,n_{\max}(\delta)\le x_{\mathrm c}.
```

Conversely, fix any $`0\lt x\lt x_{\mathrm c}`$ and take $`n(\delta)=\lfloor x/\delta\rfloor`$. As $`\delta\downarrow0`$, these lengths tend to infinity and $`n(\delta)\delta\to x`$. The attainable weak-loss frontier gives

```math
\eta_{n(\delta)}^*(\delta)
\longrightarrow
\frac4{e^2}e^{-2x}>\frac12.
```

For sufficiently small $`\delta`$, these lengths therefore support positive capacity. Hence $`n_{\max}(\delta)\ge n(\delta)`$, which gives the matching lower limit after taking $`x\uparrow x_{\mathrm c}`$. Thus

```math
\boxed{
\lim_{\delta\downarrow0}
\delta\,n_{\max}(\delta)=x_{\mathrm c},
\qquad
n_{\max}(\delta)\sim
0.03972077084\,\frac{\Gamma}{\kappa}.
}
```

This is an asymptotic statement about existence of a positive ordinary quantum capacity. It is not a sharp finite-size design rule, a lower bound on a useful finite-block rate near the boundary, or a claim about communication speed.

## Assistance and resource boundaries

Two-way classical assistance changes the communication task. A pure-loss channel with any $`\eta>0`$ has positive two-way-assisted quantum and secret-key capacities [[PLOB17]](../references/related_work.md#references). The half-transmission cutoff used here is therefore specific to ordinary unassisted quantum communication. It is not an entanglement-breaking cutoff.

The output is one physical mode at one chosen time. Access to emitted fields, joint recovery from several output modes, stored excitations in additional registers, repeated intervention within a use, or a different reset and memory model would define a different channel task. The loss–distance result applies to the contract specified in [model](model.md); [physical interpretation](physical_interpretation.md) discusses the distinction between internal-mode transfer and traveling-wave transmission.

