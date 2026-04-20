# Source Document Update — Core Procedure

Shared procedural core for `skills/source_document_update_workflow.md` and `skills/source_document_update_adhoc.md`. Not a skill; do not invoke directly. The calling skill loads `rules/global_rules.md`, establishes session scope, then loads this file and executes Steps 1-5 in order.

---

## Active Domain Load

Before any validation or writes occur, determine the active domain and load its taxonomy:

1. Read the `**Active Domain:**` value from the header of `personal/knowledge/Experience_Inventory.md`. Do not assume; read the file. If no Active Domain is declared, halt and prompt the user.

2. Load `rules/domains/<active_domain>.md` and confirm it loaded completely. Section 1 (Tag Taxonomy) is the authoritative allowed-value list for Capability, Role Level, Org Context, Outcome, and Org Type. All tag validation in this procedure references this file; do not infer tag values from archetype files or from the inventory header.

---

## Criteria for Capture

Review the session scope defined by the calling skill for information meeting any of the following criteria:
- **Gap resolutions:** experience, context, or framing confirmed during the session not currently in source documents
- **New achievement language:** specific outcomes, metrics, or accomplishments articulated for the first time
- **Framing decisions:** positioning or scope language confirmed that could apply to future roles
- **Corrections:** any instance where source document content was found to be inaccurate, incomplete, or misleading

Information that is role-specific and unlikely to generalize should not be captured.

---

## Target Source Documents

- `personal/knowledge/Experience_Inventory.md`
- `personal/knowledge/Career_Narratives.md`
- `personal/knowledge/Positioning.md`

Load only the specific documents relevant to the updates being recommended.

---

## Document-Specific Format Requirements

`personal/knowledge/Experience_Inventory.md` — Entries are atomic, role-specific achievement statements. Do not write entries as polished CV bullets. The entry describes what was done; Context and Impact annotations and tags enable retrieval and bullet construction.

**Entry format — standard employment roles:**
```
ID: EX-NNN
Role: Title | Company
**[Action statement — what specifically was done, one discrete action per entry]**
Impact: [outcome, metric, or problem solved — OPTIONAL]
Context: [scope, org stage, or framing note — OPTIONAL]
Capability: X [ | Y — multiple values permitted, pipe-separated ]
Role Level: X
Org Context: X
Outcome: X [ — OPTIONAL line, omit entirely when no genuine organizational outcome is attached ]
Added: YYYY-MM
Last Used:
```

**Entry format — independent or volunteer project entries (Org Context: Independent or Volunteer):**
```
ID: PR-NNN
Project: [Project Name]
**[Action statement — what specifically was done, one discrete action per entry]**
Impact: [outcome, metric, or problem solved — OPTIONAL]
Context: [scope, org stage, or framing note — OPTIONAL]
Capability: X [ | Y — multiple values permitted, pipe-separated ]
Role Level: X
Org Context: Independent
Outcome: X [ — OPTIONAL line, omit entirely when no genuine organizational outcome is attached ]
Added: YYYY-MM
Last Used:
```

New entries receive a sequential `ID:` per prefix (`EX-` for role entries, `PR-` for project entries): scan `personal/knowledge/Experience_Inventory.md` for existing `ID:` values, take `max + 1` per prefix, and write zero-padded to 3 digits (`EX-191`, `PR-006`). Widen past 3 digits naturally once any prefix exceeds 999. IDs are immutable: never reused after an entry is deleted, never renumbered.

New entries carry `Added: YYYY-MM` set to the current month; `Last Used:` is left blank. Last Used is stamped only by output-producing skills (`cv_targeted`, `cv_general`, `interview_prep`) at session close. Do not backfill Added with a reconstructed historical date; legacy entries carry `Added: pre-2026-04` from the migration.

**Allowed tag values — the authoritative list is Section 1 of the active domain file (`rules/domains/<active_domain>.md`), loaded at entry. Do not infer tag values from archetype files or from the inventory header.**

Dimensions governed by the domain file: Capability, Role Level, Org Context, Outcome, Org Type. Capability and Outcome values are pipe-separated on their respective lines when multiple apply. Role Level and Org Context take one value per entry. Outcome is optional; omit the entire line when no genuine organizational outcome is attached.

**Enrichment of existing inventory entries:** Adding or revising Context, Impact, or tag values on an existing entry is governed by the same conventions as new entries. When enriching, preserve the original action statement verbatim unless the user explicitly confirms a rewording. Do not invent outcomes to satisfy a retrieval preference; if the user cannot describe a real outcome, omit the Outcome line.

`personal/knowledge/Career_Narratives.md` — Follow the structure and conventions of existing entries. Story and decision body formats are governed by files in `rules/career_narratives/`; select the format matching the existing entry being extended, or the default (STAR for stories, Personal for decisions) for new entries. Include metrics where available from the session scope.

