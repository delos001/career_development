# Career Document Bootstrap Skill

## Objective

Build a structured, tagged Experience Inventory from raw career source documents (CVs, resumes, LinkedIn exports, or similar). The output is a fully assembled `Experience_Inventory.md` file ready for use by `cv_targeted` and `cv_general`. This skill handles discovery, taxonomy design, section architecture, extraction, deduplication, and assembly. Enrichment of individual entries (adding Impact and Context annotations) is handled separately by the Annotation Enrichment Phase in `skills/source_document_update.md`.

---

## When to Invoke

- A new user is setting up the CV generation workflow for the first time
- An existing inventory needs to be rebuilt from source documents
- A user wants to onboard a substantially different body of career experience

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1, 2, 3, 4, 4b, 4c, 4d, 5

**Separation of Concerns**
Extraction and enrichment are separate passes. During the extraction pass, capture only what is explicitly stated in source documents. Do not infer, embellish, or add impact language not present in the source. Flag gaps; do not fill them. Extracted entries are raw source material, not polished CV bullets. CV content rules (`rules/cv/content_rules_leadership.md` and `rules/cv/content_rules_ic.md`) do not apply during extraction; they govern only CV generation skills.

**Deduplication Discipline**
The same experience described across multiple CVs must produce one canonical entry — not one entry per CV mention. Duplicate detection is active throughout the extraction pass. When duplicates are identified and one version is clearly more detailed, keep the most detailed version and merge any complementary detail from the other. When two versions describe the same role or achievement with substantially different framing — not just different levels of detail — do not resolve autonomously. Flag the conflict, present both versions to the user, and obtain explicit direction before proceeding.

**Progressive Write Protocol — Context Management**
This skill processes potentially large volumes of source documents and extracted entries. To prevent context overflow, extracted entries are written progressively to a staging file at `temp/inventory_staging.md` rather than held in active context throughout the session. Apply this protocol during Phase 4:

- After completing extraction for each source document, append the new entries to `temp/inventory_staging.md` using the Edit tool (or Write tool if the file does not yet exist).
- Once written, do not re-read the full staging file into active context unless a specific step requires it. Reference the file by path.
- When a phase requires reviewing entries (Phase 4b, 4c, 4d, Phase 5), read the staging file at that point rather than relying on prior context.
- Source documents are read one at a time and released after extraction. Do not hold multiple source documents in active context simultaneously.

If context becomes constrained at any point, write current progress to the staging file, summarize where processing stopped, and surface the constraint to the user before stopping. Do not silently skip content.

---

## Reference Taxonomy

This is the starting point for taxonomy design in Phase 2. It is not applied directly — it is adapted based on the user's career profile. Present this as the basis for discussion, not as the final taxonomy.

**Universal Dimensions — Do Not Change**

- Role Level: IC | Manager | Senior Manager | Director | Senior Director | VP | C-Suite
- Org Context: Greenfield | Scaling | Turnaround | Mature/Enterprise | Independent | Volunteer
- Outcome: Capability Building | Quality Improvement | Risk Reduction | Efficiency Gain | Scalability/Growth Enablement | Cost Savings | Revenue Growth | Customer/User Impact

**Reference Capability Tags — Adapt Per Career Profile**

Leadership and Management:
- Team Leadership & Development
- Organizational Design
- Stakeholder Management & Influence
- Change Management & Adoption
- Strategic Planning & Roadmapping
- Financial Management & Budgeting
- Governance & Risk Management
- Program & Project Management

Operations and Quality:
- Process Design & Optimization
- Vendor Management & Oversight
- Quality & Compliance
- Operational Excellence

Data and Technology:
- Data & Analytics
- Technology Strategy & Implementation
- AI Engineering & Development
- Product Management
- Software Development & Engineering

Customer and Commercial:
- Sales & Business Development
- Customer Success & Account Management
- Marketing & Brand Strategy
- Partnership & Ecosystem Management

These groupings are starting points. Rename, remove, combine, or add tags based on what the user's career actually requires. Domain-specific tags (e.g., Clinical Trial Execution for pharma, Underwriting for insurance, Curriculum Design for education) should be added where the career warrants them. The goal is a tag set that retrieves the right entries for the roles this person targets — not a comprehensive catalogue of everything they have ever done.

