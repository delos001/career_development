# Archetype Creation Skill

## Objective

Create a new role archetype when no existing archetype in `rules/registry_archetype.md`
serves the target role. Produces two conformant archetype files (leadership and IC
variants) and a registry entry. Output must integrate with the existing role_evaluation.md
and cv_general.md workflows without modification to any existing files other than the registry.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 1b, 2a, 3a, 4a

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

## Phase 3a — Content Rules Design

*(Only after Phase 2a and 2b have been explicitly approved)*

Draft the following required sections. Present each section to the user as it is
drafted. Do not advance to the next section without confirmation.

1. **Section 1 — Purpose and Scope:** state when to apply this document, that it
   is a CV generation instruction set for Jason Delosh, and the dual-archetype rule
   (apply primary framing from this document; secondary framing selectively within
   individual achievements only where both dimensions are genuinely present).

2. **Section 2 — Archetype Match Criteria:** expand the "Use when" criteria from
   Phase 2a into full match criteria, including cross-archetype boundary notes drawn
   from the Phase 2a exclusions.

3. **Section 3 — Summary Framing Rules:** define all of the following:
   - Lead with (what the summary must open with)
   - Do NOT lead with (what must be absent from the opening)
   - Register (the voice and positioning of the candidate)
   - Length (3 to 4 sentences)
   - 4 required elements that must all be present in every summary

4. **Section 4 — Required Section Order:** list all CV sections in order.
   Specify Core Competencies item count and priority categories. Note the placement
   and visual weight of Technical Proficiencies for this archetype.

   Ask explicitly: does this archetype include a Selected Projects section? If yes,
   state its position in the section order and the selection criteria governing which
   Independent & Volunteer Projects inventory entries to include. If no, state that
   explicitly so the archetype file documents the omission intentionally.

5. **Section 5 — Inventory Tag Priorities:** identify tags from the Experience
   Inventory taxonomy in four tiers:
   - High Priority: must be represented (define minimum achievement count)
   - Medium Priority: include where space permits
   - Use If Space Permits
   - Avoid for This Archetype (with reason)
   If tag names are uncertain, load `knowledge/Experience_Inventory.md` to verify
   the actual taxonomy before drafting this section.

6. **Section 6 — Achievement Selection and Framing Rules:** define:
   - 3 selection criteria that must all be satisfied for an achievement to qualify
   - Required framing pattern (the structural arc every achievement must follow)
   - Transformation Achievement Elements if applicable (4-element requirements for
     the most prominent achievements)
   - At least 2 calibration examples: one weak, one strong; a reframe example is
     recommended where the distinction is subtle

7. **Section 7 — Content to De-emphasize:** 3-5 specific items to minimize or
   exclude, with a brief reason for each.

8. **Conditional sections:** Evaluate whether this archetype requires either of the
   following. If yes, draft the section and number it sequentially after Section 7.
   If no, state explicitly that it is not needed and why.

   - **Inventory Coverage Notice:** Required when the Experience Inventory does not
     have a dedicated capability tag for this archetype's primary domain and compound
     tag queries are needed. See Archetype 4 (Platform & Technology) for an example.
   - **Technical Proficiencies handling:** Required when this archetype needs
     expanded or different treatment of the Technical Proficiencies CV section beyond
     the default "condensed, minimal visual weight." See Archetype 2 (Data &
     Analytics) and Archetype 4 (Platform & Technology) for examples.

9. **IC variant differences:** define how the IC file differs from the leadership
   file in section order, tag priorities, or framing emphasis. IC files must
   reference `rules/cv/content_rules_ic.md` in their Purpose and Scope section.
   If there are no meaningful differences, state that explicitly and note that the
   IC file will mirror the leadership file with role-level language adjusted.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

Perform QC per Global Rules:
- **Standard QC Document Verification**

Sections 1-7: confirm each required section is present and populated. A missing or
empty section is a blocking issue.

Section 3 (Summary Framing): confirm Lead with, Do NOT lead with, Register, Length,
and 4 required elements are all defined. Any missing element is a blocking issue.

Section 4 (Section Order): confirm all sections are listed in order. Confirm
Core Competencies item count is specified. Confirm the Selected Projects question
was asked and the answer — include or omit — is explicitly documented in the archetype.

Section 5 (Inventory Tags): confirm all four tiers are present. Confirm tag names
match the actual Experience Inventory taxonomy -- invented tags are a blocking issue.
Confirm High Priority tier defines a minimum achievement count.

Section 6 (Achievement Selection): confirm 3 selection criteria are defined. Confirm
required framing pattern is stated. Confirm at least 2 calibration examples are present.

Section 7 (De-emphasize): confirm items are specific to this archetype, not generic
advice that would apply to any archetype.

Conditional sections: if an Inventory Coverage Notice or Technical Proficiencies
handling section was included, confirm it is justified by the archetype's specific
needs. If either was evaluated and deemed unnecessary, confirm that determination
is documented explicitly in the archetype file.

IC variant: confirm differences are defined. If the IC file mirrors the leadership
file, confirm that was explicitly stated and approved. Confirm the reference to
`rules/cv/content_rules_ic.md` is included.

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — File Creation and Registry Update

*(Only after Phase 3a and 3b have been explicitly approved)*

1. Read `rules/registry_archetype.md`. Count the existing archetype entries.
   The new archetype number is N+1. State it explicitly.

2. Derive the archetype name slug: replace spaces with underscores in the approved
   archetype name. State the two target file paths:
   - Leadership: `rules/Archetype_[N]_[Name].md`
   - IC: `rules/Archetype_[N]_IC_[Name].md`
   Obtain explicit user confirmation of both paths before creating any files.

3. Create the leadership archetype file at the confirmed path using the content
   approved in Phase 3a.

4. Create the IC archetype file at the confirmed path. Apply IC variant differences
   defined in Phase 3a Step 8. Ensure the Purpose and Scope section references
   `rules/cv/content_rules_ic.md`.

5. Add a new entry to `rules/registry_archetype.md` following the existing format:
   archetype number and name as the section header, Use when summary, Do NOT use
   when summary, and both file paths under Files.

6. Confirm all three writes completed successfully before closing.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control of Phase 4a

Perform QC per Global Rules:
- **Standard QC Document Verification**

Leadership file: confirm all 7 sections are present and match the content approved
in Phase 3a. Any missing section is a blocking issue.

IC file: confirm all 7 sections are present. Confirm IC-specific guidance is present
and is not a verbatim copy of the leadership file where differences were defined.
Confirm `rules/cv/content_rules_ic.md` is referenced in the Purpose and Scope section.

Registry entry: confirm the format matches existing entries exactly (section header,
Use when, Do NOT use when, Files with both paths listed). Any deviation from the
existing format is a blocking issue.

File paths in registry: confirm they match the actual created files exactly. Confirm
the archetype number is N+1 from the count performed in Phase 4a Step 1. Confirm
the name slug matches the approved archetype name.

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5.

---

## Phase 5 — Handoff

1. Confirm both archetype files and the registry entry are verified and in place.

2. If triggered from role_evaluation.md: the new archetype is now available. Direct the user to return to role_evaluation.md Phase 2a Step 5 and re-evaluate the role against the updated registry. The new archetype should now satisfy the match criteria for the role.
   If triggered from cv_general.md: direct the user to return to cv_general.md Phase 2a Step 1 and re-evaluate the archetype selection against the updated registry.

3. If triggered independently: the new archetype is available for future sessions. No further action required.
