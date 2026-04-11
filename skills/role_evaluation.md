# Role Evaluation Skill

## Objective

Evaluate a target role against established experience and positioning to determine whether to proceed with an application. Produces a structured fit assessment and GapAnalysis file used as input by `cv_targeted` and `interview_prep`.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b, 4

**Session Continuity**
A session log persists work across multiple sessions. At the start of every session, before Phase 1a, check for existing session logs in `outputs/` matching `SessionLog_*.md`. If one or more exist, list them and ask whether this is a new evaluation or a resume of an existing one. If resuming, load the identified log, state the last completed phase, confirm the resume point with the user, and skip to the next incomplete phase. If starting new, proceed to Phase 1a.

The session log is created at Phase 1a close, updated at the close of every subsequent action phase, and deleted at the close of Phase 4. Logging occurs at phase close only — if a session ends mid-phase, resume from the start of that phase using session log context from prior completed phases.

Naming convention: `SessionLog_[Company]_[Role]_[YYYYMM].md`

---

## Phase 1a — Session Setup

*(No documents are loaded in this phase)*

1. Confirm the job description has been provided. If not, request it now and do not proceed until received.

2. If the company name and title are not clearly stated at the beginning of the job description, request them now and do not proceed until received.

3. Confirm company and title information is in hand and state them explicitly before closing this phase.

4. Create the session log file at `outputs/SessionLog_[Company]_[Role]_[YYYYMM].md`. Write: company name, role title, session start date, and a note confirming the job description is available. Confirm the file was created before closing.

**Phase 1a Closing:** Follow Standard Phase Closing. Session log created in Step 4 — confirm before closing. Next phase is Phase 2a.

---

## Phase 2a — Role Classification and Context

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

1. Read the provided job description carefully.

2. Review the job description and propose the role level (IC, AD, Dir, Sr. Dir, VP, etc.). If not explicitly stated in the title, infer it from required experience, scope of responsibilities, and reporting structure. State the inferred level with rationale and obtain explicit agreement before moving forward. The agreed role level governs seniority of voice, scope framing, and achievement selection throughout all subsequent phases.

3. Research the company, industry, and role using web search to develop an expert-level understanding of what this position actually requires — including company stage, culture, competitive landscape, organizational context, and what success looks like in this type of role at this type of company. Record each source consulted (URL or publication name and date) as you go — these will be written to the session log and GapAnalysis file at phase close.

4. Identify the 4-5 most critical requirements or themes in the job description.

5. Read `rules/registry_archetype.md`. Using the match criteria summaries in the registry, identify the role archetype and state the framing angle. If the role is borderline between two archetypes, note the ambiguity explicitly before proceeding.

   If none of the archetypes in the registry satisfy the match criteria for this role, do not proceed. State specifically which match criteria failed for each archetype. Inform the user that a new archetype may be needed and that `skills/archetype_creation.md` must be triggered and completed before role evaluation can continue. Stop here and do not advance to any subsequent step or phase.

   If the role spans two archetypes, identify a primary and secondary archetype and state both explicitly with rationale. Apply the Dual-Archetype Handling Rules from `rules/global_rules.md` throughout all subsequent phases.

   Then load the archetype instruction document matching the confirmed primary archetype. Use the role level confirmed in Step 2 to select between the leadership and IC file — both file paths are listed in the registry entry for each archetype. If a dual-archetype was identified, also load the secondary archetype document using the same role-level logic.

   Confirm each loaded completely before proceeding. If loading fails, follow Document Load Instructions fallback.

6. Read `rules/registry_org_type.md`. Identify the most appropriate org type and state why. Note the framing emphasis for the confirmed org type — it will govern how the organizational environment and operating context are described throughout content generation if the application proceeds.

**Phase 2a Closing:** Follow Standard Phase Closing. Update the session log: append "Phase 2a — Complete" with date, confirmed role level, list of sources consulted in Step 3, critical requirements, archetype selection with rationale, dual-archetype details if applicable, and org type selection with rationale. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Role Level: Confirm the role level was explicitly stated or inferred with rationale, and that explicit user agreement was obtained. If agreement is not documented, flag as a blocking issue and invoke QC Failure Recovery.

