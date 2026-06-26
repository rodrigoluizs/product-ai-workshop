# CLAUDE.md — calc sandbox

This file is **always-on context**. When you open this `sandbox/` folder in the
Claude Desktop **Code feature**, Claude reads `CLAUDE.md` automatically at the
start of the session — you don't have to paste or attach it.

> This file *is* one of the lessons. Notice how specific it is. That specificity
> is what makes Claude's output good. Vague context → vague output.

## What this is

A tiny TypeScript command-line calculator used as the shared codebase for the
spec-first exercise (Module 06, with the Superpowers skills). We design and plan a
change against this code; we do not need to ship it by hand.

## File layout

```
src/lexer.ts        Token stream. Types: NUMBER, PLUS, MINUS, STAR, SLASH, END.
src/parser.ts       Recursive descent. AST = interface Node { kind, value, op, left, right }.
src/evaluator.ts    Walks the AST, returns a number. Throws Error on divide-by-zero.
src/main.ts         The REPL. Catches Error, prints it, keeps going.
tests/*.test.ts     One test file per source module.
```

In the spec-first module, Superpowers writes its design spec and implementation
plan under `docs/superpowers/` here.

## Stack conventions (so Claude matches the existing code)

- **TypeScript with `strict` mode.** No `any` escape hatches where a real type
  would be clearer.
- **Vitest only** for tests. No other test frameworks.
- **Simple types over deep class hierarchies.** `Node` is one interface with a
  `kind` discriminator; add node kinds by extending the evaluator's switch.
- **Errors throw `Error`** with a readable message. The REPL is the single catch
  point.
- **Clarity over cleverness.** This is a teaching codebase.

## What Claude should not do here

- Don't add another build system or test runner (npm + tsc + Vitest is the stack).
- Don't pull in heavy dependencies.
- Don't restructure the AST into a class hierarchy "for cleanliness".
