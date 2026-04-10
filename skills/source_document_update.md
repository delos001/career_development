# Source Document Update Skill

## Objective

Capture information surfaced during a working session that should be added to personal source documents. Keeping source documents current reduces gap closure time in future CV sessions and ensures positioning and inventory stay aligned with actual experience.

## When to Invoke

Invoke at the close of any session where new experience language, framing decisions, gap resolutions, or corrections were surfaced — not only CV sessions.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

*This skill uses Steps, not Phases. Standard Phase Closing does not apply.*

---

## Criteria for Capture

Review the session for information meeting any of the following criteria:
- **Gap resolutions:** experience, context, or framing confirmed during the session not currently in source documents
- **New achievement language:** specific outcomes, metrics, or accomplishments articulated for the first time
- **Framing decisions:** positioning or scope language confirmed that could apply to future roles
- **Corrections:** any instance where source document content was found to be inaccurate, incomplete, or misleading

Information that is role-specific and unlikely to generalize should not be captured.

---

## Target Source Documents

- `knowledge/Experience_Inventory.md`
- `knowledge/Career_Narratives.md`
- `knowledge/Positioning.md`

Load only the specific documents relevant to the updates being recommended.

---

## Document-Specific Format Requirements

`knowledge/Experience_Inventory.md` — Entries are atomic, role-specific achievement statements. Do not write entries as polished CV bullets. The entry describes what was done; Context and Impact annotations and tags enable retrieval and bullet construction.

**Entry format — standard employment roles:**
```
Role: Title | Company
**[Action statement — what specifically was done, one discrete action per entry]**
Impact: [outcome, metric, or problem solved — OPTIONAL]
Context: [scope, org stage, or framing note — OPTIONAL]
Tags: Capability: X | Role Level: X | Org Context: X | Outcome: X
```

**Entry format — independent or volunteer project entries (Org Context: Independent or Volunteer):**
```
Project: [Project Name]
**[Action statement — what specifically was done, one discrete action per entry]**
Impact: [outcome, metric, or problem solved — OPTIONAL]
Context: [scope, org stage, or framing note — OPTIONAL]
Tags: Capability: X | Role Level: X | Org Context: Independent | Outcome: X
```

**Allowed tag values — reference the Tag Taxonomy header block at the top of `knowledge/Experience_Inventory.md` for the authoritative list. Do not infer tag values from archetype files. Current values:**

- Capability: Clinical Trial Execution | Risk-Based Monitoring & Quality | Data & Analytics | Quality & Compliance | Process Design & Optimization | Technology Strategy & Implementation | Vendor Management & Oversight | Organizational Design | Governance & Risk Management | Strategic Planning & Roadmapping | Change Management & Adoption | Stakeholder Management & Influence | Team Leadership & Development | Financial Management & Budgeting | AI Engineering & Development
- Role Level: IC | Manager | Senior Manager | Director | Senior Director | VP
- Org Context: Greenfield | Scaling | Turnaround | Mature/Enterprise | Independent | Volunteer
- Outcome: Capability Building | Quality Improvement | Risk Reduction | Efficiency Gain | Scalability/Growth Enablement | Cost Savings

Multiple Capability and Outcome values are permitted per entry using pipe separators. Org Context and Role Level take one value per entry.

