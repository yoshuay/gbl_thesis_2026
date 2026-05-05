# Peer Review Report — Reviewer 1 (Methodology)

## Manuscript Information
- **Title**: For Whom Does Game-Based Learning Training Work? An RCT of a Scaffolded Digital Simulation for B2B Sales Training
- **Manuscript ID**: GBL-Thesis-2026
- **Review Date**: 2026-04-30
- **Review Round**: Round 1

---

## Reviewer Information

### Reviewer Role
Peer Reviewer 1 — Quantitative Methodology / Experimental Design

### Reviewer Identity
Associate Professor of Quantitative Research Methods in Education, specialising in experimental and quasi-experimental designs for learning interventions. Has published on ANCOVA assumptions in small-N educational studies, attrition bias in online RCTs, power analysis practices in educational technology research, and ITT/per-protocol analytical frameworks. Regular reviewer for *Journal of Educational Psychology*, *Educational Psychology Review*, and *Behavior Research Methods*. Deeply familiar with the interpretive limits of post-hoc moderator analysis and the conditions under which cluster-derived subgroup effects are scientifically defensible.

### Review Focus
My evaluation focuses on three areas: (1) the design integrity and statistical analysis plan, including ANCOVA assumptions, mediation validity, and the pre-registered continuous moderation; (2) the cluster analysis — its k-selection justification, circularity protection, stability evidence, and the relationship between cluster-level and continuous-moderation evidence; (3) the ROC analysis and the AUC-based deployment recommendation, whose sample size properties I find most concerning in this manuscript.

---

## Overall Assessment

### Recommendation
- [x] **Major Revision** — Substantial revisions needed, re-review required after revision

### Confidence Score
5 — Completely within my area of expertise, very confident in my assessment

### Summary Assessment
This paper reports a pre-registered RCT evaluating a digital game-based intervention for B2B sales training, with ANCOVA as the primary analysis and a cluster-derived moderator analysis as the principal exploratory contribution. The design is more rigorous than most published GBL studies: pre-registration, blocked allocation, ITT sensitivity analyses, and power reporting are all present and appropriate. The mediation analysis (SE fully mediates ENG→ADAPTS; bootstrapped indirect effect=1.10) and Fisher z coupling comparison are well-executed for the sample size and represent the paper's strongest statistical contributions.

However, the paper has a hierarchy problem: the unregistered cluster analysis and the cluster-derived effect sizes (especially d=−1.88 for C1, n=4 game-arm completers) carry the greatest rhetorical weight in the Discussion and Conclusion, while the pre-registered continuous moderation analysis — which carries greater evidential weight and is less vulnerable to researcher degrees of freedom — is presented as supporting rather than primary evidence. This inversion is scientifically backwards and must be corrected.

Additionally, the germane cognitive load subscale (α=.31) has internal consistency below any defensible threshold for a psychometric instrument used in quantitative inference. The CL decomposition finding (CL1 d=0.13 ns vs. CL2+CL3 d=0.90) relies on this subscale and therefore cannot be interpreted as reflecting the latent construct of germane load. Finally, the ROC analysis yielding AUC=0.985 from n=10 positives presents a precision estimate that the sample size cannot support. These three issues require substantive revision.

---

## Strengths

### S1: Pre-Registered ANCOVA Design with Covariate Baseline Control
The use of pre-test scores as covariates in ANCOVA is the appropriate primary analysis for this design — not gain scores (which inflate Type I error under differential pretest variability) and not raw post-test comparison (which ignores baseline variation). The report of both the covariate correlation (used in power estimation) and the full ANCOVA table with F, df, p, and η²p is exemplary. Table 5.1 and 5.2 present these clearly.

### S2: ITT Sensitivity Analyses Are Conducted and Reported Transparently
The two-pronged ITT approach — (a) no-gain imputation for the 38 non-completers and (b) worst-case bounding — brackets the per-protocol result and allows readers to assess directional robustness. The finding that ITT-A yields SE p=.035* (strengthening the control direction) while ITT-B worst-case remains non-significant provides useful boundary information. The explicit acknowledgement that "ITT-A direction is consistent with the per-protocol trend" (p. xliii) is appropriately cautious.

