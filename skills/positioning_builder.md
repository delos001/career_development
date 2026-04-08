# Positioning Builder Skill

## Objective

Build and maintain `knowledge/Positioning.md` — the personal brand and positioning document that articulates who the user is, how they create value, and how they communicate that value to recruiters, hiring managers, and professional networks. This document is a source for `cv_generation`, interview preparation, and direct professional outreach.

This skill handles three modes:
- **New document:** No Positioning.md exists. Build from scratch, working through all sections.
- **Update sections:** An existing document exists. Revise or deepen specific sections.
- **Full review:** An existing document exists. Review all sections for freshness and coherence, then make targeted updates.

**Boundary with `source_document_update`:** Use that skill for capturing incremental framing language, new positioning statements, or corrections surfaced during a CV or interview session. Use this skill when building a section from scratch, significantly revising a section, or reviewing the document holistically.

---

## Global Rules

**Following Instructions**
Follow this skill exactly. Do not jump phases. Do not write content before the user has reviewed and approved the draft for each section.

When in a phase, complete only steps from that phase. Do not volunteer analysis or content from future phases.

If something is ambiguous, state it explicitly and resolve it with the user before proceeding.

**Document Load Instructions**
Load documents at the phase and step specified. A document is loaded completely when all content is present with identifiable structure — not just a fragment. If a document returns only fragments, run `cat [filepath]` as fallback. Do not proceed with partial content.

**Standard Phase Closing**
At the close of each phase:
- List steps completed and steps not completed
- Confirm with user if any other topics relevant to this phase's outputs should be discussed
- Obtain explicit approval before proceeding to the next phase

**QC Failure Recovery**
If a QC phase identifies a failure, do not proceed. State the specific failure, identify the affected step or output, and present options: (a) return to the prior phase and re-run the failed step, (b) accept the gap with explicit acknowledgment, or (c) stop the session. Wait for explicit user direction before taking any action.

---

## Document Structure

A complete Positioning.md contains three tiers of content. Not every section is required in every version of the document — the user decides what is relevant to their context. The tiers define what to build first and why each section matters.

**Tier 1 — Core Identity (build first)**
The foundational content that everything else builds on. Without these, the communication assets have no coherent basis.
- Brand statement: the one-paragraph synthesis of what you do, for whom, in what context, and with what distinctive approach
- Core philosophy: the principles and mental models that guide how you work
- What makes this different: the specific combination of experience, education, and perspective that makes you unusual at your level

**Tier 2 — Market Context (build second)**
Content that connects your positioning to the external environment and demonstrates relevance.
- Industry/domain trajectory: the shifts happening in your field and where your work intersects them
- Competencies: organized capability inventory by domain
- Role-targeted accomplishments: what you have done in each capability area you target, organized for fast retrieval
- Signature themes: cross-cutting patterns across your career, each with a "use when," core message, and proof point

**Tier 3 — Communication Assets (build third)**
Ready-to-use language for specific outreach contexts. Derived from Tier 1 and Tier 2 — do not build these before the core content is stable.
- Elevator statement: 3-4 sentences for live verbal delivery
- LinkedIn about section: one or two versions for the platform
- Recruiter pitch template: fixed opening, variable middle, fixed close, with customization instructions
- Transition narrative: why you left or are leaving your current role — honest, forward-looking, concise
- Appendix: story-to-theme and theme-to-story matching tables, pitch customization notes

---

## Phase 1a — Session Setup

*(No source documents loaded yet)*

**Step 1 — Confirm mode:**
Ask the user to confirm the session mode: new document, update sections, or full review.

**Step 2 — Load existing document (if applicable):**
If mode is Update or Full Review: load `knowledge/Positioning.md` now. Confirm it loaded completely. If load fails, use bash fallback before proceeding.

**Step 3 — Load supporting documents (optional):**
Ask whether `knowledge/Experience_Inventory.md` and `knowledge/Career_Narratives.md` are available. Offer to load them as references — the Inventory informs competencies and accomplishments; Career_Narratives informs signature themes and proof points. Loading is optional; the skill functions without them. Load any the user confirms and verify each loaded completely.

