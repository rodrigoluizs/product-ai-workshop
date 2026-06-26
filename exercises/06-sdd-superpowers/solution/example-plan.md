# Parentheses Support Implementation Plan

> Example output of the Superpowers **writing-plans** skill, for reference. In a
> real session this is written to `docs/superpowers/plans/<date>-parentheses.md`.
> Note the bite-sized, test-first tasks — that's what makes it executable and
> reviewable. Abbreviated here.

> **For agentic workers:** REQUIRED SUB-SKILL: use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add round-parenthesis grouping to the calculator.

**Architecture:** Extend the lexer with two token types and the parser's `factor`
rule with a `'(' expr ')'` alternative. AST and evaluator unchanged.

**Tech Stack:** TypeScript (strict), Vitest, ESM.

## Global Constraints

- No new dependencies. npm + tsc + Vitest only.
- No new AST node kind; grouping is encoded by tree shape.
- Errors throw `Error`; the REPL stays the single catch point.

---

### Task 1: Lex parentheses

**Files:** Modify `src/lexer.ts`; Test `tests/lexer.test.ts`

- [ ] **Step 1 — failing test:** add `it("tokenizes parentheses")` expecting `"()"`
  → tokens `LPAREN, RPAREN, END`.
- [ ] **Step 2 — run it, confirm it fails** (`LPAREN` undefined).
- [ ] **Step 3 — implement:** add `LPAREN`/`RPAREN` to the token enum and emit them
  for `(` and `)` in the scan loop.
- [ ] **Step 4 — run tests, confirm pass.**
- [ ] **Step 5 — commit:** `feat: lex parentheses`.

### Task 2: Parse grouped expressions

**Files:** Modify `src/parser.ts`; Test `tests/parser.test.ts`

- [ ] **Step 1 — failing tests:** `"(1+2)*3"` → `Mul(Add(1,2),3)`; `"(1+2"` →
  throws; `"()"` → throws.
- [ ] **Step 2 — run, confirm fail.**
- [ ] **Step 3 — implement:** in `parseFactor()`, on `LPAREN` consume it, recurse
  into `parseExpr()`, then require `RPAREN`; throw `Error` on missing/empty.
- [ ] **Step 4 — run tests, confirm pass.**
- [ ] **Step 5 — commit:** `feat: parse parenthesized expressions`.

### Task 3: End-to-end evaluation + regression

**Files:** Test `tests/evaluator.test.ts`

- [ ] **Step 1 — tests:** `(1+2)*3`→9, `2*(3+4)`→14, `((1+2)*(3+4))`→21,
  `(2+3)*(4-1)`→15, and regression `1+2*3`→7.
- [ ] **Step 2 — run; they should pass** with Tasks 1–2 done (no eval change needed).
- [ ] **Step 3 — commit:** `test: parentheses end-to-end + regression`.
