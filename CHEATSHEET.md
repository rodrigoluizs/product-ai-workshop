# Cheat Sheet — Product AI Workshop

Keep this. It's the whole workshop on one page.

## The five parts of a good ask

1. **Role / goal** — who you are, what you want.
2. **Context** — what Claude can't guess (audience, product, constraints).
3. **Task** — the specific thing to produce.
4. **Format** — length, structure, tone.
5. **Guardrails** — what to avoid / out of scope.

> Bad output? Suspect a missing part above before blaming the model.

## Which tool for the job

| Need | Use |
| --- | --- |
| Context for one question | Just type it (or attach a file) |
| Same context/norms across many chats | A **Project** |
| A repeatable procedure that triggers itself | A **Skill** |
| Plan a change before building | The **spec-first** flow (planner → refine) |
| Let Claude do Git for you | The **GitHub connector** |

## Git in plain English

| Term | Meaning |
| --- | --- |
| Repo | A tracked project folder |
| Commit | A labeled snapshot of changes |
| Branch | A safe parallel copy to experiment in |
| Pull Request | "Please review and merge my branch" |

**Golden rule:** work on a branch → open a PR → get a review. Never edit `main`.

Useful commands:
```bash
git status                 # what changed
git switch -c my-branch    # new branch
git add . && git commit -m "message"
git switch main            # back to main
git restore .              # discard uncommitted changes (undo)
```

Or just ask Claude (GitHub connector on):
> "Create a branch, make this change, commit it, and open a PR. Show me the link."

## Spec-first flow

```
idea → planner → ## High-Level Plan → refine → ## Refined Plan → implement
```
The hand-off is the **exact heading**. The plan is a document you review — not a
disposable chat.

## Skills: what makes one good

- A **description** written as triggers ("use when the user asks to…").
- Explicit **rules**.
- Worked **examples**.
- A **calibration** note ("more X" / "lighter").

## One thing to do Monday

Pick one: write a reusable Project for your area · turn a recurring task into a
Skill · plan your next feature as a spec before building it.
