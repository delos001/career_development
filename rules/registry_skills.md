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

Knowledge builder skills (experience_inventory_bootstrap, career_narratives_builder, positioning_builder) run once and are maintained over time. Role-specific skills (role_evaluation through followup) run per application. Utility and standalone skills run on demand.

---

## State Detection Guide

The control skill uses the following ordered checks to determine where a user is in the workflow. Check in order — the first failing condition identifies the gap.

1. **Knowledge base complete?**
   Check: `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, `knowledge/Positioning.md` all exist with populated content.
   If no: route to the appropriate knowledge builder skill(s).

2. **Role target identified?**
   Check: User has provided or referenced a company name and role title.
   If no: ask the user what role or context they are working toward before proceeding.

3. **Role evaluation complete?**
   Check: `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md` exists for the target role.
   If no: route to `role_evaluation`.

4. **CV generated?**
   Check: A CV file matching `outputs/*CV*[Company]*[Role]*.docx` exists for the target role.
   If no: `cv_targeted` is available. Ask if the user wants to generate the CV.

5. **Interview prep complete?**
   Check: `InterviewPrep_[Company]_[Role]_[YYYYMM].docx` exists in the user's application folder.
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

**Trigger:** User is starting from scratch with no structured experience documentation; has raw CVs, resumes, or career history documents and wants to build the Experience Inventory for the first time; `knowledge/Experience_Inventory.md` does not exist or is empty.

**Prerequisites:**
- Raw career source documents provided by the user (old CVs, resumes, or equivalent)

**Completion Signal:** `knowledge/Experience_Inventory.md` exists with populated role entries and tag annotations.

**Outputs:**
- `knowledge/Experience_Inventory.md`

**Typical Next Steps:** `career_narratives_builder`, `positioning_builder`

---

### Career Narratives Builder

**File:** `skills/career_narratives_builder.md`
**Category:** Knowledge Builder
**Standalone:** Yes — can run independently, but Experience Inventory should exist first for best results

**Trigger:** User wants to build or update their stories and decisions library; preparing for interviews; `knowledge/Career_Narratives.md` does not exist or needs new entries added.

**Prerequisites:**
- `knowledge/Experience_Inventory.md` recommended but not blocking

**Completion Signal:** `knowledge/Career_Narratives.md` exists with populated story and decision entries.

**Outputs:**
- `knowledge/Career_Narratives.md`

**Typical Next Steps:** `positioning_builder`, `role_evaluation`

---

### Positioning Builder

**File:** `skills/positioning_builder.md`
**Category:** Knowledge Builder
**Standalone:** Yes — can run independently, but Experience Inventory and Career Narratives should exist first for best results

**Trigger:** User wants to build or update their strategic positioning, framing statements, and recruiter pitch; `knowledge/Positioning.md` does not exist or needs updating.

**Prerequisites:**
- `knowledge/Experience_Inventory.md` recommended
- `knowledge/Career_Narratives.md` recommended

**Completion Signal:** `knowledge/Positioning.md` exists with populated positioning statements and signature themes.

**Outputs:**
- `knowledge/Positioning.md`

**Typical Next Steps:** `role_evaluation`, `career_brief`

---

### Role Evaluation

**File:** `skills/role_evaluation.md`
**Category:** Output Delivery
**Standalone:** No — requires knowledge source documents

**Trigger:** User has a job description and wants to evaluate fit before deciding whether to apply; assessing role alignment against established experience and positioning.

**Prerequisites:**
- `knowledge/Experience_Inventory.md`
- `knowledge/Career_Narratives.md`
- `knowledge/Positioning.md`
- Job description provided by user

**Completion Signal:** `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md` exists for the target role.

**Outputs:**
- `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md`
- `outputs/SessionLog_[Company]_[Role]_[YYYYMM].md` (temporary — deleted at skill close)

**Typical Next Steps:** `cv_targeted`, `interview_prep` (can proceed to either or both)

---

### CV Targeted

**File:** `skills/cv_targeted.md`
**Category:** Output Delivery
**Standalone:** No — requires GapAnalysis file from role_evaluation

**Trigger:** User has completed role evaluation and wants to generate a tailored CV for the target role.

**Prerequisites:**
- `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md`

**Completion Signal:** `outputs/[Name]_CV_[Company]_[AbbreviatedRole]_[YYYYMM].docx` exists.

**Outputs:**
- Tailored CV `.docx` saved to `outputs/`

**Typical Next Steps:** `interview_prep`

---

### CV General

**File:** `skills/cv_general.md`
**Category:** Output Delivery
**Standalone:** Yes relative to role — no job description or GapAnalysis required, but knowledge source documents must exist

**Trigger:** User wants a generalized CV not tied to a specific role; recruiter outreach; broad job search distribution.

**Prerequisites:**
- `knowledge/Experience_Inventory.md`
- `knowledge/Career_Narratives.md`
- `knowledge/Positioning.md`

**Completion Signal:** `outputs/CV_General_[descriptor]_[YYYYMM].docx` exists.

**Outputs:**
- General CV `.docx` saved to `outputs/`

**Typical Next Steps:** None — standalone output

---

### Interview Prep

**File:** `skills/interview_prep.md`
**Category:** Output Delivery
**Standalone:** No — requires GapAnalysis file from role_evaluation

**Trigger:** User has an interview scheduled or approaching and wants to prepare; has completed role evaluation for the target role.

**Prerequisites:**
- `outputs/GapAnalysis_[Company]_[Role]_[YYYYMM].md`

**Completion Signal:** `InterviewPrep_[Company]_[AbbreviatedRole]_[YYYYMM].docx` exists in the user's application folder.

**Outputs:**
- `InterviewPrep_[Company]_[AbbreviatedRole]_[YYYYMM].docx` — reference document
- `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYYMM].docx` — editable round-tracking document pre-populated with questions
- `knowledge/Questions_Library.md` updated

**Typical Next Steps:** `followup` (after completing at least one interview round)

---

### Follow-Up Letter

**File:** `skills/followup.md`
**Category:** Output Delivery
**Standalone:** No — requires a populated InterviewCompletion document

**Trigger:** User has completed an interview round and wants to write a follow-up letter; InterviewCompletion document has at least one round filled in.

**Prerequisites:**
- `InterviewCompletion_[Company]_[AbbreviatedRole]_[YYYYMM].docx` with at least one round populated

**Completion Signal:** `Followup_[Company]_[AbbreviatedRole]_Round[N]_[YYYYMM].md` exists in the user's application folder.

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
- `knowledge/Positioning.md`

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
- At least one target source document exists: `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, or `knowledge/Positioning.md`

**Completion Signal:** No specific file signal — source documents are updated in place.

**Outputs:**
- Updated `knowledge/Experience_Inventory.md`, `knowledge/Career_Narratives.md`, or `knowledge/Positioning.md` as applicable

**Typical Next Steps:** None — returns to the calling skill or closes

---

### Archetype Creation

**File:** `skills/archetype_creation.md`
**Category:** Rules Builder
**Standalone:** No — internally triggered only
**Direct routing by control skill:** Never. This skill is triggered from within `role_evaluation` when no existing archetype matches the target role. The control skill does not route to it directly.

**Trigger:** No existing archetype in `rules/registry_archetype.md` fits the target role; `role_evaluation` has stalled at archetype selection.

**Prerequisites:**
- Active `role_evaluation` session
- Job description available
- All existing archetypes reviewed and confirmed as poor fits

**Completion Signal:** New archetype file created in `rules/`; `rules/registry_archetype.md` updated with new entry.

**Outputs:**
- New archetype instruction file in `rules/`
- Updated `rules/registry_archetype.md`

**Typical Next Steps:** Resume `role_evaluation` from archetype selection step

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
