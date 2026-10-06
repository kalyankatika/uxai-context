# Periscope working loop

Current setup and activity baseline, followed by a proposed lightweight working pattern. The proposal does not assign roles or approve a new product roadmap.

## Current setup — October 5, 2026

Repository inspection: October 6, 2026, 00:12 UTC (October 5 in New York), before this documentation change. Periscope `main`: `cdc5815`; uxai-context `main`: `50f8431`.

- **Product and execution:** [README](https://github.com/kalyankatika/uxd-periscope/blob/main/README.md), [AGENTS.md](https://github.com/kalyankatika/uxd-periscope/blob/main/AGENTS.md), [Manager Loop](https://github.com/kalyankatika/uxd-periscope/blob/main/docs/manager-loop.md), and [BUILD_STATE.md](https://github.com/kalyankatika/uxd-periscope/blob/main/BUILD_STATE.md) already connect scope, agent execution and verification. Periscope is a local Next.js / SQLite UXD workspace with fictional examples, reviewed CSV imports and a separate saved workspace. Live connectors and enterprise access controls remain future work.
- **Evidence:** tests, build checks and browser walkthroughs sit beside the implementation. The latest recorded onboarding work reports 62 passing tests and a production build. The [main-head Verify run](https://github.com/kalyankatika/uxd-periscope/actions/runs/35421602423) succeeded. Recorded local preview sessions are historical; this inspection did not verify a running app or deployment. [Head-of-UXD evaluation](https://github.com/kalyankatika/uxd-periscope/blob/main/docs/head-uxd-research.md) is AI-assisted evaluation, not participant research.
- **Shared context:** [uxai-context / Periscope](https://github.com/kalyankatika/uxai-context/tree/main/projects/periscope) provides the intended home for intent, current focus, decisions and learning. At the original inspection, its lowercase [now.md](now.md) and project overview were still placeholders; no populated work or research records were present on the inspected main branch. Treat that as a capture gap, not evidence that no work occurred.
- **People:** the October 5 working brief describes a four-person core group bringing engineering, design, research and program-management expertise, with cross-role contribution intended. Repo records do not establish outcome drivers or a standing capture owner. Those remain to be named when work is selected.
- **Direction:** [AI-native principles](https://github.com/kalyankatika/uxd-periscope/blob/main/docs/ai-native-design-principles.md) and [Operations recommendations](https://github.com/kalyankatika/uxd-periscope/blob/main/docs/uxd-operations-backlog.md) are proposals. Their presence does not make them active commitments or implemented capabilities.

## Activity snapshot

All-time PR counts at the inspection cutoff; each PR counted once by repository and number. Merged means `merged_at` is present; closed below means closed without merge. This is the original pre-change baseline. The subsequently opened Periscope #2 and its replacement context PR are outside this cutoff; include them normally in the next refresh.

| Repository | Total PRs | Open | Merged | Closed without merge |
| --- | ---: | ---: | ---: | ---: |
| uxd-periscope | 1 | 0 | 1 | 0 |
| uxai-context | 1 | 1 | 0 | 0 |
| Combined | 2 | 1 | 1 | 0 |

- Periscope [#1 — Manager Loop](https://github.com/kalyankatika/uxd-periscope/pull/1) opened September 12 and merged September 13 (UTC): a reusable recipe for bounded agent work, acceptance and handoff.
- uxai-context [#1 — governance and repository safety](https://github.com/kalyankatika/uxai-context/pull/1) opened September 29 (UTC) and remains open. Its metadata/schema and review-policy changes are pending, not the main-branch operating contract.
- **Past seven complete UTC days, September 29–October 5** (`2026-09-29T00:00:00Z` inclusive to `2026-10-06T00:00:00Z` exclusive): Periscope 0 opened / 0 merged / 0 closed without merge; uxai-context 1 opened / 0 merged / 0 closed without merge. Open-at-cutoff counts are in the table above.

PR volume understates the visible implementation history. Periscope main has **19 reachable commits**, dated September 11–19 UTC, covering the initial workspace, imports and enterprise demo, hierarchy/reporting, interface refinements, design/operations guidance, demo playback and onboarding verification. See [main history](https://github.com/kalyankatika/uxd-periscope/commits/cdc58155a8b7f55dd3d0f465a364b0e6ef4c94d5). This is an activity signal, not a count of outcomes, deployments or team productivity.

The separate [organization-explorer branch](https://github.com/kalyankatika/uxd-periscope/tree/codex/organization-explorer), head `3f102d3`, is [21 commits ahead of main](https://github.com/kalyankatika/uxd-periscope/compare/cdc58155a8b7f55dd3d0f465a364b0e6ef4c94d5...3f102d3ffe4185c119706ced22f10acb56e8d9de). It includes team/priority maps, matrix, leadership brief, timeline and static read-only sharing work, with locally recorded verification. Its latest [remote Verify run failed](https://github.com/kalyankatika/uxd-periscope/actions/runs/35629351835) on September 21; it has no open PR at the cutoff. Keep its status separate from main. Integration and CI remain an unresolved delivery question, and real-user usefulness remains an evidence question.

**Counting method:** GitHub REST `repos/{owner}/{repo}/pulls?state=all&per_page=100&page=N` for both repositories, through an empty page; classify by `state` and `merged_at`. Period counts filter `created_at`, `merged_at`, or `closed_at` within the stated half-open UTC window; a PR can be opened and merged in the same period. Main commits use `commits?sha=<full inspected head>&per_page=100&page=N`, through an empty page. Check workflow evidence against its branch and head SHA. Counts cover these two accessible repositories only, not unpushed work or other enterprise repositories.

## Proposed loop: Intent → Shape → Plan → Make → Prove → Learn ↺

Use these as questions around one outcome, not six statuses, separate files or functional handoffs. Loop back whenever evidence changes the direction. A small fix can answer several questions in one PR or work note.

| Question | Smallest useful artifact or evidence |
| --- | --- |
| **Intent:** What changes for whom, and why now? | A few lines in the existing context `now.md`, with an observable outcome and constraints. |
| **Shape:** What experience could produce that change? | Link a sketch, prototype, research finding or feasibility check; bring relevant expertise together. |
| **Plan:** What is the smallest path to evidence? | Name one outcome driver, the next experiment, completion criteria and any human/agent execution boundary. Use an existing work thread only if evolving detail needs a home. |
| **Make:** What can we build or try? | Code, prototype, research stimulus or data work in its natural home. Use the existing Manager Loop for substantial builds. |
| **Prove:** What happened against the criteria? | Relevant tests/build, observed interaction or participant evidence. State revision, result and limits; distinguish implemented, verified, deployed and useful. |
| **Learn:** What does the evidence change? | A short implication and a human decision to continue, adapt or stop; update current intent and link durable evidence. |

The driver can come from any of the four specialties and carries the outcome across the loop. Others contribute where their judgment helps. Agents can retrieve context, draft, implement and check within the agreed boundary. People own outcome choice, interpretation, consequential tradeoffs and acceptance. The existing Manager Loop's manager is the primary agent, not an extra human approval role. Program coordination can keep connections and decisions clear without becoming ticket administration.

Keep only a few active outcomes (start with 3 or fewer). Each needs **intent / driver / evidence sought / next move / links** within existing `now.md` headings. Do not preassign people or turn the proposed Operations backlog into commitments. A PR is a delivery/review artifact; an outcome may need several PRs or none.

## Capture cadence — proposal for the next two weeks

Build on uxai-context's existing [weekly habit](https://github.com/kalyankatika/uxai-context/blob/main/docs/WORKING-WITH-CONTEXT.md#a-lightweight-weekly-habit).

- **At a meaningful change:** whoever did the work leaves a short evidence link and implication. Update `BUILD_STATE.md` for execution handoff; update context `now.md` when focus, learning, a blocker or the next move changes. Avoid parallel status narratives.
- **Once a week, asynchronously:** a project owner or rotating contributor spends about 10 minutes reviewing an agent-drafted capture. Record opened / merged / closed-without-merge PRs for the last complete seven-day UTC window, open PRs at capture time, 2–3 meaningful changes, evidence/limits, and the next decision. Include relevant branch/direct-commit activity so work outside PRs remains visible. Name the first capture contributor when the team starts the trial.
- **Write only what changed:** refresh this document's activity snapshot and current setup together, including dates, inspected heads, branch/check evidence and counting exclusions; Git history retains prior captures. Keep current outcomes in context `now.md`, linking here for counts and to source artifacts for proof. Create a decision/research note only when something durable needs its own explanation. No new board, daily status request or standing documentation meeting.
- **After two captures:** assess whether someone can understand what changed and what needs judgment in under two minutes. Shorten or drop fields that did not help a decision. No recurring job is enabled by this proposal.

Reusable capture request:

> Review both repositories for the last complete seven UTC days. State the window, capture time and inspected heads. Count all PRs accurately across pages; separate opened, merged, closed without merge and currently open. Summarize only meaningful changes, including work outside PRs, with evidence links. Distinguish main, branch work, proposals and observed outcomes. Suggest the smallest edits to this activity snapshot and Periscope now.md. Flag missing evidence and decisions for human judgment; do not infer owners, adoption or productivity from counts.

First useful next move: confirm the chosen outcome, driver and evidence sought in the existing [now.md](now.md). Selecting that outcome is still a human decision; this capture does not start implementation or change the context repo's pending governance PR.
