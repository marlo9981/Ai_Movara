---
name: ai-movara-conventions
description: Development conventions and patterns for Ai_Movara. JavaScript project with mixed commits.
---

# Ai Movara Conventions

> Generated from [marlo9981/Ai_Movara](https://github.com/marlo9981/Ai_Movara) on 2026-03-23

## Overview

This skill teaches Claude the development patterns and conventions used in Ai_Movara.

## Tech Stack

- **Primary Language**: JavaScript
- **Architecture**: hybrid module organization
- **Test Location**: mixed

## When to Use This Skill

Activate this skill when:
- Making changes to this repository
- Adding new features following established patterns
- Writing tests that match project conventions
- Creating commits with proper message format

## Commit Conventions

Follow these commit message conventions based on 26 analyzed commits.

### Commit Style: Mixed Style

### Prefixes Used

- `feat`

### Message Guidelines

- Average message length: ~40 characters
- Keep first line concise and descriptive
- Use imperative mood ("Add feature" not "Added feature")


*Commit message example*

```text
feat: add Ai_Movara ECC bundle (.claude/homunculus/instincts/inherited/Ai_Movara-instincts.yaml)
```

*Commit message example*

```text
Merge pull request #1 from marlo9981/ecc-tools/Ai_Movara-1773633537205
```

*Commit message example*

```text
Merge pull request #2 from marlo9981/marlo9981-patch-1
```

*Commit message example*

```text
Create trouble
```

*Commit message example*

```text
Add files via upload
```

*Commit message example*

```text
Update README.md
```

*Commit message example*

```text
Delete .github/workflows directory
```

*Commit message example*

```text
feat: add Ai_Movara ECC bundle (.codex/agents/docs-researcher.toml)
```

## Architecture

### Project Structure: Single Package

This project uses **hybrid** module organization.

### Configuration Files

- `Claude/everything-claude-code-main/.github/workflows/ci.yml`
- `Claude/everything-claude-code-main/.github/workflows/maintenance.yml`
- `Claude/everything-claude-code-main/.github/workflows/monthly-metrics.yml`
- `Claude/everything-claude-code-main/.github/workflows/release.yml`
- `Claude/everything-claude-code-main/.github/workflows/reusable-release.yml`
- `Claude/everything-claude-code-main/.github/workflows/reusable-test.yml`
- `Claude/everything-claude-code-main/.github/workflows/reusable-validate.yml`
- `Claude/everything-claude-code-main/.opencode/package.json`
- `Claude/everything-claude-code-main/.opencode/tsconfig.json`
- `Claude/everything-claude-code-main/.prettierrc`
- `Claude/everything-claude-code-main/eslint.config.js`
- `Claude/everything-claude-code-main/package.json`
- `Claude/everything-claude-code-main/tests/brainstorm-server/package.json`

### Guidelines

- This project uses a hybrid organization
- Follow existing patterns when adding new code

## Code Style

### Language: JavaScript

### Naming Conventions

| Element | Convention |
|---------|------------|
| Files | camelCase |
| Functions | camelCase |
| Classes | PascalCase |
| Constants | SCREAMING_SNAKE_CASE |

### Import Style: Relative Imports

### Export Style: Mixed Style


*Preferred import style*

```typescript
// Use relative imports
import { Button } from '../components/Button'
import { useAuth } from './hooks/useAuth'
```

## Testing

### Test Framework

No specific test framework detected — use the repository's existing test patterns.

### File Pattern: `*.test.js`

### Test Types

- **Unit tests**: Test individual functions and components in isolation
- **Integration tests**: Test interactions between multiple components/services

### Coverage

This project has coverage reporting configured. Aim for 80%+ coverage.


## Error Handling

### Error Handling Style: Try-Catch Blocks


*Standard error handling pattern*

```typescript
try {
  const result = await riskyOperation()
  return result
} catch (error) {
  console.error('Operation failed:', error)
  throw new Error('User-friendly message')
}
```

## Common Workflows

These workflows were detected from analyzing commit patterns.

### Feature Development

Standard feature implementation workflow

**Frequency**: ~16 times per month

**Steps**:
1. Add feature implementation
2. Add tests for feature
3. Update documentation

**Files typically involved**:
- `manifests/*`
- `**/*.test.*`
- `**/api/**`

**Example commit sequence**:
```
feat: add Ai_Movara ECC bundle (.claude/skills/Ai_Movara/SKILL.md)
feat: add Ai_Movara ECC bundle (.claude/ecc-tools.json)
feat: add Ai_Movara ECC bundle (.agents/skills/Ai_Movara/SKILL.md)
```

### Add New Skill Bundle

Adds a new skill or agent bundle to the project, including configuration, documentation, and agent definitions.

**Frequency**: ~2 times per month

**Steps**:
1. Create or update .agents/skills/[SkillName]/SKILL.md
2. Create or update .agents/skills/[SkillName]/agents/openai.yaml
3. Create or update .claude/skills/[SkillName]/SKILL.md
4. Update .claude/ecc-tools.json
5. Update .claude/homunculus/instincts/inherited/[SkillName]-instincts.yaml
6. Update .claude/identity.json
7. Update .codex/AGENTS.md
8. Update .codex/agents/docs-researcher.toml
9. Update .codex/agents/explorer.toml
10. Update .codex/agents/reviewer.toml
11. Update .codex/config.toml

**Files typically involved**:
- `.agents/skills/*/SKILL.md`
- `.agents/skills/*/agents/openai.yaml`
- `.claude/skills/*/SKILL.md`
- `.claude/ecc-tools.json`
- `.claude/homunculus/instincts/inherited/*-instincts.yaml`
- `.claude/identity.json`
- `.codex/AGENTS.md`
- `.codex/agents/docs-researcher.toml`
- `.codex/agents/explorer.toml`
- `.codex/agents/reviewer.toml`
- `.codex/config.toml`

**Example commit sequence**:
```
Create or update .agents/skills/[SkillName]/SKILL.md
Create or update .agents/skills/[SkillName]/agents/openai.yaml
Create or update .claude/skills/[SkillName]/SKILL.md
Update .claude/ecc-tools.json
Update .claude/homunculus/instincts/inherited/[SkillName]-instincts.yaml
Update .claude/identity.json
Update .codex/AGENTS.md
Update .codex/agents/docs-researcher.toml
Update .codex/agents/explorer.toml
Update .codex/agents/reviewer.toml
Update .codex/config.toml
```

### Add Or Update Agent Documentation

Adds or updates agent documentation and command markdown files, often in bulk.

**Frequency**: ~2 times per month

**Steps**:
1. Add or update agents/*.md files
2. Add or update commands/*.md files
3. Optionally add or update assets/images/* for documentation
4. Optionally update tests/* for agent/command validation

**Files typically involved**:
- `agents/*.md`
- `commands/*.md`
- `assets/images/*`
- `tests/*`

**Example commit sequence**:
```
Add or update agents/*.md files
Add or update commands/*.md files
Optionally add or update assets/images/* for documentation
Optionally update tests/* for agent/command validation
```

### Add Or Update Root And Meta Files

Adds or updates top-level project files such as README.md, .vscode configs, and meta files.

**Frequency**: ~2 times per month

**Steps**:
1. Add or update README.md
2. Add or update .vscode/* files
3. Add or update requirements.txt or similar
4. Add or update git or Repo marker files

**Files typically involved**:
- `README.md`
- `.vscode/*`
- `requirements.txt`
- `git`
- `Repo`

**Example commit sequence**:
```
Add or update README.md
Add or update .vscode/* files
Add or update requirements.txt or similar
Add or update git or Repo marker files
```


## Best Practices

Based on analysis of the codebase, follow these practices:

### Do

- Follow *.test.js naming pattern
- Use camelCase for file names
- Prefer mixed exports

### Don't

- Don't skip tests for new features
- Don't deviate from established patterns without discussion

---

*This skill was auto-generated by [ECC Tools](https://ecc.tools). Review and customize as needed for your team.*
