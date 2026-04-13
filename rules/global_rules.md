# Global Rules

Shared rules that govern all skills in this workflow. Every skill loads this file at execution start before taking any other action.

---

## Following Instructions

Follow the active skill exactly. Steps will not be overridden by judgment without explicit user approval. Inference will not be applied in a way that violates the active skill without explicit user approval.

If something is ambiguous, do not use judgment or inference without approval and state the ambiguity explicitly before moving to another step or phase.

When in a phase, complete only steps from that phase. Do not perform steps or volunteer analysis from future phases.

State each step before completing it. The user should know what is about to happen before it happens.

---

## Document Load Instructions

Document load instructions apply at any point in the active skill.

Load documents at the phase and step specified in the active skill — no earlier, no later. This is a just-in-time loading workflow. Refer to `README.md` for the full loading map.

A document is loaded completely when all content is present with identifiable structure — not just a fragment. A document returning only fragments without structure must be flagged as a load failure.

If any document fails loading, do not proceed using partial content:
- Run bash with `cat [filepath]` for each failed document
- Confirm the full document content is readable before proceeding
- If the bash fallback also fails, report the specific file and error — do NOT proceed until resolved

If a read returns incomplete content mid-phase, stop, run the fallback, confirm availability, then continue. Do not silently proceed with degraded source material.

---

## Standard Phase Closing

Applies to all action phases listed in the active skill.

At the close of each action phase:
- List steps completed and steps not completed
- Confirm with user if any other topics relevant to this phase's outputs should be discussed
- Obtain explicit approval before proceeding to the next phase

---

## QC Failure Recovery

If a QC phase identifies that a step was incomplete, non-compliant, or that output does not conform to skill instructions, do not proceed. State the specific failure clearly, identify which step or output is affected, and present the user with options: (a) return to the prior phase and re-run the failed step, (b) accept the gap with explicit acknowledgment and proceed, or (c) stop the session. Do not invent a resolution or silently continue. Wait for explicit user direction before taking any action.

---

## Standard QC Document Verification

If any documents were loaded in the previous phase, verify Document Load Instructions were followed. State verification status for each document: document name, verification method, result (pass/fail/fallback used), and structural element confirmed. All documents must pass verification before proceeding.

---

## Workflow Context Check

At the start of execution, before Phase 1a, determine whether this is a fresh invocation or a continuation of a prior session or parent workflow.

- **Fresh invocation:** proceed to Phase 1a (or the equivalent session setup phase for this skill).
- **Triggered from within another skill** (e.g., `source_document_update` triggered by `cv_targeted`): confirm the parent session context is available. The calling skill should have defined the scope of "this session." If that scope is not present in context, flag the gap before proceeding — do not infer what the session covered.
- **Resuming a prior session:** if the active skill has a Session Continuity rule, that rule governs resumption. If no Session Continuity rule is defined, start from Phase 1a.
