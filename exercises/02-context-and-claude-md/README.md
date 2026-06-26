# 02 · Context Engineering + CLAUDE.md

**Time:** 40 minutes · **Format:** hands-on · **This is the heart of the workshop.**

## The one idea

> An agent's output is only as good as the context you give it.

You don't get better results by "prompting harder." You get them by giving Claude
the right *context*: what you want, for whom, with which constraints, in what
format, plus any background it can't know. Most disappointing AI answers are
actually **under-specified questions**.

## The anatomy of a good ask

1. **Role / goal** — who you are and what you're trying to achieve.
2. **Context** — the background Claude can't guess (audience, product, constraints).
3. **The task** — the specific thing to produce.
4. **Format** — how the answer should look (length, structure, tone).
5. **Guardrails** — what to avoid, what's out of scope.

---

## Exercise A — Feel the difference, then make it persistent (10 min)

In a Code-feature chat, ask the weak version, then the rich version:

- Weak: *"Write release notes for our new feature."*
- Rich: *"You're helping a PM at a grocery-deals app. We shipped saved searches:
  users save a search and get notified when a matching deal appears. Audience:
  non-technical end users in our in-app changelog. Write release notes: a punchy
  one-line title, 2–3 short sentences, friendly tone, no jargon, no emojis."*

Same model, wildly different quality. **The context did that.** Now the problem:
re-typing context every time is tiring. The fix is a file named **`CLAUDE.md`**.

In the Code feature, a `CLAUDE.md` in the folder is **loaded automatically** at
the start of every session — always-on context. Quick proof: open the
[`exercise/`](exercise/) folder, create `exercise/CLAUDE.md` containing one line —

```markdown
Always answer like a pirate. Start every answer with "Arrr".
```

— **start a new session** in that folder, and ask anything. It's pirate now,
always, with no command. That's always-on context. (Now delete that file before
the real exercise.)

## Exercise B — A CLAUDE.md that changes behavior (20 min)

A great `CLAUDE.md` doesn't just set tone — it teaches Claude **how your team
works**, so it does the right thing without being told each time. We'll encode a
real product-team convention: **where documents live and how they're named.**

In [`exercise/`](exercise/), create `exercise/CLAUDE.md` describing your filing
rules. Use [`solution/CLAUDE.md`](solution/CLAUDE.md) as the reference — the key
conventions are:

- Initiatives → `initiatives/<slug>/<slug>-initiative.md`
- Tickets for an initiative → `initiatives/<slug>/tickets/NN-<short-slug>-ticket.md`
- Filenames always end in `-initiative.md` or `-ticket.md`
- Apply this automatically — don't ask where files go.

**Start a new session** in `exercise/`, then watch the convention do the work:

1. *"Create an initiative for letting users save their searches."*
   → Claude files it at `initiatives/saved-search/saved-search-initiative.md` —
   you never said where.
2. *"Now create two tickets for that initiative."*
   → Claude creates `initiatives/saved-search/tickets/01-…-ticket.md` and
   `02-…-ticket.md`, numbered and placed correctly.

Look at the folder tree it produced. **You encoded the convention once; every
future document files itself.** That's the leap from "context as tone" to
"context as behavior."

> This sets up Module 04: those `-initiative.md` / `-ticket.md` filenames are
> exactly what the document-style **Rules** will hook onto to govern what goes
> *inside* each file.

## Exercise C — Read a real CLAUDE.md (10 min)

Open the [`sandbox/`](../../sandbox/) folder and ask:

> "Read CLAUDE.md, then explain in 3 bullets what this calculator does and what
> its coding conventions are."

Notice Claude answers from the *project's reality*. You'll use that same file in
the spec-first module.

---

## Takeaways

- Bad output → suspect missing context before blaming the model.
- The five parts (role, context, task, format, guardrails) are your checklist.
- `CLAUDE.md` makes context **persistent** *and* can encode **behavior** (filing,
  naming, conventions) — written once, applied every session.

## Anti-patterns

- Dumping everything "just in case" — irrelevant context dilutes the good context.
- Editing `CLAUDE.md` mid-session and expecting it to apply — it loads at session
  **start**; begin a new session.
