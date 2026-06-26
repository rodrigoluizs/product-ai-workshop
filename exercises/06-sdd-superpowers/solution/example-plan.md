# Parentheses Support Implementation Plan

> Example output of the Superpowers **writing-plans** skill, for reference. In a
> real session this is written to `docs/superpowers/plans/<date>-parentheses.md`.
> Note the bite-sized, test-first tasks — that's what makes it executable and
> reviewable. Abbreviated here.

> **For agentic workers:** REQUIRED SUB-SKILL: use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add round-parenthesis grouping to the calculator.

**Architecture:** `tokenize` emits `(` and `)`; `evaluate` resolves the innermost
`( … )` first (reusing itself), then runs the existing precedence passes.

**Tech Stack:** Python 3, pytest.

## Global Constraints

- No new dependencies; standard library only.
- Don't use `eval()`.
- Errors raise `ValueError`; `main()` stays the single catch point.

---

### Task 1: Tokenize parentheses

**Files:** Modify `calc.py` (`tokenize`); Test `test_calc.py`

- [ ] **Step 1 — failing test:** add `test_tokenizes_parentheses` expecting
  `tokenize("()")` to contain the `"("` and `")"` tokens.
- [ ] **Step 2 — run it, confirm it fails** (today `(` raises `ValueError`).
- [ ] **Step 3 — implement:** in `tokenize`, treat `(` and `)` as their own tokens
  instead of raising.
- [ ] **Step 4 — run tests, confirm pass.**
- [ ] **Step 5 — commit:** `feat: tokenize parentheses`.

### Task 2: Resolve parentheses in evaluate

**Files:** Modify `calc.py` (`evaluate`); Test `test_calc.py`

- [ ] **Step 1 — failing tests:** `calculate("(1 + 2) * 3")` → `9`;
  `calculate("(1 + 2")` raises `ValueError`; `calculate("()")` raises `ValueError`.
- [ ] **Step 2 — run, confirm fail.**
- [ ] **Step 3 — implement:** before the existing passes, repeatedly find the
  innermost `( … )`, evaluate the inside with `evaluate`, and replace the span with
  the result; raise `ValueError` on a missing/empty pair.
- [ ] **Step 4 — run tests, confirm pass.**
- [ ] **Step 5 — commit:** `feat: evaluate parenthesized groups`.

### Task 3: Nesting + regression

**Files:** Test `test_calc.py`

- [ ] **Step 1 — tests:** `((1 + 2) * (3 + 4))` → `21`; `(2 + 3) * (4 - 1)` → `15`;
  regression `1 + 2 * 3` → `7`.
- [ ] **Step 2 — run; they should pass** with Tasks 1–2 done.
- [ ] **Step 3 — commit:** `test: nested parentheses + regression`.
