# Parentheses Support — Design

> Example output of the Superpowers **brainstorming** skill, for reference. In a
> real session this is written to `docs/superpowers/specs/<date>-parentheses-design.md`
> and committed. Yours will read differently — what matters is that it's a
> reviewed design, agreed before any code.

## Problem

The calculator only handles flat expressions with `+ - * /` and a fixed order of
operations. Users can't control evaluation order. We want round parentheses `(`
and `)` so nested sub-expressions evaluate first. Behavior without parentheses
must not change.

## Goal / Success criteria

- `(1+2)*3` → `9`, `2*(3+4)` → `14`, `((1+2)*(3+4))` → `21`.
- Every existing expression returns the same result as before (no regression).
- Clear, non-crashing errors for `(1+2`, `1+2)`, and `()`.

## Approaches considered

1. **Grammar extension (recommended).** Treat `(` and `)` as new tokens and allow
   a parenthesized sub-expression at the innermost grammar level. Fits the
   existing recursive-descent parser; precedence/associativity untouched.
2. **Pre-pass that rewrites parentheses away.** Rejected — more code, harder to
   give good error messages, and it duplicates parser logic.

## Chosen design

- **Lexer:** add `LPAREN` / `RPAREN` token types; emit them for `(` and `)`.
- **Parser:** at the `factor` level, accept `'(' expr ')'` (recurse into a full
  expression). Report missing/extra/empty parens as `Error`.
- **Evaluator / AST:** unchanged — grouping is encoded by the tree shape, so no
  new node kind.
- **Error handling:** parser throws `Error`; the REPL stays the single catch
  point and keeps running.

## Non-Goals

Unary minus, other bracket shapes (`[]`, `{}`), variables, functions, new
operators, parser performance work.

## Testing

Lexer test for `()`; parser tests for grouping/nesting and the three error cases;
evaluator tests for the success criteria plus a no-parens regression test.
