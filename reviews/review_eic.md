# Peer Review Report — Editor-in-Chief

## Manuscript Information
- **Title**: For Whom Does Game-Based Learning Training Work? An RCT of a Scaffolded Digital Simulation for B2B Sales Training
- **Manuscript ID**: GBL-Thesis-2026
- **Review Date**: 2026-04-30
- **Review Round**: Round 1

---

## Reviewer Information

### Reviewer Role
Editor-in-Chief / Senior Associate Editor

### Reviewer Identity
Senior Associate Editor at *British Journal of Educational Technology*, with 15 years of experience editing and publishing empirical GBL research in professional and higher education contexts. Author of systematic reviews on DGBL effectiveness and editorial advisory experience at *Computers & Education*. Prioritises papers that offer clear, generalisable design implications alongside rigorous empirical evidence.

### Review Focus
This review evaluates the paper's fit with a Q1/Q2 educational technology journal, the publishability of its theoretical and practical contributions, and whether the central expertise-conditional story is supported with sufficient evidential rigour to warrant the claims made in the Discussion and Conclusion. I am not the primary arbiter of statistical fine-detail — that is Reviewer 1's role — but I assess whether the paper's framing of findings is proportionate to the evidence and whether the theoretical extension is a genuine scholarly advance.

---

## Overall Assessment

### Recommendation
- [x] **Major Revision** — Substantial revisions needed, re-review required after revision

### Confidence Score
4 — Mostly within my area of expertise, high confidence

### Summary Assessment
This thesis evaluates a scaffolded digital game-based intervention against a conventional digital module for B2B sales training using a pre-registered online RCT (N=63 completers). The primary ANCOVA outcomes are null or marginal; the paper's positive contribution is built on exploratory cluster analysis revealing an expertise-conditional reversal pattern, combined with a theoretically rich reinterpretation of the LM-GM framework extended by two novel constructs (mechanics transparency coefficient; Bloom-level prerequisite dependency).

From a journal-fit perspective, the paper's ambition is well-matched to a Q2 venue and plausibly Q1 with revision. The RCT design, ITT sensitivity analyses, mediation finding (SE fully mediates ENG→ADAPTS; β_indirect=1.10), and Fisher z coupling result (r=.877 vs. .532) are the study's strongest empirical assets. The theoretical framing of the LM-GM extension is genuinely interesting and identifies a gap (mechanics transparency) that the DGBL design literature has not systematically addressed.

However, the paper's two most prominent claims — the novice disadvantage (d=−1.88) and the "deployable" ROC screening threshold (AUC=0.985) — rest on a cluster analysis that was not pre-registered and whose most critical stratum contains only n=4 game-arm novice completers. These claims are presented with a confidence that outstrips the evidence, and this asymmetry between rhetorical weight and evidential foundation is the paper's central problem for publication.

I recommend Major Revision. The paper is worth developing: the combination of pre-registered RCT design, multi-layered analysis, and honest limitation reporting is commendable and relatively rare in the DGBL literature. But the revision must clearly reframe the expertise-conditional findings as exploratory, recalibrate the ROC threshold claim, and provide a cleaner separation between confirmatory and exploratory analyses throughout.

---

## Strengths

### S1: Pre-Registered RCT in a Literature Dominated by Quasi-Experimental Designs
The paper uses a pre-registered randomised controlled trial with alternating blocked allocation (§4.2), pre-test and post-test measurement, ANCOVA as the primary analysis, and two ITT sensitivity analyses (no-gain imputation, worst-case bounding). This design places it in a small minority of GBL studies that provide causal leverage. The explicit power analysis and retrospective power table (Table 6.1) reporting inadequate power for primary outcomes is a model of transparency that many published studies fail to provide.

### S2: Multi-Layered Analysis Revealing Internal Mechanism
The study does not stop at the aggregate comparison. The mediation analysis (SE fully mediates ENG→ADAPTS; indirect effect=1.10, 95% CI [.43, 2.24]) and the Fisher z moderation test (SE–ADAPTS coupling r=.877 vs. .532, p=.004) provide evidence that the game restructured the psychological architecture of learning among completers — even when aggregate means were comparable. This is a qualitatively different kind of finding from simple outcome comparison and represents genuine added value.

