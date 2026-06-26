# 06 · Spec-first development with Superpowers

**Time:** 50 minutes · **Format:** hands-on

This is where everything comes together into one habit a product person can own:
**design and plan a change before anyone builds it.** Instead of a homegrown
workflow, we use **Superpowers** — a free, open-source set of Claude skills that
encodes a disciplined spec-first process.

## The Superpowers factory

Superpowers gives you a three-stage assembly line, each stage producing a
**durable, reviewable artifact**:

```
   your idea
      │   brainstorming skill   (asks questions, proposes approaches)
      ▼
  design spec   →  docs/superpowers/specs/<date>-<topic>-design.md
      │   writing-plans skill   (turns the spec into bite-sized tasks)
      ▼
  implementation plan   →  docs/superpowers/plans/<date>-<feature>.md
      │   executing-plans / subagent-driven  (facilitator demo)
      ▼
  working code + tests
```

The magic isn't the AI — it's the **gates**. Brainstorming won't write a line of
code until you approve the design. Writing-plans won't hand off until the plan is
complete. **As a PM you live in the first two stages — and that's the leverage.**

## Setup (3 min)

- Install the **Superpowers** plugin (see [SETUP.md](../../SETUP.md): **Customize →
  Personal Plugins → Personal → Add marketplace**, paste
  `https://github.com/obra/superpowers.git`, **Sync**, then install **superpowers**
  from the **Code** tab and start a new session).
- Open the [`sandbox/`](../../sandbox/) folder so `CLAUDE.md` (the calculator's
  context) auto-loads.

---

## Exercise A — Brainstorm the feature (20 min)

We'll add **parentheses support** to the calculator. In the `sandbox/` session:

> "I want to add support for parentheses to the calculator, like `(1+2)*3`. Let's
> brainstorm it."

The **brainstorming** skill takes over and:
- explores the codebase (it reads `CLAUDE.md` and `src/`),
- asks you questions **one at a time** — answer them,
- proposes **2–3 approaches** with trade-offs and a recommendation — **you pick**,
- presents the design and asks for approval section by section,
- writes a **design spec** to `docs/superpowers/specs/…-design.md` and asks you to
  review it.

Open that spec file and read it. You produced a reviewed design — not a throwaway
chat. Compare with [`solution/example-design-spec.md`](solution/example-design-spec.md).

> Notice the gate: it would not start coding even if you asked. The approval is
> yours to give. That's the discipline you're learning to expect from an agent.

## Exercise B — Turn the spec into a plan (15 min)

When brainstorming finishes it hands off to **writing-plans**. Let it run:

> "Looks good — write the implementation plan."

The **writing-plans** skill produces a step-by-step plan at
`docs/superpowers/plans/…md`: exact files, bite-sized tasks, a test for each step.
Read it like a reviewer — is anything missing or risky? Compare with
[`solution/example-plan.md`](solution/example-plan.md).

This is the artifact a PM signs off on. By the time code is written, every
decision is already made and recorded.

## Exercise C — Execute (facilitator demo, 10 min)

The facilitator lets Superpowers execute the plan (via **subagent-driven
development**: a fresh subagent per task, reviewed between tasks — this is where
Module 05's subagent idea pays off). Watch it write a failing test, make it pass,
and commit, task by task. The takeaway for you: **you controlled the outcome
through the spec and the plan, without writing a line of code.**

---

## Debrief

- Where did a *gate* (design approval, plan review) change the outcome?
- Which stage is the highest-leverage one for *you* as a PM? (Hint: the first two.)
- How is a reviewed spec + plan different from "just ask the AI to build it"?

## Takeaways

- Superpowers = a disciplined, free spec-first workflow: brainstorm → plan →
  execute, each producing a durable artifact.
- Product people own brainstorming and plan review — the decisions that matter.
- The gates are the point: no code until the design is approved.
- Learn more: Superpowers — https://github.com/obra/superpowers
