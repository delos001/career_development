# CV Targeted Skill

## Objective

Generate a role-tailored CV for a specific target role. This skill begins after `role_evaluation` has been completed and a GapAnalysis file exists for the target role. It covers experience architecture, content generation, and document production, followed by a source document update.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2, 3

**Session Continuity**

A content decisions file persists Phase 2 outputs across sessions for a given target role. Before Phase 1a, check `personal/sessions/` for existing files matching `*_ContentDecisions.md`. If one or more exist, list them with the Status line from each and ask whether this is a new generation or a resume.

If resuming:
1. Load the GapAnalysis file and the ContentDecisions file for the target role. Confirm both loaded completely.
2. State the last completed phase from the Status line of the ContentDecisions file.
3. Confirm the resume point with the user.
4. Skip to the first incomplete phase. If resuming into Phase 3, treat the generated CV content captured in ContentDecisions as the approved Phase 2 output; do not regenerate.

If starting new:
- Proceed to Phase 1a.
- If a prior ContentDecisions file exists for the same company and role, state this and obtain explicit user confirmation to overwrite before any later write occurs. Do not overwrite silently.

The file is created at Phase 2 close and updated at Phase 3 close. Writes occur at phase close only. If a session ends mid-phase, resume from the start of that phase using the ContentDecisions file from prior completed phases.

Naming convention: `[Company]_[Role]_[YYYY-MM]_ContentDecisions.md`

---

## Phase 1a — Context Load

*(No documents are loaded before this phase. The GapAnalysis file is the required input)*

1. Confirm a GapAnalysis file exists for the target role. If the file path is not provided, ask for the company name and role title and locate the file at `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`. If no file is found, inform the user that `role_evaluation` must be completed before `cv_targeted` can proceed. Do not continue until the file is located.

2. Load the GapAnalysis file now. Confirm it loaded completely.

3. Extract and explicitly state the following from the GapAnalysis file:
   - Company name and role title
   - Role level
   - Active domain (with domain file path)
   - Primary archetype (and secondary if applicable), with archetype file path
   - Org type and framing emphasis
   - Critical requirements (full list)
   - Application recommendation from role evaluation

4. Active domain consistency check: read the current `**Active Domain:**` value from the header of `personal/knowledge/Experience_Inventory.md`. Compare to the active domain captured in the GapAnalysis file. If the values differ, the active domain has changed since the evaluation was run. Halt and surface the mismatch: state both values and ask the user whether to (a) revert the inventory header to the GapAnalysis domain before proceeding, (b) re-run `role_evaluation` under the current active domain, or (c) explicitly override and proceed under the current active domain with acknowledgment that pack selection and archetype fit were evaluated under a different domain. Do not proceed silently.

5. Confirm with the user that this context is accurate and that they want to proceed to CV generation. Do not proceed until confirmed.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2.

---

## Phase 2 — CV Content Creation

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load content rules:**

Load the content rules file matching the role level confirmed in Phase 1a. Confirm it loaded completely:
- AD+ roles → `rules/cv/content_rules_leadership.md`
- IC roles → `rules/cv/content_rules_ic.md`

All rules in the content rules file apply actively throughout content generation. They are not pre-conditions to confirm; they are requirements to satisfy in every line generated.

Apply the org-type framing emphasis from Phase 1a throughout content generation. Framing emphasis governs how the organizational environment and operating context are described. Archetype governs achievement selection and characterization.

**Step 2 — Load archetype and domain files:**

Content generation uses three orthogonal sources: archetype, domain, and content rules. Each file owns one axis; composition happens at generation time.

1. Determine the active domain. Read the `**Active Domain:**` value from the header of `personal/knowledge/Experience_Inventory.md`. Do not assume; read the file. If no Active Domain is declared, halt and prompt the user before continuing.

2. Load the archetype file for the primary archetype identified in Phase 1a: `rules/archetypes/Archetype_<N>_<Name>.md`. The archetype file is authoritative on match criteria, summary framing pattern, tag priority intersections, achievement framing pattern, archetype-specific handling, and de-emphasis. Level voice is supplied by the content rules file from Step 1.

