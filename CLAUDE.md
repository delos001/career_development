# Career Development — Project Context

This repo supports job search and CV generation workflows. See `README.md` for full repository structure and document loading map.

---

## Available Skills

| Skill | File | Trigger |
|---|---|---|
| Role Evaluation | `skills/role_evaluation.md` | Evaluating role fit against established experience and positioning; deciding whether to proceed with an application |
| CV Targeted | `skills/cv_targeted.md` | Generating a role-tailored CV for a specific target role; requires a completed GapAnalysis file from role_evaluation |
| CV General | `skills/cv_general.md` | Creating a generalized CV (not role-tailored) saved to `outputs/` |
| Source Document Update | `skills/source_document_update.md` | Capturing experience, framing decisions, or gap resolutions to source documents after any working session |
| Experience Inventory Bootstrap | `skills/experience_inventory_bootstrap.md` | Building the Experience Inventory from scratch using raw career source documents |
| Archetype Creation | `skills/archetype_creation.md` | Creating a new role archetype skeleton when no existing archetype serves the target role; produces skeleton only, pack entries are separate |
| Domain Creation | `skills/domain_creation.md` | Creating a new domain pack (vocabulary, taxonomy, per-archetype content) for roles outside currently covered domains; required when extending the repo to a new career domain or new tester |
| Career Narratives Builder | `skills/career_narratives_builder.md` | Building or updating `personal/knowledge/Career_Narratives.md` with new stories or decisions |
| Positioning Builder | `skills/positioning_builder.md` | Building or updating `personal/knowledge/Positioning.md` |
| Interview Prep | `skills/interview_prep.md` | Generating an interview prep document and pre-populated Interview Completion template for a target role; requires a completed GapAnalysis file from role_evaluation |
| Follow-Up Letter | `skills/followup.md` | Generating a follow-up letter for a specific interview round; requires a completed Interview Completion document from interview_prep |
| Career Brief | `skills/career_brief.md` | Generating a short professional bio or summary paragraph for recruiter outreach, networking introductions, or speaker profiles |
| Control | `skills/control.md` | Entry point for new users; mid-workflow navigation aid; assesses current workflow state and routes to the appropriate skill |

---

## Conventions

- When a skill is needed, read the corresponding file in `skills/` before doing anything else
- Document loading follows the just-in-time map defined in `README.md`
- Formatting is governed exclusively by `rules/cv/format_spec.md`
- Generated CVs are saved to `outputs/` in .docx format
