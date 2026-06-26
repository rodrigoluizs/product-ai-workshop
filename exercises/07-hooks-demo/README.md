# 07 · Hooks (demo)

**Time:** part of the closing 15 minutes · **Format:** facilitator demo

You won't build a hook today — but you should know it exists, because it's the
last rung of the ladder.

## The idea

A **Hook** runs a command **automatically when something happens** — before a file
is saved, after a change is made, or at the end of every turn. Where a Skill or
Rule waits to be *triggered by you*, a hook fires on an **event**, every time,
deterministically — no relying on the agent (or a human) to remember.

Teams use hooks as **guardrails** ("never let a secret get committed") or to
**leave a trace** of what the agent did.

## The demo

The facilitator installs a tiny hook into `sandbox/` that writes one line every
time a turn ends:

```
example/settings.json    → registers a "Stop" hook
example/trace-run.sh      → appends a line to runs/trace.jsonl
```

Install (facilitator, from `sandbox/`):

```bash
mkdir -p .claude/hooks
cp ../exercises/07-hooks-demo/example/settings.json .claude/settings.json
cp ../exercises/07-hooks-demo/example/trace-run.sh   .claude/hooks/trace-run.sh
```

Restart the session so the hook loads, run any task, then look:

```bash
cat runs/trace.jsonl
```

Each run left a record: timestamp, branch, files changed, commit count. Nobody had
to remember to log it — the **event** did.

## Why it matters (talking point)

- **Observability:** you now have a durable trail of what the agent did. In a week
  you have data you didn't have before.
- **Guardrails:** the same mechanism can *block* a bad action instead of just
  recording it.

## Where you'd graduate to this

When you're running agents on real repositories for a team and you need something
to happen *every single time* — logging, validation, a safety check — without
trusting anyone to remember. That's a hook.
