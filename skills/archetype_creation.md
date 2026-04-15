# Archetype Creation Skill

## Objective

Create a new role archetype when no existing archetype in `rules/registry_archetype.md` serves the target role. Produces a single archetype file at `rules/archetypes/Archetype_<N>_<Name>.md` and a registry entry.

Archetype files are domain-agnostic and level-agnostic. Vocabulary and calibration examples come from the active domain file; voice and register come from the content rules files. No per-domain or per-level work is needed once the archetype is created — it is ready for use by `role_evaluation`, `cv_targeted`, and `cv_general` immediately.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b, 5

---

## Phase 1a — Trigger and Context Capture

*(No documents loaded in this phase)*

1. Identify the trigger source and state it explicitly:
   - **Triggered from role_evaluation.md or cv_general.md:** the job description, company name, and role title should be available in the current session. Confirm each is present. If any are missing, request them now and do not proceed until received.
   - **Triggered independently:** request the job description, company name, and role title now. Do not proceed until all three are received.

2. State the company name, role title, and trigger source before closing this phase.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 1b.

---

## Phase 1b — Boundary Validation

*(Only after Phase 1a has been explicitly approved)*

1. Load `rules/registry_archetype.md`. Confirm it loaded completely.

2. For each archetype in the registry, load the archetype file and evaluate the role against its match criteria. State for each archetype:
   - Which criteria the role satisfies, if any
   - Which criteria the role fails to satisfy, and why

3. If any existing archetype satisfies the match criteria, do not proceed. State which archetype fits and why. Then:
   - If triggered from `role_evaluation.md`: direct the user to return to Phase 2a Step 5 with the identified archetype.
   - If triggered from `cv_general.md`: direct the user to return to Phase 2a Step 1 with the identified archetype.
   - If triggered independently: inform the user that a new archetype is not needed.
   Stop here.

4. If no existing archetype fits, document the specific failure per archetype. This is the evidence base that a new archetype is needed.

5. State a preliminary description of the unserved role type: what category of role, and what makes it distinct from all existing archetypes?

**Phase 1b Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Archetype Identity Design

*(Only after Phase 1b has been explicitly approved)*

1. Propose an archetype name: short noun phrase (2-4 words) describing the primary subject of the role type. State with rationale.

2. Draft "Use when" criteria (2-4 statements). Each must be specific and testable against a job description.

3. Draft "Do NOT use when" exclusions (1-3 statements). Each must reference the boundary with an existing archetype where overlap risk is real.

4. Boundary test: for each existing archetype, confirm the new "Use when" criteria do not overlap with its match criteria. State the result for each. If overlap exists, revise before proceeding.

5. Draft a primary differentiator: one sentence capturing what makes this archetype distinct.

6. Present name, criteria, exclusions, boundary test results, and differentiator. Obtain explicit approval.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Perform QC per Global Rules:
- **Standard QC Document Verification**

- **Name:** noun phrase, 2-4 words, describing the role type (not the person or skill set).
- **Use when criteria:** each criterion is specific and testable against a JD. Vague or unmeasurable criteria are blocking issues.
- **Exclusions:** each exclusion references an existing archetype where overlap risk is real. An exclusion without a specific target archetype is flagged.
- **Boundary test:** performed against all existing archetypes; results documented.
- **Primary differentiator:** a single sentence that stands alone.

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Archetype File Content Design

*(Only after Phase 2a and 2b have been explicitly approved)*

Read the canonical pattern before drafting: `rules/archetypes/Archetype_1_Transformation_Strategy.md`. The new archetype file must conform to this structure.

Draft the following sections. Present each to the user as drafted. Do not advance without confirmation.

1. **Identity:** expand the Phase 2a differentiator into a description of what makes a role fit this archetype (characteristic contexts, primary deliverable, scope). Note the archetype applies at both Leadership and IC levels and state explicitly that voice comes from the active content rules file; vocabulary and calibration come from the active domain file.

2. **Match Criteria:** separate Leadership and IC subsections. Each lists concrete role characteristics that activate this archetype at that level. Include verify-against notes referencing boundaries with adjacent archetypes, drawn from Phase 1b findings. Do not use domain-specific vocabulary; keep criteria abstract enough to apply across domains.

3. **Summary Framing:** bullet list covering Lead with / Do NOT lead with / Register / Required summary elements. Split Leadership vs IC within each bullet where the framing differs. Describe summary CONCEPTS (what to foreground), not domain vocabulary.

