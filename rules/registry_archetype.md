# Archetype Registry

Authoritative catalog of available CV archetypes. Read this file to make a preliminary archetype selection. The corresponding archetype file is authoritative on match criteria and framing; load it to confirm and govern.

Do not treat registry summaries as exhaustive. If the preliminary selection is unclear or borderline between two archetypes, load both archetype files and apply the match criteria defined in each.

---

## Archetype 1: Transformation & Strategy

**Use when:** the role centers on enterprise-level organizational change, building new capabilities from greenfield, or operating model redesign at scale. Primary deliverable is an organizational capability or structural change, not a product, process, or technology.

**Do NOT use when:** the role is primarily about process standardization, steady-state operational efficiency, technology platform ownership, or data and analytics capability development. If the role optimizes an existing model rather than building or transforming one, this archetype is likely wrong.

**File:** `rules/archetypes/Archetype_1_Transformation_Strategy.md`

---

## Archetype 2: Data & Analytics

**Use when:** the role centers on data strategy, data governance, analytics capability development, or analytics operating model design. Primary output is a governed data or analytics system, process, or capability.

**Do NOT use when:** the role primarily owns a technology platform (Archetype 4), or where data is incidental to process standardization (Archetype 3). Flag if the role is a hands-on IC analytics or data science role below target level.

**File:** `rules/archetypes/Archetype_2_Data_Analytics.md`

---

## Archetype 3: Process & Operations

**Use when:** the role centers on process design, standardization, or harmonization; operational efficiency or Lean/Six Sigma leadership; SOP governance, inspection readiness, or cross-functional process ownership with quality or risk emphasis.

**Do NOT use when:** the role centers on technology platform ownership, data strategy, or organizational transformation at enterprise scope. Process improvement in support of a larger transformation belongs to Archetype 1 unless process is the primary subject.

**File:** `rules/archetypes/Archetype_3_Process_Operations.md`

---

## Archetype 4: Platform & Technology

**Use when:** the role centers on technology strategy for domain-relevant platforms, platform implementation leadership, system integration, or vendor and tool ecosystem management. Technology is the primary subject the role owns and is accountable for.

**Do NOT use when:** technology is a supporting tool for data governance (Archetype 2) or process improvement (Archetype 3). If the role is primarily about driving organizational adoption of a technology change rather than owning the technology itself, verify against Archetype 1 first.

**File:** `rules/archetypes/Archetype_4_Platform_Technology.md`

---

## Adding New Archetypes

Invoke `skills/archetype_creation.md`. Do not add entries here directly. The creation skill produces the archetype file and registers it atomically.