Company Research: Confirm web search was performed in Phase 2a Step 3. State the specific sources or findings that informed the role understanding. If research was not performed or cannot be evidenced, flag as a non-compliant step.

Critical Requirements: Confirm 4-5 critical requirements were identified in Phase 2a Step 4. If fewer than 4 were identified, flag and complete before proceeding.

Archetype Selection: Verify the primary archetype selection is defensible against the match criteria defined in the loaded archetype file. State the specific match criteria satisfied and cite the job description language that supports each. If the role does not clearly satisfy the match criteria, flag as a blocking issue — a wrong archetype selection propagates through every subsequent phase and cannot be corrected without restarting from Phase 2a.

If a dual-archetype was identified: verify the secondary archetype is explicitly evidenced in the job description — not inferred from peripheral language. Confirm the primary/secondary assignment reflects which dimension the role primarily evaluates candidates on. If the secondary is weak or speculative, recommend single-archetype treatment and obtain user agreement before proceeding.

Format Selection: Confirm the org type selection is consistent with the job description and the company research completed in Phase 2a Step 3. State the specific company characteristic that drove the selection.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 2b Closing:** Follow Standard Phase Closing. Update the session log: append "Phase 2b — Complete" with date and QC pass confirmation. Note any blocking issues that were flagged and how they were resolved. Next phase is Phase 3a.

---

## Phase 3a — Fit Evaluation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

1. Load the following source documents now. Confirm each loaded completely before proceeding:
   - `knowledge/Experience_Inventory.md`
   - `knowledge/Career_Narratives.md`
   - `knowledge/Positioning.md`

2. Using the loaded source documents, map each critical requirement identified in Phase 2a to the most relevant experience, citing the source document and specific achievement. Every claim must be traceable to a source document.

3. Flag gaps, weak matches, or cases where language needs to shift to match this role's framing.

4. When gaps are identified:
   - First, present a summary table of all identified gaps: gap description, severity (High/Medium/Low), and initial hypothesis on approach (CV language, interview narrative, needs user input, or insufficient evidence)
   - Then work through each gap one at a time, waiting for a response before moving to the next
   - For each gap, search the loaded source documents for experience that could close it. Ask clarifying questions for any information that could be relevant.
   - Do not attempt to close gaps through creative framing unless discussed and approved first. Gaps that cannot be closed through source material may need to be carried by interview narrative — flag these explicitly.

5. Note anything to de-emphasize for this role and request approval/agreement.

6. Provide a structured fit assessment:
   - Overall fit rating with brief rationale
   - Top 2-3 strengths driving candidacy for this specific role
   - Top 2-3 risks or gaps that could filter early
   - Application recommendation using the following outcomes:

     **Proceed** — role clears both conditions below.
     **Proceed as speculative application** — domain exclusion passes but candidacy viability falls below threshold; user must explicitly acknowledge the risk before proceeding.
     **Do not pursue** — domain exclusion fails.

     **Threshold definition:** A role clears the threshold if it meets both conditions:
     - *Domain exclusion check* — the role does not require a primary domain that falls outside established positioning. This is an exclusion gate, not a positive fit signal.
     - *Candidacy viability* — at least 65% of critical requirements from Phase 2a have a strong, source-citable match (2 of 3, 3 of 4, or 4 of 5). Weak or inferred matches do not count.

     **Strong match definition:** A specific, named achievement or deliverable in the source documents that directly addresses the requirement — citable to a specific document and entry. General capability claims do not qualify.

     If either condition fails, state this explicitly and ask whether to proceed as a speculative application with explicitly acknowledged risk. Do not proceed to Phase 3b without a clear response.

7. Explicitly state the resolution status of every High-severity gap: resolved, carried by interview narrative, or unresolved. If any High-severity gap remains unresolved, do not request phase approval — surface it and obtain a decision on how to proceed.

