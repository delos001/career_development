# CV Generation Skill

## Objective

Generate targeted CVs to secure interviews for roles that align with established experience, education, and positioning. This skill covers role understanding, fit evaluation, gap closure, content generation, document production, and a feedback mechanism to fill gaps in knowledge documents.

---

## Global Rules

**Following Instructions**
Follow this skill exactly. Steps will not be overridden by judgment without explicit user approval. Inference will not be applied in a way that violates this skill without explicit user approval.

When in a phase, complete only steps from that phase. Do not perform steps or volunteer analysis from future phases.

If something is ambiguous, do not use judement or inference without approval and state the ambiguit explicitly before moving to another step or phase.

**Document Load Instructions**
Load documents at the phase and step specified in this skill — no earlier, no later. This is a just-in-time loading workflow. Refer to `README.md` for the full loading map.

A document is loaded completely when all content is present with identifiable structure — not just a fragment. A document returning only fragments without structure must be flagged as a load failure.

If any document fails loading, do not proceed using partial content:
- Run bash with `cat [filepath]` for each failed document
- Confirm the full document content is readable before proceeding
- If the bash fallback also fails, report the specific file and error — do NOT proceed until resolved

Document load instructions apply at any point in the skill. If a read returns incomplete content mid-phase, stop, run the fallback, confirm availability, then continue. Do not silently proceed with degraded source material.

**Standard Phase Closing — Action Phases (1a, 2a, 2b, 3a, 3b, 4a, 4b, 5a, 5b)**
At the close of each action phase:
- List steps completed and steps not completed
- Confirm with user if any other topics relevant to this phase's outputs should be discussed
- Obtain explicit approval before proceeding to the next phase

**QC Failure Recovery**
If a QC phase identifies that a step was incomplete, non-compliant, or that output does not conform to skill instructions, do not proceed. State the specific failure clearly, identify which step or output is affected, and present the user with options: (a) return to the prior phase and re-run the failed step, (b) accept the gap with explicit acknowledgment and proceed, or (c) stop the session. Do not invent a resolution or silently continue. Wait for explicit user direction before taking any action.

**Standard QC Document Verification**
If any documents were loaded in the previous phase, verify Document Load Instructions were followed. State verification status for each document: document name, verification method, result (pass/fail/fallback used), and structural element confirmed. All documents must pass verification before proceeding.

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

4. Research the company, industry, and role using web search to develop an expert-level understanding of what this position actually requires — including company stage, culture, competitive landscape, organizational context, and what success looks like in this type of role at this type of company.

5. Identify the 4-5 most critical requirements or themes in the job description.

6. Identify the role archetype from the following four options and state the framing angle:

   - **Transformation & Strategy** — enterprise-level change, operating model redesign, strategic program leadership
   - **Data & Analytics** — clinical data strategy, data governance, analytics platform development, data science enablement
   - **Process & Operations** — process excellence, clinical operations, Lean/Six Sigma, execution and efficiency
   - **Platform & Technology** — technology strategy, platform implementation, system integration, vendor and tool ecosystem

   If the role spans two archetypes, identify a primary and secondary archetypes and state both explicitly with rationale. Apply the following rules throughout all subsequent phases:

   - The primary archetype governs exclusively: section order, summary framing, Core Competencies priority, and achievement selection criteria. The secondary archetype has no authority over any of these.
   - Secondary framing appears only within individual achievements where both dimensions are genuinely present in the underlying experience — not as standalone achievements and not in the summary.
   - No more than 2-3 achievements should carry secondary framing. If more than a third of achievements require secondary framing to be relevant, the primary archetype selection is likely wrong — flag this before proceeding and re-evaluate.
   - When primary and secondary framing conflict within an achievement, primary wins. Do not weaken the primary message to accommodate the secondary dimension.
   - The summary is governed exclusively by the primary archetype framing rules. The secondary archetype does not appear in the summary.
   - Core Competencies may include 1-2 items signaling the secondary archetype capability. The secondary zone must not displace primary archetype items.

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

   If a dual-archetype was identified, also load the secondary archetype document using the same role-level logic.

   Confirm each loaded completely before proceeding. If loading fails, follow Document Load Instructions fallback.

7. Identify the most appropriate CV format reference and state why:
   - **Large Enterprise Established** — for established pharma, large CROs, or mature biotech
   - **Mid Size Scale-Up** — for growth-stage biotech OR companies undergoing significant transformation (regardless of current size or maturity)

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

Role Level: Confirm the role level was explicitly stated or inferred with rationale, and that explicit user agreement was obtained. If agreement is not documented, flag as a blocking issue and invoke QC Failure Recovery.

Company Research: Confirm web search was performed in Phase 2a Step 4. State the specific sources or findings that informed the role understanding and format selection. If research was not performed or cannot be evidenced, flag as a non-compliant step.

Critical Requirements: Confirm 4-5 critical requirements were identified in Phase 2a Step 5. If fewer than 4 were identified, flag and complete before proceeding.

Archetype Selection: Verify the primary archetype selection is defensible against the match criteria defined in the loaded archetype file. State the specific match criteria satisfied and cite the job description language that supports each. If the role does not clearly satisfy the match criteria, flag as a blocking issue — a wrong archetype selection propagates through every subsequent phase and cannot be corrected without restarting from Phase 2a.

