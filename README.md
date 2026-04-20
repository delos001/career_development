# Career Development

A personal framework for documenting professional experience and supporting the full job-search lifecycle: role fit evaluation, CV generation, interview preparation and capture, and post-interview follow-up. It is intended for professionals who want a durable record of their career and a repeatable workflow around applying, interviewing, and networking. The framework operates through Claude Code; there is no graphical UI at present.

---

## Table of Contents

- [Currently Supported and Pending](#currently-supported-and-pending)
- [Architecture Note](#architecture-note)
- [Prerequisites](#prerequisites)
- [Initial Data Investment](#initial-data-investment)
- [How to Start](#how-to-start)
- [Repository Structure](#repository-structure)
- [Framework Components](#framework-components)
  - [Skills](#skills)
  - [Rules](#rules)
  - [Templates](#templates)
  - [Support](#support)
  - [Knowledge Documents](#knowledge-documents)
  - [Session Artifacts](#session-artifacts)
  - [Outputs](#outputs)
- [Document Loading Map](#document-loading-map)
- [Knowledge Document Schemas](#knowledge-document-schemas)
- [Personal Data Storage](#personal-data-storage)

---

## Currently Supported and Pending

**Currently supported:**
- Build and maintain core experience documents: Experience Inventory, Positioning, Career Narratives (key stories and decisions), general non-role-specific CV
- Assess potential role fit against established experience and identify gaps
- Generate role-targeted CVs
- Feed experience discovered during role evaluation back into core experience documents
- Prepare for interviews against a specific role and company
- Capture information obtained during each interview round
- Generate post-interview follow-up letters
- Produce short professional bios for recruiter outreach, networking introductions, and speaker profiles

**Pending, not yet built:**
- User interface for displaying Experience Inventory, Positioning, Career Narratives, and interview prep
- Cover letter generation
- Compensation negotiation support
- Networking outreach
- Offer evaluation
- Interview outcome tracking
- Interview end-state capture and analysis

---

## Architecture Note

The framework is domain-pluggable and built on three orthogonal axes: archetype, domain, and level. Each owns a single file; nothing nests. Archetype files (`rules/archetypes/`) carry match criteria, framing patterns, tag priorities, and de-emphasis rules and are both domain-agnostic and level-agnostic. Domain files (`rules/domains/<slug>.md`) carry tag taxonomy, vocabulary, selection criteria, tech stack, and archetype calibration examples. Level files (`rules/cv/content_rules_leadership.md`, `content_rules_ic.md`) carry voice, register, and bullet construction. The active domain is declared in the user's `Experience_Inventory.md` header. Composition happens at generation time; the same skill suite serves multiple domains and testers with no skill changes.

---

## Prerequisites

| Requirement | Purpose |
|---|---|
| **Claude Code** | The framework runs through Claude Code. No other chat client or IDE extension is supported. Install from https://claude.com/claude-code. |
| **Git** | Used to clone this framework repo and the separate personal knowledge repo. |
| **GitHub account** | Required if you intend to version-control your personal knowledge in a private remote repo (recommended). Not required if you keep knowledge local-only. |
| **Python 3 with `python-docx`** | Required by `cv_targeted` and `cv_general` to generate `.docx` output. The Python executable path is recorded in `rules/config.md` and must be updated per machine. |
| **Microsoft Word or a `.docx`-compatible reader** | To open generated CV files. |
| **A plain-text or Markdown editor** | The framework reads and writes `.md` files throughout. You need something to view and occasionally edit them outside of Claude Code. VS Code, Notepad++, Obsidian, or any plain-text editor works. |

---

## Initial Data Investment

Most of this framework's functionality depends on three foundational knowledge documents that you must build before the role-targeted, CV-generation, and interview-related skills can produce meaningful results:

- `Experience_Inventory.md` — comprehensive catalog of tasks, achievements, and responsibilities across your career, classified by capability, role level, org context, and outcome
- `Positioning.md` — how you position yourself professionally: target roles, value proposition, strengths, differentiators
- `Career_Narratives.md` — key career stories (STAR, ATOLA formats) and framing decisions (ADR, Personal formats)

Building these is a meaningful up-front effort. You will need source material spanning a reasonable slice of your career: several CVs covering different periods, performance reviews, role descriptions, project summaries, and notes on major career decisions. The `experience_inventory_bootstrap` skill ingests this material and produces a first-pass Experience Inventory; you then refine alongside `positioning_builder` and `career_narratives_builder`.

Expect the initial build to take several sessions over multiple days. If you do not have this foundation in place, the `role_evaluation`, `cv_targeted`, `cv_general`, `interview_prep`, and `career_brief` skills will produce degraded, generic, or empty results. Anyone considering adopting this framework should account for this investment before committing.

---

## How to Start

Open Claude Code in the repo root and invoke the `control` skill. Natural-language invocations work (for example: "run control", "where am I?", "I have a new role to evaluate"); `/control` also works if configured as a slash command.

The control skill assesses current workflow state by inspecting which knowledge documents and session artifacts exist, identifies the single most appropriate next action, and routes you to the correct skill. Use it as the entry point for a new workflow, as a "where am I?" check mid-workflow, or any time you are unsure which skill to run.

First-time setup (cloning the knowledge repo, creating `personal/sessions/` and `outputs/`) is covered in the [Personal Data Storage](#personal-data-storage) section below.

---

## Repository Structure

```
career_development/
├── CLAUDE.md                              ← project context and skill index
├── README.md                              ← this file
├── skills/                                ← workflow instruction sets
├── rules/                                 ← rule sets read by skills during execution
│   ├── archetypes/                        ← archetype files (domain- and level-agnostic)
│   ├── domains/                           ← domain files (one flat file per domain)
│   ├── cv/                                ← CV-skill-specific rule sets
│   └── career_narratives/                 ← career-narrative-skill-specific format rules
├── templates/                             ← structural templates used by skills during document generation
├── support/                               ← scaffolding and resources for user-created artifacts
│   └── knowledge_repo_scaffolding/        ← copied into personal/knowledge/ during initial setup
├── personal/                              ← personal data root, gitignored
│   ├── knowledge/                         ← master source documents (separate private repo)
│   └── sessions/                          ← transactional session artifacts
└── outputs/                               ← generated deliverables only (gitignored)
```

Details of every file in `skills/`, `rules/`, `templates/`, and every expected file in `personal/` and `outputs/` are documented in [Framework Components](#framework-components) below.

---

## Framework Components

Every skill, rule, template, knowledge document, session artifact, and output in the framework, organized by type. Each entry shows its purpose and the files it reads or produces.

### Skills

Workflow instruction sets that tell Claude what to do and how. Located in `skills/`.

---

**`control.md` — Workflow Navigation**
- Purpose: Entry point and mid-workflow router. Assesses current workflow state via file-based detection and routes to the appropriate next skill.
- Inputs:
  - `rules/global_rules.md`
  - `rules/registry_skills.md`
- Outputs:
  - Routing decision and handoff (no file produced)

---

**`experience_inventory_bootstrap.md` — Experience Inventory Bootstrap**
- Purpose: Build the Experience Inventory from scratch using raw career source documents.
- Inputs:
  - `rules/global_rules.md`
  - User-supplied source documents (old CVs, resumes, performance reviews, role descriptions)
  - `temp/inventory_staging.md` (internal working file)
- Outputs:
  - `personal/knowledge/Experience_Inventory.md`

---

**`career_narratives_builder.md` — Career Narratives Builder**
- Purpose: Build or update the stories and decisions library.
- Inputs:
  - `rules/global_rules.md`
  - `personal/knowledge/Career_Narratives.md`
  - Selected format files from `rules/career_narratives/`
  - `personal/knowledge/Experience_Inventory.md` (optional reference)
- Outputs:
  - `personal/knowledge/Career_Narratives.md`

---

**`positioning_builder.md` — Positioning Builder**
- Purpose: Build or update strategic positioning, framing statements, and recruiter pitch.
- Inputs:
  - `rules/global_rules.md`
  - `personal/knowledge/Positioning.md`
  - `personal/knowledge/Experience_Inventory.md` (optional reference)
  - `personal/knowledge/Career_Narratives.md` (optional reference)
- Outputs:
  - `personal/knowledge/Positioning.md`

---

**`role_evaluation.md` — Role Evaluation**
- Purpose: Evaluate a role's fit against established experience; decide whether to proceed with an application.
- Inputs:
  - `rules/global_rules.md`
  - Job description (user-supplied)
  - `personal/knowledge/Experience_Inventory.md`
  - `personal/knowledge/Career_Narratives.md`
  - Active archetype file from `rules/archetypes/`
  - Active domain file at `rules/domains/<active_domain>.md`
  - `rules/registry_archetype.md`
  - `rules/registry_org_type.md`
  - `rules/cv/dual_archetype.md` (if dual-archetype identified)
  - `rules/judgment_qc.md`
- Outputs:
  - `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`
  - `personal/sessions/[Company]_[Role]_[YYYY-MM]_SessionLog.md` (temporary, deleted at skill close)

---

**`cv_targeted.md` — CV Targeted**
- Purpose: Generate a role-tailored CV for a specific target role.
- Inputs:
  - `rules/global_rules.md`
  - `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`
  - `personal/knowledge/Experience_Inventory.md`
  - `personal/knowledge/Career_Narratives.md`
  - `personal/knowledge/Contact_Info.md`
  - Active archetype file from `rules/archetypes/`
  - Active domain file at `rules/domains/<active_domain>.md`
  - `rules/cv/content_rules_leadership.md` or `rules/cv/content_rules_ic.md`
  - `rules/cv/format_spec.md`
  - `rules/cv/qc_checklist.md`
  - `rules/cv/dual_archetype.md` (if dual-archetype identified)
  - `rules/judgment_qc.md`
  - `rules/config.md`
- Outputs:
  - `outputs/[Name]_CV_[Company]_[AbbreviatedRole]_[YYYY-MM].docx`
  - `personal/sessions/[Company]_[Role]_[YYYY-MM]_ContentDecisions.md`
  - `Last Used` stamps on cited entries in `personal/knowledge/Experience_Inventory.md`

---

**`cv_general.md` — CV General**
- Purpose: Generate a generalized CV not tied to a specific role.
- Inputs:
  - `rules/global_rules.md`
  - `personal/knowledge/Experience_Inventory.md`
  - `personal/knowledge/Career_Narratives.md`
  - `personal/knowledge/Contact_Info.md`
  - Active archetype file from `rules/archetypes/`
  - Active domain file at `rules/domains/<active_domain>.md`
  - `rules/registry_archetype.md`
  - `rules/registry_org_type.md`
  - `rules/cv/content_rules_leadership.md` or `rules/cv/content_rules_ic.md`
  - `rules/cv/format_spec.md`
  - `rules/cv/dual_archetype.md` (if dual-archetype identified)
  - `rules/judgment_qc.md`
  - `rules/config.md`
- Outputs:
  - `outputs/CV_General_[descriptor]_[YYYY-MM].docx`
  - `Last Used` stamps on cited entries in `personal/knowledge/Experience_Inventory.md`

---

**`interview_prep.md` — Interview Prep**
- Purpose: Generate interview prep document, blank Interview Completion file, and blank Interview Scratch file for a target role.
- Inputs:
  - `rules/global_rules.md`
  - `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`
  - `personal/knowledge/Experience_Inventory.md`
  - `personal/knowledge/Career_Narratives.md`
  - `personal/knowledge/Positioning.md`
  - `personal/knowledge/Questions_Library.md`
  - `rules/registry_company_type.md`
  - `templates/Interview_Completion_Template.md`
  - `templates/Interview_Scratch_Template.md`
  - `rules/config.md`
- Outputs:
  - `InterviewPrep_[Company]_[Role]_[YYYY-MM].md`
  - `InterviewCompletion_[Company]_[Role]_[YYYY-MM].md` (blank, ready for capture)
  - `InterviewScratch_[Company]_[Role]_[YYYY-MM].md` (blank, ready for in-round notes)
  - Updated `personal/knowledge/Questions_Library.md`
  - `Last Used` stamps on cited entries in `personal/knowledge/Career_Narratives.md`
  - `Last Used` stamps on cited entries in `personal/knowledge/Experience_Inventory.md`

---

**`interview_capture.md` — Interview Capture**
- Purpose: Capture one completed interview round (logistics, interviewers, Q&A, debrief) into the InterviewCompletion file.
- Inputs:
  - `rules/global_rules.md`
  - `InterviewScratch_[Company]_[Role]_[YYYY-MM].md` (user-supplied path)
  - `InterviewPrep_[Company]_[Role]_[YYYY-MM].md` (path read from scratch file header)
  - `InterviewCompletion_[Company]_[Role]_[YYYY-MM].md` (path read from scratch file header)
- Outputs:
  - Updated `InterviewCompletion_[Company]_[Role]_[YYYY-MM].md` (one round populated per invocation)

---

**`interview_followup.md` — Interview Follow-Up**
- Purpose: Generate a follow-up letter for a specific captured interview round.
- Inputs:
  - `rules/global_rules.md`
  - `InterviewScratch_[Company]_[Role]_[YYYY-MM].md` (user-supplied path)
  - `InterviewCompletion_[Company]_[Role]_[YYYY-MM].md` with the target round populated
- Outputs:
  - `InterviewFollowup_[Company]_[Role]_R[N]_[YYYY-MM].md` (one per recipient if multiple)

---

**`career_brief.md` — Career Brief**
- Purpose: Generate a short professional bio or summary paragraph for recruiter outreach, networking introductions, or speaker profiles.
- Inputs:
  - `rules/global_rules.md`
  - `personal/knowledge/Positioning.md`
  - `personal/knowledge/Experience_Inventory.md` (only if Positioning lacks sufficient specificity)
- Outputs:
  - Plain text displayed in chat (no file produced)

---

**`source_document_update_workflow.md` — Source Document Update (Workflow)**
- Purpose: Capture experience, framing decisions, or gap resolutions into source documents at the close of a calling workflow skill. Invoked only from another workflow skill, never directly by the user or the control skill.
- Inputs:
  - `rules/global_rules.md`
  - `rules/source_document_update_core.md` (shared procedural core; Active Domain Load, Criteria for Capture, format requirements, Steps 1-5)
  - Target source documents as needed:
    - `personal/knowledge/Experience_Inventory.md`
    - `personal/knowledge/Career_Narratives.md`
    - `personal/knowledge/Positioning.md`
- Outputs:
  - Updated `personal/knowledge/Experience_Inventory.md` (as applicable)
  - Updated `personal/knowledge/Career_Narratives.md` (as applicable)
  - Updated `personal/knowledge/Positioning.md` (as applicable)

---

**`source_document_update_adhoc.md` — Source Document Update (Ad-Hoc)**
- Purpose: Capture new entries or enrich existing entries in the source documents ad-hoc, outside any workflow session. User-invoked entry point; also the destination for post-bootstrap inventory enrichment and pre-domain-switch inventory review.
- Inputs:
  - `rules/global_rules.md`
  - `rules/source_document_update_core.md` (shared procedural core; Active Domain Load, Criteria for Capture, format requirements, Steps 1-5)
  - Target source documents as needed:
    - `personal/knowledge/Experience_Inventory.md`
    - `personal/knowledge/Career_Narratives.md`
    - `personal/knowledge/Positioning.md`
- Outputs:
  - Updated `personal/knowledge/Experience_Inventory.md` (as applicable)
  - Updated `personal/knowledge/Career_Narratives.md` (as applicable)
  - Updated `personal/knowledge/Positioning.md` (as applicable)

---

**`archetype_creation.md` — Archetype Creation**
- Purpose: Create a new domain-agnostic, level-agnostic archetype file when no existing archetype fits the target role. The new archetype is immediately usable across all domains; no per-domain authoring required.
- Inputs:
  - `rules/global_rules.md`
  - `rules/registry_archetype.md`
  - `rules/registry_domain.md`
  - `rules/archetypes/Archetype_1_Transformation_Strategy.md` (canonical pattern)
  - `personal/knowledge/Experience_Inventory.md` header (Active Domain)
- Outputs:
  - New archetype file at `rules/archetypes/Archetype_<N>_<Name>.md`
  - Updated `rules/registry_archetype.md`

---

**`domain_creation.md` — Domain Creation**
- Purpose: Create a new domain file (taxonomy, vocabulary, selection criteria, tech stack, per-archetype calibration examples) when extending the repo to a new career domain or new tester.
- Inputs:
  - `rules/global_rules.md`
  - `rules/registry_domain.md`
  - `rules/registry_archetype.md`
  - `rules/domains/clinical_development.md` (canonical pattern)
  - Archetype files from `rules/archetypes/`
  - Representative job descriptions and practitioner sources (research phase)
- Outputs:
  - New domain file at `rules/domains/<slug>.md`
  - Updated `rules/registry_domain.md`

---

### Rules

Rule sets read by skills during execution. Located in `rules/`.

#### Shared reference files

**`global_rules.md`**
- Purpose: Rules loaded by every skill at execution start. Governs phase gating, QC failure handling, source document updates, and standard skill closing.
- Read by:
  - All skills
- Written by:
  - None (manual maintenance)

---

**`judgment_qc.md`**
- Purpose: Judgment failure modes checked at specific phases to catch output that follows formatting rules but misrepresents, miscalibrates, or inflates underlying experience.
- Read by:
  - `role_evaluation`
  - `cv_targeted`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

**`config.md`**
- Purpose: Machine-specific configuration (Python executable path for `python-docx` operations). Must be updated per machine.
- Read by:
  - `cv_targeted`
  - `cv_general`
  - `interview_prep`
- Written by:
  - None (manual maintenance per machine)

---

**`sources.md`**
- Purpose: Research and practitioner citations supporting all skill and rule design decisions. Retained for traceability only.
- Read by:
  - None at runtime
- Written by:
  - None (manual maintenance)

---

#### Registry files

**`registry_skills.md`**
- Purpose: Skill catalog with triggers, prerequisites, completion signals, and state detection guide. The authoritative source for skill routing.
- Read by:
  - `control`
- Written by:
  - None (manual maintenance)

---

**`registry_archetype.md`**
- Purpose: Archetype file catalog and selection criteria.
- Read by:
  - `role_evaluation`
  - `cv_general`
  - `archetype_creation`
  - `domain_creation`
- Written by:
  - `archetype_creation`

---

**`registry_domain.md`**
- Purpose: Domain file catalog and activation criteria.
- Read by:
  - `archetype_creation`
  - `domain_creation`
  - `control` (for Active Domain validation)
- Written by:
  - `domain_creation`

---

**`registry_org_type.md`**
- Purpose: Organization type catalog (large pharma, biotech, CRO, etc.) and selection criteria, used to adjust framing emphasis.
- Read by:
  - `role_evaluation`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

**`registry_company_type.md`**
- Purpose: Company type catalog and adaptive research branches for interview prep.
- Read by:
  - `interview_prep`
- Written by:
  - None (manual maintenance)

---

#### Archetype files (`rules/archetypes/`)

Domain-agnostic, level-agnostic archetype definitions. Files:
- `Archetype_1_Transformation_Strategy.md`
- `Archetype_2_Data_Analytics.md`
- `Archetype_3_Process_Operations.md`
- `Archetype_4_Platform_Technology.md`

**Purpose:** Define archetype identity, match criteria, summary framing pattern, inventory tag priorities, achievement framing pattern, archetype-specific handling, de-emphasis rules, and section order. Apply across all domains; vocabulary and calibration examples come from the active domain file; level voice comes from the content rules file.
- Read by:
  - `role_evaluation`
  - `cv_targeted`
  - `cv_general`
  - `archetype_creation` (canonical pattern)
- Written by:
  - `archetype_creation`

---

#### Domain files (`rules/domains/<slug>.md`)

One flat file per career domain. Each file contains tag taxonomy, domain vocabulary, pack selection criteria, technical proficiencies content, and one calibration example per registered archetype. The active domain is declared in `Experience_Inventory.md` header and governs tag taxonomy for all skills.

Current domain file: `clinical_development.md`

**Purpose:** Provide the domain lens that archetype files reference. Tag taxonomy is authoritative for inventory validation. Vocabulary and calibration examples express archetype framing patterns in the active domain's terminology.
- Read by:
  - `role_evaluation`
  - `cv_targeted`
  - `cv_general`
  - `source_document_update_core` (tag taxonomy validation)
  - `domain_creation` (canonical pattern)
- Written by:
  - `domain_creation`

---

#### CV rules (`rules/cv/`)

**`content_rules_leadership.md`**
- Purpose: Content rules for Associate Director-level and above CV bullets.
- Read by:
  - `cv_targeted`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

**`content_rules_ic.md`**
- Purpose: Content rules for individual contributor CV bullets.
- Read by:
  - `cv_targeted`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

**`format_spec.md`**
- Purpose: Authoritative CV formatting specification (layout, typography, spacing, section structure).
- Read by:
  - `cv_targeted`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

**`qc_checklist.md`**
- Purpose: QC checklist for generated CV content prior to document assembly.
- Read by:
  - `cv_targeted`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

**`dual_archetype.md`**
- Purpose: Rules for handling dual-archetype roles where two archetypes both apply (for example, strategy + analytics).
- Read by:
  - `role_evaluation`
  - `cv_targeted`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

#### Career narrative formats (`rules/career_narratives/`)

Per-format structural rules for narrative entries. Selected at session start based on the entry type. Files:
- `story_star.md` — STAR format
- `story_atola.md` — ATOLA format
- `story_personal.md` — non-work personal stories
- `decision_adr.md` — Architecture Decision Record format
- `decision_personal.md` — personal framing decisions

**Purpose:** Define body structure and content rules for each narrative entry format.
- Read by:
  - `career_narratives_builder`
- Written by:
  - None (manual maintenance)

---

### Templates

Structural templates used by skills during document generation. Located in `templates/`.

---

**`Interview_Completion_Template.md`**
- Purpose: Template for interview round tracking. Pre-populated by `interview_prep` into the per-role `InterviewCompletion` file.
- Read by:
  - `interview_prep`
- Written by:
  - None (manual maintenance)

---

**`Interview_Scratch_Template.md`**
- Purpose: Template for in-interview scratch notes. Pre-populated by `interview_prep` into the per-role `InterviewScratch` file, with header references to the Prep and Completion files.
- Read by:
  - `interview_prep`
- Written by:
  - None (manual maintenance)

---

### Support

One-time scaffolding resources. Not loaded by any skill at runtime. Located in `support/`.

#### Knowledge repo scaffolding (`support/knowledge_repo_scaffolding/`)

Template files copied into `personal/knowledge/` during initial setup. Required because `personal/` is gitignored, so a new user cloning the framework repo has no other way to obtain starter files for their own private knowledge repo.

---

**`README.md`** (scaffolding)
- Purpose: Starter README for the user's private knowledge repo. Explains the purpose of each knowledge document and references the framework-repo schema contract.
- Read by:
  - User during initial setup
- Written by:
  - None in the framework repo (user edits their copy inside the knowledge repo)

---

**`SETUP.md`** (scaffolding)
- Purpose: Canonical setup instructions for the knowledge repo. Copied into `personal/knowledge/` so the user has local documentation of the two-repo workflow and scaffolding provenance.
- Read by:
  - User during initial setup
- Written by:
  - None in the framework repo (user edits their copy inside the knowledge repo)

---

**`.gitignore`** (scaffolding)
- Purpose: Starter `.gitignore` for the knowledge repo. Excludes editor/OS artifacts, scratch directories, and local-only notes.
- Read by:
  - Git, when operating inside the knowledge repo after copy
- Written by:
  - None in the framework repo (user edits their copy inside the knowledge repo)

---

**`Contact_Info.md`** (scaffolding)
- Purpose: Skeleton `Contact_Info.md` with placeholder fields. Used because `Contact_Info.md` has no corresponding builder skill and must be filled manually.
- Read by:
  - User during initial setup (copied into knowledge repo, then populated)
- Written by:
  - None in the framework repo (user edits their copy inside the knowledge repo)

---

### Knowledge Documents

Master source documents holding the user's career content. Located in `personal/knowledge/`. Nested private git repo.

---

**`Experience_Inventory.md`**
- Purpose: Catalog of every task, responsibility, and achievement across the user's career, classified by Capability, Role Level, Org Context, and Outcome. Header declares Active Domain.
- Read by:
  - `role_evaluation`
  - `cv_targeted`
  - `cv_general`
  - `interview_prep`
  - `career_narratives_builder` (optional reference)
  - `positioning_builder` (optional reference)
  - `career_brief` (fallback if Positioning lacks specificity)
  - `source_document_update_workflow`
  - `source_document_update_adhoc`
  - `archetype_creation` (Active Domain header only)
- Written by:
  - `experience_inventory_bootstrap` (initial creation)
  - `source_document_update_workflow` (new entries or enrichment post-session)
  - `source_document_update_adhoc` (new entries or enrichment ad-hoc)
  - `cv_targeted` (Last Used stamps only)
  - `cv_general` (Last Used stamps only)
  - `interview_prep` (Last Used stamps only)

---

**`Career_Narratives.md`**
- Purpose: Library of career stories (STAR, ATOLA, Personal) and decisions (ADR, Personal) used for interview preparation and CV framing.
- Read by:
  - `role_evaluation`
  - `cv_targeted`
  - `cv_general`
  - `interview_prep`
  - `positioning_builder` (optional reference)
  - `source_document_update_workflow`
  - `source_document_update_adhoc`
- Written by:
  - `career_narratives_builder`
  - `source_document_update_workflow`
  - `source_document_update_adhoc`
  - `interview_prep` (Last Used stamps only)

---

**`Positioning.md`**
- Purpose: Strategic positioning, target roles, value proposition, signature themes, and differentiators.
- Read by:
  - `role_evaluation`
  - `cv_targeted`
  - `cv_general`
  - `interview_prep`
  - `career_brief`
  - `source_document_update_workflow`
  - `source_document_update_adhoc`
- Written by:
  - `positioning_builder`
  - `source_document_update_workflow`
  - `source_document_update_adhoc`

---

**`Contact_Info.md`**
- Purpose: Single source of truth for CV contact line values (name, email, phone, location, LinkedIn).
- Read by:
  - `cv_targeted`
  - `cv_general`
- Written by:
  - None (manual maintenance)

---

**`Questions_Library.md`**
- Purpose: Accumulating library of interview questions encountered across sessions, used to seed and refine future interview prep.
- Read by:
  - `interview_prep`
- Written by:
  - `interview_prep`

---

**`SETUP.md`**
- Purpose: User's local copy of knowledge-repo setup instructions, copied from `support/knowledge_repo_scaffolding/SETUP.md` during initial setup. Serves the user across machines or when reinitializing the knowledge repo; the canonical framework-repo copy remains the authoritative source.
- Read by:
  - User during initial setup or cross-machine sync
- Written by:
  - User (manual edits after copy)

---

### Session Artifacts

Transactional per-role artifacts written during skill execution. Located in `personal/sessions/` or a user-designated per-application folder.

---

**`[Company]_[Role]_[YYYY-MM]_SessionLog.md`**
- Purpose: Temporary progress log during role evaluation, used for in-session resume if the user steps away.
- Read by:
  - `role_evaluation` (for resume)
- Written by:
  - `role_evaluation` (deleted at skill close)

---

**`[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`**
- Purpose: Persistent role evaluation result: archetype selection, org type, fit assessment, identified gaps.
- Read by:
  - `cv_targeted`
  - `interview_prep`
- Written by:
  - `role_evaluation`

---

**`[Company]_[Role]_[YYYY-MM]_ContentDecisions.md`**
- Purpose: CV content decisions and resume path for `cv_targeted`; supports session continuity across breaks.
- Read by:
  - `cv_targeted` (on resume)
- Written by:
  - `cv_targeted`

---

**`InterviewPrep_[Company]_[Role]_[YYYY-MM].md`**
- Purpose: Reference prep document: research, alignment map, stories bank, gap handling, anticipated questions.
- Read by:
  - User during prep
  - `interview_capture` (path referenced from scratch file header)
- Written by:
  - `interview_prep`

---

**`InterviewScratch_[Company]_[Role]_[YYYY-MM].md`**
- Purpose: In-round scratch file for live note-taking during an interview. Header references the Prep and Completion files.
- Read by:
  - `interview_capture`
  - `interview_followup`
- Written by:
  - `interview_prep` (blank, created from template)
  - User (populated live during each interview round)

---

**`InterviewCompletion_[Company]_[Role]_[YYYY-MM].md`**
- Purpose: Per-round record: interviewers, Q&A, debrief. One round populated per `interview_capture` invocation.
- Read by:
  - `interview_followup`
  - `interview_capture` (round auto-detection)
- Written by:
  - `interview_prep` (blank, created from template)
  - `interview_capture` (one round populated per invocation)

---

### Outputs

Final deliverables. Located in `outputs/` or a user-designated application folder. Gitignored.

---

**`[Name]_CV_[Company]_[AbbreviatedRole]_[YYYY-MM].docx`**
- Purpose: Role-targeted CV delivered to the applicant.
- Produced by:
  - `cv_targeted`

---

**`CV_General_[descriptor]_[YYYY-MM].docx`**
- Purpose: General CV for broad distribution, recruiter outreach, or networking.
- Produced by:
  - `cv_general`

---

**`InterviewFollowup_[Company]_[Role]_R[N]_[YYYY-MM].md`**
- Purpose: Post-interview follow-up letter for one interview round. One file per recipient; if multiple recipients, recipient last name is appended to the filename.
- Produced by:
  - `interview_followup`

---

## Document Loading Map

Documents are loaded just-in-time. This map defines what is loaded, when, and why, at the phase level. For a flat list of every input and output per skill, see [Framework Components > Skills](#skills) above.

### role_evaluation

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | None — job description, company, and title collected only |
| 2a step 1 | Active domain load | `personal/knowledge/Experience_Inventory.md` header (Active Domain); `rules/domains/<active_domain>.md` |
| 2a step 5 | Archetype identified | `rules/registry_archetype.md`; `rules/cv/dual_archetype.md` if dual-archetype identified |
| 2a step 6 | Archetype file load | primary archetype file from `rules/archetypes/Archetype_<N>_<Name>.md`; secondary archetype file if dual-archetype |
| 2a step 7 | Org type confirmed | `rules/registry_org_type.md`; framing emphasis noted |
| 3a step 1 | Fit evaluation begins | `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md` |
| 3b | Gap rating judgment QC | `rules/judgment_qc.md` |
| Phase 4 | Source update review | Specific knowledge docs loaded only as needed |

### cv_targeted

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md` |
| 1a step 4 | Active domain consistency check | `personal/knowledge/Experience_Inventory.md` header (Active Domain) compared to GapAnalysis-captured domain |
| 2 step 1 | Content generation begins | `rules/cv/content_rules_leadership.md` (AD+) or `rules/cv/content_rules_ic.md` (IC) |
| 2 step 2 | Archetype and domain load | `personal/knowledge/Experience_Inventory.md` header (Active Domain); primary archetype file from `rules/archetypes/Archetype_<N>_<Name>.md`; `rules/domains/<active_domain>.md`; secondary archetype file and `rules/cv/dual_archetype.md` if dual-archetype identified |
| 2 step 3 | Source and judgment constraints | `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md`, `personal/knowledge/Positioning.md`, `rules/judgment_qc.md` (Modes 1-6 apply as generation constraints in Step 5; Mode 8 applies in Step 4) |
| 2 step 6 | Consolidated QC sweep | `rules/cv/qc_checklist.md` |
| 3 step 1 | Document generation begins | `rules/cv/format_spec.md`; `personal/knowledge/Contact_Info.md` |
| 3 step 2 | Python script execution | `rules/config.md` |
| Phase 4 | Source update review | Specific knowledge docs loaded only as needed |

### cv_general

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | None — targeting context collected only |
| 2a step 1 | Archetype selection begins | `rules/registry_archetype.md` |
| 2a step 2 | Archetype and domain load | `personal/knowledge/Experience_Inventory.md` header (Active Domain); primary archetype file from `rules/archetypes/Archetype_<N>_<Name>.md`; `rules/domains/<active_domain>.md`; secondary archetype file and `rules/cv/dual_archetype.md` if dual-archetype identified |
| 2a step 3 | Org type confirmed | `rules/registry_org_type.md`; framing emphasis noted for use in Phase 4a |
| 3a step 1 | Source review begins | `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md` |
| 3a step 3 | Experience architecture judgment QC | `rules/judgment_qc.md` (retained through Phase 4b) |
| 4a step 1 | Content generation begins | `rules/cv/content_rules_leadership.md` (AD+) or `rules/cv/content_rules_ic.md` (IC) |
| 5a step 1 | Document generation begins | `rules/cv/format_spec.md`; `personal/knowledge/Contact_Info.md` |
| 5a step 3 | Python script execution | `rules/config.md` |

### career_narratives_builder

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a step 2 | Format selection | Selected story format file from `rules/career_narratives/`; selected decision format file from `rules/career_narratives/` |
| 1a step 3 | Adding or updating entries | `personal/knowledge/Career_Narratives.md` |
| 1a step 4 | Optional reference load | `personal/knowledge/Experience_Inventory.md` (if user confirms) |

### interview_prep

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a | Session start | `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md` |
| 1a step 4 | Active domain consistency check | `personal/knowledge/Experience_Inventory.md` header (Active Domain) compared to GapAnalysis-captured domain |
| 2a step 1 | Company type identification | `rules/registry_company_type.md` |
| 3a step 1 | Content generation begins | `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md`, `personal/knowledge/Positioning.md` |
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
| 2a step 1 | Generation begins | `personal/knowledge/Positioning.md`; `personal/knowledge/Experience_Inventory.md` only if Positioning.md lacks sufficient specificity |

### interview_capture

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a step 1 | Session start | `InterviewScratch_[Company]_[AbbreviatedRole]_[YYYY-MM].md` (user-supplied path) |
| 1a step 2 | Header path resolution | `InterviewPrep_[Company]_[AbbreviatedRole]_[YYYY-MM].md`, `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].md` (paths read from scratch file header) |
| 1a step 3 | Round auto-detection | `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].md` parsed for unpopulated round |
| 1a step 4 | Anchor material load | Target round section of `InterviewScratch_[Company]_[AbbreviatedRole]_[YYYY-MM].md` |
| 3a step 3 | Writeback | `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].md` saved with target round populated |

### interview_followup

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a step 1 | Session start | `InterviewScratch_[Company]_[AbbreviatedRole]_[YYYY-MM].md` (user-supplied path) |
| 1a step 2 | Header path resolution | `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].md` (path read from scratch file header) |
| 1a step 3 | Round selection | Target round content parsed from `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].md` |

### source_document_update_workflow

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| Session Scope | Scope check | Calling skill's session context (no file load) |
| Procedure load | Procedure delegation | `rules/source_document_update_core.md` |
| Core Step 1 | Identifying updates | Target source documents loaded as needed: `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md`, `personal/knowledge/Positioning.md`; active domain file from `rules/domains/<active_domain>.md` |

### source_document_update_adhoc

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| Session Scope | Scope prompt | No file load; scope gathered from user response |
| Procedure load | Procedure delegation | `rules/source_document_update_core.md` |
| Core Step 1 | Identifying updates | Target source documents loaded as needed: `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md`, `personal/knowledge/Positioning.md`; active domain file from `rules/domains/<active_domain>.md` |

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
| 3a | Archetype file content design | `rules/archetypes/Archetype_1_Transformation_Strategy.md` (canonical pattern); active domain file's Section 1 (tag taxonomy validation) |
| 4a step 1 | File creation | `rules/registry_archetype.md` |
| 5 | Handoff routing | `personal/knowledge/Experience_Inventory.md` header (Active Domain); `rules/registry_domain.md` |

### domain_creation

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1b step 1 | Boundary validation against existing domains | `rules/registry_domain.md` |
| 1b step 5 | Archetype coverage planning | `rules/registry_archetype.md` |
| 3a | Domain file design | `rules/domains/clinical_development.md` (canonical pattern); relevant archetype files from `rules/archetypes/` for calibration example pattern |
| 4a step 1 | File creation and registration | `rules/registry_domain.md` |

### positioning_builder

| Phase | Trigger | Documents Loaded |
|---|---|---|
| Execution start | Skill invoked | `rules/global_rules.md` |
| 1a step 2 | Existing document load (if applicable) | `personal/knowledge/Positioning.md` |
| 1a step 3 | Optional reference load | `personal/knowledge/Experience_Inventory.md`; `personal/knowledge/Career_Narratives.md` (if user confirms) |

---

## Knowledge Document Schemas

The three knowledge documents carry schema metadata that skills read and write. Any skill that adds, cites, or revises content in these files must follow the contract below.

### `personal/knowledge/Experience_Inventory.md`

- Active Domain pointer at the top of the file (`**Active Domain:** <slug>`) declares which domain file governs the tag taxonomy for this inventory. Section 1 of `rules/domains/<active_domain>.md` is the authoritative allowed-value list for Capability, Role Level, Org Context, Outcome, and Org Type. Skills must not infer tag values from any other source.
- Classification appears on separate lines per entry: `Capability:`, `Role Level:`, `Org Context:`, and (optional) `Outcome:`. No inline `Tags:` line. Capability and Outcome allow pipe-separated multi-values on their line; Role Level and Org Context take one value each. Omit the `Outcome:` line entirely when no genuine organizational outcome is attached.
- Every entry carries an `ID:` line as its first line: `EX-NNN` for entries in Section 8 (All Tasks Performed) and `PR-NNN` for entries in Section 10 (Independent & Volunteer Projects). IDs are sequentially assigned per prefix (scan max, increment, zero-pad to 3 digits minimum; widen naturally past 999). IDs are immutable: never reused after deletion, never renumbered. IDs are the stable citation handle used by downstream skills.
- Every entry under "All Tasks Performed" carries `Added: YYYY-MM` (stamped at entry creation) and `Last Used:` (blank at creation, updated on use).
- `Added` is stamped by `experience_inventory_bootstrap` at extraction and by `source_document_update_workflow` and `source_document_update_adhoc` when new entries are added. Historical entries imported before the schema change carry `Added: pre-2026-04`.
- `Last Used` is stamped only by output-producing skills at session close, only after explicit user acceptance of the final output: `cv_targeted` Phase 3, `cv_general` Phase 5a, `interview_prep` Phase 4a. A single YYYY-MM is overwritten each time, no history.

### `personal/knowledge/Career_Narratives.md`

- Metadata header at the top of the file governs allowed values. Tags (Capability) are governed by Section 1 of the active domain file (`rules/domains/<active_domain>.md`). Archetype values come from `rules/registry_archetype.md`. Era values (by company) are listed in the Career_Narratives header itself (narrative-local dimension, not domain-governed). Free-text values are not permitted; unmatched values trigger either a mapping decision or a header/taxonomy extension.
- Every story and decision entry carries a 5-line metadata block directly under the `## [Title]` heading: `Tags:`, `Archetype:`, `Era:`, `Added: YYYY-MM`, `Last Used:`. Entry headings are the title alone, no sequential numbering.
- `Added` is stamped by `career_narratives_builder` at entry creation and by `source_document_update_workflow` and `source_document_update_adhoc` when new narrative entries are added. Historical entries carry `Added: pre-2026-04`.
- `Last Used` is stamped only by `interview_prep` at session close, only after explicit user acceptance of the prep doc. `cv_targeted` and `cv_general` load narratives for reference but do not stamp narrative Last Used.
- Body structure per entry is governed by the format file loaded from `rules/career_narratives/` at session start (STAR, ATOLA, Personal for stories; ADR, Personal for decisions).

### `personal/knowledge/Positioning.md`

- Read whole; no per-entry tags or dates. Single metadata line at the top: `Last Revised: YYYY-MM`, immediately under the document title.
- `positioning_builder` updates this line on every Phase 6a write. Neither `source_document_update_workflow` nor `source_document_update_adhoc` updates this line; incremental positioning edits made via those skills should be followed by a `positioning_builder` pass when accumulated changes warrant a revised date.

---

## Personal Data Storage

**Two-repo design.** This framework repo (`career_development`) holds skills, rules, templates, and the README. It contains no personal data and is safe to push to public or shared remotes. A separate private repo (`career_development_knowledge`) holds your master data: `Experience_Inventory.md`, `Career_Narratives.md`, `Positioning.md`, `Contact_Info.md`, `Questions_Library.md`, and `SETUP.md`. It is cloned into `personal/knowledge/` and version-controlled independently.

**What is gitignored.** `personal/` (entire directory, including `knowledge/` and `sessions/`) and `outputs/` are gitignored by the framework repo. Personal content never gets committed to the framework repo.

**Session artifacts backup.** `personal/sessions/` holds transactional session artifacts (SessionLog, GapAnalysis, ContentDecisions, InterviewPrep, InterviewScratch, InterviewCompletion). These are gitignored. Backup is the user's responsibility; optionally track them in their own repo.

**Outputs backup.** `outputs/` holds final generated deliverables (CV `.docx` files). Gitignored. Backup is the user's responsibility.

**Two-repo commit workflow:**
- Framework changes (skills, rules, README): commit and push in `career_development`
- Master data changes (knowledge documents): commit and push from within `personal/knowledge/` to `career_development_knowledge`

**First-time setup (new user, no existing knowledge repo):**
1. Clone this framework repo: `git clone https://github.com/<your-username>/career_development.git`
2. Create a private GitHub repository for your knowledge data (suggested name: `career_development_knowledge`).
3. Create the `personal/` directory at the framework repo root.
4. Clone your new empty knowledge repo into `personal/knowledge/`: `git clone https://github.com/<your-username>/career_development_knowledge.git personal/knowledge/`
5. Copy the contents of `support/knowledge_repo_scaffolding/` into `personal/knowledge/`. This gives you a starting `README.md`, `SETUP.md`, `.gitignore`, and `Contact_Info.md` skeleton.
6. Commit and push the scaffolding files from within `personal/knowledge/` to the knowledge repo.
7. Create `personal/sessions/` (gitignored, not committed).
8. Create `outputs/` (gitignored, not committed).
9. Update the Python executable path in `rules/config.md` to match the local machine's `python-docx`-enabled environment.
10. Fill in `personal/knowledge/Contact_Info.md` with your personal contact details.
11. Run the `control` skill to start the workflow; it will route you to `experience_inventory_bootstrap` as the first step in building your knowledge base.

**Setup on a new machine (existing knowledge repo):**
1. Clone this framework repo.
2. Create the `personal/` directory at the framework repo root.
3. Clone your existing knowledge repo into `personal/knowledge/`.
4. Create `personal/sessions/` and `outputs/` (both gitignored).
5. Update the Python executable path in `rules/config.md` to match this machine's environment.

**Job descriptions.** Raw job descriptions are stored separately in OneDrive or the user's preferred storage, not in this repo.
