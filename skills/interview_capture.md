# Interview Capture Skill

## Objective

Capture structured content for one completed interview round and write it into the InterviewCompletion `.md` file for the target role. This skill is invoked immediately after each interview round concludes. It persists interviewer details, questions asked, responses given, and round debrief, producing the primary input for the `interview_followup` skill. Sparse capture degrades follow-up letter quality, so the skill enforces minimum-completeness gates before writing.

---

## Global Rules

Load `rules/global_rules.md` at the start of this skill. Confirm it loaded completely before proceeding. All rules in that file govern this skill.

**Action Phases:** 1a, 2a, 2b, 3a, 3b

---

## Phase 1a — Context Load

*(No documents are loaded before this phase)*

1. Ask the user for the absolute path to the `InterviewScratch_[Company]_[AbbreviatedRole]_[YYYY-MM].md` file for the interview round just completed. This is the single required input. Confirm the file exists and loaded completely.

2. Read the scratch file's header block. Extract the paths to the InterviewPrep file and the InterviewCompletion file recorded there by `interview_prep` at creation time. Confirm both paths resolve on disk. If either path is missing or unreachable, halt and inform the user — the scratch file is malformed and must be repaired before the skill can proceed.

3. Read the InterviewCompletion file. Parse round headings to auto-detect the first unpopulated round. A round is considered unpopulated when no interviewer name is recorded and no question/response pair is recorded in that round's sections. State the detected round number to the user and ask for explicit confirmation before proceeding.

   If the auto-detected round is already populated (accidental invocation, or user wants to redo an earlier round), present two options and wait for the user's choice:
   - **Edit the `.md` file directly:** skill exits without changes; user edits the completion file in their text editor.
   - **Overwrite:** skill proceeds with capture, and the existing round content will be replaced. The overwrite must be reconfirmed in Phase 2b before any write occurs.

4. Read the scratch file's section for the confirmed target round (e.g., `## Round 2` body content — everything between that heading and the next `## Round N` heading). Exclude HTML comments. If content exists under that round heading, it serves as anchor material for Phase 2a Step 3 (Q&A reconstruction in anchor-driven mode). Do not read other rounds' sections — they belong to prior captures and must not contaminate the current round.

   If the target round's section is empty, ask the user whether they want to proceed in cold-recall mode (no anchor material, relying on memory alone). If declined, halt and state the impact: without captured round content, `interview_followup` cannot generate a meaningful follow-up letter for this round.

5. State the resolved context explicitly before closing: scratch file path, InterviewCompletion file path, confirmed target round number, capture mode (anchor-driven or cold-recall), overwrite disposition if applicable.

**Phase 1a Closing:** Follow Standard Phase Closing. Next phase is Phase 2a.

---

## Phase 2a — Structured Capture

*(Only after Phase 1a has been explicitly approved)*
*(State each step before completing the step)*

Capture content for the confirmed round through four sequential steps. Prompt one step at a time and wait for the user's response before moving to the next.

**Step 1 — Logistics:**

Ask in sequence:
- Type (phone screen / remote interview / in-person interview)
- Sub-Type (single / panel)
- Date and time

**Step 2 — Interviewers:**

Ask the user to list all interviewers for this round. For each: name, title, and any notes the user wants captured (focus area, tone, what they emphasized). At least one interviewer with name and title is a hard requirement enforced in Phase 2b.

**Step 3 — Q&A Capture (dump, then refine):**

**Anchor-driven mode** (scratch file body had content):
- Present the scratch file body back to the user as reference.
- Ask the user to dump all question/response pairs from the round in a single message, one pair per line in format `Q: <question> | A: <response summary>`. Encourage expansion of anchor keywords into full question/response wording.
- After the dump, re-present every pair back to the user in a numbered list and ask for refinements, corrections, or additions. Collect all edits in one pass — do not refine per-pair.

**Cold-recall mode** (scratch file body empty, user opted into cold recall):
- Prompt: "Reconstruct the questions and responses from memory. List each question asked and your response, one pair per line: `Q: <question> | A: <response summary>`."
- Use the same dump-then-refine pattern.

