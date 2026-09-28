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

As roles increasingly overlap, organize contribution around the **function being performed**, not a rigid job boundary.

Common functions include:

- **Explore** — research, discovery, evidence, questions
- **Create** — experience ideas, content, flows, design intent
- **Build** — prototypes, implementation, technical learning
- **Guide** — outcomes, strategy, priorities, decisions
- **Enable** — systems, facilitation, operations, connections
- **Learn** — evaluation, synthesis, reflection, iteration

A person may contribute through several of these functions on the same project.

This does **not** remove specialist expertise. It lets deep specialists participate across more of the delivery loop when they have the context and capability to do so.

Capture context close to the work that produced it, regardless of title. Anyone can update `now.md` when reality changes.

> **Deep expertise. Broader contribution. Shared context.**

Ownership stays close to the source.

---

# 3. Scale reuse from real work

Reusable capability should emerge from work that has already proven useful.

Use this progression:

```text
one-off work
    ↓
useful again
    ↓
repeatable pattern
    ↓
shared asset
```

Do not build a library of hypothetical future assets.

Start inside the project. When something clearly helps another project or team, distill the smallest reusable part and place it under [`shared/`](../shared/README.md).

Examples may eventually include:

- patterns
- skills or workflows
- lightweight agent recipes
- prompts with demonstrated repeat value
- starter/reference implementations
- internal tooling references
- pointers to authoritative standards

Do not pre-create category folders until enough real assets exist to justify them.

> **Capture the reusable part, not everything.**

This is how prototype and project work compounds instead of disappearing when the immediate work ends.

# 4. Scale through common metadata

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

# 5. Scale through consumers

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

# 6. Scale permissions carefully

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

# 7. Scale agent capability gradually

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

# 8. Health checks for scale

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
