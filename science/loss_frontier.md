# Optimal transfer with unavoidable uniform loss

Let the engineered drift $`A_0`$ satisfy the [passive scalar path model](model.md), with diagonal amplitude damping bounded by $`\Gamma>0`$:

```math
A_0+A_0^\dagger\preceq0,
\qquad
0\le\nu_j=-\operatorname{Re}(A_0)_{jj}\le\Gamma.
```

Add independent vacuum loss on every mode:

```math
A=A_0-\kappa I,
\qquad
\kappa\ge0.
```

The added physical jumps are $`\sqrt{2\kappa}\,a_j`$. Both $`\nu_j`$ and $`\kappa`$ are amplitude damping rates. The engineered generator is passive separately, so it cannot compensate the added loss with gain.

Define the all-design optimum

```math
\eta_n^*(\delta)
=
\sup_{A_0,t\ge0}
\left|[e^{(A_0-\kappa I)t}]_{n1}\right|^2,
\qquad
\delta=\frac{\kappa}{\Gamma}.
```

The supremum includes arbitrary allowed couplings and onsite frequencies, as well as readout time. Rescaling time by $`\Gamma`$ shows that the optimum depends only on $`n`$ and the dimensionless ratio $`\delta`$.

We obtain an exact finite-size upper bound, a reduction of the finite-size optimization to the two endpoint rates and time, the exact attenuation exponent at fixed positive loss, and the exact optimized limit when $`n\delta`$ remains finite. The finite-size upper bound is not generally claimed to equal the finite-size optimum.

## 1. Universal finite-size bound

Set

```math
r=\frac{\Gamma}{\Gamma+\kappa}=\frac1{1+\delta}.
```

For every allowed design and every time,

```math
\boxed{
\eta(t)\le\frac4{e^2}\,r^{2(n-1)}.
}
```

To prove this, first discard the trivial case of a broken path. Put $`\lambda_j=\nu_j+\kappa>0`$. The product inequality for the engineered drift gives

```math
\prod_{j=1}^{n-1}|w_j|
\le
2\sqrt{\nu_1\nu_n}\prod_{j=2}^{n-1}\nu_j.
```

The propagator with extra loss has the same convolution form as before, with decay rates $`\lambda_j`$. Reorganizing its coefficient yields

```math
\left|[e^{At}]_{n1}\right|
\le
\Pi(\nu,\kappa)\,
(F_{\lambda_1,\lambda_n}*
\widetilde k_2*\cdots*\widetilde k_{n-1})(t),
```

where

```math
\begin{aligned}
\Pi(\nu,\kappa)
&=
\sqrt{\frac{\nu_1}{\nu_1+\kappa}}\,
\sqrt{\frac{\nu_n}{\nu_n+\kappa}}\,
\prod_{j=2}^{n-1}
\frac{\nu_j}{\nu_j+\kappa},\\
\widetilde k_j(t)
&=
(\nu_j+\kappa)e^{-(\nu_j+\kappa)t}
\mathbf1_{\{t\ge0\}}.
\end{aligned}
```

The endpoint function $`F`$ is defined in [path ceiling](path_ceiling.md), and every $`\widetilde k_j`$ has unit integral. Its peak is therefore at most $`2/e`$. Since $`\nu/(\nu+\kappa)`$ is nondecreasing in $`\nu`$,

```math
\Pi(\nu,\kappa)\le r^{n-1}.
```

There are $`n-2`$ internal factors and two endpoint square roots, which together contribute $`n-1`$ powers of $`r`$. Squaring proves the bound.

For $`n=2`$ it is exact: choose equal engineered rates $`\Gamma`$, coupling $`2\Gamma`$, and time $`t=1/(\Gamma+\kappa)`$. For $`n\ge3`$, the convolution with a nonzero relay delay prevents an individual finite-rate design from saturating the displayed bound. We do not infer the exact finite-size optimum from it.

## 2. Exact reduction of the finite-size optimization

The diagonal-rate budget permits a stronger structural statement: **all internal damping rates can be set to their maximum without decreasing the optimized peak transfer**. This concerns optimization over readout time; it is not a pointwise comparison at a fixed time.

First, remove detunings. The triangle inequality in the path convolution shows that the resonant design with the same rates and edge magnitudes has at least as large an amplitude at every time. Next, saturate the path-product inequality. This increases its nonnegative prefactor, and the [adjacent-jump construction](attainable_designs.md) proves that the required edge profile is physically realizable for arbitrary positive diagonal rates.

