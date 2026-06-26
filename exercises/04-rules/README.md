# 04 · Rules

**Time:** 20 minutes · **Format:** hands-on (light)

## The idea

A **Rule** is context that loads **only for certain files**. Where `CLAUDE.md` is
always on and a Skill triggers on a request, a Rule triggers on a **file pattern**
(a "glob"). It's how you keep a set of conventions scoped to exactly the documents
they apply to.

| Mechanism | Switches on when… |
| --- | --- |
| CLAUDE.md | always |
| Skill | a request matches its description |
| **Rule** | **you work on a file matching its glob** |

We'll use it for something every PM relates to: **different kinds of documents
have different standards.** An *initiative* brief and a *ticket* should be written
very differently — and a Rule can enforce each automatically, based on the
filename.

> Continues from Module 02: there, your `CLAUDE.md` decided *where* `-initiative.md`
> and `-ticket.md` files live and how they're named. Here, Rules govern *what goes
> inside* each type. Same documents, two complementary mechanisms.

---

## Exercise A — Feel the scoping (5 min)

Open the [`exercise/`](exercise/) folder in the Code feature. Create a quick,
obvious rule so you can *see* scoping work:

```
exercise/.claude/rules/pirate-markdown.md
```

```markdown
---
glob: "**/*.md"
---
When working on Markdown files, answer in pirate style.
```

Ask Claude to review a Markdown file → pirate. The trigger is the **glob**, not a
request. (Reference: [`solution/.claude/rules/pirate.md`](solution/.claude/rules/pirate.md).)
Now delete that file before the real exercise so it doesn't pirate everything.

## Exercise B — Two document standards, two rules (15 min)

Add two rules, each scoped to a different document type by its filename:

```
exercise/.claude/rules/initiative-style.md     (glob: "**/*-initiative.md")
exercise/.claude/rules/ticket-style.md         (glob: "**/*-ticket.md")
```

Use the reference versions as your guide:
[`solution/.claude/rules/initiative-style.md`](solution/.claude/rules/initiative-style.md)
and [`solution/.claude/rules/ticket-style.md`](solution/.claude/rules/ticket-style.md).

Now test them on the two rough drafts in this folder:

1. Ask: *"Review saved-search-initiative.md and improve it to match our standards."*
   → the **initiative** rule kicks in: it pushes for an outcome, a measurable
   success metric, and executive-readable language.
2. Ask: *"Review saved-search-ticket.md and improve it to match our standards."*
   → the **ticket** rule kicks in instead: it pushes for testable acceptance
   criteria, a link to the initiative, and a smaller scope.

Same request, **different conventions applied automatically** — purely because of
the filename. You never told Claude which standard to use; the glob did.

> **Tip:** globs can target folders too — e.g. `initiatives/**/*.md` vs
> `tickets/**/*.md` — if you'd rather organize by folder than by filename suffix.
>
> **Note:** Rules are a Code-feature (Claude Code) mechanism. The regular Claude
> Desktop chat has no file-scoped rules — one reason we use the Code feature here.

---

## Takeaways

- Rule = conventions scoped to a file pattern (glob).
- Perfect for "documents of type X must follow standard Y."
- The right standard applies itself based on the file — no reminding needed.
