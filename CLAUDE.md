# Career Development — Project Context

## Purpose

This repo supports job search and CV generation workflows. It contains personal source documents, archetype instruction sets, formatting specifications, content rules, and generated CV outputs.

---

## Repository Structure

```
career_development/
├── CLAUDE.md                              ← this file
├── README.md                              ← repo orientation and document loading map
├── skills/                                ← workflow instruction sets
│   └── cv_generation.md
├── context/                               ← reference documents read by skills
│   ├── cv_format_spec.md
│   ├── cv_content_rules_leadership.md
│   ├── cv_content_rules_ic.md
│   ├── Archetype_1_Transformation_Strategy.md
│   ├── Archetype_2_Data_Analytics.md
│   ├── Archetype_3_Process_Operations.md
│   └── Archetype_4_Platform_Technology.md
├── knowledge/                             ← personal source documents — gitignored
└── outputs/                               ← generated CVs — gitignored
```

---

## Available Skills

| Skill | File | Trigger |
|---|---|---|
| CV Generation | `skills/cv_generation.md` | Creating, tailoring, or evaluating fit for a CV or role |

---

## Conventions

- When a skill is needed, read the corresponding file in `skills/` before doing anything else
- Document loading follows the just-in-time map defined in `README.md`
- Formatting is governed exclusively by `context/cv_format_spec.md`
- Generated CVs are saved to `outputs/` in .docx format
