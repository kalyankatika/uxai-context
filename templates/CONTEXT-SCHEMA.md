# Context Record Schema

Durable context records use YAML front matter so people, automation, and agents can reason about maturity, ownership, and freshness consistently.

## Required fields

```yaml
---
status: proposal
owner: "@owner-or-team"
last-reviewed: 2026-09-28
---
```

### `status`

Use exactly one of:

- `idea` — an early thought or exploration that is not yet a proposed direction
- `proposal` — a direction under active consideration or validation
- `decision` — an agreed direction or durable conclusion
- `superseded` — retained for history but replaced by newer context

Do not use delivery-status values such as `active` or `done` here.

### `owner`

The person or team accountable for keeping the record understandable and current.

Prefer a GitHub handle or clearly named team when available.

### `last-reviewed`

ISO date: `YYYY-MM-DD`.

A record is considered stale when it has not been reviewed in **90 days**. The repository hygiene check flags stale or missing review dates.

## Scope

This schema applies to durable context records created from the templates in this folder, including decisions, research notes, meeting outcomes, work threads, prototype learnings, and promoted shared assets.

Navigation files such as `README.md`, living project snapshots such as `now.md`, and folder guides are not context records under this schema.

Project-level ownership and freshness may be tracked separately in `project.yaml`.

## Review behavior

Reviewing a file does not require rewriting it. If the content is still accurate, update only `last-reviewed`.

If the content is no longer current:

- update it if it is still the same record, or
- mark it `superseded` and link to the newer record

Do not rewrite history to make old records appear current.