3. Load the domain file: `rules/domains/<active_domain>.md`. The domain file is authoritative on tag taxonomy, vocabulary, framing conventions, pack selection criteria, technical proficiencies content, and archetype calibration examples.

4. If a secondary archetype was identified in Phase 1a, load the secondary archetype file and load `rules/cv/dual_archetype.md`. Apply dual-archetype rules throughout all subsequent phases.

5. Confirm each file loaded completely. If loading fails, follow Document Load Instructions fallback.

**Step 3 — Load source documents and judgment constraints:**

Load the following now and confirm each loaded completely:
- `personal/knowledge/Experience_Inventory.md`
- `personal/knowledge/Career_Narratives.md`
- `personal/knowledge/Positioning.md`
- `rules/judgment_qc.md`

`rules/judgment_qc.md` is loaded here so that Modes 1-6 operate as active constraints during generation (Step 5), and Mode 8 applies during architecture design (Step 4). It is not re-applied as a retrospective bullet-by-bullet sweep.

**Step 4 — Experience architecture:**

Use Section 7 (Employment & Role History) of `personal/knowledge/Experience_Inventory.md` as the authoritative source for company, title, employment type, and date ranges when assessing 10-year continuity and proposing treatment per role.

All roles in the last 10 years belong in the main experience section to demonstrate career continuity. For roles that don't add credibility to critical requirements from Phase 1a, a one or two-line summary entry may be used. A role that adds credibility to critical requirements from Phase 1a belongs in the main experience section regardless of age.

Before generating any content, produce a proposed experience section architecture and present for approval. For each role in the full career history, state:
- Company name and role title
- Proposed treatment: Full entry with bullets (main section) | One-line entry in main section | One-line entry in Earlier Professional Roles | Omit entirely
- Rationale tied to critical requirements from Phase 1a

Also check the Independent & Volunteer Projects section of the inventory. If entries exist, present them separately to the user for consideration as a Selected Projects CV section. Do not fold project entries into the main experience section. Whether a Selected Projects section appears in the output is governed by the active archetype. If the archetype does not include it, flag this to the user before proceeding.

Apply Mode 8 (Experience architecture miscalibration) from `rules/judgment_qc.md` against every role in the proposed architecture before presenting. Cite each role, its proposed treatment, 10-year continuity status, and the Phase 1a critical requirement(s) it does or does not support. Resolve any conflict with the continuity-plus-credibility rules before presentation.

Wait for explicit approval of the experience architecture before proceeding to Step 5.

**Step 5 — Generate CV content:**

Generate complete CV content. Apply all rules from the active archetype, the loaded content rules file, the domain file, and `rules/judgment_qc.md` Modes 1-6 simultaneously as active generation constraints. Every bullet must be source-cited at the time it is written. Its framing, scope, outcome, duration, and attribution must match the inventory entry it derives from. Do not write a bullet whose framing you would then have to defend in QC. Generate only bullets that are already defensible.

Present content as fully drafted text organized by section in the order determined by the approved archetype. All bullets are final-form.

**Step 6 — Consolidated QC sweep:**

Load `rules/cv/qc_checklist.md` now. Confirm it loaded completely. Run one consolidated sweep against the generated content, then stop:

1. Universal items (U1-U7): cite specific evidence for each, state Pass or Fail.
2. Archetype items matching the active archetype and role level: cite specific evidence for each, state Pass or Fail.
3. Judgment integrity attestation: for any bullet whose scope, framing, outcome, duration, or attribution is not directly traceable to a single inventory entry, name the bullet and the entries it composes from. If no such bullets exist, state so explicitly. Do not re-run Modes 1-6 bullet-by-bullet. Modes 1-6 were applied as generation constraints in Step 5; this attestation surfaces only composites or stretches that require explicit acknowledgment.

Any Fail invokes QC Failure Recovery per Global Rules before presenting to the user.

**Step 7 — Write ContentDecisions file:**

Write to `personal/sessions/[Company]_[Role]_[YYYY-MM]_ContentDecisions.md`. If a file with this name already exists, confirm user approval to overwrite (per Session Continuity). If the `personal/sessions/` directory does not exist, create it. The file must contain:

