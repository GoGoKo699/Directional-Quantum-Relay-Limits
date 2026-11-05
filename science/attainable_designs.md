# Physical designs and the cost of approaching the ceiling

The [path ceiling](path_ceiling.md) is sharp for every number of modes. With two modes it is attained exactly. With one or more relays it is approached by making the endpoints slow compared with the fluctuations in the relay delay.

The construction uses adjacent loss couplings and static coherent hoppings. Its local coefficients remain bounded as the chain grows. The required endpoint rates and readout time are explicit.

## A local realization of the sharp product profile

First fix arbitrary positive diagonal amplitude damping rates $`\nu_1,\ldots,\nu_n`$. For $`n\ge3`$, choose real positive drift couplings

```math
w_1=\sqrt{2\nu_1\nu_2},
\qquad
w_{n-1}=\sqrt{2\nu_{n-1}\nu_n},
\qquad
w_j=\sqrt{\nu_j\nu_{j+1}}
\quad(2\le j\le n-2).
```

These are the product-saturating weights from the classical weighted-shift extremum [[Crabb1971, LewisOverton2020]](../references/related_work.md#references). They have the following adjacent-pair jump realization:

```math
\begin{aligned}
L_1&=\sqrt{2\nu_1}\,a_1-\sqrt{\nu_2}\,a_2,\\
L_j&=\sqrt{\nu_j}\,a_j-\sqrt{\nu_{j+1}}\,a_{j+1},
&&2\le j\le n-2,\\
L_{n-1}&=\sqrt{\nu_{n-1}}\,a_{n-1}-\sqrt{2\nu_n}\,a_n.
\end{aligned}
```

The middle line is empty for $`n=3`$. Every internal mode appears in two jumps, while each endpoint has the factor $`\sqrt2`$ in its single jump. Consequently,

```math
(K^\dagger K)_{jj}=2\nu_j,
\qquad
(K^\dagger K)_{j+1,j}=(K^\dagger K)_{j,j+1}=-w_j.
```

Choose zero onsite frequencies and the Hermitian current Hamiltonian

```math
H=
\frac{i}{2}\sum_{j=1}^{n-1}
w_j\left(a_{j+1}^\dagger a_j-a_j^\dagger a_{j+1}\right).
```

The Hamiltonian contributes $`+w_j/2`$ to the lower drift entry and $`-w_j/2`$ to the upper one. The dissipator contributes $`+w_j/2`$ to both. Thus

```math
A_{jj}=-\nu_j,
\qquad
A_{j+1,j}=w_j,
\qquad
A_{j,j+1}=0.
```

The Hamiltonian–dissipator cancellation is the standard directional reservoir-engineering mechanism [[MetelmannClerk15]](../references/related_work.md#references). The construction also proves directly that saturation of the path-product bound is physically compatible with arbitrary positive diagonal rates.

For $`n=2`$, use instead

```math
L_1=\sqrt{2\nu_1}\,a_1-\sqrt{2\nu_2}\,a_2,
\qquad
w_1=2\sqrt{\nu_1\nu_2},
```

with the same Hamiltonian formula.

If $`\nu_j\le\Gamma`$, every jump coefficient is at most $`\sqrt{2\Gamma}`$. For $`n\ge3`$, the largest drift hopping is at most $`\sqrt2\,\Gamma`$; for $`n=2`$ it is at most $`2\Gamma`$. These are bounds on the coefficients, not operator norms of the unbounded oscillator operators.

## Slow endpoints and equal internal rates

Let $`n\ge3`$ and put $`m=n-2`$. Choose

```math
\nu_1=\nu_n=a,
\qquad
\nu_j=\Gamma\quad(2\le j\le n-1),
\qquad
0\lt a\le\frac{\Gamma}{2}.
```

The resulting drift couplings are

```math
w_1=w_{n-1}=\sqrt{2a\Gamma},
\qquad
w_j=\Gamma\quad(2\le j\le n-2).
```

In this family the diagonal amplitude rates and all drift hoppings are at most $`\Gamma`$, the coherent hopping magnitudes are at most $`\Gamma/2`$, and the coefficients in the adjacent jumps are at most $`\sqrt\Gamma`$. The restriction $`a\le\Gamma/2`$ ensures this stronger edge bound; the jump construction itself remains physical for any positive $`a`$.

There are $`n-1`$ independent vacuum bath inputs. No excited relay mode, delay line, pulse-shaping control, measurement record, or postselection is supplied. The coherent–dissipative cancellation must be implemented with the stated coefficients.

## Exact random-delay representation

Let

```math
F_{a,a}(u)=2au\,e^{-au}\mathbf1_{\{u\ge0\}}.
```

Because the product of the edge couplings is $`2a\Gamma^m`$, the endpoint amplitude is exactly

```math
G(t)
=
(F_{a,a}*k_\Gamma^{*m})(t),
\qquad
k_\Gamma(s)=\Gamma e^{-\Gamma s}\mathbf1_{\{s\ge0\}}.
```

Equivalently,

```math
G(t)=\mathbb E[F_{a,a}(t-S)],
\qquad
S\sim\mathrm{Gamma}(m,\text{ rate }\Gamma).
```

In particular,

```math
\mathbb E S=\frac m\Gamma,
\qquad
\mathrm{Var}S=\frac m{\Gamma^2}.
```

The relays therefore create a positive random delay. To preserve the peak of the endpoint response, its width $`1/a`$ must exceed the standard deviation $`\sqrt m/\Gamma`$. The mean delay $`m/\Gamma`$ determines the leading propagation time.

## A finite-size lower bound

Read out at

```math
t_*=\frac m\Gamma+\frac1a.
```

For $`Y=a(S-m/\Gamma)`$, we have

```math
G(t_*)
=
\frac2e\,
\mathbb E\!\left[(1-Y)e^Y\mathbf1_{\{Y\le1\}}\right].
```

For every real $`y`$,

```math
(1-y)e^y\mathbf1_{\{y\le1\}}\ge1-y^2.
```

For $`y\le1`$, this follows by multiplying $`e^y\ge1+y`$ by the nonnegative factor $`1-y`$. For $`y>1`$, the left-hand side is zero and the right-hand side is negative. Therefore

```math
\boxed{
G(t_*)\ge
\frac2e\left(1-\frac{ma^2}{\Gamma^2}\right).
}
```

When $`ma^2/\Gamma^2\le1`$, squaring the nonnegative lower bound gives

```math
\boxed{
\eta(t_*)\ge
\frac4{e^2}
\left(1-\frac{ma^2}{\Gamma^2}\right)^2.
}
```

If the parenthesis is negative, the amplitude inequality remains true but cannot be squared to obtain a probability lower bound. One should then use the trivial bound $`\eta\ge0`$.

## Accuracy, waiting time, and rate hierarchy

To obtain relative amplitude deficit at most $`\delta`$, choose

```math
a=\Gamma\sqrt{\frac{\delta}{m}},
\qquad
0\lt \delta\lt 1,
\qquad
\delta\le\frac m4.
```

The last condition ensures $`a\le\Gamma/2`$. The guaranteed performance and readout time are

```math
G(t_*)\ge\frac2e(1-\delta),
\qquad
\eta(t_*)\ge\frac4{e^2}(1-\delta)^2,
\qquad
t_*=\frac{m+\sqrt{m/\delta}}{\Gamma}.
```

For each fixed $`n`$, taking $`\delta\to0`$ approaches the ceiling without increasing any local coefficient. It does require $`a\to0`$ and a waiting time growing as $`\delta^{-1/2}`$. For fixed nonzero accuracy, the leading time is $`n/\Gamma`$ and the endpoint amplitude rates scale as $`\Gamma/\sqrt n`$.

One may also approach the ceiling while taking the chain length to infinity. Choose

```math
a_n=\Gamma n^{-\alpha},
\qquad
\frac12\lt \alpha\lt 1.
```

Then

```math
\frac{(n-2)a_n^2}{\Gamma^2}\longrightarrow0,
\qquad
t_n=\frac{n-2+n^\alpha}{\Gamma},
\qquad
\frac{\Gamma t_n}{n}\longrightarrow1.
```

The condition $`\alpha>1/2`$ makes the endpoint response broad compared with the delay fluctuations. The condition $`\alpha\lt 1`$ makes the additional endpoint waiting time subleading to propagation. These same two conditions permit the [weak-loss frontier](loss_frontier.md) to be attained when unavoidable loss acts on the slow endpoints as well as on every relay.

For $`n=2`$, no limiting construction is needed. Taking $`\nu_1=\nu_2=a`$ gives $`G(t)=2at e^{-at}`$, with exact peak $`2/e`$ at $`t=1/a`$.

## Comparison with equal diagonal damping

The distinction between a relay-delay spread and an endpoint response width is visible in the equal-rate benchmark. If every diagonal amplitude rate is $`\Gamma`$ and the edge product is saturated, then

```math
G_{\mathrm{eq}}(t)
=
2\,\frac{(\Gamma t)^{n-1}}{(n-1)!}\,e^{-\Gamma t}.
```

Its peak probability is asymptotic to

```math
\max_t|G_{\mathrm{eq}}(t)|^2
\sim\frac{2}{\pi(n-1)}.
```

The endpoint edges in this benchmark are the product-saturating ones, so “equal-rate” refers to the diagonal damping rather than identical edge coefficients. The asymptotic follows directly from Stirling's formula; the [loss analysis](loss_frontier.md) gives its full expression with extra damping.

Slow endpoints remove this algebraic dilution and retain a nonzero transfer probability at ballistic leading-order time. They do not improve the two-endpoint ceiling, create autonomous storage at the receiver, or remove the waiting-time exposure to additional loss.

