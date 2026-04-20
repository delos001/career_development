# Interview Prep Skill

## Objective

Generate a role-specific interview preparation document, a blank Interview Completion file, and a blank Interview Scratch file for a target role. This skill uses the GapAnalysis file from `role_evaluation` as its primary input. It produces three output files, all as `.md`: the interview prep reference document, the interview completion file (populated post-interview by `interview_capture`), and the interview scratch file (used by the user during each interview round as a minimal anchor-note surface). All three are saved to the application folder specified by the user.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b, 4a, 4b

---

## Phase 1a — Context Load

*(No documents are loaded before this phase)*

1. Confirm a GapAnalysis file exists for the target role. If the file path is not provided, ask for the company name and role title and locate the file at `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`. If no file is found, inform the user that `role_evaluation` must be completed before `interview_prep` can proceed. If multiple files match the company and role name (e.g., from multiple application cycles), list them and ask the user to confirm which to use. Do not continue until a single file is confirmed.

2. Load the GapAnalysis file. Confirm it loaded completely.

3. Extract and explicitly state the following:
   - Company name and role title
   - Role level
   - Active domain
   - Primary archetype (and secondary if applicable)
   - Org type and framing emphasis
   - Critical requirements (full list)
   - Application recommendation from role evaluation
   - Research sources from role evaluation (these seed company research in Phase 2a)

4. Active domain consistency check: read the current `**Active Domain:**` value from the header of `personal/knowledge/Experience_Inventory.md`. Compare to the active domain captured in the GapAnalysis file. If the values differ, the active domain has changed since the evaluation was run. Halt and surface the mismatch: state both values and ask the user whether to (a) revert the inventory header to the GapAnalysis domain before proceeding, (b) re-run `role_evaluation` under the current active domain, or (c) explicitly override and proceed under the current active domain with acknowledgment that the role was evaluated under a different domain. Do not proceed silently.

5. Ask the user for the absolute path to the output folder where all three documents will be saved. This is the folder where application documents for this role are stored. Do not proceed until this path is confirmed.

6. Confirm all context is in hand and state it explicitly before closing.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Research and Role Analysis

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

1. Load `rules/registry_company_type.md`. Confirm it loaded completely. Identify the company type from the GapAnalysis context and the research sources already available. Do not ask the user — determine it from available information. State the identified type and the rationale before proceeding.

   If no existing type fits the company without forcing a poor match, do not proceed silently. Inform the user that no matching type was found, state which types were considered and why each failed, and work with the user to define a new entry. Follow the "Adding New Types" instructions at the bottom of the registry: collect the type name, a one-line description of when it applies, and the specific research branches relevant beyond Universal. Write the new entry to `rules/registry_company_type.md` and confirm it was written before proceeding.

2. Review the research sources extracted from the GapAnalysis file in Phase 1a. Note which topics those sources already covered. Then execute the Universal research branches from the registry plus the branches specific to the identified company type, prioritizing branches not already addressed by prior research. Do not re-research topics already well-covered by the GapAnalysis sources unless new developments warrant it. Record each source consulted (URL or publication name and date) as research is performed.

3. Decompose the role beyond the job description. Using the research context, state what this role actually requires day-to-day: decision rights, stakeholder landscape, operating environment, and what success looks like in the first year. This must go materially beyond paraphrasing the JD.

4. Build First 90 Days framing from the role decomposition and company context. Do not use a generic 30/60/90 template. Derive the framing from what the role actually needs given the organizational context. If insufficient information exists to make the framing meaningful, note explicitly that the prepared answer for this question is to challenge the premise rather than deliver a rehearsed plan.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

**Company Type Identification:** Confirm the company type was identified from available context with stated rationale. If the type was forced to a poor fit, flag and re-evaluate.

**Research Coverage:** Confirm the Universal branches were executed. Confirm the type-specific branches from the registry were executed. For each branch, state a specific finding — general summaries without specific findings are non-compliant.

**Role Decomposition:** Confirm the decomposition goes beyond JD paraphrase. It must include at least one specific observation about operating context, stakeholder landscape, or success criteria not explicitly stated in the JD. If it does not, flag as non-compliant and re-run Step 3.