1. **Status line:** `Phase 2 Complete: YYYY-MM-DD`
2. **Reference:** path to the GapAnalysis file that anchored this session
3. **Experience Architecture:** for each role, state company, role title, treatment, and rationale tied to critical requirements
4. **Selected Projects:** inclusion decision, rationale, and entries if included
5. **Framing Decisions:** org-type framing emphasis as applied, primary archetype (and secondary plus dual-archetype handling if applicable), de-emphasis items carried from GapAnalysis, and any notable framing calls made during generation
6. **Inventory Entries Cited:** per role block, the `ID:` value (`EX-NNN` or `PR-NNN`) for every `personal/knowledge/Experience_Inventory.md` entry cited in Step 5.
7. **Generated CV Content:** the full final-form content set, organized by section in the approved archetype order
8. **QC Pass Log:** Phase 2 pass date

Confirm the file was written before closing.

**Step 8 — Present to user:**

State the content is ready for review. Wait for explicit approval before proceeding to Phase 3. If the user requests changes, loop to the appropriate earlier step and regenerate only the affected portion.

**Phase 2 Closing:** Follow Standard Phase Closing. Next phase is Phase 3.

---

## Phase 3 — CV Document Generation

*(Only after Phase 2 has been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load formatting specification and contact information:**

Load `rules/cv/format_spec.md` now. Confirm it loaded completely. All formatting decisions are governed by this file. It is the authoritative source; do not infer or recreate formatting from any other reference.

Load `personal/knowledge/Contact_Info.md` now. Confirm it loaded completely. All contact line values (name, email, phone, LinkedIn, GitHub, and any present Website) must be sourced from this file. Do not hardcode any contact information in the generated script.

**Step 2 — Generate document:**

Generate the Word document programmatically using Python with python-docx. Load `rules/config.md` and use the Python executable path defined there. Write a Python script and execute it via Bash. All formatting decisions must reference `rules/cv/format_spec.md`; do not infer or recreate formatting from any other source. Use Windows-style paths in all Python file operations. Unix-style paths will fail.

Structure decisions were made in Phase 2 and govern the output. Do not default to any reference document's structure. Do not omit or collapse roles because they do not appear in a reference. A role that adds credibility to critical requirements from Phase 1a belongs in the main experience section.

**Step 3 — Save output:**

Save the completed CV to `outputs/` using this naming convention:
`Jason_Delosh_CV_[CompanyName]_[AbbreviatedRole]_[YYYY-MM].docx`

State the actual filename written and confirm it matches the convention.

**Step 4 — User acceptance and Last Used stamping:**

State "File is ready for your review." Ask the user to confirm acceptance of the generated CV before any metadata stamping occurs. If the user requests revisions, loop back to the appropriate earlier step and regenerate. Do not stamp Last Used on rejected or draft output.

After explicit user acceptance:

1. Use the **Inventory Entries Cited** list from the ContentDecisions file as the citation set. If the list is not present (e.g., a legacy session without a ContentDecisions file), identify every `personal/knowledge/Experience_Inventory.md` entry cited in the Phase 2 generated content by matching the `ID:` value of each source entry.
2. For each cited entry, overwrite the `Last Used:` line with the current `YYYY-MM`. Single date only. Do not append or keep history.
3. Write the updated inventory file. State the count of entries stamped and the month written.
4. Update the ContentDecisions file: change Status to `Phase 3 Complete: YYYY-MM-DD`, and append a **Phase 3 Output** section containing the CV output filename, the count of inventory entries stamped, the stamp month, and the acceptance date.

Do not stamp entries that were not cited in the accepted output. `cv_targeted` does not stamp `Career_Narratives.md` entries. Narratives are loaded as reference depth for anchor bullets, but narrative Last Used is owned by `interview_prep`.

**Phase 3 Closing:** Follow Standard Phase Closing. Next phase is Phase 4.

---

## Phase 4 — Source Document Update

Dedicated to capturing information surfaced during this CV session that should be added to source documents.

Load `skills/source_document_update_workflow.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 3.
