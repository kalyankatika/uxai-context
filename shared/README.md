# Shared

`shared/` is for lightweight assets that have proven useful beyond one project.

Do **not** add something here because it might be reusable someday.

Start inside the project where the work happened. Promote only the part that has demonstrated value elsewhere.

## Promotion path

```text
one-off work
    ↓
useful again
    ↓
repeatable pattern
    ↓
shared asset
```

A shared asset might eventually be:

- a reusable pattern
- a skill or workflow
- a small agent recipe
- a prompt with clear repeat value
- a starter or reference implementation
- an internal tool reference
- a concise link to an authoritative standard

The exact structure should emerge from real use. We intentionally do **not** pre-create category folders until there are enough genuine assets to justify them.

## Promotion criteria

Promote something into `shared/` only when **all** of these are true:

1. **Recurring value** — it solves a problem that is useful beyond the project where it originated.
2. **Proven in real work** — it has been used, tested, or reviewed in at least one real project; it is not only a speculative idea.
3. **Portable** — another team can understand and use it without reconstructing the original project.
4. **Bounded** — the reusable part can be separated from project-specific detail.
5. **Owned** — a person or team is named as the owner.
6. **Traceable** — it links back to the source project, evidence, implementation, or authoritative standard when relevant.
7. **Safe to share here** — it contains no secrets, credentials, customer data, personal data, or confidential employer content.

If those conditions are not met, keep the work with the originating project until they are.

### Example

A project-specific prototype review prompt used once should stay with that project.

If the workflow is then used successfully on another prototype, the reusable steps are generalized, an owner is named, the limits are documented, and the source projects are linked, the reusable workflow can be promoted to `shared/`.

Promote the **generalized workflow**, not the project notes, transcripts, or source artifacts.

## What belongs here

A good shared asset should:

- solve a recurring problem
- be understandable outside the project where it originated
- be small enough to reuse
- link back to authoritative sources or implementation when relevant
- explain when to use it and when not to
- have enough ownership/context to remain trustworthy

## What does not belong here

Avoid:

- dumping project-specific notes
- copying whole code repositories
- collecting prompts with no demonstrated reuse
- duplicating standards owned elsewhere
- creating taxonomy before there is content

> **Capture the reusable part, not everything.**

The goal is compounding leverage: one team's useful work should make the next team's starting point better.
