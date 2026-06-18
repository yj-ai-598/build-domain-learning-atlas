# Atlas Interaction Specification

## Contents

1. Information model
2. Visual hierarchy
3. Search behavior
4. Inspector rendering
5. Responsive behavior
6. QA matrix

## Information Model

- Document: one Markdown file.
- Node: one semantic H1-H4 heading.
- Parent edge: heading ancestry.
- Cross-document edge: shared concept, method, tool, standard, audience, or quality criterion.
- Match: title-exact, title-contains, or body-contains.

Parse numbered headings semantically:

- `1.` -> H2 chapter.
- `1.1` -> H3 topic.
- `1.1.1` -> H4 detail.

## Visual Hierarchy

- H1: central hub with document title.
- H2: compact persistent one-line navigation tag. Show short index and truncated title. Use minimal surface area and no default border.
- H3: medium solid orbital node. Show a full two-line information flag only on hover, selection, or match focus.
- H4: small outlined orbital node. Use the same interactive flag pattern as H3 but identify it as H4.
- Related document: outer outlined satellite using the document's category color.

Keep H2 and H3 visually distinct. H2 is navigation chrome; H3 is contextual information.

Reserve the right-side inspector region when positioning canvas labels. Labels must not sit underneath the inspector.

## Search Behavior

Search the complete corpus.

Rank:

1. Title exactly equals query after normalization.
2. Number-stripped title exactly equals query.
3. Title contains query.
4. Body contains query.

Result row must show:

- Highlighted title.
- Document name and color.
- H level and semantic label.
- Title or body match.

Canvas behavior:

- Dim nonmatching nodes strongly enough to be obvious.
- Give matching nodes a visible ring.
- Keep selected result emphasized after closing the result panel.
- Preserve the query so the inspector title and breadcrumb remain highlighted.

Zero-result state must say no results and suggest shorter example terms.

## Inspector Rendering

Use a stable order:

1. Level metadata.
2. Node title.
3. Breadcrumb.
4. Structured content.
5. Source line and child count.

Render:

- Standalone `Label:` lines as subheadings.
- Bullet and numbered lists as lists.
- `Term: explanation` with a bold term.
- Markdown tables as tables.
- Fenced prompt templates as structured groups.
- Empty parents as child outlines.

## Responsive Behavior

- Close the file sidebar by default below 720px.
- Reduce persistent graph labels on small screens.
- Keep search results within the viewport.
- Place inspector above depth controls.
- Preserve minimum touch targets for controls.
- Never allow controls or text to overlap incoherently.

## QA Matrix

| Surface | Required checks |
|---|---|
| Corpus | headings, empty parents, lists, tables, fences, duplicates |
| Graph | all levels, satellites, labels, overlap, pan/zoom |
| Search | exact, contains, body, cross-file, zero results |
| Inspector | prose, list, glossary table, long template, empty parent |
| Responsive | desktop, narrow desktop, mobile |
| Delivery | running preview, production build, self-contained HTML |
