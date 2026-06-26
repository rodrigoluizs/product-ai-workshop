# CONTEXT.md — calc sandbox

This is a **context note**: a short, durable description of a codebase that we
hand to Claude so it answers with the project's reality instead of generic
guesses. In Claude Desktop you give Claude this context in one of two ways:

1. Paste it (or attach this file) into a **Project**'s instructions/knowledge, or
2. Enable the **Filesystem connector** pointed at this folder, then ask Claude to
   "read CONTEXT.md before answering."

> This file *is* one of the lessons. Notice how specific it is. That specificity
> is what makes Claude's output good. Vague context → vague output.

## What this is

A tiny TypeScript command-line calculator used as the shared codebase for the
spec-first ("factory") exercise. Participants plan a change against this code;
they do not have to build or run it.

## File layout

```
src/lexer.ts        Token stream. Types: NUMBER, PLUS, MINUS, STAR, SLASH, END.
src/parser.ts       Recursive descent. AST = interface Node { kind, value, op, left, right }.
src/evaluator.ts    Walks the AST, returns a number. Throws Error on divide-by-zero.
src/main.ts         The REPL. Catches Error, prints it, keeps going.
tests/*.test.ts     One test file per source module.
package.json        Scripts and dependencies (ESM module).
tsconfig.json       TypeScript config (strict mode).
specs/<name>.md     One spec per feature — the plan artifacts (see below).
```

## How the "factory" produces a spec

A **spec** is a plain markdown file in `specs/`. It is filled in two stages, and
the contract between stages is the exact section headings:

1. **Planner** writes a `## High-Level Plan` section (the approach + acceptance
   criteria, no file paths yet).
2. **Refine** reads `## High-Level Plan` and adds a `## Refined Plan` section
   (the concrete files to touch + a test sketch).

Each stage *appends* its section; it never rewrites the file from scratch. The
headings are the hand-off contract — that is the whole point of the exercise.

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
