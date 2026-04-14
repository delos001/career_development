# Archetype Registry

This file is the authoritative catalog of available CV archetypes. Read this file
to make a preliminary archetype selection. The corresponding skeleton file is the
authority on match criteria and structural rules; load it to confirm and govern.

Do not treat registry summaries as exhaustive. If the preliminary selection is
unclear or borderline between two archetypes, load both skeleton files and apply
the match criteria defined in each.

## Three-Layer Model

Archetype content for CV generation is assembled from three sources:

1. **Archetype skeleton** (`rules/archetypes/Archetype_<N>_<Name>.md`): level-agnostic structural rules, archetype identity, and pack-supplied content placeholders.
2. **Domain pack entry** (`rules/domains/<domain>/archetype<N>_<level>.md`): match criteria, summary framing, tag priorities, calibration examples, and de-emphasis content for the archetype at the specified level within the active domain. The active domain is declared in the Experience Inventory header; the catalog of domains is `rules/registry_domain.md`.
3. **Level content rules** (`rules/cv/content_rules_leadership.md` or `rules/cv/content_rules_ic.md`): voice, register, bullet construction (CCAR), impact statement types, tag priority query rules, competencies count.

Skills load all three for the confirmed archetype, level, and active domain at Phase 2a of CV generation.

---

## Archetype 1: Transformation & Strategy

**Use when:** The role centers on enterprise-level organizational change, building
new capabilities from greenfield, or operating model redesign at scale. The primary
deliverable is an organizational capability or structural change; not a product,
process, or technology.

**Do NOT use when:** The role is primarily about process standardization or
steady-state operational efficiency, technology platform ownership, or data and
analytics capability development. If the role optimizes an existing model rather
than building or transforming one, this archetype is likely wrong.

**Skeleton:** `rules/archetypes/Archetype_1_Transformation_Strategy.md`

---

## Archetype 2: Data & Analytics

**Use when:** The role centers on data strategy, data governance, analytics
capability development, or analytics operating model design. The primary output
is a governed data or analytics system, process, or capability; not a technology
platform or a process improvement program.

**Do NOT use when:** The role primarily owns a technology platform (Archetype 4),
or where data is incidental to process standardization (Archetype 3). Flag if the
role is a hands-on IC analytics or data science role below target level; this may
fall outside scope and should be noted in the fit assessment.

**Skeleton:** `rules/archetypes/Archetype_2_Data_Analytics.md`

---

## Archetype 3: Process & Operations

**Use when:** The role centers on process design, standardization, or
harmonization; operational efficiency or Lean/Six Sigma leadership; SOP
governance, inspection readiness, or cross-functional process ownership with
quality or risk emphasis.

**Do NOT use when:** The role centers on technology platform ownership, data
strategy, or organizational transformation at enterprise scope. Process
improvement in support of a larger transformation belongs to Archetype 1 unless
process is the primary subject of the role.

**Skeleton:** `rules/archetypes/Archetype_3_Process_Operations.md`

---

## Archetype 4: Platform & Technology

**Use when:** The role centers on technology strategy for clinical or data
platforms, platform implementation leadership, system integration, or vendor and
tool ecosystem management. Technology is the primary subject the role owns and
is accountable for.

**Do NOT use when:** Technology is a supporting tool for data governance
(Archetype 2) or process improvement (Archetype 3). If the role is primarily
about driving organizational adoption of a technology change rather than owning
the technology itself, verify against Archetype 1 first.

**Skeleton:** `rules/archetypes/Archetype_4_Platform_Technology.md`

---

## Adding New Archetypes

Invoke `skills/archetype_creation.md`. Do not add entries here directly. The
creation skill produces a level-agnostic skeleton and registers it atomically.
Domain-specific content for the new archetype is added separately by
`skills/domain_creation.md` or by appending a pack entry to an existing domain
directory.
