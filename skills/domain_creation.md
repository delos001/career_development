# Domain Creation Skill

## Objective

Create a new career domain pack so that `role_evaluation`, `cv_targeted`, and `cv_general` can operate on roles outside the currently covered domains. Produces one domain header file (`rules/domains/<slug>/domain.md`) and one pack entry per registered archetype and level (`rules/domains/<slug>/archetype<N>_leadership.md` and `archetype<N>_ic.md`), plus a catalog entry in `rules/registry_domain.md`.

Scope boundary: this skill does not create or modify archetypes. Archetype skeletons are governed by `skills/archetype_creation.md`. This skill populates pack content for every archetype that already exists in `rules/registry_archetype.md`. If the user needs a new archetype, that work must precede this skill.

Activation of a new domain happens by user edit of the `**Active Domain:**` pointer in `personal/knowledge/Experience_Inventory.md`; this skill does not flip the pointer automatically.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b, 5a, 5b, 6

---

## Phase 1a — Trigger and Scope Motivation

*(No documents loaded in this phase)*

1. Identify the trigger source and state it explicitly:
   - **Triggered from a role evaluation domain scope mismatch:** the job description and a stated domain mismatch should be available in the current session. Confirm both are present.
   - **Triggered from a user career pivot:** the user is preparing to represent experience in a new functional or industry domain.
   - **Triggered independently:** the user is building domain coverage for another person who will use this repo (see "multiple testers" goal in README).

2. Collect and state explicitly:
   - Proposed domain name (human-readable, e.g., "Medical Affairs", "Product Management")
   - Proposed domain slug (lowercase, underscores, no spaces; e.g., `medical_affairs`, `product_management`)
   - Target user (self, another tester, or unspecified generalization)
   - Motivation (why this domain is needed and what roles it must cover)

3. Confirm all four items before closing this phase. Do not proceed until the user has explicitly agreed to the name, slug, and scope statement.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 1b.

---

## Phase 1b — Boundary Validation

*(Only after Phase 1a has been explicitly approved)*

1. Load `rules/registry_domain.md`. Confirm it loaded completely.

2. For each domain already in the registry, evaluate whether the proposed domain overlaps:
   - Does the proposed scope fall inside an existing domain's "Use when" criteria? If yes, the new domain is likely unnecessary; state specifically which existing domain covers it and halt.
   - Does the proposed scope partially overlap with an existing domain? Document the overlap explicitly; the boundary must be defensible in Phase 3a's pack selection criteria.

3. If the proposed domain is fully covered by an existing one, do not proceed. State the finding. Direct the user to activate the existing domain rather than create a new one.

4. If the proposed domain is genuinely new, document for each existing domain why it does not cover the proposed scope. This is the evidence base that the new domain is needed.

5. Load `rules/registry_archetype.md`. Confirm it loaded completely. State every registered archetype by number and name. Every registered archetype will receive two pack entries (leadership and IC) in Phase 4a. Confirm with the user that the proposed domain is intended to cover all currently registered archetypes; if the user intends to exclude any archetype, state the exclusion explicitly and record the rationale (a pack entry will still be created for consistency, but with a documented note that the archetype is not expected to apply within this domain).

**Phase 1b Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Domain Research

*(Only after Phase 1b has been explicitly approved)*

This phase establishes the vocabulary, conventions, and framing that will govern the domain pack. The pack must reflect current practitioner usage in the domain, not assumed or generic language. Research is mandatory; do not skip.

1. Propose research sources and obtain user alignment before executing any research. Present:
   - Target sources by type: practitioner publications, industry associations, representative job descriptions, authoritative reference documents, regulatory or standards bodies if applicable
   - Specific publications, associations, or URLs the user wants included (user-supplied)
   - Specific publications, associations, or URLs the user wants excluded (user-supplied)
   - Research depth: how many representative job descriptions to review; how many practitioner sources to consult

   Obtain explicit approval of the research plan before executing.

2. Execute the agreed research plan using web search and any user-supplied materials. Record each source consulted (URL or publication name and date) as research is performed. These sources will be written into the domain header in Phase 3a.

