# Skills Registry

Used by `skills/control.md` to understand the available skill suite, route users to the correct skill, and assess current workflow state. When a skill is added, renamed, or its dependencies change, update this file — the control skill reads from here and should not require changes for routine skill updates.

---

## Workflow Sequence Overview

The typical end-to-end path from a standing start to interview follow-up:

```
[Bootstrap]
experience_inventory_bootstrap → career_narratives_builder → positioning_builder
                                                                      ↓
[Per Role]                                              role_evaluation
                                                       ↙              ↘
                                               cv_targeted       interview_prep
                                                                       ↓
                                                                   followup

[Standalone — any point]
career_brief, cv_general, source_document_update
```

Knowledge builder skills (experience_inventory_bootstrap, career_narratives_builder, positioning_builder) run once and are maintained over time. Role-specific skills (role_evaluation through followup) run per application. Utility and standalone skills run on demand. Rules builder skills (archetype_creation, domain_creation) extend the repo itself — invoked only when the available archetype or domain coverage does not fit a target role; not part of per-role workflow.

---

## State Detection Guide

The control skill uses the following ordered checks to determine where a user is in the workflow. Check in order — the first failing condition identifies the gap.

1. **Knowledge base complete?**
   Check: `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md`, `personal/knowledge/Positioning.md` all exist with populated content.
   If no: route to the appropriate knowledge builder skill(s).

2. **Role target identified?**
   Check: User has provided or referenced a company name and role title.
   If no: ask the user what role or context they are working toward before proceeding.

3. **Role evaluation complete?**
   Check: `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md` exists for the target role.
   If no: route to `role_evaluation`.

4. **CV generated?**
   Check: A CV file matching `outputs/*CV*[Company]*[Role]*.docx` exists for the target role.
   If no: `cv_targeted` is available. Ask if the user wants to generate the CV.

5. **Interview prep complete?**
   Check: `InterviewPrep_[Company]_[Role]_[YYYY-MM].docx` exists in the user's application folder.
   If no: `interview_prep` is available if an interview is scheduled or approaching.

6. **Interview round completed?**
   Check: User confirms at least one round of the InterviewCompletion document has been filled in.
   If yes: `followup` is available.

---

## Skill Entries

---

### Experience Inventory Bootstrap

**File:** `skills/experience_inventory_bootstrap.md`
**Category:** Bootstrap
**Standalone:** Yes — no prior skills required

**Trigger:** User is starting from scratch with no structured experience documentation; has raw CVs, resumes, or career history documents and wants to build the Experience Inventory for the first time; `personal/knowledge/Experience_Inventory.md` does not exist or is empty.

**Prerequisites:**
- Raw career source documents provided by the user (old CVs, resumes, or equivalent)

**Completion Signal:** `personal/knowledge/Experience_Inventory.md` exists with populated role entries and tag annotations.

**Outputs:**
- `personal/knowledge/Experience_Inventory.md`

**Typical Next Steps:** `career_narratives_builder`, `positioning_builder`

---

### Career Narratives Builder

**File:** `skills/career_narratives_builder.md`
**Category:** Knowledge Builder
**Standalone:** Yes — can run independently, but Experience Inventory should exist first for best results

**Trigger:** User wants to build or update their stories and decisions library; preparing for interviews; `personal/knowledge/Career_Narratives.md` does not exist or needs new entries added.

**Prerequisites:**
- `personal/knowledge/Experience_Inventory.md` recommended but not blocking

**Completion Signal:** `personal/knowledge/Career_Narratives.md` exists with populated story and decision entries.

**Outputs:**
- `personal/knowledge/Career_Narratives.md`

**Typical Next Steps:** `positioning_builder`, `role_evaluation`

---

### Positioning Builder

**File:** `skills/positioning_builder.md`
**Category:** Knowledge Builder
**Standalone:** Yes — can run independently, but Experience Inventory and Career Narratives should exist first for best results

**Trigger:** User wants to build or update their strategic positioning, framing statements, and recruiter pitch; `personal/knowledge/Positioning.md` does not exist or needs updating.

**Prerequisites:**
- `personal/knowledge/Experience_Inventory.md` recommended
- `personal/knowledge/Career_Narratives.md` recommended

**Completion Signal:** `personal/knowledge/Positioning.md` exists with populated positioning statements and signature themes.

**Outputs:**
- `personal/knowledge/Positioning.md`

**Typical Next Steps:** `role_evaluation`, `career_brief`

---

### Role Evaluation

**File:** `skills/role_evaluation.md`
**Category:** Output Delivery
**Standalone:** No — requires knowledge source documents

**Trigger:** User has a job description and wants to evaluate fit before deciding whether to apply; assessing role alignment against established experience and positioning.

