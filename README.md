# UX AI Context

`uxai-context` is a shared, versioned context repository for UX AI work.

It gives teams a lightweight place to capture durable project context: current state, plans, decisions, research, meeting outcomes, prototype learnings, important references, and links to source artifacts.

> **Goal: make project context easy for people and AI to find, understand, and reuse.**

We are starting small with a baseline structure and a few conventions. We will evolve it through actual use.

## New here? Start here

You do **not** need deep Git knowledge to contribute. If you can edit a Markdown file, you can help keep context current.

### 1. Get the repository
Using **GitHub Desktop**: open GitHub Desktop → **File → Clone Repository** → select `uxai-context` → choose a local folder → **Clone**.

### 2. Open it in VS Code
From GitHub Desktop choose **Repository → Open in Visual Studio Code**.

### 3. Use GitHub Copilot
Sign in to GitHub in VS Code and make sure Copilot is enabled.

Useful prompts:
- "Read the project README and now.md before helping me with this task."
- "Find previous decisions or research related to this topic."
- "Turn these notes into the appropriate context update using our templates."
- "What project context should I update based on what I just worked on?"

Copilot should reduce documentation effort, not create more process.

## What are you trying to do?

| I want to... | Go here |
|---|---|
| Understand the current project | [Project README](projects/periscope/README.md) |
| See what is happening now | [Current state](projects/periscope/now.md) |
| Capture an important decision | [Decision template](templates/decision.md) |
| Capture useful meeting outcomes | [Meeting template](templates/meeting.md) |
| Add a research finding | [Research note template](templates/research-note.md) |
| Capture a meaningful piece of work | [Work thread template](templates/work-thread.md) |
| Browse decisions | [Decisions](projects/periscope/decisions/) |
| Browse meeting notes | [Meetings](projects/periscope/meetings/) |
| Browse research | [Research](projects/periscope/research/) |
| Browse prototype context | [Prototypes](projects/periscope/prototypes/) |

If you are unsure where something belongs, use the closest reasonable place. We can improve the structure later.

## The simplest contribution flow

1. **Pull** the latest version in GitHub Desktop.
2. **Open** the relevant file or copy a template.
3. **Write normally** in Markdown.
4. **Save** in VS Code.
5. Review the change in GitHub Desktop.
6. **Commit** with a short meaningful message.
7. **Push** your change.

For larger or higher-impact changes, use a branch and pull request when review adds value. GitHub.com is also useful for quick reading, small edits, history, and review.

## What should I capture?

Do not document everything.

Ask:

> **Would another teammate benefit from knowing this next week or three months from now?**

Good things to capture:
- an important decision
- something research taught us
- a meaningful change in direction
- a useful meeting outcome
- a prototype and what we learned from it
- an assumption being tested
- a blocker or open question
- the team's current focus
- links to important artifacts

Usually do **not** capture every chat message, every small task, routine status updates, or copies of information that already has a clear authoritative source elsewhere.

## Where does information live?

| Type of work | Usually lives in |
|---|---|
| Design | Figma |
| Code | Product/code repository |
| Enterprise documents | SharePoint / OneDrive |
| Formal delivery tracking | Jira |
| Fast conversation | Teams |
| Durable project context | `uxai-context` |

> **Link, don't duplicate.**

Use the repository to preserve the context around source artifacts: why they matter, what changed, what we learned, and where the source lives.

## Initial use cases

1. **Shared project context** — quickly understand what a project is, where it stands, and what matters now.
2. **Day-to-day collaboration** — preserve useful context created through research, design, content, product, engineering, planning, and working sessions.
3. **AI-assisted project work** — give GitHub Copilot and future agents reliable, versioned project context.
4. **Onboarding** — help someone new orient without reconstructing project history through meetings and chat.
5. **Reporting and synthesis** — derive summaries, decisions, risks, and progress from existing work instead of creating separate reporting.
6. **Context experiences** — structured context can be consumed by experiences such as **Periscope** for discovery, navigation, relationships, summaries, project visibility, and dogfooding UX AI capabilities against real working context.
7. **Future discovery** — shared conventions can increasingly connect projects, people, research, decisions, prototypes, capabilities, and learnings.

## Designed for people and AI

This repository should remain easy for a teammate to read while also becoming increasingly useful to capable AI systems and long-running agents.

Clear, linked, structured, versioned files can support agents that help with project orientation, finding related decisions and research, preparing for meetings, summarizing changes, identifying open questions, maintaining context, connecting artifacts, preparing reviews, and continuing longer-running tasks.

We do **not** need to build all of that now.

Our starting point is simply to keep context:

**clear, current, linked, structured, and versioned.**

See [AGENTS.md](AGENTS.md) for lightweight guidance for AI tools working in this repository.

## Repository structure

```text
uxai-context/
├── README.md
├── AGENTS.md
├── projects/
│   └── periscope/
│       ├── README.md
│       ├── now.md
│       ├── project.yaml
│       ├── decisions/
│       ├── meetings/
│       ├── research/
│       └── prototypes/
└── templates/
    ├── decision.md
    ├── meeting.md
    ├── research-note.md
    └── work-thread.md
```

This is intentionally small. Additional projects and structure can be added when useful.

## Lightweight metadata

Some files use a small block at the top called **frontmatter**:

```yaml
---
type: decision
project: periscope
status: active
date: 2026-09-27
topics:
  - discoverability
  - context
---
```

You usually do not need to worry about it. Templates already include it.

Metadata should stay minimal and only exist when it improves discoverability, AI context, automation, reporting, or downstream experiences.

## A simple rule for everyone

When you finish meaningful work, ask:

> **Did we learn, decide, or change something another person should be able to find later?**

If yes, spend a few minutes updating the appropriate context.

That is the system.

## Working principles

- **Keep context close to the work.**
- **Capture what will remain useful.**
- **Link rather than duplicate.**
- **Prefer current context over exhaustive documentation.**
- **Make decisions and learnings discoverable.**
- **Use AI to reduce documentation effort, not increase process.**
- **Write once and enable many uses.**
- **Let the system evolve through use.**
