# Judgment QC

Quality control for judgment failures that conventional QC cannot detect. Conventional QC (format, structure, traceability, bullet length, em dash) catches rule violations. It does not catch output that complies with every rule but misrepresents, miscalibrates, or inflates the underlying experience.

This file defines the judgment failure modes that must be checked at specific phases of role_evaluation, cv_targeted, and cv_general. Each mode is structured as Pattern, Check, Evidence required, and Flag trigger. Apply the same evidence-citation discipline used in `rules/cv/qc_checklist.md`: cite specific bullets, gap rows, architecture lines, or inventory entries. General confirmations are not acceptable. Any Fail invokes QC Failure Recovery per Global Rules.

---

## Application Points

- **Content-level checks (Modes 1-6):** applied in `cv_targeted` Phase 2b and `cv_general` post-content-generation QC, after content has been generated and before document assembly.
- **Evaluation-level check (Mode 7):** applied in `role_evaluation` Phase 3b, after gap analysis is drafted.
- **Architecture-level check (Mode 8):** applied in `cv_targeted` Phase 2a Step 4 and `cv_general` equivalent, before the experience architecture is approved by the user.

The loading skill is responsible for invoking this file at the correct phase and applying only the sections relevant to that phase.

---

## Content-Level Checks

Applied to generated CV content. For each bullet in the generated content, run every mode in this section.

### Mode 1 — Scope misrepresentation

- **Pattern:** Bullet implies larger scope than the source supports. Scope includes geographic reach (global, regional, enterprise), organizational scale (team size, portfolio size, budget), timeframe span, and stakeholder breadth. Rounding up, extrapolating from context, or generalizing a specific effort to an implied broader mandate all fall here.
- **Check:** For each bullet containing scope language, locate the source inventory entry. Confirm the scope claim is explicitly supported by source language.
- **Evidence required:** Cite the specific bullet and the specific inventory entry. Quote or paraphrase the source language that supports the scope claim.
- **Flag trigger:** Any scope claim not directly supported by explicit source language is a Fail. Inference is not acceptable; if the source says "a program in the US division" the bullet cannot say "a global program."

### Mode 2 — Framing mismatch

- **Pattern:** Achievement framed as transformation or strategy when the underlying source describes optimization, execution, or incremental improvement. Or the reverse: optimization framing applied to genuinely transformational work, weakening the archetype message.
- **Check:** For each generated bullet, identify the framing verb and stance (transformed, rebuilt, redesigned, led strategy vs. optimized, delivered, executed, improved). Locate the source inventory entry. Confirm the source entry supports the framing applied.
- **Evidence required:** Cite the specific bullet and the specific inventory entry. State why the source supports or does not support the framing.
- **Flag trigger:** Any bullet whose framing is not supported by its source entry. A bullet derived from multiple entries via inference must state the inference explicitly; unstated inference is a Fail.

### Mode 3 — Archetype drift

- **Pattern:** A bullet reads cleanly on its own but characterizes the work through a lens that fits a different archetype than the active primary. Examples: active primary is Process & Operations but the bullet's stance reads Transformation & Strategy; active primary is Data & Analytics but the bullet reads Platform & Technology.
- **Check:** For each bullet, state which archetype its framing most naturally fits based on its verbs, stance, and signals. Compare against the active primary archetype.
- **Evidence required:** Cite the bullet, the specific signal words or stance that identify its archetype framing, and the active primary archetype for comparison.
- **Flag trigger:** Any bullet whose framing is stronger for a non-primary archetype than for the primary archetype is a Fail, unless a dual-archetype is active AND the bullet is one of the 2-3 sanctioned secondary-framed achievements per `rules/cv/dual_archetype.md`.

### Mode 4 — Outcome inflation

- **Pattern:** Qualitative outcomes stated as quantitative when no number exists in source. Speculative, planned, or in-flight outcomes stated as delivered. Contributions to an outcome stated as ownership of that outcome. Estimated figures presented without qualification.
- **Check:** For each bullet containing a numeric claim, a delivery claim, or an outcome ownership claim, locate the source entry. Confirm the claim is explicitly stated in the source.
- **Evidence required:** Cite the bullet and the specific source entry language that supports the number, the delivery, or the ownership.
- **Flag trigger:** Any numeric figure, delivery claim, or outcome ownership not explicitly stated in a source entry is a Fail. Approximating from context is a Fail. If the outcome was partial, contributed, or estimated, the bullet must reflect that qualification.

