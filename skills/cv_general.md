# General CV Builder Skill

## Objective

Generate a generalized CV — not tailored to a specific role or company — that represents the user's best case for a defined targeting context. Used for recruiter outreach, networking, and situations where a polished, ready-to-send CV is needed without running the full `role_evaluation` and `cv_targeted` workflow.

Output is a .docx file saved to `outputs/` with a descriptor-based filename confirmed with the user.

**Boundary with `cv_targeted`:** Use `role_evaluation` followed by `cv_targeted` when a specific job description is available and the goal is a role-tailored CV with fit evaluation and gap closure. Use this skill when no specific role is in hand and the goal is a strong general representation for a defined targeting context.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b, 4a, 4b, 5a, 5b

---

## Phase 1a — Session Setup and Targeting

*(No documents are loaded in this phase)*

1. Ask the user to state the targeting context for this CV. Collect the following:
   - **Level:** Leadership (Associate Director and above) or Individual Contributor
   - **Primary capability focus:** The domain or archetype this CV should foreground — e.g., transformation and strategy, data and analytics, process and operations, platform and technology
   - **Org type context:** Large enterprise established, or mid-size scale-up (refer to `rules/registry_org_type.md` selection criteria if needed)
   - **Any additional targeting notes:** Industry, specific audience (e.g., executive search firm), or other framing context the user wants to apply

   Do not proceed without all four inputs confirmed.

2. Confirm the targeting context in full and state it explicitly before closing this phase.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Archetype and Context Selection

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

1. Read `rules/registry_archetype.md`. Present the archetype options with their match criteria summaries. Based on the primary capability focus stated in Phase 1a, propose an archetype. If the targeting context spans two archetypes, propose a primary and secondary with rationale.

   If the user's stated targeting context does not satisfy the match criteria for any archetype, do not proceed. State specifically which criteria failed for each archetype. Inform the user that a new archetype may be needed and that `skills/archetype_creation.md` must be triggered and completed before this skill can continue.

   If a dual-archetype is identified, load `rules/cv/dual_archetype.md` now and confirm it loaded completely. Apply its rules throughout all subsequent phases.

   Obtain explicit user agreement on the archetype selection before proceeding.

2. Load the archetype and domain files for the confirmed primary archetype. Content generation uses three orthogonal sources: archetype (loaded here), domain (loaded here), and content rules (loaded in Phase 4a).

   a. Determine the active domain. Read the `**Active Domain:**` value from the header of `personal/knowledge/Experience_Inventory.md`. Do not assume; read the file. If no Active Domain is declared, halt and prompt the user before continuing.

   b. Load the archetype file: `rules/archetypes/Archetype_<N>_<Name>.md` per `rules/registry_archetype.md`. Authoritative on match criteria, summary framing pattern, tag priority intersections, achievement framing pattern, archetype-specific handling, and de-emphasis.

   c. Load the domain file: `rules/domains/<active_domain>.md`. Authoritative on tag taxonomy, vocabulary, framing conventions, pack selection criteria, technical proficiencies content, and archetype calibration examples.

   d. If a dual-archetype was identified, load the secondary archetype file.

   Confirm each loaded completely before proceeding.

3. Read `rules/registry_org_type.md`. Confirm the org type selection from Phase 1a against the registry selection criteria. State the framing emphasis for the confirmed org type — it will govern how the organizational environment and operating context are described throughout content generation.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

**Archetype Selection:** Confirm the selected archetype satisfies the match criteria in the registry. State which specific criteria were met. If the selection was borderline, confirm the rationale was stated and user agreement was obtained.

**Level Confirmation:** Confirm the level (leadership or IC) was explicitly stated by the user in Phase 1a. The level will govern voice at content generation time via the content rules file loaded in Phase 4a; no per-level archetype or domain file exists.

**Org Type:** Confirm the org type was confirmed against the registry selection criteria and the framing emphasis was noted.

**Standard QC Document Verification:** Verify all documents loaded in Phase 2a loaded completely.

State the result of each check. Flag failures and invoke QC Failure Recovery before proceeding.

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Source Document Review and Experience Architecture

*(Only after Phase 2b has been explicitly approved)*
*(State each step before completing the step)*

1. Load the following source documents now. Confirm each loaded completely before proceeding:
   - `knowledge/Experience_Inventory.md`
   - `knowledge/Career_Narratives.md`
   - `knowledge/Positioning.md`

