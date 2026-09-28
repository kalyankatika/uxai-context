# Getting Started

This guide is for anyone joining `uxai-context` for the first time — including people who have never worked in GitHub before.

You may arrive here from a Teams post, Viva Engage conversation, email, demo, meeting, or a direct project link. You do **not** need to become a Git expert or even contribute immediately. Browsing, reusing, and sharing useful context are all valid ways to participate.

You can contribute in two ways:

1. **GitHub.com — easiest path.** No local setup required.
2. **GitHub Desktop + VS Code + Copilot — best for regular contributors.**

Start with GitHub.com. Move to the local workflow when it becomes useful.

A simple participation path is:

```text
browse → understand → contribute when useful → reuse/share
```

The goal is participation, not process.

---

## 1. First, understand the project

From the repository home page:

1. Open the relevant folder under [`projects/`](../projects/).
2. Read the project's `README.md`.
3. Read the project's `now.md`.

For Periscope:

- [Project overview](../projects/periscope/README.md)
- [Current state](../projects/periscope/now.md)

You do **not** need to read every file.

Think of:

- `README.md` as **what this project is**
- `now.md` as **what matters right now**
- the folders below them as **deeper context when you need it**

---

# Fast path: contribute on GitHub.com

Use this path when you want to make a quick update and do not want to set up anything locally.

## Update an existing file

For example, if the current project status changed:

1. Open the project's `now.md`.
2. Select the **Edit** pencil on GitHub.com.
3. Update only the section that changed.
4. Select **Commit changes**.
5. Add a short description of what you changed.
6. Commit the change. If the repository requires review, GitHub will guide you through creating a branch or pull request.

That's it.

## Add a new note

If you need to capture a decision, research finding, meeting outcome, or work thread:

1. Open [Templates](../templates/README.md).
2. Open the template you need.
3. Copy its contents.
4. Go to the appropriate project folder.
5. Choose **Add file → Create new file**.
6. Give the file a simple name, for example:
   - `2026-09-27-navigation-decision.md`
   - `2026-09-27-research-synthesis.md`
   - `2026-09-27-working-session.md`
7. Paste the template.
8. Replace the prompts with your useful context.
9. Commit the change.

You do not need to complete every section. Delete anything that does not apply.

## Where should my note go?

| I am capturing... | Put it in... |
|---|---|
| A change in current focus or status | `projects/<project>/now.md` |
| An important decision | `projects/<project>/decisions/` |
| Useful meeting outcomes | `projects/<project>/meetings/` |
| Research evidence or findings | `projects/<project>/research/` |
| Prototype context or learning | `projects/<project>/prototypes/` |
| A meaningful ongoing piece of work | Use the work-thread template and place it with the most relevant project context |

If you are unsure, choose the closest place. The team can reorganize later.

---

# Full path: GitHub Desktop + VS Code + Copilot

Use this when you expect to contribute regularly.

## One-time setup

1. Install and open **GitHub Desktop**.
2. Choose **File → Clone Repository**.
3. Select `uxai-context`.
4. Choose a local folder.
5. Select **Clone**.
6. In GitHub Desktop choose **Repository → Open in Visual Studio Code**.
7. Sign in to GitHub in VS Code and enable **GitHub Copilot**.

## Each time you work

1. In GitHub Desktop, **Fetch origin** and **Pull origin** if updates are available.
2. Open the relevant project in VS Code.
3. Read `README.md` and `now.md`.
4. Make your update.
5. Review the change in GitHub Desktop.
6. Add a short commit message.
7. Commit and **Push origin**.

Useful commit messages:

- `update current project focus`
- `add navigation research finding`
- `capture prototype review decision`
- `add working session notes`

---

# Use Copilot as a guide

You do not need to know where every file belongs.

Try:

> Read this project's README and now.md and orient me to the current context.

> I have these notes. Tell me what should be captured in this repository and where.

> Use our meeting template to turn these notes into a concise durable record.

> Find prior decisions or research related to this topic before I add anything new.

> Update now.md based on these changes, without rewriting sections that did not change.

Copilot should help you navigate the system rather than require you to learn the system first.

---

# What is worth capturing?

Ask:

> **Will this help another teammate understand or advance the work later?**

Usually capture:

- decisions and why they were made
- research findings and implications
- meaningful project changes
- prototype learnings
- important open questions
- useful meeting outcomes
- links to authoritative artifacts

Usually skip:

- every chat message
- every task
- routine status narration
- copies of Figma, Jira, SharePoint, or other source content

When in doubt:

> **Link to the artifact. Capture the context.**

---

# Your first contribution

A good first contribution is intentionally small.

Examples:

- fix a stale line in `now.md`
- add one research finding
- capture one decision
- add a missing Figma or source link

The repository becomes valuable through small, current contributions — not large documentation efforts.
