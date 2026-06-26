# 06 · Spec-first factory (lightweight SDD)

**Time:** 45 minutes · **Format:** hands-on

This is where Git, Context, CLAUDE.md, Skills, and Subagents come together into
one habit a product person can own: **write the plan before anyone builds.**

## The idea: a tiny "factory"

Good agentic work isn't one giant prompt. It's a small assembly line where each
stage hands off a **durable artifact** to the next:

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
review, and hand off. As a PM you'll mostly live in the first two stages — and
that's where the leverage is.

> The `planner` and `refine` skills are already installed in
> [`sandbox/.claude/skills/`](../../sandbox/.claude/skills/), so they load
> automatically when you open `sandbox/` in the Code feature. We use plain
> markdown spec files in `sandbox/specs/` — no extra tooling.

## Setup (2 min)

- Open the [`sandbox/`](../../sandbox/) folder in the Code feature (so `CLAUDE.md`
  and both skills auto-load).
- Skim the worked example:
  [`sandbox/specs/EXAMPLE-decimal-numbers.md`](../../sandbox/specs/EXAMPLE-decimal-numbers.md).
  That's what a finished spec looks like.

---

## Exercise A — Plan a feature (20 min)

We'll plan **parentheses support** for the calculator. The starter spec already
has the idea written down:
[`sandbox/specs/parentheses.md`](../../sandbox/specs/parentheses.md).

Ask:

> "Use the planner skill on specs/parentheses.md."

Now **do the work with Claude**:
- It surfaces findings, then asks you questions one at a time. Answer them.
- It proposes 2–3 approaches. **You pick one** — it won't decide for you.
- It writes a `## High-Level Plan` into the file.

Open `parentheses.md` and read what got written. You produced a reviewable
artifact — not a throwaway chat.

## Exercise B — Refine into a file-level plan (15 min)

> "Now use the refine skill on specs/parentheses.md."

Claude reads your High-Level Plan, looks at the real source files, and appends a
`## Refined Plan` listing the exact files to change and tests to write. Compare it
to the worked example. Notice: **refine couldn't run if planner hadn't written
the heading it reads.** That hand-off is the whole point.

*(Stretch: ask refine to use the `codebase-explorer` subagent from Module 05 for
its exploration.)*

## Exercise C — See the hand-off (facilitator demo, 8 min)

The facilitator runs an "implement" pass (or shows the finished branch): Claude
reads the `## Refined Plan`, makes the change on a branch, and runs the tests. The
takeaway for you: by the time code is written, every decision was already made,
reviewed, and recorded. **You controlled the outcome without writing a line of
code.**

---

## Debrief

- Why is an exact heading ("`## High-Level Plan`") doing so much work here?
- What would break if a stage rewrote the file instead of appending?
- Where in *your* real work could a "plan artifact before building" stage help?

## Takeaways

- A factory = stages that hand off durable artifacts via an exact contract.
- The plan is a reviewable document, not a disposable chat.
- Product people own the planning stages — the highest-leverage part.
