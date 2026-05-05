# Devil's Advocate Review Report

## Manuscript Information
- **Title**: For Whom Does Game-Based Learning Training Work? An RCT of a Scaffolded Digital Simulation for B2B Sales Training
- **Manuscript ID**: GBL-Thesis-2026
- **Review Date**: 2026-04-30
- **Review Round**: Round 1

---

## Reviewer Role
Devil's Advocate — Core Argument Challenger

---

## ⚔️ Strongest Counter-Argument (200–300 words)

The paper's positive story — that GBL works for experienced learners, fails novices, and that this expertise-conditional pattern reveals how to deploy GBL responsibly — is intellectually compelling. It is also, possibly, a post-hoc rationalisation of a null finding.

Here is the alternative reading: the study ran a pre-registered RCT and found no significant effect on either primary outcome. The ANCOVA results for self-efficacy trend toward favouring *the control* (p=.064, marginal in the wrong direction from H1). ADAPTS is null. Cognitive load is significantly higher in the game (the wrong direction from design intent). By the pre-registered analysis plan, this is a null study with one adverse finding (CL elevation). 

The post-registration exploratory analysis found, in an unregistered k-means cluster analysis, that a 10-person novice cluster appears to be severely harmed by the game. This is reported as d=−1.88 — one of the largest effect sizes in the manuscript. But this effect rests on n=4 surviving game-arm novice completers, drawn from a pool of participants who experienced 41.8% attrition in the game arm specifically. The 4 survivors are almost certainly the most motivated, most persistent novice participants. The "true" effect for deployed novices — who would include the 6 game-arm novices who dropped out — is likely more negative, and the paper acknowledges this. But it then proceeds as if d=−1.88 tells us something precise and actionable, when it may tell us mainly that 4 motivated novices still found the game hard to complete.

The question the paper does not answer is: what is the probability that this pattern — a near-null aggregate, a massive post-hoc novice disadvantage, a clean expertise gradient — would occur by chance across an unregistered clustering analysis applied to n=63 cases with two features? That probability is not zero.

---

## Issue List

### CRITICAL Issues

**CRITICAL-1: The ROC "Deployable Screening Threshold" Is a Circularity Dressed as Precision**

**Category**: Circular Reasoning / Overgeneralization
**Location**: §5.7, §6.7, Conclusion (p. lxii, lxxii)

The ROC analysis classifies completers into C1 vs. C2+C3 using pre-ADAPTS scores. The clusters themselves were defined using pre-ADAPTS scores (as one of two clustering features). Therefore the ROC analysis is predicting cluster membership from a feature that was used to define the clusters. AUC=0.985 with sensitivity=1.000 in this context is almost guaranteed by construction: a k-means cluster defined partly by pre-ADAPTS will be nearly perfectly separable by pre-ADAPTS scores, because pre-ADAPTS variability is what created the cluster boundary in the first place. This is not a finding about the predictive validity of pre-ADAPTS for novice identification — it is a confirmation that the clustering algorithm did its job.

To make an honest case for the ROC threshold, the authors would need to predict C1 membership in a held-out sample that was clustered independently, or — better — use an externally defined criterion for "novice" (e.g., less than 1 year of sales experience) and show that pre-ADAPTS ≤46.7% predicts that criterion with AUC=0.985. As reported, the AUC tells us nothing about the threshold's validity for screening real-world novices.

**Implication**: The "deployable screening criterion" claim should be removed or fundamentally reframed as a hypothesis for future validation. The current framing constitutes a scientific overclaim.

---

**CRITICAL-2: Survivor Bias Is Not Quantified — and Quantification Is Possible**

**Category**: Incomplete Analysis
**Location**: §5.6, §6.4, §6.8 Limitation (p. lviii–lix, lxiii)

The paper acknowledges (§6.8) that "game-arm novices who completed the study (n=4) may be the most persistent subset of novice participants, meaning the true game disadvantage for novices could be larger than observed." This caveat is correct — but the analysis stops there, when it should not. 

The study has behavioral log data on all 80 participants who enrolled and initiated the game or control condition. Non-completers' time-to-exit data is available (used in §5.3 for the dropout timing analysis, 5-minute threshold discussion). Among game-arm participants who exited before completion, a substantial proportion exited in phase 1 (within 5 minutes), which the paper classifies as "cognitive friction." For game-arm novices who exited, what was their exit timing distribution? This data appears to be available and would allow at least a descriptive characterisation of whether the non-completing novices were uniform early exiters (cognitive friction) or distributed across the full game duration (time intolerance). This matters because the d=−1.88 estimate for C1 is drawn from the post-dropout sample and is therefore conditional on survival — and the degree to which survival is expertise-dependent determines whether the true novice disadvantage is larger or smaller than observed.

**Implication**: The authors should use available behavioral log data to characterise the exit patterns of non-completing game-arm participants by cluster-predicted membership (using the pre-ADAPTS ≤46.7% threshold as a proxy for C1 membership among non-completers). This analysis would at minimum provide a lower bound on the magnitude of survivor bias and would substantially strengthen the paper's honest treatment of the attrition problem.

---

