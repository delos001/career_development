# Archetype Creation Skill

## Objective

Create a new role archetype when no existing archetype in `rules/registry_archetype.md` serves the target role. Produces a single level-agnostic archetype skeleton at `rules/archetypes/Archetype_<N>_<Name>.md` and a registry entry.

Scope boundary: this skill produces the skeleton only. Domain-specific content (match criteria, summary framing, tag priorities, calibration examples, content to de-emphasize) is the concern of the domain pack entry for this archetype and is out of scope here. A pack entry must exist in the active domain before the new archetype can be used by `role_evaluation`, `cv_targeted`, or `cv_general`. Pack entries are created either by `skills/domain_creation.md` (when a new domain is being stood up and all registered archetypes are populated together) or by authoring `rules/domains/<active_domain>/archetype<N>_leadership.md` and `rules/domains/<active_domain>/archetype<N>_ic.md` against an existing domain. Phase 5 routes the user to the appropriate next step.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b, 5

---

## Phase 1a — Trigger and Context Capture

*(No documents loaded in this phase)*

1. Identify the trigger source and state it explicitly:
   - **Triggered from role_evaluation.md or cv_general.md:** the job description, company name, and
     role title should be available in the current session. Confirm each is present.
     If any are missing, request them now and do not proceed until received.
   - **Triggered independently:** request the job description, company name, and
     role title now. Do not proceed until all three are received.

2. State the company name, role title, and trigger source before closing this phase.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 1b.

---

## Phase 1b — Boundary Validation

*(Only after Phase 1a has been explicitly approved)*

1. Load `rules/registry_archetype.md`. Confirm it loaded completely before proceeding.

2. For each archetype in the registry, evaluate the role against its match criteria.
   State for each archetype:
   - Which criteria the role satisfies, if any
   - Which criteria the role fails to satisfy, and why

3. If any existing archetype satisfies the match criteria for this role, do not
   proceed. State which archetype fits and why. Then:
   - If triggered from role_evaluation.md: direct the user to return to Phase 2a Step 5 with the identified archetype.
   - If triggered from cv_general.md: direct the user to return to Phase 2a Step 1 with the identified archetype.
   - If triggered independently: inform the user that a new archetype is not needed.
   Stop here in either case.

4. If no existing archetype satisfies the match criteria, document the specific
   failure for each archetype. This is the evidence base that a new archetype is
   genuinely needed.

5. State a preliminary description of the unserved role type: what category of role
   is this, and what makes it distinct from all existing archetypes?

**Phase 1b Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Archetype Identity Design

*(Only after Phase 1b has been explicitly approved)*

1. Propose an archetype name. The name must be a short noun phrase (2-4 words)
   describing the primary subject of the role type. State it with rationale.

2. Draft "Use when" criteria: 2-4 statements describing the role types this archetype
   serves. Each criterion must be specific and testable against a job description.

3. Draft "Do NOT use when" exclusions: 1-3 statements. Each must reference the
   boundary with an existing archetype where overlap risk is real.

4. Boundary test: for each existing archetype, confirm that the new "Use when"
   criteria do not overlap with its match criteria. State the result for each.
   If overlap exists, revise the criteria before proceeding.

5. Draft a primary differentiator: one sentence capturing what makes this archetype
   distinct from all others.

6. Present name, criteria, exclusions, boundary test results, and differentiator
   to the user. Obtain explicit approval before proceeding.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Perform QC per Global Rules:
- **Standard QC Document Verification**

Name: confirm it is a noun phrase of 2-4 words describing the role type, not
the person or the skill set.

Use when criteria: confirm each criterion is specific and testable against a job
description. Flag any vague or unmeasurable criterion as a blocking issue.

Exclusions: confirm each exclusion references an existing archetype where overlap
risk is real. If an exclusion does not reference a specific existing archetype,
flag it.

Boundary test: confirm it was performed against all existing archetypes and results
are documented. If any archetype was skipped, flag as a blocking issue.

Primary differentiator: confirm it is one sentence that stands alone as a clear
explanation of why this archetype is distinct.

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Skeleton Content Design

*(Only after Phase 2a and 2b have been explicitly approved)*

Read the canonical skeleton pattern before drafting: `rules/archetypes/Archetype_1_Transformation_Strategy.md`. The new skeleton must conform to this structure.

Draft the following skeleton sections. Present each section to the user as drafted. Do not advance to the next section without confirmation. The skeleton is level-agnostic; level-specific and domain-specific content is out of scope and belongs in the domain pack entry, not here.