**Prerequisites:**
- `personal/knowledge/Experience_Inventory.md`
- `personal/knowledge/Career_Narratives.md`
- `personal/knowledge/Positioning.md`
- Job description provided by user

**Completion Signal:** `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md` exists for the target role.

**Outputs:**
- `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`
- `personal/sessions/[Company]_[Role]_[YYYY-MM]_SessionLog.md` (temporary — deleted at skill close)

**Typical Next Steps:** `cv_targeted`, `interview_prep` (can proceed to either or both)

---

### CV Targeted

**File:** `skills/cv_targeted.md`
**Category:** Output Delivery
**Standalone:** No — requires GapAnalysis file from role_evaluation

**Trigger:** User has completed role evaluation and wants to generate a tailored CV for the target role.

**Prerequisites:**
- `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`

**Completion Signal:** `outputs/[Name]_CV_[Company]_[AbbreviatedRole]_[YYYY-MM].docx` exists.

**Outputs:**
- Tailored CV `.docx` saved to `outputs/`
- `personal/knowledge/Experience_Inventory.md` — `Last Used: YYYY-MM` stamped on every entry cited in the accepted CV (Phase 3a closing, post user acceptance)

**Typical Next Steps:** `interview_prep`

---

### CV General

**File:** `skills/cv_general.md`
**Category:** Output Delivery
**Standalone:** Yes relative to role — no job description or GapAnalysis required, but knowledge source documents must exist

**Trigger:** User wants a generalized CV not tied to a specific role; recruiter outreach; broad job search distribution.

**Prerequisites:**
- `personal/knowledge/Experience_Inventory.md`
- `personal/knowledge/Career_Narratives.md`
- `personal/knowledge/Positioning.md`

**Completion Signal:** `outputs/CV_General_[descriptor]_[YYYY-MM].docx` exists.

**Outputs:**
- General CV `.docx` saved to `outputs/`
- `personal/knowledge/Experience_Inventory.md` — `Last Used: YYYY-MM` stamped on every entry cited in the accepted CV (Phase 5a closing, post user acceptance)

**Typical Next Steps:** None — standalone output

---

### Interview Prep

**File:** `skills/interview_prep.md`
**Category:** Output Delivery
**Standalone:** No — requires GapAnalysis file from role_evaluation

**Trigger:** User has an interview scheduled or approaching and wants to prepare; has completed role evaluation for the target role.

**Prerequisites:**
- `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`

**Completion Signal:** `InterviewPrep_[Company]_[AbbreviatedRole]_[YYYY-MM].docx` exists in the user's application folder.

**Outputs:**
- `InterviewPrep_[Company]_[AbbreviatedRole]_[YYYY-MM].docx` — reference document
- `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].docx` — editable round-tracking document pre-populated with questions
- `personal/knowledge/Questions_Library.md` updated
- `personal/knowledge/Career_Narratives.md` — `Last Used: YYYY-MM` stamped on every narrative cited in the Stories Bank, Alignment Map, or Gap Handling Language (Phase 4a closing, post user acceptance)
- `personal/knowledge/Experience_Inventory.md` — `Last Used: YYYY-MM` stamped on every inventory entry cited in the Alignment Map, Gap Handling Language, or supporting a Stories Bank entry (Phase 4a closing, post user acceptance)

**Typical Next Steps:** `followup` (after completing at least one interview round)

---

### Follow-Up Letter

**File:** `skills/followup.md`
**Category:** Output Delivery
**Standalone:** No — requires a populated InterviewCompletion document

**Trigger:** User has completed an interview round and wants to write a follow-up letter; InterviewCompletion document has at least one round filled in.

**Prerequisites:**
- `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYY-MM].docx` with at least one round populated

**Completion Signal:** `Followup_[Company]_[AbbreviatedRole]_Round[N]_[YYYY-MM].md` exists in the user's application folder.

**Outputs:**
- Follow-up letter `.md` saved to application folder (one per round; individual files per recipient if multiple letters generated)

**Typical Next Steps:** `followup` again for subsequent interview rounds

---

### Career Brief

**File:** `skills/career_brief.md`
**Category:** Output Delivery
**Standalone:** Yes

**Trigger:** User needs a short professional bio or summary paragraph for recruiter outreach, networking introductions, speaker profiles, or similar contexts where a standalone written summary is needed.

**Prerequisites:**
- `personal/knowledge/Positioning.md`

**Completion Signal:** Output is plain text displayed in chat — no file is generated.

**Outputs:**
- Plain text short bio (150-200 words, third-person) or professional summary paragraph (4-6 lines, implicit first-person) displayed in chat for copy-paste

**Typical Next Steps:** None — standalone output

---

### Source Document Update

**File:** `skills/source_document_update.md`
**Category:** Utility
**Standalone:** Yes — but typically triggered from within other skills at session close