### MAJOR Issues

**MAJOR-1: The Mechanics Transparency Coefficient Is Currently a Metaphor, Not a Construct**

**Category**: Theoretical Overreach / Operationalisation Gap
**Location**: §7 Conclusion (p. lxx–lxxi)

The mechanics transparency coefficient (MTC) is presented as a theoretical contribution to the LM-GM framework. The concept is defined as "the working memory overhead required to operate a game interface, independent of domain content." This is a clear and useful conceptual definition. However, nowhere in the paper is a measurement procedure specified for the MTC. How would a designer estimate it? What units does it carry? What observable behaviour or performance indicator operationalises "working memory overhead for mechanic operation independent of domain content"? Without a measurement procedure or at least candidate operationalisation criteria, the MTC is a useful metaphor for why game mechanics can interfere with learning for novices — not a theoretical construct that can generate testable hypotheses or be applied by practitioners.

This is not a trivial gap. The Bloom-level prerequisite dependency concept has the same problem. Both are post-hoc narrative labels attached to the observed data pattern. The data pattern is real; the labels are apt. But the labels are not yet constructs, and the paper should not claim they are.

**Implication**: Designate MTC and BPD as "conceptual proposals" in the Conclusion rather than "theoretical contributions to the LM-GM framework." The latter designation implies operationalisation and testability that the current paper does not provide.

---

**MAJOR-2: The Alternative Explanation for the Aggregate Null Is Underweighted**

**Category**: Confirmation Bias Detection
**Location**: §6.8 Limitation 6 (p. lxiv)

The format–measurement alignment concern is the strongest alternative explanation for the aggregate ADAPTS null, and it is listed as the sixth of eight limitations in a brief paragraph. The argument is: the control condition delivers content in propositional text slides; ADAPTS-SV measures beliefs through propositional declarative statements; these share a surface format. Any effect of format familiarity — independent of genuine adaptive selling belief change — would advantage the control group on ADAPTS-SV.

If this alternative explanation accounts for even a moderate fraction of the ADAPTS gap (real or absent), then the aggregate null finding's interpretation as "the game failed to improve adaptive selling beliefs" is threatened, and the expertise-conditional story built on top of it (which depends on C1 game-arm ADAPTS being particularly poor) is equally threatened.

The paper states "this alternative explanation cannot be ruled out from the present data." This is correct — and more serious than its placement as Limitation 6 implies. The paper should discuss whether the within-game mediation evidence (SE→ADAPTS inside the game group) partially addresses this — if format matching were the entire story, the SE-mediated pathway within the game group would not be expected. But this counter-argument is not made.

---

**MAJOR-3: The Pre-Registered Continuous Moderation Is the Falsifiable Test of Expertise Effects, Not the Cluster Analysis — The Paper Should Lead With It**

**Category**: Cherry-Picking / Confirmatory-Exploratory Inversion
**Location**: §5.6, §5.7, §6.4

The continuous moderation analysis (pre-ADAPTS × condition interaction F(1,59)=11.65, p=.0012; simple slopes: Low-1SD: −15.17pp, Mean: −4.83pp, High+1SD: +5.51pp) is pre-registered and shows that ADAPTS outcomes are moderated by pre-ADAPTS in the expected direction with a statistically robust effect. This is the paper's strongest and most defensible evidence for the expertise-conditional hypothesis. It is presented in §5.7 after the cluster analysis in §5.6, and is discussed as corroborating the cluster pattern rather than as the primary evidence.

The rhetorical effect of this ordering is that readers attribute the expertise-conditional story primarily to the cluster analysis (with its dramatic d=−1.88 for n=4 completers) rather than to the pre-registered moderation (with its robust F(1,59) and coherent simple slopes). This is a presentation choice that amplifies the more fragile finding and de-emphasises the more robust one. Whether intentional or not, it functions as a form of selective emphasis.

**Implication**: Swap the order of §5.6 and §5.7. Lead with the pre-registered moderation as primary evidence for expertise effects; present the cluster analysis as an exploratory illustration of what the moderation looks like in practice when learners are partitioned into profiles.

---

### MINOR Issues

**MINOR-1: The Germane CL Finding Is Used Without Its Reliability Caveat In the Mechanism Story**
The paper's "extraneous vs. germane load" dissociation (CL2+CL3 d=0.90 vs. CL1 d=0.13) is central to the mechanistic interpretation in §6.2 and the "CL as currency" metaphor in §7. The germane subscale α=.31 means the CL1 measure is dominated by error variance. The extraneous/germane framing of the result is presented throughout the Discussion as established fact when it is in fact an interpretation unsupported by the measurement quality. At minimum, each invocation of "extraneous vs. germane" load in §6.2 and §7 should be accompanied by a parenthetical reliability note.

