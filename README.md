# Career Development

Private repository supporting job search and CV generation workflows.

---

## Repository Structure

```
career_development/
├── CLAUDE.md                              ← project context and skill index
├── README.md                              ← this file
├── skills/                                ← workflow instruction sets
│   ├── role_evaluation.md
│   ├── cv_targeted.md
│   ├── cv_general.md
│   ├── source_document_update.md
│   ├── experience_inventory_bootstrap.md
│   ├── archetype_creation.md
│   ├── career_narratives_builder.md
│   ├── positioning_builder.md
│   ├── interview_prep.md
│   ├── followup.md
│   ├── career_brief.md
│   └── control.md
├── rules/                                 ← rule sets read by skills during execution
│   ├── global_rules.md                   ← shared: global rules loaded by every skill at execution start
│   ├── sources.md                        ← shared: research citations for all skills
│   ├── registry_archetype.md             ← shared: archetype catalog and selection criteria
│   ├── registry_org_type.md              ← shared: organization type catalog and selection criteria
│   ├── registry_company_type.md          ← shared: company type catalog and adaptive research branches for interview_prep
│   ├── registry_skills.md                ← skill catalog with triggers, dependencies, completion signals; read by control skill
│   ├── config.md                         ← machine-specific configuration (Python executable path); update per machine
│   ├── Archetype_1_Transformation_Strategy.md
│   ├── Archetype_1_IC_Transformation_Strategy.md
│   ├── Archetype_2_Data_Analytics.md
│   ├── Archetype_2_IC_Data_Analytics.md
│   ├── Archetype_3_Process_Operations.md
│   ├── Archetype_3_IC_Process_Operations.md
│   ├── Archetype_4_Platform_Technology.md
│   ├── Archetype_4_IC_Platform_Technology.md
│   ├── cv/                               ← CV skill specific rule sets
│   │   ├── content_rules_leadership.md
│   │   ├── content_rules_ic.md
│   │   ├── format_spec.md
│   │   └── qc_checklist.md
│   └── career_narratives/               ← career narratives skill specific rule sets
│       ├── story_star.md
│       ├── story_atola.md
│       ├── story_personal.md
│       ├── decision_personal.md
│       └── decision_adr.md
├── templates/                             ← structural templates used by skills during document generation
│   └── Interview_Completion_Template.md  ← template for interview round tracking; pre-populated by interview_prep
├── knowledge/                             ← personal source documents — gitignored
│   ├── SETUP.md                          ← committed: setup instructions for new users
│   └── Contact_Info.md                   ← single source of truth for CV contact line values
└── outputs/                               ← generated CVs and role evaluation artifacts — gitignored
```

---

## Folder Definitions

| Folder | Purpose | Committed |
|---|---|---|
| `skills/` | Workflow instruction sets that tell Claude what to do and how | Yes |
| `rules/` | Rule sets read by skills during execution; shared files at root, skill-specific files in subdirectories | Yes |
| `templates/` | Structural templates used by skills to generate output documents | Yes |
| `knowledge/` | Personal source documents (CV content, experience, positioning) | No — gitignored |
| `outputs/` | Generated CV files and role evaluation artifacts | No — gitignored |

---

## Available Skills

| Skill | File | Trigger |
|---|---|---|
| Role Evaluation | `skills/role_evaluation.md` | Evaluating role fit against established experience and positioning; deciding whether to proceed with an application |
| CV Targeted | `skills/cv_targeted.md` | Generating a role-tailored CV for a specific target role; requires a completed GapAnalysis file from role_evaluation |
| CV General | `skills/cv_general.md` | Creating a generalized CV (not role-tailored) saved to `outputs/` |
| Source Document Update | `skills/source_document_update.md` | Capturing experience, framing decisions, or gap resolutions to source documents after any working session |
| Experience Inventory Bootstrap | `skills/experience_inventory_bootstrap.md` | Building the Experience Inventory from scratch using raw career source documents |
| Archetype Creation | `skills/archetype_creation.md` | Creating a new role archetype when no existing archetype serves the target role |
| Career Narratives Builder | `skills/career_narratives_builder.md` | Building or updating `knowledge/Career_Narratives.md` with new stories or decisions |
| Positioning Builder | `skills/positioning_builder.md` | Building or updating `knowledge/Positioning.md` |
| Interview Prep | `skills/interview_prep.md` | Generating an interview prep document and pre-populated Interview Completion template for a target role; requires a completed GapAnalysis file from role_evaluation |
| Follow-Up Letter | `skills/followup.md` | Generating a follow-up letter for a specific interview round; requires a completed Interview Completion document from interview_prep |
| Career Brief | `skills/career_brief.md` | Generating a short professional bio or summary paragraph for recruiter outreach, networking introductions, or speaker profiles |
| Control | `skills/control.md` | Entry point and mid-workflow navigation aid; assesses current workflow state via file-based detection and routes to the appropriate skill; reads from registry_skills.md |

