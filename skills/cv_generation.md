# CV Generation Skill

## Objective

Generate targeted CVs to secure interviews for roles that align with established experience, education, and positioning. This skill covers role understanding, fit evaluation, gap closure, content generation, document production, and a feedback mechanism to fill gaps in knowledge documents.

---

## Global Rules

**Following Instructions**
Follow this skill exactly. Every step is dictated by the skill. Steps will not be overridden by judgment without explicit user approval. Inference will not be applied in a way that violates this skill without explicit user approval.

When in a phase, complete only steps from that phase. Do not perform steps or volunteer analysis from future phases.

Do not proceed to the next phase without explicit approval.

If something is ambiguous, ask questions immediately before moving to another step or phase.  Do not use judgment or inference without user approval.

**Document Load Instructions**
Load documents at the phase and step specified in this skill — no earlier, no later. This is a just-in-time loading workflow. Refer to `README.md` for the full loading map.

A document is loaded completely when all content is present with identifiable structure — not just a fragment. A document returning only fragments without structure must be flagged as a load failure.

If any document fails loading, do not proceed using partial content:
- Run bash with `cat [filepath]` for each failed document
- Confirm the full document content is readable before proceeding
- If the bash fallback also fails, report the specific file and error — do NOT proceed until resolved

This applies at any point in the skill. If a read returns incomplete content mid-phase, stop, run the fallback, confirm availability, then continue. Do not silently proceed with degraded source material.

**Standard Phase Closing — Action Phases (1a, 2a, 2b, 3a, 3b, 4a, 4b, 5a, 5b)**
At the close of each action phase:
- List steps completed and steps not completed
- Confirm with user if any other topics relevant to this phase's outputs should be discussed
- Obtain explicit approval before proceeding to the next phase

**QC Failure Recovery**
If a QC phase identifies that a step was incomplete, non-compliant, or that output does not conform to skill instructions, do not proceed. State the specific failure clearly, identify which step or output is affected, and present the user with options: (a) return to the prior phase and re-run the failed step, (b) accept the gap with explicit acknowledgment and proceed, or (c) stop the session. Do not invent a resolution or silently continue. Wait for explicit user direction before taking any action.

**Standard QC Document Verification**
If any documents were loaded in the previous phase, verify Document Load Instructions were followed. State verification status for each document: document name, verification method, result (pass/fail/fallback used), and structural element confirmed. All documents must pass verification before proceeding.

**QC Phases (1b, 2b, 3b, 4b, 5b)**
All QC procedures are performed independently of steps taken in the previous non-QC phase. For each step or checklist item, identify a logical method or rule that allows independent verification. State the QC rule used and the outcome. Steps and checklist items are not considered enforced until independent QC confirms compliance.

State any judgment calls or inferred actions performed during this phase or the previous phase.

---

## Phase 1a — Session Setup

*(No documents are loaded in this phase)*

1. Confirm the job description has been provided. If not, request it now and do not proceed until received.

2. If the company name and title are not clearly stated at the beginning of the job description, request them now and do not proceed until received.

3. Confirm company and title information is in hand and state them explicitly before closing this phase.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Alignment Analysis

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

1. Read the provided job description carefully.

2. Review the job description and propose the role level (IC, AD, Dir, Sr. Dir, VP, etc.). If not explicitly stated in the title, infer it from required experience, scope of responsibilities, and reporting structure. State the inferred level with rationale and obtain explicit agreement before moving forward. The agreed role level governs seniority of voice, scope framing, achievement selection, and content rules throughout all subsequent phases.

3. If role level is confirmed as Associate Director or above, load `knowledge/CV_General_Leadership.md` now. Confirm it loaded completely before proceeding.

4. Research the company, industry, and role using web search to develop an expert-level understanding of what this position actually requires — including company stage and culture, competitive landscape, organizational context, and what success looks like in this type of role at this type of company.

