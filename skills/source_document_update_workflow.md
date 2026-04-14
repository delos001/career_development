# Source Document Update — Workflow (Session-Triggered)

## Objective

Capture information surfaced during a calling workflow session that should be added to personal source documents. Keeping source documents current reduces gap closure time in future sessions and ensures positioning and inventory stay aligned with actual experience.

This skill is the workflow-triggered entry point for source document updates. For ad-hoc invocations unrelated to a workflow session, use `skills/source_document_update_adhoc.md` instead.

---

## When to Invoke

Invoked at the close of a workflow skill (`role_evaluation`, `cv_targeted`, `cv_general`, `interview_prep`, `career_narratives_builder`, `positioning_builder`, or similar) where new experience language, framing decisions, gap resolutions, or corrections were surfaced. The calling skill loads this file and defines what "this session" covers.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

*This skill uses Steps, not Phases. Standard Phase Closing does not apply.*

---

## Session Scope

The calling skill has defined the scope of "this session" (the specific phases, interactions, and content this update pass should cover). Confirm the scope is available in context before proceeding. If the scope is not present, halt and flag the gap. Do not infer what the session covered.

---

## Procedure

Load `rules/source_document_update_core.md` and execute Steps 1-5 in order against the session scope defined above. The core file governs Active Domain Load, Criteria for Capture, target documents, format requirements, pre-write QC, and write and confirmation steps.
