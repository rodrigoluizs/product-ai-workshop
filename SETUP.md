# Setup — do this before the workshop

Plan ~20 minutes. None of this requires writing code. There's a setup helping
hand in the first 15 minutes of the workshop, but the more you finish here, the
more time we spend learning.

You'll install three things and open one folder:

1. Claude Desktop (with the **Code feature**)
2. Git
3. This repository on your computer — opened in the Code feature

---

## 1. Install Claude Desktop + enable the Code feature

- Download from **https://claude.ai/download** (macOS or Windows) and sign in.
- Make sure you can access the **Code** feature (Claude Code inside the Desktop
  app — it opens a project folder and a terminal). If you don't see it, update to
  the latest version.
- The Code feature requires a paid plan (Pro/Max/Team/Enterprise). If you're on a
  free plan, tell the facilitator — we'll pair you up.

> We use the **Code feature**, not the regular chat. The Code feature opens a real
> project folder and automatically loads its `CLAUDE.md`, skills, and rules —
> which is the whole point of the workshop.

## 2. Install Git

Git tracks versions of files. You'll barely type Git yourself — Claude does most
of it — but it must be installed.

- **macOS:** open **Terminal** and run `git --version`. If missing, macOS offers
  to install developer tools — accept.
- **Windows:** install from **https://git-scm.com/download/win** (default options).

Verify:

```bash
git --version
```

## 3. Sign in to GitHub

- Go to **https://github.com** and sign in (or create a free account). It's where
  this workshop lives online.

## 4. Get this repository and open it in the Code feature

"Cloning" = downloading a copy you can work with.

```bash
# pick a folder you'll remember (e.g. your Documents folder), then:
git clone https://github.com/rodrigoluizs/product-ai-workshop.git
```

Then, in Claude Desktop's **Code feature**, **open the `product-ai-workshop`
folder**.

Test it: in that session, ask —

> "List the files in this folder and read sandbox/CLAUDE.md."

If Claude lists the files and summarizes the calculator's context note, you're
ready. ✅

---

## How the workshop folders work

Each module lives in `exercises/<module>/` and usually has:

- **`exercise/`** — your work area. For most modules you'll **open this subfolder**
  in the Code feature so the `.claude/` files you create there load automatically.
- **`solution/`** — a reference to compare against.

The facilitator will tell you which folder to open for each module.

## Setup checklist

- [ ] Claude Desktop installed, signed in, **Code feature** available
- [ ] `git --version` shows a version
- [ ] Signed in to GitHub
- [ ] `product-ai-workshop` cloned
- [ ] Code feature can open the folder and read `sandbox/CLAUDE.md`

Bring the folder path and your laptop charger. See you there.
