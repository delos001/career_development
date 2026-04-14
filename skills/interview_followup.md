# Interview Follow-Up Skill

## Objective

Generate a follow-up letter for a specific interview round. This skill reads the InterviewCompletion `.md` file (populated by `interview_capture`) as its primary input and generates either a verbose detailed letter or a concise thank-you, based on user selection at runtime. The letter is saved to the application folder specified by the user.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b

---

## Phase 1a — Context Load

*(No documents are loaded before this phase)*

1. Ask the user for the absolute path to the `InterviewScratch_[Company]_[AbbreviatedRole]_[YYYY-MM].md` file for the target role. This is the single input. Confirm the file exists and loaded completely. If the scratch file cannot be located, inform the user that `interview_prep` must be completed before this skill can proceed — it is the skill that generates the scratch file.

2. Read the scratch file's header block. Extract the path to the InterviewCompletion file recorded there. Confirm the path resolves on disk. If the path is missing from the header or not reachable, halt and inform the user — the scratch file is malformed and must be repaired before this skill can proceed.

3. Read the InterviewCompletion file. Identify which rounds have data populated. For the purposes of this skill, a round is considered populated when its Interviewers section contains at least one captured block (not just the hint-text HTML comment) and its Questions and Responses section contains at least one captured block. Hint-text HTML comments (pattern `<!-- hint: ... -->`) do not count as content.

   List the populated rounds to the user, then ask which round this follow-up is for. Once the round is confirmed, read the target round's full content: Logistics, Interviewers, Questions and Responses, and Round Debrief. If the Round Debrief fields contain only hint-text HTML comments rather than captured values, note this explicitly — the user will need to supply that context in Phase 2a. If no rounds are populated, inform the user that `interview_capture` must be run for the target round before this skill can proceed.

4. Ask for the absolute path to the output folder where the follow-up letter will be saved.

5. Confirm all context is in hand and state it explicitly before closing.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — User Prompts

*(Only after Phase 1a has been explicitly approved)*

Collect the following inputs from the user. Prompt for each one at a time and wait for a response before moving to the next. If the Round Debrief from Phase 1a already contains relevant information for a prompt, state what was found and ask the user to confirm or update rather than re-asking from scratch.

**Prompt 1 — Letter format:**
"Which letter format would you like?
- Verbose detailed: a substantive letter that connects your experience to their priorities, addresses any concerns raised, and reinforces your differentiated value
- Concise thank-you: a brief, professional letter with a specific callback to the interview and a clean close"

**Prompt 2 — Interest level:**
"After this round, how would you characterize your interest level?
- Strong: you want this role and want to signal that clearly
- Uncertain but continuing: you want to keep the conversation going but are not ready to commit
- Undecided: you want to keep the door open without signaling strong enthusiasm"

**Prompt 3 — Rough patches:**
"Were there any moments in this interview you want to address or correct in the letter — a question you fumbled, a concern they raised that you did not fully resolve, or a topic where your answer felt incomplete? (Yes / No — if yes, describe)"

**Prompt 4 — Next steps:**
"Were explicit next steps or a timeline discussed during the interview? (Yes / No — if yes, what was said)"
If this was captured in the Round Debrief, confirm it rather than re-asking.

**Prompt 5 — Competitive positioning:**
"Are you actively pursuing other roles, and does this interviewer or company know that? (Yes, they know / Yes, they do not know / No other active pursuits)"

**Prompt 6 — Relationship threads:**
"Did anything personal or memorable come up — shared background, a project they mentioned, something unexpected from the conversation that stood out? (Yes / No — if yes, describe)"

**Prompt 7 — Recipient:**
"Who is the primary recipient of this letter?" Confirm name and title from the Round Debrief. If the round had multiple interviewers, ask whether the user wants a single letter addressed to the primary contact or individual letters for each interviewer. If individual letters, confirm the list of recipients — each will be generated sequentially in Phase 3a.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

**All Prompts Answered:** Confirm all seven prompts received explicit user responses. If any was skipped or unanswered, flag as a blocking issue. Do not generate the letter with unresolved inputs.

