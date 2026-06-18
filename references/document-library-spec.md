# Document Library Specification

## Contents

1. Architecture rules
2. Recommended modules
3. Writing patterns
4. Quality gates

## Architecture Rules

- Give each file one clear learning responsibility.
- Prefer 6-10 files with 300-1000 useful lines each over dozens of fragments.
- Keep terminology consistent across files.
- Introduce concepts before methods, methods before cases, and cases before evaluation.
- Cross-link related ideas conceptually; avoid duplicating whole sections.
- Use realistic examples that match the learner's intended application.

## Recommended Modules

### Domain Overview

Explain scope, adjacent disciplines, major outcomes, foundational mental models, workflow, capability map, and learning path.

### Terminology

Organize terms by category. Use tables for `term | meaning | when used | common mistake` when useful.

### Workflow And Methods

Describe inputs, decisions, outputs, roles, checkpoints, failure modes, and examples.

### Cases

Cover representative contexts, not cosmetic variations. Each case should include background, goal, constraints, method, expected output, and review criteria.

### Standards And Systems

Cover reusable primitives, conventions, state/variant completeness, accessibility/safety requirements, and consistency rules.

### Analysis Method

Give a repeatable teardown or diagnostic process that converts observations into professional language and actionable prompts.

### Reference Library

Provide categories, tags, selection criteria, useful vocabulary, combinations, and anti-pattern terms.

### Review And Roadmap

Include quick checks, detailed scoring, domain-specific checks, final-delivery checks, and staged practice.

### Prompt Library

When relevant, include universal scaffolds, domain variants, complete examples, negative constraints, and self-review prompts.

## Writing Patterns

- Opening paragraph: explain why the topic matters.
- Named group: use a short line ending in `：` or a heading.
- Parallel items: use a list.
- Comparisons and glossaries: use a table.
- Reusable input: use a fenced block.
- Terminology items: bold the term before the explanation.
- Parent topic without prose: list child topics instead of writing generic filler.

## Quality Gates

- Every file has exactly one H1.
- Numbering and semantic heading level agree.
- No accidental duplicate chapter titles within one file.
- Lists are not flattened into paragraphs.
- Tables remain valid Markdown tables.
- Fenced blocks open and close correctly.
- Long templates are complete, not arbitrarily truncated.
- Each module contains practical examples or application guidance.
