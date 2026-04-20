# Role Evaluation Skill

## Objective

Evaluate a target role against established experience and positioning to determine whether to proceed with an application. Produces a structured fit assessment and GapAnalysis file used as input by `cv_targeted` and `interview_prep`.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 2c, 3a, 3b, 3c, 4

**Session Continuity**

A session log persists work across sessions.  The log is created at Phase 1a close, appended at every subsequent action phase close only, and deleted at Phase 4 close. If a session ends mid-phase, resume from the start of that phase.

Before Phase 1a, check `personal/sessions/` for files matching `*_SessionLog.md`. If any exist, list them and ask whether this is a new evaluation or resuming a previous evaluation. If resuming, load the log, state the last completed phase, confirm the resume point, and skip to the start of the next incomplete phase. If starting new, proceed to Phase 1a.

File Naming: `[Company]_[Role]_[YYYY-MM]_SessionLog.md`

---

## Phase 1a — Session Setup

*(No documents are loaded in this phase)*

1. Confirm the job description has been provided. If not, request it and do not proceed until user provides it.

2. Confirm company and role title from the JD or user. Obtain agreement.

3. Propose the role level (IC, AD, Dir, Sr. Dir, VP); if not explicit in the title, infer from required experience, scope, and reporting structure. State rationale and obtain agreement. Level governs seniority of voice, scope framing, and achievement selection throughout.

4. Create `personal/sessions/[Company]_[Role]_[YYYY-MM]_SessionLog.md` with company, role, level, session start date, and JD availability note. Confirm creation.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Role Classification and Context

*(Only after Phase 1a has been explicitly approved)*

1. Load the active domain: read `**Active Domain:**` from the header of `personal/knowledge/Experience_Inventory.md` (do not assume); load `rules/domains/<active_domain>.md` and confirm it loaded.

2. Check the JD against the domain file's Section 3 Pack Selection Criteria. If a "Do NOT use when" condition applies, flag the scope mismatch and obtain user direction: halt for a different domain, or continue as an explicit cross-domain evaluation with acknowledged mismatch.

3. Research the company, industry, and role via web search to an expert-level understanding: company stage, culture, competitive landscape, organizational context, and what success looks like. Record each source (URL or publication and date). Use authoritative sources only (company/IR/regulatory filings, peer-reviewed or analyst publications, recognized trade press); do not cite Wikipedia, crowd-sourced wikis, forums, or unattributed blogs.

4. Identify the 4-5 most critical requirements or themes in the job description.

5. Read `rules/registry_archetype.md`. Identify the role archetype and state the framing angle. If no archetype satisfies the match criteria, halt: state which criteria failed, inform the user that `skills/archetype_creation.md` must be completed first, and do not advance. If the role spans two archetypes, identify primary and secondary with rationale, then load `rules/cv/dual_archetype.md` and apply its rules throughout. Obtain user agreement on archetype selection.

6. Load `rules/archetypes/Archetype_<N>_<Name>.md` (and the secondary file for dual-archetype). Confirm each loaded completely. The archetype file is authoritative on identity, match criteria, summary framing, tag priorities, achievement framing pattern, and de-emphasis. Domain vocabulary and calibration examples come from the domain file loaded in Step 1.

7. Read `rules/registry_org_type.md`. Select the org type, state rationale, obtain agreement. Note the framing emphasis for later content generation.

**Phase 2a Closing:** Follow Standard Phase Closing. Terse report to user: domain, archetype, org type, and count of critical requirements. Append to the session log: "Phase 2a Complete" with date, active domain, any scope-mismatch handling, sources consulted, critical requirements, archetype selection and rationale (plus dual-archetype detail if applicable), and org type with rationale. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Run QC internally against the checks below. Do not present passing checks to the user; only failures surface, per QC Failure Recovery.

