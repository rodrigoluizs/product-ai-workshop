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
| 3:00–3:45 | **06 Spec-first factory** | planner → refine on `sandbox/specs/parentheses.md`; you demo implement. | Time sink. Keep planner's Phase-2 questions moving. |
| 3:45–4:00 | **07 Hooks + wrap** | Demo the trace hook in `sandbox/`. Hand out the cheat sheet. Each person names one Monday action. | Don't oversell; end on commitment. |

## Timing cushions

- **01 Git** and **06 Factory** overrun most. If behind: in 01 make Exercise C a
  demo; in 06 skip refine (Exercise B) and just show the completed solution.
- **02 Context** should **never** be cut — highest-value block.
- **04/05** are "light" by design — keep them to 20 min each.

## The narrative thread (use it out loud)

The workshop builds one coherent story, not seven disconnected tricks:

1. **CLAUDE.md** (02) decides *where* initiative/ticket docs live and how they're
   named.
2. **Rules** (04) decide *what's inside* those `-initiative.md` / `-ticket.md` files.
3. **Skills** (03) package a repeatable procedure.
4. The **factory** (06) chains skills into planner → refine → implement via a
   durable spec artifact.
5. **Subagents** (05) keep exploration tidy; **Hooks** (07) make things happen
   automatically.

## Common pitfalls and fixes

- **A `.claude/` file isn't taking effect** → almost always: created mid-session.
  Start a new session in that folder.
- **Skill won't trigger** → description too vague. Show how trigger phrases fix it.
- **Planner picks the approach itself** → it shouldn't; point at the skill rule and
  re-ask. Good teaching moment about skill discipline.
- **Rule applies to the wrong files** → check the glob; `**/*-ticket.md` matches
  nested `initiatives/<slug>/tickets/` too (that's intended).
- **Git auth prompts** → let Claude handle it in-session, or use the GitHub web UI;
  avoid SSH-key setup in the room.

## Materials checklist

- [ ] Projector + your Claude Desktop signed in, Code feature open
- [ ] Dry-run completed for every module
- [ ] Printed [CHEATSHEET.md](CHEATSHEET.md) per person
- [ ] Backup pre-cloned repo on USB / shared drive
