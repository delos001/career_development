# Role Evaluation Skill

## Objective

Evaluate a target role against established experience and positioning to determine whether to proceed with an application. Produces a structured fit assessment and GapAnalysis file used as input by `cv_targeted` and `interview_prep`.

---

## Setup

**Global Rules Loading**
Load `rules/global_rules.md` at the start of this skill. Verify load by citing the final section heading (or last line if unstructured). If not verifiable, apply Document Load Instructions fallback. All rules in that file govern this skill.

**Phases**
Action Phases: 1a, 2a, 3a
QC Phases: 2b, 3b
Presentation Phases: 2c, 3c
Transition Phases: 4

**Session Continuity**
A session log persists work across sessions. The log is created at Phase 1c close, appended at every subsequent phase close, and retained for history (no deletion at skill close). If a session ends mid-phase, resume from the start of that phase.

Before Phase 1a, check `personal/sessions/` for files matching `*_SessionLog.md`. If any exist, list them and ask whether this is a new evaluation or resuming a previous evaluation. If resuming, load the log, state the last completed phase, confirm the resume point, and skip to the start of the next incomplete phase. If starting new, proceed to Phase 1a.

Session Log File Naming Convention: `[Company]_APP-NNN_[YYYY-MM]_SessionLog.md`

---

## Phase 1a — Session Setup

1. Confirm the job description (JD) has been provided. If not, request the user paste it into the chat or provide a path or address where it can be retrieved.  Do not proceed until user provides it.
2. Extract the company name and role title from the job description. If either is absent or ambiguous, ask the user to provide the information now.
3. Determine the role level (IC, AD, Dir, Sr. Dir, VP); if not explicit in the title, infer from required experience, scope, and reporting structure. Record the rationale. Role level governs seniority of voice, scope framing, and achievement selection throughout.
4. Assign the application unique ID (APP-NNN) per `rules/global_rules.md`. Hold the value in working memory for recording at Phase 1c close when the SessionLog is created.
5. Provide concise list of one-liners for each step taken.

**Phase 1a Closing:** Follow Global Rules Action Phase Closing. Next phase is Phase 1b.

---

## Phase 1b - Quality Control of Phase 1a

*(Only after Phase 1a has been explicitly approved)*

Run QC internally against the checks below. Do not present passing checks to the user; only failures surface, per QC Failure Recovery.

- **JD Read:** the JD was read completely. Partial content or read failure fails.
- **Company and Role Title:** both present and unambiguous or provided by the user. Any flagged ambiguity from Phase 1a Step 2 fails and requires resolution in Phase 1c.
- **Role Level:** level is stated. If inferred, the rationale cites required experience, scope, or reporting structure. Unsupported inference fails.
- **APP-NNN:** an APP-NNN was generated in Phase 1a Step 4. The value matches the format `APP-NNN` with three or more zero-padded digits. A scan of `personal/sessions/` was performed before assignment. Missing or malformed fails.
- **Standard QC Document Verification** per Global Rules.

**Phase 1b Closing:** Follow Global Rules QC Phase Closing. Next phase is Phase 1c.

---

## Phase 1c - Presentation of Phase 1

*(Only after Phase 1b has been explicitly approved)*

1. Present the company name. Obtain agreement or correction.
2. Present the role title. Obtain agreement or correction.
3. Present the role level with rationale. Obtain agreement or correction.
4. Create `personal/sessions/[Company]_APP-NNN_[YYYY-MM]_SessionLog.md` with the initial content including:
   - Header metadata: company, role, level, APP-NNN, session start date, JD source
   - `Phase 1a complete, YYYY-MM-DD.`
   - `Phase 1b complete, YYYY-MM-DD. QC outcome: <pass | fail; brief resolution>.`

**Phase 1c Closing:** Follow Global Rules Presentation Phase Closing. Append to the session log: "Phase 1c Complete" with any updates to date, company, role, level, and JD source. Next phase is Phase 2a.

---

## Phase 2a — Role Classification and Context

*(Only after Phase 1c has been explicitly approved)*

