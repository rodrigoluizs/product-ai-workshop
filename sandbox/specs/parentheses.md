# Parentheses support in the calculator

> **This is a starter spec** — only the idea is written down. In the spec-first
> exercise you will use the **planner** and **refine** skills to fill in the
> `## High-Level Plan` and `## Refined Plan` sections, the same way the
> decimal-numbers example was filled in.

Status: todo
Type: feature

The calculator currently only supports flat expressions with `+ - * /` and a
fixed, built-in order of operations. Users cannot control the evaluation order
themselves. We want to add round parentheses `(` and `)` for grouping, so that
arbitrarily nested sub-expressions are evaluated before the surrounding
expression. Behavior without parentheses stays unchanged.

**Notes:**
- Preferred approach: smallest possible change — accept `(` and `)` as new input
  symbols and add a "grouped sub-expression" option at the innermost level.
- The existing precedence and associativity rules stay untouched.
- Unary minus, functions, and other bracket shapes are explicitly out of scope
  for this spec.

<!-- The planner skill will append "## High-Level Plan" below this line. -->
<!-- The refine skill will then append "## Refined Plan". -->