### S3: Bootstrapped Mediation with Confidence Interval Reporting
The decision to use bootstrap-estimated confidence intervals for the indirect effect (rather than the Sobel test, which assumes normality and underestimates power at small N) is methodologically appropriate. The 95% CI [.43, 2.24] for β_indirect=1.10 does not include zero, providing defensible evidence for the mediation chain (ENG → SE → ADAPTS). The limitation that this is within-group only and observed from completer data is acknowledged.

### S4: Cluster Stability via 100-Seed ARI Analysis
The 100-random-seed ARI=1.000 stability result is a meaningful addition to the cluster analysis, demonstrating that the k=3 solution is not sensitive to initialisation. This type of stability check is underused in educational research cluster analyses and adds credibility to the basic cluster structure.

### S5: Transparent Retrospective Power Analysis
Table 6.1 reporting observed η²p, N, α, and achieved power for each outcome — alongside the N required for 80% power — is unusually transparent. The acknowledgement that the study was powered only for CL (power=0.792) but substantially underpowered for SE (0.462) and ADAPTS (0.313) contextualises the null findings appropriately and should inform how reviewers and readers interpret the primary outcomes.

---

## Weaknesses

### W1: Germane Cognitive Load Subscale α=.31 Invalidates the CL Decomposition Analysis
**Problem**: The paper reports (§6.8, Limitation, and briefly in the CL results) that the germane load subscale (CL1) had internal consistency α=.31. The paper proceeds to use CL1 scores in the decomposition analysis (CL1 d=0.13 ns; CL2+CL3 d=0.90) and treats this dissociation as supporting the conclusion that the game imposed "extraneous rather than germane" load. An internal consistency of α=.31 is below any scientifically defensible threshold for a psychometric instrument; α<.50 is typically considered insufficient for research use (Nunnally, 1978; George & Mallery, 2003). At α=.31, the subscale's item intercorrelations are effectively near-zero, meaning CL1 scores are dominated by measurement error rather than the target construct.

**Why it matters**: The extraneous/germane decomposition is central to the paper's mechanistic interpretation in §6.2 and §7. The "CL as currency" metaphor — and the claim that "participants found the game harder and more complex, but did not invest more deliberate effort" — depends critically on the validity of the CL1 (germane/effort) subscale. If this subscale is unreliable, the dissociation cannot be attributed to construct-level differences and the mechanistic interpretation is unsupported by the data as measured.

**Suggestion**: The authors have two options. Option A (preferred): Report the CL1 finding only as a descriptive trend, remove it from the mechanistic interpretation in §6.2 and §7, and reframe the CL finding as "the game produced higher perceived difficulty and complexity (CL2+CL3 d=0.90), while the directed effort measure was unreliable (α=.31) and should not be interpreted." Option B: If the original CL items were retained, the authors could report item-level statistics and attempt to identify which item(s) contributed to poor internal consistency; but a single-study fix of a validated instrument is not appropriate, and the germane subscale's original formulation in the CL literature (Leppink et al., 2013) was not used here.

**Severity**: Critical

### W2: Continuous Moderation Analysis Should Be Presented as Primary Expertise-Effect Evidence; Cluster Analysis as Exploratory Secondary
**Problem**: The pre-registered continuous moderation analysis (pre-ADAPTS × condition interaction, F(1,59)=11.65, p=.0012; pre-SE × condition, F(1,59)=5.52, p=.022) provides the pre-registered primary evidence for expertise-conditional effects. Yet the manuscript presents the cluster analysis (unregistered) in §5.6 as the headline expertise story, with the continuous moderation appearing in §5.7 in a supporting role. The simple slopes from the continuous moderation (Low-1SD: −15.17pp; Mean: −4.83pp; High+1SD: +5.51pp) are compelling and tell a coherent directional story consistent with the cluster pattern — but they are confirmatory while the cluster-derived d=−1.88 is not. This hierarchy is inverted.

