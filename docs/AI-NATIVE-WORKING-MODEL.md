# AI-native working model

**A lightweight routine for continuous, context-driven product delivery.**

This is an approach for small, cross-disciplinary teams working with AI agents. It is **our synthesis**, not a formal industry-standard methodology. It complements [Working with Context](WORKING-WITH-CONTEXT.md): that guide explains what to preserve; this one explains how to keep work moving without replicating a Scrum, Jira, or Kanban administration layer.

> Make useful progress visible, keep context durable, and spend less time managing the work than doing it.

## The routine

**Orient → Focus → Act → Verify → Capture → Repeat**

1. **Orient.** Open the project's `README.md` and `now.md`. Follow only links relevant to your work.
2. **Focus.** Pick up a useful current priority or propose a change in focus. Name a driver for substantial collaborative work.
3. **Act.** Work with people and agents; research, design, implement, or investigate directly. Create a work record only if the effort needs durable context.
4. **Verify.** Check the result using the evidence appropriate to the work: tests, review, a working demonstration, user observation, or another explicit check.
5. **Capture.** Link implementation artifacts, note consequential decisions and learning, update the next move if it changed.
6. **Repeat.** Revisit `now.md` when priorities change. A week-end report is a snapshot, **not** a deadline or sprint boundary.

Inside meaningful work, use **Intent → Shape → Plan → Make → Prove → Learn ↺** to reason and execute. This is a loop, not six required files, role-owned phases, or approval meetings. Small changes can complete the loop in one session; complex work may need a more detailed plan and independent verification.

## What replaces what?

| Familiar need | Our default | Keep the existing tool when… |
| --- | --- | --- |
| Kanban / sprint board | One living project `now.md` for current focus, a short Next section, and things needing judgment | A visual board genuinely improves coordination |
| Backlog | A **small, curated Next** section; record longer-term ideas only if useful | There is a real product backlog already owned elsewhere |
| Epic / Loop page | One `work/<topic>.md` record for substantial work | The source material belongs in another authoritative tool |
| Story / task | A brief next move or local checklist | An Issue needs an assignee, reproduction steps, discussion, or agent assignment |
| Build / code review | Existing product repository, commits, PRs, tests, and deployment checks | Always; Markdown never replaces implementation history |
| Weekly status | A brief, human-reviewed, agent-assisted `activity.md` summary where worthwhile | Reporting or audit requirements require another channel |
| Decisions / research | Link authoritative artifacts; capture only the durable rationale or implication | The canonical record already exists elsewhere |

**One fact, one authoritative home.** Don't copy Issue status into a checklist, copy PR review states into `now.md`, or recreate the source files of Figma/SharePoint/Teams in Markdown. Link to them.

## The smallest project contract

```text
projects/<project>/
├── README.md       # stable product/project orientation
├── now.md          # one living view of current focus
├── work/           # substantial work threads, only when needed
└── activity.md     # optional append-only weekly synthesis, when useful
```

Use the [project starter](../templates/project-starter/) and existing [work-thread template](../templates/work-thread.md). Other established project directories (decisions, research, prototypes, meetings) remain valid. **Do not create duplicate structures** just to match this diagram.

### `now.md`: one current view

Keep the project's existing headings. Under Current focus, a useful entry needs only **what / driver / next move / context link**, for example:

```markdown
### Navigation coherence
Driver: Contributor B
Next: Review the integrated route on the working build.
Context: [Navigation work](work/navigation.md)
```

Keep a few meaningful priorities under **Current focus**, a short list under **Next**, and unresolved questions under an existing relevant heading. Do not require every future idea to become a tracked item. **Edit `now.md` in place**; Git is its version history, not dated copies of the file.

### `work/<topic>.md`: enough context to resume

Use the existing work-thread template when the work spans sessions or collaborators, needs an explicit plan, or has important decisions/evidence. Include as needed: intent, current shape, next moves, artifact links, proof, learning, and resolution.

A **driver** keeps the next move clear; they do not own a functional queue or approve every contribution. A designer can implement with an agent; a researcher can prototype or help with automated checks; engineering can participate in discovery; product/program expertise can drive a capability.

For small fixes, no separate work record is necessary. A PR and appropriate verification may be enough.

### `activity.md`: history without status theatre

When development pace warrants it, append a short weekly synthesis that includes:
- PRs opened and merged **from the product repository**, with the exact reporting dates and repository stated.
- Material work changes and links to real PRs/artifacts.
- What was verified, and what is still **not** verified.
- Consequential decisions, learning, and open questions.

Have an agent draft from sources it can actually access; a human checks counts, facts, links, and interpretations. **PR counts describe activity, not individual productivity or value.** If the summary adds no insight, skip it; do not require a weekly meeting to justify a weekly file.

## What counts as done?

- **Small change:** implemented, appropriately reviewed and tested, and integrated/released according to the actual team's rules.
- **Substantial work:** its intent is achieved, partially achieved, invalidated, or deliberately stopped; evidence and follow-ups are findable.
- **Ongoing platform:** continues as long as useful. Neither Friday nor a three-week mark forces closure.

Working code proves a capability can run under tested conditions. Technical checks do not, on their own, prove usefulness. User evidence does not automatically prove reliability. Be explicit about each kind of proof.

## Agent usage and safeguards

Agents can orient in repository context, investigate, propose plans, implement bounded changes, run checks, review a separate assumption, and draft context/activity updates. Human contributors choose priorities, review consequential tradeoffs, approve conclusions, and ensure necessary security/privacy, code review, and deployment controls remain in place. Do not promote an agent inference to a fact or decision without checking it.

In the application repository, keep agent-executable commands and local conventions near the code (e.g., agent instructions) and link the project context where accessible. Agents should not silently alter `now.md` or record a milestone as completed on their own.

## Starting tomorrow

1. Point the team to the current `now.md`.
2. Agree on a few current priorities and a next move for each.
3. Create one work record only when a piece of work needs shared continuity.
4. Keep building and reviewing PRs as usual.
5. Ask an agent to propose a weekly activity summary; review it and refresh current focus only if needed.

For a complete fictional Monday–Friday example with four unnamed contributors, open [One fictional week](../templates/examples/ai-native-week/README.md). **The example is not real project history.**

## Public inspiration (not a claim about internal team boards)

- [Anthropic: AI-native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook) — intent, planning, agent execution, feedback and verification.
- [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/) — repository legibility, explicit context, feedback loops and reliable agent execution.

Our use of `now.md` / work records / weekly synthesis is a practical adaptation within `uxai-context`. It does not imply either company uses these exact Markdown files.
