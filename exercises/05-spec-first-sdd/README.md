# 05 · Spec-first (lightweight SDD)

**Time:** 45 minutes · **Format:** hands-on

This is where Git, Context, Projects, and Skills come together into one habit
that product people can own: **write the plan before anyone builds.**

## The idea: a tiny "factory"

Good agentic work isn't one giant prompt. It's a small assembly line where each
stage hands off a **durable artifact** to the next. Ours has three stages:

```
   your idea
      │   planner skill
      ▼
  ## High-Level Plan       (approach + acceptance criteria)
      │   refine skill
      ▼
  ## Refined Plan          (which files change + how to test)
      │   implement  (facilitator demo)
      ▼
  working code
```

The magic isn't the AI — it's the **contract**: each stage reads and writes
**exact section headings** in a shared spec file. That's what lets you stop,
review, and hand off. As a PM, you'll mostly live in the first two stages — and
that's exactly where the leverage is.

> Developers do this in Claude Code with branches and a `beans` tool. We do the
> same thing with **plain markdown files** in `sandbox/specs/`, edited by Claude
> via the Filesystem connector. Same lesson, no command line.

## Setup (3 min)

- Make sure the **Filesystem connector** can see the workshop folder.
- Install the two skills the same way as Module 04 (zip the folder so `SKILL.md`
  is at the top, then **Settings → Capabilities → Upload skill**):
  [`solution/planner/`](solution/planner/) and [`solution/refine/`](solution/refine/).
- Skim the worked example: [`sandbox/specs/EXAMPLE-decimal-numbers.md`](../../sandbox/specs/EXAMPLE-decimal-numbers.md).
  That's what a finished spec looks like.

---

## Exercise A — Plan a feature (20 min)

We'll plan **parentheses support** for the calculator. The starter spec already
has the idea written down: [`sandbox/specs/parentheses.md`](../../sandbox/specs/parentheses.md).

In Claude Desktop:

> "Use the planner skill on sandbox/specs/parentheses.md. Read sandbox/CONTEXT.md
> first."

Now **do the work with Claude**:
- It will surface findings, then ask you questions one at a time. Answer them.
- It will propose 2–3 approaches. **You pick one** — Claude won't decide for you.
- It writes a `## High-Level Plan` into the file.

Open `parentheses.md` and read what got written. You just produced a reviewable
artifact — not a throwaway chat.

## Exercise B — Refine into a file-level plan (15 min)

> "Now use the refine skill on sandbox/specs/parentheses.md."

Claude reads your High-Level Plan, looks at the real source files, and appends a
`## Refined Plan` listing the exact files to change and tests to write. Compare it
to the worked example. Notice: **refine couldn't run if planner hadn't written
the heading it reads.** That hand-off is the whole point.

## Exercise C — See the hand-off (facilitator demo, 7 min)

The facilitator runs an "implement" pass (or shows the finished branch). The
takeaway for you: by the time code is written, every decision was already made,
reviewed, and recorded in the spec. **You controlled the outcome without writing
a line of code.**

---

## Debrief

- Why is an exact section heading ("`## High-Level Plan`") doing so much work here?
- What would break if a stage rewrote the file instead of appending to it?
- Where in *your* real work could a "plan artifact before building" stage help?

## Takeaways

- A factory = stages that hand off durable artifacts via an exact contract.
- The plan is a reviewable document, not a disposable chat.
- Product people own the planning stages — the highest-leverage part.
