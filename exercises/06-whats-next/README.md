# 06 · What's next: Rules, Subagents, Hooks

**Time:** 20 minutes · **Format:** concept (no hands-on)

You've done the things you can do today in Claude Desktop. This module is a map of
what's *beyond* Desktop — the mechanisms engineers use in **Claude Code** (the
developer command-line tool). You don't need them yet. But knowing they exist
means you'll recognize when a problem calls for one, and you can ask an engineer
(or graduate to Claude Code yourself).

Think of it as a ladder. You've climbed the first rungs:

| Mechanism | Loads when | You already use the Desktop version |
| --- | --- | --- |
| **Project instructions** | Always-on for a workspace | ✅ Module 03 |
| **Skill** | On demand, when the task matches | ✅ Module 04 |
| **Rule** | Only for certain files/folders | ⬇️ Claude Code only |
| **Subagent** | A delegated, isolated helper | ⬇️ Claude Code only |
| **Hook** | Automatically, on a specific event | ⬇️ Claude Code only |

## Rules — context scoped to certain files

A **Rule** is like a Project instruction, but it only switches on for specific
files (e.g. "for any `.sql` file, always filter by date"). Desktop has no
file-scoped rules; its Projects apply everywhere. In Claude Code, Rules keep
narrow conventions from cluttering the always-on context.

*You'd want this when:* different parts of a codebase need different conventions.

## Subagents — delegating to a focused helper

A **Subagent** is a separate, narrow assistant the main agent can hand a job to —
e.g. "explore this large codebase and come back with a 5-bullet summary." It works
in its own context so it doesn't flood the main conversation with noise.

*The Desktop analogy you can use today:* open a **separate chat/Project** for a
big research task, then paste only the conclusion back. Same instinct, manual.

*You'd want the real thing when:* a task involves heavy reading/searching whose
transcript would otherwise drown your main conversation.

## Hooks — automatic guardrails on events

A **Hook** runs a command automatically when something happens — before a file is
saved, after a change is made, at the start of a session. Teams use them as
guardrails ("never let a secret get committed") or to prime context automatically.

*You'd want this when:* you need something to happen *every single time*,
deterministically, without relying on the agent (or a human) to remember.

---

## When would *you* graduate to Claude Code?

- You're editing real repositories regularly, not occasional files.
- You want guardrails (Hooks) and file-scoped Rules enforced for a team.
- You want the full planner → refine → **implement** factory running end-to-end,
  including branches, commits, and tests — automatically.

Until then, Desktop + Projects + Skills + the spec-first habit covers an enormous
amount of real product work.

## Where this came from

The hands-on engineering version of this workshop — with Subagents, Hooks, Rules,
evaluations, and observability as real exercises — lives in
`hackersandwizards/dev-bootcamp-factory-workshop`. That's your next step when
you're ready for Claude Code.
