# Decimal number support in the calculator

> **This is a worked example** — a finished spec, both stages filled in. Use it as
> your reference for "what good looks like". In the spec-first exercise you will
> produce a *new* spec (for parentheses) that looks like this one.

Status: example / completed
Type: feature

The calculator currently only handles whole-number arithmetic. Users want to
calculate with decimals (e.g. `1.5 + 2.5`). This feature moves the whole
calculation pipeline to floating point, accepts a decimal point in the input,
and prints results without unnecessary trailing zeros.

**Notes:**
- Full migration of the internal number type to floating point (no coexistence
  with a separate integer type).
- The decimal separator in input and output is the point `.`.
- Output trims trailing zeros; whole-number results print without a decimal point.
- Existing division behavior changes on purpose: `7/2` now yields `3.5` instead
  of `3`. That is part of the feature, not a regression.
- Divide-by-zero stays a runtime `Error`; the REPL remains the single catch point.

## High-Level Plan

**Approach** — Direct migration in one spec. Because changing the value type
inherently runs through every layer of the pipeline (lexer, AST, evaluator,
REPL output), one coherent change is clearer than an artificially split
intermediate state. Tests are updated per module alongside the change.

**Steps**
- The lexer accepts decimal literals with a point as the separator; the number
  token carries a floating-point value.
- AST nodes and parser constants carry values as a floating-point type.
- The evaluator computes in floating point throughout; divide-by-zero stays a
  runtime error.
- The REPL formats results: trailing zeros removed, point as the decimal
  separator, whole-number results without a decimal point.
- Existing unit tests for each module plus one end-to-end REPL test reflect the
  new behavior.

**Acceptance Criteria**
- `2+2` prints `4` (not `4.0`).
- `1.5+2.5` prints `4`.
- `7/2` prints `3.5`.
- `1.5*2` prints `3`.
- `1/0` throws a runtime error; the REPL catches it, prints a readable message,
  and keeps running.
- Output never contains trailing zeros after the decimal point.
- Existing tests stay green, except those that explicitly check the old
  integer division behavior — those are updated to the new behavior.

**Non-Goals**
- No scientific notation (`1e5`, `2.5e3`).
- No separate integer type in the AST or evaluator.
- No configurable number of decimal places.
- No thousands separator in input or output.
- No new operators (e.g. `%`, `^`).

## Refined Plan

### Files to change
- `src/lexer.ts` — the number-reading branch accepts an optional `.` followed by
  more digits; the NUMBER token carries a floating-point value.
- `src/parser.ts` — the number constant carries a floating-point value (no new
  node kind needed).
- `src/evaluator.ts` — arithmetic already returns `number`; confirm divide-by-zero
  still throws.
- `src/main.ts` — format the result: strip trailing zeros, no decimal point for
  whole results.
- `tests/lexer.test.ts` — add a case tokenizing `1.5`.
- `tests/evaluator.test.ts` — add `1.5+2.5 → 4`, `7/2 → 3.5`, `1.5*2 → 3`.

### Test sketch
- lexer "tokenizes a decimal" — input `"1.5"` → one NUMBER token with value `1.5`.
- evaluator "adds decimals" — input `"1.5+2.5"` → `4`.
- evaluator "division yields decimal" — input `"7/2"` → `3.5`.
- evaluator "regression: integers still work" — input `"1+2*3"` → `7`.
