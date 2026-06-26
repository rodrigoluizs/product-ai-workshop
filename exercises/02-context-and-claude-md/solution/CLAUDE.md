# Product workspace conventions

This workspace holds product-planning documents. Follow these filing conventions
**automatically** — create files in the right place, with the right name, without
asking where they go.

## Initiatives

- One folder per initiative under `initiatives/`, named with a short kebab-case
  slug.
- The brief lives at `initiatives/<slug>/<slug>-initiative.md`.
- Example: an initiative "Saved Search" →
  `initiatives/saved-search/saved-search-initiative.md`.

## Tickets

- Tickets for an initiative live under `initiatives/<slug>/tickets/`.
- Name each ticket `NN-<short-slug>-ticket.md`, where `NN` is a zero-padded order
  number (`01`, `02`, …).
- Example: `initiatives/saved-search/tickets/01-save-button-ticket.md`.
- Continue numbering from the highest existing `NN` in that folder.

## General

- Slugs are lowercase with words separated by hyphens.
- Filenames always end in `-initiative.md` or `-ticket.md` (so document-style
  Rules can recognize them — see Module 04).
- Don't ask where to put a document or what to call it; apply these conventions
  and tell the user the path you used.