It remains to optimize a positive convolution. Write the endpoint rates as $`a=\nu_1`$ and $`b=\nu_n`$, and define

```math
h_\nu(t)=\nu e^{-(\nu+\kappa)t}\mathbf1_{\{t\ge0\}}.
```

For fixed endpoints, every internal site contributes one factor $`h_\nu`$. Its Laplace transform is $`H_\nu(s)=\nu/(s+\nu+\kappa)`$. For $`0<\nu\le\Gamma`$,

```math
\frac{H_\nu(s)}{H_\Gamma(s)}
=
\frac{\nu}{\Gamma}
+
\frac{\nu(\Gamma-\nu)}
{\Gamma(s+\nu+\kappa)}.
```

The inverse transform is the nonnegative measure

```math
q_{\nu,\Gamma}
=
\frac{\nu}{\Gamma}\,\delta_0
+
\frac{\nu(\Gamma-\nu)}{\Gamma}
e^{-(\nu+\kappa)t}\mathbf1_{\{t\ge0\}}\,dt.
```

Its total mass is

```math
\|q_{\nu,\Gamma}\|_1
=
\frac{\nu(\Gamma+\kappa)}
{\Gamma(\nu+\kappa)}
\le1.
```

Thus $`h_\nu=h_\Gamma*q_{\nu,\Gamma}`$. If $`G_{\mathrm{old}}`$ is a saturated resonant amplitude with one internal rate $`\nu`$, and $`G_{\mathrm{new}}`$ is obtained by replacing that rate with $`\Gamma`$ and readjusting the physical product-saturating couplings, then

```math
G_{\mathrm{old}}=G_{\mathrm{new}}*q_{\nu,\Gamma},
\qquad
\sup_tG_{\mathrm{old}}(t)
\le
\|q_{\nu,\Gamma}\|_1\sup_tG_{\mathrm{new}}(t)
\le
\sup_tG_{\mathrm{new}}(t).
```

Repeating this replacement for all internal sites proves the reduction. In terms of the causal functions $`f_z(t)=e^{-zt}\mathbf1_{\{t\ge0\}}`$,

```math
\boxed{
\eta_n^*(\delta)
=
\left[
\sup_{\substack{0<a,b\le\Gamma\\t\ge0}}
2\sqrt{ab}\,\Gamma^{n-2}
\left(
f_{a+\kappa}*
f_{b+\kappa}*
f_{\Gamma+\kappa}^{*(n-2)}
\right)(t)
\right]^2.
}
```

For $`n=2`$, the last convolution factor is absent. Rates equal to zero need not be included because they break the path and yield zero transfer.

The displayed expression is an exact reduction to three real variables. It does not assume that the optimal endpoint rates are equal. The symmetric endpoints used below are a sufficient attaining construction for the asymptotic statements.

For $`\kappa>0`$, the reduced optimization has a finite maximum. Indeed, passivity gives $`|G(t)|\le e^{-\kappa t}`$, so the large-time tail can be excluded once any positive achievable value is fixed. On the remaining compact time interval the amplitude is continuous in $`a,b\in[0,\Gamma]`$, with zero transfer when either endpoint rate vanishes. For $`\kappa=0`$ and $`n\ge3`$, the ceiling remains a supremum approached by slow endpoints.

## 3. Equal diagonal rates attain the fixed-loss exponent

Choose all engineered diagonal rates equal to $`\Gamma`$ and saturate the path-product bound. The required edge couplings are

```math
w_1=w_{n-1}=\sqrt2\,\Gamma,
\qquad
w_j=\Gamma\quad(2\le j\le n-2)
```

for $`n\ge3`$, and $`w_1=2\Gamma`$ for $`n=2`$. The local realization is the one in [attainable designs](attainable_designs.md). All coefficients remain bounded by constants times $`\Gamma`$.

Put $`k=n-1`$. Equal diagonal decay rates make the convolution elementary:

```math
G_{\mathrm{eq}}(t)
=
2\Gamma^k\frac{t^k}{k!}
e^{-(\Gamma+\kappa)t}.
```

Its maximum occurs at

```math
t_{\mathrm{eq}}=\frac{k}{\Gamma+\kappa},
```

and gives

```math
\eta_{\mathrm{eq}}^{\max}
=
4r^{2k}
\left(\frac{k^ke^{-k}}{k!}\right)^2.
```

Stirling's formula gives

