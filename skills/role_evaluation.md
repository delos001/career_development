# Role Evaluation Skill

## Objective

Evaluate a target role against established experience and positioning to determine whether to proceed with an application. Produces a structured fit assessment and GapAnalysis file used as input by `cv_targeted` and `interview_prep`.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b, 4

**Session Continuity**

A session log persists work across sessions.  The log is created at Phase 1a close, appended at every subsequent action phase close only, and deleted at Phase 4 close. If a session ends mid-phase, resume from the start of that phase.

Before Phase 1a, check `personal/sessions/` for files matching `*_SessionLog.md`. If any exist, list them and ask whether this is a new evaluation or resuming a previous evaluation. If resuming, load the log, state the last completed phase, confirm the resume point, and skip to the next incomplete phase. If starting new, proceed to Phase 1a.

File Naming: `[Company]_[Role]_[YYYY-MM]_SessionLog.md`

---

## Phase 1a — Session Setup

*(No documents are loaded in this phase)*

1. Confirm the job description has been provided. If not, request it and halt until received.

2. Confirm the company name and role title are stated in the JD or supplied by the user. State both explicitly before closing.

3. Create the session log at `personal/sessions/[Company]_[Role]_[YYYY-MM]_SessionLog.md` with company, role title, session start date, and a note that the JD is available. Confirm the file was created.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Role Classification and Context

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing it)*

1. Read the job description. Read the `**Active Domain:**` value from the header of `personal/knowledge/Experience_Inventory.md` (do not assume). Load `rules/domains/<active_domain>.md` and confirm it loaded. Check the JD against the domain file's Section 3 Pack Selection Criteria. If a "Do NOT use when" condition applies, flag the scope mismatch and obtain user direction before proceeding: halt for a different domain, or continue as an explicit cross-domain evaluation with acknowledged mismatch.

2. Propose the role level (IC, AD, Dir, Sr. Dir, VP). If not explicit in the title, infer from required experience, scope, and reporting structure. State rationale and obtain explicit agreement. The agreed level governs seniority of voice, scope framing, and achievement selection in all subsequent phases.

3. Research the company, industry, and role via web search to an expert-level understanding: company stage, culture, competitive landscape, organizational context, and what success looks like. Record each source (URL or publication and date); these go to the session log and GapAnalysis file at phase close.

4. Identify the 4-5 most critical requirements or themes in the job description.

5. Read `rules/registry_archetype.md`. Identify the role archetype and state the framing angle. If no archetype satisfies the match criteria, halt: state which criteria failed for each archetype, inform the user that `skills/archetype_creation.md` must be completed first, and do not advance. If borderline between two archetypes, note the ambiguity. If the role spans two archetypes, identify a primary and secondary with rationale, then load `rules/cv/dual_archetype.md` and apply its rules throughout.

   Load the archetype file: `rules/archetypes/Archetype_<N>_<Name>.md`. For a dual-archetype, load the secondary archetype file as well. Confirm each loaded completely. The archetype file is authoritative on identity, match criteria, summary framing, tag priorities, achievement framing pattern, and de-emphasis. Domain vocabulary and calibration examples come from the domain file loaded in Step 1. Level voice comes from the content rules file (loaded later by `cv_targeted`; not needed for fit evaluation).

6. Read `rules/registry_org_type.md`. Select the org type, state why, and note the framing emphasis that will govern organizational environment description in later content generation.

**Phase 2a Closing:** Follow Standard Phase Closing. Append to the session log: "Phase 2a Complete" with date, role level, active domain, any scope-mismatch handling, sources consulted, critical requirements, archetype selection and rationale (plus dual-archetype detail if applicable), and org type with rationale. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

For each item, cite evidence from Phase 2a. Any Fail invokes QC Failure Recovery.

- **Role Level:** explicit user agreement is documented for the level stated in Step 2.
- **Company Research:** Step 3 sources are listed with enough detail to revisit.
- **Critical Requirements:** 4-5 items are present from Step 4; fewer than 4 fails.
- **Archetype Selection:** the primary archetype is defensible against the match criteria in the loaded archetype file. Cite each satisfied criterion and the JD language supporting it. A wrong archetype propagates through every subsequent phase.
- **Dual-Archetype (if applicable):** the secondary archetype is explicitly evidenced in the JD, not inferred from peripheral language. Primary/secondary assignment reflects the dimension the role primarily evaluates on. Weak or speculative secondary fails; recommend single-archetype treatment and obtain user agreement.
- **Domain Scope:** active domain was read from the Inventory header, the domain file was loaded, and Section 3 was checked. If a scope mismatch was flagged, user direction is documented.
- **Org Type:** selection is consistent with the JD and the Step 3 research. Cite the specific company characteristic that drove it.
- **Standard QC Document Verification** per Global Rules.

**Phase 2b Closing:** Follow Standard Phase Closing. Append to the session log: "Phase 2b Complete" with date, QC pass, and any flagged issues plus resolution. Next phase is Phase 3a.

---

## Phase 3a — Fit Evaluation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing it)*

1. Load the following. Confirm each loaded completely:
   - `personal/knowledge/Experience_Inventory.md`
   - `personal/knowledge/Career_Narratives.md`

2. Map each critical requirement to the most relevant experience, citing the source document and specific achievement. Every claim must be traceable.

