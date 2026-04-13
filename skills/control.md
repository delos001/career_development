# Control Skill

## Objective

Orient the user within the career development workflow, assess current workflow state, and route to the appropriate skill. This skill serves as the entry point for new users, a navigation aid for returning users, and a mid-workflow "where am I?" check at any point. It reads from `rules/registry_skills.md` for all skill knowledge — skill names, triggers, dependencies, and outputs are defined there, not here.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a

---

## Phase 1a — Load and Assess

*(No documents are loaded before this phase)*

1. Load `rules/registry_skills.md`. Confirm it loaded completely.

2. Determine the user's entry context from their invocation message. Classify it as one of:
   - **Specific intent:** User stated what they want to do (e.g., "I want to evaluate this role," "I have an interview tomorrow," "I need to update my experience docs")
   - **Orientation request:** User is asking where to start, what to do next, or what this workflow does
   - **State check:** User wants to know where they are in an active workflow
   - **Workflow question:** User is asking about a specific skill or how part of the workflow works

   If the invocation message is ambiguous, classify it as Orientation request and proceed. Do not ask the user to clarify before running state detection.

3. Run the State Detection Guide from `rules/registry_skills.md` in order. For each check, determine pass or fail silently — do not interrupt the user during detection. Build a complete state picture before presenting anything.

   While running detection, note:
   - Which knowledge source documents exist and appear populated
   - Which company/role combinations have active artifacts (GapAnalysis, CV, InterviewPrep, InterviewCompletion files)
   - Whether any `personal/sessions/[Company]_[Role]_[YYYY-MM]_SessionLog.md` files exist (in-progress role evaluation sessions)
   - Whether any InterviewCompletion documents have populated rounds (follow-up available)

4. If multiple active roles are detected, list them. You will ask the user which to focus on in Phase 2a before routing.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Orient and Route

*(Only after Phase 1a has been explicitly approved)*

Apply the routing logic below. Present the result clearly and decisively — what state the user is in, what is recommended next, and which skill to invoke. Do not present a menu of all possible skills. Identify the single most appropriate next action. The user can push back, but this skill leads.

---

### Routing by Entry Context and State

---

**Workflow question:**
User asked about a specific skill or how part of the workflow works. Answer the question using the registry entry for the relevant skill — trigger, prerequisites, outputs, and typical next steps. Then ask if they want to proceed to that skill or need anything else. Do not route unless the user confirms.

---

**New user — knowledge base absent or incomplete:**
State detection check 1 fails for one or more knowledge source documents. Present a brief orientation before routing:

"This workflow takes you from raw career history to tailored CVs, interview preparation, and follow-up letters through a structured, human-guided process. Everything builds from three source documents — Experience Inventory, Career Narratives, and Positioning — that all subsequent skills draw from. Once those exist, the workflow supports role evaluation, CV generation, interview preparation, and follow-up letters."

Then state the starting point based on what is missing, in this priority order:
- `experience_inventory_bootstrap` if Experience_Inventory.md is absent or empty
- `career_narratives_builder` if Career_Narratives.md is absent or empty
- `positioning_builder` if Positioning.md is absent or empty

If more than one is missing, route to the first in the priority order above. State which comes after so the user knows the path ahead.

---

**Returning user — knowledge base complete, no active role, no specific intent:**
State detection passes check 1, no active role artifacts found. Ask: "Are you working toward a specific role right now, or would you like to do something else — update your source documents, generate a general CV, or create a career brief?"

Route based on their response using the registry entries.

---

**Returning user — active role in progress, no specific intent:**
State detection identifies one active role with partial completion. Present the state for that role concisely:
- What exists (GapAnalysis, CV, InterviewPrep, InterviewCompletion)
- What is next in the sequence based on the registry Workflow Sequence Overview

Route to the next incomplete step. Do not ask the user to confirm what step they are on — state it and let them push back if wrong.

If multiple active roles were detected in Phase 1a, ask which to focus on before presenting state.

---

**Active SessionLog detected:**
A `[Company]_[Role]_[YYYY-MM]_SessionLog.md` exists in `personal/sessions/`. State:

"There is an active role evaluation session in progress for [Company] — [Role]. You can resume it by triggering `role_evaluation` — it will detect the session log and pick up from where you left off."

If the user also has a specific intent for a different role, handle both: address the open session first, then route to the new intent.

---

**Specific intent — prerequisites met:**
State detection confirms all prerequisites for the requested skill exist. Route directly. State the skill to invoke and provide the handoff information (see Handoff Format below).

---

**Specific intent — prerequisites missing:**
State detection identifies a gap between what the user wants to do and what currently exists. Do not route to the requested skill. Instead:

1. State clearly what is needed before the requested skill can run.
2. Identify which skill produces the missing prerequisite, referencing the registry entry.
3. Offer to route to that prerequisite skill first.
4. Once the user confirms, provide the handoff for the prerequisite skill — not the originally requested skill.

When the prerequisite skill completes and the user returns to the control skill, re-run state detection and route to the originally requested skill.

---

**Standalone request — career_brief or cv_general:**
Confirm the required knowledge documents exist per the registry entry:
- `career_brief`: requires `personal/knowledge/Positioning.md`
- `cv_general`: requires all three knowledge documents

If prerequisites exist, route directly. If not, identify the gap and route to the appropriate builder first.

---

**Source document update request:**
Confirm `personal/knowledge/Experience_Inventory.md` exists. If yes, route directly to `source_document_update`. If not, inform the user that the Experience Inventory must be built first via `experience_inventory_bootstrap`.

---

**Mid-workflow state check ("where am I?"):**
User wants to know their current status. Present a complete state summary for all active roles detected:
- Knowledge base status (which documents exist)
- Per active role: which workflow steps are complete and which remain
- Any open SessionLog sessions
- Any InterviewCompletion documents with populated rounds awaiting a follow-up letter

After presenting the summary, ask: "Where would you like to pick up?"

---

### Handoff Format

Every routing outcome ends with three items stated explicitly:

1. **Skill to invoke:** `skills/[filename].md`
2. **What to bring:** File paths, context, or inputs the skill will need at Phase 1 (e.g., GapAnalysis file path, application folder path, job description)
3. **State note:** Any relevant context from state detection (e.g., "The GapAnalysis for this role is at `personal/sessions/[Company]_[Role]_[YYYY-MM]_GapAnalysis.md`"; "This is your first session for this role — no prior artifacts exist")

Example handoff:
> Invoke `skills/interview_prep.md`. Bring the GapAnalysis file at `personal/sessions/Fortrea_ClinDataStratDelivLead_2025-03_GapAnalysis.md` and the absolute path to your Fortrea application folder. This is a new prep session — no InterviewPrep document exists yet for this role.

---

**Phase 2a Closing:** Follow Standard Phase Closing. This skill does not proceed to further phases — execution passes to the routed skill.
