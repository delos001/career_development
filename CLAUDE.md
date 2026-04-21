# Career Development — Project Context

This repo supports job search and CV generation workflows. See `README.md` for full repository structure and document loading map.

---

## Personal Data Architecture

- `personal/` is a nested private git repo. Remote: `career_development_knowledge.git`. `personal/` itself is the repo root, not `personal/knowledge/`.
- `personal/` tracks four subdirectories:
  - `knowledge/` — master data: Experience_Inventory, Career_Narratives, Positioning, Contact_Info, Questions_Library, SETUP
  - `sessions/` — role_evaluation SessionLog files only, at `[Company]_APP-NNN_[YYYY-MM]_SessionLog.md`; retained permanently to anchor APP-NNN numbering
  - `applications/` — per-application folders at `[Company]_APP-NNN_[YYYY-MM]/` for pursued roles, holding GapAnalysis, ContentDecisions, InterviewPrep, InterviewScratch, InterviewCompletion, InterviewFollowup files (all named `<DocType>_[YYYY-MM].md`)
  - `do_not_pursue/` — per-application folders at `[Company]_APP-NNN_[YYYY-MM]/` for roles evaluated but not pursued; holds GapAnalysis only
- APP-NNN is the unique application ID referenced in session, application, and do_not_pursue folder names. Assignment procedure is defined in `rules/global_rules.md`.
- Framework repo (`career_development/`) gitignores `personal/` entirely. Commit framework changes from the framework repo root. Commit personal data changes from inside `personal/`.
- `outputs/` at the framework repo root holds generated `.docx` CVs only. Gitignored and has no backup remote. Backup is the user's responsibility.

Verification command if state is ever in doubt: `cd personal && git config --get remote.origin.url && git ls-files | head`. Do not infer the architecture from `git config` run inside a subdirectory alone; `git config` walks up the tree and can mislead.

---

## Available Skills

| Skill | File | Trigger |
|---|---|---|
| Role Evaluation | `skills/role_evaluation.md` | Evaluating role fit against established experience and positioning; deciding whether to proceed with an application |
| CV Targeted | `skills/cv_targeted.md` | Generating a role-tailored CV for a specific target role; requires a completed GapAnalysis file from role_evaluation |
| CV General | `skills/cv_general.md` | Creating a generalized CV (not role-tailored) saved to `outputs/` |
| Source Document Update (Workflow) | `skills/source_document_update_workflow.md` | Capturing experience, framing decisions, or gap resolutions to source documents at the close of a calling workflow skill |
| Source Document Update (Ad-Hoc) | `skills/source_document_update_adhoc.md` | Ad-hoc user-initiated updates to source documents outside any workflow session; new entries or enrichment of existing entries |
| Experience Inventory Bootstrap | `skills/experience_inventory_bootstrap.md` | Building the Experience Inventory from scratch using raw career source documents |
| Archetype Creation | `skills/archetype_creation.md` | Creating a new domain-agnostic, level-agnostic archetype file when no existing archetype serves the target role; immediately usable after creation |
| Domain Creation | `skills/domain_creation.md` | Creating a new domain file (taxonomy, vocabulary, selection criteria, tech stack, per-archetype calibration examples) for roles outside currently covered domains |
| Career Narratives Builder | `skills/career_narratives_builder.md` | Building or updating `personal/knowledge/Career_Narratives.md` with new stories or decisions |
| Positioning Builder | `skills/positioning_builder.md` | Building or updating `personal/knowledge/Positioning.md` |
| Interview Prep | `skills/interview_prep.md` | Generating an interview prep document, a blank Interview Completion file, and a blank Interview Scratch file for a target role; requires a completed GapAnalysis file from role_evaluation |
| Interview Capture | `skills/interview_capture.md` | Capturing one completed interview round (logistics, interviewers, Q&A, debrief) into the InterviewCompletion file; runs immediately after each round using the InterviewScratch file as anchor material |
| Interview Follow-Up | `skills/interview_followup.md` | Generating a follow-up letter for a specific interview round; requires the target round to be captured in the InterviewCompletion file by interview_capture |
| Career Brief | `skills/career_brief.md` | Generating a short professional bio or summary paragraph for recruiter outreach, networking introductions, or speaker profiles |
| Control | `skills/control.md` | Entry point for new users; mid-workflow navigation aid; assesses current workflow state and routes to the appropriate skill |

---

## Conventions

- When a skill is needed, read the corresponding file in `skills/` before doing anything else
- Document loading follows the just-in-time map defined in `README.md`
- Formatting is governed exclusively by `rules/cv/format_spec.md`
- Generated CVs are saved to `outputs/` in .docx format
