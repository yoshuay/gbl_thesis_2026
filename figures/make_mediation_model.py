"""Generate the H2 path diagram (game group, n = 32): the full hypothesised
network including cognitive load. Solid black paths = significant
unstandardised coefficients from the mediation model (ADAPTS on its native
1-7 scale). Dashed grey paths = hypothesised cognitive-load relationships,
shown as bivariate correlations, none significant.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

BOX = dict(facecolor="white", edgecolor="#5a5a5a", linewidth=2.4)


def box(ax, cx, cy, w, h, text, fontsize=11):
    ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, **BOX, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            fontweight="bold", zorder=4)


fig, ax = plt.subplots(figsize=(9.2, 4.8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

box(ax, 0.13, 0.82, 0.24, 0.18, "Cognitive load\n(CL)", 10.5)
box(ax, 0.56, 0.82, 0.26, 0.18, "Self-efficacy\n(SE)", 10.5)
box(ax, 0.13, 0.25, 0.24, 0.18, "Engagement\n(ENG)", 10.5)
box(ax, 0.87, 0.25, 0.24, 0.18, "Performance\n(ADAPTS-SV)", 10.5)

GREY = "#9a9a9a"

# CL -> SE (hypothesised negative; observed ns)
ax.add_patch(FancyArrowPatch((0.255, 0.82), (0.425, 0.82), arrowstyle="-|>",
                             mutation_scale=14, color=GREY, linewidth=1.6,
                             linestyle=(0, (5, 4)), zorder=2))
ax.text(0.34, 0.875, r"$r$ = .04 ns", fontsize=9.5, fontweight="bold",
        color="#7a7a7a", ha="center")

# CL -> ENG (hypothesised negative; observed ns)
ax.add_patch(FancyArrowPatch((0.13, 0.72), (0.13, 0.355), arrowstyle="-|>",
                             mutation_scale=14, color=GREY, linewidth=1.6,
                             linestyle=(0, (5, 4)), zorder=2))
ax.text(0.115, 0.54, r"$r$ = .24 ns", fontsize=9.5, fontweight="bold",
        color="#7a7a7a", ha="right")

# a: ENG -> SE
ax.add_patch(FancyArrowPatch((0.235, 0.345), (0.46, 0.715), arrowstyle="-|>",
                             mutation_scale=16, color="black", linewidth=1.8, zorder=2))
ax.text(0.385, 0.475, r"a = 0.89***", fontsize=10.5, fontweight="bold", ha="left")

# b: SE -> ADAPTS
ax.add_patch(FancyArrowPatch((0.665, 0.715), (0.845, 0.37), arrowstyle="-|>",
                             mutation_scale=16, color="black", linewidth=1.8, zorder=2))
ax.text(0.785, 0.585, r"b = 1.24***", fontsize=10.5, fontweight="bold", ha="left")

# c': ENG -> ADAPTS direct (grey solid = tested, ns after mediation)
ax.add_patch(FancyArrowPatch((0.26, 0.25), (0.74, 0.25), arrowstyle="-|>",
                             mutation_scale=16, color=GREY, linewidth=1.8, zorder=2))
ax.text(0.50, 0.295, r"c$'$ = 0.31 ns", fontsize=10.5, fontweight="bold",
        color="#7a7a7a", ha="center")
ax.text(0.50, 0.175, r"(c = 1.41***)", fontsize=10, color="#7a7a7a", ha="center")

ax.text(0.50, 0.02,
        "Indirect effect a$\\times$b = 1.10, 95% CI [.43, 2.24].  "
        "Dashed paths: hypothesised CL relationships, ns (CL$-$performance: $r$ = .17 ns).",
        fontsize=9.5, ha="center")

fig.tight_layout()
fig.savefig("figures/mediation_path_model.png", dpi=200, bbox_inches="tight")
print("saved figures/mediation_path_model.png")
