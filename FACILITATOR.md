# Facilitator Guide

A timed run-of-show for the 4-hour Product AI Workshop. Audience: non-technical
product people, mixed experience, all on **Claude Desktop**.

## Before the day

- Send [SETUP.md](SETUP.md) **at least 3 days early.** Setup-in-the-room kills the
  first hour. Offer a 20-min drop-in the day before.
- Have a backup plan for people who didn't finish setup: pair them up, and keep a
  pre-cloned folder on a USB stick / shared drive.
- Pre-install the four skills yourself and screenshot each step (Skills menu paths
  change).
- Test the **GitHub connector** flow on your own account the morning of.

## Guiding principles

- **They direct, they don't code.** Repeat this. Their job is judgment and
  context, not syntax.
- **Show, then let them do.** Every module: 1 demo on screen, then they try.
- **It's okay not to finish.** This is a menu, not a race (inherited from the
  original bootcamp's design).
- **Normalize "I broke it."** They almost never can. Show the recovery commands
  early so fear doesn't build.

## Run-of-show

| Time | Module | Your job | Watch for |
| --- | --- | --- | --- |
| 0:00–0:15 | **Framing** | Set the "you direct" frame. One live demo: a vague prompt vs. a context-rich one. | Don't lecture. Get to the demo fast. |
| 0:15–0:55 | **01 Git** | Demo the mental-model table, then Exercises A–D. | Terminal panic. Have the recovery block ready. The GitHub-connector exercise is the "wow". |
| 0:55–1:05 | Break | | |
| 1:05–1:50 | **02 Context Eng** | Run the release-notes before/after live. Then they rewrite their own. | This is the heart — give it air. Collect 2–3 before/afters to share. |
| 1:50–2:10 | **03 Projects** | Pirate test live, then a useful Project. | Make sure everyone creates *one* real Project. |
| 2:10–2:30 | **04 Skills** | Install pirate-speak, trigger it, read the SKILL.md. | The "it triggered itself" moment is the lesson. |
| 2:30–2:40 | Break | | |
| 2:40–3:25 | **05 Spec-first** | Install planner+refine. Run planner on parentheses live up to the approach choice, then they continue. | Time sink. Keep Phase-2 questions moving. Demo "implement" yourself. |
| 3:25–3:45 | **06 What's next** | Walk the ladder table. Keep it short and concrete. | Don't oversell Claude Code; frame it as "later". |
| 3:45–4:00 | **Wrap** | Hand out [CHEATSHEET.md](CHEATSHEET.md). Each person names one thing they'll use Monday. | End on commitment, not features. |

## Module timing cushions

- Git (01) and Spec-first (05) are the two that overrun. If behind: in 01 make
  Exercise C (GitHub connector) a demo instead of hands-on; in 05 skip Exercise B
  (refine) and just show the completed solution.
- Context Engineering (02) should **never** be cut — it's the highest-value hour.

## Common pitfalls and fixes

- **Filesystem connector can't see files** → wrong folder added, or permissions not
  granted. Re-add the exact cloned folder; restart Desktop.
- **Skill won't trigger** → description too vague. Show how trigger phrases in the
  description fix it.
- **Planner picks the approach itself** → it shouldn't; if it does, point out the
  skill rule and re-ask. Good teaching moment about skill discipline.
- **Git auth prompts** → push them toward the GitHub connector and the web UI;
  avoid SSH-key setup in the room.

## Materials checklist

- [ ] Projector + your Claude Desktop signed in
- [ ] All four skills pre-installed on your machine
- [ ] GitHub connector authorized
- [ ] Printed [CHEATSHEET.md](CHEATSHEET.md) per person
- [ ] Backup pre-cloned repo on USB / shared drive