**Step 4 — Identify scope:**
- For **New document**: confirm the user is ready to work through all three tiers. Note that a complete document may take multiple sessions. Offer to complete Tier 1 in this session and defer Tiers 2 and 3.
- For **Update sections**: ask which specific section(s) the user wants to revise. Confirm the list before proceeding. The skill will work through only those sections.
- For **Full review**: confirm the full document will be reviewed for freshness and coherence. Note that this mode identifies what needs updating — actual revision happens in the same session or a follow-up.

**Step 5 — Confirm readiness:**
State the mode, scope, and what was loaded. Confirm with user before closing.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Core Identity

*(Only for New document mode, or when a Tier 1 section is in scope)*
*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*
*(Skip this phase entirely if no Tier 1 sections are in scope for this session)*

**Step 1 — Brand statement:**
Ask the user to describe what they do, for whom, in what context, and what makes their approach distinctive. Use follow-up questions to draw out specificity — avoid accepting vague answers like "I help organizations improve." Push for: what kind of organizations, what specific problem, what outcome, what is distinctive about how you do it.

Draft a brand statement of one paragraph. Present it and refine with the user until they confirm it accurately reflects their positioning. The brand statement is the foundation for all Tier 3 communication assets — it must be precise.

**Step 2 — Core philosophy:**
Ask the user to articulate the principles that guide how they approach their work. What do they believe about how problems should be diagnosed, how solutions should be designed, how change should be managed? What do they do consistently that others in their field do not?

Draft a philosophy section capturing these principles. This is not a list of values — it is a description of how the user thinks and works. Refine with the user until confirmed.

**Step 3 — What makes this different:**
Ask the user to identify what combination of experience, education, and perspective makes them unusual at their level. This is not a humility exercise — it should state clearly and specifically what is rare about the path they have taken and what that produces.

Draft this section. It should be concrete — name the domains, the credentials, the experiences, the cross-functional capabilities. Refine with the user until confirmed.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Market Context

*(Only for New document mode, or when a Tier 2 section is in scope)*
*(Only after Phase 2a has been explicitly approved, or Phase 1a if Phase 2a was skipped)*
*(State each step before completing the step)*
*(Skip this phase entirely if no Tier 2 sections are in scope for this session)*

**Step 1 — Industry/domain trajectory:**
Ask the user to identify the major shifts happening in their field. What forces are reshaping how organizations in this domain operate? Where is pressure coming from — regulatory, technological, competitive, structural? Where does the user's work intersect these shifts?

Draft an industry trajectory section. It should read as evidence of informed perspective on the field — not a textbook description. The section should explicitly connect the user's work to the shifts described. Refine with the user until confirmed.

**Step 2 — Competencies:**
Ask the user to identify their core capability domains. Organize these into 3-5 domain groups (e.g., Process & Operations, Analytics & Data, Technology & Platforms, Leadership & Transformation). Within each domain, list the specific competencies.

Present the organized competency inventory. Refine with the user — add missing items, remove anything that overstates current capability, ensure domain groupings make sense. Confirm before proceeding.

**Step 3 — Role-targeted accomplishments:**
Ask the user to identify the role archetypes or capability areas they target. For each, list 5-8 accomplishment statements — concise, polished, outcome-oriented. These are not full stories (those live in Career_Narratives.md) — they are fast-retrieval summary statements that demonstrate capability in that area.

If Career_Narratives.md was loaded, draw from it to inform these statements. Draft and refine with the user.

**Step 4 — Signature themes:**
Ask the user to identify 3-5 cross-cutting patterns across their career — recurring strengths that appear across multiple situations, roles, and outcomes. For each theme:
- Name: a short, memorable label
- Use when: the role or question context where this theme is most relevant
- Core message: one to two sentences stating the distinctive value this theme demonstrates
- Proof point: one specific, citable example that demonstrates the theme

If Career_Narratives.md was loaded, use it to identify and support proof points. Draft and refine each theme with the user. The themes must be mutually distinct — if two themes overlap significantly, consolidate them.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — Communication Assets

