# Setup — before the workshop

None of this requires writing code. The main things you do are sign in to Claude
Desktop and open the repo; the rest is having a couple of tools available on your
machine ahead of time.

There's a setup helping hand in the first 15 minutes of the workshop, but the
more is ready beforehand, the more time we spend learning.

---

## 0. Tools your machine needs (ahead of time)

The hands-on parts assume these are installed:

- **Git** — version control (Claude does most of the Git work for you, but it must
  be present).
- **GitHub CLI (`gh`)** — used for the GitHub exercises (branches, commits, pull
  requests). You'll also sign it in to your account (`gh auth login`).
- **Python 3** — runs the small sample program in the spec-first module.

If your machine is locked down and you can't install software yourself, ask your
IT/admin team to pre-install Git, the GitHub CLI, and Python 3 before the
workshop. You can verify they're present in step 3.

## 1. Claude Desktop + the Code feature

- Open Claude Desktop, sign in, and confirm you can start a **Code** session
  (Claude Code inside the Desktop app — it opens a project folder and a terminal).

> We use the **Code feature**, not the regular chat. The Code feature opens a real
> project folder and automatically loads its `CLAUDE.md`, skills, and rules —
> which is the whole point of the workshop.

## 2. GitHub account

You need a **GitHub account** for the branch / commit / pull-request exercises in
Module 01. Sign the GitHub CLI in to it:

```bash
gh auth login
```

(Follow the browser prompt — no SSH keys needed.)

> If you're attending as part of an organization, check whether you should use an
> **organization** account rather than a personal one — and avoid putting any
> work/confidential material in a personal account.

## 3. Get the repo and open it in the Code feature

The workshop repo is public. Get a copy onto your machine (the facilitator will
confirm the exact method for your setup — terminal clone, or download as a ZIP
from GitHub if the terminal is locked down):

```bash
git clone https://github.com/rodrigoluizs/product-ai-workshop.git
```

Then, in Claude Desktop's **Code feature**, **open the `product-ai-workshop`
folder** and verify everything is in place by asking:

> "List the files in this folder, run `git --version`, `gh --version`,
> `gh auth status`, and `python3 --version`, and read sandbox/CLAUDE.md."

If Claude lists the files, shows the tool versions, confirms `gh` is signed in,
and summarizes the calculator's context note, you're ready. ✅ (If any tool is
missing, get it installed before the day.)

## 4. Install the Superpowers plugin (for Module 06)

Superpowers is a free, open-source set of Claude skills we use for the spec-first
module. It's a **Claude plugin** (not machine software), added inside Claude
Desktop:

1. **Customize → Personal Plugins** (the **+** icon) **→ Personal → +** (add) **→
   Add marketplace**.
2. Paste this URL and click **Sync**:
   ```
   https://github.com/obra/superpowers.git
   ```
3. The **`superpowers-dev`** marketplace now appears under **Customize → Personal
   Plugins → Code** tab. Install the **superpowers** plugin from there.
4. Start a new session so it loads. Test by asking: *"What superpowers skills do
   you have?"* — you should see `brainstorming`, `writing-plans`, and others.

If you can't find it, don't worry — we'll install it together in the room.

---

## How the workshop folders work

Each module lives in `exercises/<module>/` and usually has:

- **`exercise/`** — your work area. For most modules you'll **open this subfolder**
  in the Code feature so the `.claude/` files you create there load automatically.
- **`solution/`** — a reference to compare against.

The facilitator will tell you which folder to open for each module.

## Setup checklist

- [ ] Git, GitHub CLI (`gh`), and Python 3 available on the machine
- [ ] `gh auth login` done — `gh auth status` shows you signed in
- [ ] Claude Desktop signed in, **Code feature** available
- [ ] `product-ai-workshop` opened in the Code feature
- [ ] Verified: files listed, `git --version` + `python3 --version` work, `sandbox/CLAUDE.md` read
- [ ] Superpowers marketplace added and plugin installed (Personal Plugins)

Bring your laptop charger. See you there.
