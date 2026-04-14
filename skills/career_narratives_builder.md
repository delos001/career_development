# Career Narratives Builder Skill

## Objective

Build and maintain `knowledge/Career_Narratives.md` — a structured record of the most consequential situations, decisions, and outcomes from the user's career. This document serves two purposes: it is a source document for `cv_targeted` when building complex, high-depth CV entries, and it is a reference for interview preparation by organizing key situations and decisions into retrievable, structured form.

This skill handles three modes:
- **New document:** No Career_Narratives.md exists. Build from scratch.
- **Adding entries:** An existing document exists. Add one or more new stories or decisions.
- **Updating entries:** An existing document exists. Deepen or revise specific existing entries.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 3a, 4a, 5a

---

## Document Structure

`knowledge/Career_Narratives.md` contains two sections. Both are present in a complete document. Volume within each section varies by individual.

**Section 1 — Stories**
Full narrative entries for complex situations. Written at sufficient depth to support a 2-3 minute interview answer. Format is selected by the user in Phase 1a and governed by the corresponding rules file in `rules/career_narratives/`.

**Section 2 — Decisions**
Structured entries for key professional decisions — situations where the path forward was non-obvious, alternatives existed, and the reasoning behind the choice matters. Decisions are distinct from stories: a story describes what happened in a complex situation; a decision documents why a specific choice was made, what alternatives were rejected, and what the reasoning was. A single situation may produce both a story entry and a decision entry if it contains enough of each. Format is selected by the user in Phase 1a and governed by the corresponding rules file in `rules/career_narratives/`.

---

## Available Formats

**Story formats** — select one per session:
- `rules/career_narratives/story_star.md` — STAR (Situation, Task, Action, Result). Widely recognized default.
- `rules/career_narratives/story_atola.md` — ATOLA (Actions, Thinking, Outcomes, Learnings, Applications). Used by AstraZeneca and similar organizations. Emphasizes reasoning process.
- `rules/career_narratives/story_personal.md` — Expanded personal format. Maximum depth for CV generation and interview prep. Includes Baseline, My Role, Thinking, Tradeoff, Constraints, Value Translation, Scale, and Application fields not present in STAR or ATOLA.

**Decision formats** — select one per session:
- `rules/career_narratives/decision_personal.md` — Personal format. Comprehensive. Optimized for interview depth.
- `rules/career_narratives/decision_adr.md` — ADR (Architecture Decision Record). Lean and portable. Widely recognized in technical and leadership contexts.

---

## Entry Selection Criteria

An entry belongs in this document if it passes the depth test: does this situation or decision have enough behind it to support a 2-3 minute conversation with real substance?

Strong results alone do not qualify for a story. The situation must have meaningful complexity, non-obvious choices, or significant stakes behind it.

A decision entry qualifies when the path forward was genuinely non-obvious — when alternatives existed, reasoning was required, and the outcome depended on judgment rather than procedure.

Use the following prompting questions conversationally to help the user assess each candidate. Not all must be answered affirmatively, but the more that apply, the stronger the case for inclusion.

- What triggered the need for action — was the problem well understood or did you have to diagnose it first?
- Why was the approach taken the right or necessary one, and what alternatives existed?
- Who had a stake in the outcome, and were any of them resistant or opposed?
- What made this non-trivial — what constraints, ambiguity, or competing priorities were present?
- What would have happened if you had not acted, or had acted differently?
- What did you have to decide under uncertainty, and how did you think through it?
- What did you learn that changed how you work or think?

If a situation produces strong answers to two or more of these questions, it belongs here. If the work was important but straightforward, it belongs in `knowledge/Experience_Inventory.md`, not here.

---

## Phase 1a — Session Setup

*(No source documents loaded yet)*

**Step 1 — Confirm mode:**
Ask the user to confirm the session mode: creating a new document, adding new entries, or updating existing entries.

**Step 2 — Select formats:**
Present the available story and decision formats listed above with a one-line description of each. Ask the user to select one story format and one decision format for this session. If the user is unsure, recommend STAR for stories and Personal for decisions as the defaults.

Load the selected story format file and the selected decision format file. Confirm both loaded completely before proceeding. These files govern all entry structure throughout the session.

**Step 3 — Load existing document (if applicable):**
If mode is Adding or Updating: load `knowledge/Career_Narratives.md` now. Confirm it loaded completely. If load fails, use bash fallback before proceeding.

**Step 4 — Load Experience Inventory (optional):**
Ask whether `knowledge/Experience_Inventory.md` is available. If yes, offer to load it as a reference for identifying candidates — it can surface entries with sufficient depth for a story or decision that have not yet been captured here. Loading is optional; the skill functions without it. If the user confirms, load it and confirm it loaded completely.

**Step 5 — Confirm readiness:**
State the mode, formats selected, and what was loaded. Confirm with user before closing.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Candidate Identification

*(State each step before completing the step)*

**Step 1 — Surface candidates:**
Ask the user to describe the situations or decisions they are considering for this session. Accept everything offered without filtering at this stage. If the Experience Inventory was loaded, scan it for entries that may have story or decision depth not yet captured in Career_Narratives.md and surface them as additional candidates.

**Step 2 — Apply selection criteria:**
For each candidate, apply the Entry Selection Criteria above. Work through the prompting questions conversationally — do not present them as a checklist. The goal is to help the user think through each candidate from a different angle and surface depth that may not be immediately obvious.