**First 90 Days:** Confirm it is derived from the role decomposition and company context, not from generic 30/60/90 language. If it reads as templated, flag and re-derive.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Content Generation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load source documents:**
Load the following now. Confirm each loaded completely before proceeding:
- `personal/knowledge/Experience_Inventory.md`
- `personal/knowledge/Career_Narratives.md`
- `personal/knowledge/Positioning.md`

**Step 2 — Alignment map:**
Map each critical requirement from the GapAnalysis to the most relevant experience in the loaded source documents, citing the specific document and entry. Every claim must be traceable. No general capability statements. Label this section "Alignment Map — Why Hire You" in the output document. This is the primary answer to "why should we hire you" and "what is your strongest qualification for this role."

**Step 3 — Gap handling language:**
For each gap identified in the GapAnalysis, draft specific interview handling language. This is not a repeat of the gap summary — it is the framing the user should use when the gap is raised or when the topic surfaces naturally. For each gap state: the gap, the handling approach (bridge to strength, honest acknowledgment with offset, or reframe), and the specific language to use.

**Step 4 — Stories bank:**
Ask the user: "Does this company have a known preference for story format — STAR, ATOLA, or another framework? If you're not sure, just say so and I'll default to STAR."

Based on the response:
- If STAR (or unknown): format all stories as STAR keyword-level cues — not full scripts, keywords and phrases to trigger memory
- If ATOLA: format all stories using the ATOLA structure (Actions, Thinking, Outcomes, Learnings, Applications). Flag any story that does not adapt cleanly to ATOLA — state why and present the best available adaptation or note if the story should be set aside
- If another framework is named: apply it as described by the user; if the framework is unfamiliar, ask the user to describe it before generating

Pull 6-10 relevant stories from `personal/knowledge/Career_Narratives.md` and supporting entries from `personal/knowledge/Experience_Inventory.md` that address the critical requirements or likely interview themes for this role. For each story: provide the formatted cue in the confirmed framework, note which critical requirement or question type it serves, and note any story that could serve an alternate format if requested later.

If fewer than 6 relevant stories exist in the source documents, do not pad with irrelevant stories to hit the count. State the number of relevant stories available, identify which critical requirements lack story coverage, and flag these gaps explicitly to the user before proceeding. The user may choose to continue with the available stories or pause to add new ones via `skills/career_narratives_builder.md`.

Philosophy or knowledge questions get a short conversational draft rather than a structured cue.

**Step 5 — Likely questions:**
Generate likely interview questions organized by type:
- Behavioral (minimum 8): for each, provide a keyword cue pointing to the best story from the stories bank
- Functional / technical (minimum 5): derive from critical requirements first. If critical requirements total fewer than 5, derive additional questions from the role decomposition and JD themes to reach the minimum. Do not force overlap or repetition.
- Situational (minimum 3): provide a framing note for each
- "Why this company" and "why this role": include these as anticipated interviewer questions. The user's prepared answers are in Sections 2 and 3 of the output document — do not duplicate them here, only flag them as questions the interviewer is likely to ask.
- Leadership or management questions (minimum 3): include this category if the role is Director level or above, or if the JD explicitly mentions direct reports, team leadership, or people management regardless of title. Omit for IC roles where the JD contains no leadership indicators.

**Step 6 — Questions to ask them:**
Generate 10-12 strong questions to ask interviewers. Questions must reference specific findings from Phase 2a research and the role decomposition — not generic. Organize by theme: role foundation and charter, team and structure, success metrics, organizational dynamics, strategic context. For non-corporate environments (government, academic, nonprofit, early-stage startup), adapt themes to fit the actual operating model — substitute themes like funding model, governance structure, or mission execution as appropriate. Flag 3-4 questions as highest priority for a short or constrained interview.

After presenting the generated questions, ask: "Are there specific questions you want to make sure are covered, or topics you need answers to that aren't already addressed?"

If the user says no, proceed to Step 7.

If the user raises items:
- First check whether each item is already addressed by a question in the generated list. If yes, confirm coverage explicitly.
- If not covered, evaluate whether a well-framed interview question is an appropriate vehicle to surface the answer. If yes, propose question wording and add it to the list.
- If a question is not the right vehicle — because it would be inappropriate to ask, would reveal a concern better handled elsewhere, or is more logistical than strategic — tell the user explicitly: "That concern isn't well-suited for an interview question because [reason]." Then identify the appropriate section and route it there: salary and logistics, gaps handling, or a note in the follow-up letter. Be transparent about where it is going and why.