**Phase 3a Closing:** Follow Standard Phase Closing. Update the session log: append "Phase 3a — Complete" with date. Write the full requirement mapping, gap summary table, de-emphasis items and approval status, fit assessment, application recommendation, and High-severity gap resolution statuses. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

**Requirement Mapping:** Enumerate the critical requirements identified in Phase 2a. For each, confirm a source-citable match was presented in Phase 3a Step 2. A specific named achievement or deliverable traceable to a source document is required — general capability claims do not qualify. Flag any requirement without a citable match.

**Gap Enumeration:** Confirm all gaps identified in Phase 3a Step 3 were included in the summary table from Step 4. For each gap, confirm the severity rating is defensible — state the specific reason severity was assigned. Flag any gap rated without clear rationale.

**Gap Resolution Completeness:** Enumerate every gap from the Phase 3a summary table. For each, confirm: (a) it was worked through individually with a user response before moving to the next, and (b) the resolution is one of the three allowed states — resolved via CV language, carried by interview narrative, or unresolved with explicit user acknowledgment. Any gap without a recorded resolution or acknowledgment is a blocking issue — invoke QC Failure Recovery.

**High-Severity Gaps:** Confirm every High-severity gap has an explicit resolution status. Any unresolved High-severity gap without an explicit user decision is a blocking issue — invoke QC Failure Recovery.

**De-Emphasis Approvals:** Confirm any items flagged for de-emphasis in Phase 3a Step 5 received explicit user agreement. De-emphasis applied without approval is a non-compliant step — flag it.

**Fit Threshold Verification:** Confirm Phase 3a Step 6 applied the threshold correctly. State: the number of critical requirements, the number with strong source-citable matches, and verify the 65% calculation. Confirm the domain exclusion check was performed. Confirm the application recommendation outcome matches the threshold result. If the recommendation was Proceed as Speculative Application, confirm explicit user acknowledgment of risk was obtained and documented.

**GapAnalysis File:** Before closing this phase, write a gap analysis file to `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md` containing:
1. Role context: company name, role title, role level, primary archetype name and instruction file path for the confirmed role level (and secondary archetype name and file path if applicable, with rationale for both), org type, and org-type framing emphasis
2. The list of critical requirements from Phase 2a and the source-citable match for each
3. The full gap summary table including severity and resolution status for every gap
4. The fit assessment summary from Phase 3a Step 6 including the threshold calculation and application recommendation
5. A sources section listing all research sources consulted during Phase 2a Step 3, with enough detail for the user to revisit them (URL or publication name and date)

This file is the terminal output of this skill. It is used as input by `cv_targeted` and `interview_prep`. If the `outputs/` directory does not exist, create it. Confirm the file was written before closing.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 3b Closing:** Follow Standard Phase Closing. Update the session log: append "Phase 3b — Complete" with date and GapAnalysis file path.

Before presenting next steps, review the full session for experience descriptions, framing decisions, gap resolutions, or positioning language surfaced that is not yet reflected in source documents. Present a summary of what was found with brief rationale for why each item is worth capturing.

If capturable content was identified:
- Recommend proceeding to Phase 4 to capture it
- If the user confirms, proceed to Phase 4
- If the user declines, proceed to application next steps below

If no capturable content was identified:
- State that no new capturable content was surfaced and proceed to application next steps below

**Application next steps:**

If the application recommendation is Proceed or Proceed as Speculative Application:
- Inform the user that `cv_targeted` can now be triggered using the GapAnalysis file written in this phase as context.
- Inform the user that interview preparation can begin in parallel. The GapAnalysis file is available as starting context for `interview_prep` when that skill is triggered.

If the application recommendation is Do Not Pursue:
- Ask whether the user wants to close the workflow.

---

## Phase 4 — Source Document Update

Dedicated to capturing information surfaced during this role evaluation that should be added to source documents.

Load `skills/source_document_update.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 3b.

At the close of Phase 4, delete the session log file at `outputs/SessionLog_[Company]_[Role]_[YYYYMM].md`. Confirm deletion before closing.