### S3: Theoretically Grounded Framework Extension
The conceptualisation of the LM-GM framework's implicit mechanics transparency assumption, formalised as the mechanics transparency coefficient, is an intellectually coherent theoretical contribution (§7, lxx–lxxi). The argument that alignment at the design level is necessary but not sufficient — because transparency is expertise-dependent and cannot be verified at the design stage — is clear, testable in principle, and builds naturally from the empirical pattern. The Bloom-level prerequisite dependency argument is similarly well-grounded in Arnab et al.'s (2015) own Figure 3 mapping.

### S4: Transparent and Thorough Limitation Reporting
The eight-limitation section (§6.8) is unusually comprehensive and self-critical: differential attrition, MAR assumption limits, unregistered cluster analysis, germane CL subscale reliability (α=.31), all-self-report design, measurement timing structural disadvantage for game conditions, and format–measurement alignment are all explicitly named. This level of transparency materially strengthens the paper's credibility and is appropriate for the type of exploratory-confirmatory mixed-evidence paper this is.

### S5: Practical Deployment Contribution with Operational Specificity
The recommendation to route learners by pre-ADAPTS score, with a specific ROC-identified threshold (≤46.7%) and AUC=0.985, gives practitioners an operationally concrete starting point rather than the generic "match instruction to learner level" advice common in GBL literature. The behavioral log supplementary signal (≤5-minute early exits as cognitive friction indicator) adds further practical texture. Even if the threshold requires validation, the framework for operationalising expertise routing is a genuine practitioner contribution.

---

## Weaknesses

### W1: Evidential Weight of Central Positive Claim Does Not Match Rhetorical Confidence
**Problem**: The paper's most impactful empirical claim — that game-based training severely disadvantages novice learners (d=−1.88 on ADAPTS gain; §6.4) — derives from an unregistered k-means cluster analysis, with the "novice" cluster (C1) based on n=10 completers, of whom only n=4 were in the game arm (acknowledged in §6.8 survivor bias caveat). Throughout §6.4, §6.5, §7, and the Conclusion, this finding is presented with the rhetorical confidence appropriate to a pre-registered primary outcome — the C1 game disadvantage appears in topic sentences, drives the "precision prescription" conclusion, and anchors the ROC deployment recommendation.

**Why it matters**: A finding from n=4 surviving novice game-arm completers is statistically fragile. The confidence interval around d=−1.88 in this stratum is presumably very wide (not reported). Survivor bias — acknowledged but not quantified — means these 4 completers are plausibly the most motivated novices, and the true effect for deployed novices could be substantially larger in magnitude or, if less motivated novices had somehow persisted, different in direction.

**Suggestion**: The paper should restructure the presentation to clearly demarcate the pre-registered findings (ANCOVA primary outcomes, continuous moderation) from exploratory findings (cluster analysis, cluster-conditional effects, ROC threshold). A clear "Confirmatory Results / Exploratory Results" header structure in §5 and corresponding caveating in §6 would make the paper honest about its evidential hierarchy without sacrificing the interest of the exploratory story. The d=−1.88 finding should be accompanied by its confidence interval.

**Severity**: Critical

### W2: ROC "Deployable Screening Threshold" Claim Is Over-Stated for N=10 Positives
**Problem**: §6.7 presents the pre-ADAPTS ≤46.7% threshold as a "deployable screening criterion" and a "concrete and measurable screening criterion" (p. lxii). This AUC=0.985 estimate is derived from a binary classification model distinguishing C1 (n=10) from C2+C3 (n=53) among completers. In receiver operating characteristic analysis, AUC estimates from binary classifiers with fewer than 30 positive cases are highly unstable: the 95% CI on AUC=0.985 with n=10 positives will be very wide (roughly ±0.05–0.15 in practice), and the optimism from fitting and evaluating on the same small sample is considerable.

**Why it matters**: Practitioners reading this paper may implement a screening cutoff based on a threshold that has not been validated in an independent sample and whose apparent precision (≤46.7%, AUC=0.985) is an artefact of the small derivation set. This is the paper's most likely real-world harm if over-interpreted.