1. Obtain the active domain: read `**Active Domain:**` from the header of `personal/knowledge/Experience_Inventory.md` (do not assume)
2. Based on the active domain, load `rules/domains/<active_domain>.md`. Verify load by citing the final section heading (or last line if unstructured). If not verifiable, apply Document Load Instructions fallback.
3. Check the JD against the domain file's Section 3 Pack Selection Criteria. If a "Do NOT use when" condition applies, record the scope mismatch with a brief note describing which criterion was triggered. Do not halt or obtain user direction; the mismatch is surfaced in Phase 2c.
4. Research the company, industry, and role via web search to an expert-level understanding: company stage, culture, competitive landscape, organizational context, and what success looks like. Use authoritative sources only (company/IR/regulatory filings, peer-reviewed or analyst publications, recognized trade press); do not cite Wikipedia, crowd-sourced wikis, forums, or unattributed blogs.
5. Record each source (URL or publication and date).
6. Identify the 4-5 most critical requirements or themes in the job description.
7. Load `rules/registry_archetype.md`. Verify load by citing the final section heading (or last line if unstructured). If not verifiable, apply Document Load Instructions fallback.
   - Identify the role archetype and record the framing angle.
   - If the role spans two archetypes, identify primary and secondary and record the rationale. Load `rules/cv/dual_archetype.md`, verify load, apply its rules throughout the skill.
   - If no archetype satisfies the match criteria, record this as a no-archetype-match condition. Do not halt or inform the user; Phase 2b will surface the condition via QC Failure Recovery.
8. Load `rules/archetypes/Archetype_<N>_<Name>.md` for the primary archetype selected in Step 7. If a secondary archetype was selected, load its archetype file as well. Verify each load by citing the final section heading (or last line if unstructured). If any load is not verifiable, apply Document Load Instructions fallback. The archetype file is authoritative on identity, match criteria, summary framing, tag priorities, achievement framing pattern, and de-emphasis. Domain vocabulary and calibration examples come from the domain file loaded in Step 2.
9. Load `rules/registry_org_type.md`. Verify load by citing the final section heading (or last line if unstructured). If not verifiable, apply Document Load Instructions fallback. Select the organization type and record the rationale. Note the framing emphasis for capture in the GapAnalysis output.

**Phase 2a Closing:** Follow Global Rules Action Phase Closing.

Closing output (single line): `Phase 2a complete. <N> critical requirements identified, archetype and org type selected. Proceeding to Phase 2b.`

Session log append: `Phase 2a complete, YYYY-MM-DD.`

---

## Phase 2b — Quality Control of Phase 2a

*(Only after Phase 2a has been explicitly approved)*

Run QC internally against the checks below. Do not present passing checks to the user; only failures surface, per QC Failure Recovery.

- **Domain Scope:** active domain was read from the Inventory header, the domain file was loaded, and Section 3 was checked. If a scope mismatch was flagged, confirm it is recorded with the triggered criterion noted.
- **Company Research:** Step 4 sources are listed with enough detail to revisit.
- **Critical Requirements:** 4-5 items are present from Step 6; fewer than 4 fails.
- **Archetype Selection:** an archetype was selected in Phase 2a Step 7 and is defensible against the match criteria in the loaded archetype file, with each satisfied criterion mapped to specific JD language. A recorded no-archetype-match condition fails and requires `skills/archetype_creation.md` to be completed before this skill can proceed (surface via QC Failure Recovery).
- **Dual-Archetype (if applicable):** the secondary archetype is explicitly evidenced in the JD, not inferred from peripheral language. Primary/secondary assignment reflects the dimension the role primarily evaluates on. A weak or speculative secondary fails; surface via QC Failure Recovery, recommending single-archetype treatment.
- **Org Type:** selection is consistent with the JD and the Step 3 research. The specific company characteristic that drove it is identifiable.
- **Standard QC Document Verification** per Global Rules.

**Phase 2b Closing:** Follow Global Rules QC Phase Closing. Next phase is Phase 2c.

---

## Phase 2c — Presentation of Phase 2

*(Only after Phase 2b has been explicitly approved)*

Present items to the user for review. For each item, obtain user agreement or adjustment.