3. Synthesize research findings into the following outputs (draft only; formal drafting occurs in Phase 3a):
   - Characteristic terms and acronyms used in this domain
   - Regulatory, standards, or compliance context (if applicable)
   - Framing conventions: what practitioners emphasize; what reads as outsider language
   - Metric conventions: what outcomes the domain measures against (cycles, units, revenue, adoption, etc.)
   - Career progression patterns: how roles at Leadership and IC levels are typically described

4. Present the synthesis to the user. Flag any area where research was inconclusive or where practitioner usage diverges materially from expectations. Obtain user confirmation or correction on each synthesized point.

**Phase 2a Closing:** Follow Standard Phase Closing. Update any session log with research sources consulted and synthesis points confirmed. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Research plan approval:** Confirm the research plan was presented and explicitly approved in Step 1 before any research was executed. If approval is not documented, flag as a blocking issue.

**Source traceability:** Confirm every source consulted was recorded with enough detail for the user to revisit (URL or publication name plus date). Unrecorded sources are a blocking issue.

**Practitioner grounding:** Confirm at least one of the consulted sources is a current practitioner publication, industry association, or representative job description in the domain (not a generic reference or textbook). A research pass that relies only on generic references is insufficient grounding for the pack and is a blocking issue.

**Synthesis completeness:** Confirm the synthesis covers all five output areas listed in Step 3. Missing output areas are a blocking issue.

**User confirmation of synthesis:** Confirm each synthesis point received explicit confirmation or correction. Unconfirmed points must be revisited before proceeding.

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Domain Header Design

*(Only after Phase 2a and 2b have been explicitly approved)*

Read the canonical domain header pattern before drafting: `rules/domains/clinical_development/domain.md`. The new domain header must conform to this structure.

Draft the following sections. Present each to the user as drafted. Do not advance to the next section without confirmation.

1. **Header:** domain name, version (1.0 for new creation), last-updated date (current date in YYYY-MM-DD), and a one-line list of archetypes to be covered (all archetypes from `rules/registry_archetype.md`).

2. **Scope statement:** two to four sentences describing the careers and role categories this domain covers. State industry, function, and the dividing line with adjacent domains.

3. **Section 1 — Tag Taxonomy:** define allowed values for each required dimension:
   - **Capability:** pipe-separated list of values characteristic of this domain's functional skills; aim for 12 to 16 values; draw from the Phase 2a research, not from other domains
   - **Role Level:** pipe-separated list; typically IC, Manager, Senior Manager, Director, Senior Director, VP; adjust if the domain has materially different level conventions
   - **Org Context:** pipe-separated list; typically Greenfield, Scaling, Turnaround, Mature/Enterprise, Independent, Volunteer; adjust only if the domain has materially different context conventions
   - **Outcome (OPTIONAL):** pipe-separated list of organizational-outcome categories this domain measures against
   - **Org Type (career breadth):** pipe-separated list of organization types where careers in this domain are pursued

   Include the taxonomy rules paragraph verbatim (from the canonical pattern): Capability, Role Level, and Org Context required on every entry; Outcome optional; reject forced outcomes; multiple Capability and Outcome values pipe-separated; single Role Level and Org Context per entry.

4. **Section 2 — Domain Vocabulary:** characteristic terms and acronyms (drawn from Phase 2a research), framing conventions (what practitioners emphasize; what reads as outsider language), metric conventions (what outcomes the domain measures against).

5. **Section 3 — Pack Selection Criteria:** "Activate this pack when" and "Do NOT activate this pack when" statements. Use the Phase 1b overlap findings to define the boundary with adjacent domains explicitly.

6. **Section 4 — Pack Files:** list every pack entry path that will be created in Phase 4a (`archetype<N>_leadership.md` and `archetype<N>_ic.md` for every N in the archetype registry).

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Slug compliance:** Confirm the domain slug from Phase 1a is lowercase with underscores and no spaces. Non-compliance is a blocking issue.

**Scope distinctness:** Confirm the Section 3 pack selection criteria explicitly differentiate the new domain from every existing domain in `rules/registry_domain.md`. A missing boundary statement for any existing domain is a blocking issue.

**Taxonomy grounding:** Confirm the Capability values in Section 1 are drawn from Phase 2a research, not copied from other domains. A domain that reuses another domain's Capability list verbatim has no independent grounding and is a blocking issue.