**Round Data Sufficiency:** Confirm the interview round data from Phase 1a contains enough content to produce a specific, non-generic letter. Minimum required: at least one interviewer name and title, and at least one question/response pair or topic captured. If this minimum is not met, flag the gap and ask the user to supplement before proceeding — typically by running `interview_capture` against the target round if capture was incomplete.

**Multiple Recipients:** If individual letters were confirmed in Prompt 7, confirm the count and recipient list. This determines the generation loop in Phase 3a.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Letter Generation

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Apply tone modifier:**
Apply the interest level from Prompt 2 as a consistent tone modifier throughout the letter:
- Strong: affirmative, forward-leaning language; restate fit and interest directly
- Uncertain but continuing: frame around wanting to learn more and continuing the conversation; do not overstate enthusiasm, do not understate engagement
- Undecided: neutral and professional; keep the door open without signaling strong interest or disinterest

**Step 2 — Generate letter(s):**

Apply the selected format from Prompt 1:

**Concise thank-you format:**
- Paragraph 1: Express appreciation for the time. Reference one specific topic, detail, or moment from the interview by name — not generic gratitude.
- Paragraph 2: One to two sentences connecting a specific aspect of your background to something they said or emphasized.
- Paragraph 3: Interest and fit statement adjusted for the confirmed interest level tone. If next steps were discussed, reference them directly. If not, ask for them cleanly.
- Maximum four short paragraphs total.

**Verbose detailed format:**
- Paragraph 1: Express appreciation. Reference one specific topic or moment from the interview by name.
- Paragraph 2: Substantive alignment paragraph. Connect your most relevant experience to the priorities or themes they emphasized. Be specific — cite what they said and what you bring. This is the letter's central value, not a courtesy paragraph. If the application was speculative or direct experience fit is partial, frame this paragraph around transferable strengths and growth trajectory rather than requiring a direct experience match — do not fabricate alignment that does not exist.
- Paragraph 3 — conditional: Include only if Prompt 3 identified rough patches. Address the gap or fumble directly and provide the complete or corrected answer. Do not over-apologize — state what you should have said and move forward.
- Paragraph 4 — conditional: Include only if Prompt 5 confirmed active competing roles AND interest level is Strong. A brief, non-pushy urgency signal. Do not fabricate or exaggerate urgency. Omit this paragraph if either condition is not met.
- Paragraph 5 — conditional: Include only if Prompt 6 identified a relationship thread worth continuing. A brief, genuine callback to the personal or memorable moment. Two sentences maximum.
- Closing paragraph: Interest and fit statement adjusted for the confirmed interest level tone. Reference next steps if discussed. If not discussed, ask for them cleanly.

**Step 3 — Multiple recipients:**
If individual letters were confirmed in Phase 2b, repeat Step 2 for each recipient. Personalize the specific callback in Paragraph 1 and the relationship thread paragraph (if applicable) to each recipient individually. The alignment content and interest framing may be consistent across letters.

**Step 4 — Save output:**
Save completed letter(s) to the output folder confirmed in Phase 1a. Naming convention:
`InterviewFollowup_[Company]_[AbbreviatedRole]_R[N]_[YYYY-MM].md`

If individual letters were generated per recipient, append the recipient's last name:
`InterviewFollowup_[Company]_[AbbreviatedRole]_R[N]_[LastName]_[YYYY-MM].md`

Confirm each file was saved before closing.

**Phase 3a Closing:** State "Letter is ready for your review." Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

**Tone Consistency:** Confirm the interest level tone modifier was applied consistently. State the confirmed interest level and identify the specific language in the letter that reflects it. If the tone contradicts the confirmed interest level, flag and correct before closing.

**Format Compliance:** Confirm the selected format was applied. For concise: confirm no more than four paragraphs. For verbose: confirm required paragraphs are present and conditional paragraphs appear only when their conditions were met. State the condition status for each conditional paragraph.

**Specificity Check:** Confirm the letter references at least one specific topic, name, or detail from the interview. A letter that could have been written without conducting the interview fails this check — flag and revise.

**Filename Convention:** State the actual filename(s) and confirm each matches the naming convention.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 3b Closing:** Follow Standard Phase Closing.