4. **Inventory Tag Priorities:** tag intersections per priority tier (High / Medium / Use if space permits / Avoid), separated by level if the archetype calls for level-specific priorities. State explicitly: "Level filter on queries comes from the active content rules file." Use the canonical tag vocabulary from `rules/domains/<active_domain>.md` Section 1. New tag values must be added to the domain file, not invented here.

5. **Achievement Framing Pattern:** the structural arc achievements must follow at this archetype, split by level where the pattern differs. State that calibration examples are provided by the active domain file.

6. **Archetype-Specific Handling (optional):** if this archetype has a universal pattern applying regardless of domain (like Archetype 2's technical credibility or Archetype 4's compound query requirement), draft it here. If no universal pattern, state so explicitly and skip.

7. **De-Emphasize:** patterns to suppress or route elsewhere, split by level where it differs.

8. **Section Order:** numbered CV section order. Ask explicitly whether this archetype includes Selected Projects; if yes, specify its position and inclusion rule. If no, state the omission.

9. **Dual-Archetype:** standard boilerplate referencing `rules/cv/dual_archetype.md`.

Explicitly excluded: domain-specific vocabulary (regulatory contexts, industry-specific terms, specific systems or tools); concrete calibration examples using domain language; tech stack lists. All of those belong in the active domain file, not in the archetype file. If any of this content surfaces during drafting, route it as starting material for a domain file update rather than placing it in the archetype file.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

Perform QC per Global Rules:
- **Standard QC Document Verification**

- **Sections present:** Identity, Match Criteria, Summary Framing, Inventory Tag Priorities, Achievement Framing Pattern, De-Emphasize, Section Order, Dual-Archetype. Archetype-Specific Handling is optional. Any missing required section is a blocking issue.
- **Domain-agnostic compliance:** confirm no section uses domain-specific vocabulary (e.g., "regulated clinical environments," specific systems, domain tag values not in every domain's taxonomy). Domain-coupled language is a blocking issue and must be moved to the domain file.
- **Level split present where appropriate:** Match Criteria, Summary Framing, Tag Priorities, Achievement Framing Pattern, and De-Emphasize each have Leadership and IC subsections where the content differs by level.
- **Tag values valid:** every tag value cited in Inventory Tag Priorities exists in the active domain file's Section 1 taxonomy. Values not in taxonomy are a blocking issue; either add to taxonomy or remove.
- **Canonical pattern compliance:** section numbering and naming match `rules/archetypes/Archetype_1_Transformation_Strategy.md`.

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — File Creation and Registry Update

*(Only after Phase 3a and 3b have been explicitly approved)*

1. Read `rules/registry_archetype.md`. Count existing archetype entries. The new archetype number is N+1. State it.

2. Derive the name slug: replace spaces with underscores, drop connector words (`&`, `and`) per the canonical convention (e.g., "Transformation & Strategy" → "Transformation_Strategy"). State the target file path: `rules/archetypes/Archetype_<N>_<Name_slug>.md`. Obtain explicit confirmation.

3. Create the archetype file at the confirmed path using the Phase 3a content.

4. Add a new entry to `rules/registry_archetype.md` matching the format used for Archetypes 1-4: section header with number and name, Use when summary, Do NOT use when summary, and a `**File:**` line pointing to the created archetype file path.

5. Confirm both writes completed before closing.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control of Phase 4a

Perform QC per Global Rules:
- **Standard QC Document Verification**

- **Archetype file:** Sections 1-9 present and match Phase 3a content.
- **File path:** created at `rules/archetypes/Archetype_<N>_<Name_slug>.md`, not at any legacy path.
- **Registry entry:** format matches existing entries; `**File:**` path matches the created file exactly; archetype number is N+1; name slug matches the approved name.

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5.

---

## Phase 5 — Handoff and Next Steps

1. Confirm the archetype file and registry entry are verified and in place.

2. State that the new archetype is immediately usable by `role_evaluation`, `cv_targeted`, and `cv_general` across all domains. No per-domain or per-level work is required.

3. Consider whether the active domain file should be updated with a calibration example for the new archetype. If yes, direct the user to update `rules/domains/<active_domain>.md` Section 5 with one STRONG example. This is optional but improves generation quality.

4. Trigger-source next steps:
   - If triggered from `role_evaluation.md`: direct the user to return to Phase 2a Step 5 and re-evaluate the role against the updated registry.
   - If triggered from `cv_general.md`: direct the user to return to Phase 2a Step 1 and re-evaluate the archetype selection.
   - If triggered independently: the archetype is registered and available for use.