1. **Section 1 — Purpose and Scope:** boilerplate stating the skeleton applies when the confirmed archetype is this one. State that it loads alongside (a) the active domain pack (declared in `personal/knowledge/Experience_Inventory.md` header), which supplies match criteria, summary content, tag priorities, calibration examples, and de-emphasis; and (b) the level-specific content rules file (`rules/cv/content_rules_leadership.md` for AD+, `rules/cv/content_rules_ic.md` for IC), which supplies voice, register, CCAR bullet construction, impact statement types, tag priority query rules, and competencies count.

2. **Section 2 — Archetype Identity:** expand the Phase 2a differentiator into a level-agnostic description of what makes a role fit this archetype (characteristic contexts, primary deliverable, scope). Note that the archetype applies at both Leadership and IC levels with scope and authority claims adjusting per level rules. State explicitly that specific match criteria and framing language are supplied by the active domain pack.

3. **Section 3 — Structural Rules:** define:
   - Required Section Order: list all CV sections. Ask explicitly whether this archetype includes a Selected Projects section. If yes, specify its position and the rule for inclusion (e.g., "include when entries exist in the Independent & Volunteer Projects inventory section; omit if empty"). If no, state that explicitly so the skeleton documents the omission intentionally.
   - Professional Summary structure: sentence count (3 to 4) and required-element count (4). Do not specify lead-with, do-not-lead-with, register, or required-element content here; those are pack-supplied.
   - Universal framing pattern: challenge or problem, approach, outcome. Note that level-general framing emphasis (strategy/ownership vs contribution/deliverable) is governed by the content rules file and archetype-specific framing language is supplied by the domain pack.
   - Achievement line count rules: 2 lines standard, 3 lines acceptable only for highest-complexity achievements, 4+ never acceptable.

4. **Section 4 — Pack-Supplied Content:** enumerate what the domain pack supplies for this archetype, organized into Leadership and IC sub-sections. Standard list: match criteria; summary framing (lead-with, do-not-lead-with, register, required-element content); inventory tag priorities (High, Medium, Use-if-space, Avoid); achievement framing language and archetype-specific achievement elements; calibration examples (WEAK, STRONG, REFRAME); content to de-emphasize; archetype-specific handling (optional).

5. **Section 5 — Dual-Archetype:** standard boilerplate. Apply primary framing from this archetype's pack content and secondary framing selectively within individual achievements only where both dimensions are genuinely present in the underlying experience. Reference `rules/cv/dual_archetype.md` for the full procedure.

6. **Archetype-specific universal patterns (optional):** Evaluate whether this archetype carries a universal pattern that applies across all domains (not a domain-specific vocabulary or tag list). Examples from existing skeletons: Archetype 2's Technical Credibility pattern; Archetype 4's Compound Query Requirement and Technical Proficiencies expansion. If the pattern is genuinely universal (applies regardless of domain), draft a section describing it. If the pattern is domain-specific (e.g., specific tools or systems), it belongs in the pack entry, not the skeleton; state explicitly that no universal pattern section is needed and why.

Explicitly excluded from skeleton (belongs in the domain pack entry): match criteria language, summary lead-with/do-not-lead-with/register/required-element content, inventory tag priorities, calibration examples, content to de-emphasize, IC vs Leadership differences in framing. If any of this content surfaces during drafting, route it to domain pack notes for use in Phase 5 handoff rather than placing it in the skeleton.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

Perform QC per Global Rules:
- **Standard QC Document Verification**

Sections 1-5 present: confirm each required section (Purpose and Scope, Archetype Identity, Structural Rules, Pack-Supplied Content, Dual-Archetype) is present and populated. A missing or empty section is a blocking issue.

Level-agnostic compliance: confirm no section of the drafted skeleton specifies lead-with, do-not-lead-with, register, required-element content, tag priority tiers, calibration examples, or content-to-de-emphasize. Any of this content appearing in the skeleton is a blocking issue; it belongs in the domain pack entry. The skeleton must be level-agnostic; confirm no Leadership-vs-IC framing differences are written into the skeleton.

Section 1 (Purpose and Scope): confirm references to the active domain pack, level-specific content rules file, and `personal/knowledge/Experience_Inventory.md` header are present.

Section 3 (Structural Rules): confirm Required Section Order lists all CV sections, the Selected Projects question was asked and documented (include with rule, or omit with rationale), Professional Summary sentence and required-element counts are stated, universal framing pattern is named, and achievement line count rules are specified. Confirm the skeleton does not specify summary content (that is pack-supplied).

Section 4 (Pack-Supplied Content): confirm the standard list is present and organized into Leadership and IC sub-sections. This is a contract with the pack entry — any omission means a pack entry will have no instruction to populate that slot.

Section 6 (Archetype-specific universal pattern): confirm the evaluation was performed. If a pattern was drafted, confirm it is genuinely universal (not a domain-specific vocabulary or tag list). If the evaluation concluded no pattern is needed, confirm the rationale is documented.