---

## Phase 1 — Career Profile Discovery

*(No documents are loaded in this phase)*

The purpose of this phase is to understand who this person is and where they are going before touching any source documents. The career profile produced here governs every subsequent decision in this skill.

**Step 1 — Current state:**
Ask the following and wait for complete responses before proceeding:
- What is your current or most recent role and industry?
- Approximately how many years of career history will the inventory cover?
- How many source documents are you providing (CVs, resumes, other)?

**Step 2 — Career direction:**
Ask:
- What types of roles are you targeting? Be as specific as you can — titles, levels, functions, or industries.
- Is your target a continuation of your current path, a pivot, or an expansion into adjacent areas?
- Are there specific capabilities or experiences you want to make sure are prominently represented?

**Step 3 — Known strengths and gaps:**
Ask:
- What do you consider your strongest areas of expertise?
- Are there areas where you feel your CV has historically undersold you?
- Are there gaps or transitions in your career history that will need to be handled carefully?

**Step 4 — Produce and confirm career profile:**
Synthesize the responses into a brief career profile summary covering: career stage, domain(s), target direction, key strengths to surface, and known sensitivity areas. Present to the user and obtain explicit confirmation before proceeding. This profile is the governing reference for all subsequent phases.

**Phase 1 Closing:** Follow Standard Phase Closing. Next phase is Phase 2.

---

## Phase 2 — Taxonomy and Section Architecture Design

*(Only after Phase 1 has been explicitly approved)*

**Step 1 — Propose Capability tags:**
Using the career profile from Phase 1 and the Reference Taxonomy above, propose a Capability tag set for this user. State which reference tags are included, which are renamed or combined, which are dropped, and which domain-specific tags are being added. Explain the reasoning briefly for any non-obvious decisions.

Present the proposed Capability tag set alongside the universal dimensions (Role Level, Org Context, Outcome) as the complete proposed taxonomy.

> **Warning before approval:** The taxonomy confirmed here governs every tag applied during extraction. Changing it after extraction requires re-tagging every entry in the inventory — a substantial rework. Take time to get this right before approving. If you are unsure whether a tag belongs, it is better to add it now and remove it later than to discover it was needed after extraction is complete.

Obtain explicit approval. Revise and re-present if the user wants changes. Do not proceed until the taxonomy is confirmed.

**Step 2 — Propose section architecture:**
Propose the thematic groupings for the "All Tasks Performed" section of the inventory. Base the groupings on the confirmed Capability tags and the career profile. Group related capabilities together in a way that makes the inventory readable and navigable for a human reviewer.

If the user has independent or volunteer project work — self-initiated projects, open source contributions, or volunteer roles — include an "Independent & Volunteer Projects" section as a named grouping. Entries in this section use the `Project:` header variant and are tagged with Org Context: Independent or Volunteer. If none exist at this stage, omit the section — it can be added later when entries are available.

Present the proposed section list with a brief description of what belongs in each section. Obtain explicit approval. Revise if needed. This architecture governs how extracted entries are organized in the assembled document.

**Phase 2 Closing:** Follow Standard Phase Closing. Next phase is Phase 3.

---

## Phase 3 — Document Intake and Deduplication Strategy

*(Only after Phase 2 has been explicitly approved)*

**Step 1 — Confirm source documents:**
Ask the user to confirm which documents are being provided and their format (docx, pdf, plain text, LinkedIn export, etc.). Attempt to read each document now to confirm it is accessible and readable. State the result for each document — accessible and readable, or failed. For any document that fails to read, instruct the user to convert it to plain text or markdown and confirm it is accessible before proceeding. Do not proceed until all documents are confirmed readable.

**Step 2 — Establish deduplication approach:**
State the deduplication strategy that will be applied during extraction:
- The same role at the same company produces one role block, regardless of how many CVs describe it
- The same achievement described in multiple CVs produces one canonical entry — the most detailed version is kept; complementary detail from other versions is merged in
- Entries that describe the same underlying work but are framed differently are collapsed to one entry with the strongest framing noted

Ask the user if there are any known duplication patterns or edge cases (e.g., the same role described very differently across CVs, contract roles with overlapping timelines) that should be handled specifically. Confirm the deduplication approach before proceeding.