1. Present the user's active domain
2. Scope mismatch (only if recorded in Phase 2a): present the triggered criterion and the mismatch summary. Obtain user direction: (a) halt and restart with a different domain, or (b) continue as an explicit cross-domain evaluation with acknowledged mismatch.
3. State the organization type, rationale and framing emphasis
4. Present each critical requirement one at a time. State the requirement and the JD language it maps to.
5. State role archetype 1 and framing angle
6. State role archetype 2 and framing angle (if dual archetype was selected)
7. Present the list of research sources from Phase 2a Step 3. Confirm coverage is sufficient; ask whether additional research is needed.

**Phase 2c Closing:** Follow Global Rules Presentation Phase Closing. Next phase is Phase 3a.

Append to the session log: `Phase 2c complete, YYYY-MM-DD. Active domain: <domain>. Scope-mismatch handling: <note if applicable, else omit>. Archetype (agreed): <primary (and secondary if dual) with rationale>. Org type (agreed): <type with rationale>. Critical requirements (agreed): <list>. Sources consulted: <list>. Adjustments from presentation: <list or "none">.`

---

## Phase 3a — Fit Evaluation

*(Only after Phase 2c has been explicitly approved)*

1. Load `personal/knowledge/Experience_Inventory.md` and `personal/knowledge/Career_Narratives.md`. Verify load by citing the final section heading (or last line if unstructured). If not verifiable, apply Document Load Instructions fallback.
2. Map each critical requirement to the most relevant experience using the strong-match criterion: a strong match is a specific, named achievement or deliverable traceable to a specific source document and entry. General capability claims do not qualify. For each match, record the source document and specific achievement. If no strong match exists, do not map it; it will be flagged as a gap in Step 3.
3. Flag gaps (requirements without a strong match per Step 2) and cases where the role's framing requires a language shift on an otherwise-mapped experience. For each language-shift case, record the source entry and the target framing.
4. For each gap, assign severity (High/Medium/Low) and resolution method (CV language, interview narrative, or insufficient evidence). Do not close gaps via creative framing without explicit approval.
5. For each gap, gather closing information: search source documents first; if the gap cannot be closed from sources, ask the user directly for the information needed. Record what is gathered. No presentation of the completed gap list in this phase.
6. Record a resolution for each gap. Resolutions can be resolved by source documents, carried by interview narrative, or marked unresolved with explicit user acknowledgment. If any unresolved gaps remain, obtain agreement from the user that the gap is unresolved.
7. Record items to de-emphasize for this role with rationale for each.
8. Perform Domain exclusion check to verify the role does not require a primary domain outside established positioning. Exclusion gate only, not a positive fit signal.
9. Compute the fit assessment:
   - Count critical requirements and count those with a strong match per Step 2.
   - Candidacy viability: compute whether at least 65% of critical requirements have a strong match (2 of 3, 3 of 4, or 4 of 5).
   - Apply domain exclusion gate from Step 8.
   - Determine recommendation: Proceed (both conditions clear), Proceed as speculative application (domain exclusion passes but viability below threshold), or Do not pursue (domain exclusion fails).

**Phase 3a Closing:** Follow Global Rules Action Phase Closing. Next phase is Phase 3b.

Session log append: `Phase 3a complete, YYYY-MM-DD.`

---

## Phase 3b — Quality Control of Phase 3a

*(Only after Phase 3a has been explicitly approved)*

Run QC internally against the checks below. Do not present passing checks to the user; only failures surface, per QC Failure Recovery.

- **Requirement Mapping:** every critical requirement from Phase 2a is classified as either mapped to a specific experience (source document and specific achievement recorded per Phase 3a Step 2) or flagged as a gap (per Phase 3a Step 3). No requirement is left unclassified.
- **Gap Enumeration:** every gap from Step 3 is utilized in steps 4.
- **Gap Rating Judgment:** load `rules/judgment_qc.md`. Verify load by citing the final section heading (or last line if unstructured). If not verifiable, apply Document Load Instructions fallback. Apply Mode 7 (Gap rating miscalibration) from Evaluation-Level Check to every gap. Cite the gap, the JD language, the supporting inventory entries by `ID:`, the assessed match distance, and the severity the evidence supports. Any stated severity that does not match the evidence fails.
- **Language Shifts:** every case flagged in Phase 3a Step 3 as requiring a language shift has both the source entry and the target framing recorded.
- **Gap Resolution Completeness:** every gap has a recorded resolution from Phase 3a Step 6 tagged as one of: resolved by source evidence, carried by interview narrative, or unresolved (pending user acknowledgment in Phase 3c).
- **Domain Exclusion:** Confirm the domain exclusion check was performed.
- **Fit Assessment:** the fit assessment was computed in Phase 3a Step 9. Count math is correct, threshold conditions match the domain exclusion outcome and viability percentage, and recommendation follows the outcome mapping.
- **Standard QC Document Verification** per Global Rules.

