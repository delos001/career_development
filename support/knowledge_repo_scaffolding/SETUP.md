# personal/knowledge/ — Master Career Documents

This folder is not part of the framework repository. It holds master source documents used at runtime by the CV generation, role evaluation, and interview prep skills.

This file originates in the framework repo at `support/knowledge_repo_scaffolding/SETUP.md`. When you set up your own knowledge repo, copy this file (along with `README.md`, `.gitignore`, and `Contact_Info.md` from the same scaffolding folder) into your knowledge repo as the starting point.

---

## What belongs here

- `Experience_Inventory.md` — canonical source of all career experience entries, tagged and annotated for retrieval
- `Career_Narratives.md` — stories and decisions for interview preparation and CV anchor bullets
- `Positioning.md` — strategic framing statements, signature themes, recruiter pitch language
- `Contact_Info.md` — single source of truth for CV contact line values
- `Questions_Library.md` — reusable interview questions accumulated by `interview_prep`

What does not belong here:
- Session artifacts (SessionLog, GapAnalysis, ContentDecisions) live in `personal/sessions/` and are not committed to this repo.
- Generated deliverables (CV `.docx`) live in `outputs/` and are not committed to this repo.

---

## Setup

This folder is designed to hold a separate private git repository cloned into this location. Personal documents stay version controlled but are never committed to the framework repo.

**Steps:**

1. Create a private repository on GitHub (suggested name: `career_development_knowledge`).
2. From the framework repo root, ensure the `personal/` directory exists, then clone the knowledge repo into it:
   ```
   git clone https://github.com/<your-github-username>/career_development_knowledge.git personal/knowledge/
   ```
3. Copy the contents of `support/knowledge_repo_scaffolding/` from the framework repo into your newly cloned `personal/knowledge/` directory. This gives you a starting `README.md`, `SETUP.md`, `.gitignore`, and `Contact_Info.md` skeleton.
4. Commit and push the scaffolding files to your knowledge repo.
5. Use the framework skills (`experience_inventory_bootstrap`, `career_narratives_builder`, `positioning_builder`) to generate `Experience_Inventory.md`, `Career_Narratives.md`, and `Positioning.md`.
6. Fill in `Contact_Info.md` with your personal contact details.

**Two-repo workflow:**
- Framework changes (skills, rules, README): commit and push from `career_development/`
- Master document changes: commit and push from within `career_development/personal/knowledge/`

---

## Why it is gitignored

The `career_development` framework repo gitignores the entire `personal/` directory, with no file-level exemptions, to ensure personal career data is never accidentally committed to a public or shared repository. This means new users cannot read this file from a fresh clone of the framework repo; instead, the canonical copy is shipped in `support/knowledge_repo_scaffolding/` within the framework repo itself and copied into the knowledge repo during setup.
