---
type: decision
project: example-project
status: decision
owner: example-owner
last-reviewed: 2026-09-28
date: 2026-09-27
topics:
  - discoverability
  - navigation
---

# Decision: Use relationships as the primary discovery model

> **Reference example only — not an actual project record.**

## Context

The team explored both category tags and visible relationships as ways to help people discover related work.

Early feedback suggested tags were useful for filtering, but did not explain *why* two items were related.

## Decision

Use explicit relationships as the primary discovery model. Keep tags as supporting metadata rather than the main navigation pattern.

## Why

Relationships better communicate how work connects across projects, people, research, and artifacts.

This also gives future search and AI experiences a clearer structure to reason over.

## Alternatives

- Category-only navigation
- Free-form tags
- Folder hierarchy

## Implications

- The next prototype should make relationships visible.
- Research should validate whether people understand the relationship labels.
- Metadata should support both relationships and lightweight tags.

## Related

- Figma: <link>
- GitHub: <link>
- Jira: <link>
- Research: <link>
- Other: <link>
