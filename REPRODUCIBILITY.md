# Reproducing the calculations and figures

The scripts use the explicitly stated passive path model and require no external data or network access. They evaluate a selected physical construction, independent finite checks, and rigorous analytic bounds. They do not perform a numerical optimization over all finite chains.

## Run

From the repository root:

```sh
python scripts/verify_science.py
python scripts/make_figures.py
```

The first command writes `data/verification.json` and exits with an error if a stated check fails. A different destination can be supplied with `--output PATH`. The second command regenerates the two SVG figures, their CSV data, and `data/figure_metadata.json`.

The dependencies are Python, NumPy, SciPy, and Matplotlib. The checked environment was:

| Dependency | Version |
| --- | --- |
| Python | 3.12.14 |
| NumPy | 2.3.5 |
| SciPy | 1.17.0 |
| Matplotlib | 3.10.8 |

To install the pinned numerical packages in an existing Python environment:

```sh
python -m pip install numpy==2.3.5 scipy==1.17.0 matplotlib==3.10.8
```

These are the versions used to produce the committed numerical record. Floating-point residuals and SVG layout may differ slightly with other versions or fonts. The numerical checks use explicit tolerances rather than bytewise comparison.

## Generated files

| File | Content |
| --- | --- |
| [data/verification.json](data/verification.json) | Full parameters and numerical residuals for the finite checks, package versions, and status. |
| [data/finite_loss_comparison.csv](data/finite_loss_comparison.csv) | Fixed $`\kappa/\Gamma=10^{-5}`$, including each endpoint rate, readout time, evaluated probability, lower bound, upper bound, and homogeneous benchmark. |
| [data/weak_loss_crossover.csv](data/weak_loss_crossover.csv) | Finite families at $`n=20,200,2000,20000`$ as $`x=n\kappa/\Gamma`$ varies. |
| [data/figure_metadata.json](data/figure_metadata.json) | Plot domains, rate and time selection, conventions, filenames, and Matplotlib version. |
| [figures/finite_loss_comparison.svg](figures/finite_loss_comparison.svg) | Explicit finite designs and rigorous bounds at fixed additional loss. |
| [figures/weak_loss_crossover.svg](figures/weak_loss_crossover.svg) | Finite constructions approaching the optimized weak-loss limit. |

The SVGs retain text rather than embedding a raster plot. Their actual SVG output was rendered with Inkscape and visually checked for readable labels, legends, and threshold annotations.

## Rate, time, and optimization conventions

The budget $`\Gamma`$ bounds the engineered **diagonal amplitude damping** $`\nu_j`$. It is not an edge-coupling bound or an occupation damping rate. The added uniform loss parameter $`\kappa`$ is also an amplitude rate and is implemented by vacuum jumps $`\sqrt{2\kappa}\,a_j`$. Occupation damping is twice the corresponding amplitude damping. All tabled rates and times are dimensionless ratios to $`\Gamma`$.

For $`m=n-2`$, the finite endpoint family sets internal rates to $`\Gamma`$, equal endpoint rates to $`a`$, and reads out at

```math
\Gamma t_* = m+\frac{\Gamma}{a}.
```

Writing $`y=a/\Gamma`$ and $`\delta=\kappa/\Gamma>0`$, the endpoint choice is the unique positive root of

```math
2my^3+\delta my^2-\delta=0,
```

clipped at $`y=1/2`$. This maximizes the stated finite lower bound within that family and time prescription. It does not claim to maximize the exact finite probability. The general finite optimization reduces to two possibly unequal endpoint rates and time, as proved in [loss frontier](science/loss_frontier.md). The plotted family supplies an explicit attainable value within that problem.

The homogeneous benchmark sets all diagonal rates equal to $`\Gamma`$ and saturates the path-product bound. Its endpoint edge amplitudes are $`\sqrt2\,\Gamma`$ for $`n\ge3`$, so its diagonal rates, rather than every edge, are homogeneous. Its curve uses its exact best readout time $`\Gamma t=(n-1)/(1+\delta)`$.

At fixed positive $`x=n\kappa/\Gamma`$, the selected endpoint rates decrease as $`n^{-2/3}`$ and the time has leading order $`n/\Gamma`$. The CSV data record this rate hierarchy and the full waiting time. The $`x=0`$ endpoint of the lower-bound optimization would require $`a\to0`$ and unbounded waiting time, so finite-design curves are drawn only for $`x>0`$. The asymptotic frontier itself includes $`x=0`$.

The [finite examples](science/finite_examples.md) derive the endpoint rule and the exact incomplete-gamma expression used to evaluate each design.

## What the verification checks

| Check | Independent calculation and purpose |
| --- | --- |
| Local jump realization | Builds the adjacent jump matrix and Hermitian hopping matrix, then checks that $`-ih-K^\dagger K/2`$ equals the specified lower-bidiagonal drift and has a positive semidefinite damping matrix. Includes $`n=3`$, where no purely internal edge is present, and a nonunit rate scale. |
| Phases, detunings, and passivity | Builds deterministic admissible paths with heterogeneous rates, edge phases, and onsite frequencies. Checks the passive edge-product inequality, the removable path phase, the resonant comparison, the probability ceiling, and the uniform-loss factor. All sampled parameters are recorded; these examples are not a proof for arbitrary parameters. |
| Gamma convolution | Compares the incomplete-gamma expression against both direct integration of the gamma-distributed delay and dense matrix exponentiation at three parameter sets, including zero and positive additional loss. |
| Internal-rate factorization | Integrates the positive-measure identity $`h_\nu=h_\Gamma*q_{\nu,\Gamma}`$ and checks its total mass is at most one. Includes equality at $`\nu=\Gamma`$, zero additional loss, and a late-time case with $`h_\nu(t)>h_\Gamma(t)`$. Thus the check does not impose a false fixed-time monotonicity. |
| Finite bounds and weak-loss sequence | Evaluates six lengths at $`x=0.02`$, checks the stated lower and upper bounds, and compares against sparse matrix exponentiation for lengths through $`n=2000`$. The larger analytic evaluations display approach to the limiting value. |
| Exact bypass | Builds the passive three-mode generator from its jump and Hamiltonian and compares its transfer amplitude with the exact expression at $`t=1`$. Checks that the additional direct edge allows probability above the path ceiling. |

The phase and detuning examples use the fixed random seed `72109` only to choose deterministic test parameters. Figure construction itself uses no randomness. The script records the actual selected parameters so reproduction does not depend on inferring them from a plot.

## Observed numerical agreement

The recorded run passed every check. Local-jump drift residuals were below $`3\times10^{-17}`$. The gamma formula agreed with dense matrix exponentiation and independent quadrature to within $`5\times10^{-16}`$ in amplitude at the three checked points. The longest independently propagated path, $`n=2000`$, agreed with the analytic probability within $`5\times10^{-13}`$. The exact bypass amplitude agreed within $`2\times10^{-16}`$.

These residuals verify the finite implementations and conventions. The all-design ceiling, internal-rate reduction, loss exponent, and weak-loss limit rest on the analytical arguments in the scientific account. A finite numerical sequence does not establish those theorems or a general monotonic convergence property.