**Why it matters**: Readers and subsequent researchers who rely on this paper will attribute the expertise-reversal finding to the cluster analysis (because it drives the headlines and carries the d-value rhetoric) when the pre-registered moderation provides the confirmatory evidence. This risks misrepresenting the paper's evidential structure in downstream citations.

**Suggestion**: Restructure §5 to present the continuous moderation analysis (§5.7 current) as "Primary Expertise-Effect Analysis (Pre-Registered)" and the cluster analysis (§5.6 current) as "Exploratory Expertise Profiling (Unregistered)." The Discussion should then lead with the continuous moderation as the confirmatory finding and treat the cluster patterns as illustrative elaboration. The d-values from the cluster strata should be presented with appropriate hedging and confidence intervals.

**Severity**: Critical

### W3: k=3 Selection Justification Is Insufficient; Cluster Analysis Results Should Include CIs on Effect Sizes
**Problem**: The justification for k=3 over k=2 or k=4 relies on silhouette analysis (silhouette=0.49 for k=3 vs. "lower" for alternatives, not reported) and the within-cluster homogeneity criterion. However, silhouette=0.49 is in the "acceptable but not strong" range (Kaufman & Rousseeuw, 1990), and k=2 (simple novice/experienced split) would have been more theoretically parsimonious and would have produced a larger cell size in the novice stratum — potentially yielding more reliable cluster-conditional effect estimates. The paper does not report the silhouette value for k=2 or k=4 to allow readers to evaluate the selection.

**Why it matters**: With k=3 and n=10 in C1 (n=4 game-arm completers), the cluster structure maximally fragments the sample. A k=2 solution with n=10 novices split between arms (say ~5 each) would still yield small but less extreme cells, and the d=−1.88 estimate would not be as fragile. The choice of k=3 over k=2 is a methodological decision with major consequences for the headline effect size — and it deserves explicit justification.

**Suggestion**: Report the silhouette values for k=2, k=3, and k=4 in a table or supplementary material. Justify the choice of k=3 based on these values. Report 95% confidence intervals (bootstrapped) on the d estimates for each cluster-conditional comparison, particularly C1 (d=−1.88) where the interval will be very wide. If k=2 yields a more defensible solution, consider presenting k=2 as the primary cluster analysis.

**Severity**: Major

### W4: ANCOVA Assumption Reporting Is Incomplete
**Problem**: ANCOVA requires (a) homogeneity of regression slopes (the treatment effect does not depend on the covariate — ironically, this assumption is violated if the continuous moderation hypothesis is correct), (b) covariate measured without error, and (c) normality of residuals. The paper does not report tests of these assumptions. The homogeneity of regression slopes assumption is particularly relevant here: if pre-ADAPTS × condition interaction is significant (which the moderation analysis confirms it is), then the standard ANCOVA is formally misspecified for the ADAPTS outcome, and ANCOVA-adjusted means should be interpreted with caution.

**Why it matters**: If the homogeneity of regression slopes assumption is violated for ADAPTS, the ANCOVA null finding may reflect the averaging of opposing slopes rather than a true null. This would be consistent with the moderation results but would undermine the interpretation of the ANCOVA as a clean primary analysis.

**Suggestion**: Report the results of the homogeneity of regression slopes test for each primary outcome. If the assumption is violated for ADAPTS (which seems likely given the moderation results), acknowledge this explicitly and discuss whether a moderated regression model might be a more appropriate primary analysis for revision.

**Severity**: Major

### W5: ROC Threshold AUC Confidence Interval Not Reported; Small-N Instability Not Acknowledged in Results
**Problem**: The ROC analysis identifies a threshold of ≤46.7% ADAPTS with AUC=0.985 (§5.7, §6.7). AUC estimates from binary classifiers with n=10 in the positive class are substantially influenced by individual case placement. The 95% CI on AUC=0.985 with n=10/n=53 is approximately 0.93–1.00 at best, but the upper bound is constrained at 1.0, which makes this effectively an uninformative interval. The reported AUC should be accompanied by its 95% CI (using the DeLong, DeLong & Clarke-Pearson, 1988, method or bootstrapping), and the text should explicitly note that AUC precision at n=10 positives is limited.

