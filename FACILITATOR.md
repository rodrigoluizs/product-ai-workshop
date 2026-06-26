# Facilitator Guide

Timed run-of-show for the 4-hour Product AI Workshop. Audience: non-technical
product people, mixed experience, all using the Claude Desktop **Code feature**.

## Before the day

- Send [SETUP.md](SETUP.md) **at least 3 days early.** Setup-in-the-room kills the
  first hour. Offer a 20-min drop-in the day before.
- Confirm everyone can access the **Code feature** (paid plan). Pair up anyone who
  can't.
- Have a backup pre-cloned folder on a USB stick / shared drive.
- Do a full dry run yourself: open each `exercise/` folder, create the `.claude/`
  files, and confirm they load on a **new session** (auto-load happens at session
  start — restarting matters).

## Guiding principles

- **They direct, they don't code.** Repeat this. Their job is judgment and
  context, not syntax.
- **Show, then let them do.** Each module: one demo on screen, then they try.
- **Auto-load is at session start.** The #1 confusion: creating a `.claude/` file
  mid-session and expecting it to work. Drill "new session to load it."
- **Normalize "I broke it."** They almost never can. Show the recovery ask early.

## Run-of-show

| Time | Module | Your job | Watch for |
| --- | --- | --- | --- |
| 0:00–0:15 | **Framing** | "You direct." One live demo: vague vs context-rich prompt. | Don't lecture; get to the demo fast. |
| 0:15–0:50 | **01 Git** | Mental-model table, then Exercises A–D (Claude does the Git). | Terminal panic. Have the recovery ask ready. |
| 0:50–1:00 | Break | | |
| 1:00–1:40 | **02 Context + CLAUDE.md** | Release-notes before/after, pirate proof, then the **filing-convention CLAUDE.md** (initiatives/tickets). | The heart — give it air. The "it filed itself" moment is the payoff. Reinforce new-session-to-load. |
| 1:40–2:10 | **03 Skills** | Build pirate-speak in `.claude/skills/`, new session, trigger it. | "It triggered itself" is the lesson. |
| 2:10–2:20 | Break | | |
| 2:20–2:40 | **04 Rules** | Quick pirate-markdown scope demo, then the two doc-style rules on the rough drafts. | Connect back to Module 02 filenames. Keep it light. |
| 2:40–3:00 | **05 Subagents** | Drop codebase-explorer into `sandbox/`, run it, read its guardrails. | Frame as "delegate, get a summary, not a transcript." |
| 3:00–3:50 | **06 Spec-first / Superpowers** | brainstorm → writing-plans on the parentheses feature in `sandbox/`; you demo execution. | Time sink. Keep brainstorming's one-at-a-time questions moving; let the gates land. |
| 3:50–4:00 | **Wrap** | Hand out the cheat sheet. Each person names one Monday action. | End on commitment, not features. |

## Timing cushions

- **01 Git** and **06 Superpowers** overrun most. If behind: in 01 make Exercise C
  a demo; in 06 stop after writing-plans (Exercise B) and just show the example
  plan + execution as a quick demo.
- **02 Context** should **never** be cut — highest-value block.
- **04/05** are "light" by design — keep them to 20 min each.
- Pre-install the Superpowers plugin yourself (Customize → Personal Plugins →
  Personal → Add marketplace → `https://github.com/obra/superpowers.git` → Sync →
  install from the Code tab). Have everyone who skipped setup install it during the
  Module 05 → 06 transition.

## The narrative thread (use it out loud)

The workshop builds one coherent story, not six disconnected tricks:

1. **CLAUDE.md** (02) decides *where* initiative/ticket docs live and how they're
   named.
2. **Rules** (04) decide *what's inside* those `-initiative.md` / `-ticket.md` files.
3. **Skills** (03) package a repeatable procedure.
4. **Subagents** (05) delegate a focused job and return a summary, not a transcript.
5. **Superpowers** (06) chains it all into brainstorm → plan → execute, with gates
   and a fresh subagent per task — the disciplined version of everything above.

## Common pitfalls and fixes

- **A `.claude/` file isn't taking effect** → almost always: created mid-session.
  Start a new session in that folder.
- **Skill won't trigger** → description too vague. Show how trigger phrases fix it.
- **Superpowers won't stop to let you approve** → it should gate before coding; if
  it races ahead, that's a great moment to point out the design-approval gate and
  ask it to wait. Reinforces that *you* hold the decision.
- **Rule applies to the wrong files** → check the glob; `**/*-ticket.md` matches
  nested `initiatives/<slug>/tickets/` too (that's intended).
- **Git auth prompts** → let Claude handle it in-session, or use the GitHub web UI;
  avoid SSH-key setup in the room.

## Materials checklist

- [ ] Projector + your Claude Desktop signed in, Code feature open
- [ ] Dry-run completed for every module
- [ ] Printed [CHEATSHEET.md](CHEATSHEET.md) per person
- [ ] Backup pre-cloned repo on USB / shared drive
