# Scale the System

`uxai-context` should scale by repeating a small project contract, not by turning into a centralized documentation program.

The system has four layers.

```text
People + teams
     ↓
Project folders
     ↓
Shared conventions
     ↓
Consumers: GitHub / Copilot / agents / Periscope / reporting
```

---

# 1. Scale by replication

New projects use the same starter structure:

- `README.md` — stable orientation
- `now.md` — current state
- `project.yaml` — lightweight structured identity
- standard durable-context folders
- shared templates

This consistency lets people move between projects without relearning the system.

It also gives AI and downstream products a predictable contract.

---

# 2. Scale contribution, not documentation

The system works when context is updated as part of normal work.

Do not create a central documentation owner who becomes responsible for reconstructing everyone else's project.

Instead:

- designers capture durable design decisions and learnings
- researchers capture findings and implications
- content captures durable language or content decisions
- design engineering captures prototype/implementation context
- product captures outcome, priority, and major direction changes
- anyone can update `now.md` when the project changes

Ownership stays close to the source.

---

# 3. Scale through common metadata

Keep frontmatter small and consistent.

A durable record generally needs only enough metadata to answer:

- what type of record is this?
- which project does it belong to?
- when was it created?
- what is its current status?
- what topics help discovery?

Do not build a large ontology before a consumer needs it.

Periscope and agent workflows can drive future metadata additions based on actual use.

---

# 4. Scale through consumers

The repository itself does not need to become the final experience for every audience.

Markdown is the durable substrate.

Different consumers can provide different views:

```text
                    uxai-context
                         │
                  Markdown + Git
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   GitHub/Copilot     Periscope       Agents
        │                │                │
   contributor view   discovery view   task view
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                 Reports / summaries
```

This means we should avoid optimizing the source files for one downstream experience.

Keep the source understandable by itself.

---

# 5. Scale permissions carefully

The repo can point to source systems with different access levels.

A link in this repository does not change the permissions of the source system.

As automated retrieval grows:

- preserve source-system permissions
- avoid copying restricted artifacts merely to make retrieval easier
- retain provenance
- separate generated synthesis from authoritative sources
- use least-privilege access for automated integrations

The context layer should connect governed systems, not bypass them.

---

# 6. Scale agent capability gradually

The repository is already useful to Copilot and other agents because state is explicit and versioned.

Future agentic capabilities may:

- orient themselves to a project
- find relevant research and decisions
- prepare meetings
- suggest context updates
- identify contradictions or stale context
- generate summaries
- traverse projects
- continue longer-running tasks using Git as durable state

Add agent infrastructure only when a real workflow requires it.

Do not prematurely add:

- memory databases
- embeddings
- orchestration frameworks
- large task ledgers
- custom agent manifests

Good files, links, Git history, and clear instructions are the foundation.

---

# 7. Health checks for scale

A project is healthy when:

- its `README.md` still accurately describes it
- `now.md` is current
- important decisions are findable
- useful research is linked
- primary artifacts have authoritative links
- someone new can orient without a meeting
- people and AI can answer important project questions from the repo and its linked sources
- missing answers expose useful context gaps rather than triggering blanket documentation
- the team is not spending significant time maintaining the system

If maintaining the context becomes the work, simplify it.

---

# The scaling principle

> **Standardize the entry points. Keep the content flexible.**

That gives people consistency without forcing every discipline and project into the same shape.
