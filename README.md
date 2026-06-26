# Product AI Workshop

A 4-hour, hands-on workshop that teaches **non-technical people** (product
managers, designers, analysts) how to work effectively with coding agents using
the **Claude Desktop "Code" feature** (Claude Code, embedded in the Desktop app).

You will not be asked to write code. You *will* learn to direct an agent well:
give it the right context, package repeatable know-how as Skills and Rules,
delegate to Subagents, and plan a real change before any code is written.

> **Adapted from** the engineering bootcamp
> `hackersandwizards/dev-bootcamp-factory-workshop`. This version is rebuilt for a
> non-technical audience, trimmed to 4 hours, translated fully into English, and
> simplified for the audience. Everything runs in the Code feature, so the real
> Claude Code mechanisms — `CLAUDE.md`, Skills, Rules, Subagents — all work
> hands-on, and the spec-first module uses the open-source **Superpowers** skills.

## Why the "Code feature" and not regular chat?

The Code feature opens a real project folder and **automatically loads** that
folder's `.claude/` setup — `CLAUDE.md`, `.claude/skills/`, `.claude/rules/`,
`.claude/agents/`. Regular Claude Desktop chat does not. That auto-loading is what
makes the mechanisms in this workshop "just work" when you open a folder.

## Who this is for

People who work with engineering teams but don't code, want to use Claude
seriously for real product work, and have little or no Git/GitHub experience.

## What you'll be able to do by the end

- Move comfortably around Git/GitHub and let Claude do the Git for you.
- Engineer context so Claude's answers are sharp instead of generic.
- Use `CLAUDE.md` for persistent, always-on context.
- Build and trigger a **Skill** (reusable know-how).
- Scope conventions to document types with **Rules**.
- Delegate exploration to a **Subagent**.
- Run a lightweight **spec-first** workflow with **Superpowers**: brainstorm a
  design, turn it into a reviewed plan, then hand off to implementation.

## The 4-hour agenda

| Time | Module | Format |
| --- | --- | --- |
| 0:00–0:15 | Framing: you direct, you don't code | talk |
| 0:15–0:50 | [01 · Git & GitHub](exercises/01-git/README.md) | hands-on |
| 0:50–1:00 | Break | |
| 1:00–1:40 | [02 · Context + CLAUDE.md](exercises/02-context-and-claude-md/README.md) | hands-on |
| 1:40–2:10 | [03 · Skills](exercises/03-skills/README.md) | hands-on |
| 2:10–2:20 | Break | |
| 2:20–2:40 | [04 · Rules](exercises/04-rules/README.md) | hands-on |
| 2:40–3:00 | [05 · Subagents](exercises/05-subagents/README.md) | hands-on |
| 3:00–3:50 | [06 · Spec-first with Superpowers](exercises/06-sdd-superpowers/README.md) | hands-on |
| 3:50–4:00 | Wrap + [cheat sheet](CHEATSHEET.md) | |

## Before you arrive

Complete **[SETUP.md](SETUP.md)** — install Claude Desktop, Git, clone this repo,
and confirm the Code feature can open the folder. ~20 minutes, much calmer done at
home than in the room.

## Repository map

```
README.md         you are here
SETUP.md          one-time setup (do this before the workshop)
FACILITATOR.md    run-of-show and talking points (for the person teaching)
CHEATSHEET.md     one-page handout for participants
exercises/        the six modules, in order — each with exercise/ + solution/
sandbox/          a tiny calculator codebase (with CLAUDE.md) used by the
                  spec-first module
```

## How each exercise folder is laid out

- `exercise/` — your work area. Open this folder in the Code feature; you create
  the `.claude/...` files here.
- `solution/` — a reference implementation to compare against.