Canonical pattern compliance: confirm the drafted skeleton structure matches `rules/archetypes/Archetype_1_Transformation_Strategy.md` in section numbering and naming conventions. Deviations without rationale are a blocking issue.

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — Skeleton File Creation and Registry Update

*(Only after Phase 3a and 3b have been explicitly approved)*

1. Read `rules/registry_archetype.md`. Count the existing archetype entries. The new archetype number is N+1. State it explicitly.

2. Derive the archetype name slug: replace spaces with underscores and drop connector words (`&`, `and`) per the canonical convention (e.g., "Transformation & Strategy" → "Transformation_Strategy"). State the target file path:
   - Skeleton: `rules/archetypes/Archetype_<N>_<Name_slug>.md`
   Obtain explicit user confirmation of the path before creating the file.

3. Create the skeleton file at the confirmed path using the Section 1-5 content approved in Phase 3a, plus the optional archetype-specific universal pattern section if one was drafted.

4. Add a new entry to `rules/registry_archetype.md` following the existing format used for Archetypes 1-4: archetype number and name as the section header, Use when summary, Do NOT use when summary, and a `**Skeleton:**` line pointing to the created file path. Do not list pack entry paths in the registry; the registry catalogs skeletons only, and pack entries are discovered via `rules/registry_domain.md` plus the per-archetype naming convention.

5. Confirm both writes (skeleton file and registry update) completed successfully before closing.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control of Phase 4a

Perform QC per Global Rules:
- **Standard QC Document Verification**

Skeleton file: confirm Sections 1-5 (Purpose and Scope, Archetype Identity, Structural Rules, Pack-Supplied Content, Dual-Archetype) are present and match the content approved in Phase 3a. If an archetype-specific universal pattern section was drafted in Phase 3a Step 6, confirm it is present. Any missing approved section is a blocking issue.

File path: confirm the skeleton file was created at `rules/archetypes/Archetype_<N>_<Name_slug>.md` and not at the legacy `rules/Archetype_*.md` path. Files created at the legacy path are a blocking issue and must be moved before closing.

Registry entry: confirm the format matches existing entries in `rules/registry_archetype.md` (section header with archetype number and name, `**Use when:**`, `**Do NOT use when:**`, `**Skeleton:**` line with the file path). Any deviation from the existing format is a blocking issue.

Registry path accuracy: confirm the `**Skeleton:**` path matches the actual created file exactly. Confirm the archetype number is N+1 from the count performed in Phase 4a Step 1. Confirm the name slug matches the approved archetype name.

Level-agnostic compliance: confirm the created skeleton contains no Leadership-only or IC-only content. If a Leadership/IC split is present in the skeleton, that content must be moved to the domain pack entry before closing; the skeleton must be refactored accordingly.

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5.

---

## Phase 5 — Handoff and Next Steps

1. Confirm the skeleton file and the registry entry are verified and in place.

2. State the gap: the new archetype cannot yet be used by `role_evaluation`, `cv_targeted`, or `cv_general` because no domain pack entry exists for it in any domain. Pack entries supply the match criteria, summary framing, tag priorities, calibration examples, and de-emphasis content that CV generation actually consumes.

3. Route to the appropriate pack-creation path. Read the current `**Active Domain:**` value from the header of `personal/knowledge/Experience_Inventory.md` and read `rules/registry_domain.md`:

   - If the user's intent is to stand up a new domain that includes this archetype: direct them to `skills/domain_creation.md`, which will populate pack entries for all registered archetypes in the new domain (including this one) as part of its normal flow.

   - If the user's intent is to use this archetype within an existing domain: a pack entry must be appended to that domain's directory. State the target paths explicitly: `rules/domains/<existing_domain>/archetype<N>_leadership.md` and `rules/domains/<existing_domain>/archetype<N>_ic.md`. Reference the canonical pack-entry pattern at `rules/domains/clinical_development/archetype1_leadership.md` and `archetype1_ic.md`. If any Phase 3 drafting surfaced pack-destined content (match criteria language, summary framing, tag priorities, calibration, de-emphasis) that was excluded from the skeleton, hand that content off as starting material for the pack-entry drafting.

4. Trigger-source next steps after pack entry exists:

   - If triggered from `role_evaluation.md`: after the pack entry for the new archetype exists in the active domain, direct the user to return to `role_evaluation.md` Phase 2a Step 5 and re-evaluate the role against the updated registry.
   - If triggered from `cv_general.md`: after the pack entry exists, direct the user to return to `cv_general.md` Phase 2a Step 1 and re-evaluate the archetype selection against the updated registry.
   - If triggered independently: the archetype skeleton is registered. Pack-entry work remains before the archetype can be used in CV generation.
