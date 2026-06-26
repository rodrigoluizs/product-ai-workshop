# 02 · Context Engineering

**Time:** 45 minutes · **Format:** hands-on · **This is the heart of the workshop.**

## The one idea

> An agent's output is only as good as the context you give it.

You don't get better results by "prompting harder." You get them by giving Claude
the right *context*: what you want, for whom, with which constraints, in what
format, plus any background it can't know. Most disappointing AI answers are
actually **under-specified questions**.

## The anatomy of a good ask

A strong request usually has five parts:

1. **Role / goal** — who you are and what you're trying to achieve.
2. **Context** — the background Claude can't guess (audience, product, constraints).
3. **The task** — the specific thing to produce.
4. **Format** — how the answer should look (length, structure, tone).
5. **Guardrails** — what to avoid, what's out of scope.

You rarely need all five every time, but naming them is how you debug a bad answer.

---

## Exercise A — Feel the difference (10 min)

Ask Claude this weak prompt in a fresh chat:

> "Write release notes for our new feature."

Look at how generic it is. Now give it real context:

> "You're helping a product manager at a grocery-deals app. We just shipped
> *saved searches*: users can save a search (e.g. 'organic milk') and get a
> notification when a matching deal appears. Audience: non-technical end users in
> our in-app changelog. Write release notes: a punchy one-line title, 2–3 short
> sentences, friendly tone, no jargon, no emojis."

Compare the two outputs. Same model — wildly different quality. **The context did
that, not the model.**

## Exercise B — Rewrite your own (15 min)

Take a real request from your actual work (a summary, an email, a PRD section, a
competitor analysis). Write it the lazy way first. Then rewrite it using the five
parts above. Run both. Keep notes on what changed.

Share one before/after with the group.

## Exercise C — Context that lives in files (15 min)

Context doesn't have to be typed every time. With the **Filesystem connector**
on, ask:

> "Read sandbox/CONTEXT.md, then explain in 3 bullets what this calculator does
> and what its coding conventions are."

Notice Claude now answers from the *project's reality*, not generic knowledge.
That file is reusable context — you wrote it once, Claude uses it forever.

This is the bridge to the next module: when context is this useful, you want to
make it **persistent** (Projects) and **packaged** (Skills).

---

## Takeaways

- Bad output → suspect missing context before blaming the model.
- The five parts (role, context, task, format, guardrails) are your checklist.
- Context can be typed, attached, or read from a file — reusable beats retyped.

## Anti-patterns

- Dumping everything you know "just in case" — irrelevant context dilutes the good
  context. Be relevant, not exhaustive.
- Asking for output without saying who it's for or how long it should be.
- Treating a weak first answer as the model's ceiling instead of your prompt's floor.