3. Flag gaps, weak matches, and cases where language needs to shift to match the role's framing.

4. Gap handling:
   - Present a summary table of all gaps: description, severity (High/Medium/Low), and initial hypothesis on approach (CV language, interview narrative, needs user input, or insufficient evidence).
   - Then work through each gap one at a time, waiting for a response before moving to the next.
   - For each gap, search the source documents for closing evidence and ask clarifying questions.
   - Do not close gaps via creative framing without explicit approval. Gaps that cannot be closed through source material may be carried by interview narrative; flag these.

5. Note items to de-emphasize for this role and request approval.

6. Provide the fit assessment:
   - Overall fit rating with brief rationale
   - Top 2-3 strengths driving candidacy for this specific role
   - Top 2-3 risks or gaps that could filter early
   - Application recommendation: **Proceed**, **Proceed as speculative application**, or **Do not pursue**

   Threshold (a role clears only if both conditions hold):
   - *Domain exclusion check*: the role does not require a primary domain outside established positioning. Exclusion gate only, not a positive fit signal.
   - *Candidacy viability*: at least 65% of critical requirements have a strong, source-citable match (2 of 3, 3 of 4, or 4 of 5). Weak or inferred matches do not count.

   *Strong match*: a specific, named achievement or deliverable traceable to a specific source document and entry. General capability claims do not qualify.

   Outcome mapping:
   - **Proceed**: both conditions clear.
   - **Proceed as speculative application**: domain exclusion passes but viability falls below threshold. User must explicitly acknowledge the risk before continuing.
   - **Do not pursue**: domain exclusion fails.

   If either condition fails, state it and ask how to proceed. Do not advance to Phase 3b without a clear response.

7. State the resolution status of every High-severity gap: resolved, carried by interview narrative, or unresolved. If any remain unresolved, surface it and obtain a decision before requesting phase approval.

**Phase 3a Closing:** Follow Standard Phase Closing. Append to the session log: "Phase 3a Complete" with date, full requirement mapping, gap summary table, de-emphasis items and approval status, fit assessment, application recommendation, and High-severity gap resolutions. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

For each item, cite evidence from Phase 3a. Any Fail invokes QC Failure Recovery.

- **Requirement Mapping:** every critical requirement from Phase 2a has a source-citable match per the strong-match definition.
- **Gap Enumeration:** every gap from Step 3 appears in the Step 4 summary table.
- **Gap Rating Judgment:** load `rules/judgment_qc.md` and confirm it loaded completely. Apply Mode 7 (Gap rating miscalibration) from Evaluation-Level Check to every gap row. Cite the gap, the JD language, the supporting inventory entries, the assessed match distance, and the severity the evidence supports. Any stated severity that does not match the evidence fails.
- **Gap Resolution Completeness:** every gap was worked through individually with a user response, and ends in one of: resolved via CV language, carried by interview narrative, or unresolved with explicit user acknowledgment.
- **High-Severity Gaps:** every High gap has an explicit resolution. Any unresolved High gap without a user decision fails.
- **De-Emphasis Approvals:** each Step 5 item has explicit user agreement.
- **Fit Threshold:** state the count of critical requirements, the count with strong source-citable matches, and the 65% calculation. Confirm the domain exclusion check was performed and the recommendation matches the threshold result. If the outcome was Proceed as Speculative Application, confirm explicit user risk acknowledgment.
- **Standard QC Document Verification** per Global Rules.

**GapAnalysis File:** Before closing, write `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md` containing:
1. Role context: company, role title, role level, active domain (with domain file path `rules/domains/<active_domain>.md`), primary archetype (number, name, archetype file path `rules/archetypes/Archetype_<N>_<Name>.md`) and secondary if applicable, rationale for each archetype, org type, and org-type framing emphasis.
2. Critical requirements from Phase 2a with the source-citable match for each.
3. Full gap summary table with severity and resolution status per gap.
4. Fit assessment summary from Phase 3a Step 6 including the threshold calculation and application recommendation.
5. Sources section listing every research source from Phase 2a Step 3 with enough detail to revisit.

If `personal/sessions/` does not exist, create it. Confirm the file was written. This file is the terminal output of this skill and is used as input by `cv_targeted` and `interview_prep`.

**Phase 3b Closing:** Follow Standard Phase Closing. Append to the session log: "Phase 3b Complete" with date and GapAnalysis file path.

Before presenting next steps, review the session for experience descriptions, framing decisions, gap resolutions, or positioning language not yet reflected in source documents. Summarize what was found and why each item is worth capturing.

- If capturable content was found: recommend Phase 4. If the user confirms, proceed to Phase 4. If the user declines, proceed to application next steps.
- If none was found: state so and proceed to application next steps.

**Application next steps:**
- If the recommendation is Proceed or Proceed as Speculative Application: inform the user that `cv_targeted` can be triggered with the GapAnalysis file as context, and that `interview_prep` can begin in parallel using the same file.
- If the recommendation is Do Not Pursue: ask whether to close the workflow.

---

## Phase 4 — Source Document Update

Dedicated to capturing information surfaced during this role evaluation that should be added to source documents.

Load `skills/source_document_update_workflow.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 3b.

At the close of Phase 4, delete the session log at `personal/sessions/[Company]_[Role]_[YYYY-MM]_SessionLog.md`. Confirm deletion.
