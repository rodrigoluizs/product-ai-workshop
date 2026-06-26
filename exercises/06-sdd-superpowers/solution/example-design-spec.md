# Parentheses Support — Design

> Example output of the Superpowers **brainstorming** skill, for reference. In a
> real session this is written to `docs/superpowers/specs/<date>-parentheses-design.md`
> and committed. Yours will read differently — what matters is that it's a
> reviewed design, agreed before any code.

## Problem

The calculator (`calc.py`) only handles flat expressions with `+ - * /` and a
fixed order of operations. Users can't control evaluation order. We want round
parentheses `(` and `)` so nested sub-expressions evaluate first. Behavior without
parentheses must not change.

## Goal / Success criteria

- `(1 + 2) * 3` → `9`, `2 * (3 + 4)` → `14`, `((1 + 2) * (3 + 4))` → `21`.
- Every existing expression returns the same result as before (no regression).
- Clear, non-crashing errors for `(1 + 2`, `1 + 2)`, and `()`.

## Approaches considered

1. **Tokenize parens, then resolve innermost groups first (recommended).** Let
   `tokenize` recognize `(` and `)`. In `evaluate`, before the existing
   multiply/divide and add/subtract passes, repeatedly find the innermost
   `( … )`, evaluate what's inside with the existing logic, and replace the group
   with its result. Reuses everything we already have; precedence untouched.
2. **Switch to Python's built-in `eval()`.** Rejected — it would do the whole job
   but hide the lesson and lose our friendly error messages.

## Chosen design

- **`tokenize`:** also emit `"("` and `")"` as tokens (today they raise an error).
- **`evaluate`:** add a first step that resolves parentheses — find the innermost
  matching pair, evaluate the tokens between them (reusing `evaluate`), replace the
  whole `( … )` span with that single number, and repeat until no parens remain.
  Then run the existing `*`/`/` and `+`/`-` passes unchanged.
- **Errors:** a missing/extra/empty pair raises `ValueError` with a readable
  message; `main()` stays the single catch point.

## Non-Goals

Unary minus, other bracket shapes (`[]`, `{}`), variables, functions, new
operators.

## Testing (pytest, in `test_calc.py`)

A test that `tokenize("()")` yields the two paren tokens; calculate tests for the
success criteria; a test per error case; and a no-parens regression test.
