# CV Targeted Skill

## Objective

Generate a role-tailored CV for a specific target role. This skill begins after `role_evaluation` has been completed and a GapAnalysis file exists for the target role. It covers experience architecture, content generation, and document production, followed by a source document update.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b

**Session Continuity**

A content decisions file persists Phase 2 outputs across sessions for a given target role. Before Phase 1a, check `personal/sessions/` for existing files matching `*_ContentDecisions.md`. If one or more exist, list them with the Status line from each and ask whether this is a new generation or a resume.

If resuming:
1. Load the GapAnalysis file and the ContentDecisions file for the target role. Confirm both loaded completely.
2. State the last completed phase from the Status line of the ContentDecisions file.
3. Confirm the resume point with the user.
4. Skip to the first incomplete phase. If resuming into Phase 3a, treat the generated CV content captured in ContentDecisions as the approved Phase 2a output; do not regenerate.

If starting new:
- Proceed to Phase 1a.
- If a prior ContentDecisions file exists for the same company and role, state this and obtain explicit user confirmation to overwrite before any later write occurs. Do not overwrite silently.

The file is created at Phase 2b close, updated at Phase 3a Step 4 after user acceptance, and updated again at Phase 3b close. Writes occur at phase close only. If a session ends mid-phase, resume from the start of that phase using the ContentDecisions file from prior completed phases.

Naming convention: `[Company]_[Role]_[YYYY-MM]_ContentDecisions.md`

---

## Phase 1a — Context Load

*(No documents are loaded before this phase — the GapAnalysis file is the required input)*

1. Confirm a GapAnalysis file exists for the target role. If the file path is not provided, ask for the company name and role title and locate the file at `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`. If no file is found, inform the user that `role_evaluation` must be completed before `cv_targeted` can proceed. Do not continue until the file is located.

2. Load the GapAnalysis file now. Confirm it loaded completely.

3. Extract and explicitly state the following from the GapAnalysis file:
   - Company name and role title
   - Role level
   - Primary archetype (and secondary if applicable)
   - Org type and framing emphasis
   - Critical requirements (full list)
   - Application recommendation from role evaluation

4. Confirm with the user that this context is accurate and that they want to proceed to CV generation. Do not proceed until confirmed.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — CV Content Creation

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load content rules:**
Load the content rules file matching the role level confirmed in Phase 1a. Confirm the content rules file loaded completely:
- AD+ roles → `rules/cv/content_rules_leadership.md`
- IC roles → `rules/cv/content_rules_ic.md`

All rules in the content rules file apply actively throughout content generation — they are not pre-conditions to confirm, they are requirements to satisfy in every line generated.

Apply the org-type framing emphasis from Phase 1a throughout content generation. Framing emphasis governs how the organizational environment and operating context are described — archetype governs achievement selection and characterization.

**Step 2 — Load archetype instruction set:**
Load the archetype instruction document using the file path provided in the GapAnalysis file for the primary archetype. If a secondary archetype was identified in Phase 1a, load that document using its file path from the GapAnalysis file as well, and also load `rules/cv/dual_archetype.md`. Apply the dual-archetype rules throughout all subsequent phases. Confirm each loaded completely before proceeding. If loading fails, follow Document Load Instructions fallback.

**Step 3 — Load source documents:**
Load the following source documents now. Confirm each loaded completely before proceeding:
- `personal/knowledge/Experience_Inventory.md`
- `personal/knowledge/Career_Narratives.md`
- `personal/knowledge/Positioning.md`

**Step 4 — Experience architecture:**
All roles in the last 10 years belong in the main experience section to demonstrate career continuity. For those roles that don't add credibility to critical requirements from Phase 1a, a one or two-line summary entry may be used. A role that adds credibility to critical requirements from Phase 1a belongs in the main experience section regardless of age.

Before generating any content, produce a proposed experience section architecture and present for approval. For each role in the full career history, state:
- Company name and role title
- Proposed treatment: Full entry with bullets (main section) | One-line entry in main section | One-line entry in Earlier Professional Roles | Omit entirely
- Rationale tied to critical requirements from Phase 1a

Also check the Independent & Volunteer Projects section of the inventory. If entries exist, present them separately to the user for consideration as a Selected Projects CV section. Do not fold project entries into the main experience section. Whether a Selected Projects section appears in the output is governed by the active archetype — if the archetype does not include it, flag this to the user before proceeding.

Before presenting the architecture to the user for approval, load `rules/judgment_qc.md` and confirm it loaded completely. Apply Mode 8 (Experience architecture miscalibration) from the Architecture-Level Check section against every role in the proposed architecture. Cite each role, its proposed treatment, the 10-year continuity status, and the Phase 1a critical requirement(s) it does or does not support. Any conflict with the continuity-plus-credibility rules must be resolved and reflected in the architecture before the architecture is presented. Keep `rules/judgment_qc.md` loaded — it is re-used in Phase 2b.

Wait for explicit approval of the experience architecture before proceeding to Step 5.

**Step 5 — Generate CV content:**
Generate complete CV content applying all rules from the active archetype instruction set and the loaded content rules file simultaneously. Present content as fully drafted text organized by section in the order determined by the approved archetype. All bullets are final-form. This output is the complete content set placed into the document in Phase 3.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control for Phase 2a

**Experience Architecture Approval:** Confirm the proposed experience architecture from Step 4 was presented to the user and explicitly approved before content generation began in Step 5. If approval is not documented, flag as a blocking issue and invoke QC Failure Recovery.

**Content Rules Verification:** Verify the loaded content rules file was actively applied throughout generation. For each rule, state the verification method and result. Any rule that cannot be verified against the output must be flagged as non-compliant and QC Failure Recovery invoked.

