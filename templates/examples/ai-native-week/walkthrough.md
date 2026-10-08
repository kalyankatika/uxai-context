# Fictional Monday–Friday walkthrough

> **ALL EVENTS, PRs AND EVIDENCE HERE ARE INVENTED.** This is a demonstration of the workflow, not Periscope project history.

## Monday — Orient, choose focus

The team reads `now.md` and agrees that navigation coherence and portfolio data are useful next areas. Two work records are opened because both span multiple sessions. Each gets a driver and a next move.

Earlier `now.md` excerpt (illustration only, **not** a second file):

```markdown
## Current focus
### Navigation
Driver: Contributor B
Next: Trace the portfolio → initiative → portfolio journey.
Context: work/platform-navigation.md

### Portfolio data
Driver: Contributor A
Next: Check a minimal model with representative portfolio examples.
Context: work/portfolio-data.md
```

Contributor C joins interaction evaluation. Contributor D prepares representative portfolio examples. Expertise does not create exclusive lanes.

## Tuesday — Build instead of administering

- A uses an agent to inspect routes and builds the change (Demo PR 101).
- B revises labels and implements with an agent (Demo PR 102).
- D contributes working sample portfolio fixtures (Demo PR 104).

No separate design/engineering/PM ticket queues are needed; PRs hold their own review status.

## Wednesday — Integrate and verify

- B and D integrate a clearer return path (Demo PR 103).
- A builds the first save/reload flow (Demo PR 105).
- C helps author automated checks with an agent (Demo PR 106).

Update the work records with links, evidence and revised next moves; `now.md` needn't change if priorities don't.

## Thursday — Evidence changes the work

A fictional task walkthrough by C finds only **2/4** people can complete the navigation journey unaided. Labels and the empty state are confusing. C helps implement a correction (Demo PR 107). B opens a keyboard-focus follow-up (Demo PR 108) that remains in review.

## Friday — Resolve what is proven; keep other work open

A fictional four-person recheck finds **4/4** can complete the revised core journey. The group accepts navigation for its defined scope and records evidence and the unresolved focus follow-up. Persistence happy-path checks pass; validation/recovery are not proven, so the data work stays active.

An agent drafts [activity.md](activity.md) from source evidence, and a person verifies it. `now.md` is edited **in place** to reflect the new focus. Friday is **not** a sprint boundary.

## File behavior

| File | Behavior |
| --- | --- |
| `now.md` | Edit in place when focus changes; Git is history. |
| `work/platform-navigation.md` | Evolve during work; resolve with evidence and explicit follow-up. |
| `work/portfolio-data.md` | Continue next week; don't artificially close it. |
| `activity.md` | Append a weekly, source-supported summary. |

**Done** means an accepted result with appropriate evidence, not merely merged PRs or an elapsed reporting period.