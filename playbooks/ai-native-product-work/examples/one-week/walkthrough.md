# Fictional Monday–Friday walkthrough

> **ALL EVENTS, PRs, AGENT SESSIONS AND EVIDENCE HERE ARE INVENTED.** This is a teaching scenario, not Periscope project history.

The example uses four unnamed human contributors (A: engineering/AI emphasis, B: design, C: research, D: product/program), plus a bounded **agent execution driver** for portfolio data. The distinction is important: people and agents alike can move work, but agent autonomy is scoped and consequential decisions have a human steward.

## Monday — Orient, choose focus

The team reads `now.md` and agrees that navigation coherence and portfolio data reliability are useful current priorities. Two work records are opened because these efforts span sessions. Contributor B drives navigation. **Agent-01 drives portfolio data execution**, with Contributor A as the human steward who approves the scope and acceptance checks.

Earlier `now.md` excerpt (illustrative, **not a second file**):

```markdown
## Current focus

### Navigation
Driver: Contributor B
Next: Trace the portfolio → initiative → portfolio journey.
Context: work/platform-navigation.md

### Portfolio data
Driver: Agent-01 (approved bounded task)
Human steward: Contributor A
Next: Inspect persistence model, plan the smallest checked change.
Context: work/portfolio-data.md
```

Contributor C supports evaluation and automated checks. Contributor D prepares representative product examples. No person gets a separate functional queue.

## Tuesday — Humans and agents drive work

- A person driving navigation asks an agent for route analysis, then guides a change (fictional Demo PR 101).
- B revises labels and implements with an agent (Demo PR 102).
- **Agent-01**, driving a separate approved workstream, inspects the data model, plans fixtures and implements them (Demo PR 104), without needing new human instructions for every micro-step.

The human steward is available for escalation but is not a ticket administrator. The agent retains durable evidence in the work record and implementation artifacts in GitHub.

## Wednesday — Integrate and verify

- B and D improve the return path (Demo PR 103).
- **Agent-01** implements the save/reload path (Demo PR 105) and adds happy-path tests (Demo PR 106).
- Contributor C helps challenge the test coverage and drafts additional checks.

Work records link to evidence and keep the next move visible. `now.md` needn't be touched if priorities remain unchanged.

## Thursday — Evidence changes the work

A **fictional** small task walkthrough by C finds only **2 of 4** participants complete the navigation journey unaided. Labels and empty states cause confusion.

C helps implement a correction (Demo PR 107). B opens a keyboard-focus follow-up (Demo PR 108), which remains in review. The navigation driver incorporates evidence into the work record.

Agent-01 identifies an **unresolved product decision**: reject incomplete data or save with a warning. It **proposes alternatives and escalates**, rather than deciding product policy autonomously.

## Friday — Resolve what is proven, continue what isn't

A **fictional** recheck finds **4 of 4** can complete the revised navigation journey. Navigation resolves for the defined scope; keyboard focus remains a follow-up.

Agent-01 has successfully driven its **bounded happy-path execution** through reviewed PRs, but validation/recovery are still unproven. The human steward does not accept the broader data foundation outcome as complete. That work remains active in the *same* record for the following week.

An agent can also drive synthesis: draft [activity.md](activity.md) from sources, show opened/merged counts and evidence, and propose current-state edits. A person checks the claims. `now.md` is updated **in place** only where current focus changed.

## The files did not become a board

| File | Behavior |
| --- | --- |
| `now.md` | One current view, edited when focus changes; Git stores previous versions |
| `work/platform-navigation.md` | Human-driven; scope resolved with evidence and follow-up |
| `work/portfolio-data.md` | Agent-driven execution with human steward; stays active until evidence supports resolution |
| `activity.md` | Historical, source-linked synthesis of change, not sprint closure |

**Done** is an appropriately evidenced, accepted result, not a merged PR, an agent saying “done,” or an elapsed week. See [the guided tutorial](README.md) for how to apply this to a real project.