2. Review the loaded source documents against the confirmed archetype's inventory tag priorities. Identify which entries, themes, and narratives are most relevant to the targeting context. State the top-tier material explicitly — these are the achievements that must be represented in the finished CV.

   Unlike `cv_targeted`, there is no job description to match against. The archetype's tag priorities are the primary selection guide. The user's additional targeting notes from Phase 1a provide secondary context.

3. Propose the experience architecture:
   - Which roles belong in the main experience section and which receive summary treatment
   - Which achievements within each role should be developed as full bullets versus brief mentions
   - How to apply the 10-year recency rule: all roles in the last 10 years belong in the main experience section; roles that add credibility to the archetype's core capabilities belong regardless of age

   Also check the Independent & Volunteer Projects section of the inventory. If entries exist, present them separately to the user for consideration as a Selected Projects CV section. Do not fold project entries into the main experience section. Whether a Selected Projects section appears in the output is governed by the active archetype — if the archetype does not include it, flag this to the user before proceeding.

   Before presenting the architecture to the user for approval, load `rules/judgment_qc.md` and confirm it loaded completely. Apply Mode 8 (Experience architecture miscalibration) from the Architecture-Level Check section against every role in the proposed architecture. The credibility basis for this skill is three factors taken together: the confirmed role level from Phase 1a (what candidates at this level are evaluated on), the active archetype's High Priority tag combinations, and the user's targeting context from Phase 1a. These are the native credibility frame for a non-targeted CV — this skill does not produce a role-specific CV and does not use role-specific critical requirements. Any conflict with the continuity-plus-credibility rules must be resolved and reflected in the architecture before the architecture is presented. Keep `rules/judgment_qc.md` loaded — it is re-used in Phase 4b.

   Present the proposed architecture and obtain explicit user approval before proceeding to content generation.

4. Note any gaps — source material that is thin or missing for the stated targeting context. Flag these for the user. Unlike `cv_targeted`, there is no gap closure phase here — this CV represents what currently exists in the source documents. If gaps are significant enough to warrant source document work before generating the CV, recommend triggering the appropriate builder skill first and stopping this session.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

**Source Document Verification:** Confirm all three source documents loaded completely per Standard QC Document Verification.

**Archetype Alignment:** Confirm the top-tier material identified in Step 2 maps directly to the archetype's High Priority tag combinations. If any High Priority tag combination has no identified source material, flag it explicitly.

**Experience Architecture Approval:** Confirm the proposed architecture was presented to the user and explicitly approved before this phase closes. If approval is not documented, flag as a blocking issue.

**Gap Acknowledgment:** Confirm any material gaps identified in Step 4 were stated to the user and acknowledged before proceeding.

State the result of each check. Flag failures and invoke QC Failure Recovery before proceeding.

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — CV Content Generation

*(Only after Phase 3a and 3b have been explicitly approved)*
*(State each step before completing the step)*

1. Load the content rules file matching the level confirmed in Phase 1a. Confirm it loaded completely:
   - Leadership (AD+) → `rules/cv/content_rules_leadership.md`
   - IC → `rules/cv/content_rules_ic.md`

   All rules in the content rules file apply actively throughout content generation — they are requirements to satisfy in every line generated, not pre-conditions to confirm in advance.

   Apply the org-type framing emphasis from the registry entry confirmed in Phase 2a throughout content generation. Framing emphasis governs how the organizational environment and operating context are described — archetype governs achievement selection and characterization.

2. Confirm the archetype file and domain file are still available in context. If not, reload them now before proceeding.

3. Confirm the approved experience architecture from Phase 3a. This governs which roles appear in full and which receive summary treatment.

4. Generate complete CV content applying all rules from the archetype file, domain file, and content rules file simultaneously. Present content as fully drafted text organized by section in the order determined by the archetype. All bullets are final-form. This output is the complete content set placed into the document in Phase 5a.

   Because there is no job description, framing is governed entirely by the archetype's summary framing rules, achievement selection criteria, and content to de-emphasize — not by a specific role's requirements. The CV should read as a strong, principled representation of the user's capability in the stated targeting context.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control of Phase 4a

**Content Rules Verification:** Verify the loaded content rules file was actively applied throughout generation. For each rule, state the verification method and result. Any rule that cannot be verified against the output must be flagged as non-compliant and QC Failure Recovery invoked.

**Archetype Compliance:** Verify the generated content satisfies the archetype's required section order, summary framing rules, and achievement selection criteria. Verify that content flagged as "avoid for this archetype" is not present.

