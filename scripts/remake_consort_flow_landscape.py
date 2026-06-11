from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "consort_flow.png"


C = {
    "ink": "#1f2937",
    "muted": "#6b7280",
    "line": "#334155",
    "stage": "#374151",
    "neutral_fill": "#f1f5f9",
    "neutral_edge": "#334155",
    "game_fill": "#eff6ff",
    "game_edge": "#2563eb",
    "control_fill": "#f0fdf4",
    "control_edge": "#16a34a",
    "loss_fill": "#fef3c7",
    "loss_edge": "#b45309",
}


def box(ax, x, y, w, h, text, fill, edge, fs=10.5, weight="normal"):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1.4,
        edgecolor=edge,
        facecolor=fill,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        color=C["ink"],
        fontweight=weight,
        linespacing=1.25,
    )
    return patch


def stage(ax, text, x, y, w=0.12):
    patch = FancyBboxPatch(
        (x, y),
        w,
        0.035,
        boxstyle="round,pad=0.004,rounding_size=0.006",
        linewidth=0,
        facecolor=C["stage"],
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + 0.0175,
        text,
        ha="center",
        va="center",
        fontsize=8.8,
        color="white",
        fontweight="bold",
    )


def arrow(ax, start, end, rad=0.0):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=1.25,
            color=C["line"],
            connectionstyle=f"arc3,rad={rad}",
        )
    )


def elbow(ax, points):
    xs, ys = zip(*points)
    ax.plot(xs, ys, color=C["line"], linewidth=1.25, solid_capstyle="round")


def down_arrow(ax, x, y0, y1):
    arrow(ax, (x, y0), (x, y1))


def main() -> None:
    fig, ax = plt.subplots(figsize=(16, 9), dpi=220)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.955,
        "CONSORT Participant Flow",
        ha="center",
        va="center",
        fontsize=18,
        color=C["ink"],
        fontweight="bold",
    )
    stage(ax, "ENROLMENT", 0.44, 0.845, w=0.14)
    accessed = box(
        ax,
        0.08,
        0.74,
        0.24,
        0.09,
        "Accessed study website\n$n = 179$",
        C["neutral_fill"],
        C["neutral_edge"],
        fs=10.5,
    )
    assessed = box(
        ax,
        0.37,
        0.74,
        0.28,
        0.09,
        "Completed demographic form;\nassessed for pre-test completion\n$n = 124$",
        C["neutral_fill"],
        C["neutral_edge"],
        fs=10.0,
    )
    excluded = box(
        ax,
        0.73,
        0.725,
        0.22,
        0.12,
        "Excluded ($n = 32$)\nDid not complete pre-test",
        C["loss_fill"],
        C["loss_edge"],
        fs=10.0,
    )

    arrow(ax, (0.32, 0.785), (0.365, 0.785))
    arrow(ax, (0.65, 0.785), (0.725, 0.785))

    stage(ax, "RANDOMIZATION", 0.44, 0.64, w=0.14)
    randomized = box(
        ax,
        0.36,
        0.535,
        0.28,
        0.09,
        "Randomized\nblock randomization via assign.php\n$n = 92$",
        C["neutral_fill"],
        C["neutral_edge"],
        fs=10.0,
    )
    arrow(ax, (0.50, 0.74), (0.50, 0.63))

    stage(ax, "ALLOCATION", 0.44, 0.47, w=0.14)
    game_alloc = box(
        ax,
        0.10,
        0.36,
        0.30,
        0.09,
        "Allocated to game condition\n$n = 55$",
        C["game_fill"],
        C["game_edge"],
        fs=10.6,
        weight="bold",
    )
    ctrl_alloc = box(
        ax,
        0.60,
        0.36,
        0.30,
        0.09,
        "Allocated to control condition\n$n = 37$",
        C["control_fill"],
        C["control_edge"],
        fs=10.6,
        weight="bold",
    )
    elbow(ax, [(0.50, 0.535), (0.50, 0.49), (0.25, 0.49)])
    arrow(ax, (0.25, 0.49), (0.25, 0.455))
    elbow(ax, [(0.50, 0.49), (0.75, 0.49)])
    arrow(ax, (0.75, 0.49), (0.75, 0.455))

    stage(ax, "FOLLOW-UP", 0.44, 0.305, w=0.14)
    game_lost = box(
        ax,
        0.10,
        0.195,
        0.30,
        0.10,
        "Lost to follow-up / incomplete\n$n = 23$ (41.8%)\nPhase 1: 7  |  Phase 2: 12  |  Post-game survey: 4",
        C["loss_fill"],
        C["loss_edge"],
        fs=8.9,
    )
    ctrl_lost = box(
        ax,
        0.60,
        0.195,
        0.30,
        0.10,
        "Lost to follow-up / incomplete\n$n = 6$ (16.2%)\nDuring slide training: 4  |  After pre-test: 2",
        C["loss_fill"],
        C["loss_edge"],
        fs=8.9,
    )
    down_arrow(ax, 0.25, 0.36, 0.30)
    down_arrow(ax, 0.75, 0.36, 0.30)

    stage(ax, "ANALYSIS", 0.44, 0.135, w=0.14)
    game_analysis = box(
        ax,
        0.10,
        0.035,
        0.30,
        0.08,
        "Analyzed (per-protocol)\n$n = 32$",
        C["game_fill"],
        C["game_edge"],
        fs=10.5,
        weight="bold",
    )
    ctrl_analysis = box(
        ax,
        0.60,
        0.035,
        0.30,
        0.08,
        "Analyzed (per-protocol)\n$n = 31$",
        C["control_fill"],
        C["control_edge"],
        fs=10.5,
        weight="bold",
    )
    down_arrow(ax, 0.25, 0.195, 0.12)
    down_arrow(ax, 0.75, 0.195, 0.12)

    fig.savefig(OUT, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