**Step 3 — Establish processing order:**
If more than three source documents are provided, confirm the processing order. Recommended: most recent CV first, then chronologically backward. This reduces duplication detection burden — earlier CVs are checked against already-extracted entries rather than the reverse.

**Phase 3 Closing:** Follow Standard Phase Closing. Next phase is Phase 4.

---

## Phase 4 — Extraction Pass

*(Only after Phase 3 has been explicitly approved)*

**Entry format — apply to every extracted entry:**

For standard employment roles:
```
Role: [Title] | [Company]
**[Action statement — one discrete action, what specifically was done]**
Impact: [outcome, metric, or problem solved — OPTIONAL, only if stated in source]
Context: [scope, org stage, or framing note — OPTIONAL, only if stated in source]
Tags: Capability: X | Role Level: X | Org Context: X [ | Outcome: X — OPTIONAL, include only when a genuine organizational outcome is attached ]
Added: YYYY-MM
Last Used:
```

For independent or volunteer project entries (Org Context: Independent or Volunteer):
```
Project: [Project Name]
**[Action statement — one discrete action, what specifically was done]**
Impact: [outcome, metric, or problem solved — OPTIONAL, only if stated in source]
Context: [scope, org stage, or framing note — OPTIONAL, only if stated in source]
Tags: Capability: X | Role Level: X | Org Context: Independent [ | Outcome: X — OPTIONAL, include only when a genuine organizational outcome is attached ]
Added: YYYY-MM
Last Used:
```

**Extraction rules:**
- One discrete action per entry — do not combine multiple actions into one entry
- Action statements describe what was done, not a polished CV bullet — these are source material, not output
- Impact and Context are populated only if the source document states them — do not infer
- Every entry must have Capability, Role Level, and Org Context. Outcome is optional — include an Outcome value only when the source indicates a genuine organizational outcome attached to the action (capability built, risk reduced, efficiency gained, etc.). Omit Outcome for breadth-evidence, routine-task, and "did X" entries where no such outcome exists. Do not invent outcomes to satisfy the schema; doing so pollutes the filter used by archetype-driven CV retrieval. Tag values for all dimensions must match the confirmed taxonomy — no free text
- Role Level tag reflects the level at which the work was performed, not the target level. For entries spanning a promotion within the same company, tag each entry at the level held when that work was done
- Org Context is inferred from the source documents and career profile where not explicitly stated — flag any inferences made
- Every entry carries an `Added: YYYY-MM` stamp set to the current month at extraction time, and a `Last Used:` line left blank. Last Used is stamped only by output-producing skills (`cv_targeted`, `cv_general`, `interview_prep`) at session close — never during extraction or enrichment

**Extraction process:**

Process one source document at a time. For each document:

1. Read the full document before extracting anything.
2. Identify all roles and the time periods covered.
3. Extract entries role by role, most recent first.
4. After completing each role block, check against already-extracted entries for duplicates. Resolve duplicates before moving to the next role.
5. Append the extracted entries for this document to `temp/inventory_staging.md` per the Progressive Write Protocol. State the number of entries extracted and the number of duplicates resolved. Release the source document from active context before loading the next one.

After all documents are processed:

6. Read `temp/inventory_staging.md` and present an extraction summary: total entries, total roles represented, total duplicates resolved. Identify enrichment priority entries — entries without Impact or Context at or above the target seniority level stated in the career profile from Phase 1 that are likely to serve as anchor citations in a future CV session. Flag best-effort Outcome tags for user review. Do not begin enrichment here. Present the full flagged list and obtain user review before proceeding. The user may request corrections or additions at this point.

**Phase 4 Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Structural Reconciliation

*(Only after Phase 4 has been explicitly approved)*

The purpose of this phase is to confirm that no roles or companies from the source documents were silently dropped during extraction.

**Step 1 — Build the role coverage table:**
Read `temp/inventory_staging.md` to compile the list of roles and entry counts present in the extracted inventory. Then re-read each source document (one at a time) to confirm every role that appears in the source is represented in the staging file. For each role, state:
- Company name and role title
- Approximate time period
- Number of entries in staging file for this role
- Status: Represented | Missing | Partially Represented (entries exist but count appears low relative to what the source document covered for that role)