```math
\eta_{\mathrm{eq}}^{\max}
\sim
\frac{2}{\pi k}\,r^{2k}.
```

Combining this lower bound with the universal upper bound,

```math
4r^{2(n-1)}
\left(
\frac{(n-1)^{n-1}e^{-(n-1)}}{(n-1)!}
\right)^2
\le
\eta_n^*(\delta)
\le
\frac4{e^2}r^{2(n-1)}.
```

Therefore, for each fixed $`\delta>0`$,

```math
\boxed{
\lim_{n\to\infty}
-\frac1n\log\eta_n^*(\delta)
=
2\log(1+\delta).
}
```

The polynomial prefactor of the all-design optimum is not determined by this comparison. In particular, the $`1/n`$ factor of the equal-rate lower bound is not asserted to be optimal.

## 4. Exact optimized weak-loss frontier

Now let $`\delta_n=\kappa_n/\Gamma`$ vary with chain length, and assume

```math
n\delta_n\longrightarrow x,
\qquad
0\le x<\infty.
```

Then

```math
\boxed{
\lim_{n\to\infty}\eta_n^*(\delta_n)
=
\frac4{e^2}e^{-2x}.
}
```

For the upper bound, $`\delta_n\to0`$ and hence

```math
(1+\delta_n)^{-2(n-1)}
\longrightarrow e^{-2x}.
```

For attainability, take the slow-endpoint family

```math
a_n=\Gamma n^{-\alpha},
\qquad
\frac12<\alpha<1,
\qquad
t_n=\frac{n-2}{\Gamma}+\frac1{a_n}.
```

Without the added loss, the finite lower bound in [attainable designs](attainable_designs.md) gives

```math
G_{0,n}(t_n)
\ge
\frac2e
\left(1-(n-2)n^{-2\alpha}\right)
\longrightarrow\frac2e.
```

Uniform extra loss commutes with the engineered drift:

```math
e^{(A_0-\kappa_n I)t_n}
=
e^{-\kappa_n t_n}e^{A_0t_n}.
```

Its total attenuation satisfies

```math
\kappa_n t_n
=
\delta_n(n-2+n^\alpha)
\longrightarrow x.
```

The endpoint waiting time contributes $`\delta_nn^\alpha\to0`$, while propagation contributes $`\delta_n(n-2)\to x`$. Consequently the constructed amplitude tends to $`(2/e)e^{-x}`$ and its transmissivity tends to $`(4/e^2)e^{-2x}`$, matching the upper bound.

The construction charges loss during the entire evolution, including the slow endpoint emission and capture. Its leading readout time is $`n/\Gamma`$; there is no assumption of lossless endpoint storage.

## 5. A usable finite-size lower bound

For $`m=n-2\ge1`$, choose any $`0<a\le\Gamma/2`$ satisfying $`ma^2/\Gamma^2\le1`$. The same physical family gives

```math
\boxed{
\eta_n^*(\delta)
\ge
\frac4{e^2}
\exp\!\left[
-2\kappa\left(\frac m\Gamma+\frac1a\right)
\right]
\left(1-\frac{ma^2}{\Gamma^2}\right)^2.
}
```

This is a rigorous construction bound, not a claimed finite-size optimum. It displays the tradeoff directly: reducing $`a`$ narrows the relative effect of relay-delay fluctuations, but increases exposure to unavoidable loss.

For the scaling $`\delta_n=x/n`$, the choice $`a_n=\Gamma n^{-2/3}`$ balances the orders of the two error terms in this simple lower bound: the delay-variance correction and the extra endpoint-loss exponent both scale as $`n^{-1/3}`$. This does not establish an optimal convergence rate.

## Boundaries of the result

The conclusions rely on uniform extra loss and a bound on the engineered diagonal amplitude rates. They do not determine the optimal finite-size endpoint rates, the fixed-loss polynomial prefactor, or transfer under a prescribed time deadline. The exact endpoint-and-time reduction above makes the remaining finite-size optimization explicit.

If $`\Gamma=0`$, passivity forces every engineered path coupling to vanish and transfer is zero; the nontrivial formulas assume $`\Gamma>0`$. If $`\kappa=0`$, the general path ceiling is recovered.

The [channel consequences](channel_consequences.md) apply standard pure-loss capacity facts to this physically optimized transmissivity. The attenuation frontier itself does not assert a capacity formula for active, assisted, multimode, or memory-bearing communication protocols.