5. Identify the 4-5 most critical requirements or themes in the job description.

6. Identify the role archetype from the following four options and state the framing angle:

   - **Transformation & Strategy** — enterprise-level change, operating model redesign, strategic program leadership
   - **Data & Analytics** — clinical data strategy, data governance, analytics platform development, data science enablement
   - **Process & Operations** — process excellence, clinical operations, Lean/Six Sigma, execution and efficiency
   - **Platform & Technology** — technology strategy, platform implementation, system integration, vendor and tool ecosystem

   If the role spans two archetypes, identify a primary and secondary. The primary drives section order, summary framing, and achievement selection. The secondary informs emphasis within individual achievements where both dimensions are genuinely present. State both explicitly with rationale.

   Then load the archetype instruction document matching the confirmed primary archetype AND the role level confirmed in Step 2:

   Leadership (Associate Director and above):
   - Transformation & Strategy → `context/Archetype_1_Transformation_Strategy.md`
   - Data & Analytics → `context/Archetype_2_Data_Analytics.md`
   - Process & Operations → `context/Archetype_3_Process_Operations.md`
   - Platform & Technology → `context/Archetype_4_Platform_Technology.md`

   Individual Contributor:
   - Transformation & Strategy → `context/Archetype_1_IC_Transformation_Strategy.md`
   - Data & Analytics → `context/Archetype_2_IC_Data_Analytics.md`
   - Process & Operations → `context/Archetype_3_IC_Process_Operations.md`
   - Platform & Technology → `context/Archetype_4_IC_Platform_Technology.md`

   If a dual-archetype was identified, also load the secondary archetype document using the same role-level logic. Confirm each loaded completely before proceeding. If loading fails, follow Document Load Instructions fallback.

7. Identify the most appropriate CV format reference and state why:
   - **Large Enterprise Established** — for established pharma, large CROs, or mature biotech
   - **Mid Size Scale-Up** — for growth-stage biotech or companies undergoing significant transformation

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Role Level: Confirm the role level was explicitly stated or inferred with rationale, and that explicit user agreement was obtained. If agreement is not documented, flag as a blocking issue and invoke QC Failure Recovery.

Perform QC per Global Rules:
- **QC Failure Recovery**
- **Standard QC Document Verification**
- **QC Phases**

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Fit Evaluation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

1. Load the following source documents now. Confirm each loaded completely before proceeding:
   - `knowledge/Experience_Inventory.md`
   - `knowledge/Accomplishments.md`
   - `knowledge/CV_Verbose.md`
   - `knowledge/Positioning.md`

2. Using the loaded source documents, map each critical requirement identified in Phase 2a to the most relevant experience, citing the source document and specific achievement. Every claim must be traceable to a source document.

3. Flag gaps, weak matches, or cases where language needs to shift to match this role's framing.

4. When gaps are identified:
   - First, present a summary table of all identified gaps: gap description, severity (High/Medium/Low), and initial hypothesis on approach (CV language, interview narrative, needs user input, or insufficient evidence)
   - Then work through each gap one at a time, waiting for a response before moving to the next
   - For each gap, search the loaded source documents for experience that could close it. Ask clarifying questions for any information that could be relevant.
   - Do not attempt to close gaps through creative framing unless discussed and approved first. Gaps that cannot be closed through source material may need to be carried by interview narrative — flag these explicitly.

5. Note anything to de-emphasize for this role and request approval/agreement.

6. Provide a structured fit assessment:
   - Overall fit rating with brief rationale
   - Top 2-3 strengths driving candidacy for this specific role
   - Top 2-3 risks or gaps that could filter early
   - Recommendation: does this role warrant full CV tailoring, or does fit fall below threshold?

   **Threshold definition:** A role clears the threshold if it meets both conditions:
   - *Domain exclusion check* — the role does not require a primary domain that falls outside established positioning. This is an exclusion gate, not a positive fit signal.
   - *Candidacy viability* — at least 65% of critical requirements from Phase 2a have a strong, source-citable match (2 of 3, 3 of 4, or 4 of 5). Weak or inferred matches do not count.

   **Strong match definition:** A specific, named achievement or deliverable in the source documents that directly addresses the requirement — citable to a specific document and entry. General capability claims do not qualify.

   If either condition fails, state this explicitly and ask whether to proceed as a speculative application with explicitly acknowledged risk. Do not proceed to Phase 4 without a clear response.