**Suggestion**: Add the AUC 95% CI to the text wherever AUC=0.985 appears. Change "deployable screening criterion" to "provisional screening threshold requiring validation in an independent, prospectively collected sample" everywhere it appears.

**Severity**: Major

---

## Detailed Comments

### Methodology / Research Design
Allocation concealment is described but the specific mechanism (automated alternating assignment vs. researcher allocation) is not entirely clear from §4.2. The paper should clarify whether participants were allocated automatically or manually and how the blocking was implemented. Were assessors blinded to condition during data collection? (Likely not possible in self-report, but should be stated.)

### Results / Findings
The Fisher z comparison of SE–ADAPTS correlations (r=.877 game vs. r=.532 control, p=.004) is an unusual but appropriate test. The paper should verify that the two samples are independent (game completers and control completers are independent by design) and state this explicitly, as Fisher z is formulated for independent samples. The test correctly uses Fisher's transformation prior to the z-test.

The within-group pre-post change statistics (Table 5.3) are presented as means and standard deviations without formal tests — appropriate given that between-group ANCOVA is the primary analysis — but the paper should note explicitly that within-group changes are descriptive only and cannot be interpreted as causal in isolation.

The mediation model (§5.5) uses complete-case data for the game group only. The potential for selection bias (completers vs. non-completers) in the game group mediation model should be noted here, not only in §6.8.

### Discussion
The CL decomposition discussion in §6.2 should be prefaced with a clear statement that the germane subscale's α=.31 limits the inferential status of the CL1 vs. CL2+CL3 dissociation. Without this caveat, readers will misread the mechanistic interpretation as empirically established.

---

## Questions for Authors

1. Were the ANCOVA homogeneity of regression slopes assumptions formally tested for each outcome? If so, what were the results, and how do they bear on the interpretation of the ANCOVA F-tests given that the continuous moderation confirms the pre-ADAPTS × condition interaction?

2. Was k=2 evaluated as a cluster solution? What were the silhouette values for k=2, k=3, and k=4? If k=2 yields competitive silhouette performance, why was k=3 selected?

3. What was the correlation between the three CL subscale items that comprise CL1 (directed mental effort)? Is there a specific item responsible for the poor internal consistency, or is the subscale uniformly unreliable in this sample?

4. The bootstrapped mediation CI [.43, 2.24] is wide. What was the bootstrap sample size (n iterations) used? Was the percentile method or the bias-corrected accelerated (BCa) method used?

---

## Minor Issues

### Statistical Reporting
- Effect size CIs are missing for cluster-conditional d values throughout §5.6. These should be added for C1 in particular.
- Bootstrap iterations and method (percentile vs. BCa) for the mediation should be stated in §4.5.
- The ANCOVA F, df, p, and η²p are well reported; residual normality and homoscedasticity tests are not mentioned.

### Figures and Tables
- Table 5.5 (cluster profiles) would benefit from a column showing n per arm within each cluster (game vs. control completers).

---

## Dimension Scores

| Dimension | Score (0–100) | Descriptor | Notes |
|---|---|---|---|
| Originality (20%) | 68 | Adequate–Strong | Continuous moderation + ITT + mediation combination is novel for GBL; cluster-as-primary-finding is less original |
| Methodological Rigor (25%) | 58 | Adequate | RCT and ITT are strong; α=.31 for CL1, unregistered cluster hierarchy, ANCOVA assumption gap reduce score |
| Evidence Sufficiency (25%) | 62 | Adequate | Mediation and Fisher z well-supported; cluster strata too thin for headline claims; ROC n=10 insufficient |
| Argument Coherence (15%) | 70 | Adequate–Strong | Confirmatory/exploratory hierarchy inversion is the key coherence problem |
| Writing Quality (15%) | 80 | Strong | Precise statistical language; some minor inconsistencies in labelling CL subscales |
| **Weighted Average** | **64** | **Major Revision** | Pre-registered design is a genuine asset; α=.31 and cluster hierarchy issues must be resolved |
