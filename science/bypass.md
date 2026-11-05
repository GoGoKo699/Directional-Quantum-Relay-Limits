# A passive bypass that exceeds the path ceiling

The unique directed path is essential. A static passive Markovian network with three scalar modes can exceed $`4/e^2`$ once it contains a direct bypass from input to output.

This example keeps the same vacuum input conditions and the same single-mode readout as the [path model](model.md). Its drift remains strictly one-way, but is lower triangular rather than lower bidiagonal. It therefore identifies a concrete boundary of the theorem without appealing to gain, control, non-Markovian dynamics, or an excited auxiliary mode.

## Physical realization

Measure time in units for which every diagonal amplitude damping rate is one. Use the single common loss jump

```math
L=\sqrt2\,(a_1+a_2+a_3)
```

and the number-conserving Hamiltonian $`H=a^\dagger h a`$ with

```math
h=
\begin{pmatrix}
0&i&i\\
-i&2\pi&i\\
-i&-i&0
\end{pmatrix}.
```

The Hamiltonian is Hermitian. Since

```math
K^\dagger K
=
2\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix},
```

the drift is

```math
A=-ih-\frac12K^\dagger K
=
\begin{pmatrix}
-1&0&0\\
-2&-1-i2\pi&0\\
-2&-2&-1
\end{pmatrix}.
```

In particular,

```math
A+A^\dagger
=
-2\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix}
\preceq0.
```

The dynamics are passive, with no upper-triangular propagation. There are two directed routes from mode $`1`$ to mode $`3`$: the direct edge $`1\to3`$ and the route $`1\to2\to3`$.

The direct entry $`A_{31}\ne0`$ is precisely the violation of the lower-bidiagonal assumption. A common bath can generate such nonadjacent effective couplings; one-way propagation alone does not impose the unique-path structure.

## Exact transfer amplitude

Start with amplitude one in mode $`1`$ and zero in modes $`2,3`$. Write the components of $`e^{At}(1,0,0)^T`$ as $`u_1,u_2,u_3`$, and put $`\Omega=2\pi`$. Then

```math
u_1(t)=e^{-t},
```

and variation of constants gives

```math
u_2(t)
=
-2e^{-t}\frac{1-e^{-i\Omega t}}{i\Omega}.
```

The output obeys

```math
\dot u_3=-u_3-2u_1-2u_2.
```

Consequently,

```math
\begin{aligned}
u_3(t)
&=
e^{-t}\left[
-2t
+
4\int_0^t(t-s)e^{-i\Omega s}\,ds
\right]\\
&=
e^{-t}\left[
-2t
+
4\left(
\frac{t}{i\Omega}
+
\frac{1-e^{-i\Omega t}}{\Omega^2}
\right)
\right].
\end{aligned}
```

At $`t=1`$, the detuned relay completes one phase cycle, so

```math
[e^A]_{31}
=
e^{-1}\left(-2-\frac{2i}{\pi}\right).
```

The single-mode channel therefore has transmissivity

```math
\boxed{
\eta(1)
=
\frac4{e^2}\left(1+\frac1{\pi^2}\right)
=
0.5961904573\ldots
>
\frac4{e^2}.
}
```

No postselection is involved. By the passive channel reduction, this is the unconditional bosonic transmissivity and the unconditional single-excitation transfer probability.

## Why the path proof no longer applies

In a lower-bidiagonal drift, the input–output propagator is one product of edge couplings multiplied by one convolution. Complete positivity bounds that product, and the internal normalized kernels only broaden or delay the endpoint response.

Here the output contains a sum of contributions from paths of different lengths. Their phases need not align in the manner assumed by a single positive-kernel reduction. At the displayed readout time, the direct contribution is real and the two-edge contribution is imaginary; their combined magnitude exceeds the familiar two-mode peak.

The associated damping matrix also contains a nonadjacent entry, so its normalization is no longer the weighted path matrix used in the product argument.

This example establishes only that a bypass can exceed the ceiling. It does not determine the optimal three-mode transfer, the optimum over arbitrary directed graphs, or how many additional paths are needed to approach unit transmissivity. The theorem remains an exact statement about strictly one-way nearest-neighbor scalar paths, and the counterexample prevents it from being extended to all passive cascaded networks.