**CV QC Checklist:** Load `rules/cv/qc_checklist.md` now. Apply the Universal section against the generated CV content. Then apply the archetype section matching the active archetype and role level confirmed in Phase 1a. For each item, cite specific evidence from the generated content — a specific bullet, section, or line. General confirmations are not acceptable. State Pass or Fail for each item. Any Fail invokes QC Failure Recovery before this phase can close.

**Judgment QC:** Confirm `rules/judgment_qc.md` is still loaded from Phase 2a Step 4; if not, load it now and confirm it loaded completely. Apply Modes 1 through 6 from the Content-Level Checks section against every bullet in the generated content. For each mode, cite the specific bullet under review and the specific inventory entry (or gap analysis source) that supports or contradicts the bullet. State Pass or Fail for each bullet per mode. Any Fail invokes QC Failure Recovery before this phase can close.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Content Decisions File:** Before closing this phase, write a content decisions file to `personal/sessions/[Company]_[Role]_[YYYY-MM]_ContentDecisions.md`. If a file with this name already exists, confirm user approval to overwrite (per Session Continuity). The file must contain:

1. **Status line:** `Phase 2b Complete: YYYY-MM-DD`
2. **Reference:** path to the GapAnalysis file that anchored this session
3. **Experience Architecture (Phase 2a Step 4):** for each role in the full career history, state company, role title, treatment (Full entry with bullets | One-line main | Earlier Professional Roles | Omit), and rationale tied to critical requirements
4. **Selected Projects:** inclusion decision, rationale, and entries if included
5. **Framing Decisions:** org-type framing emphasis as applied, primary archetype (and secondary plus dual-archetype handling if applicable), de-emphasis items carried from GapAnalysis, and any notable framing calls made during generation
6. **Inventory Entries Cited:** per role block, the bold action statement and associated `Role:` line for every `personal/knowledge/Experience_Inventory.md` entry cited in the Phase 2a Step 5 generated content. Match via the bold action statement and Role line to disambiguate same-verb entries across different roles.
7. **Generated CV Content (Phase 2a Step 5):** the full final-form content set, organized by section in the approved archetype order
8. **QC Pass Log:** Phase 2b pass date

If the `personal/sessions/` directory does not exist, create it. Confirm the file was written before closing.

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — CV Document Generation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load formatting specification and contact information:**
Load `rules/cv/format_spec.md` now. Confirm it loaded completely. All formatting decisions are governed by this file. It is the authoritative source — do not infer or recreate formatting from any other reference.

Load `personal/knowledge/Contact_Info.md` now. Confirm it loaded completely. All contact line values — name, email, phone, LinkedIn, GitHub, and any present Website — must be sourced from this file. Do not hardcode any contact information in the generated script.

**Step 2 — Generate document:**
Generate the Word document programmatically using Python with python-docx. Load `rules/config.md` and use the Python executable path defined there. Write a Python script and execute it via Bash. All formatting decisions must reference `rules/cv/format_spec.md` — do not infer or recreate formatting from any other source. Use Windows-style paths in all Python file operations — Unix-style paths will fail.

Structure decisions were made in Phase 2 and govern the output. Do not default to any reference document's structure. Do not omit or collapse roles because they do not appear in a reference. A role that adds credibility to critical requirements from Phase 1a belongs in the main experience section.

**Step 3 — Save output:**
Save the completed CV to `outputs/` using this naming convention:
`Jason_Delosh_CV_[CompanyName]_[AbbreviatedRole]_[YYYY-MM].docx`

**Step 4 — User acceptance and Last Used stamping:**
State "File is ready for your review." Ask the user to confirm acceptance of the generated CV before any metadata stamping occurs. If the user requests revisions, loop back to the appropriate earlier phase and regenerate. Do not stamp Last Used on rejected or draft output.

After explicit user acceptance:

1. Use the **Inventory Entries Cited** list from the ContentDecisions file as the citation set. If the list is not present (e.g., a legacy session without a ContentDecisions file), identify every `personal/knowledge/Experience_Inventory.md` entry cited in the Phase 2a generated content by matching the bold action statement and the associated `Role:` line (to disambiguate same-verb entries across different roles).
2. For each cited entry, overwrite the `Last Used:` line with the current `YYYY-MM`. Single date only — do not append or keep history.
3. Write the updated inventory file. State the count of entries stamped and the month written.
4. Update the ContentDecisions file: change Status to `Phase 3a Complete: YYYY-MM-DD`, and append a **Phase 3a Output** section containing the CV output filename, the count of inventory entries stamped, the stamp month, and the acceptance date.

Do not stamp entries that were not cited in the accepted output. `cv_targeted` does not stamp `Career_Narratives.md` entries — narratives are loaded as reference depth for anchor bullets, but narrative Last Used is owned by `interview_prep`.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control for Phase 3a

**Document Generation:** Confirm python-docx was used to generate the document via a Python script executed through Bash. Confirm all formatting decisions reference `rules/cv/format_spec.md` and were not inferred from any other source. If either cannot be confirmed, flag as a non-compliant step and invoke QC Failure Recovery.

**Filename Convention:** Confirm the output file was saved with the correct filename format. State the actual filename and confirm it matches the convention.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Content Decisions File Update:** Before closing this phase, update the ContentDecisions file: change Status to `Phase 3b Complete: YYYY-MM-DD` and append the Phase 3b pass date to the QC Pass Log. Confirm the file was written before closing.

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4.

---

## Phase 4 — Source Document Update

Dedicated to capturing information surfaced during this CV session that should be added to source documents.

Load `skills/source_document_update.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 3b.
