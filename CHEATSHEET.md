# Cheat Sheet — Product AI Workshop

Keep this. It's the whole workshop on one page.

## The five parts of a good ask

1. **Role / goal** — who you are, what you want.
2. **Context** — what Claude can't guess (audience, product, constraints).
3. **Task** — the specific thing to produce.
4. **Format** — length, structure, tone.
5. **Guardrails** — what to avoid / out of scope.

> Bad output? Suspect a missing part above before blaming the model.

## The mechanism ladder (Code feature)

| Mechanism | Lives in | Switches on when… |
| --- | --- | --- |
| **CLAUDE.md** | folder root | always (loaded at session start) |
| **Skill** | `.claude/skills/` | a request matches its description |
| **Rule** | `.claude/rules/` | you work on a file matching its glob |
| **Subagent** | `.claude/agents/` | the agent delegates a focused job |

> All of these **auto-load when you open the folder** — but only at **session
> start**. Change one? Start a new session.

## The product workflow we built

- **Where docs go** (CLAUDE.md): `initiatives/<slug>/<slug>-initiative.md`;
  tickets at `initiatives/<slug>/tickets/NN-<slug>-ticket.md`.
- **What's inside** (Rules): `*-initiative.md` → outcome + success metric;
  `*-ticket.md` → testable acceptance criteria.

## Git in plain English

| Term | Meaning |
| --- | --- |
| Repo | A tracked project folder |
| Commit | A labeled snapshot of changes |
| Branch | A safe parallel copy to experiment in |
| Pull Request | "Please review and merge my branch" |

**Golden rule:** branch → commit → PR → review. Never edit `main` directly.

Or just ask Claude in the Code feature:
> "Create a branch, make this change, commit it, and open a PR. Show me the link."

Undo anything:
> "Discard my uncommitted changes and switch me back to a clean main."

## Spec-first with Superpowers

```
idea → brainstorming → design spec → writing-plans → plan → execute
```
Each arrow is a **gate**: no code until you approve the design; no execution until
the plan is reviewed. The spec and plan are durable documents, not a disposable
chat. You own brainstorming and plan review — the decisions that matter.

Install: `/plugin` → `superpowers`. Start with: *"Let's brainstorm <feature>."*

## Skills: what makes one good

- A **description** written as triggers ("use when the user asks to…").
- Explicit **rules** · worked **examples** · a **calibration** note.

## One thing to do Monday

Pick one: write a `CLAUDE.md` of conventions for your area · turn a recurring task
into a Skill · plan your next feature as a spec before building it.
