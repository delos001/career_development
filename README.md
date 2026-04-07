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
│   └── source_document_update.md
├── context/                               ← reference documents read by skills
│   ├── cv_format_spec.md
│   ├── cv_content_rules_leadership.md
│   ├── cv_content_rules_ic.md
│   ├── Archetype_1_Transformation_Strategy.md
│   ├── Archetype_2_Data_Analytics.md
│   ├── Archetype_3_Process_Operations.md
│   ├── Archetype_4_Platform_Technology.md
│   ├── Archetype_1_IC_Transformation_Strategy.md
│   ├── Archetype_2_IC_Data_Analytics.md
│   ├── Archetype_3_IC_Process_Operations.md
│   ├── Archetype_4_IC_Platform_Technology.md
│   ├── cv_qc_checklist.md
│   └── sources.md
├── knowledge/                             ← personal source documents — gitignored
└── outputs/                               ← generated CVs — gitignored
```

---

## Folder Definitions

| Folder | Purpose | Committed |
|---|---|---|
| `skills/` | Workflow instruction sets that tell Claude what to do and how | Yes |
| `context/` | Reference documents read by skills during execution | Yes |
| `knowledge/` | Personal source documents (CV content, experience, positioning) | No — gitignored |
| `outputs/` | Generated CV files | No — gitignored |

---

## Available Skills

| Skill | File | Trigger |
|---|---|---|
| CV Generation | `skills/cv_generation.md` | Evaluating role fit and tailoring and creating CV |
| Source Document Update | `skills/source_document_update.md` | Capturing experience, framing decisions, or gap resolutions to source documents after any working session |

---

## Document Loading Map

Documents are loaded just-in-time. This map defines what is loaded, when, and why.

| Phase | Trigger | Documents Loaded |
|---|---|---|
| 1a | Session start | None — job description, company, and title collected only |
| 2a step 2 | If role level is confirmed as Associate Director or above | `knowledge/CV_General_Leadership.md` |
| 2a step 6 | Archetype confirmed (AD+) | Primary archetype file from `context/` (leadership version); secondary if dual-archetype identified |
| 2a step 6 | Archetype confirmed (IC) | Primary archetype IC file from `context/` (IC version); secondary if dual-archetype identified |
| 3a step 1 | Fit evaluation begins | `knowledge/Experience_Inventory.md`, `knowledge/Accomplishments.md`, `knowledge/Positioning.md` |
| 4a step 1 | Content generation begins | `knowledge/CV_General_Lrge_Enterprise_Established.md` or `knowledge/CV_General_Mid_Size_Scale_Up.md` — whichever matches format confirmed in Phase 2a; `context/cv_content_rules_leadership.md` (AD+) or `context/cv_content_rules_ic.md` (IC) |
| 4b start | QC of generated CV content | `context/cv_qc_checklist.md` |
| 5a start | Document generation begins | `context/cv_format_spec.md` |
| Phase 6 | Source update review | Specific knowledge docs loaded only as needed |

**Excluded from current workflow:**
- `Executive_Summary.md` — excluded pending source document consolidation review
- `context/sources.md` — research and practitioner citations supporting workflow design decisions. Not loaded by any skill. Retained for traceability.
- `context/cv_bullet_construction_guide.md` — retired. Content incorporated into content rules files. Sources moved to `context/sources.md`.

---

## Notes

- `knowledge/` and `outputs/` are gitignored — personal content never committed
- `skills/` and `context/` are committed — framework only, no personal data
- Job descriptions are stored separately in OneDrive, not in this repo
