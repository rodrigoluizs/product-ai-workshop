---
name: refine
description: Use after a spec already has a "## High-Level Plan" and the user wants to turn it into a concrete, file-level plan before implementation. Trigger on "refine this spec", "make the plan concrete", "what files would change", or when the user points at a spec that has a High-Level Plan but no Refined Plan yet.
---

# Refine

You turn a high-level plan into a concrete, file-level plan. You still do not
write product code — you produce the plan that an implementer (or a facilitator
demo) would follow.

## The artifact contract

You work on the same spec file the planner used. You **read** the existing
`## High-Level Plan` section and **append** exactly one new section with this
exact heading:

```
## Refined Plan
```

Append only — never rewrite the file or touch the High-Level Plan. If the spec
has no `## High-Level Plan`, stop and tell the user to run the planner first.

## Workflow

1. **Read** the spec's `## High-Level Plan` and the project context
   (`sandbox/CONTEXT.md`) plus the actual source files the plan implies.
2. **Map each step to real files.** For every change, name the real file and what
   changes in it. Verify the files exist by reading them — do not guess paths.
3. **Sketch the tests** that would prove each acceptance criterion.
4. **Append** the `## Refined Plan` section.

## The Refined Plan section must contain

- **Files to change** — a list of real files, each with a one-line reason.
- **New signatures** (if any) — new functions/types, or explicitly "none".
- **Test sketch** — for each acceptance criterion, the input → expected result.

## Rules
- Never write product code.
- Every file path must reference a real file you actually read.
- Append under the exact heading `## Refined Plan`; leave everything above intact.
- If acceptance criteria are vague, ask before inventing them.
