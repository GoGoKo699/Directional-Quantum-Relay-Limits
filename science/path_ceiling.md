# A sharp ceiling for static directional paths

For the [passive path model](model.md), adding any number of static nearest-neighbor relays cannot raise the single-mode endpoint transmissivity above

```math
\eta_{\mathrm{path}}=\frac4{e^2}=0.5413411329\ldots.
```

The two-emitter value is an established absorption limit for a decaying exponential photon [[Stobinska09, Wang11]](../references/related_work.md#references), also used as the point-coupled benchmark in current passive-transfer work [[Diekmann26]](../references/related_work.md#references). The statement here quantifies over the entire allowed path: arbitrary finite damping rates, complex couplings, onsite frequencies, number of relays, and readout time.

The proof combines a classical extremum for weighted shifts with numerical radius at most one with the positive convolution structure of a unique directed path. The product extremum and its saturating edge profile are inherited operator-theoretic results; a self-contained elementary proof is included below [[Pearcy1966, Crabb1971, LewisOverton2020]](../references/related_work.md#references).

## Theorem

Let $`n\ge2`$ and let $`A`$ be lower bidiagonal, with

```math
A_{jj}=-\nu_j-i\omega_j,
\qquad
A_{j+1,j}=w_j,
\qquad
A+A^\dagger\preceq0.
```

Then, for every $`t\ge0`$,

```math
\left|[e^{At}]_{n1}\right|\le\frac2e,
\qquad
\eta(t)\le\frac4{e^2}.
```

For $`n=2`$, equality is attained at finite rates and time. For each fixed $`n\ge3`$, the bound is a supremum over designs and times; every individual finite-rate design has a strict inequality at finite time. The [bounded-rate construction](attainable_designs.md) approaches the supremum.

## 1. Degenerate rates break the path

Define the Hermitian damping matrix

```math
R=-\frac12(A+A^\dagger)\succeq0.
```

Its diagonal is $`R_{jj}=\nu_j`$, and its adjacent off-diagonal entries are $`R_{j+1,j}=-w_j/2`$.

For any positive semidefinite matrix, the two-by-two principal minors give

```math
|R_{jk}|^2\le R_{jj}R_{kk}.
```

Consequently, if $`\nu_j=0`$, every entry in row and column $`j`$ of $`R`$ vanishes. Every incident path coupling is then zero. A zero $`w_j`$ also disconnects the only route from input to output. In either case $`[e^{At}]_{n1}=0`$.

It therefore suffices to prove the result when all $`\nu_j`$ and $`|w_j|`$ are positive.

## 2. The sharp path-product inequality

A diagonal change of mode phases makes all adjacent drift couplings positive without changing the diagonal rates or transfer magnitude. Let $`D=\operatorname{diag}(\nu_1,\ldots,\nu_n)`$. After this phase change,

```math
D^{-1/2}RD^{-1/2}=I-B\succeq0,
```

where $`B`$ is the real symmetric weighted path adjacency matrix with

```math
B_{j,j+1}=B_{j+1,j}=b_j,
\qquad
b_j=\frac{|w_j|}{2\sqrt{\nu_j\nu_{j+1}}}>0.
```

Let $`\rho`$ be the Perron eigenvalue of $`B`$ and let $`u>0`$ be its Perron vector. Since $`I-B\succeq0`$, we have $`\rho\le1`$.

Define

```math
p_j=b_j\frac{u_{j+1}}{u_j}\quad(1\le j<n),
\qquad
q_j=b_{j-1}\frac{u_{j-1}}{u_j}\quad(2\le j\le n),
```

and set $`q_1=p_n=0`$. The eigenvector equation gives

```math
p_j+q_j=\rho,
\qquad
p_1=q_n=\rho.
```

Pairing the two contributions from each edge yields

```math
\begin{aligned}
\prod_{j=1}^{n-1}b_j^2
&=\prod_{j=1}^{n-1}p_jq_{j+1}\\
&=p_1q_n\prod_{j=2}^{n-1}p_jq_j\\
&\le \rho^2\left(\frac{\rho^2}{4}\right)^{n-2}\\
&\le4^{-(n-2)}.
\end{aligned}
```

The middle inequality is the arithmetic-geometric mean inequality applied at every internal vertex. Empty products are one, so the argument also covers $`n=2`$.

Undoing the normalization gives

```math
\boxed{
\prod_{j=1}^{n-1}|w_j|
\le
2\sqrt{\nu_1\nu_n}
\prod_{j=2}^{n-1}\nu_j.
}
```

The inequality is sharp for arbitrary positive diagonal rates. For $`n\ge3`$, take

```math
b_1=b_{n-1}=\frac1{\sqrt2},
\qquad
b_j=\frac12\quad(2\le j\le n-2).
```

The positive vector $`u=(1,\sqrt2,\ldots,\sqrt2,1)^T`$ then satisfies $`Bu=u`$, so $`\rho=1`$ and all product inequalities are equalities. For $`n=2`$, the corresponding choice is $`b_1=1`$.

### Classical operator-theory interpretation

Let $`T`$ be the weighted shift with superdiagonal entries $`2b_j`$. Its numerical range is rotationally symmetric, and

```math
w(T)=\lambda_{\max}\!\left(\frac{T+T^\dagger}{2}\right)
=\rho(B)\le1.
```

The classical numerical-radius power bound gives

```math
\|T^{n-1}\|\le2\,w(T)^{n-1}\le2.
```

But $`T^{n-1}`$ has just one possibly nonzero entry, equal to $`2^{n-1}\prod_j b_j`$. This recovers the product inequality directly. The saturating shift with weights $`\sqrt2,1,\ldots,1,\sqrt2`$ is the classical Crabb matrix. The Perron calculation above is an elementary path-specific proof of that inherited extremum [[Pearcy1966, Crabb1971, LewisOverton2020]](../references/related_work.md#references).

## 3. The propagator is a single convolution

For $`\operatorname{Re}z>0`$, define the causal function

```math
f_z(t)=e^{-zt}\mathbf1_{\{t\ge0\}}.
```

The exponential of a bidiagonal matrix has the standard product-of-edges and divided-difference structure [[Higham2024]](../references/related_work.md#references). For the present generator, its convolution form follows directly: the first column of $`e^{At}`$ satisfies a sequence of driven scalar equations, and variation of constants at each site gives

```math
[e^{At}]_{n1}
=
\left(\prod_{j=1}^{n-1}w_j\right)
(f_{\nu_1+i\omega_1}*\cdots*f_{\nu_n+i\omega_n})(t).
```

The convolution is over nonnegative times. This identity uses the existence of only one directed route; it is not a formula for an arbitrary lower-triangular network.

Taking the modulus and applying the product inequality gives

```math
\left|[e^{At}]_{n1}\right|
\le
(F_{a,b}*k_2*\cdots*k_{n-1})(t),
```

where $`a=\nu_1`$, $`b=\nu_n`$,

```math
F_{a,b}(t)=2\sqrt{ab}\,(f_a*f_b)(t),
\qquad
k_j(t)=\nu_je^{-\nu_jt}\mathbf1_{\{t\ge0\}}.
```

Every $`k_j`$ is a probability density. When there are no internal sites, the right-hand side is simply $`F_{a,b}(t)`$.

The triangle inequality also shows that, at fixed diagonal damping rates and edge magnitudes, detunings cannot improve transfer over the resonant design. Setting all onsite frequencies equal aligns the convolution phases and leaves passivity unchanged.

## 4. The two-endpoint response has peak 2/e

For unequal endpoint rates,

```math
F_{a,b}(t)
=
2\sqrt{ab}\,
\frac{e^{-at}-e^{-bt}}{b-a}
\qquad(t\ge0).
```

The expression is symmetric in $`a,b`$. Assume $`b>a`$ and write $`r=b/a>1`$. Differentiation gives the unique maximum at

```math
t_*=\frac{\log r}{b-a},
\qquad
\max_tF_{a,b}(t)
=
2r^{-(r+1)/(2(r-1))}.
```

The elementary inequality

```math
\log r\ge\frac{2(r-1)}{r+1},
\qquad r\ge1,
```

follows because the difference vanishes at $`r=1`$ and has derivative $`(r-1)^2/[r(r+1)^2]\ge0`$. Hence the peak is at most $`2/e`$.

For equal rates,

```math
F_{a,a}(t)=2at\,e^{-at}\mathbf1_{\{t\ge0\}},
\qquad
\max_tF_{a,a}(t)=\frac2e
\quad\text{at }t=\frac1a.
```

Finally, convolution with a probability density cannot increase a supremum norm. Therefore

```math
\left|[e^{At}]_{n1}\right|
\le
\|F_{a,b}\|_\infty
\prod_{j=2}^{n-1}\|k_j\|_1
\le\frac2e.
```

Squaring proves the theorem.

## 5. Attainment and strictness

For two modes, choose $`\nu_1=\nu_2=a>0`$, $`w_1=2a`$, and equal onsite frequencies. Then

```math
|[e^{At}]_{21}|=2at\,e^{-at},
```

which reaches $`2/e`$ at $`t=1/a`$.

For $`n\ge3`$ with all path rates positive, the convolution of the internal exponential densities is the distribution of a positive random delay $`S`$ with an unbounded tail. At any finite time,

```math
(F_{a,b}*k_2*\cdots*k_{n-1})(t)
=
\mathbb E[F_{a,b}(t-S)]
\le\frac2e\,\Pr(S\le t)
<\frac2e.
```

Thus a finite-rate path with at least one relay never reaches the ceiling exactly at a finite time. Its supremum is nevertheless the same two-mode value. The [explicit construction](attainable_designs.md) makes the endpoint response broad compared with the internal delay fluctuations while keeping all local coefficients bounded.

The conclusion is architectural. The classical product extremum constrains the coherent transfer allowed by complete positivity, and the normalized relay kernels cannot sharpen the endpoint response. A [single additional bypass](bypass.md) removes this convolution structure and defeats the ceiling.

