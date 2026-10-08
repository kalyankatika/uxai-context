# Tutorial: One fictional week of people- and agent-driven product work

> **TRAINING SIMULATION, NOT PROJECT HISTORY.** Every contributor, agent session, PR number, user observation, test, and activity metric in this directory is invented. Do not copy these claims into a real status report.

**Estimated reading:** 5 minutes for the quick tour; 20–30 minutes to follow the full tutorial. **No software setup required** to read it.

This is a *walk-through you can actually follow*, not an instruction to copy a six-stage process or hold a weekly sprint. Four contributors and one bounded agent driver build two parts of a sample portfolio product without Scrum, Jira or a second Kanban board.

**Industry description:** *AI-native, context-driven product work*. This is a descriptive label, **not** a formal standard. The team routine comes from the [AI-native working model](../../../docs/AI-NATIVE-WORKING-MODEL.md); the fictional week shows what that routine looks like in practice.

## Choose a path

| I have… | Do this |
| --- | --- |
| **5 minutes** | Read [the map](#1-understand-the-map), [Friday's current view](now.md), and [the weekly activity report](activity.md). |
| **15 minutes** | Add [the walkthrough](walkthrough.md), then compare the [navigation](work/platform-navigation.md) and [data](work/portfolio-data.md) records. |
| **30 minutes** | Follow the [step-by-step exercise](#3-follow-the-week) and [try the prompts](#5-try-it-with-an-agent). |

## 1. Understand the map

```text
example/
├── README.md                       ← This tutorial
├── now.md                          ← One living view of current focus (Friday state)
├── walkthrough.md                  ← What changed during the fictitious week
├── activity.md                     ← A weekly summary of actual change IN THE FICTION
└── work/
    ├── platform-navigation.md      ← Human-driven work, resolved
    └── portfolio-data.md           ← Agent-driven work, still active
```

Every file has a different job. **You don't need every file for every change.**

| Familiar coordination need | In this approach | Who updates it? |
| --- | --- | --- |
| Kanban / “What are we doing?” | `now.md` | A person **or agent**, with review for priority changes |
| Epic or Loop project note | `work/<topic>.md` when substantial | Whoever drives the work (human or agent) |
| Small task | A PR, optional Issue, or short checklist | Person or scoped agent |
| Code delivery | Product repo commits/PRs/tests | Person or agent, reviewed per repo policy |
| Weekly status / evidence of movement | `activity.md` | Agent can own compilation; person checks facts |
| Earlier versions | Git history | Git, automatically |

**Do not create `now-monday.md`, `now-friday.md`, or a fresh work record each week.** The current view is edited in place; Git already versions it.

## 2. The week's fictional scenario

The team wants two concrete improvements to a sample product:

- **Navigation coherence:** Help someone go portfolio → initiative → portfolio without confusion. **Contributor B (a person)** drives this work; the other contributors and agents assist. It **resolves** by Friday for its agreed scope.
- **Portfolio data foundation:** Make representative portfolio data survive a save/reload. **Agent Session D1** is the **execution driver** within a human-approved scope; **Contributor A** is the accountable human steward. It **does not resolve** by Friday because error recovery is still unproven.

Other human contributors are **Contributor C** (research emphasis) and **Contributor D** (product/program emphasis). All can cross these boundaries.

This is the critical distinction:

> **The person or the agent closest to advancing the work can drive it. A human steward remains accountable for the boundaries and consequential acceptance of agent-led work.**

The agent is not merely taking notes or assisting a person: it investigates the repo, plans its bounded changes, implements, verifies, opens PRs and proposes the next step. The human steward is not asked to micromanage every micro-step.

## 3. Follow the week

### Step A — Monday: Orient and choose focus

Read the **Monday excerpt** in [walkthrough.md](walkthrough.md#monday--orient-choose-focus). That is how the single living `now.md` looked *then*. Compare it with [the Friday view](now.md). Notice the file did not multiply: Git would retain its Monday revision.

**Question to answer:** Can you see what matters and the next useful move without reading a board?

### Step B — Tuesday: Let humans and agents drive

Open [navigation](work/platform-navigation.md). Read **Intent** and **Next**. A person drives the outcome and others contribute.

Then open [portfolio data](work/portfolio-data.md). Look for:

- **Agent driver** and its session/task link (fictional in this example)
- **Human steward**
- **Approved scope and stop/escalate conditions**
- **Expected proof**
- **What remains unverified**

**Question:** Could a fresh agent or contributor continue safely from this record?

### Step C — Wednesday: See where execution lives

Read [the PR entries](activity.md#fictional-pr-ledger). These are *illustrative*, not clickable GitHub PRs. In a real project, link the actual product-repository PRs/Issues rather than mirroring their status in Markdown.

**Question:** Does a merged PR alone establish that users can complete the task? (No: it establishes a reviewed implementation change; user evidence is separate.)

### Step D — Thursday: Prove, change direction

Read [the evaluation](walkthrough.md#thursday--evidence-changes-the-work). A small fictional walkthrough shows a comprehension problem. The design and code change, and the work record captures why.

**Question:** Do we need a retrospective to retain that learning? (No: capture it with the work when it changes what we do.)

### Step E — Friday: Resolve one record, carry another forward

Read the **Resolution** in both work records. One is accepted for the *defined* scope, with a follow-up; the other stays **open**.

Read [activity.md](activity.md) as a human-reviewed summary. It includes a fictional count of 8 opened / 7 merged PRs and explicitly describes what those counts do **not** establish.

**Question:** What continues on Monday? Read [now.md](now.md) to answer in under a minute.

## 4. Translate this to an actual project

In the real `uxai-context` repo:

1. Open [the Periscope project](../../../projects/periscope/README.md) and its [real current view](../../../projects/periscope/now.md). **Don't replace that view with this fictional example.**
2. Confirm current focus and near-term candidates; edit existing headings rather than introduce a second board.
3. Choose a small, actionable improvement. If it needs continuity, copy the [work-thread template](../../work-thread.md) into the project's `work/` folder; otherwise work in the actual product repository.
4. If an agent will drive the task, state its approved scope, human steward, verifiable output, and where it must stop/ask.
5. Link resulting PRs, prototype/research evidence, and decisions. Verify any conclusion before declaring it accepted.
6. If a weekly snapshot would help, let an agent draft an `activity.md` entry from **real, accessible** GitHub and work records, with exact dates and links, then check it.

**Need help editing files?** Follow [Getting Started](../../../docs/GETTING-STARTED.md): either edit from GitHub.com (no installation), or use GitHub Desktop + VS Code for regular work.

### What belongs where?

- `uxai-context`: why, current focus, decisions, learning, links.
- Product repository: implementation, tests, PRs, agent session/Issue state.
- Figma/research tools: original design and evaluation artifacts.
- Teams or other conversation tools: discussions; bring over only consequential context.

## 5. Try it with an agent

These are **example prompts to adapt** to authorized tools and actual files; they do not execute anything automatically.

**Orient me (read-only):**

```text
Read the project README and now.md, then the relevant work record.
What is active, who or what is driving each item, what was verified,
and where are the meaningful unknowns? Cite the source file or PR.
Do not infer a missing decision.
```

**Agent-driven bounded work:**

```text
You are the execution driver for the following approved scope:
[small goal]. Human steward: [person or role].
Read README, now.md, relevant work record and repo instructions.
Investigate and propose a short plan, implement only within [scope],
run [checks], and open a PR. Update the work record with evidence,
remaining uncertainty and the next move. Stop and ask if you need
new permissions, sensitive access, production changes, or a
consequential product decision. Don't mark the work accepted yourself.
```

**Independent review:**

```text
Review the proposed result from a fresh perspective.
Compare the intent, accepted scope, changed artifacts, tests and
observed evidence. Identify gaps or unsupported success claims.
Do not approve your own changes or invent test results.
```

**Weekly activity report:**

```text
For [repo] over [start inclusive, end exclusive), retrieve actual PRs
opened and merged, their URLs, the relevant work records, and any
accessible verification evidence. Draft a short activity entry showing
movement, decisions, learning and still-open risks. Distinguish facts
from interpretation. If a source is inaccessible, say so. Propose
now.md changes separately; don't rewrite priorities without review.
```

## 6. Define “done” without tickets or sprint closure

| Type | What counts |
| --- | --- |
| Tiny fix | Correct change, appropriate checks and accepted PR/deployment state |
| Human-driven work | Intended scope met or deliberately resolved, evidence and follow-up recorded |
| Agent-driven work | Agent reports completed **execution** and evidence; human steward accepts or redirects the substantive outcome |
| Ongoing product | Continues across weeks/months; each verified improvement can be recognized without declaring the platform finished |

**Never equate PR volume with customer value.** Technical checks, prototype feasibility, user comprehension and production reliability answer different questions.

## 7. Industry references and what we actually borrow

| Public reference | What it documents | What our approach adds |
| --- | --- | --- |
| [Anthropic AI-native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook) | Intent artifacts, agent-produced specs/plans, independent feedback loops, review gates; monitoring can initiate agent work. | A lighter default: one living work record rather than forcing all SDLC artifacts on every task. |
| [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/) | “Humans steer. Agents execute.” Agent-legible repositories, feedback and a small number of humans directing substantial agent execution. | Human or agent can be the visible execution driver; a human steward remains accountable. |
| [GitHub agent activity](https://github.blog/changelog/2026-03-26-agent-activity-in-github-issues-and-projects/) | Agent sessions can be tracked through Issues and Projects, including review states. | Link to execution instead of copying agent session status into Markdown. |
| [DORA software delivery metrics](https://dora.dev/guides/dora-metrics/) | Delivery throughput and instability both matter. | Treat PR counts as descriptive activity evidence alongside quality and actual results. |

**Not an industry standard:** Our specific `now.md`, `work/`, `activity.md` arrangement. It is a lightweight, testable team convention informed by those public approaches.

## 8. Five-minute onboarding check

After following the example, you should be able to answer:

- Where do I look first? **The project's living `now.md`.**
- Can an agent drive? **Yes, inside approved scope with a human steward for accountability.**
- When do I create a work record? **When ongoing work needs durable context.**
- Where is the PR or issue status? **GitHub, not copied into Markdown.**
- What happens Friday? **Optionally summarize activity; don't force work to close.**
- What is done? **An accepted result backed by the appropriate evidence.**

**Ready to apply it?** Open the [actual project](../../../projects/periscope/README.md) and start from its current focus. No new methodology rollout required.
