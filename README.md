# Product AI Workshop

A 4-hour, hands-on workshop that teaches **non-technical people** (product
managers, designers, analysts) how to work effectively with coding agents using
**Claude Desktop**.

You will not be asked to write code. You *will* learn to direct an agent well:
give it the right context, package repeatable know-how as Skills, keep persistent
preferences in Projects, and plan a real change before any code is written.

> **Adapted from** the engineering "factory" bootcamp
> (`hackersandwizards/dev-bootcamp-factory-workshop`). That version targets Claude
> Code (the developer CLI). This version is rebuilt for Claude Desktop and a
> non-technical audience: the command-line and developer-only mechanisms
> (Subagents, Hooks, file-scoped Rules) are covered as *concepts* in the closing
> module, not as hands-on exercises.

## Who this is for

People who:
- work with engineering teams but don't write code themselves,
- want to use Claude (Desktop) seriously for real product work,
- have little or no experience with Git/GitHub.

## What you'll be able to do by the end

- Move comfortably around Git/GitHub: branches, commits, pull requests — and let
  Claude do the Git work for you via the GitHub connector.
- Engineer context so Claude's answers are sharp instead of generic.
- Use **Projects** to give Claude persistent instructions and knowledge.
- Build and use a **Skill** — reusable, packaged know-how.
- Run a lightweight **spec-first** workflow: plan a change as a durable artifact
  before anyone builds it.
- Know what Rules, Subagents, and Hooks are, and when you'd graduate to Claude
  Code to use them.

## The 4-hour agenda

| Time | Module | Format |
| --- | --- | --- |
| 0:00–0:15 | Framing: you direct, you don't code | talk |
| 0:15–0:55 | [01 · Git & GitHub](exercises/01-git-intro/README.md) | hands-on |
| 0:55–1:05 | Break | |
| 1:05–1:50 | [02 · Context Engineering](exercises/02-context-engineering/README.md) | hands-on |
| 1:50–2:30 | [03 · Projects](exercises/03-projects/README.md) + [04 · Skills](exercises/04-skills/README.md) | hands-on |
| 2:30–2:40 | Break | |
| 2:40–3:25 | [05 · Spec-first (lightweight SDD)](exercises/05-spec-first-sdd/README.md) | hands-on |
| 3:25–3:45 | [06 · What's next: Rules, Subagents, Hooks](exercises/06-whats-next/README.md) | concept |
| 3:45–4:00 | Wrap + [cheat sheet](CHEATSHEET.md) | |

## Before you arrive

Complete **[SETUP.md](SETUP.md)** — install Claude Desktop, Git, clone this repo,
and enable the Filesystem connector. It takes about 20 minutes and is much less
stressful done at home than in the room.

## Repository map

```
README.md         you are here
SETUP.md          one-time setup (do this before the workshop)
FACILITATOR.md    run-of-show and talking points (for the person teaching)
CHEATSHEET.md     one-page handout for participants
exercises/        the six modules, in order
sandbox/          a tiny calculator codebase Claude reads during the spec exercise
```
