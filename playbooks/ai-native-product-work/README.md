# AI-native product work — portable playbook

**Entry point for onboarding, adoption and the fictional tutorial.**

This is a reusable, lightweight **human + agent product-delivery routine**. It is not specific to Periscope, and it is not a formal industry methodology.

> **Orient → Focus → Drive & Execute → Verify → Capture → Repeat**

## Start here

| Need | Open |
| --- | --- |
| Understand our operating principles and when to use Markdown, Issues or PRs | [PLAYBOOK.md](PLAYBOOK.md) |
| See an end-to-end fictional week with human and agent drivers | [examples/one-week/README.md](examples/one-week/README.md) |
| Browse the final living current view in the example | [examples/one-week/now.md](examples/one-week/now.md) |
| Understand agent-led work with human stewardship | [examples/one-week/work/portfolio-data.md](examples/one-week/work/portfolio-data.md) |
| See a fictional source-linked activity summary | [examples/one-week/activity.md](examples/one-week/activity.md) |

The example is **fictional training data**, not any actual project's delivery history.

## File layout

```text
playbooks/ai-native-product-work/
├── README.md                  # Start here
├── PLAYBOOK.md                # Reusable operating convention
└── examples/
    └── one-week/
        ├── README.md          # Guided tutorial
        ├── walkthrough.md     # Monday–Friday exercise
        ├── now.md             # Example current view
        ├── activity.md        # Example reporting summary
        └── work/
            ├── platform-navigation.md
            └── portfolio-data.md
```

## Adopt in a different repository

1. Copy **this directory as a single unit**, retaining the internal `examples/` folder and links.
2. Decide where your project's actual `README.md`, living `now.md`, work records and code reside. **Do not copy fictional example data into them.**
3. Adapt references in `PLAYBOOK.md` to the destination's onboarding guides and work-thread templates (they currently point to other parts of `uxai-context`).
4. Keep one authoritative operating playbook in your organization; link to it from project READMEs instead of maintaining drifting copies.
5. For changes arising in another repository, compare and selectively reconcile the Markdown documents. **Do not automatically merge unrelated Git histories.** Review company IP/data restrictions before moving materials between an enterprise repo and a personal GitHub repo.

## Where Periscope fits

Periscope is the **first project adopting this routine**, not the owner of the generic playbook.

- [Periscope context](../../projects/periscope/README.md)
- [Periscope current work](../../projects/periscope/now.md)

The general context/onboarding guides remain in `uxai-context/docs/`. Their content is not duplicated in this portable package.

## Industry grounding

See the industry source table in [PLAYBOOK.md](PLAYBOOK.md#why-this-is-industry-informed) for public lessons from Anthropic, OpenAI, GitHub and DORA, and what is our local adaptation.
