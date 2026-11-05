#!/usr/bin/env python3
"""Generate the two figures and their numerical tables.

Every finite curve is an evaluated explicit design or a rigorous analytic
bound. No curve represents an unproved numerical optimum over all designs.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

from verify_science import (
    ROOT, CEILING, CRITICAL_X, finite_family_point, weak_loss_limit,
)

FIGURES = ROOT / "figures"
DATA = ROOT / "data"


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def style_axes(ax) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["bottom", "left"]].set_color("#8b929b")
    ax.tick_params(colors="#333b45", labelsize=11)
    ax.grid(axis="y", color="#e0e4e8", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)


def save_figure(fig, name: str) -> None:
    fig.savefig(FIGURES / name, format="svg", metadata={
        "Title": name.removesuffix(".svg").replace("_", " "),
        "Description": "Explicit passive path constructions and rigorous bounds; see the accompanying data and reproducibility notes.",
        "Date": None,
    })
    plt.close(fig)


def finite_loss_figure() -> dict:
    delta = 1e-5
    sizes = np.unique(np.r_[np.round(np.geomspace(3, 20000, 150)).astype(int),
                            [20, 100, 500, 2000, 3000, 4000]])
    rows = [finite_family_point(int(n), delta) for n in sizes]
    write_csv(DATA / "finite_loss_comparison.csv", rows)
    y = lambda key: np.array([row[key] for row in rows])

    fig, ax = plt.subplots(figsize=(9.4, 5.9))
    fig.subplots_adjust(left=0.10, right=0.97, top=0.80, bottom=0.22)
    style_axes(ax)
    ax.set_xscale("log")
    ax.plot(sizes, y("universal_upper_bound"), color="#20252b", linewidth=1.9,
            linestyle=(0, (5, 3)), label="All-design upper bound", zorder=4)
    ax.fill_between(sizes, y("family_lower_bound"), y("family_probability"),
                    color="#2393ad", alpha=0.18, zorder=2)
    ax.plot(sizes, y("family_probability"), color="#007f9c", linewidth=2.5,
            label="Selected endpoint family", zorder=5)
    ax.plot(sizes, y("family_lower_bound"), color="#007f9c", linewidth=1.6,
            linestyle=(0, (1, 2)), label="Rigorous family lower bound", zorder=4)
    ax.plot(sizes, y("homogeneous_probability"), color="#a15e34", linewidth=2.0,
            label="Equal-damping family at its best time", zorder=3)
    ax.axhline(0.5, color="#a44360", linewidth=1.2, linestyle=(0, (4, 3)), zorder=1)
    ax.text(3.5, 0.487, r"$\eta=1/2$", color="#a44360", fontsize=10,
            va="top", bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.2))
    ax.set_ylim(0.0, 0.565)
    ax.set_xlim(3, 20000)
    ax.set_xticks([3, 10, 100, 1000, 10000])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda val, _: f"{int(val):,}"))
    ax.set_xlabel("Number of modes n", fontsize=12, labelpad=8)
    ax.set_ylabel(r"Transfer probability $\eta$", fontsize=12, labelpad=10)
    fig.text(0.10, 0.946, "Finite chains at fixed unavoidable loss", fontsize=17,
             weight="semibold", color="#20252b")
    fig.text(0.10, 0.898, r"$\kappa/\Gamma=10^{-5}$  |  $\Gamma$ caps diagonal amplitude damping",
             fontsize=11.5, color="#4d5865")
    fig.text(0.10, 0.854, "Endpoint rate maximizes the stated lower bound; it is not a global finite-chain optimum.",
             fontsize=10.5, color="#4d5865")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.21), ncol=2,
              frameon=False, fontsize=10.5, handlelength=3.0, columnspacing=1.8)
    save_figure(fig, "finite_loss_comparison.svg")
    return dict(kappa_over_gamma=delta, min_n=int(sizes.min()), max_n=int(sizes.max()),
                points=len(rows),
                table="data/finite_loss_comparison.csv",
                figure="figures/finite_loss_comparison.svg")


def weak_loss_figure() -> dict:
    xs = np.linspace(0.002, 0.08, 100)
    sizes = [20, 200, 2000, 20000]
    rows = []
    fig, ax = plt.subplots(figsize=(9.4, 5.9))
    fig.subplots_adjust(left=0.10, right=0.97, top=0.80, bottom=0.22)
    style_axes(ax)
    colors = ["#bd734c", "#4e789f", "#008d9d", "#1f5550"]
    for n, color in zip(sizes, colors):
        selected = []
        for x in xs:
            row = finite_family_point(n, float(x) / n)
            row["limiting_frontier_probability"] = weak_loss_limit(float(x))
            rows.append(row)
            selected.append(row["family_probability"])
        ax.plot(xs, selected, color=color, linewidth=2.0, label=f"Family: n = {n:,}", zorder=3)
    limit_x = np.linspace(0.0, 0.08, 250)
    ax.plot(limit_x, [weak_loss_limit(float(x)) for x in limit_x], color="#20252b",
            linewidth=2.1, linestyle=(0, (5, 3)), label=r"All-design limit ($n\to\infty$)", zorder=4)
    ax.axhline(0.5, color="#a44360", linewidth=1.2, linestyle=(0, (4, 3)), zorder=1)
    ax.axvline(CRITICAL_X, color="#8e949b", linewidth=1.2, linestyle=(0, (2, 3)), zorder=1)
    ax.scatter([CRITICAL_X], [0.5], s=35, color="#20252b", zorder=5)
    ax.annotate(r"$x_c=(\log 8-2)/2\approx0.03972$", xy=(CRITICAL_X, 0.5),
                xytext=(0.045, 0.535), fontsize=10.5, color="#303943",
                arrowprops=dict(arrowstyle="-", color="#59636f", linewidth=0.9),
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="none", alpha=0.95))
    ax.text(0.079, 0.503, r"$\eta=1/2$", ha="right", va="bottom", color="#a44360", fontsize=10)
    ax.set_xlim(0.0, 0.08)
    ax.set_ylim(0.365, 0.55)
    ax.set_xticks([0, 0.02, 0.04, 0.06, 0.08])
    ax.set_yticks([0.38, 0.42, 0.46, 0.50, 0.54])
    ax.set_xlabel(r"Scaled loss $x=n\kappa/\Gamma$", fontsize=12, labelpad=8)
    ax.set_ylabel(r"Transfer probability $\eta$", fontsize=12, labelpad=10)
    fig.text(0.10, 0.946, "The weak-loss crossover", fontsize=17, weight="semibold", color="#20252b")
    fig.text(0.10, 0.898, r"Finite designs approach $\eta_*(x)=(4/e^2)e^{-2x}$ as $n\to\infty$",
             fontsize=11.5, color="#4d5865")
    fig.text(0.10, 0.854, "Each finite curve uses the selected endpoint family; endpoint rates decrease and waiting times grow.",
             fontsize=10.5, color="#4d5865")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.21), ncol=3,
              frameon=False, fontsize=10.5, handlelength=2.5, columnspacing=1.5)
    write_csv(DATA / "weak_loss_crossover.csv", rows)
    save_figure(fig, "weak_loss_crossover.svg")
    return dict(sizes=sizes, min_x=float(xs.min()), max_x=float(xs.max()),
                points_per_size=len(xs), table="data/weak_loss_crossover.csv",
                figure="figures/weak_loss_crossover.svg",
                zero_loss_endpoint="The finite cubic-rate curves start at x>0. At x=0 the bound's optimum requires a->0 and unbounded waiting time.")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "svg.fonttype": "none", "svg.hashsalt": "directional-passive-paths",
        "axes.labelcolor": "#303943", "text.color": "#303943",
        "figure.facecolor": "white", "axes.facecolor": "white",
    })
    metadata = {
        "matplotlib_version": matplotlib.__version__,
        "endpoint_selection": "Positive cubic root maximizing the rigorous family lower bound; capped at a/Gamma=1/2.",
        "time_selection": "The selected family uses Gamma*t=(n-2)+Gamma/a. The homogeneous curve uses its exact optimum Gamma*t=(n-1)/(1+kappa/Gamma).",
        "no_finite_global_optimum": "Evaluated finite curves are constructions, not all-design optimized values.",
        "gamma_convention": "Gamma caps engineered diagonal amplitude damping, not each edge amplitude or occupation damping.",
        "constants": {"probability_ceiling": CEILING, "critical_scaled_loss": CRITICAL_X},
        "finite_loss": finite_loss_figure(),
        "weak_loss": weak_loss_figure(),
    }
    (DATA / "figure_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print("Wrote two SVG figures and their CSV tables.")
    print(FIGURES / "finite_loss_comparison.svg")
    print(FIGURES / "weak_loss_crossover.svg")


if __name__ == "__main__":
    main()
