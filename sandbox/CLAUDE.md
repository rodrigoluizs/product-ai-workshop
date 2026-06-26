# CLAUDE.md — calc sandbox

This file is **always-on context**. When you open this `sandbox/` folder in the
Claude Desktop **Code feature**, Claude reads `CLAUDE.md` automatically at the
start of the session — you don't have to paste or attach it.

> This file *is* one of the lessons. Notice how specific it is. That specificity
> is what makes Claude's output good. Vague context → vague output.

## What this is

A tiny Python command-line calculator used as the shared codebase for the
spec-first exercise (Module 06, with the Superpowers skills). We design and plan a
change against this code; we do not need to ship it by hand. It's intentionally
small enough to read top to bottom.

## File layout

```
calc.py         The whole calculator: tokenize -> evaluate -> print, plus a REPL.
test_calc.py    Plain tests (pytest), one per behavior.
```

`calc.py` reads in three small steps:
1. **tokenize(text)** — splits "1 + 2*3" into `[1.0, "+", 2.0, "*", 3.0]`.
2. **evaluate(tokens)** — collapses `*` and `/` first, then `+` and `-`.
3. **main()** — the interactive prompt.

In the spec-first module, Superpowers writes its design spec and implementation
plan under `docs/superpowers/` here.

## What it does today

- Operators `+ - * /` on whole numbers and decimals.
- Multiply/divide happen before add/subtract (`1 + 2 * 3` → `7`).
- It does **not** support parentheses yet — that's the feature we plan in Module 06.

## Conventions (so Claude matches the existing code)

- **Plain, readable Python.** Simple functions, no classes, clear names. This is a
  teaching codebase — clarity beats cleverness.
- **Errors raise exceptions** (`ValueError`, `ZeroDivisionError`) with a readable
  message. `main()` is the single place that catches them and keeps the prompt
  running.
- **Tests use pytest**, one test per behavior, written to read like a sentence.
- **No new dependencies.** The standard library is enough.

## What Claude should not do here

- Don't add heavy dependencies or a framework.
- Don't rewrite it into classes "for cleanliness" — keep the plain functions.
- Don't use Python's built-in `eval()` to do the math (it would hide the lesson).
