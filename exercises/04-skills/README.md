# 04 · Skills

**Time:** 20 minutes · **Format:** hands-on

You already know roughly what Skills are, so this is short and practical.

## The idea

A **Skill** is packaged, reusable know-how: a folder with a `SKILL.md` file that
tells Claude *when* to use it and *how* to do the task. Once installed, Claude
reaches for it automatically when your request matches — no need to re-explain the
procedure each time.

**Project vs. Skill:**
- A **Project** = persistent context for *a workspace* (Module 03).
- A **Skill** = a reusable *procedure* that travels with you and triggers *on
  demand* when the task matches its description.

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

## Exercise A — Install and trigger a Skill (8 min)

1. In Claude Desktop: **Settings → Capabilities / Skills → add a skill.**
2. Add the `pirate-speak` skill from
   [`solution/pirate-speak/`](solution/pirate-speak/SKILL.md).
3. In a normal chat, type: *"Piraterize this: Hello team, the deploy is delayed."*
4. Claude should rewrite it in pirate dialect **without** you explaining how —
   the skill's description matched your request.

Notice you never said "use the skill." Good descriptions make skills trigger
themselves.

## Exercise B — Read how it's built (7 min)

Open [`solution/pirate-speak/SKILL.md`](solution/pirate-speak/SKILL.md) and notice
what makes it reliable:

- a **description** full of trigger phrases,
- explicit **rules** (preserve meaning, never pirate code/URLs),
- worked **examples**,
- a **calibration** section ("more pirate" / "lighter").

That structure — when to use, rules, examples, calibration — is the template for
any good skill, serious or silly.

## Exercise C — Sketch your own (5 min)

On paper, design a skill you'd use at work. Just fill in:

- **name:**
- **description (triggers):** "Use when the user asks to …"
- **3 rules it must follow:**
- **1 example (input → output):**

Examples product people often want: *"turn meeting notes into action items",*
*"draft a release note from a ticket",* *"rewrite this in our brand voice".*
We'll build one properly in the next module's style.

---

## Takeaways

- Skill = reusable procedure; the **description** decides when it fires.
- Good skills have: when-to-use, rules, examples, calibration.
- Skills work in Claude Desktop — no developer tooling required.
