# Setup — before the workshop

None of this requires writing code. Most of the installing is handled **by
IT-Ops ahead of time** (you can't install software yourself on a Bonial machine),
so the main things *you* do are sign in to Claude Desktop and open the repo.

There's a setup helping hand in the first 15 minutes of the workshop, but the
more is ready beforehand, the more time we spend learning.

---

## 0. IT-Ops prerequisites (request ~1 week ahead)

Bonial machines can't self-install software, so we ask **IT-Ops to pre-install**
the following on each participant's laptop before the workshop:

- **Git** — version control (Claude does most of the Git work for you, but it must
  be present).
- **Python 3** — runs the small sample program in the spec-first module.
- *(optional)* **GitHub CLI (`gh`)** — only if we decide to do pull requests from
  the machine; not required for the core exercises.

The facilitator coordinates this request. If your machine already has these, great
— you can verify in step 3.

## 1. Claude Desktop + the Code feature

- Everyone in P&D has access to Claude AI, and therefore the **Code feature**
  (Claude Code inside the Desktop app — it opens a project folder and a terminal).
- Open Claude Desktop, sign in, and confirm you can start a **Code** session.

> We use the **Code feature**, not the regular chat. The Code feature opens a real
> project folder and automatically loads its `CLAUDE.md`, skills, and rules —
> which is the whole point of the workshop.

## 2. GitHub account

> ⚠️ **To confirm with Steven/IT:** whether we use **company/organization** GitHub
> accounts (preferred) or personal ones. Personal accounts must **not** be used to
> host Bonial artifacts. Your facilitator will tell you which to use before the
> day — don't create a personal account just for this unless asked.

You do **not** need an account just to get the repo (it's public). An account only
matters if we do the optional pull-request step.

## 3. Get the repo and open it in the Code feature

The workshop repo is public. Get a copy onto your machine (the facilitator will
confirm the exact method for your setup — terminal clone, or download as a ZIP
from GitHub if the terminal is locked down):

```bash
git clone https://github.com/rodrigoluizs/product-ai-workshop.git
```

Then, in Claude Desktop's **Code feature**, **open the `product-ai-workshop`
folder** and verify everything is in place by asking:

> "List the files in this folder, run `git --version` and `python3 --version`, and
> read sandbox/CLAUDE.md."

If Claude lists the files, shows Git + Python versions, and summarizes the
calculator's context note, you're ready. ✅ (If Git or Python is missing, that's
an IT-Ops gap — flag it before the day.)

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

- [ ] (IT-Ops, ahead of time) Git + Python 3 installed on the machine
- [ ] Claude Desktop signed in, **Code feature** available
- [ ] GitHub account approach confirmed with facilitator (company vs personal)
- [ ] `product-ai-workshop` opened in the Code feature
- [ ] Verified: files listed, `git --version` + `python3 --version` work, `sandbox/CLAUDE.md` read
- [ ] Superpowers marketplace added and plugin installed (Personal Plugins)

Bring your laptop charger. See you there.
