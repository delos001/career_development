# Domain Creation Skill

## Objective

Create a new career domain so `role_evaluation`, `cv_targeted`, and `cv_general` can operate on roles outside currently covered domains. Produces a single flat file at `rules/domains/<slug>.md` and a catalog entry in `rules/registry_domain.md`.

Scope boundary: this skill does not create or modify archetypes. Archetype files are governed by `skills/archetype_creation.md` and are already domain-agnostic. The domain file supplies tag taxonomy, vocabulary, selection criteria, tech stack content, and per-archetype calibration examples that archetype files reference generically.

Activation happens by user edit of the `**Active Domain:**` pointer in `personal/knowledge/Experience_Inventory.md`; this skill does not flip the pointer automatically.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b, 5

---

## Phase 1a — Trigger and Scope Motivation

*(No documents loaded in this phase)*

1. Identify the trigger source and state it explicitly:
   - **From a role evaluation domain scope mismatch:** the JD and stated mismatch should be available. Confirm both.
   - **From a user career pivot:** the user is preparing to represent experience in a new functional or industry domain.
   - **Triggered independently:** the user is building coverage for another person who will use this repo.

2. Collect and state:
   - Proposed domain name (human-readable, e.g., "Medical Affairs")
   - Proposed domain slug (lowercase, underscores, no spaces)
   - Target user (self, another tester, or generalization)
   - Motivation (why this domain is needed, what roles it must cover)

3. Confirm all four items before closing.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 1b.

---

## Phase 1b — Boundary Validation

*(Only after Phase 1a has been explicitly approved)*

1. Load `rules/registry_domain.md`. Confirm it loaded completely.

2. For each existing domain, evaluate overlap with the proposed domain:
   - Does the proposed scope fall inside an existing domain's "Use when" criteria? If yes, state which and halt.
   - Does it partially overlap? Document the overlap; the boundary must be defensible in Phase 3a.

3. If fully covered by an existing domain, do not proceed. Direct the user to activate the existing domain.

4. If genuinely new, document for each existing domain why it does not cover the proposed scope. Evidence base that the new domain is needed.

5. Load `rules/registry_archetype.md`. State every registered archetype by number and name. Confirm the proposed domain is intended to cover all archetypes with calibration examples; if the user intends to exclude any archetype, record the rationale (a calibration slot will still be present with a documented note).

**Phase 1b Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Domain Research

*(Only after Phase 1b has been explicitly approved)*

Research is mandatory. The domain file must reflect current practitioner usage, not assumed or generic language.

1. Propose research sources and obtain user alignment before executing:
   - Target source types: practitioner publications, industry associations, representative job descriptions, authoritative references, regulatory or standards bodies if applicable
   - Specific sources to include (user-supplied)
   - Specific sources to exclude (user-supplied)
   - Research depth: how many representative JDs; how many practitioner sources

   Obtain explicit approval of the research plan.

2. Execute the plan using web search and any user-supplied materials. Record each source consulted (URL or publication name and date); these go into the domain file header.

3. Synthesize research into:
   - Characteristic terms and acronyms
   - Regulatory, standards, or compliance context (if applicable)
   - Framing conventions (what practitioners emphasize; what reads as outsider language)
   - Metric conventions (what outcomes the domain measures against)
   - Tech stack and tools (systems, languages, platforms relevant to the domain)
   - Career progression patterns

4. Present the synthesis. Flag any inconclusive areas or divergence from expectations. Obtain confirmation on each point.

**Phase 2a Closing:** Follow Standard Phase Closing. Update any session log with sources and confirmed synthesis. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Perform QC per Global Rules:
- **Standard QC Document Verification**

- **Research plan approval** documented before execution.
- **Source traceability:** every source recorded with enough detail to revisit.
- **Practitioner grounding:** at least one source is a current practitioner publication, industry association, or representative job description.
- **Synthesis completeness:** all output areas covered.
- **User confirmation** on each synthesis point.

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Domain File Design

*(Only after Phase 2a and 2b have been explicitly approved)*

Read the canonical pattern before drafting: `rules/domains/clinical_development.md`. The new domain file must conform to this structure.

Draft the following. Present each section to the user as drafted. Do not advance without confirmation.

1. **Header:** domain name, version (1.0), last-updated (YYYY-MM-DD), archetypes covered (all from the registry).

2. **Scope statement:** 2-4 sentences describing the careers and role categories covered. State industry, function, and dividing lines with adjacent domains.