*(Only for New document mode, or when a Tier 3 section is in scope)*
*(Only after Phase 3a has been explicitly approved, or Phase 1a if earlier phases were skipped)*
*(State each step before completing the step)*
*(Skip this phase entirely if no Tier 3 sections are in scope for this session)*

**Step 1 — Elevator statement:**
Draft a 3-4 sentence elevator statement for live verbal delivery. It must be derivable from the brand statement — not a new invention. It should be natural to say aloud, not read like a written paragraph. Test it: would it hold up in a 30-second window?

Refine with the user until confirmed.

**Step 2 — LinkedIn about section:**
Draft one or two versions of the LinkedIn about section. These are longer than the elevator statement and written for reading, not speaking. They should connect the user's positioning to the work they want to do next, not just summarize what they have done.

Refine with the user. If two versions are drafted, note what distinguishes them and when each would be appropriate.

**Step 3 — Recruiter pitch template:**
Draft a recruiter pitch with three components:
- Fixed opening: 2-3 sentences that are role-agnostic and always delivered the same way
- Variable middle: a template with explicit placeholders for role/company-specific customization, with instructions for filling them in
- Fixed close: 1-2 sentences stating what the user is targeting

Include customization instructions in the appendix that explain how to adapt the variable middle for specific roles, including how to match to a signature theme and select a proof point.

Refine with the user until confirmed.

**Step 4 — Transition narrative (if applicable):**
If the user is between roles or has a recent transition to explain, draft a transition narrative. It should be: honest about the reason, forward-looking about the decision, and free of complaints about individuals, culture, or burnout. It should answer "why are you looking?" without creating doubt about the user's commitment or judgment.

Refine with the user until confirmed. If no transition narrative is needed, skip this step.

**Step 5 — Appendix:**
Compile story-to-theme and theme-to-story matching tables if Signature Themes were built or updated in this session. Update the recruiter pitch customization instructions if the pitch was updated.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 5a.

---

## Phase 5a — Quality Control

*(Only after all in-scope phases have been explicitly approved)*

**Coherence check:** Verify that the communication assets (Tier 3) are derivable from the core content (Tier 1 and 2). The elevator statement should echo the brand statement. The recruiter pitch should reference the signature themes. The LinkedIn about section should reflect the core philosophy and differentiators. Flag any communication asset that introduces framing not grounded in the Tier 1 and 2 content.

**Consistency check:** Verify that the same role scope, seniority level, domain focus, and value proposition appear consistently across all sections. Flag any section where the framing contradicts or significantly diverges from the others.

**Freshness check (Full Review mode only):** For each section, assess whether the content reflects the user's current state. Flag any section that references a role, company, or market context that has materially changed. Do not propose updates — identify what needs attention and let the user decide.

**Honesty check:** Verify that competency claims are accurate to the user's actual experience. Verify that differentiators are specific — not generic statements that any candidate at this level could make. Flag any claim that overstates scope, tenure, or contribution.

State the result of each check. Flag failures explicitly and invoke QC Failure Recovery before proceeding.

**Phase 5a Closing:** Follow Standard Phase Closing. Next phase is Phase 6a.

---

## Phase 6a — Document Write

*(Only after Phase 5a has been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Confirm write scope:**
State exactly which sections will be written or updated. For Update mode, confirm that only the in-scope sections will be modified — existing sections not in scope will not be touched. Confirm with user before writing.

**Step 2 — Write:**
Write each approved section to `knowledge/Positioning.md` at the correct location. For new documents, assemble all sections in tier order. For updates, insert or replace only the confirmed sections. Confirm each write completed successfully.

**Step 3 — Handoff:**
After all writes are complete, confirm the session is complete and summarize what was added or changed.

If positioning work surfaced experience or framing that is not yet captured in `knowledge/Experience_Inventory.md` or `knowledge/Career_Narratives.md`, flag those items and offer to trigger `skills/source_document_update.md`.

**Phase 6a Closing:** Follow Standard Phase Closing. Session complete.
