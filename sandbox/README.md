# calc — Workshop Sandbox

A minimal TypeScript command-line calculator: a lexer + a recursive-descent
parser + a tree-walking evaluator + a small REPL (the interactive prompt).

**You do not need to understand or run this code.** In this workshop it is just
a small, realistic codebase that Claude can *read* so we can practice planning a
change against real files. A facilitator may run it on screen; participants are
never asked to build or test it.

## What it does (for the curious)

It evaluates simple math typed at a prompt:

```
> 1+2*3
7
> 10/2
5
> 1/0
error: division by zero
```

It handles `+ - * /`, multiplication before addition, and whole numbers only.

## Layout

```
src/
  lexer.ts        turns the typed text into tokens (NUMBER, PLUS, MINUS, ...)
  parser.ts       turns tokens into a tree the computer can evaluate
  evaluator.ts    walks the tree and returns the number
  main.ts         the interactive prompt (REPL)
tests/            automated checks, one file per source file
package.json      project metadata and scripts
CLAUDE.md         always-on context, auto-loaded by the Code feature (read this — it is the lesson)
specs/            feature specs (plans) — the artifacts our "factory" produces
```

## If a facilitator wants to run it

```bash
npm install
npm run build
npm test       # all tests should pass
npm run repl   # try the calculator yourself
```
