# Source Document Update — Ad-Hoc (User-Triggered)

## Objective

Capture new experience, framing language, stories, decisions, positioning shifts, or enrichment of existing entries into the personal source documents, invoked on demand without a prior workflow session as the source.

This skill is the ad-hoc entry point for source document updates. For invocations triggered at the close of a workflow skill, use `skills/source_document_update_workflow.md` instead.

---

## When to Invoke

User wants to update one or more knowledge documents ad-hoc. Common triggers:
- "I did something important today and want to capture it."
- "I want to add a decision or story I just remembered."
- "I want to enrich some existing inventory entries with Context or Impact."
- "I want to clean up entries flagged for enrichment during bootstrap."

This skill can also be invoked by the control skill in response to a generic "I want to update my knowledge docs" request.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

*This skill uses Steps, not Phases. Standard Phase Closing does not apply.*

---

## Session Scope

Ad-hoc invocations have no calling workflow; the session scope must be established explicitly at entry. Before loading the procedural core, prompt the user:

1. **What do you want to capture or update?**
   - New entries (new experience, new stories, new positioning language)
   - Enrichment of existing entries (Context, Impact, tags, or narrative body content)
   - Both

2. **Where is the source material coming from?**
   - Something that happened recently and should be captured atomically
   - A role or period you want to revisit and flesh out
   - A pre-identified target list (e.g., entries flagged for enrichment during `experience_inventory_bootstrap` close-out)
   - Corrections or framing revisions surfaced since the last update

Record the user's answers as the session scope. If the user supplies a pre-identified target list, use it as the starting point for Step 1 of the core procedure rather than re-identifying targets from scratch.

---

## Procedure

Load `rules/source_document_update_core.md` and execute Steps 1-5 in order against the session scope established above. The core file governs Active Domain Load, Criteria for Capture, target documents, format requirements, pre-write QC, and write and confirmation steps.