**Org-Type Framing:** Verify the org-type framing emphasis was applied in how the organizational environment and operating context are described.

**Experience Architecture:** Verify the approved architecture from Phase 3a was followed. Confirm no roles were omitted or collapsed outside of what was approved.

**Source Traceability:** Verify that every achievement and claim is traceable to a source document loaded in this session or information explicitly provided by the user during this session. Flag any content that cannot be traced.

**CV QC Checklist:** Load `rules/cv/qc_checklist.md` now. Apply the Universal section against the generated CV content. Then apply the archetype section matching the active archetype and role level confirmed in Phase 1a. For each item, cite specific evidence from the generated content — a specific bullet, section, or line. General confirmations are not acceptable. State Pass or Fail for each item. Any Fail invokes QC Failure Recovery before this phase can close.

**Judgment QC:** Confirm `rules/judgment_qc.md` is still loaded from Phase 3a Step 3; if not, load it now and confirm it loaded completely. Apply Modes 1 through 6 from the Content-Level Checks section against every bullet in the generated content. For each mode, cite the specific bullet under review and the specific inventory entry (or other in-session source) that supports or contradicts the bullet. State Pass or Fail for each bullet per mode. Any Fail invokes QC Failure Recovery before this phase can close.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5a.

---

## Phase 5a — Document Generation

*(Only after Phase 4a and 4b have been explicitly approved)*
*(State each step before completing the step)*

1. Load `rules/cv/format_spec.md` now. Confirm it loaded completely. All formatting decisions are governed by this file — do not infer or recreate formatting from any other source.

   Load `knowledge/Contact_Info.md` now. Confirm it loaded completely. All contact line values — name, email, phone, LinkedIn, GitHub, and any present Website — must be sourced from this file. Do not hardcode any contact information in the generated script.

2. Propose an output descriptor based on the targeting context confirmed in Phase 1a. The descriptor should reflect the combination of level, domain, and org type in a concise, readable format — for example: `Leadership_DataAnalytics_Enterprise` or `IC_Transformation_ScaleUp`. Present the proposed descriptor and obtain user confirmation or override before proceeding.

3. Generate the Word document programmatically using Python with python-docx. Load `rules/config.md` and use the Python executable path defined there. Write a Python script and execute it via Bash. All formatting decisions must reference `rules/cv/format_spec.md` — do not infer or recreate formatting from any other source. Use Windows-style paths in all Python file operations.

   Structure decisions were made in Phase 4a and govern the output. Do not default to any reference document's structure.

4. Save the completed CV to `outputs/` using this naming convention: `CV_General_[descriptor]_[YYYY-MM].docx` where descriptor is the confirmed value from Step 2.

5. **User acceptance and Last Used stamping:**

   State "File is ready for your review." Ask the user to confirm acceptance of the generated CV before any metadata stamping occurs. If the user requests revisions, loop back to the appropriate earlier phase and regenerate. Do not stamp Last Used on rejected or draft output.

   After explicit user acceptance:

   a. Identify every `knowledge/Experience_Inventory.md` entry cited in the Phase 4a generated content. Match via the bold action statement line and the associated `Role:` line (to disambiguate same-verb entries across different roles).
   b. For each cited entry, overwrite the `Last Used:` line with the current `YYYY-MM`. Single date only — do not append or keep history.
   c. Write the updated inventory file. State the count of entries stamped and the month written.

   Do not stamp entries that were not cited in the accepted output. `cv_general` does not stamp `Career_Narratives.md` entries — narratives are loaded as reference depth, but narrative Last Used is owned by `interview_prep`.

**Phase 5a Closing:** Follow Standard Phase Closing. Next phase is Phase 5b.

---

## Phase 5b — Quality Control of Phase 5a

Verify the generated document against `rules/cv/format_spec.md`. Confirm:
- File saved to `outputs/` with the confirmed filename
- Document structure matches the approved section order from the archetype
- Formatting elements (fonts, spacing, bullet style, header treatment) conform to the format spec
- No content was altered during document generation relative to the approved Phase 4a output

State the result of each check. Flag failures and invoke QC Failure Recovery.

**Phase 5b Closing:** Follow Standard Phase Closing. Next phase is Phase 6.

---

## Phase 6 — Source Document Update

Dedicated to capturing information surfaced during this CV session that should be added to source documents.

Load `skills/source_document_update_workflow.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 5b.