Repeat for each item the user raises before proceeding.

**Step 7 — Personal inputs:**
Collect the following from the user. Prompt for each one at a time and wait for a response before moving to the next:

   a. Why This Role: Ask the user to state what draws them to this specific role. Draft a polished version from their input and confirm before finalizing.

   b. Why This Company: Ask the user to state what draws them to this specific company — distinct from why the role. Draft a polished version and confirm before finalizing.

   c. Employment Gap: Ask whether there is an employment gap likely to be raised. If yes, draft a clean explanation from their input. If no, note that this section will be omitted.

   d. Salary and Logistics: Ask for the target range, acceptable floor, and any logistics considerations (relocation, remote preference, start date flexibility). Draft handling language covering: how to state the range, how to respond if the range is borderline, how to defer without closing the door, and the internal acceptance condition.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

**Source Document Load:** Confirm all three source documents loaded completely before content generation began in Step 2.

**Alignment Map:** Enumerate each critical requirement. For each, confirm a source-citable match was provided — specific entry traceable to a source document. General capability claims do not qualify. Flag any requirement without a citable match.

**Gap Handling Language:** Confirm every gap from the GapAnalysis has handling language. If any gap is missing, flag as non-compliant.

**Stories Bank:** Confirm minimum 6 stories were pulled and each is citable to a source document. Confirm the confirmed story format was applied consistently. If ATOLA was selected, confirm flagging was applied to any story that did not adapt cleanly.

**Likely Questions:** Confirm minimum 8 behavioral, 5 functional, and 3 situational questions. Confirm each behavioral question references a story from the stories bank.

**Questions to Ask:** Confirm minimum 10 questions. Confirm they reference specific findings from Phase 2a. Confirm 3-4 high-priority questions are flagged. Confirm any user-raised items were addressed per the Step 6 routing logic — either added, confirmed as covered, or explicitly routed to another section.

**Personal Inputs:** Confirm all required prompted sections received user input. Confirm "Why This Role" and "Why This Company" are finalized and confirmed. Confirm salary handling language is present. If employment gap was omitted, confirm user explicitly said there was no gap.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — Document Generation

