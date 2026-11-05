#!/usr/bin/env python3
"""Deterministic finite checks for passive directional quantum paths.

Gamma bounds engineered diagonal AMPLITUDE damping. Additional loss kappa
also denotes an amplitude rate; occupation damping rates are twice these.
The checks support the formulas and their implementation. They do not prove
the all-design theorem or numerically optimize over all finite chains.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply
from scipy.special import gammainc, gammaln
from scipy.stats import gamma as gamma_distribution

ROOT = Path(__file__).resolve().parents[1]
CEILING = 4.0 / math.e**2
CRITICAL_X = (math.log(8.0) - 2.0) / 2.0


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def universal_upper(n: int, kappa: float, gamma: float = 1.0) -> float:
    """Finite-n all-design probability bound; n >= 2."""
    require(n >= 2 and gamma > 0 and kappa >= 0, "Invalid path parameters")
    return CEILING * math.exp(-2.0 * (n - 1) * math.log1p(kappa / gamma))


def weak_loss_limit(x: float) -> float:
    return CEILING * math.exp(-2.0 * x)


def homogeneous_probability(n: int, kappa: float, gamma: float = 1.0) -> float:
    """Homogeneous extremal path at its exact maximizing time.

    Every diagonal engineered amplitude damping is Gamma. The two endpoint
    edge amplitudes are sqrt(2)*Gamma for n >= 3, and the internal ones are
    Gamma. For n=2, the sole edge amplitude is 2*Gamma.
    """
    require(n >= 2 and gamma > 0 and kappa >= 0, "Invalid path parameters")
    order = n - 1
    log_amp = (
        math.log(2.0)
        - order * math.log1p(kappa / gamma)
        + order * math.log(order)
        - order
        - float(gammaln(order + 1))
    )
    return math.exp(2.0 * log_amp)


def endpoint_rate_from_lower_bound(n: int, kappa: float, gamma: float = 1.0) -> float:
    """Maximize the stated finite lower bound within the endpoint family.

    For m=n-2, y=a/Gamma, delta=kappa/Gamma, its stationary equation is
    2*m*y**3 + delta*m*y**2 - delta = 0. It has one positive root with
    m*y**2 < 1. We impose the construction's extra condition y <= 1/2.
    This optimizes a rigorous lower bound at t=m/Gamma+1/a, not the exact
    transfer probability or all possible chains/times.
    """
    require(n >= 3 and gamma > 0 and kappa > 0, "This choice needs n>=3 and kappa>0")
    m = n - 2
    delta = kappa / gamma
    # Solve in u=sqrt(m)*y so the bracket is always [0,1].
    beta = delta * math.sqrt(m)
    u = brentq(lambda u: 2.0 * u**3 + beta * u**2 - beta,
               0.0, 1.0, xtol=1e-14, rtol=1e-14)
    return gamma * min(0.5, u / math.sqrt(m))


def family_coefficients(n: int, a: float, gamma: float = 1.0):
    require(n >= 3 and 0 < a <= gamma / 2, "Invalid endpoint family")
    nu = np.full(n, gamma, dtype=float)
    nu[0] = nu[-1] = a
    w = np.full(n - 1, gamma, dtype=float)
    w[0] = w[-1] = math.sqrt(2.0 * a * gamma)
    return nu, w


def family_amplitude(n: int, a: float, t: float, gamma: float = 1.0,
                     kappa: float = 0.0) -> float:
    """Exact gamma-convolution formula, including uniform extra loss.

    With m=n-2, b=Gamma-a and regularized lower incomplete gamma P,
    alpha(t) = 2*a*exp[-(a+kappa)t]*(Gamma/b)**m
               * [t*P(m,b*t) - (m/b)*P(m+1,b*t)].
    The combined exponent avoids large intermediate powers.
    """
    require(n >= 3 and 0 < a < gamma and t >= 0 and kappa >= 0,
            "Invalid convolution parameters")
    if t == 0:
        return 0.0
    m = n - 2
    b = gamma - a
    first = t * float(gammainc(m, b * t))
    second = (m / b) * float(gammainc(m + 1, b * t))
    bracket = first - second
    require(bracket >= -1e-12 * max(1.0, first, second),
            "Numerically negative gamma-convolution bracket")
    exponent = -(a + kappa) * t - m * math.log1p(-a / gamma)
    return 2.0 * a * math.exp(exponent) * max(0.0, bracket)


def finite_family_point(n: int, kappa: float, gamma: float = 1.0) -> dict:
    """One explicitly selected design, its value, and the rigorous bounds."""
    a = endpoint_rate_from_lower_bound(n, kappa, gamma)
    m = n - 2
    t = m / gamma + 1.0 / a
    jitter = m * (a / gamma)**2
    require(jitter < 1.0, "Lower bound must be nonnegative before squaring")
    eta = family_amplitude(n, a, t, gamma, kappa)**2
    lower = CEILING * math.exp(-2.0 * kappa * t) * (1.0 - jitter)**2
    upper = universal_upper(n, kappa, gamma)
    require(lower <= eta + 1e-10, "Family finite lower bound failed")
    require(eta <= upper + 1e-10, "Family universal upper bound failed")
    return {
        "n": n,
        "kappa_over_gamma": kappa / gamma,
        "x_n_kappa_over_gamma": n * kappa / gamma,
        "endpoint_rate_over_gamma": a / gamma,
        "scaled_time_gamma_t": gamma * t,
        "jitter_m_a2_over_gamma2": jitter,
        "family_probability": eta,
        "family_lower_bound": lower,
        "universal_upper_bound": upper,
        "homogeneous_probability": homogeneous_probability(n, kappa, gamma),
        "homogeneous_scaled_time_gamma_t": (n - 1) / (1.0 + kappa / gamma),
    }


def check_local_jumps() -> list[dict]:
    records = []
    for n, a, gamma in [(3, 0.08, 1.0), (9, 0.035, 1.7)]:
        nu, w = family_coefficients(n, a, gamma)
        K = np.zeros((n - 1, n))
        for j in range(n - 1):
            K[j, j] = math.sqrt(2.0 * a) if j == 0 else math.sqrt(gamma)
            K[j, j + 1] = -math.sqrt(2.0 * a) if j == n - 2 else -math.sqrt(gamma)
        h = np.diag(1j * w / 2.0, -1) + np.diag(-1j * w / 2.0, 1)
        A = -1j * h - K.conj().T @ K / 2.0
        target = -np.diag(nu) + np.diag(w, -1)
        residual = float(np.max(np.abs(A - target)))
        smallest_damping_eigenvalue = float(np.linalg.eigvalsh(-(A + A.conj().T)).min())
        require(residual < 1e-12, "Local jumps did not reproduce the target drift")
        require(smallest_damping_eigenvalue > -1e-12, "Nonpassive local realization")
        records.append(dict(n=n, a=a, gamma=gamma, drift_max_residual=residual,
                            smallest_damping_eigenvalue=smallest_damping_eigenvalue))
    return records


def check_phases_detunings() -> list[dict]:
    """Finite admissible examples, not a numerical proof for arbitrary paths."""
    rng = np.random.default_rng(72109)
    records = []
    for n, spectral_radius in [(2, 1.0), (5, 0.8), (8, 1.0)]:
        nu = np.exp(rng.uniform(-2.0, 1.0, n))
        gamma = float(nu.max())
        b = np.exp(rng.uniform(-1.5, 0.5, n - 1))
        B = np.diag(b, 1) + np.diag(b, -1)
        b *= spectral_radius / np.linalg.eigvalsh(B).max()
        magnitudes = 2.0 * b * np.sqrt(nu[:-1] * nu[1:])
        phases = rng.uniform(-math.pi, math.pi, n - 1)
        omega = 0.2 * gamma * rng.normal(size=n)
        w = magnitudes * np.exp(1j * phases)
        A = np.diag(-nu - 1j * omega) + np.diag(w, -1)
        A_zero_phase = np.diag(-nu - 1j * omega) + np.diag(magnitudes, -1)
        A_resonant = np.diag(-nu) + np.diag(magnitudes, -1)
        t = float(np.sum(1.0 / nu[1:-1]) + 2.0 / (nu[0] + nu[-1]))
        amp = complex(expm(t * A)[-1, 0])
        phase_reference = np.exp(1j * phases.sum()) * expm(t * A_zero_phase)[-1, 0]
        resonant_amp = float(expm(t * A_resonant)[-1, 0])
        damping_min = float(np.linalg.eigvalsh(-(A + A.conj().T)).min())
        product_bound = 2.0 * math.sqrt(nu[0] * nu[-1]) * float(np.prod(nu[1:-1]))
        product_ratio = float(np.prod(magnitudes)) / product_bound
        eta = abs(amp)**2
        kappa = 0.07 * gamma
        lossy_amp = complex(expm(t * (A - kappa * np.eye(n)))[-1, 0])
        factor_residual = abs(lossy_amp - math.exp(-kappa * t) * amp)
        require(damping_min > -1e-10, "Admissible phase example is not passive")
        require(product_ratio <= 1.0 + 1e-12, "Edge-product bound failed")
        require(abs(amp - phase_reference) < 1e-10, "Path phase gauge check failed")
        require(abs(amp) <= resonant_amp + 1e-10, "Detuning convolution bound failed")
        require(eta <= CEILING + 1e-10, "Path ceiling failed")
        require(factor_residual < 1e-10, "Uniform-loss factorization failed")
        require(abs(lossy_amp)**2 <= universal_upper(n, kappa, gamma) + 1e-10,
                "Finite uniform-loss bound failed")
        records.append({
            "n": n, "nu": nu.tolist(), "edge_magnitudes": magnitudes.tolist(),
            "edge_phases": phases.tolist(), "omega": omega.tolist(), "time": t,
            "gamma_diagonal_cap": gamma, "damping_min_eigenvalue": damping_min,
            "edge_product_over_bound": product_ratio, "probability": eta,
            "resonant_probability_same_rates": resonant_amp**2,
            "phase_gauge_residual": float(abs(amp - phase_reference)),
            "uniform_loss_factor_residual": float(factor_residual),
            "lossy_probability": abs(lossy_amp)**2,
            "lossy_universal_upper": universal_upper(n, kappa, gamma),
        })
    return records


def check_gamma_convolution() -> list[dict]:
    records = []
    for n, a, t, kappa in [(3, 0.04, 15.0, 0.0),
                            (7, 0.08, 17.5, 0.03),
                            (15, 0.11, 22.0, 0.01)]:
        gamma = 1.0
        nu, w = family_coefficients(n, a, gamma)
        A = -np.diag(nu + kappa) + np.diag(w, -1)
        dense = float(expm(t * A)[-1, 0])
        analytic = family_amplitude(n, a, t, gamma, kappa)
        m = n - 2
        integral, integration_error = quad(
            lambda s: 2.0 * a * (t - s) * math.exp(-a * (t - s))
            * gamma_distribution.pdf(s, a=m, scale=1.0 / gamma),
            0.0, t, epsabs=1e-12, epsrel=1e-11,
        )
        integral *= math.exp(-kappa * t)
        require(abs(dense - analytic) < 1e-10, "Gamma formula and expm disagree")
        require(abs(integral - analytic) < 1e-10, "Gamma integral and formula disagree")
        records.append(dict(n=n, a=a, time=t, kappa=kappa, expm_amplitude=dense,
                            analytic_amplitude=analytic, quadrature_amplitude=integral,
                            expm_residual=abs(dense - analytic),
                            quadrature_residual=abs(integral - analytic),
                            quadrature_reported_error=integration_error))
    return records


def check_internal_kernel_factorization() -> list[dict]:
    """Check the positive measure behind internal-rate saturation.

    For h_nu(t)=nu*exp[-(nu+kappa)t], h_nu=h_Gamma*q, where q
    has an atom nu/Gamma at zero and a nonnegative exponential density.
    Its mass is <=1. This controls the supremum over time, not the value
    at each fixed time: the examples include h_nu(t)>h_Gamma(t).
    """
    records = []
    for nu, gamma, kappa, t in [(0.25, 1.0, 0.0, 2.0),
                                (0.25, 1.0, 0.07, 2.0),
                                (0.8, 1.0, 0.07, 0.5),
                                (1.0, 1.0, 0.07, 0.5)]:
        atom = nu / gamma
        density_coefficient = nu * (gamma - nu) / gamma
        integral, integration_error = quad(
            lambda s: gamma * math.exp(-(gamma + kappa) * (t - s))
            * density_coefficient * math.exp(-(nu + kappa) * s),
            0.0, t, epsabs=1e-12, epsrel=1e-11,
        )
        fast_kernel = gamma * math.exp(-(gamma + kappa) * t)
        slow_kernel = nu * math.exp(-(nu + kappa) * t)
        convolution = atom * fast_kernel + integral
        mass = atom + density_coefficient / (nu + kappa)
        mass_formula = nu * (gamma + kappa) / (gamma * (nu + kappa))
        require(abs(convolution - slow_kernel) < 1e-12,
                "Internal-kernel convolution factorization failed")
        require(abs(mass - mass_formula) < 1e-12 and 0.0 < mass <= 1.0 + 1e-12,
                "Internal-kernel measure mass failed")
        records.append(dict(nu=nu, gamma=gamma, kappa=kappa, time=t,
                            slow_kernel=slow_kernel, fast_kernel=fast_kernel,
                            convolution_value=convolution, measure_mass=mass,
                            residual=abs(convolution - slow_kernel),
                            quadrature_reported_error=integration_error,
                            slow_kernel_exceeds_fast_at_this_time=slow_kernel > fast_kernel))
    require(any(row["slow_kernel_exceeds_fast_at_this_time"] for row in records),
            "The check should expose the absence of fixed-time monotonicity")
    return records


def check_weak_loss_sequence() -> dict:
    x = 0.02
    limit = weak_loss_limit(x)
    rows = []
    for n in [20, 100, 500, 2000, 20000, 200000]:
        point = finite_family_point(n, x / n)
        if n <= 2000:
            a = point["endpoint_rate_over_gamma"]
            nu, w = family_coefficients(n, a)
            A = diags([-(nu + x / n), w], [0, -1], format="csc")
            t = point["scaled_time_gamma_t"]
            initial = np.zeros(n)
            initial[0] = 1.0
            evolved = expm_multiply(t * A, initial,
                                    traceA=float(t * A.diagonal().sum()))
            sparse_eta = float(evolved[-1]**2)
            residual = abs(sparse_eta - point["family_probability"])
            require(residual < 1e-9, "Sparse propagation and analytic family disagree")
            point["sparse_expm_probability"] = sparse_eta
            point["sparse_expm_probability_residual"] = residual
        point["distance_from_limiting_frontier"] = abs(point["family_probability"] - limit)
        rows.append(point)
    require(rows[-1]["distance_from_limiting_frontier"] < rows[0]["distance_from_limiting_frontier"],
            "Displayed weak-loss sequence did not approach the predicted limit")
    return dict(x=x, limiting_probability=limit, rows=rows,
                scope="One displayed convergence sequence, not a proof of the limit.")


def check_bypass() -> dict:
    K = math.sqrt(2.0) * np.ones((1, 3))
    h = np.diag([0.0, 2.0 * math.pi, 0.0]).astype(complex)
    for j in range(3):
        for ell in range(j + 1, 3):
            h[j, ell] = 1j
            h[ell, j] = -1j
    A = -1j * h - K.conj().T @ K / 2.0
    target = np.array([[-1, 0, 0], [-2, -1 - 2j * math.pi, 0], [-2, -2, -1]], complex)
    amp = complex(expm(A)[2, 0])
    exact = math.exp(-1.0) * (-2.0 - 2j / math.pi)
    eta = abs(amp)**2
    exact_eta = CEILING * (1.0 + 1.0 / math.pi**2)
    require(np.max(np.abs(A - target)) < 1e-12, "Bypass Lindblad realization failed")
    require(np.max(np.abs(A + A.conj().T + 2.0 * np.ones((3, 3)))) < 1e-12,
            "Bypass damping matrix failed")
    require(abs(amp - exact) < 1e-12, "Bypass exact amplitude failed")
    require(eta > CEILING, "Bypass should exceed the unique-path ceiling")
    return dict(time=1.0, amplitude_real=amp.real, amplitude_imag=amp.imag,
                probability=eta, exact_probability=exact_eta,
                amplitude_residual=abs(amp - exact),
                scope="One direct bypass is present; this is not a nearest-neighbor path.")


def run_checks() -> dict:
    return {
        "scope": "Deterministic finite formula/model checks; not an all-design numerical optimization or a substitute for proof.",
        "conventions": {
            "gamma": "Upper bound on engineered diagonal amplitude damping nu_j.",
            "kappa": "Additional uniform amplitude damping; loss jumps are sqrt(2*kappa)*a_j.",
            "occupation_rates": "Twice the corresponding amplitude damping rates.",
            "endpoint_choice": "Unique positive cubic root maximizing the stated lower bound, capped at a/Gamma=1/2.",
        },
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "constants": {"zero_loss_probability_ceiling": CEILING,
                      "weak_loss_critical_x": CRITICAL_X,
                      "unconstrained_capacity_ceiling_qubits_per_use": math.log2(CEILING / (1.0 - CEILING))},
        "local_jump_realizations": check_local_jumps(),
        "phase_and_detuning_examples": check_phases_detunings(),
        "gamma_convolution_examples": check_gamma_convolution(),
        "internal_kernel_factorization": check_internal_kernel_factorization(),
        "weak_loss_convergence": check_weak_loss_sequence(),
        "exact_bypass": check_bypass(),
        "status": "passed",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "data" / "verification.json")
    args = parser.parse_args()
    record = run_checks()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, allow_nan=False) + "\n")
    print("Passed: local Lindblad realization, phase/detuning checks, gamma convolution,")
    print("internal-kernel factorization, finite bounds, weak-loss sequence, and exact bypass.")
    print(f"Verification record: {args.output}")


if __name__ == "__main__":
    main()
