# Activity and capture notes

Reference for the agent maintaining [the team page](now.md). Teammates do not need to maintain this file.

## Keep the team page useful

Read the existing work, then summarize what works, what changed and what needs a person's attention. Keep the page under roughly 250 words. Preserve important decisions and their source links; remove repetition and stale instructions.

People can contribute a sentence, a link or a correction. Do not ask them to classify work, fill in fields, update tickets or write weekly reports. Name owners only when agreed. Keep implementation and build evidence in [uxd-periscope](https://github.com/kalyankatika/uxd-periscope).

Use Intent → Shape → Plan → Make → Prove → Learn as an internal completeness check: understand the purpose, consider an approach, choose a small next step, make it, check what happened and capture what changes the next decision. Do not expose these as required stages or templates.

## Weekly capture

The agent checks both repos once a week and prepares only useful changes to the team page and this snapshot. Also incorporate meaningful findings supplied during the work. Keep one reviewable update; do not create another PR when one already covers this work. Do not merge automatically or treat generated suggestions as team decisions.

Include PR counts and meaningful work outside PRs. Link evidence, distinguish main from branch work, and flag unverified usefulness. Stay quiet when nothing meaningful changed; bring the user only a material change or a decision that needs them. No team reporting meeting or rotating documentation duty.

## Activity baseline

Inspected October 6, 2026, 00:12 UTC (October 5, 20:12 New York). Heads: Periscope `cdc5815`; context `50f8431`. Historical baseline before the documentation PRs in this task.

| Repository | PRs total | Open | Merged | Closed without merge |
| --- | ---: | ---: | ---: | ---: |
| uxd-periscope | 1 | 0 | 1 | 0 |
| uxai-context | 1 | 1 | 0 | 0 |

Periscope [#1](https://github.com/kalyankatika/uxd-periscope/pull/1) added the Manager Loop and merged September 13. Context [#1](https://github.com/kalyankatika/uxai-context/pull/1) proposed governance changes and was open at capture.

For September 29–October 5 UTC: Periscope had 0 opened / 0 merged / 0 closed without merge; context had 1 / 0 / 0.

The broader work includes [19 main-history commits](https://github.com/kalyankatika/uxd-periscope/commits/cdc58155a8b7f55dd3d0f465a364b0e6ef4c94d5) and [21 additional organization-explorer commits](https://github.com/kalyankatika/uxd-periscope/compare/cdc58155a8b7f55dd3d0f465a364b0e6ef4c94d5...3f102d3ffe4185c119706ced22f10acb56e8d9de). [Main verification passed](https://github.com/kalyankatika/uxd-periscope/actions/runs/35421602423); the [branch check failed](https://github.com/kalyankatika/uxd-periscope/actions/runs/35629351835). These are activity and technical evidence, not deployment or user-value measures.

For each refresh, record capture time and heads; list all PR pages from both repos, deduplicate by repo/number, and separate merged from closed without merge. Use the last seven complete UTC days for event counts, and capture-time state for open counts. Include this task's documentation PRs normally after the original cutoff. Update the dates, counts and related state together; Git history keeps earlier snapshots.