7. Explicitly state the resolution status of every High-severity gap: resolved, carried by interview narrative, or unresolved. If any High-severity gap remains unresolved, do not request phase approval — surface it and obtain a decision on how to proceed.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

Gaps: Enumerate every High-severity gap identified in Phase 3a. For each, confirm its documented resolution status. If any High-severity gap has no recorded resolution or user acknowledgment, flag as a blocking issue and invoke QC Failure Recovery.

Perform QC per Global Rules:
- **QC Failure Recovery**
- **Standard QC Document Verification**
- **QC Phases**

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — CV Content Creation

*(Only after Phase 3a and 3b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load documents:**
Load the CV reference file matching the format confirmed in Phase 2a Step 7. Confirm it loaded completely before proceeding:
- Large Enterprise Established → `knowledge/CV_General_Lrge_Enterprise_Established.md`
- Mid Size Scale-Up → `knowledge/CV_General_Mid_Size_Scale_Up.md`

Then load the content rules file matching the role level confirmed in Phase 2a Step 2:
- AD+ roles → `context/cv_content_rules_leadership.md`
- IC roles → `context/cv_content_rules_ic.md`

Confirm the content rules file loaded completely. All rules in that file apply actively throughout content generation — they are not pre-conditions to confirm, they are requirements to satisfy in every line generated.

**Step 2 — Confirm archetype instruction set:**
State the primary archetype document loaded in Phase 2a. Confirm it is still available in context. If not, reload it now before proceeding.

**Step 3 — Experience architecture:**
All roles in the last 10 years belong in the main experience section to demonstrate career continuity. For those roles that don't add credibility to Phase 2a critical requirements, a one-line entry may be used. A role that adds credibility to Phase 2a critical requirements belongs in the main experience section regardless of age.

Before generating any content, produce a proposed experience section architecture and present for approval. For each role in the full career history, state:
- Company name and role title
- Proposed treatment: Full entry with bullets (main section) | One-line entry in main section | One-line entry in Earlier Professional Roles | Omit entirely
- Rationale tied to Phase 2a critical requirements

Wait for explicit approval of the experience architecture before proceeding to Step 4.

**Step 4 — Generate CV content:**
Generate complete CV content applying all rules from the active archetype instruction set and the loaded content rules file simultaneously. Present content as fully drafted text organized by section in the order determined by the approved archetype. All bullets are final-form. This output is the complete content set placed into the document in Phase 5.

**Phase 4a Closing:** Follow Standard Phase Closing. Next phase is Phase 4b.

---

## Phase 4b — Quality Control for Phase 4a

Content Rules Verification: Verify the loaded content rules file was actively applied throughout generation. For each rule, state the verification method and result. Any rule that cannot be verified against the output must be flagged as non-compliant and QC Failure Recovery invoked.

CV QC Checklist: Load `context/cv_qc_checklist.md` now. Apply the Universal section against the generated CV content. Then apply the archetype section matching the active archetype and role level confirmed in Phase 2a. For each item, cite specific evidence from the generated content — a specific bullet, section, or line. General confirmations are not acceptable. State Pass or Fail for each item. Any Fail invokes QC Failure Recovery before this phase can close.

Perform QC per Global Rules:
- **QC Failure Recovery**
- **Standard QC Document Verification**
- **QC Phases**

**Phase 4b Closing:** Follow Standard Phase Closing. Next phase is Phase 5a.

---

## Phase 5a — CV Document Generation

*(Only after Phase 4a and 4b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load formatting specification:**
Load `context/cv_format_spec.md` now. Confirm it loaded completely. All formatting decisions are governed by this file. It is the authoritative source — do not infer or recreate formatting from any other reference.

**Step 2 — Generate document:**
Use the docx skill (`/mnt/skills/public/docx/SKILL.md`) to generate the Word document programmatically. Apply all formatting rules from `context/cv_format_spec.md`.

Structure decisions were made in Phase 4 and govern the output. Do not default to any reference document's structure. Do not omit or collapse roles because they do not appear in a reference. A role that adds credibility to Phase 2a critical requirements belongs in the main experience section.

**Step 3 — Save output:**
Save the completed CV to `outputs/` using this naming convention:
`[Name]_CV_[CompanyName]_[AbbreviatedRole]_[YYYYMM].docx`

**Phase 5a Closing:** State "File is ready for your review." Then follow Standard Phase Closing. Next phase is Phase 5b.

---

## Phase 5b — Quality Control for Phase 5a

Confirm the output file was saved with the correct filename format. State the actual filename and confirm it matches the convention.

Perform QC per Global Rules:
- **QC Failure Recovery**
- **Standard QC Document Verification**
- **QC Phases**

**Phase 5b Closing:** Follow Standard Phase Closing. Next phase is Phase 6.

---

## Phase 6 — Source Document Update

Dedicated to capturing information surfaced during this session that should be added to source documents. Keeping source documents current reduces gap closure time in future sessions.

For each source document, review this session for information meeting any of the following criteria:
- Gap resolutions: experience, context, or framing confirmed during Phase 3 gap closure not currently in source documents
- New achievement language: specific outcomes, metrics, or accomplishments articulated for the first time this session
- Framing decisions: positioning or scope language confirmed that could apply to future roles
- Corrections: any instance where source document content was found to be inaccurate, incomplete, or misleading

Information that is role-specific and unlikely to generalize should not be captured.

Target source documents:
- `knowledge/Positioning.md`
- `knowledge/Accomplishments.md`
- `knowledge/CV_Verbose.md`
- `knowledge/Experience_Inventory.md`

Load only the specific documents relevant to the updates being recommended. For each item, provide:
- Target source document
- Location within the document where the information should be inserted
- The information, formatted per the document-specific conventions below

**Document-specific format requirements:**

`knowledge/Experience_Inventory.md` — Every entry must include all applicable structured tags. Do not write inventory entries as CV bullets or impact statements. The entry describes what was done; the tags enable retrieval.
- Capability: [the capability or capabilities demonstrated — match existing tag values in the document]
- Context: [Greenfield | Scaling | Turnaround | Mature/Enterprise]
- Role Level: [IC | Manager | Senior Manager | Director | Senior Director | VP]
- Outcome: [Capability Building | Quality Improvement | Risk Reduction | Efficiency Gain | Scalability/Growth Enablement]
- Achievement: [factual, descriptive statement of what was done — not a polished CV bullet]

`knowledge/CV_Verbose.md` — Entries are full narrative descriptions in CV language, written at sufficient detail to serve as source material for future tailoring. Follow the structure and voice of existing entries in the document.

`knowledge/Accomplishments.md` — Follow the structure and conventions of existing entries. Include metrics where available from this session.

`knowledge/Positioning.md` — Entries are strategic positioning statements, not achievement bullets. Follow the framing conventions of existing entries.

Before presenting the summary, verify each recommended addition: (a) traceable to an explicit user statement or source document from this session, (b) not role-specific content unlikely to generalize, (c) does not contradict existing source document content. Any item failing verification must be flagged and excluded unless the user explicitly approves inclusion.

Present the summary clearly so updates can be applied manually.

Before closing, ask: "Is there anything else from this session — gap resolutions, framing decisions, or confirmed context — that should be captured before we close?"
