# AI-native working model
### Getting started with continuous, context-driven product work

> **Purpose:** Help people **and agents** originate, drive, execute, verify and learn from valuable work with minimal coordination overhead.

**This is our team convention**, not an official or standardized industry methodology. It synthesizes documented practices from Anthropic, OpenAI, GitHub and software-delivery research. It complements [Working with Context](WORKING-WITH-CONTEXT.md), which explains what to preserve; this document explains how the work moves.

**New?** Read the [five-minute setup](#5-minute-start), then the [guided fictional week](../templates/examples/ai-native-week/README.md). For GitHub basics see [Getting Started](GETTING-STARTED.md).

## The two loops

**The team operates continuously:**

```text
Orient → Focus → Drive & Execute → Verify → Capture → Repeat
```

**Any substantial piece of work develops through:**

```text
Intent → Shape → Plan → Make → Prove → Learn ↺
```

These are **loops, not phases or documents**. An agent may complete several steps in one session; humans and agents may move backward when evidence changes the problem. There are no mandatory sprints, approvals for each step, or six required files.

**Driving work is not reserved for a person.** An agent can propose a change, investigate it, drive a well-scoped task, create an implementation, run its own checks, request independent review, and bring back a proposed next move. A person can do exactly the same. For agent-driven work, a named **human steward** remains accountable for boundaries, consequential decisions and acceptance; the agent is the **execution driver**, not an unreviewed authority.

## 5-minute start

1. **Orient:** Open the project's `README.md` and single living `now.md`; read only related work context.
2. **Focus:** Choose an active item or propose a better one. Each substantial item names its **driver** (person or agent), **next move**, and **context link**. Agent-driven items also name a **human steward** and permissible scope.
3. **Move it forward:** People and agents investigate, design, build, test or research directly in the appropriate tools. Create one `work/<topic>.md` only if work benefits from continuity across sessions.
4. **Verify:** Use appropriate code checks, independent review, working demo or user evidence; state *which* kind of proof you have, and what's missing.
5. **Capture and repeat:** Link PRs and artifacts, record meaningful changes, refresh `now.md` when focus changes. Weekly activity synthesis records history, **not a weekly delivery deadline**.

### Fast answers

| Question | Answer |
| --- | --- |
| Where is the board? | One living `now.md`: Current focus, Next, decisions/help needed. |
| Where is the backlog? | A small curated **Next** list. No exhaustive queue or backlog grooming required. |
| Where do tasks live? | In execution: PRs, optional Issues, or a small checklist in a work record. |
| Where do decisions and research live? | Their established source systems; link and retain durable rationale when useful. |
| Where does progress history live? | Git/PR history and an optional agent-assisted weekly `activity.md`. |
| Who can drive? | A person **or** a scoped agent. A person stewards agent-owned outcomes. |
| When is it done? | Appropriate proof and an accepted result; never merely a PR count or Friday's date. |

## The minimum project surfaces

```text
projects/<project>/
├── README.md         # stable orientation (already exists)
├── now.md            # ONE living current view, edit in place
├── work/             # evolving context for substantial work only
└── activity.md       # OPTIONAL append-only activity snapshots
```

Keep existing `decisions/`, `research/`, `prototypes/`, `meetings/` where useful. The application repo keeps code, tests, agent instructions, Issues, PRs and deployment controls. **Do not duplicate authoritative artifacts.**

### 1. `now.md` — current focus, not a journal

Keep the headings that already exist in the project's file. Under **Current focus**, record only enough to act:

```markdown
### Portfolio data
Driver: Agent — scoped data-foundation task
Human steward: Contributor A
Next: Verify incomplete-record handling and propose a safe fix.
Context: [Data work](work/portfolio-data.md)

### Navigation refinement
Driver: Contributor B
Next: Evaluate the integrated flow.
Context: [Navigation work](work/platform-navigation.md)
```

Agent sessions or task links should be included if they exist. A specific agent's execution may end while the work item persists: transfer the driver or spawn a new **approved, bounded** agent session rather than assuming infinite autonomous continuity.

**Edit the same `now.md` as reality changes.** Git stores historical versions. When an item resolves, remove it from Current focus. Don't accumulate weekly status blocks or create `now-YYYY-MM-DD.md` files.

### 2. `work/<topic>.md` — context sufficient to resume

Use the [existing work-thread template](../templates/work-thread.md) when work spans sessions, needs collaboration, involves uncertainty, or should be understood later. Keep intent, thinking, useful plan/checklist, linked artifacts, proof, learning and resolution **in one evolving record**, unless complexity justifies separate deeper materials.

Example for agent-driven work:

```markdown
# Portfolio data foundation
Driver: Agent — bounded implementation task
Human steward: Contributor A
State: Active
Scope: Data persistence and local test cases; PR only, no deployment.

## Intent
Make representative portfolio data reliable after reload.

## Current thinking / plan
Reuse existing model; verify happy path, incomplete data and recovery.

## Artifacts
- [Agent run or GitHub Issue/PR]
- [Checks and demo]

## Evidence / learning
Happy path passes; recovery remains unverified.

## Next
Agent: propose error-path tests.
Steward: review output and decide whether scope can expand.

## Resolution
Open.
```

An **agent can create or advance this record** within agreed permissions. The steward reviews assertions of fact and consequential interpretation. Small changes can be just a PR: no record needed.

### 3. `activity.md` — historical synthesis

If useful, append a short, reviewed weekly entry. For each reporting window say **exact start/end dates and repository**. Distinguish PRs **opened**, **merged**, and **still open**; do not assume counts sum (some merged PRs opened earlier). Summarize verified product movement, tests, observations, decisions, and unproven areas.

The agent may *drive the report itself*: gather accessible evidence, compute counts, draft the synthesis, identify source gaps, request corrections, and propose `now.md` updates. The human steward checks consequential claims before accepting them.

**PR throughput is not a score for an individual, human or agent.** If deeper measurement is worthwhile, prefer a balanced view of delivery speed and stability; don't measure only number of PRs.

## How people and agents initiate and drive work

| Origin / driver | Typical path | Human accountability |
| --- | --- | --- |
| Person → person-driven | Identify need → shape → work → verify → update | Driver accepts scope and conclusion |
| Person → agent-driven | Delegate bounded intent and success checks → agent plans/executes/verifies → review | Named steward grants scope and accepts result |
| Agent proposes → person-driven | Agent flags an opportunity with evidence → person chooses priority → work proceeds | Person accepts or rejects priority |
| Agent detects → agent-driven | Within an approved trigger/runbook, agent investigates, drafts intent, acts within permission, opens PR and reports proof | Named steward/maintainer owns policy and review gates |

**Agent-driven is a real execution ownership mode, not merely “agent assistance.”** The system must know: *what the agent is allowed to change, what proof is expected, where its run/PR is tracked, and when to escalate.* A person may initiate a run, but the agent can own the bounded execution from there.

Autonomy should match risk. Read-only investigation can be broader; code changes should use branches/PRs, tests and appropriate review; sensitive data, production deployment and material product decisions require the applicable human approvals and organizational controls.

## A practical agent-work contract

When delegating, give the agent enough context to carry work rather than becoming a conversational helper:

```text
Read project README, now.md and the relevant work record.
Goal: [what better looks like].
Scope: [repos/files/environments allowed].
Constraints: [security, UX, engineering, known tradeoffs].
Driver: you, within this approved task.
Human steward: [role or person].
Proof: [tests, review, evidence, screenshots, evaluation].
Output: [PR, artifact, updated work record, concise explanation].
Stop/escalate when: [risk, missing permission, ambiguous product decision].
Don't declare success without evidence; report what remains unverified.
```

For recurring monitoring, triggers and escalation tiers should be approved in advance. Do not infer that unrestricted autonomous operation is allowed merely because an agent can technically run.

## What replaces what?

| Familiar tool or ritual | Our default | Keep it when useful |
| --- | --- | --- |
| Kanban / sprint board | `now.md` current focus + Next | A visual board materially improves coordination |
| Backlog refinement | Only curate near-term possibilities | An authoritative external product backlog already exists |
| Epic / Loop planning page | One evolving work record when needed | Original source is elsewhere |
| Story / task / subtasks | Brief next move, checklist, optional Issue | A discrete assigned or agent-executable task benefits from GitHub tracking |
| Engineering implementation | Product-repo commits, branches, tests and PRs | **Always** |
| Daily status meeting | Self-service current state and work links | Synchronous judgment is needed |
| Weekly status deck | Source-linked, agent-generated activity summary | Reporting requirements dictate otherwise |
| Retrospective | Learning captured when it matters | A deliberate team reflection is helpful |

**One fact, one authoritative home:** An Issue owns its own state, a PR owns its review state, original research owns its evidence, and `uxai-context` connects the rationale and relevant links.

## How we establish “done”

- **Small change:** Implementation is accepted after appropriate technical checks, review and relevant integration/deployment controls.
- **Substantial work:** The intended result is **achieved, partial, invalidated or stopped**; relevant proof and follow-up are recorded.
- **Agent-driven work:** The agent can mark its bounded execution **ready for acceptance** with evidence, but cannot turn unreviewed assertions into an approved product outcome.
- **Platform development:** Continuous, with capabilities and releases that can be verified; weekly reporting never forces closure.

A working demo proves a specific flow runs. Technical tests prove defined behavior. User evaluations offer evidence about usefulness. These are **different claims** and should be labeled accordingly.

## Cadence: continuous work, optional weekly synthesis

Work moves whenever it is ready. No mandatory standups, sprints, story points, ceremony-led planning or weekly closure. Refresh `now.md` whenever priorities/next moves change.

Weekly, if valuable, ask an agent to inspect the **exact date range** of PRs and accessible work sources, calculate activity, draft `activity.md`, link evidence, and flag gaps. Review before publishing. The review can be async; it needn't become another meeting.

### Agent prompt: summarize activity

```text
Read this project's README, now.md and relevant work records.
For [repo] during [inclusive start, exclusive end), retrieve real PRs
opened and merged, including links. Summarize verified work movement,
tests/evaluations, decisions and unresolved risks. Distinguish evidence
from inference and identify any inaccessible sources. Draft an
append-only activity.md entry and propose now.md edits separately.
Do not change team priorities or claim a work item is complete.
```

## Why this is industry-informed

We are borrowing **documented principles**, not asserting industry-wide endorsement of our exact files:

| Source | Published practice | What we adapt |
| --- | --- | --- |
| [Anthropic — AI-native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook) | Durable intent, agent plans/specs, feedback loops, evaluations and review gates. The maintenance stage includes monitoring-triggered agent work. | One evolving work record by default; detailed versioned plans when complexity/risk warrants them; agents can originate work. |
| [OpenAI — Harness Engineering](https://openai.com/index/harness-engineering/) | “Humans steer. Agents execute.” Emphasis on agent-readable repositories, environments and feedback. | Make current context and next actions legible so an agent can drive execution end to end. |
| [GitHub — Agent activity in Issues and Projects](https://github.blog/changelog/2026-03-26-agent-activity-in-github-issues-and-projects/) | Assigned coding agents and session status can be surfaced with Issues and Projects. | Don't recreate session state in Markdown; link to real runs/PRs. |
| [DORA — Software delivery performance](https://dora.dev/guides/dora-metrics/) | Throughput and instability should be considered together. | Contextualize PR counts with tests, reliability, lead time and meaningful product results. |

These sources do **not** prescribe `now.md`, `work/*.md` or `activity.md`. That minimal structure is the `uxai-context` team's proposed experiment.

## Learn by following one week

[**Tutorial: One fictional week of human- and agent-driven work →**](../templates/examples/ai-native-week/README.md)

The tutorial follows the current view, work records, agent-driven execution, evidence and activity. All illustrative metrics and PRs are labeled fictional.

> **Success is when a person or agent can join, understand the current focus, do meaningful work, verify it and leave the context clearer — without reconstructing a board or asking for a status meeting.**
