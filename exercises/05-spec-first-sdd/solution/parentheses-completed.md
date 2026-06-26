# Parentheses support in the calculator (completed)

> Reference solution: what `sandbox/specs/parentheses.md` should look like after
> the planner and refine skills have both run. Yours will differ in wording —
> that's fine. What matters is the structure and the exact section headings.

Status: completed
Type: feature

The calculator currently only supports flat expressions with `+ - * /` and a
fixed order of operations. We add round parentheses `(` and `)` for grouping, so
nested sub-expressions are evaluated before the surrounding expression. Behavior
without parentheses stays unchanged.

## High-Level Plan

**Approach** — Grammar extension. Round parentheses are recognized as new input
symbols and allowed as an extra option at the innermost expression level. Grouping
fits cleanly into the existing recursive structure; operator precedence and
associativity stay unchanged.

**Steps**
- Recognize the two parenthesis symbols so `(` and `)` become their own tokens.
- Extend the innermost expression level with a "parenthesized sub-expression"
  option that may recursively contain a full expression.
- Report error cases (missing closing paren, extra closing paren, empty
  parentheses) as readable parser errors without crashing the REPL.
- Add tests at every level: symbol recognition, nested grammar, end-to-end
  evaluation, and the error paths.

**Acceptance Criteria**
- `(1+2)*3` → `9`
- `2*(3+4)` → `14`
- Nested parentheses resolve correctly, e.g. `((1+2)*(3+4))` → `21`
- Parentheses override precedence, e.g. `(2+3)*(4-1)` → `15`
- All previous expressions without parentheses return the same results (no
  regression).
- A missing closing paren (`(1+2`) gives a readable parser error; REPL continues.
- An extra closing paren (`1+2)`) gives a parser error; REPL continues.
- Empty parentheses `()` give a parser error.

**Non-Goals**
- Unary minus / unary plus.
- Square `[]` or curly `{}` brackets.
- Variables, functions, additional operators.
- Changing the existing operator precedence.
- Parser performance optimizations.

## Refined Plan

### Files to change
- `src/lexer.ts` — add `LPAREN` and `RPAREN` to the token-type enum; in the
  symbol switch in `next()`, return a single-char token for `(` and `)`; add their
  names to the token-name helper (used in parser error messages).
- `src/parser.ts` — update the grammar comment to `factor := NUMBER | '(' expr ')'`;
  in `parseFactor()`, add an `LPAREN` branch: consume `(`, recursively parse a full
  expression, then require `)`; treat empty `()` and a missing `)` as `Error`.
- `tests/lexer.test.ts` — add `it("tokenizes parentheses")`.
- `tests/parser.test.ts` — add tests for grouping overriding precedence, nesting,
  missing/extra/empty parens.
- `tests/evaluator.test.ts` — add end-to-end evaluation tests plus a no-parens
  regression test.

### New signatures
- None. `Lexer.next()` and `Parser.parseFactor()` keep their signatures —
  the change is inside existing switches/branches. The AST/evaluator are
  unchanged; grouping is encoded by the tree shape, so no new node kind.

### Test sketch
- lexer "tokenizes parentheses" — input `"()"` → tokens `LPAREN, RPAREN, END`.
- parser "parens override precedence" — `"(1+2)*3"` → `Mul(Add(1,2), 3)`.
- parser "nested parens" — `"((1+2)*(3+4))"` → `Mul(Add(1,2), Add(3,4))`.
- parser "missing closing paren" — `"(1+2"` → `Error`.
- parser "empty parens" — `"()"` → `Error`.
- parser "stray closing paren" — `"1+2)"` → `Error`.
- evaluator "(1+2)*3" → `9`; "2*(3+4)" → `14`; "((1+2)*(3+4))" → `21`;
  "(2+3)*(4-1)" → `15`; regression "1+2*3" → `7`.
