# Source Document Update Skill

## Objective

Capture information surfaced during a working session that should be added to personal source documents. Keeping source documents current reduces gap closure time in future CV sessions and ensures positioning and inventory stay aligned with actual experience.

## When to Invoke

Invoke at the close of any session where new experience language, framing decisions, gap resolutions, or corrections were surfaced — not only CV sessions.

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
- `knowledge/Accomplishments.md`
- `knowledge/Positioning.md`

Load only the specific documents relevant to the updates being recommended.

---

## Document-Specific Format Requirements

`knowledge/Experience_Inventory.md` — Entries are atomic, role-specific achievement statements. Do not write entries as polished CV bullets. The entry describes what was done; Context and Impact annotations and tags enable retrieval and bullet construction.

**Entry format:**
```
Role: Title | Company
**[Action statement — what specifically was done, one discrete action per entry]**
Impact: [outcome, metric, or problem solved — OPTIONAL]
Context: [scope, org stage, or framing note — OPTIONAL]
Tags: Capability: X | Role Level: X | Org Context: X | Outcome: X
```

**Allowed tag values — reference the Tag Taxonomy header block at the top of `knowledge/Experience_Inventory.md` for the authoritative list. Do not infer tag values from archetype files. Current values:**

- Capability: Clinical Trial Execution | Risk-Based Monitoring & Quality | Data & Analytics | Quality & Compliance | Process Design & Optimization | Technology Strategy & Implementation | Vendor Management & Oversight | Organizational Design | Governance & Risk Management | Strategic Planning & Roadmapping | Change Management & Adoption | Stakeholder Management & Influence | Team Leadership & Development | Financial Management & Budgeting
- Role Level: IC | Manager | Senior Manager | Director | Senior Director | VP
- Org Context: Greenfield | Scaling | Turnaround | Mature/Enterprise
- Outcome: Capability Building | Quality Improvement | Risk Reduction | Efficiency Gain | Scalability/Growth Enablement | Cost Savings

Multiple Capability and Outcome values are permitted per entry using pipe separators. Org Context and Role Level take one value per entry.

`knowledge/Accomplishments.md` — Follow the structure and conventions of existing entries. Include metrics where available from this session.

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

**Step 3 — Present for approval:**
Present all verified proposed updates. For each item show the target document, insertion location, and the exact content to be written. State the total number of proposed updates and request explicit approval before writing. If the user wants to review individually rather than approve all at once, present one at a time and wait for approval before proceeding to the next.

**Step 4 — Write approved updates:**
For each approved update, write the content to the target document at the specified location using the Edit tool. Write exactly what was approved — do not paraphrase or reformat at this stage.

**Step 5 — Confirm changes:**
After all writes are complete, display a summary of every change made: target document, insertion location, and the exact content written. This allows the user to review what was added before closing the session.

Before closing, ask: "Is there anything else from this session — gap resolutions, framing decisions, or confirmed context — that should be captured before we close?"
