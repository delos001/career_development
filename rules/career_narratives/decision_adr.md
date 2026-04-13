# Decision Format: ADR (Architecture Decision Record)

Adapted from the Architecture Decision Record format, originally developed for software engineering but adopted broadly across technical and organizational leadership contexts. Lean and portable — favors concision over depth. Use when decisions need to be recorded quickly, shared across an organization, or maintained as a log across many decisions over time. Less optimized for interview depth than the personal format.

---

## Format

Every entry carries a 5-line metadata block directly under the `## [Title]` heading, before any section:

```
Tags: [pipe-separated Capability values]
Archetype: [pipe-separated Archetype values]
Era: [single Era value]
Added: YYYY-MM
Last Used:
```

Controlled values come from the Tag Taxonomy header at the top of `knowledge/Career_Narratives.md`. `Added` is stamped at creation (current month). `Last Used` is left blank by the builder and stamped by output-producing skills at session close.

### Context
The situation, constraint, or organizational pressure that made a decision necessary. Include relevant background — what was the environment, what was changing, and why the decision could not be deferred.

### Decision
The choice made, stated clearly in one or two sentences. Active voice — "We selected X" or "I chose X" rather than "X was selected."

### Alternatives
Options that were considered and rejected. For each alternative: name it and state the specific reason it was not chosen. One or two sentences per alternative is sufficient.

### Consequences
The outcomes of the decision — both positive and negative. Include known tradeoffs accepted as part of the choice. Distinguish between outcomes that were anticipated and those that emerged afterward.

---

## Guidance Notes

- ADR is the most widely recognized decision documentation format outside of healthcare. It is used at AWS, Microsoft, Thoughtworks, and across engineering and architecture organizations.
- The format is intentionally lean. It is designed for auditability and organizational sharing, not for interview depth. If interview-level detail is needed, use the Personal format instead.
- The Alternatives field is the most important for demonstrating judgment. A decision with no documented alternatives appears unconsidered.
- ADR entries can be maintained as a numbered log (ADR-001, ADR-002, etc.) to support retrieval and cross-referencing over time.

---

## References

- Nygard, Michael. *Documenting Architecture Decisions.* Cognitect, 2011. Original description of the ADR format.
- AWS Prescriptive Guidance. *Architecture Decision Records.* docs.aws.amazon.com/prescriptive-guidance
- Microsoft Azure Well-Architected Framework. *Architecture Decision Records.* learn.microsoft.com/azure/well-architected
- ADR GitHub. *ADR Templates and Tools.* adr.github.io