`knowledge/Career_Narratives.md` — Follow the structure and conventions of existing entries. Stories follow STAR format; decisions follow the decision entry format (Decision, Context, Options, Criteria, Reasoning, Pushback, Outcome, What I'd Own Differently). Include metrics where available from this session.

`knowledge/Positioning.md` — Entries are strategic positioning statements, not achievement bullets. Follow the framing conventions of existing entries.

---

## Steps

**Step 1 — Identify proposed updates:**
For each proposed update, identify the target document, the insertion location, and the proposed content formatted per the document-specific format requirements above.

**Step 2 — Pre-write QC:**
Before presenting any proposed update for approval, verify each against all of the following. Flag and exclude any item that fails — do not present failed items without explicitly noting the failure and obtaining user approval to include anyway.

- Traceable: directly sourced from an explicit user statement or source document from this session
- Not role-specific: the information generalizes to future roles and sessions
- Convention-compliant: the proposed content matches the format and voice of existing entries in the target document. For `Experience_Inventory.md`, all required tag fields must be present and tag values must match the taxonomy header block in the document.
- Non-contradictory: does not conflict with or duplicate existing source document content
- Complete (Experience_Inventory.md entries only): Before writing, verify all required elements are present:
  - Action statement: present, atomic (one discrete action), not a polished CV bullet
  - Tags: all four dimensions present — Capability, Role Level, Org Context, and Outcome where an outcome is evident
  - For Director-level entries and above: determine whether this entry is likely to serve as an anchor citation for a critical requirement match in a CV session. If yes, and if both Context and Impact are absent, query the user for this information before writing. Do not write a Director+ anchor entry without at least one of Context or Impact annotated. Breadth and delivery evidence entries at this level do not require annotation — use judgment based on whether the entry describes a discrete, citable accomplishment or a general responsibility.

**Step 3 — Present for approval:**
Present all verified proposed updates. For each item show the target document, insertion location, and the exact content to be written. State the total number of proposed updates and request explicit approval before writing. If the user wants to review individually rather than approve all at once, present one at a time and wait for approval before proceeding to the next.

**Step 4 — Write approved updates:**
For each approved update, write the content to the target document at the specified location using the Edit tool. Write exactly what was approved — do not paraphrase or reformat at this stage.

**Step 5 — Confirm changes:**
After all writes are complete, display a summary of every change made: target document, insertion location, and the exact content written. This allows the user to review what was added before closing the session.

Before closing, ask: "Is there anything else from this session — gap resolutions, framing decisions, or confirmed context — that should be captured before we close?"

---

## Annotation Enrichment Phase

A standalone process for retrospectively adding Context and Impact annotations to existing inventory entries. Invoke independently when the goal is to enrich existing entries rather than add new ones. Trigger phrases: "let's do annotation work," "enrich the inventory," "annotate the inventory."

**When to annotate:** Director-level and above entries that are likely anchor citations for critical requirement matches in CV sessions. Not every entry requires annotation. Breadth and delivery evidence entries do not. The target is 2-3 anchor entries per role block.

**Step 1 — Load documents:**
Load `knowledge/Experience_Inventory.md` and `rules/cv/content_rules_leadership.md`. Confirm both loaded completely.

**Step 2 — Identify annotation targets:**
For each Director-level or above role block, identify the 2-3 entries most likely to serve as anchor citations for a critical requirement match. Present the identified entries to the user and confirm the target list before proceeding. Do not begin annotation work without explicit confirmation of which entries to work on.

**Step 3 — Work through entries one at a time:**
For each confirmed target entry, present the current entry text and ask the user to describe what happened, what the outcome was, and what the before-state looked like if relevant. Extract structured facts from the narrative — specifically what was delivered vs. designed vs. planned-but-not-completed. Do not conflate these: an initiative designed but not implemented is not the same as one fully delivered.

**Step 4 — Draft annotation:**
Draft a Context annotation, an Impact annotation, or both, based on what the user provided. Apply the impact statement type hierarchy from `rules/cv/content_rules_leadership.md`: quantified first, then bounded qualitative, then contextual narrative. Never use vague category labels.

**Step 5 — Honesty check:**
Before presenting for approval, verify the draft against the following: Is the scope accurate per what the user described? Does the Impact claim reflect what was actually delivered, not what was intended? Is the language defensible if questioned in an interview? Flag any overstated claims explicitly before presenting.

**Step 6 — Present and confirm:**
Present the draft annotation to the user. Wait for explicit approval before writing. If the user requests changes, revise and re-present. Do not write until approved.

**Step 7 — Write:**
Write the approved annotation to the entry in `knowledge/Experience_Inventory.md` using the Edit tool. Write exactly what was approved. Move to the next entry only after the current one is written and confirmed.

**Step 8 — Close:**
After all target entries are annotated, summarize what was written. Ask whether any additional entries should be annotated before closing.
