from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Rectangle


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "expertise_reversal_heatmap.png"


rows = [
    "SE change",
    "ADAPTS gain",
    "CL reduction",
    "Engagement",
    "Transfer intent",
]

cols = [
    "Low expertise\n(4G / 6C)",
    "Moderate expertise\n(15G / 13C)",
    "High expertise\n(13G / 12C)",
]

# Cohen's d values are oriented so positive values always indicate a game
# advantage. The cognitive-load row is coded as CL reduction, so positive means
# the game lowered cognitive load relative to control.
values = np.array(
    [
        [-0.73, -0.65, -0.07],
        [-1.88, -0.15, 0.24],
        [-0.25, -1.05, -0.55],
        [-2.06, -0.27, -0.43],
        [-1.46, -0.42, -0.15],
    ]
)

labels = [
    ["-0.73", "-0.65\u2020", "-0.07"],
    ["-1.88***", "-0.15", "+0.24"],
    ["-0.25", "-1.05**", "-0.55"],
    ["-2.06**", "-0.27", "-0.43"],
    ["-1.46*", "-0.42", "-0.15"],
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(10.4, 6.2), dpi=220)
    norm = TwoSlopeNorm(vmin=-2.2, vcenter=0, vmax=2.2)
    cmap = plt.get_cmap("RdBu")

    image = ax.imshow(values, cmap=cmap, norm=norm, aspect="auto")

    ax.set_xticks(np.arange(len(cols)), labels=cols, fontsize=10)
    ax.set_yticks(np.arange(len(rows)), labels=rows, fontsize=10)
    ax.tick_params(axis="both", length=0)

    ax.set_title(
        "Game vs Control by Pre-Intervention Expertise",
        fontsize=14,
        fontweight="bold",
        pad=26,
    )
    ax.text(
        0.5,
        1.045,
        "Cohen's d, RCT-clean; blue = game advantage, red = control advantage",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        color="#374151",
    )

    ax.set_xticks(np.arange(-0.5, len(cols), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(rows), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2.4)
    ax.tick_params(which="minor", bottom=False, left=False)

    for row in range(values.shape[0]):
        for col in range(values.shape[1]):
            v = values[row, col]
            color = "white" if abs(v) > 1.15 else "#111827"
            ax.text(
                col,
                row,
                labels[row][col],
                ha="center",
                va="center",
                fontsize=11,
                fontweight="bold",
                color=color,
            )

    for spine in ax.spines.values():
        spine.set_visible(False)

    cbar = fig.colorbar(image, ax=ax, fraction=0.045, pad=0.18)
    cbar.set_ticks([-2, -1, 0, 1, 2])
    cbar.ax.tick_params(labelsize=9)
    cbar.set_label("Cohen's d\n(+ = game advantage)", fontsize=10, labelpad=10)

    fig.subplots_adjust(left=0.18, right=0.84, top=0.82, bottom=0.15)
    fig.savefig(OUT, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