**Suggestion**: Add bootstrap or cross-validated confidence intervals for AUC. Change the language from "deployable" to "provisional" and "requires validation in an independent sample before deployment." A single-sentence acknowledgement in §6.7 that AUC estimates from n=10 positives are unstable would suffice to recalibrate the claim appropriately.

**Severity**: Critical

### W3: Sample Composition Limits the B2B Sales Training Generalisability Claim
**Problem**: §6.8 Limitation 8 notes that approximately 69% of participants work in the education sector, with the remainder distributed across industries "predominantly from Southeast Asia" in a voluntary online enrolment setting. The paper's framing — including the title, the abstract, and the practical recommendations in §6.7 — speaks to "B2B sales training" as a professional domain. A sample that is predominantly educators voluntarily enrolling in a sales simulation is substantially different from the typical corporate B2B sales training population (professional salespeople in revenue-generating roles, often mandated participation).

**Why it matters**: The ADAPTS-SV scores, the expertise distribution (C1 novice profile), the attrition pattern, and possibly the SE baseline all reflect a population whose characteristics may differ systematically from the intended deployment population. The expertise-routing recommendation based on this distribution may not transfer.

**Suggestion**: Reframe the practical recommendations as contingent on sample characteristics similar to this study's. Add a brief discussion of how the sample's predominantly education-sector profile might affect the expertise distribution observed, and note that the novice stratum's characteristics (low prior sales schema) may or may not be representative of novice populations in, for example, a commercial sales onboarding context.

**Severity**: Major

### W4: Theoretical Constructs Introduced Without Measurement Operationalisation
**Problem**: The mechanics transparency coefficient (MTC) and Bloom-level prerequisite dependency (BPD) are introduced in §7 as theoretical contributions to the LM-GM framework extension. While the conceptual argument is clear and compelling, neither construct is operationalised with measurement criteria. How would a designer calculate or estimate the MTC of a given game interface? What empirical indicators distinguish a "high BPD" from a "low BPD" design? Without operationalisation, these remain useful metaphors but cannot function as scientific constructs.

**Why it matters**: A theoretical extension that cannot guide measurement is of limited use to the field. Future researchers would not be able to test the MTC hypothesis without first solving the operationalisation problem the present paper leaves open.

**Suggestion**: Add a brief sub-section in §7 (or §6.5) offering candidate operationalisation strategies — for example, MTC could be estimated via think-aloud protocols during mechanic onboarding, time-to-first-successful-mechanic-use, or NASA-TLX administered after a brief mechanic onboarding module only. BPD could be estimated via sequential task analysis. Even a paragraph outlining candidate approaches would substantially strengthen the theoretical contribution.

**Severity**: Major

---

## Detailed Comments

### Title & Abstract
The title is strong and directly poses the research question. The abstract accurately represents the study design and findings, including the aggregate null and the expertise-conditional pattern. One concern: the abstract's phrase "a deployable screening criterion" (for the ROC threshold) appears without caveat. Given n=10 in the C1 class, this claim should be softened to "a provisional screening criterion requiring external validation."

### Introduction
The introduction clearly motivates the study and establishes the gap (GBL effectiveness for professional training, prior knowledge as moderator). The transition from research gap to research questions is logical. The research questions are clearly stated and appropriate.

### Literature Review / Theoretical Framework
Comprehensive for a thesis. The multi-theory integration (CLT + SE theory + engagement + LM-GM) is handled coherently. The LM-GM framework discussion is particularly well-grounded. One gap: the paper does not engage with Wouters et al.'s (2013) meta-analysis finding that serious game advantages are larger for retention (d=0.36) than immediate learning (d=0.29) until §6.8 — this temporal asymmetry argument should be foregrounded in the literature review, as it contextualises the immediate post-test design limitation from the outset.

### Methodology / Research Design
The design description is thorough. The pre-registration statement in §4.1 is appropriate. The description of the game (§4.2) is adequate at a structural level (card mechanics, two-phase structure, token economy, branching scenarios) but would benefit from a figure or table mapping each mechanic to its intended learning function per the LM-GM framework — this would make the alignment claim concrete and verifiable for readers. The control condition description is thinner than the game description; §4.2 should clarify more explicitly what "digital module with non-linear navigation" means in terms of content density and interactivity level.

