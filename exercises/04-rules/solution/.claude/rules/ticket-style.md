---
glob: "**/*-ticket.md"
---

# Ticket document style

When working on a ticket document (`*-ticket.md`), enforce these conventions.
Tickets are for the team that will build the thing — they must be concrete and
buildable.

- **Small and single-purpose.** One ticket = one shippable change. If it's big,
  suggest splitting it.
- **Required sections:** Context (1–2 lines + link to the initiative) ·
  Acceptance Criteria · Out of scope.
- **Testable acceptance criteria.** Each criterion is a checkable statement
  ("Given X, when Y, then Z"). Vague criteria ("works well") are not allowed —
  ask for the concrete behavior.
- **Link up to the initiative** it serves, so the *why* is one click away.
- It's fine to mention concrete UI/behavior; keep solution detail minimal and
  leave room for engineering judgment.