- **Role Level:** explicit user agreement is documented for the level stated in Phase 1a Step 3.
- **Domain Scope:** active domain was read from the Inventory header, the domain file was loaded, and Section 3 was checked. If a scope mismatch was flagged, user direction is documented.
- **Company Research:** Step 3 sources are listed with enough detail to revisit.
- **Critical Requirements:** 4-5 items are present from Step 4; fewer than 4 fails.
- **Archetype Selection:** the primary archetype is defensible against the match criteria in the loaded archetype file. Each satisfied criterion maps to specific JD language.
- **Dual-Archetype (if applicable):** the secondary archetype is explicitly evidenced in the JD, not inferred from peripheral language. Primary/secondary assignment reflects the dimension the role primarily evaluates on. Weak or speculative secondary fails; recommend single-archetype treatment and obtain user agreement.
- **Org Type:** selection is consistent with the JD and the Step 3 research. The specific company characteristic that drove it is identifiable.
- **Standard QC Document Verification** per Global Rules.

**Phase 2b Closing:** Follow Standard Phase Closing. Terse report: QC pass; any failures and resolution. Append to the session log: "Phase 2b Complete" with date, QC outcome, and any flagged issues plus resolution. Next phase is Phase 2c.

---

## Phase 2c — Presentation of Phase 2

*(Only after Phase 2b has been explicitly approved)*

Items already agreed inline in Work (role level, archetype, org type) are not re-reviewed here. Presentation covers items not yet individually reviewed.

1. Present each critical requirement one at a time. State the requirement and the JD language it maps to. Obtain agreement or adjustment per requirement.

2. Present the list of research sources from Phase 2a Step 3. Confirm coverage is sufficient; ask whether additional research is needed.

**Phase 2c Closing:** Follow Standard Phase Closing. Append to the session log: "Phase 2c Complete" with date and any adjustments. Next phase is Phase 3a.

---

## Phase 3a — Fit Evaluation

*(Only after Phase 2c has been explicitly approved)*

1. Load `personal/knowledge/Experience_Inventory.md` and `personal/knowledge/Career_Narratives.md`. Confirm each loaded completely.

2. Map each critical requirement to the most relevant experience with the user, one at a time. For each: cite the source document and specific achievement, and obtain agreement. Every claim must be traceable.

3. Flag gaps, weak matches, and cases where language needs to shift to match the role's framing.

4. Work through each gap with the user, one at a time. For each: state the gap, search source documents for closing evidence, ask clarifying questions if needed, propose severity (High/Medium/Low) and resolution (CV language, interview narrative, needs user input, or insufficient evidence), and obtain agreement. Do not close gaps via creative framing without explicit approval.

5. Identify items to de-emphasize for this role. Present each one at a time with rationale; obtain per-item approval.

6. Compute the fit assessment and obtain user agreement on the rating and recommendation:
   - Overall fit rating with brief rationale
   - Application recommendation: **Proceed**, **Proceed as speculative application**, or **Do not pursue**

   Threshold (a role clears only if both conditions hold):
   - *Domain exclusion check*: the role does not require a primary domain outside established positioning. Exclusion gate only, not a positive fit signal.
   - *Candidacy viability*: at least 65% of critical requirements have a strong, source-citable match (2 of 3, 3 of 4, or 4 of 5). Weak or inferred matches do not count.

   *Strong match*: a specific, named achievement or deliverable traceable to a specific source document and entry. General capability claims do not qualify.

   Outcome mapping:
   - **Proceed**: both conditions clear.
   - **Proceed as speculative application**: domain exclusion passes but viability falls below threshold. User must explicitly acknowledge the risk before continuing.
   - **Do not pursue**: domain exclusion fails.

7. Verify every High-severity gap has a resolution (resolved, carried by interview narrative, or unresolved with explicit user acknowledgment). If any unresolved remain, obtain a decision before closing.

**Phase 3a Closing:** Follow Standard Phase Closing. Terse report: fit rating, recommendation, count of gaps by severity, count of de-emphasis items. Append to the session log: "Phase 3a Complete" with date, full requirement mapping, gap summary table, de-emphasis items and approval status, fit assessment, application recommendation, and High-severity gap resolutions. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