**Phase 3b Closing:** Follow Global Rules QC Phase Closing. Next phase is Phase 3c.

---

## Phase 3c — Presentation of Phase 3

*(Only after Phase 3b has been explicitly approved)*

1. Present the requirement mapping: each requirement with its matched source (one line each, no rationale)
2. Present the gaps: each gap with severity and resolution (one line each, one line at a time)
3. Present De-emphasis items: each item (list only, no rationale)
4. Present cases where language needs to shift to match the role's framing (one line each, one at a time)
5. Present the fit assessment computed in Phase 3a Step 9:
   - Count of critical requirements and count with strong source-citable matches
   - Overall fit rating with brief rationale
   - Application recommendation: **Proceed**, **Proceed as speculative application**, or **Do not pursue**
6. Write the GapAnalysis file. The destination folder depends on the recommendation from Step 5:
   - **Proceed** or **Proceed as speculative application**: `personal/applications/[Company]_APP-NNN_[YYYY-MM]/GapAnalysis_[YYYY-MM].md`
   - **Do not pursue**: `personal/do_not_pursue/[Company]_APP-NNN_[YYYY-MM]/GapAnalysis_[YYYY-MM].md`

   Create the destination folder if it does not exist. The file contents are the same regardless of outcome:
   1. Role context: company, role title, role level, APP-NNN, active domain (with domain file path `rules/domains/<active_domain>.md`), primary archetype (number, name, archetype file path `rules/archetypes/Archetype_<N>_<Name>.md`) and secondary if applicable, rationale for each archetype, org type, and org-type framing emphasis.
   2. Critical requirements from Phase 2a with the source-citable match for each.
   3. Full gap summary table with severity and resolution status per gap.
   4. Fit assessment summary from Phase 3a Step 9 including the count math, threshold outcome, and application recommendation.
   5. Sources section listing every research source from Phase 2a Step 3 with enough detail to revisit.

   Confirm the file was written. This file is used as input by `cv_targeted` and `interview_prep` when the recommendation is Proceed or Proceed as speculative application.

Outcome mapping:
- **Proceed**: both conditions clear.
- **Proceed as speculative application**: domain exclusion passes but viability falls below threshold. User must explicitly acknowledge the risk before continuing.
- **Do not pursue**: domain exclusion fails.

**Phase 3c Closing:** Follow Global Rules Presentation Phase Closing.

Before presenting next steps, review the session for experience descriptions, framing decisions, gap resolutions, or positioning language not yet reflected in source documents. If capturable content was found, summarize briefly and recommend Phase 4. If the user confirms, proceed to Phase 4. If the user declines or no capturable content was found, proceed to application next steps.

**Application next steps:**
- If the recommendation is Proceed or Proceed as Speculative Application: inform the user that `cv_targeted` can be triggered with the GapAnalysis file as context, and that `interview_prep` can begin in parallel using the same file.
- If the recommendation is Do Not Pursue: ask whether to close the workflow.

The SessionLog is retained at `personal/sessions/[Company]_APP-NNN_[YYYY-MM]_SessionLog.md` as a historical record; do not delete it.

---

## Phase 4 — Source Document Update

Dedicated to capturing information surfaced during this role evaluation that should be added to source documents.

Load `skills/source_document_update_workflow.md` now. Verify load by citing the final section heading (or last line if unstructured). If not verifiable, apply Document Load Instructions fallback. Follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 3c.

**Phase 4 Closing:** Follow Global Rules Transition Phase Closing. This skill is complete.