Do not rely on memory or summary. Read from both the staging file and the source documents to build this table.

**Step 2 — Resolve gaps:**
For any role marked Missing or Partially Represented, identify the specific source document and section where that role appears. Extract the missing entries now before proceeding. Do not defer to a later pass.

**Step 3 — Confirm coverage:**
Present the completed coverage table to the user. Obtain explicit confirmation that all roles are accounted for. If the user identifies a role that is missing from the table entirely, extract it now.

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 4c.

---

## Phase 4c — Content Completeness Spot-Check

*(Only after Phase 4b has been explicitly approved)*

The purpose of this phase is to give the user an opportunity to identify material under-extraction at the role level — cases where the entry count is technically present but does not reflect the depth of experience in the source.

**Step 1 — Present role-level entry summary:**
For each role in the coverage table from Phase 4b, present:
- The number of entries extracted
- A one-line description of what the source documents covered for that role (based on reading the source, not summarizing extracted entries)

**Step 2 — User review:**
Ask the user to review the summary and flag any role where the extracted entry count appears materially incomplete relative to what they know was in their career history. The user is the authority here — they know their own career.

**Step 3 — Resolve flagged roles:**
For each flagged role, return to the source documents and extract any entries that were missed. Add them to the inventory before proceeding. State what was added.

**Phase 4c Closing:** Follow Standard Phase Closing. Next phase is Phase 4d.

---

## Phase 4d — Convention Audit

*(Only after Phase 4c has been explicitly approved)*

The purpose of this phase is to verify that extracted entries conform to the required conventions. This is an evidence-cited audit — general confirmations are not acceptable. Each check must cite specific entries.

**Step 1 — Select audit sample:**
Read `temp/inventory_staging.md`. Select a representative sample of entries for audit: at minimum, three entries per seniority level present in the inventory (IC, Manager, Senior Manager, Director, Senior Director, VP), drawn from different roles and different thematic sections. State the entries selected and why they represent a reasonable cross-section.

**Step 2 — Run convention checks against each sampled entry:**

For each entry in the sample, verify and state Pass or Fail for each of the following:

- **Atomicity:** The action statement describes exactly one discrete action. Compound statements ("did X and Y" or "led X while managing Y") fail this check. Cite the action statement and state the determination.
- **Action statement voice:** The action statement describes what was done in plain terms — not a polished CV bullet. Entries written as finished resume language rather than raw source statements fail this check.
- **Impact sourcing:** If an Impact annotation is present, confirm it was sourced from the source document, not inferred. If it cannot be traced to a source document statement, it fails.
- **Context sourcing:** Same check as Impact sourcing.
- **Tag completeness:** Capability, Role Level, and Org Context are present on every entry — any missing dimension is a failure. Outcome is optional: present on entries with a genuine organizational outcome, absent on breadth-evidence or routine-task entries. Omitted Outcome is not a failure. An Outcome value that doesn't reflect a real outcome (forced-fit to satisfy the schema) IS a failure.
- **Tag validity:** All tag values match the confirmed taxonomy from Phase 2. Any value outside the approved taxonomy fails.
- **Role Level accuracy:** The Role Level tag reflects the seniority at which the work was performed, not the target role level.
- **Metadata presence:** Every entry has an `Added: YYYY-MM` line carrying the current extraction month and a `Last Used:` line (blank at extraction). Missing or malformed lines fail.

**Step 3 — Resolve failures and determine sweep scope:**
If any sampled entry fails a check, identify all other entries likely affected by the same type of failure and run a targeted sweep before proceeding.

**Step 4 — Present audit results for user review:**
Present a summary of the audit results before closing this phase:
- Which checks passed cleanly across all sampled entries
- Which checks produced failures, and what the failure pattern was
- How many entries were corrected in any sweep, and what was changed

The user must review and explicitly approve the audit results before this phase closes. If the user identifies additional concerns from the audit summary, resolve them before proceeding.

**Phase 4d Closing:** Follow Standard Phase Closing. Next phase is Phase 5.

---

## Phase 5 — Assembly and Write

*(Only after Phase 4d has been explicitly approved)*

