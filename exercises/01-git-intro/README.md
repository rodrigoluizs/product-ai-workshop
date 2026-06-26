# 01 · Git & GitHub

**Time:** 40 minutes · **Format:** hands-on

## Why a product person should care

When you work with an agent on real files, you're touching the same machinery
engineers use: **Git** (versioning) and **GitHub** (where it lives online).
You don't need to master it. You need enough to:

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
| **Push / Pull** | Send your commits up to GitHub / get the latest down. |

The golden rule: **work on a branch, open a PR, let someone review.** You never
edit `main` directly.

---

## Exercise A — Read the history (5 min)

In a Terminal (macOS) or Git Bash (Windows), go into the workshop folder and run:

```bash
cd product-ai-workshop
git log --oneline -10      # the last 10 commits
git status                 # what's changed right now (should be clean)
```

You just read the project's history. Each line in `git log` is one commit.

## Exercise B — Make a safe change on a branch (15 min)

We'll add your name to a shared file, on your own branch, the proper way.

```bash
git switch -c rodrigo/add-my-name      # create + switch to your own branch
```

Now open `exercises/01-git-intro/attendees.md` in any text editor and add a line
with your name. Save it. Then:

```bash
git add exercises/01-git-intro/attendees.md
git commit -m "docs: add <your name> to attendees"
```

You made a commit on your branch. `main` is untouched. Check it:

```bash
git log --oneline -3
git switch main && git log --oneline -3   # your commit is NOT here
git switch rodrigo/add-my-name            # back to your branch
```

> Tip: `git switch -c <name>` makes a branch; `git switch <name>` moves between
> existing ones. Use a name like `rodrigo/...` so it's obviously yours.

## Exercise C — Let *Claude* do the Git (10 min)

This is the real point: you usually won't type the commands above. With the
**GitHub connector** enabled (see SETUP.md), try this in Claude Desktop:

> "On the product-ai-workshop repo, create a branch called
> `claude/hello-from-me`, add a file `hello.md` that says hello from <your name>,
> commit it, and open a pull request to main. Show me the PR link before merging."

Watch what Claude does, then open the PR link. Notice it did exactly what you did
by hand in Exercise B — branch, commit, PR — but you described it in English.

## Exercise D — Review a Pull Request (5 min)

On GitHub.com, open the PR Claude created. Look at the **Files changed** tab —
green lines are additions. Add a comment. **Do not merge** (we'll discuss first).

This is the skill you'll actually use most: reading and commenting on changes.

---

## Debrief questions

- What's the difference between a commit and a pull request?
- Why work on a branch instead of editing `main`?
- When would you let Claude do the Git, and when would you do it yourself?

## If something breaks

You almost certainly didn't break anything. To throw away local changes and get
back to a clean `main`:

```bash
git switch main
git restore .          # discard uncommitted edits
```

Your branches and commits are still there until you delete them.
