# Career Development

Private repository supporting job search and CV generation workflows.

---

## Repository Structure

```
career_development/
├── CLAUDE.md                              ← project context and skill index
├── README.md                              ← this file
├── skills/                                ← workflow instruction sets
│   ├── cv_generation.md
│   ├── source_document_update.md
│   ├── career_document_bootstrap.md
│   ├── archetype_creation.md
│   ├── career_narratives_builder.md
│   ├── positioning_builder.md
│   └── general_cv_builder.md
├── rules/                                 ← rule sets read by skills during execution
│   ├── sources.md                        ← shared: research citations for all skills
│   ├── registry_archetype.md             ← shared: archetype catalog and selection criteria
│   ├── registry_org_type.md              ← shared: organization type catalog and selection criteria
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
├── knowledge/                             ← personal source documents — gitignored
│   └── SETUP.md                          ← committed: setup instructions for new users
└── outputs/                               ← generated CVs — gitignored
```

---

## Folder Definitions

| Folder | Purpose | Committed |
|---|---|---|
| `skills/` | Workflow instruction sets that tell Claude what to do and how | Yes |
| `rules/` | Rule sets read by skills during execution; shared files at root, skill-specific files in subdirectories | Yes |
| `knowledge/` | Personal source documents (CV content, experience, positioning) | No — gitignored |
| `outputs/` | Generated CV files | No — gitignored |

---

## Available Skills

| Skill | File | Trigger |
|---|---|---|
| CV Generation | `skills/cv_generation.md` | Evaluating role fit and tailoring and creating CV |
| Source Document Update | `skills/source_document_update.md` | Capturing experience, framing decisions, or gap resolutions to source documents after any working session |
| Career Document Bootstrap | `skills/career_document_bootstrap.md` | Building the Experience Inventory from scratch using raw career source documents |
| Archetype Creation | `skills/archetype_creation.md` | Creating a new role archetype when no existing archetype serves the target role |
| Career Narratives Builder | `skills/career_narratives_builder.md` | Building or updating `knowledge/Career_Narratives.md` with new stories or decisions |
| Positioning Builder | `skills/positioning_builder.md` | Building or updating `knowledge/Positioning.md` |
| General CV Builder | `skills/general_cv_builder.md` | Creating a generalized CV (not role-tailored) saved to `outputs/` |

---

## Document Loading Map

Documents are loaded just-in-time. This map defines what is loaded, when, and why.

| Phase | Trigger | Documents Loaded |
|---|---|---|
| 1a | Session start | None — job description, company, and title collected only |
| 2a step 5 | Archetype confirmed (AD+) | `rules/registry_archetype.md`; primary archetype leadership file from `rules/`; secondary if dual-archetype identified |
| 2a step 5 | Archetype confirmed (IC) | `rules/registry_archetype.md`; primary archetype IC file from `rules/`; secondary if dual-archetype identified |
| 2a step 6 | Org type confirmed | `rules/registry_org_type.md`; framing emphasis noted for use in Phase 4a |
| 3a step 1 | Fit evaluation begins | `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, `knowledge/Positioning.md` |
| 4a step 1 | Content generation begins | `rules/cv/content_rules_leadership.md` (AD+) or `rules/cv/content_rules_ic.md` (IC); org-type framing emphasis applied from registry entry confirmed in Phase 2a |
| 4b start | QC of generated CV content | `rules/cv/qc_checklist.md` |
| 5a start | Document generation begins | `rules/cv/format_spec.md` |
| Phase 6 | Source update review | Specific knowledge docs loaded only as needed |

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
