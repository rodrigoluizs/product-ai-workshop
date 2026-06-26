# calc — Workshop Sandbox

A tiny Python command-line calculator, small enough to read in a couple of
minutes. In this workshop it's just a realistic codebase that Claude can *read*
so we can practice planning a change against it.

**You do not need to run this code.** A facilitator may run it on screen;
participants are never asked to build or test it.

## What it does

It evaluates simple math typed at a prompt:

```
> 1 + 2 * 3
7
> 10 / 2
5
> 1 / 0
error: Cannot divide by zero
```

It handles `+ - * /`, does multiplication/division before addition/subtraction,
and works with whole numbers and decimals. It does **not** support parentheses —
that's the feature we plan in Module 06.

## Layout

```
calc.py         the calculator: tokenize -> evaluate -> print, plus the prompt
test_calc.py    the tests (one per behavior)
CLAUDE.md       always-on context, auto-loaded by the Code feature (read this — it is the lesson)
```

In Module 06, the Superpowers skills write their design spec and plan under
`docs/superpowers/` here.

## If a facilitator wants to run it

```bash
python3 calc.py        # try the calculator
pip install pytest     # one-time, if needed
pytest                 # run the tests — all should pass
```