---

## Document Loading Map

Documents are loaded just-in-time. This map defines what is loaded, when, and why.

### role_evaluation

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | None — job description, company, and title collected only |
| 2a step 5 | Archetype confirmed (AD+) | `rules/registry_archetype.md`; primary archetype leadership file from `rules/`; secondary archetype file and `rules/cv/dual_archetype.md` if dual-archetype identified |
| 2a step 5 | Archetype confirmed (IC) | `rules/registry_archetype.md`; primary archetype IC file from `rules/`; secondary archetype file and `rules/cv/dual_archetype.md` if dual-archetype identified |
| 2a step 6 | Org type confirmed | `rules/registry_org_type.md`; framing emphasis noted |
| 3a step 1 | Fit evaluation begins | `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, `knowledge/Positioning.md` |
| 3b | Gap rating judgment QC | `rules/judgment_qc.md` |
| Phase 4 | Source update review | Specific knowledge docs loaded only as needed |

### cv_targeted

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md` |
| 2a step 1 | Content generation begins | `rules/cv/content_rules_leadership.md` (AD+) or `rules/cv/content_rules_ic.md` (IC) |
| 2a step 2 | Archetype load | Primary archetype file (leadership or IC); secondary archetype file and `rules/cv/dual_archetype.md` if dual-archetype identified in Phase 1a |
| 2a step 3 | Source review begins | `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, `knowledge/Positioning.md` |
| 2a step 4 | Experience architecture judgment QC | `rules/judgment_qc.md` (retained through Phase 2b) |
| 2b start | QC of generated CV content | `rules/cv/qc_checklist.md` |
| 3a step 1 | Document generation begins | `rules/cv/format_spec.md`; `knowledge/Contact_Info.md` |
| 3a step 2 | Python script execution | `rules/config.md` |
| Phase 4 | Source update review | Specific knowledge docs loaded only as needed |

### cv_general

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | None — targeting context collected only |
| 2a step 1 | Archetype selection begins | `rules/registry_archetype.md`; primary archetype file (leadership or IC); secondary archetype file and `rules/cv/dual_archetype.md` if dual-archetype identified |
| 2a step 3 | Org type confirmed | `rules/registry_org_type.md`; framing emphasis noted for use in Phase 4a |
| 3a step 1 | Source review begins | `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, `knowledge/Positioning.md` |
| 3a step 3 | Experience architecture judgment QC | `rules/judgment_qc.md` (retained through Phase 4b) |
| 4a step 1 | Content generation begins | `rules/cv/content_rules_leadership.md` (AD+) or `rules/cv/content_rules_ic.md` (IC) |
| 5a step 1 | Document generation begins | `rules/cv/format_spec.md`; `knowledge/Contact_Info.md` |
| 5a step 3 | Python script execution | `rules/config.md` |

### career_narratives_builder

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a step 2 | Format selection | Selected story format file from `rules/career_narratives/`; selected decision format file from `rules/career_narratives/` |
| 1a step 3 | Adding or updating entries | `knowledge/Career_Narratives.md` |
| 1a step 4 | Optional reference load | `knowledge/Experience_Inventory.md` (if user confirms) |

### interview_prep

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md` |
| 2a step 1 | Company type identification | `rules/registry_company_type.md` |
| 3a step 1 | Content generation begins | `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, `knowledge/Positioning.md` |
| 4a step 2 | Completion document generation | `templates/Interview_Completion_Template.md` |
| 4a steps 1-2 | Python script execution | `rules/config.md` |
| Phase 5 | Source update review | Specific knowledge docs loaded only as needed |

### control

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | `rules/registry_skills.md` |

### career_brief

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 2a step 1 | Generation begins | `knowledge/Positioning.md`; `knowledge/Experience_Inventory.md` only if Positioning.md lacks sufficient specificity |

### followup

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYYMM].docx` (extracted via python-docx from application folder) |
| 1a step 2 | Python script execution | `rules/config.md` |

### source_document_update

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| Step 1 | Identifying updates | Target source documents loaded as needed: `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, `knowledge/Positioning.md` |
| Annotation Step 1 | Annotation enrichment | `knowledge/Experience_Inventory.md`; `rules/cv/content_rules_leadership.md` |

### experience_inventory_bootstrap

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| Phase 4 | Extraction pass | Source documents provided by user (one at a time per Progressive Write Protocol) |
| Phase 4b | Structural reconciliation | `temp/inventory_staging.md`; source documents re-read for coverage verification |