3. **Section 1 — Tag Taxonomy:**
   - **Capability:** pipe-separated list of 12-16 values characteristic of this domain, drawn from Phase 2a research
   - **Role Level:** pipe-separated list (typically IC | Manager | Senior Manager | Director | Senior Director | VP; adjust if the domain differs)
   - **Org Context:** pipe-separated list (typically Greenfield | Scaling | Turnaround | Mature/Enterprise | Independent | Volunteer)
   - **Outcome (OPTIONAL):** pipe-separated list of outcome categories this domain measures against
   - **Org Type (career breadth):** pipe-separated list of organization types where careers in this domain are pursued

   Include the taxonomy rules paragraph (Capability/Role Level/Org Context required per entry; Outcome optional; reject forced outcomes; pipe-separated when multiple Capability or Outcome values apply; single Role Level and Org Context per entry).

4. **Section 2 — Domain Vocabulary:** characteristic terms and acronyms; framing conventions (what to emphasize, what reads as outsider language); metric conventions; scale signals (what establishes seniority in this domain).

5. **Section 3 — Pack Selection Criteria:** "Use when" and "Do NOT use when" statements. Use Phase 1b overlap findings to define boundaries with adjacent domains explicitly.

6. **Section 4 — Technical Proficiencies Content:** the tech stack list used by archetypes that foreground technology or analytics (Archetypes 2 and 4). Organize into subsections (systems, languages, frameworks, environments, tools) appropriate to the domain. State explicitly: "List format only. Exclude proficiency levels, first-appearance dates, and application narratives." If the domain has no distinct tech stack (e.g., pure advisory domains), state so and provide a minimal baseline.

7. **Section 5 — Archetype Calibration Reference:** for every archetype in `rules/registry_archetype.md`, one STRONG calibration example in Leadership voice using domain vocabulary, illustrating the archetype's framing pattern. Pull pattern shape from each archetype file (`rules/archetypes/Archetype_<N>_<Name>.md`) but express in this domain's vocabulary. For any archetype flagged for exclusion in Phase 1b, include a one-sentence note explaining why the archetype does not apply in this domain.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

Perform QC per Global Rules:
- **Standard QC Document Verification**

- **Slug compliance:** lowercase, underscores, no spaces.
- **Scope distinctness:** Section 3 differentiates the new domain from every existing domain in `rules/registry_domain.md`.
- **Taxonomy grounding:** Section 1 Capability values drawn from Phase 2a research, not copied from other domains.
- **Taxonomy rules text present:** the required paragraph about required vs optional dimensions.
- **Vocabulary grounding:** Section 2 based on Phase 2a research, not generic language.
- **Tech stack grounding:** Section 4 list is domain-relevant and sourced from research.
- **Calibration coverage:** Section 5 has a calibration entry for every registered archetype (STRONG example or exclusion note). Examples use domain vocabulary from Phase 2a, not foreign-domain language.
- **Archetype pattern compliance:** each calibration example illustrates the framing pattern defined in the corresponding archetype file. Examples that violate the archetype's pattern are blocking issues.
- **Canonical pattern compliance:** section numbering and naming match `rules/domains/clinical_development.md`.

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — File Creation and Registration

*(Only after Phase 3a and 3b have been explicitly approved)*

Both file writes must succeed together. If either fails, halt and report.

1. Confirm the target file path: `rules/domains/<slug>.md`. If a file already exists at that path, halt and surface the conflict; do not overwrite.

2. Present the full list of changes and obtain explicit confirmation:
   - Create `rules/domains/<slug>.md`
   - Append one entry to `rules/registry_domain.md`

3. Write the domain file with Phase 3a content.

4. Append the new domain entry to `rules/registry_domain.md`. Follow the existing format: domain name as section header, scope statement, file path, archetypes covered, Use when summary, Do NOT use when summary.

5. Confirm both writes completed before closing.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control of Phase 4a

Perform QC per Global Rules:
- **Standard QC Document Verification**

- **File exists** at `rules/domains/<slug>.md`; not at any legacy folder path.
- **Content match:** file content matches Phase 3a approved draft.
- **Registry entry:** matches the existing format; file path, archetypes covered, selection criteria all correct.
- **No inventory header change:** `personal/knowledge/Experience_Inventory.md` Active Domain pointer was not changed by this skill.

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5.

---

## Phase 5 — Handoff

1. Confirm the domain is registered and the Active Domain pointer is unchanged.

2. State the activation step: to use the new domain, edit the `**Active Domain:**` line in the header of `personal/knowledge/Experience_Inventory.md` to the new slug. Any subsequent `role_evaluation`, `cv_targeted`, or `cv_general` session will load the new domain automatically.

3. State the inventory-migration implication: if existing Experience_Inventory entries carry tags that do not exist in the new domain's taxonomy, those entries will fail validation. If a domain switch is planned, recommend an inventory review pass before the switch.

4. Trigger-source next steps:
   - From a role evaluation domain scope mismatch: the user can activate the new domain and re-run `role_evaluation`.
   - From a career pivot: recommend source document review before the switch.
   - Triggered independently: the domain is available for activation whenever needed.
