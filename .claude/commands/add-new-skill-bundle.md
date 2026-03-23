---
name: add-new-skill-bundle
description: Workflow command scaffold for add-new-skill-bundle in Ai_Movara.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-new-skill-bundle

Use this workflow when working on **add-new-skill-bundle** in `Ai_Movara`.

## Goal

Adds a new skill or agent bundle to the project, including configuration, documentation, and agent definitions.

## Common Files

- `.agents/skills/*/SKILL.md`
- `.agents/skills/*/agents/openai.yaml`
- `.claude/skills/*/SKILL.md`
- `.claude/ecc-tools.json`
- `.claude/homunculus/instincts/inherited/*-instincts.yaml`
- `.claude/identity.json`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update .agents/skills/[SkillName]/SKILL.md
- Create or update .agents/skills/[SkillName]/agents/openai.yaml
- Create or update .claude/skills/[SkillName]/SKILL.md
- Update .claude/ecc-tools.json
- Update .claude/homunculus/instincts/inherited/[SkillName]-instincts.yaml

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.