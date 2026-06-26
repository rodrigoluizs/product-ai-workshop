# Setup — do this before the workshop

Plan ~20 minutes. None of this requires writing code. If you get stuck, that's
fine — there is a setup helping hand in the first 15 minutes of the workshop, but
the more you finish here, the more time we spend learning.

You'll install four things and connect them:

1. Claude Desktop
2. Git
3. A GitHub account
4. This repository on your computer, connected to Claude Desktop

---

## 1. Install Claude Desktop

- Download from **https://claude.ai/download** (macOS or Windows).
- Sign in with your account.
- Open **Settings** and confirm you can see **Connectors** and **Capabilities /
  Skills** — we'll use both.

> We are **not** using Claude Code (the developer command-line tool) in this
> workshop. Just the Claude Desktop app.

## 2. Install Git

Git is the tool that tracks versions of files. You will barely type Git commands
yourself — Claude will do most of it — but it must be installed.

- **macOS:** open the **Terminal** app and run `git --version`. If it's missing,
  macOS will offer to install the developer tools — accept it.
- **Windows:** download from **https://git-scm.com/download/win** and install
  with the default options.

Verify (in Terminal / Git Bash):

```bash
git --version
```

You should see a version number like `git version 2.x`.

## 3. Create / sign in to GitHub

- Go to **https://github.com** and sign in (or create a free account).
- GitHub is where code lives online. We'll clone this workshop from there.

## 4. Get this repository onto your computer

"Cloning" = downloading a copy you can work with.

```bash
# pick a folder you'll remember, e.g. your Documents folder, then:
git clone https://github.com/rodrigoluizs/product-ai-workshop.git
```

You now have a `product-ai-workshop` folder. Remember where it is.

## 5. Connect Claude Desktop to that folder (Filesystem connector)

This lets Claude **read and write the files** in the workshop folder.

- In Claude Desktop: **Settings → Connectors → Filesystem** (also called
  "local files" / "directories").
- Add the `product-ai-workshop` folder you just cloned.
- Test it: start a new chat and ask:
  *"List the files in the product-ai-workshop folder and read sandbox/CONTEXT.md."*
- If Claude can list the files and summarize the context note, you're done. ✅

## 6. (Optional but recommended) GitHub connector

This lets Claude do Git/GitHub actions for you (branches, commits, pull requests).

- **Settings → Connectors → GitHub**, then authorize your account.
- We use this in Module 01.

---

## Setup checklist

- [ ] Claude Desktop installed and signed in
- [ ] `git --version` shows a version
- [ ] Signed in to GitHub
- [ ] `product-ai-workshop` folder cloned
- [ ] Filesystem connector can read the folder
- [ ] (optional) GitHub connector authorized

Bring the folder path and your laptop charger. See you there.