If a dual-archetype was identified: verify the secondary archetype is explicitly evidenced in the job description — not inferred from peripheral language. Confirm the primary/secondary assignment reflects which dimension the role primarily evaluates candidates on. If the secondary is weak or speculative, recommend single-archetype treatment and obtain user agreement before proceeding.

Format Selection: Confirm the Large Enterprise Established vs Mid-Size Scale-Up selection is consistent with the job description and the company research completed in Phase 2a Step 4. State the specific company characteristic that drove the selection.


Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Fit Evaluation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

1. Load the following source documents now. Confirm each loaded completely before proceeding:
   - `knowledge/Experience_Inventory.md`
   - `knowledge/Accomplishments.md`
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

**Requirement Mapping:** Enumerate the critical requirements identified in Phase 2a. For each, confirm a source-citable match was presented in Phase 3a Step 2. A specific named achievement or deliverable traceable to a source document is required — general capability claims do not qualify. Flag any requirement without a citable match.

**Gap Enumeration:** Confirm all gaps identified in Phase 3a Step 3 were included in the summary table from Step 4. For each gap, confirm the severity rating is defensible — state the specific reason severity was assigned. Flag any gap rated without clear rationale.

**Gap Resolution Completeness:** Enumerate every gap from the Phase 3a summary table. For each, confirm: (a) it was worked through individually with a user response before moving to the next, and (b) the resolution is one of the three allowed states — resolved via CV language, carried by interview narrative, or unresolved with explicit user acknowledgment. Any gap without a recorded resolution or acknowledgment is a blocking issue — invoke QC Failure Recovery.

**High-Severity Gaps:** Confirm every High-severity gap has an explicit resolution status. Any unresolved High-severity gap without an explicit user decision is a blocking issue — invoke QC Failure Recovery.

**De-Emphasis Approvals:** Confirm any items flagged for de-emphasis in Phase 3a Step 5 received explicit user agreement. De-emphasis applied without approval is a non-compliant step — flag it.

**Fit Threshold Verification:** Confirm Phase 3a Step 6 applied the threshold correctly. State: the number of critical requirements, the number with strong source-citable matches, and verify the 65% calculation. Confirm the domain exclusion check was performed. If either condition failed and the session continued, confirm explicit user approval to proceed as a speculative application was obtained and documented.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 3b Closing:** Follow Standard Phase Closing. Next phase is Phase 4a.

---

## Phase 4a — CV Content Creation

*(Only after Phase 3a and 3b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load documents:**
Load the CV reference file matching the format confirmed in Phase 2a Step 7. Confirm it loaded completely before proceeding:
- Large Enterprise Established → `knowledge/CV_General_Lrge_Enterprise_Established.md`
- Mid Size Scale-Up → `knowledge/CV_General_Mid_Size_Scale_Up.md`

Then load the content rules file matching the role level confirmed in Phase 2a Step 2. Confirm the content rules file loaded completely:
- AD+ roles → `context/cv_content_rules_leadership.md`
- IC roles → `context/cv_content_rules_ic.md`

All rules in the content rules file apply actively throughout content generation — they are not pre-conditions to confirm, they are requirements to satisfy in every line generated.

**Step 2 — Confirm archetype instruction set:**
State the primary archetype document loaded in Phase 2a. Confirm it is still available in context. If not, reload it now before proceeding.

**Step 3 — Experience architecture:**
All roles in the last 10 years belong in the main experience section to demonstrate career continuity. For those roles that don't add credibility to Phase 2a critical requirements, a one or two-line summary entry may be used. A role that adds credibility to Phase 2a critical requirements belongs in the main experience section regardless of age.

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

**Experience Architecture Approval:** Confirm the proposed experience architecture from Step 3 was presented to the user and explicitly approved before content generation began in Step 4. If approval is not documented, flag as a blocking issue and invoke QC Failure Recovery.

**Content Rules Verification:** Verify the loaded content rules file was actively applied throughout generation. For each rule, state the verification method and result. Any rule that cannot be verified against the output must be flagged as non-compliant and QC Failure Recovery invoked.

**CV QC Checklist:** Load `context/cv_qc_checklist.md` now. Apply the Universal section against the generated CV content. Then apply the archetype section matching the active archetype and role level confirmed in Phase 2a. For each item, cite specific evidence from the generated content — a specific bullet, section, or line. General confirmations are not acceptable. State Pass or Fail for each item. Any Fail invokes QC Failure Recovery before this phase can close.

Perform QC per Global Rules:
- **Standard QC Document Verification**

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

**Document Generation:** Confirm the docx skill was used to generate the document. Confirm all formatting decisions reference `context/cv_format_spec.md` and were not inferred from any other source. If either cannot be confirmed, flag as a non-compliant step and invoke QC Failure Recovery.

**Filename Convention:** Confirm the output file was saved with the correct filename format. State the actual filename and confirm it matches the convention.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 5b Closing:** Follow Standard Phase Closing. Next phase is Phase 6.

---

## Phase 6 — Source Document Update

Dedicated to capturing information surfaced during this CV session that should be added to source documents.

Load `skills/source_document_update.md` now and follow it completely. "This session" refers to all phases and interactions from Phase 1a through Phase 5b.
