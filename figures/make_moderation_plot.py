"""Generate the continuous moderation interaction figure (post ~ condition x pre).

Reproduces the pre-registered moderation models reported in the Results chapter
and renders fitted condition-specific regression lines over the raw data.
"""
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/participants_log_final_63.csv")
df = df[df["grp"].isin(["game", "control"])].copy()
print("N =", len(df), "| game:", (df.grp == "game").sum(), "control:", (df.grp == "control").sum())

panels = [
    ("adapts_pre_score", "adapts_post_score", "Performance (ADAPTS-SV, %)", "performance"),
    ("pre_se_score", "post_se_score", "Sales self-efficacy (SE, %)", "SE"),
]

colors = {"game": "#C0392B", "control": "#2C5F8A"}
labels = {"game": "Game", "control": "Control"}

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharey=False)

for ax, (pre_col, post_col, title, short) in zip(axes, panels):
    d = df.dropna(subset=[pre_col, post_col]).copy()
    pre_c = d[pre_col] - d[pre_col].mean()
    cond = (d["grp"] == "game").astype(float)
    X = np.column_stack([np.ones(len(d)), cond, pre_c, cond * pre_c])
    y = d[post_col].to_numpy(dtype=float)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    df_err = len(d) - 4
    mse = resid @ resid / df_err
    # F-test for the interaction term
    Xr = X[:, :3]
    br, *_ = np.linalg.lstsq(Xr, y, rcond=None)
    rr = y - Xr @ br
    F = ((rr @ rr - resid @ resid) / 1) / mse
    print(f"{title}: beta_int = {beta[3]:.3f}, F(1,{df_err}) = {F:.2f}")

    for g in ["control", "game"]:
        sub = d[d["grp"] == g]
        ax.scatter(sub[pre_col], sub[post_col], s=28, alpha=0.65,
                   color=colors[g], edgecolor="white", linewidth=0.5, label=labels[g])
        xs = np.linspace(d[pre_col].min(), d[pre_col].max(), 50)
        xc = xs - d[pre_col].mean()
        c = 1.0 if g == "game" else 0.0
        ys = beta[0] + beta[1] * c + beta[2] * xc + beta[3] * c * xc
        ax.plot(xs, ys, color=colors[g], linewidth=2)

    ax.set_xlabel(f"Pre-test {short} (%)")
    ax.set_ylabel(f"Post-test {short} (%)")
    ax.set_title(title, fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, loc="lower right", fontsize=9)

fig.tight_layout()
fig.savefig("figures/continuous_moderation_interaction.png", dpi=200)
print("saved figures/continuous_moderation_interaction.png")
