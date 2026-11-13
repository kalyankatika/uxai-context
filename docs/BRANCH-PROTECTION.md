# Branch Protection Notes

These are **recommended settings**, not a statement of current GitHub configuration. Apply them through the repository or enterprise GitHub settings according to internal policy.

For `main`, recommend:

- require a pull request before merging
- require at least 1 approval
- require review from CODEOWNERS
- dismiss stale approvals when new commits are pushed
- require all review conversations to be resolved
- require status checks before merging:
  - **Secret scan**
  - **Context staleness**
- block force pushes
- block branch deletion
- apply the same protection to administrators unless internal policy requires an exception

## Native GitHub security

If available under the enterprise GitHub plan and internal policy, also enable:

- GitHub secret scanning
- push protection for detected secrets
- dependency/security alerts appropriate to the repository

The repository-local checks are a baseline and do not replace enterprise security controls.