**Trigger:** New experience descriptions, framing decisions, gap resolutions, or positioning language surfaced during any session that should be captured in source documents before the session closes; also triggered explicitly by other skills at Phase close.

**Prerequisites:**
- At least one target source document exists: `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md`, or `personal/knowledge/Positioning.md`

**Completion Signal:** No specific file signal — source documents are updated in place.

**Outputs:**
- Updated `personal/knowledge/Experience_Inventory.md`, `personal/knowledge/Career_Narratives.md`, or `personal/knowledge/Positioning.md` as applicable

**Typical Next Steps:** None — returns to the calling skill or closes

---

### Archetype Creation

**File:** `skills/archetype_creation.md`
**Category:** Rules Builder
**Standalone:** No — internally triggered only
**Direct routing by control skill:** Never. This skill is triggered from within `role_evaluation` or `cv_general` when no existing archetype matches the target role. The control skill does not route to it directly.

**Trigger:** No existing archetype in `rules/registry_archetype.md` fits the target role; `role_evaluation` or `cv_general` has stalled at archetype selection.

**Scope:** Produces a level-agnostic archetype skeleton only. Does not produce domain pack content (match criteria, summary framing, tag priorities, calibration, de-emphasis). A pack entry must exist in the active domain before the new archetype can be used in CV generation; pack entries are created by `domain_creation` (when a new domain is being stood up) or by authoring per-archetype pack entries into an existing domain directory. Phase 5 of this skill routes the user to the appropriate path.

**Prerequisites:**
- Active `role_evaluation` or `cv_general` session, or independent invocation with job description in hand
- All existing archetypes reviewed and confirmed as poor fits

**Completion Signal:** New skeleton file created at `rules/archetypes/Archetype_<N>_<Name>.md`; `rules/registry_archetype.md` updated with new entry.

**Outputs:**
- New archetype skeleton file at `rules/archetypes/Archetype_<N>_<Name>.md`
- Updated `rules/registry_archetype.md`

**Typical Next Steps:** Pack entry creation (via `domain_creation` for a new domain, or manual pack entry authoring for an existing domain), then resume `role_evaluation` or `cv_general` from archetype selection step

---

### Domain Creation

**File:** `skills/domain_creation.md`
**Category:** Rules Builder
**Standalone:** Yes — invoked when a new career domain is needed
**Direct routing by control skill:** Never. This skill is triggered when a domain scope mismatch is flagged during `role_evaluation`, when the user pivots to a career domain not currently covered, or when the repo is being extended to support a new tester. The control skill does not route to it directly.

**Trigger:** No existing domain in `rules/registry_domain.md` covers the target roles; `role_evaluation` flagged a domain scope mismatch; the user is extending the repo to a new career domain or new tester.

**Scope:** Produces one domain header file (`rules/domains/<slug>/domain.md`) and one pack entry per registered archetype and level (two per archetype). Does not create or modify archetype skeletons; those are governed by `archetype_creation`. Does not flip the Active Domain pointer in `personal/knowledge/Experience_Inventory.md`; activation is an explicit user action after the skill completes.

**Prerequisites:**
- User-supplied scope motivation (what domain and why)
- Access to representative job descriptions and practitioner sources for the domain (research phase is gated; source plan must be approved before research executes)

**Completion Signal:** `rules/domains/<slug>/` directory exists with `domain.md` and all archetype pack entries; `rules/registry_domain.md` updated with new entry.

**Outputs:**
- New domain pack directory at `rules/domains/<slug>/` with `domain.md` + one pack entry per archetype and level
- Updated `rules/registry_domain.md`

**Typical Next Steps:** Inventory migration review (if existing inventory entries use tags not present in the new domain's taxonomy), then user edits the Active Domain pointer in `personal/knowledge/Experience_Inventory.md` to activate the new domain

---

### Control

**File:** `skills/control.md`
**Category:** Navigation
**Standalone:** Yes — entry point at any stage of the workflow
**Direct routing by control skill:** The control skill does not route to itself. It is the router.

**Trigger:** User is starting fresh and does not know where to begin; user wants to know where they are in an active workflow; user wants to be routed to the right skill based on current state.

**Prerequisites:**
- None — can be invoked at any point including before any other skill has run

**Completion Signal:** No file produced — output is a routing decision and handoff.

**Outputs:**
- Workflow state summary presented to user
- Routing decision and handoff to the appropriate skill

**Typical Next Steps:** Whichever skill the user is routed to

---

## Adding New Skills

When a new skill is added to the workflow:
1. Add a full entry to this registry following the structure above
2. Update the Workflow Sequence Overview diagram if the skill fits into the sequence
3. Update the State Detection Guide if the skill produces a file-based completion signal that should be checked
4. Update `CLAUDE.md` skills table and `README.md` skills table and loading map
5. Do not modify `skills/control.md` unless the routing logic itself needs to change — skill knowledge lives here, not there