### archetype_creation

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1b step 1 | Boundary validation | `rules/registry_archetype.md` |
| 3a step 5 | Tag verification (if needed) | `knowledge/Experience_Inventory.md` |
| 4a step 1 | File creation | `rules/registry_archetype.md` |

### positioning_builder

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a step 2 | Existing document load (if applicable) | `knowledge/Positioning.md` |
| 1a step 3 | Optional reference load | `knowledge/Experience_Inventory.md`; `knowledge/Career_Narratives.md` (if user confirms) |

---

## Knowledge Document Schemas

The three knowledge documents carry schema metadata that skills read and write. Any skill that adds, cites, or revises content in these files must follow the contract below.

### `knowledge/Experience_Inventory.md`

- Tag Taxonomy header block at the top of the file is the authoritative source for controlled Capability, Role Level, Org Context, and Outcome values. Skills must not infer tag values from any other source.
- Classification appears on separate lines per entry: `Capability:`, `Role Level:`, `Org Context:`, and (optional) `Outcome:`. No inline `Tags:` line. Capability and Outcome allow pipe-separated multi-values on their line; Role Level and Org Context take one value each. Omit the `Outcome:` line entirely when no genuine organizational outcome is attached.
- Every entry under "All Tasks Performed" carries `Added: YYYY-MM` (stamped at entry creation) and `Last Used:` (blank at creation, updated on use).
- `Added` is stamped by `experience_inventory_bootstrap` at extraction and by `source_document_update` when new entries are added post-session. Historical entries imported before the schema change carry `Added: pre-2026-04`.
- `Last Used` is stamped only by output-producing skills at session close, only after explicit user acceptance of the final output: `cv_targeted` Phase 3a, `cv_general` Phase 5a, `interview_prep` Phase 4a. A single YYYY-MM is overwritten each time — no history.

### `knowledge/Career_Narratives.md`

- Tag Taxonomy header block at the top of the file is the authoritative source for controlled Capability (shared with Experience_Inventory), Archetype (mirrors `rules/registry_archetype.md`), and Era (by company) values. Free-text values are not permitted; unmatched values trigger either a mapping decision or a taxonomy extension.
- Every story and decision entry carries a 5-line metadata block directly under the `## [Title]` heading: `Tags:`, `Archetype:`, `Era:`, `Added: YYYY-MM`, `Last Used:`. Entry headings are the title alone — no sequential numbering.
- `Added` is stamped by `career_narratives_builder` at entry creation and by `source_document_update` when new narrative entries are added post-session. Historical entries carry `Added: pre-2026-04`.
- `Last Used` is stamped only by `interview_prep` at session close, only after explicit user acceptance of the prep doc. `cv_targeted` and `cv_general` load narratives for reference but do not stamp narrative Last Used.
- Body structure per entry is governed by the format file loaded from `rules/career_narratives/` at session start (STAR, ATOLA, Personal for stories; ADR, Personal for decisions).

### `knowledge/Positioning.md`

- Read whole; no per-entry tags or dates. Single metadata line at the top: `Last Revised: YYYY-MM`, immediately under the document title.
- `positioning_builder` updates this line on every Phase 6a write. `source_document_update` does not update this line — incremental positioning edits made via that skill should be followed by a positioning_builder pass when accumulated changes warrant a revised date.

---

**Excluded from current workflow:**
- `rules/sources.md` — research and practitioner citations supporting all skill and rules design decisions. Not loaded by any skill. Retained for traceability.
- `cv_bullet_construction_guide.md` — retired. Content incorporated into content rules files. Sources moved to `rules/sources.md`.

---

## Notes

- `knowledge/` and `outputs/` are gitignored — personal content never committed to this repo
- `skills/` and `rules/` are committed — framework only, no personal data
- Job descriptions are stored separately in OneDrive, not in this repo

---

## Knowledge Storage

`knowledge/` is a separate private git repository (`career_development_knowledge`) cloned into this directory. It is gitignored by this repo and version controlled independently.

**Two-repo workflow:**
- Framework changes (skills, rules, README) → commit and push in `career_development`
- Knowledge document changes (Experience_Inventory, Accomplishments, Positioning, CV references) → commit and push from within `knowledge/` to `career_development_knowledge`

**Setup on a new machine:**
1. Clone this repo: `git clone https://github.com/delos001/career_development.git`
2. Clone the knowledge repo into the knowledge folder: `git clone https://github.com/delos001/career_development_knowledge.git knowledge/`
3. Create `outputs/` directory if needed (gitignored, not committed)
