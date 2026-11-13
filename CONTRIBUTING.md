# Contributing to UX AI Context

You do not need to be a Git expert to contribute.

## New to the repository?

Start with [Getting Started](docs/GETTING-STARTED.md).

## The short version

1. Read the relevant project's `README.md` and `now.md`.
2. Make the smallest useful context update.
3. Link to source artifacts rather than duplicating them.
4. Use a [template](templates/README.md) when helpful.
5. Commit with a short description of what changed.

## Common contributions

| Contribution | Where |
|---|---|
| Project changed | update `projects/<project>/now.md` |
| Important decision | `projects/<project>/decisions/` |
| Meeting outcome | `projects/<project>/meetings/` |
| Research finding | `projects/<project>/research/` |
| Prototype learning | `projects/<project>/prototypes/` |
| Proven reusable pattern, skill, agent recipe, prompt, or tooling reference | [`shared/`](shared/README.md) |

## Two ways to contribute

### GitHub.com
Best for quick edits and people new to Git.

Open a file → **Edit** → make the change → **Commit changes**.

For a new file, use **Add file → Create new file** and copy the relevant template.

### GitHub Desktop + VS Code
Best for regular contributors.

Pull → edit in VS Code → review in GitHub Desktop → commit → push.

See the full [Getting Started guide](docs/GETTING-STARTED.md).

## Never commit

Never commit:

- secrets, API keys, tokens, passwords, private keys, or other credentials
- customer data
- personal data or personally identifiable information
- confidential employer content
- environment files or exports that may contain any of the above

Use placeholders, synthetic examples, or links to approved source systems instead.

Before opening or updating a pull request, run:

```sh
python3 scripts/secret_scan.py
python3 scripts/context_staleness.py
```

The repository hygiene workflow runs these checks on pull requests.

## Keep it light

Capture durable context, not every activity.

If something came from a Teams, Viva Engage, email, demo, or working conversation, only bring it here when it will remain useful beyond that moment.

If something proves useful beyond one project, capture only the reusable part in [`shared/`](shared/README.md).

> **Link to the artifact. Capture the context.**
