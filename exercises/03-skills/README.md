# 03 · Skills

**Time:** 30 minutes · **Format:** hands-on

## The idea

A **Skill** is packaged, reusable know-how: a folder with a `SKILL.md` file that
tells Claude *when* to use it and *how* to do the task. In the Code feature,
skills in a folder's `.claude/skills/` are **loaded automatically** — Claude
reaches for one when your request matches its description. No upload, no command.

**CLAUDE.md vs. Skill:**
- **CLAUDE.md** = always-on context for a folder (Module 02). It's a *personality
  / facts* layer that's always present.
- **Skill** = a reusable *procedure* that stays dormant until a request matches
  its description, then activates.

## Anatomy of a SKILL.md

```markdown
---
name: pirate-speak
description: Use this skill whenever the user wants text rewritten in pirate dialect...
---

# Pirate Speak
(step-by-step instructions, rules, examples)
```

The **description** is the most important line — it's how Claude decides whether
the skill applies. Write it as triggers ("use when the user asks to…"), not as a
summary.

---

## Exercise A — Build a Skill (15 min)

Open the [`exercise/`](exercise/) folder in the Code feature. Create:

```
exercise/.claude/skills/pirate-speak/SKILL.md
```

Ask Claude to help, or write it yourself. At minimum:

```markdown
---
name: pirate-speak
description: Rephrase text in pirate language. Use when the user asks to "piraterize", "make it pirate", "talk like a pirate", or wants text converted to pirate dialect.
---

# Pirate Speak
Convert ordinary text into pirate dialect while preserving meaning. Keep code,
URLs, file paths, and identifiers untouched.
(add a few vocabulary swaps and one example)
```

**Start a new session** in the `exercise/` folder so the skill loads. Then test:

> "Make this pirate: Hello team, I will update the deployment."

It should rewrite in pirate dialect. Now ask something unrelated — the skill
should **not** activate. That on-demand behavior is the lesson: a skill is a tool
in the toolbox, not a permanent personality.

## Exercise B — Read a polished one (8 min)

Compare yours to [`solution/.claude/skills/pirate-speak/SKILL.md`](solution/.claude/skills/pirate-speak/SKILL.md).
Notice what makes it reliable: a description full of trigger phrases, explicit
rules (preserve code/URLs), worked examples, and a calibration section
("more pirate" / "lighter"). That structure is the template for any good skill.

## Exercise C — Sketch your own (7 min)

On paper, design a skill you'd use at work:

- **name:**
- **description (triggers):** "Use when the user asks to …"
- **3 rules it must follow:**
- **1 example (input → output):**

PM-friendly ideas: *"turn meeting notes into action items"*, *"draft a release
note from a ticket"*, *"rewrite this in our brand voice"*.

---

## Takeaways

- Skill = reusable procedure; the **description** decides when it fires.
- In the Code feature, `.claude/skills/` loads automatically — no upload.
- Good skills have: when-to-use, rules, examples, calibration.
