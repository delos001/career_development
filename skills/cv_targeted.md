# CV Targeted Skill

## Objective

Generate a role-tailored CV for a specific target role. This skill begins after `role_evaluation` has been completed and a GapAnalysis file exists for the target role. It covers experience architecture, content generation, and document production, followed by a source document update.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b

---

## Phase 1a — Context Load

*(No documents are loaded before this phase — the GapAnalysis file is the required input)*

1. Confirm a GapAnalysis file exists for the target role. If the file path is not provided, ask for the company name and role title and locate the file at `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md`. If no file is found, inform the user that `role_evaluation` must be completed before `cv_targeted` can proceed. Do not continue until the file is located.

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
- `knowledge/Experience_Inventory.md`
- `knowledge/Career_Narratives.md`
- `knowledge/Positioning.md`

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

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — CV Document Generation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load formatting specification and contact information:**
Load `rules/cv/format_spec.md` now. Confirm it loaded completely. All formatting decisions are governed by this file. It is the authoritative source — do not infer or recreate formatting from any other reference.

Load `knowledge/Contact_Info.md` now. Confirm it loaded completely. All contact line values — name, email, phone, LinkedIn, GitHub, and any present Website — must be sourced from this file. Do not hardcode any contact information in the generated script.

**Step 2 — Generate document:**
Generate the Word document programmatically using Python with python-docx. Load `rules/config.md` and use the Python executable path defined there. Write a Python script and execute it via Bash. All formatting decisions must reference `rules/cv/format_spec.md` — do not infer or recreate formatting from any other source. Use Windows-style paths in all Python file operations — Unix-style paths will fail.

Structure decisions were made in Phase 2 and govern the output. Do not default to any reference document's structure. Do not omit or collapse roles because they do not appear in a reference. A role that adds credibility to critical requirements from Phase 1a belongs in the main experience section.

**Step 3 — Save output:**
Save the completed CV to `outputs/` using this naming convention:
`Jason_Delosh_CV_[CompanyName]_[AbbreviatedRole]_[YYYYMM].docx`

**Phase 3a Closing:** State "File is ready for your review." Then follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control for Phase 3a

**Document Generation:** Confirm python-docx was used to generate the document via a Python script executed through Bash. Confirm all formatting decisions reference `rules/cv/format_spec.md` and were not inferred from any other source. If either cannot be confirmed, flag as a non-compliant step and invoke QC Failure Recovery.

**Filename Convention:** Confirm the output file was saved with the correct filename format. State the actual filename and confirm it matches the convention.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4.

---

## Phase 4 — Source Document Update

Dedicated to capturing information surfaced during this CV session that should be added to source documents.

Load `skills/source_document_update.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 3b.
