# Working with Context

This is the day-to-day operating guide for contributors.

The repository is not a second project-management system. It is the durable context layer around the work.

---

# The basic rhythm

## Before work

Read:

1. the project `README.md`
2. the project `now.md`
3. deeper context only if it is relevant

## During work

Keep primary artifacts in their natural systems:

- design → Figma
- implementation → code repository
- delivery tracking → Jira
- enterprise documents → SharePoint / OneDrive
- quick conversation → Teams

Use `uxai-context` to capture what those systems often lose:

- why
- what changed
- what we learned
- what we decided
- what is still unknown
- where the source artifact lives

## After meaningful work

Ask:

> Did we learn, decide, or change something another person should be able to find later?

If yes, make the smallest useful update.

---

# Five common contribution types

## 1. Current state

Update `now.md` when the project itself has materially changed.

Good examples:

- current focus changed
- a major blocker appeared or cleared
- a meaningful learning changed direction
- a decision is now pending
- next steps changed

Do not turn `now.md` into a timeline. It is a current snapshot.

## 2. Decision

Create a decision record when someone may later ask:

> Why did we do this?

A decision record should preserve enough context to reconstruct the choice without replaying every conversation.

## 3. Research

Capture findings and implications, not an entire research archive.

Link back to the authoritative study, recording, synthesis, or repository.

## 4. Meeting outcome

Not every meeting needs notes.

Capture a meeting when it creates durable:

- decisions
- useful context
- open questions
- actions

## 5. Prototype / work thread

Capture why something was explored, where it lives, what was learned, and what happens next.

---

# The source rule

When information already has an authoritative home, keep it there.

Examples:

- do not export a Figma file into this repo
- do not copy an entire SharePoint document into Markdown
- do not recreate Jira here
- do not paste long Teams transcripts

Instead:

1. link the source
2. summarize the durable context
3. capture decisions or learning

This keeps the repository useful without creating another stale copy of enterprise information.

---

# Naming files

Use simple, readable names.

Recommended:

`YYYY-MM-DD-short-description.md`

Examples:

- `2026-09-27-navigation-decision.md`
- `2026-09-27-research-synthesis.md`
- `2026-09-27-prototype-review.md`

The date helps history sort naturally. The description helps humans and agents understand the file before opening it.

---

# Keep records small

Prefer a useful one-page record over a comprehensive report.

A good record lets someone answer:

- What happened?
- Why does it matter?
- What evidence exists?
- What changed?
- Where can I learn more?

If a section adds no value, remove it.

---

# Review and trust

Anyone can use AI to help draft or summarize context.

Before committing AI-assisted material:

- confirm the facts
- check links
- distinguish evidence from interpretation
- do not turn a proposal into a decision
- do not turn a generated summary into authoritative project history without review

The Git history gives us traceability. Human judgment gives us trust.

---

# A lightweight weekly habit

The team does not need a documentation meeting.

Once a week, a project owner or rotating contributor can ask Copilot:

> Review the changes in this project from the past week. Suggest only the updates needed to keep now.md current and identify any decisions or learnings that should be captured durably.

Review the suggestions and commit only what is useful.

This keeps the context layer healthy without creating a new reporting process.