For each candidate, state a recommendation:
- **Full story entry** — sufficient situational complexity and narrative arc
- **Decision entry** — a genuine choice between alternatives with meaningful reasoning
- **Both** — the situation contains both a complex narrative and a key decision worth documenting separately
- **Inventory only** — strong result but limited depth; belongs in Experience_Inventory, not here
- **Exclude** — insufficient depth or relevance

**Step 3 — Confirm candidate list:**
Present the full recommended list with proposed treatment for each. Obtain explicit user agreement before proceeding. User may add, remove, or change the treatment of any candidate.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Entry Development

*(Only after Phase 2a has been explicitly approved)*
*(State each step before completing the step)*
*(Work through one entry at a time. Fully complete each entry before moving to the next.)*

**Step 1 — Determine entry type:**
State which entry type is being built (story, decision, or both) and confirm with the user before beginning.

**Step 2 — Build the entry:**
Follow the loaded format file for the entry type being built. Work through each field in the order defined by that file. For each field, ask the user to describe what happened, then draft the field content from what they provide. Do not generate fields from inference alone — each field requires user input or explicit confirmation that nothing applicable was present.

Apply the guidance notes in the loaded format file throughout. Flag any field that the format file identifies as a depth section and ensure it meets the standard described.

After completing a draft, ask whether the entry has enough depth to support a real interview answer, or whether any field needs to be developed further before moving on.

**Step 3 — Assign metadata block (stories AND decisions):**
After completing the entry draft, assign the 5-line metadata block that sits directly under the entry heading. The Tag Taxonomy header at the top of `knowledge/Career_Narratives.md` is the authoritative source for controlled values; consult it before assigning.

Format:

```
Tags: [pipe-separated Capability values]
Archetype: [pipe-separated Archetype values]
Era: [single Era value]
Added: YYYY-MM
Last Used:
```

Rules:
- **Tags:** values must come from the Capability list in the Tag Taxonomy header (shared vocabulary with `Experience_Inventory.md`). Multiple allowed. Reject free-text values; if the user proposes a Capability not in the controlled list, flag it and ask whether to (a) map to an existing value or (b) extend the Tag Taxonomy header before proceeding.
- **Archetype:** values must come from the Archetype list (mirrors `rules/registry_archetype.md`). Multiple allowed. Same free-text rejection rule.
- **Era:** single Era value matching the company-by-era list. If the entry spans multiple eras, choose the era in which the work was primarily performed; if the user insists on multiple, pipe-separate.
- **Added:** stamp the current YYYY-MM at entry creation. Never backfill historical entries with a constructed date — those carry `Added: pre-2026-04` from the migration.
- **Last Used:** leave blank at creation. This field is stamped by output-producing skills (`cv_targeted`, `cv_general`, `interview_prep`) at session close, not by this skill.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — Quality Control

*(Only after Phase 3a has been explicitly approved)*

For each entry developed in Phase 3a, verify:

**Depth test:** Does the entry contain enough substance to support a 2-3 minute interview answer? Verify against the guidance notes in the loaded format file. An entry that describes only what happened without the thinking, tradeoffs, or reasoning behind it fails this test regardless of format.

**Dual-use test:** Can `cv_targeted` extract a concrete outcome and organizational impact from this entry? Can the user use this entry as a reference during an interview without reconstructing the narrative from memory? Both must be true.

**Honesty check:** Are scope claims accurate? Does the outcome reflect what was actually delivered, not what was intended? Are tradeoffs, pushback, and retrospective reflection documented honestly, or have they been softened? Flag any overstated claims before writing.

**Format compliance:** Verify each entry follows the loaded format file. All fields defined by the format are present or explicitly noted as not applicable with a brief reason.

**Metadata compliance:** Verify the 5-line metadata block (Tags, Archetype, Era, Added, Last Used) is present on every entry — both stories and decisions. Verify all Tags values appear in the Capability list of the Tag Taxonomy header, all Archetype values appear in the Archetype list, and Era matches a value in the Era list. Reject any free-text value not in the controlled vocabulary. Verify Added carries the current YYYY-MM and Last Used is blank for new entries.

State the result of each check. Flag failures explicitly and invoke QC Failure Recovery before proceeding.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 5a.

---

## Phase 5a — Document Write

*(Only after Phase 4a has been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Confirm write mode:**
State whether this session will: (a) create a new document at `knowledge/Career_Narratives.md`, (b) append new entries to an existing document, or (c) replace specific existing entries. Confirm with user before writing.

**Step 2 — Confirm section placement:**
For each entry, confirm which section it belongs in (Stories or Decisions) and where within that section it will be inserted. Entries are not numbered; the heading is the title alone (e.g., `## Longitudinal Stability Surveillance`, not `## 5. Longitudinal Stability Surveillance`).

**Step 3 — Write:**
Write each approved entry to `knowledge/Career_Narratives.md` at the confirmed location. Confirm each write completed successfully before moving to the next entry.

**Step 4 — Handoff:**
After all writes are complete, confirm the session is complete and summarize what was added.

If new stories or decisions surfaced experience, framing, or positioning language not yet captured in `knowledge/Experience_Inventory.md` or `knowledge/Positioning.md`, flag those items and offer to trigger `skills/source_document_update_workflow.md` to capture them.

**Phase 5a Closing:** Follow Standard Phase Closing. Session complete.