### Results / Findings
Results are clearly presented. CONSORT flow diagram is appropriate. Tables are well-formatted. The CL decomposition results (CL2+CL3 d=0.90 vs. CL1 d=0.13) are interesting but the germane subscale α=.31 should be flagged in the Results section itself, not only in §6.8 — readers may otherwise over-interpret the decomposition.

### Discussion
The discussion is the paper's strongest section. The interpretations in §6.2–6.5 are careful and theoretically grounded. §6.6 (Non-Completers) is an important addition to the literature and is well-argued. §6.8 (Limitations) is exemplary in its candour.

### Conclusion
The three-part conclusion structure (Theoretically / Practically / Methodologically) is well-executed and provides a clean payoff for the theoretical framework. The "CL as currency" metaphor is memorable and appropriate. The closing sentence answers the central question directly. Minor concern: the Conclusion repeats several passages from §6 near-verbatim, which can be tightened.

### References
50 references is appropriate for a thesis. All major touchstones are present. No obvious missing citations in the GBL core literature, though see Reviewer 2 for possible domain omissions. The bibliography format appears consistent.

---

## Questions for Authors

1. The continuous moderation analysis (pre-ADAPTS × condition interaction, F(1,59)=11.65, p=.0012) is pre-registered and should be the primary evidence for the expertise-conditional hypothesis. How does the effect size and directionality of this interaction compare to the cluster-based finding? Does the continuous moderation analysis alone — without the cluster analysis — tell the same story about novice disadvantage?

2. The paper claims the format–measurement alignment concern (Limitation 6, §6.8) "cannot be ruled out from the present data." Have the authors considered supplementary analyses — for example, examining whether ADAPTS gain correlates with time-on-task in the control condition more than in the game condition, as one would expect if format matching were driving the effect? Even a null supplementary analysis would be informative.

3. The game description (§4.2) mentions card mechanics, token economy, and scenario-based phase 2, but does not provide the specific content taught or a mapping of mechanics to learning objectives. Would the authors be willing to add a supplementary LM-GM alignment table mapping each game mechanic to its intended LM counterpart and Bloom level?

---

## Minor Issues

### Language / Grammar
- p. lxii: "concrete and measurable screening criterion" — "deployable" implies external validity that the data do not yet support; suggest "provisional" or "candidate."
- p. lv: "disproportionately in phase 2" — clarify that this refers to the game's phase 2, not a study phase, to avoid ambiguity.

### Figures and Tables
- Table 6.1 is clear and appropriate. Consider adding the 95% CI on AUC for the ROC finding alongside the AUC value wherever it appears in the text.
- A LM-GM alignment table (game mechanics → learning mechanics → Bloom level) would strengthen §4.2 substantially.

---

## Dimension Scores

| Dimension | Score (0–100) | Descriptor | Notes |
|---|---|---|---|
| Originality (20%) | 72 | Strong | LM-GM extension with MTC and BPD is genuinely novel; expertise routing recommendation adds practical originality |
| Methodological Rigor (25%) | 65 | Adequate | Pre-registered RCT and ITT analyses are strong; cluster analysis centrality and n=10 ROC threshold reduce rigor score |
| Evidence Sufficiency (25%) | 60 | Adequate | Mediation and Fisher z findings are well-supported; cluster-conditional effects and ROC claim rest on thin strata |
| Argument Coherence (15%) | 78 | Strong | Argumentation is largely fluent; the confirmatory/exploratory hierarchy is muddled in §6.4 and §7 |
| Writing Quality (15%) | 82 | Strong | Prose is clear, precise, and appropriately academic throughout |
| Literature Integration (optional) | 74 | Strong | Core GBL literature well-covered; see Reviewer 2 for possible gaps |
| Significance & Impact (optional) | 76 | Strong | Design implications are concrete and the expertise-routing framework is practically useful if validated |
| **Weighted Average** | **69** | **Major Revision** | Solid foundation; requires structural recalibration of exploratory vs. confirmatory claims |
