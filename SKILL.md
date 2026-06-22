---
name: build-domain-learning-atlas
description: Build a structured learning system for any new domain, including a Markdown knowledge library and an interactive visual knowledge atlas. Use when the user wants to systematically learn, understand, onboard into, map, or study a field; asks for a knowledge framework, terminology, cases, standards, references, assessment checklist, prompt library, or visual knowledge graph; or says they want the same kind of learning artifact previously made for UI.
---

# Build Domain Learning Atlas

Turn an unfamiliar field into a navigable learning system, not a loose collection of notes.

## Confirm The Learning Brief

Infer what is already clear. Ask only when the answer changes the architecture materially:

- Domain and desired outcome.
- Learner level: beginner, practitioner, or advanced.
- Intended use: general understanding, job transition, project execution, exam, or prompting.
- Desired freshness: foundational only or current industry practice.
- Deliverables: Markdown library only, atlas only, or both.

Default to Chinese, beginner-to-practitioner depth, Markdown library plus interactive atlas, and a practical/project-oriented perspective.

## Research Before Structuring

Browse when the domain depends on current tools, standards, laws, market practices, products, or terminology. Prefer primary and authoritative sources.

Separate:

- Stable foundations.
- Current practices and tools.
- Contested opinions or schools.
- Region-specific rules.

Do not fabricate coverage to make the map look complete. Mark uncertainty and source-sensitive claims.

## Build The Knowledge Architecture

Create a small set of substantial documents instead of one enormous file. Adapt the modules to the field, using this default set:

1. Role/domain overview and knowledge architecture.
2. Core terminology and mental models.
3. Workflow, methods, or operating process.
4. Subdomains and realistic case library.
5. Tools, components, standards, or system handbook.
6. Analysis, teardown, or problem-solving method.
7. Reference library and taxonomy/style vocabulary.
8. Quality review, self-assessment, and learning roadmap.

Add a prompt/template library when the user will use AI or vibe coding in the field.

Read [references/document-library-spec.md](references/document-library-spec.md) before creating the Markdown files.

## Write The Markdown Library

Use consistent semantic hierarchy across every file:

- `H1`: document knowledge domain.
- `H2`: major chapter.
- `H3`: concrete topic.
- `H4`: method, rule, or detail.

Use paragraphs for explanations, subheadings for named groups, lists for parallel points, tables for comparisons/glossaries, and fenced blocks for reusable templates.

Numbering such as `3.1` is semantic even if the source Markdown uses `##`; normalize it when building the atlas.

Do not flatten Markdown into plain text. Preserve bold terms, lists, tables, code/template blocks, and hierarchy.

## Validate The Corpus

Run:

```bash
python3 scripts/analyze_markdown_corpus.py <knowledge-directory>
```

Review:

- H1-H4 distribution.
- Empty parent sections.
- Sections containing lists, tables, and fenced blocks.
- Duplicate headings.
- Files with missing H1.

Fix structural problems before building the visualization.

## Build The Interactive Atlas

Use the established orbital knowledge-atlas pattern unless the user requests another visualization:

- Use a NotebookLM-style three-column workspace when AI conversation is a primary workflow.
- Current document at the center.
- H2 as compact persistent navigation labels.
- H3/H4 as orbital nodes with full labels on hover, selection, or search.
- Other documents as outer satellites.
- Cross-document links based on shared concepts.
- File switcher, depth control, zoom/pan, node inspector, and responsive layout.
- Context-aware AI follow-up chat below H3 node content.

Search must be explanatory:

- Search all documents, not only the current canvas.
- Show result count, file, level, and match type.
- Highlight the exact query text.
- Rank exact title, title contains, then body matches.
- Clicking a result switches file, reveals the needed depth, selects the node, and keeps query highlights visible.
- Show an explicit zero-result state.

Read [references/atlas-interaction-spec.md](references/atlas-interaction-spec.md) before implementation.

Use [assets/ui-knowledge-atlas-reference.html](assets/ui-knowledge-atlas-reference.html) only as a behavioral and visual reference. Replace its domain data and do not copy UI-specific learning content into a new field.

## Render Markdown Faithfully

The inspector must support:

- Paragraphs and spacing.
- Group labels as small subheadings.
- Ordered and unordered lists.
- Bold term names and inline code.
- Markdown tables with sticky headers.
- Fenced templates rendered as structured content.
- Empty parent sections rendered as a child-topic outline.
- Long content in an internal scroll region with fixed metadata footer.

Keep H1/H2/H3/H4 metadata and typography consistent across all nodes.

## Add Context-Aware AI Follow-Up

When AI conversation is a primary workflow, use this layout:

- Left: collapsible source/document library.
- Center: largest region for the atlas; show node details as a floating inspector only after selection.
- Right: collapsible persistent AI conversation.

Without a selected node, ground the conversation in the complete knowledge library. With a selected node, switch to focused context containing the current document title, node title, ancestry path, and rendered node content.

- Keep the selected node visible as a removable context indicator above the chat.
- Include concise starter questions such as examples, adjacent concepts, and reusable prompts.
- Start a new conversation when the context changes between the full library and a node, or between nodes.
- Stream answers when the provider supports it and show loading, failure, retry, and empty states.

Use a configurable OpenAI-compatible provider instead of embedding credentials. The generated atlas must never contain an API key. Let each user configure:

- Provider preset or custom provider.
- Complete Chat Completions endpoint.
- Exact model identifier.
- API key.

Treat these values as one connection profile. Do not hardcode the model merely because the API key is user-supplied. Provider presets may fill recommended values, but endpoint and model must remain editable. Label the expected protocol and authentication method, validate missing fields and malformed URLs, and only send provider-specific request parameters when the selected provider supports them.

Store browser-only credentials in `sessionStorage` by default, provide a clear remove action, and explain that the key is sent directly to the configured model provider. For a public or production deployment, recommend a server-side proxy so API keys are not exposed to page scripts.

When DeepSeek V4 is requested, use the current official model identifiers and API format. As of June 2026, the defaults are:

- Base URL: `https://api.deepseek.com`
- Model: `deepseek-v4-pro`
- Faster option: `deepseek-v4-flash`

Verify provider model names against official documentation because they can change.

## Verify And Iterate

Test at least:

- One H1 document overview.
- One empty H2 parent.
- One prose/list H3 topic.
- One H4 detail.
- One glossary table.
- One long fenced template.
- One title search, one body search, one exact search, one cross-file result, and one zero-result query.
- Three-column expanded state, both sidebars collapsed independently, no-selection state, and floating selected-node inspector.
- One full-library chat state, one node-focused chat state, configuration, starter question, streaming response, and API error state.
- Desktop and mobile layouts.

Check screenshots for label collisions, clipped text, inspector overlap, unreadable dimming, and graph controls covering content.

Do not claim completion after checking a single representative node. Corpus-wide consistency is part of the deliverable.

## Deliver

Provide:

- Clickable Markdown files.
- A running local preview URL.
- A self-contained single-file HTML version.
- A concise summary of document count, node count, search behavior, and validation performed.

Keep the dev server running for review when applicable.
