# Example Project — Now

> **FICTIONAL.** Friday's view of the one living current-state file.

## What we are trying to accomplish

Build and verify coherent core navigation and persistent portfolio data for a small product demonstration.

## Current focus

### Portfolio data foundation
**Driver:** Contributor A (engineering/AI depth)  
**Next:** Verify validation and failure/recovery behavior before resolving.  
**Context:** [Portfolio data](work/portfolio-data.md)

### Accessibility follow-up
**Driver:** Contributor B (design depth)  
**Next:** Verify the keyboard-focus update in Demo PR 108.  
**Context:** [Navigation](work/platform-navigation.md)

## What changed recently

- **Navigation resolved** for its defined core workflow; related work and evidence: [navigation](work/platform-navigation.md).
- Data save/reload path now passes narrow happy-path checks, but validation remains unproven.

## What we are learning

A technically working route still needs understandable labels. Representative data can reveal product questions before new infrastructure is built.

## Decisions pending

Should incomplete portfolio records be rejected or saved with warnings?

## Blockers / open questions

Failure recovery remains untested.

## Next

- Evaluate filtering patterns.
- Consider grounded AI orientation after the underlying data flow is dependable.