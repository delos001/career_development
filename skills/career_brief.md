# Career Brief Skill

## Objective

Generate a short professional bio or summary paragraph for use in recruiter outreach, networking introductions, speaker profiles, or similar contexts where a standalone written summary is needed. Output is plain text for copy-paste — no file is generated.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b

---

## Phase 1a — Context Collection

*(No documents are loaded before this phase)*

1. Ask the user: "Who is this for and how will it be used?" Accept a free-form response. Do not present format options — infer the appropriate format from their answer.

   Apply the following format selection logic:
   - If someone else will be sharing or forwarding it on the user's behalf (recruiter introducing to a hiring manager, networking contact making an introduction, conference or panel bio submission): select **Short Bio** format.
   - If the user is sending it directly in response to a request for a written summary (recruiter asking for a quick overview, outreach email, LinkedIn message): select **Professional Summary Paragraph** format.
   - If the use case is ambiguous, state the two options plainly and ask the user to confirm which fits.

2. Ask: "Is there a specific industry, role type, or opportunity you want this tailored to, or should I draw from your general positioning?" Accept a free-form response. If specific context is provided, note it — it will govern emphasis and framing in Phase 2a.

3. State the selected format and the tailoring context explicitly before closing. Confirm with the user before proceeding.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Generation

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Load source documents:**
Load `knowledge/Positioning.md` now. Confirm it loaded completely before proceeding.

If Positioning.md does not contain enough specificity to tailor the output to the context confirmed in Phase 1a, load `knowledge/Experience_Inventory.md` as a supplementary source. State why the supplementary load is needed before loading. Do not load it by default.

**Step 2 — Generate:**

Apply the format confirmed in Phase 1a:

**Short Bio format:**
- Length: 150-200 words
- Voice: third-person throughout; never use "I"
- Structure: opening sentence establishes current role and domain; second sentence establishes depth and scope of experience; middle sentences highlight 2-3 signature strengths or accomplishments drawn from Positioning.md, framed for the stated context; closing sentence states professional focus or what [Name] brings to the work
- Tone: confident and specific; not a list of job titles, not a CV in prose form
- Do not open with the person's name as a standalone fragment — work the name into the first sentence naturally
- If the user is currently unemployed, between roles, or in transition: do not open with a current role. Open with most recent role framed as recent experience, or lead with domain expertise and career focus. Do not reference the gap directly in the bio.

**Professional Summary Paragraph format:**
- Length: 4-6 lines of prose (not bullets)
- Voice: implicit first-person — no "I" but written from the first-person perspective
- Structure: opening line establishes positioning and domain; middle sentences connect 2-3 specific strengths or achievements to the stated context; closing line signals forward intent or value offered
- Tone: direct and grounded; reads as something a person would actually say, not a keyword list
- Tailored to the specific context from Phase 1a — not pulled verbatim from Positioning.md

**Step 3 — Present output:**
Display the generated text in full. Ask the user if they want any adjustments — tone, emphasis, length, or specific content changes. If adjustments are requested, revise and re-present. Repeat until the user confirms it is ready.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control

**Format Compliance:**
- Short Bio: confirm word count is within 150-200 words. Confirm third-person voice throughout — flag any use of "I." Confirm the name appears naturally in the first sentence, not as a standalone fragment.
- Professional Summary Paragraph: confirm the output is 4-6 lines of prose. Confirm no explicit "I" appears. Confirm it reads as tailored to the stated context, not generic.

**Source Grounding:** Confirm the output draws from Positioning.md content — not fabricated claims or generic language. If the supplementary load of Experience_Inventory.md was triggered, confirm it was justified and that its content contributed to the output.

**Context Alignment:** Confirm the output reflects the tailoring context stated in Phase 1a. If a specific industry, role type, or opportunity was named, confirm it is reflected in the framing and emphasis.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 2b Closing:** Follow Standard Phase Closing.