*(Only after Phase 3a and 3b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Generate interview prep document:**
Generate the interview prep document as a `.md` file. Write the file directly — no Python or python-docx required.

Naming convention: `InterviewPrep_[Company]_[AbbreviatedRole]_[YYYY-MM].md`

Use markdown heading hierarchy so the document is navigable in any markdown-aware editor:
- Document title (company and role): `#` (H1)
- Section headers (the 13 section names below): `##` (H2)
- Sub-headers within sections where content has named groupings (e.g., individual research branches, story titles, question categories): `###` (H3)
- Field labels or emphasis within body text: bold (`**label:**`), not a heading

Sections in this order:
1. Role and Company Snapshot — quick reference list: company, role title, role level, archetype, org type, application recommendation from role evaluation
2. Why This Role — finalized text from Phase 3a Step 7a
3. Why This Company — finalized text from Phase 3a Step 7b
4. Company Research — organized by research branch with all sources listed (URL or publication and date)
5. Role Decomposition — from Phase 2a Step 3
6. Alignment Map — Why Hire You — from Phase 3a Step 2
7. Gaps and How to Handle Them — from Phase 3a Step 3
8. Likely Questions and Framing — from Phase 3a Step 5
9. Stories Bank — from Phase 3a Step 4
10. Questions to Ask Them — from Phase 3a Step 6 (full list, high-priority questions flagged)
11. Salary and Logistics — from Phase 3a Step 7d
12. Employment Gap Explanation — from Phase 3a Step 7c (omit this section entirely if user confirmed no gap)
13. First 90 Days Framing — from Phase 2a Step 4

Confirm the file was written before proceeding.

**Step 2 — Generate interview completion file:**
Load `templates/Interview_Completion_Template.md`. Confirm it loaded completely. Write its content to the output path as-is, with the following header-field substitutions only:
- Document title line: substitute `[Company]`, `[Role]`, and `[YYYY-MM]` with actual values
- Application Reference block: substitute the hint-text HTML comments for Company, Job Title, GapAnalysis File, and Interview Prep File with the actual values

Do not pre-populate any round's fields. All Logistics, Interviewers, Questions and Responses, and Round Debrief sections must retain their hint-text HTML comments verbatim. `interview_capture` is the skill that populates rounds post-interview; pre-population here would contaminate its writeback.

Save to the output folder confirmed in Phase 1a. Naming convention:
`InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].md`

Confirm the file was written before proceeding.

**Step 3 — Generate interview scratch file:**
Load `templates/Interview_Scratch_Template.md`. Confirm it loaded completely. Write its content to the output path with the following substitutions:
- Document title line: substitute `[Company]`, `[Role]`, and `[YYYY-MM]` with actual values
- File References block: substitute the Interview Prep path (absolute path to the file written in Step 1) and the Interview Completion path (absolute path to the file written in Step 2)

All round section headings (`## Round 1` through `## Round 4`) must remain with empty bodies below them. These are the surfaces the user will write anchor notes into during each interview round.

Save to the output folder confirmed in Phase 1a. Naming convention:
`InterviewScratch_[Company]_[AbbreviatedRole]_[YYYY-MM].md`

Confirm the file was written before proceeding.

**Step 4 — Update questions library:**
Check for an existing file at `personal/knowledge/Questions_Library.md`. If it does not exist, create it with this header:

```
# Questions Library

Reusable interview questions accumulated across applications. Tagged by company, role, and date.
```

Append the questions from Phase 3a Step 6 to the library. For each entry include: the question text, the company and role it was generated for, and the date. Check for semantic duplicates before appending — do not add a question that is substantively the same as one already present.

Confirm the library was updated before proceeding.

**Step 5 — User acceptance and Last Used stamping:**

State "All three documents are ready for your review." Ask the user to confirm acceptance of the generated prep, completion, and scratch files before any metadata stamping occurs. If the user requests revisions, loop back to the appropriate earlier phase and regenerate. Do not stamp Last Used on rejected or draft output.

After explicit user acceptance:

1. Identify every `personal/knowledge/Career_Narratives.md` entry cited in the Stories Bank (Phase 3a Step 4), Alignment Map (Phase 3a Step 2), or Gap Handling Language (Phase 3a Step 3). Match via entry title (the `## [Title]` heading of the narrative).
2. Identify every `personal/knowledge/Experience_Inventory.md` entry cited in the Alignment Map, Gap Handling Language, or supporting any Stories Bank entry. Match via the `ID:` value of each source entry.
3. For each cited narrative and inventory entry, overwrite the `Last Used:` line with the current `YYYY-MM`. Single date only — do not append or keep history.
4. Write the updated files. State the count of narrative entries stamped, the count of inventory entries stamped, and the month written.

Narratives are the primary citation in this skill; inventory entries are secondary. Stamp both when cited. Do not stamp entries that were loaded but not cited in the accepted output.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control of Phase 4a

**Interview Prep Document:** Confirm the file was written to the correct output path as a `.md`. Confirm all 13 sections are present in the specified order using `##` (H2) headings. State the actual filename and confirm it matches the naming convention.

**Interview Completion File:** Confirm the file was written to the correct output path as a `.md`. Confirm the document title and Application Reference block were populated with actual values (no `[Company]`, `[Role]`, `[YYYY-MM]` placeholders remain; no hint-text HTML comments remain in those four header fields). Confirm all round sections (Logistics, Interviewers, Questions and Responses, Round Debrief) retain their hint-text HTML comments verbatim — no round pre-population occurred. State the actual filename and confirm it matches the naming convention.

**Interview Scratch File:** Confirm the file was written to the correct output path as a `.md`. Confirm the document title was populated with actual values. Confirm the File References block now contains absolute paths to the Interview Prep and Interview Completion files just written, and no hint-text HTML comments remain in those two references. Confirm all four `## Round N` headings are present with empty bodies. State the actual filename and confirm it matches the naming convention.

**Questions Library:** Confirm `personal/knowledge/Questions_Library.md` was updated. State the number of questions added and confirm no semantic duplicates were added.

**Template Load:** Confirm both `templates/Interview_Completion_Template.md` and `templates/Interview_Scratch_Template.md` were loaded before generating the respective files.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5.

---

## Phase 5 — Source Document Update

Dedicated to capturing information surfaced during this session that should be added to source documents.

Load `skills/source_document_update_workflow.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 4b.