**Taxonomy rules text:** Confirm the required taxonomy rules paragraph (Capability/Role Level/Org Context required, Outcome optional, reject forced outcomes, pipe-separated rules) is present.

**Vocabulary grounding:** Confirm Section 2 vocabulary and framing conventions are drawn from Phase 2a research. Generic or textbook language without practitioner grounding is a blocking issue.

**Pack file completeness:** Confirm Section 4 lists a pack entry for every archetype registered in `rules/registry_archetype.md` at both levels. Missing pack entries are a blocking issue.

**Canonical pattern compliance:** Confirm the drafted header conforms to `rules/domains/clinical_development/domain.md` in section numbering and naming conventions. Deviations without rationale are a blocking issue.

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — Per-Archetype Pack Entry Drafting

*(Only after Phase 3a and 3b have been explicitly approved)*

Read the canonical pack entry pattern before drafting: `rules/domains/clinical_development/archetype1_leadership.md` and `rules/domains/clinical_development/archetype1_ic.md`. Every pack entry must conform to this structure.

Iterate through every registered archetype. For each archetype, draft the Leadership entry first, then the IC entry. Present each entry to the user as drafted. Do not advance to the next entry without confirmation.

For each pack entry, draft all of the following sections:

1. **Header:** `# <Domain Name>: Archetype <N> <Archetype Name> (<Level>)` followed by a one-paragraph statement that the file is pack content for this archetype at this level within the domain, and that it loads alongside the archetype skeleton and level rules file. Cite the three paths explicitly.

2. **Match criteria:** bullet list of role characteristics that activate this archetype at this level within the domain. Include cross-archetype boundary verification notes drawn from the archetype skeleton's identity section and the Phase 1b boundary findings.

3. **Summary framing:**
   - Lead with: what the professional summary must open with (domain-grounded)
   - Do NOT lead with: what must be absent from the opening
   - Register: the voice and positioning (leader/IC + archetype identity within the domain)
   - Required-element content: the four content elements every summary must include for this archetype at this level within this domain

4. **Inventory tag priorities:** drawn from the domain's tag taxonomy in Section 1 of `domain.md`. Organize in four tiers:
   - High priority (must be represented; define minimum count)
   - Medium priority (include where space permits)
   - Use if space permits
   - Avoid (with reason)

   Tag values must come from the domain's taxonomy, not from another domain's taxonomy or from invented vocabulary. Reject any tag value not present in `domain.md` Section 1.

5. **Achievement framing language:** the structural arc every achievement must follow, plus archetype-specific achievement elements if the archetype skeleton calls for them (see the Pack-Supplied Content section of the skeleton for the contract).

6. **Calibration examples:** at least two examples, one WEAK and one STRONG. A REFRAME example is recommended when the distinction between archetypes is subtle within the domain. Examples must use domain vocabulary from Phase 2a, not generic or other-domain language.

7. **Content to de-emphasize:** specific items to minimize or exclude at this archetype and level, with a brief reason for each.

**IC variant notes:** when drafting the IC entry for an archetype, apply the level conventions from `rules/cv/content_rules_ic.md`: no ownership-framed language, contribution-level scope, no org-scope authority claims. Summary framing, tag priorities, and calibration examples must reflect the IC level; do not mirror the Leadership entry verbatim with the header swapped.

**Excluded archetype handling:** if the user flagged any archetype for exclusion in Phase 1b Step 5, still draft a pack entry. The entry body should be a single paragraph stating the exclusion rationale and referring the user to other archetypes within the domain. This preserves the pack's structural completeness so CV skills do not fail on missing files.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control of Phase 4a

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Pack entry completeness:** Confirm every archetype in `rules/registry_archetype.md` has both a Leadership and an IC entry drafted. Any missing entry is a blocking issue.

**Section completeness per entry:** For each drafted entry, confirm the seven sections (Header, Match criteria, Summary framing, Inventory tag priorities, Achievement framing language, Calibration examples, Content to de-emphasize) are present. A missing section in any entry is a blocking issue.

**Taxonomy compliance:** For every tag value cited in any pack entry's Inventory tag priorities section, confirm the value exists in Section 1 of the drafted `domain.md`. A tag value not present in the domain's taxonomy is a blocking issue; either add the value to the taxonomy (and re-confirm the taxonomy with the user) or remove it from the pack entry.

