# 03 · Projects (persistent context)

**Time:** 20 minutes · **Format:** hands-on

## The idea

A **Project** in Claude Desktop is a workspace with **persistent instructions**
and **knowledge files** that apply to every chat inside it. Instead of re-pasting
context (Module 02) every time, you set it once.

> In the developer tool (Claude Code), this same idea is a file called
> `CLAUDE.md` that's loaded automatically. In Claude Desktop it's a **Project**.
> Same purpose: always-on context and norms.

This is also the closest thing Desktop has to "**Rules**" — persistent
instructions Claude follows by default. (True file-scoped Rules are a Claude Code
feature; we cover that in Module 06.)

---

## Exercise A — The "always answer like a pirate" test (8 min)

This mirrors the classic developer exercise — it makes persistent context
*obvious*.

1. Ask Claude (no project): *"Tell me a short story about a deadline."* Note the
   normal tone.
2. Create a new **Project**. In its **instructions**, paste:
   > Always answer like a pirate. Start every answer with "Arrr".
3. Inside that Project, ask the same question.

The behavior is now **always on** — you didn't trigger it with a command, it's
just how this Project behaves. That's the lesson: a Project sets defaults.

## Exercise B — A useful Project (10 min)

Now make one you'd actually use. Create a Project called something like
**"Product Writing"** and give it real instructions, e.g.:

> You help a product manager at a grocery-deals app.
> - Audience for most outputs: non-technical end users.
> - Tone: clear, friendly, concrete; no jargon, no emojis.
> - When you write release notes, use a one-line title + 2–3 short sentences.
> - When unsure about a product detail, ask before assuming.

Optionally add a **knowledge file** (drag in a real doc — a style guide, a
glossary, a past PRD). Then run a couple of real requests and notice you no longer
have to re-explain who you are.

---

## When to use a Project vs. just typing context

- **Type it** (Module 02) for one-off asks.
- **Project** when the same context/norms apply across many chats: a product area,
  a writing style, an ongoing initiative.

## Takeaways

- Projects = persistent context + knowledge, set once.
- They're the Desktop home for "how Claude should behave by default."
- Knowledge files let Claude reference your real documents every time.
