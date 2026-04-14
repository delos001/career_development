# Domain Registry

Authoritative catalog of available domain packs. Read this file to select the active domain or validate a domain reference. The corresponding directory holds the pack files.

---

## Domain: Clinical Development

**Scope:** Careers in clinical development, clinical data management, clinical operations, and analytics leadership within regulated pharma, biotech, or CRO environments.

**Directory:** `rules/domains/clinical_development/`
**Header file:** `domain.md` (taxonomy, vocabulary, selection criteria)
**Archetypes covered:** Archetype 1 (Transformation & Strategy), Archetype 2 (Data & Analytics), Archetype 3 (Process & Operations), Archetype 4 (Platform & Technology). All four at both Leadership and IC levels.
**Pack files:** `archetype<N>_leadership.md` and `archetype<N>_ic.md` for N in 1 to 4 (8 files).

**Use when:** The user's career centers on pharma, biotech, or CRO clinical functions; the Experience Inventory is populated primarily with entries tagged to clinical trial execution, clinical data management, clinical operations, or regulated-environment quality and governance; the active role search targets sponsor-side or CRO-side clinical functions.

**Do NOT use when:** The user's career is primarily in medical affairs without clinical operations exposure, commercial or market access roles, pure regulatory affairs, or adjacent life-sciences sectors (medical device, diagnostics) where vocabulary and framing diverge materially.

---

## Adding New Domains

Invoke `skills/domain_creation.md`. Do not add entries here directly. The creation skill validates scope, designs taxonomy, populates per-archetype content, and registers the new domain atomically.