Every narrative entry carries a 5-line metadata block directly under the heading:

```
## [Title]

Tags: [pipe-separated Capability values]
Archetype: [pipe-separated Archetype values]
Era: [single Era value]
Added: YYYY-MM
Last Used:

[body content per format file]
```

Allowed metadata values by dimension: Tags (Capability) must come from Section 1 of the active domain file (`rules/domains/<active_domain>.md`). Archetype must come from `rules/registry_archetype.md`. Era must come from the Era list in the `personal/knowledge/Career_Narratives.md` header block. Reject free-text values. If the user proposes a Capability value not in the domain file, an Archetype not in the registry, or an Era not in the narratives header, flag it and ask whether to (a) map to an existing value or (b) extend the governing file before proceeding. `Added: YYYY-MM` is set to the current month at creation; `Last Used:` is left blank. Entry headings are the title alone — no sequential numbering.

`personal/knowledge/Positioning.md` — Entries are strategic positioning statements, not achievement bullets. Follow the framing conventions of existing entries.

---

## Steps

*This procedure uses Steps, not Phases. Standard Phase Closing does not apply.*

**Step 1 — Identify proposed updates:**
Working from the session scope established by the calling skill, identify for each proposed update the target document, the insertion location, and the proposed content formatted per the document-specific format requirements above. Proposed updates include both new entries and enrichment of existing entries (revised or added Context, Impact, tag values, or narrative body content).

If the calling skill supplied a pre-identified target list (e.g., a flagged enrichment list from `experience_inventory_bootstrap`), use that list as the starting point rather than re-identifying targets from scratch.

**Step 2 — Pre-write QC:**
Before presenting any proposed update for approval, verify each against all of the following. Flag and exclude any item that fails. Do not present failed items without explicitly noting the failure and obtaining user approval to include anyway.

- Traceable: directly sourced from an explicit user statement or source document within the session scope
- Not role-specific: the information generalizes to future roles and sessions
- Convention-compliant: the proposed content matches the format and voice of existing entries in the target document. For `Experience_Inventory.md`, all required tag fields must be present and tag values must match Section 1 of the active domain file.
- Non-contradictory: does not conflict with or duplicate existing source document content
- Complete (Experience_Inventory.md entries only): Before writing, verify all required elements are present:
  - Action statement: present, atomic (one discrete action), not a polished CV bullet
  - Classification lines: `Capability:`, `Role Level:`, and `Org Context:` each present as their own line on every entry. `Outcome:` line is optional; include only when a genuine organizational outcome is attached to the action; omit the entire line for breadth-evidence, routine-task, and "did X" entries. Do not invent outcomes to satisfy the schema. All values must match Section 1 of the active domain file (`rules/domains/<active_domain>.md`); reject free-text values.
  - Metadata: `ID:` assigned per the ID assignment rule (first line, unique per prefix, new entries only), `Added: YYYY-MM` set to current month (new entries only), and `Last Used:` left blank (new entries only; existing entries retain their current value)
  - For Director-level entries and above: determine whether this entry is likely to serve as an anchor citation for a critical requirement match in a CV session. If yes, and if both Context and Impact are absent, query the user for this information before writing. Do not write a Director+ anchor entry without at least one of Context or Impact annotated. Breadth and delivery evidence entries at this level do not require annotation — use judgment based on whether the entry describes a discrete, citable accomplishment or a general responsibility.
- Complete (Career_Narratives.md entries only): the 5-line metadata block is present, Tags (Capability) values match Section 1 of the active domain file, Archetype values match `rules/registry_archetype.md`, Era values match the Era list in the `personal/knowledge/Career_Narratives.md` header, `Added: YYYY-MM` is the current month (new entries only), and `Last Used:` is blank (new entries only).
- Enrichment honesty check (enrichment of existing entries only): Is the scope accurate per what the user described? Does the Impact claim reflect what was actually delivered, not what was intended or designed? Is the language defensible if questioned in an interview? Flag any overstated claims explicitly before presenting.

**Step 3 — Present for approval:**
Present all verified proposed updates. For each item show the target document, insertion or revision location, and the exact content to be written. State the total number of proposed updates and request explicit approval before writing. If the user wants to review individually rather than approve all at once, present one at a time and wait for approval before proceeding to the next.

**Step 4 — Write approved updates:**
For each approved update, write the content to the target document at the specified location using the Edit tool. Write exactly what was approved — do not paraphrase or reformat at this stage. For enrichment of existing entries, preserve the original action statement verbatim unless the user explicitly confirmed a rewording during approval.

**Step 5 — Confirm changes:**
After all writes are complete, display a summary of every change made: target document, insertion or revision location, and the exact content written. This allows the user to review what was added or revised before closing the session.

Before closing, ask: "Is there anything else within the session scope — gap resolutions, framing decisions, confirmed context, or existing entries that need enrichment — that should be captured before we close?"
