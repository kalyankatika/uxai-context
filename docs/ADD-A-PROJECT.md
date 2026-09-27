# Add a Project

Use this guide when a team wants to bring another project into `uxai-context`.

The goal is **repeatability without bureaucracy**.

Every project starts with the same small contract and expands only when needed.

---

# The project contract

Every project begins with:

```text
projects/<project-name>/
├── README.md
├── now.md
├── project.yaml
├── decisions/
├── meetings/
├── research/
└── prototypes/
```

Use [`templates/project-starter/`](../templates/project-starter/) as the starter kit.

---

# Step 1 — Choose the folder name

Use a short lowercase name with hyphens if needed.

Examples:

- `customer-discovery`
- `design-system-pilot`
- `new-experience`

Avoid organizational jargon when a clearer project name exists.

---

# Step 2 — Copy the starter kit

From a local clone:

1. Copy `templates/project-starter/`.
2. Paste it under `projects/`.
3. Rename the folder.
4. Replace the starter text.
5. Commit and push.

If working only on GitHub.com, create the three top-level files from the starter kit and add the subfolders as they become necessary.

---

# Step 3 — Fill in only three things

## `README.md`

Explain:

- what the project is
- who it is for
- what outcome it is trying to create
- where the important source artifacts live

Think of this as the stable project front door.

## `now.md`

Explain:

- what matters right now
- current focus
- recent changes
- current learning
- open questions
- next steps

Think of this as the living snapshot.

## `project.yaml`

Provide a minimal machine-readable identity and source map.

Do not add fields unless there is a demonstrated use for them.

---

# Step 4 — Start using it

Do not backfill years of history.

Start with:

- the current state
- current important links
- active decisions
- useful recent research
- work that is actually moving

Historic material can be added later when it proves valuable.

---

# Step 5 — Make the project discoverable

Once committed, the project can be:

- browsed directly in GitHub
- used by Copilot and other agents
- linked from Teams or project materials
- indexed by Periscope or other context experiences
- summarized for onboarding or reporting

The same Markdown remains the durable source.

---

# When should a project get more structure?

Only add structure when the project has enough activity to justify it.

Examples:

- add a dedicated `work/` folder when work threads become numerous
- add `plans/` when durable plans need their own home
- add project-specific templates only if the shared templates are insufficient

Avoid designing a bespoke taxonomy for every project.

Consistency across projects is more valuable than theoretical completeness within one project.