**MINOR-2: Gaming Experience As An Alternative Moderator Is Dismissed Too Quickly**
The paper acknowledges (§6.8, Limitation) that gaming experience was not measured. The expertise reversal literature that is cited (Hernández & Moreno, 2019) characterises the moderator as gaming experience, not domain expertise. The present study's moderator is domain expertise (operationalised as pre-ADAPTS and pre-SE). The paper argues these are "structurally parallel." But for the novice cluster (C1), it is equally plausible that low game fluency (inability to quickly decode card mechanics, token economy, phase transitions) — not low domain knowledge — produced the cognitive overload. Without a gaming experience measure, this alternative cannot be ruled out, and the entire Bloom-level prerequisite dependency story (which attributes the novice disadvantage to domain schema insufficiency) could be wrong.

**MINOR-3: The "So What?" Test for the Methodology Contribution**
The paper's methodological contribution — "pre-intervention-only clustering provides a template for identifying moderation-relevant subgroups without circularity; ITT sensitivity analyses bound attrition bias; measurement-timing critique applies broadly to GBL evaluation" — is genuinely useful for the field. However, the cluster analysis, as noted, is at risk from the ROC circularity issue (CRITICAL-1) which partially undermines the "without circularity" claim. The authors should clarify that the circularity protection applies to the cluster derivation step (using pre-intervention features only to define clusters) but that the ROC analysis subsequently reintroduces a form of circularity in its AUC estimation.

---

## Ignored Alternative Explanations / Paths

1. **The aggregate null finding is the correct answer.** The pre-registered RCT found no effect on either primary outcome. The expertise-conditional story is one of multiple possible post-hoc explanations for a null; others include: (a) the game genuinely does not work for any learner in this domain, (b) the format–measurement alignment explained whatever advantage the control showed, (c) the 4-week-only training duration is too short for any format to produce detectable adaptive selling belief change. The paper should engage more explicitly with the possibility that the null is real and the expertise moderation is a false positive from the cluster analysis.

2. **The SE partial support (ITT-A p=.035) favours the control, not the game.** This is mentioned briefly but not prominently discussed: under ITT-A imputation, the control group outperforms the game on SE. If this effect were real, it would mean that even among the full allocated sample, the game had a negative average effect on self-efficacy. The paper treats ITT-A as "directionally consistent with per-protocol" without fully interrogating what it would mean if ITT-A is a better estimate than the per-protocol.

3. **Attrition differential may itself be the finding.** A training format that loses 41.8% of assigned participants before analysis, and selectively loses novices and Phase-2 participants, may have failed at the fundamental task of training delivery — not merely failed to outperform the control on belief measures. The paper touches on this but could position it more centrally.

---

## Missing Stakeholder Perspectives

1. **Non-completers' experience** is entirely absent from the data. The paper uses behavioral log timing to infer reasons for dropout, but no direct data on non-completers' experience is available. Any conclusions about why novices dropped out are inferential, not empirical.

2. **Organisational administrators** of sales training — who decide whether to deploy a training format and who absorb the cost of attrition — would view this study's results very differently from the learner-centered perspective the paper adopts. The implicit stakeholder throughout is the individual learner; the deployment recommendation needs to account for the organisational stakeholder who manages training pipelines and cannot easily implement a two-track expertise-routing system without significant infrastructure.

3. **The game developers** are absent from the discussion. Whether the game was evaluated for design fidelity (did it implement the LM-GM alignment as intended?) or whether the "mechanics transparency" problem identified post-hoc was detectable to the developers at design time is not addressed.

---

## Observations (Non-Defects — Do Not Conflate With Defects)

1. The mediation finding (SE fully mediates ENG→ADAPTS; β_indirect=1.10, CI excludes 0) is the paper's most robust positive finding and does not depend on the cluster analysis. It is a within-game-group correlational finding, and its completer-only scope is appropriately noted. This finding would stand independently of the cluster-analysis issues.

2. The Fisher z coupling difference (r=.877 vs. .532, p=.004) is a genuine statistical finding with an appropriate test. The interpretation that the game "restructured the psychological architecture of learning" is a large claim, but the test itself is sound and the magnitude is meaningful.

3. The honest reporting of inadequate statistical power (Table 6.1) is exemplary and rare. The paper does not pretend its null findings are conclusive evidence of ineffectiveness; it correctly presents them as underpowered estimates. This is scientifically honest.

4. The eight-limitation §6.8 section is comprehensive and intellectually courageous. Papers that identify their own format–measurement alignment concern, survivor bias, and CL reliability problem in the Limitations section are more trustworthy than those that do not, even when those concerns are serious.

---

## Devil's Advocate Verdict

The paper is a net contribution to the GBL literature — the pre-registered RCT design, the honest null reporting, the within-game mediation finding, and the LM-GM framework critique are genuine advances. However, the paper's current framing inverts its evidential hierarchy: the most robust finding (pre-registered continuous moderation) is subordinated to the most fragile finding (cluster-based d=−1.88 from n=4 completers), and a circular AUC estimate is presented as a "deployable screening criterion." The theoretical extension (MTC, BPD) is conceptually valuable but not yet operationalised as a construct.

**The paper needs to be honest about what it is: a pre-registered RCT that found no primary-outcome effect, followed by exploratory analyses that generated expertise-conditional hypotheses consistent with the pre-registered moderation. In that framing, it is publishable and important. In its current framing — a GBL study that discovered that expertise routing is the solution — it is overclaiming.**