**Step 1 — Confirm output location:**
The default output path is `knowledge/Experience_Inventory.md`. Confirm this with the user before writing.

> **Warning:** The CV generation skill loads the inventory from `knowledge/Experience_Inventory.md`. If you save to a different location, cv_targeted and cv_general will not find it and Phase 3a will fail. Only change the output path if you are setting up a different workflow or file structure, and update the skill load instructions accordingly.

If an `Experience_Inventory.md` already exists at the output path, warn the user before overwriting. Obtain explicit confirmation to overwrite.

**Step 2 — Assemble document:**
Assemble the full inventory document in the following structure:

1. **Taxonomy Header Block** — the confirmed taxonomy from Phase 2, encoded as a reference block at the top of the document. This block is read by `skills/source_document_update.md` to validate tag values. Format:

```
# Experience Inventory

## Tag Taxonomy

Capability: [list all confirmed Capability tags separated by |]
Role Level: IC | Manager | Senior Manager | Director | Senior Director | VP | C-Suite
Org Context: Greenfield | Scaling | Turnaround | Mature/Enterprise | Independent | Volunteer
Outcome (OPTIONAL): Capability Building | Quality Improvement | Risk Reduction | Efficiency Gain | Scalability/Growth Enablement | Cost Savings | Revenue Growth | Customer/User Impact

Tag rules: Capability, Role Level, and Org Context are required on every entry. Outcome is optional — include only when a genuine organizational outcome is attached to the action. Omit for breadth-evidence, routine-task, and "did X" entries. Do not invent outcomes to satisfy the schema; doing so pollutes the filter used by archetype-driven CV retrieval. Archetype files match against Outcome-bearing entries when their High Priority tag combinations require it; entries without Outcome are still retrievable via the other dimensions.

Entry metadata: every entry under "All Tasks Performed" carries an `Added: YYYY-MM` stamp set at creation and a `Last Used: YYYY-MM` stamp updated by output-producing skills at session close. Historical entries imported before the schema change carry `Added: pre-2026-04`.
```

2. **Education** — degrees in reverse chronological order, compact format
3. **Professional Certifications and Training** — compact, inline where possible
4. **Technical Experience** — tools, platforms, methodologies, standards, frameworks; sub-grouped by type relevant to the career profile
5. **Domain and Industry Exposure** — industries, functional domains, geographies, and any domain-specific exposure relevant to the career profile (e.g., therapeutic areas for pharma, market segments for commercial roles)
6. **All Tasks Performed** — read entries from `temp/inventory_staging.md` and organize into the thematic sections confirmed in Phase 2, reverse chronological by role within each section
7. **Academic Coursework Detail** (optional) — include only if the user has graduate-level coursework relevant to their target roles

**Step 3 — Pre-write preview and approval:**
Before writing, present a structural preview of the assembled document:
- List each section and the number of entries it contains
- For each thematic section in "All Tasks Performed," show two to three representative entries so the user can confirm the format and content look correct
- State the total entry count and confirm the taxonomy header block is present and correct

Obtain explicit approval before writing. If the user raises concerns about the structure, content, or format, resolve them before proceeding. Do not write until approved.

**Step 4 — Write:**
Write the assembled document to the confirmed output path using the Edit tool (or Write tool if the file does not yet exist). Confirm the write completed successfully.

**Step 5 — Post-write summary:**
State: total entries written, sections included, and the list of enrichment priority entries flagged during Phase 4.

**Phase 5 Closing:** Follow Standard Phase Closing. Proceed to Handoff.

---

## Handoff — Annotation Enrichment

The inventory is now populated but unenriched. Entries flagged as enrichment priorities in Phase 4 are the recommended starting point.

Ask the user: "Would you like to begin annotation enrichment now, or stop here and continue in a future session?"

**If now:** Load `skills/source_document_update.md` and execute the Annotation Enrichment Phase. Use the enrichment priority entries flagged in Phase 4 as the starting target list — present them to the user as the recommended starting point rather than re-identifying targets from scratch.

**If later:** Close the session. Remind the user that enrichment can be started at any time using the trigger phrase "let's do annotation work" or "enrich the inventory." Note that cv_targeted and cv_general can be used before enrichment is complete — unenriched entries are still retrievable, they just have less context for anchor citations.
