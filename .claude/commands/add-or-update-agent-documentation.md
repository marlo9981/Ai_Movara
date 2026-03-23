---
name: add-or-update-agent-documentation
description: Workflow command scaffold for add-or-update-agent-documentation in Ai_Movara.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-or-update-agent-documentation

Use this workflow when working on **add-or-update-agent-documentation** in `Ai_Movara`.

## Goal

Adds or updates agent documentation and command markdown files, often in bulk.

## Common Files

- `agents/*.md`
- `commands/*.md`
- `assets/images/*`
- `tests/*`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add or update agents/*.md files
- Add or update commands/*.md files
- Optionally add or update assets/images/* for documentation
- Optionally update tests/* for agent/command validation

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.