### Mode 5 — Temporal ambiguity

- **Pattern:** Bullet implies sustained capability, recurring outcome, or ongoing practice when the source describes a single event, short-duration pilot, or one-time effort. Verb tense and aspect carry this: "established a practice of X" vs. "ran one instance of X"; "ongoing governance of Y" vs. "one-time Y review."
- **Check:** For each bullet describing a practice, capability, program, or recurring outcome, confirm the source describes durability beyond a single instance.
- **Evidence required:** Cite the specific bullet and the specific source entry. State the source evidence of duration, recurrence, or institutional persistence.
- **Flag trigger:** Any bullet that implies sustained or recurring activity when source supports only a single instance or short-duration effort is a Fail. If duration is ambiguous in the source, the bullet must match source specificity rather than imply durability.

### Mode 6 — Attribution inflation

- **Pattern:** Individual contribution framed as organizational leadership ("led" when source says "contributed to"). Team output framed as personal delivery ("delivered X" when source describes a collaborative or subordinate-led effort). Advisory or influence work framed as direct ownership.
- **Check:** For each bullet using leadership or ownership verbs (led, directed, owned, drove, delivered, managed), locate the source entry. Confirm the attribution claim matches the user's actual role in the described work.
- **Evidence required:** Cite the bullet's attribution verb and the source language describing the user's role in the work.
- **Flag trigger:** Any bullet whose attribution is stronger than the source supports is a Fail. "Led" when the user was a contributor is a Fail. "Owned" when the user advised is a Fail. Collaborative work framed without acknowledging the collaborative context, when that context is material to the claim, is a Fail.

---

## Evaluation-Level Check

Applied to the gap analysis produced by role_evaluation. Run this mode against every gap row in the gap table.

### Mode 7 — Gap rating miscalibration

- **Pattern:** A gap in the gap table is rated Medium or Low when evidence supports High, or rated High when supporting evidence would lower the severity. The rating appears defensible because the surrounding language is polished, but the severity reflects preferred positioning rather than the actual distance between the job requirement and the user's evidenced experience.
- **Check:** For each gap row, re-read the specific job description language describing the requirement and re-read the specific inventory entries cited as supporting evidence. Independently assess severity based on match distance: exact match, near match (direct analog), partial match (adjacent but incomplete), or no match.
- **Evidence required:** Cite the gap row, the job description language that defines the requirement, the supporting inventory entries (if any), the assessed match distance, and the rationale. State the severity that the evidence supports.
- **Flag trigger:** Any gap whose rating does not match the severity the evidence independently supports is a Fail. Optimistic ratings (downgrading a real High to Medium to preserve fit) and pessimistic ratings (upgrading Medium to High to appear candid) are both Fails.

---

## Architecture-Level Check

Applied to the proposed experience architecture before user approval and before content generation.

### Mode 8 — Experience architecture miscalibration

- **Pattern:** The proposed experience architecture includes, excludes, or summarizes roles in a way not supported by the governing rules. Examples: omitting a role that adds credibility to a Phase 1a critical requirement; giving full treatment to a role that does not support any critical requirement; summarizing a role in a way that suppresses relevant credibility; retaining a role that is outside the 10-year continuity window and does not add critical-requirement credibility.
- **Check:** For each role in the proposed architecture, cross-reference the proposed treatment (full entry, one-line main, one-line Earlier Professional Roles, omit) against two rules: (a) whether the role falls inside the 10-year continuity window, and (b) whether the role adds credibility to any Phase 1a critical requirement.
- **Evidence required:** For each role, cite the role, the proposed treatment, the role's age relative to the 10-year window, and the specific Phase 1a critical requirement(s) it does or does not support. State whether the treatment matches the governing rules.
- **Flag trigger:** Any role whose proposed treatment conflicts with the continuity-plus-credibility rules is a Fail. Any role added, omitted, or summarized without rationale tied to Phase 1a critical requirements is a Fail. A role may be retained outside the 10-year window only when it carries credibility for a critical requirement; this must be stated explicitly in the rationale.