In both modes, confirm the final Q&A pair count. Warn explicitly if fewer than three pairs — this triggers a Phase 2b gate.

**Step 4 — Round Debrief:**

Ask each field one at a time:
- Impression (overall read of the round)
- Interest level (Strong / Uncertain but continuing / Undecided)
- Rough patches (anything to address in follow-up; if none, say so explicitly)
- Personal connection threads (anything personal or memorable that came up; if none, say so)
- Next steps communicated (what they said about timeline or process; if nothing discussed, say so)
- Awareness of competing pursuits (Y / N)

An explicit "none" or "not discussed" is an answer. Leaving a field truly blank triggers a Phase 2b gate.

**Phase 2a Closing:** Follow Standard Phase Closing. Next phase is Phase 2b.

---

## Phase 2b — Quality Control of Phase 2a

**Interviewer Minimum (blocking):**
Confirm at least one interviewer was captured with both name and title. If not, flag as a blocking issue per Global Rules QC Failure Recovery. Do not proceed to Phase 3a until resolved.

**Q&A Minimum (warn + confirm):**
If fewer than three Q&A pairs were captured, state the count and ask the user to confirm the interview was actually completed as expected. Proceed only on explicit user confirmation. If the user declines, halt the skill without writing the round.

**Debrief Completeness (warn + confirm):**
If any debrief field was left truly blank (not answered with "none" or "not discussed"), list the incomplete fields and advise the user to complete them. Proceed only on explicit user confirmation. If declined, halt.

**Overwrite Reconfirmation (if applicable):**
If Phase 1a Step 3 resolved to overwrite an already-populated round, state that overwriting will occur and reconfirm with the user before proceeding. Do not silently overwrite.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 2b Closing:** Follow Standard Phase Closing. Next phase is Phase 3a.

---

## Phase 3a — Writeback

*(Only after Phase 2a and 2b have been explicitly approved)*
*(State each step before completing the step)*

**Step 1 — Locate target round in InterviewCompletion file:**

Parse the completion file's markdown structure to locate the heading for the confirmed target round (e.g., `## Round 2`). All writes are scoped to this section and its subsections (`### Logistics`, `### Interviewers`, `### Questions and Responses`, `### Round Debrief`).

**Step 2 — Write captured content to the round's subsections:**

For each field captured in Phase 2a:
- Replace the hint-text HTML comment (pattern `<!-- hint: ... -->`) with the captured value.
- Preserve markdown structure and heading hierarchy exactly. Do not reorder, rename, or restructure sections.
- For fields with no value captured in this session, leave the hint-text HTML comment in place. Blank fields must remain blank with hints intact so the file stays valid for future round captures and for `interview_followup` read-back.

**Step 3 — Save the updated file:**

Write the modified content back to the InterviewCompletion file path resolved in Phase 1a. Confirm the file saved successfully.

**Step 4 — Report completion:**

State to the user: the round captured, the path to the updated completion file, and a note that `interview_followup` can now be run for this round.

**Phase 3a Closing:** Follow Standard Phase Closing. Next phase is Phase 3b.

---

## Phase 3b — Quality Control of Phase 3a

**Writeback Verification:**
Re-read the InterviewCompletion file. Confirm the target round now contains the captured values: at minimum the interviewer name/title, the Q&A pairs captured in Phase 2a (at least the count confirmed there), and any debrief fields the user provided.

**Hint Text Preservation:**
Confirm that any field not captured in this session still carries its hint-text HTML comment intact. The completion file must remain valid for future round captures.

**Other Rounds Unchanged:**
Confirm that rounds other than the target round were not modified by the writeback. State which rounds were inspected and the inspection result.

Perform QC per Global Rules:
- **Standard QC Document Verification**

**Phase 3b Closing:** State: "Round [N] captured for [Company] — [Role]. `interview_followup` can now be run for this round." Follow Standard Phase Closing.