**IC-Leadership differentiation:** For every archetype, confirm the IC entry is not a verbatim copy of the Leadership entry with header changes only. Summary framing, tag priorities, and calibration must reflect IC-level differences. A near-identical IC entry is a blocking issue.

**Domain vocabulary coherence:** For each entry, confirm summary framing and calibration examples use vocabulary consistent with Phase 2a research and `domain.md` Section 2. An entry that uses foreign-domain vocabulary (for instance, clinical-development terms in a product-management pack) is a blocking issue.

**Archetype skeleton contract compliance:** For each entry, confirm the sections align with the "Pack-Supplied Content" enumeration in the corresponding archetype skeleton. If the skeleton lists archetype-specific achievement elements, confirm those elements are addressed in Section 5 of the entry.

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5a.

---

## Phase 5a — Atomic File Creation and Registration

*(Only after Phase 4a and 4b have been explicitly approved)*

All file writes in this phase must succeed together. If any write fails, halt and report the failure to the user before any further action. Do not leave a partially populated domain directory or a stranded registry entry.

1. Confirm the target directory path: `rules/domains/<slug>/`. If the directory already exists, halt and surface the conflict; do not overwrite an existing domain without explicit user direction.

2. Present the full list of files to be written and obtain explicit user confirmation of the list before any write occurs:
   - `rules/domains/<slug>/domain.md`
   - `rules/domains/<slug>/archetype<N>_leadership.md` for every archetype
   - `rules/domains/<slug>/archetype<N>_ic.md` for every archetype
   - One entry to be appended to `rules/registry_domain.md`

3. Create the domain directory.

4. Write `domain.md` with the Phase 3a content.

5. Write each pack entry file with the Phase 4a content. Iterate through all archetypes at both levels.

6. Append the new domain entry to `rules/registry_domain.md`. Follow the existing format used for Clinical Development: domain name as section header, scope statement, directory path, header file, archetypes covered, pack files naming pattern, "Use when" summary, "Do NOT use when" summary.

7. Confirm every file write completed successfully and the registry update is in place.

**Phase 5a Closing:** Follow Standard Phase Closing. Next phase is Phase 5b.

---

## Phase 5b — Quality Control of Phase 5a

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Directory existence:** Confirm `rules/domains/<slug>/` exists and contains all planned files.

**File count:** Confirm the file count matches: one `domain.md` plus two pack entries per archetype in `rules/registry_archetype.md`. A mismatch is a blocking issue.

**Content match:** For each written file, confirm the content matches what was approved in Phase 3a (header) or Phase 4a (pack entries). Deviations from approved content are a blocking issue.

**Registry entry:** Confirm the `rules/registry_domain.md` entry matches the existing format used for other domains. Confirm directory path, header file, archetypes covered, and pack files pattern are correct. Any deviation is a blocking issue.

**No inventory header change:** Confirm `personal/knowledge/Experience_Inventory.md` Active Domain pointer was not changed by this skill. Domain activation is a user decision made separately; the skill must not flip the pointer automatically.

**Phase 5b Closing:** Follow Standard Phase Closing. Next phase is Phase 6.

---

## Phase 6 — Handoff

1. Confirm the domain is registered, the pack is complete, and the Active Domain pointer in `personal/knowledge/Experience_Inventory.md` is unchanged.

2. State the activation step explicitly to the user: to use the new domain, edit the `**Active Domain:**` line in the header of `personal/knowledge/Experience_Inventory.md` to the new slug. Any subsequent `role_evaluation`, `cv_targeted`, or `cv_general` session will load the new domain automatically.

3. State the inventory-migration implication: if the user's existing Experience_Inventory entries carry tags that do not exist in the new domain's taxonomy, those entries will fail validation. If a domain switch is planned, recommend an inventory review pass (standalone `source_document_update_adhoc` session, or a dedicated migration) before the switch.

4. Trigger-source next steps:
   - If triggered from a role evaluation domain scope mismatch: the user can now activate the new domain and re-run `role_evaluation` against the role.
   - If triggered from a career pivot: recommend source document review before the switch (see Step 3).
   - If triggered independently: state that the domain is available for activation whenever needed.
