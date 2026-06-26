# 05 · Subagents

**Time:** 20 minutes · **Format:** hands-on (light)

## The idea

A **Subagent** is a separate, focused helper that the main agent can hand a job
to — for example, "explore this codebase and come back with a tight summary." It
works in its **own context**, so the messy details of its search don't flood your
main conversation. You get back just the conclusion.

Think of it as delegating to a specialist and receiving a one-page report instead
of watching them rummage through every drawer.

A subagent is defined by a file in `.claude/agents/`, with frontmatter that says
its name, when to use it, and which tools it's allowed to use.

---

## Exercise A — Install and run a subagent (12 min)

Open the [`sandbox/`](../../sandbox/) folder in the Code feature, then copy the
ready-made explorer into it (ask Claude, or do it by hand):

```
copy  exercises/05-subagents/solution/.claude/agents/codebase-explorer.md
into  sandbox/.claude/agents/codebase-explorer.md
```

Start a new session in `sandbox/` and ask:

> "Use the codebase-explorer subagent to find where the calculator turns text
> into numbers, and where division by zero is handled."

Watch what comes back: a compact, structured summary with `file:line` references
— not a wall of search output. The exploration happened "out of sight" in the
subagent's own context.

## Exercise B — Read why it's safe (8 min)

Open [`solution/.claude/agents/codebase-explorer.md`](solution/.claude/agents/codebase-explorer.md)
and notice the guardrails:

- **read-only** — it's only allowed to look, never edit;
- a strict **output contract** (Summary / Findings / Relationships);
- a length cap so it returns a summary, not a transcript.

That's the pattern: a subagent has a narrow job, limited tools, and a defined
output shape.

> **Where this connects:** in Module 06, Superpowers executes a plan with
> *subagent-driven development* — a fresh subagent per task — the same idea you're
> seeing here, applied to building, so each task stays in its own clean context.

---

## Takeaways

- Subagent = a focused, isolated helper that returns a conclusion, not its
  scratch work.
- Best for read-heavy exploration, summaries, and specialized checks.
- Defined in `.claude/agents/`; give it a narrow job, limited tools, and an
  output contract.
