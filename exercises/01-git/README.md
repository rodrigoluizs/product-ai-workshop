# 01 · Git & GitHub

**Time:** 35 minutes · **Format:** hands-on

## Why a product person should care

The Code feature works on a real **repository** — the same machinery engineers
use: **Git** (versioning) and **GitHub** (where it lives online). You don't need
to master it. You need enough to:

- understand what Claude is doing when it "commits" or "opens a PR",
- review and comment on changes safely,
- never be afraid you'll "break" something (you almost can't — that's the point).

## The mental model (5 min)

| Term | Plain-English meaning |
| --- | --- |
| **Repository ("repo")** | A project folder whose every change is tracked. |
| **Commit** | A labeled snapshot — "here's what changed and why." |
| **Branch** | A safe parallel copy where you experiment without touching the main version. |
| **Pull Request (PR)** | A proposal: "please review my branch and merge it into main." |
| **Clone** | Download a copy of a repo to your computer. |
| **Push / Pull** | Send commits up to GitHub / get the latest down. |

The golden rule: **work on a branch, open a PR, let someone review.** Never edit
`main` directly.

---

## Exercise A — Read the history (5 min)

Open the `product-ai-workshop` folder in the Claude Desktop **Code feature**, then
ask Claude:

> "Show me the last 10 commits and the current status of this repo, and explain
> in plain English what each of the recent commits did."

Behind the scenes Claude runs `git log` and `git status`. You just read the
project's history without typing a Git command.

## Exercise B — Make a safe change on a branch (12 min)

Tell Claude:

> "Create a new branch called `rodrigo/add-my-name`. Add my name, '<your name>',
> as a new line in exercises/01-git/attendees.md. Then commit it with a clear
> message. Don't push yet — show me what you did."

Then verify your understanding:

> "Show me the difference between my branch and main, and confirm that main was
> not changed."

You just produced a commit on a branch — and `main` is untouched. That separation
is the whole safety model.

## Exercise C — Open a Pull Request (8 min)

> "Push my branch and open a pull request to main with a short description.
> Give me the link, but do not merge it."

Open the link Claude gives you on GitHub.com. Look at the **Files changed** tab —
green lines are additions. **Don't merge** (we'll discuss first).

## Exercise D — Do one by hand (5 min)

So the commands aren't a black box, do the smallest one yourself in the Code
feature's terminal:

```bash
git status
git log --oneline -3
```

That's it. You now know what Claude was doing for you.

---

## Debrief

- What's the difference between a commit and a pull request?
- Why work on a branch instead of editing `main`?
- When would you let Claude do the Git, and when would you check by hand?

## If something feels broken

You almost certainly didn't break anything. Ask Claude:

> "Discard all my uncommitted changes and switch me back to a clean main branch."

Your earlier branches and commits stay intact until you delete them.
