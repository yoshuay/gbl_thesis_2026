# GBL Thesis — Status & Revision Roadmap

**Manuscript**: For Whom Does Game-Based Learning Training Work? An RCT of a Scaffolded Digital Simulation for B2B Sales Training
**Author**: Yoshua Yanottama
**Last updated**: 2026-05-05
**Current stage**: Post peer review — Major Revision

---

## Repo structure

```
gbl-thesis/
├── main.tex            ← Working LaTeX manuscript (compiles clean, 72 pages)
├── main.pdf            ← Latest compiled output
├── figures/            ← Drop figure files here (currently placeholders)
├── data/
│   └── participants_log_final_63.csv   ← N=63 completer dataset
├── reviews/
│   ├── review_eic.md
│   ├── review_r1_methodology.md
│   ├── review_r2_domain.md
│   ├── review_r3_practitioner.md
│   ├── review_devils_advocate.md
│   └── editorial_decision.md
└── STATUS.md           ← this file
```

---

## Compile

```bash
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```
Three passes resolve all cross-references. No BibTeX used (citations inline).
Compiles clean with no undefined references as of 2026-05-05.

---

## Review outcome

| Reviewer | Role | Decision | Score |
|---|---|---|---|
| EIC | Editor-in-Chief | Major Revision | 69 |
| R1 | Quantitative Methodology | Major Revision | 64 |
| R2 | GBL / Instructional Design | **Minor Revision** | 74 |
| R3 | Sales Training / HRD | Major Revision | 66 |
| DA | Devil's Advocate | — | — |
| **Overall** | | **Major Revision** | **68** |

---

## Required revisions (R1–R8)

| # | Issue | Source | Status |
|---|---|---|---|
| R1 | Lead with pre-registered continuous moderation; cluster analysis as exploratory secondary | R1-W2, DA-MAJOR-3 | ⬜ pending |
| R2 | Drop CL germane subscale claim (α=.31); use total CL + design logic + behavioral log | R1-W1 (Critical) | ⬜ pending |
| R3 | Reframe ROC as provisional; remove "deployable screening criterion" language | DA-CRITICAL-1, R1-W5 | ⬜ pending |
| R4 | Characterise non-completing novice exit timing using behavioral log | DA-CRITICAL-2 | ⬜ pending |
| R5 | Add LM-GM alignment table (supplementary) mapping mechanics → learning mechanic → Bloom level | R2-W1 | ⬜ pending |
| R6 | Add ANCOVA homogeneity of regression slopes test results | R1-W4 | ⬜ pending |
| R7 | Recalibrate practical recommendations to "adaptive selling training in professional development contexts" not "B2B sales training broadly" | R3-W1 | ⬜ pending |
| R8 | Consistently use "self-reported adaptive selling beliefs" not "adaptive selling competency" | R3-W2 | ⬜ pending |

---

## Suggested revisions (S1–S10)

| # | Issue | Source | Status |
|---|---|---|---|
| S1 | Report silhouette values for k=2, k=3, k=4; justify k=3 selection | R1-W3 | ⬜ pending |
| S2 | Add bootstrapped CIs on cluster-conditional d values (esp. C1 d=−1.88) | R1-W3 | ⬜ pending |
| S3 | Add AUC 95% CI on ROC result | R1-W5 | ⬜ pending |
| S4 | Engage Mayer's CTML (coherence/signalling principles) in §2/§3 | R2-W2 | ⬜ pending |
| S5 | Cite Leppink et al. (2013) in measures section; explain why used instead | R2-W2 | ⬜ pending |
| S6 | Cite DDA literature (Serrano-Laguna et al., 2012; Zohaib, 2018) for dynamic difficulty recommendation | R2-W2 | ⬜ pending |
| S7 | Connect BPD concept to Gagné (1985) prerequisite conditions / Merrill (2002) First Principles | R2-W4 | ⬜ pending |
| S8 | Elevate format–measurement alignment concern from Limitation 6 to more prominent Discussion placement | R3-W3, DA-MAJOR-2 | ⬜ pending |
| S9 | Describe control condition content more fully (§4.2 or supplementary) | R2-W3, R3-W4 | ⬜ pending |
| S10 | Add paragraph in §6.7 addressing organisational barriers to expertise-routing implementation | R3 Discussion comment | ⬜ pending |

---

## Design decisions in progress

These are unresolved before revision work can begin on the relevant sections.

### 1. Framework naming (supervisor input)
Supervisor suggested proposing a **defined framework** rather than just extending Arnab et al. (2015). Working candidates:
- MTC (Mechanics Transparency Coefficient) + BPD (Bloom-level Prerequisite Dependency) as named criteria
- Needs a framework name and three explicit testable criteria
- **Decision needed**: Name the framework, operationalise MTC/BPD

### 2. Dropout/attrition handling (supervisor input)
Supervisor suggested removing dropouts from the analysis. Recommended alternative: keep attrition statistic (41.8% vs 16.2%, Fisher's p=.010) but shorten §6.6 and move interpretation to Limitations.
- Removing entirely leaves n=4 C1 game-arm completers unexplained
- **Decision needed**: Shorten §6.6 vs. full removal

### 3. ITT renaming
- ITT-A → "ITT no-gain imputation"
- ITT-B → "ITT worst-case boundary"
- **Status**: Recommended and agreed in principle; not yet implemented in main.tex

### 4. Cluster demographic validation
Available from `data/participants_log_final_63.csv`:
- C1 (n=10): 100% have <3yr sales experience (supports cluster = novice)
- Game familiarity: no clean separation across C1/C2/C3 (supports domain expertise, not gaming fluency, as operative moderator)
- **Status**: Analysis done; write-up not yet added to §5.6 or §6.4

### 5. Bootstrap cluster stability
Run Jaccard resampling via `clusterboot()` (R) to complement ARI=1.000 result.
**Status**: Not yet run

### 6. CL instrument item mapping
4 items in data: cl_1, cl_2, cl_3, cl_4. Which grouping caused α=.31? Need to confirm to write the caveat sentence correctly.
**Status**: Needs author clarification

---

## Key statistics (reference)

| Outcome | F | df | p | η²p | Power |
|---|---|---|---|---|---|
| SE (H1a) | 3.56 | 1,60 | .064† | .056 | 0.462 |
| ADAPTS (H1b) | 2.22 | 1,60 | .141 | .036 | 0.313 |
| CL total | — | — | — | — | 0.792 |

**Continuous moderation (pre-registered)**
- pre-ADAPTS × condition: F(1,59)=11.65, p=.0012
- pre-SE × condition: F(1,59)=5.52, p=.022
- Simple slopes (ADAPTS): Low−1SD=−15.17pp, Mean=−4.83pp, High+1SD=+5.51pp

**Cluster profiles (k=3, pre-intervention features only)**
- C1 Novice (n=10): pre_SE=2.31, pre_ADAPTS=33.0% → 100% have <3yr sales exp
- C2 Moderate (n=28): pre_SE=3.40, pre_ADAPTS=57.1%
- C3 Advanced (n=25): pre_SE=4.17, pre_ADAPTS=80.7%
- ARI=1.000 (100-seed stability), Silhouette=0.49

**Mediation (game group completers only)**
- ENG → SE → ADAPTS; indirect effect=1.10, 95% CI [.43, 2.24]
- SE–ADAPTS coupling: r=.877 (game) vs. .532 (control), Fisher z p=.004

**Attrition**: 41.8% game vs. 16.2% control, Fisher's exact p=.010, OR=0.28