Run QC internally against the checks below. Do not present passing checks to the user; only failures surface, per QC Failure Recovery.

- **Requirement Mapping:** every critical requirement from Phase 2a has a source-citable match per the strong-match definition.
- **Gap Enumeration:** every gap from Step 3 appears in the Step 4 iteration.
- **Gap Rating Judgment:** load `rules/judgment_qc.md` and confirm it loaded completely. Apply Mode 7 (Gap rating miscalibration) from Evaluation-Level Check to every gap. Cite the gap, the JD language, the supporting inventory entries by `ID:`, the assessed match distance, and the severity the evidence supports. Any stated severity that does not match the evidence fails.
- **Gap Resolution Completeness:** every gap was worked through individually with a user response, and ends in one of: resolved via CV language, carried by interview narrative, or unresolved with explicit user acknowledgment.
- **High-Severity Gaps:** every High gap has an explicit resolution. Any unresolved High gap without a user decision fails.
- **De-Emphasis Approvals:** each Step 5 item has explicit user agreement.
- **Fit Threshold:** verify the count of critical requirements, the count with strong source-citable matches, and the 65% calculation. Confirm the domain exclusion check was performed and the recommendation matches the threshold result. If the outcome was Proceed as Speculative Application, confirm explicit user risk acknowledgment.
- **Standard QC Document Verification** per Global Rules.

**Phase 3b Closing:** Follow Standard Phase Closing. Terse report: QC pass; any failures and resolution. Append to the session log: "Phase 3b Complete" with date, QC outcome, and any flagged issues plus resolution. Next phase is Phase 3c.

---

## Phase 3c — Presentation of Phase 3

*(Only after Phase 3b has been explicitly approved)*

1. Present the Phase 3 compact recap one section at a time (each bullet below = one exchange):
   - Requirement mapping: each requirement with its matched source (one line each, no rationale)
   - Gaps: each gap with severity and resolution (one line each)
   - De-emphasis items (list only, no rationale)
   - Fit rating and application recommendation

2. Write the GapAnalysis file at `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md` containing:
   1. Role context: company, role title, role level, active domain (with domain file path `rules/domains/<active_domain>.md`), primary archetype (number, name, archetype file path `rules/archetypes/Archetype_<N>_<Name>.md`) and secondary if applicable, rationale for each archetype, org type, and org-type framing emphasis.
   2. Critical requirements from Phase 2a with the source-citable match for each.
   3. Full gap summary table with severity and resolution status per gap.
   4. Fit assessment summary from Phase 3a Step 6 including the threshold calculation and application recommendation.
   5. Sources section listing every research source from Phase 2a Step 3 with enough detail to revisit.

   If `personal/sessions/` does not exist, create it. Confirm the file was written. This file is the terminal output of this skill and is used as input by `cv_targeted` and `interview_prep`.

**Phase 3c Closing:** Follow Standard Phase Closing. Append to the session log: "Phase 3c Complete" with date and GapAnalysis file path.

Before presenting next steps, review the session for experience descriptions, framing decisions, gap resolutions, or positioning language not yet reflected in source documents. If capturable content was found, summarize briefly and recommend Phase 4. If the user confirms, proceed to Phase 4. If the user declines or no capturable content was found, proceed to application next steps.

**Application next steps:**
- If the recommendation is Proceed or Proceed as Speculative Application: inform the user that `cv_targeted` can be triggered with the GapAnalysis file as context, and that `interview_prep` can begin in parallel using the same file.
- If the recommendation is Do Not Pursue: ask whether to close the workflow.

---

## Phase 4 — Source Document Update

Dedicated to capturing information surfaced during this role evaluation that should be added to source documents.

Load `skills/source_document_update_workflow.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 3c.

At the close of Phase 4, delete the session log at `personal/sessions/[Company]_[Role]_[YYYY-MM]_SessionLog.md`. Confirm deletion.
