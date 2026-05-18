# KernelPilot Knowledge Schema — Evidence Routes

This directory supports three equal evidence-acquisition routes for GPU kernel
work: local PR diffs, cloned external source-map repositories, and live
web/official/upstream source research. It deliberately does not include local
wiki pages, doc summaries, blog summaries, contest notes, pseudocode, or
generated topic indices.

## Navigation

PR route:

```bash
python3 scripts/query.py "<keywords>" --compact
python3 scripts/search-pr-diffs.py <term1> <term2> [--any]
```

Fetch a selected PR page:

```bash
python3 scripts/get_page.py pr-flash-attention-1940
```

Then inspect the evidence bundle named by `artifact_dir`:

```bash
less evidence/pull-bundles/flash-attention/gh-1940/review.diff
find evidence/pull-bundles/flash-attention/gh-1940/source-snapshot -type f
```

Source-map route:

```bash
python3 scripts/clone-index-repos.py
python3 scripts/search-index-repos.py <term1> <term2> <term3>
```

Live route:

```text
Use web search, official docs, GitHub PR pages, and upstream source search.
```

## Data Shape

- `sources/prs/{repo}/PR-{N}.md` — one metadata page per tracked upstream PR
- `evidence/pull-bundles/{repo}/gh-{N}/review.diff` — materialized PR diff
- `evidence/pull-bundles/{repo}/gh-{N}/source-snapshot/` — changed upstream
  source files captured from the PR
- `evidence/pull-bundles/{repo}/gh-{N}/upstream.json` — upstream PR metadata
- `evidence/pull-bundles/{repo}/gh-{N}/ORIGIN.yaml` — provenance
- `candidates/*.yaml` — PR candidate ledgers
- `data/*.yaml` — PR corpus metadata, aliases, tags, schema, refresh state
- `index.json` — external source map for live repository research; not indexed
  by the local PR query path

## Page Type

Only `source-pr` pages are indexed by the query scripts.

Required fields are defined in `data/schemas.yaml`. The important fields for
retrieval are:

- `repo`
- `pr`
- `title`
- `architectures`
- `tags`
- `techniques`
- `hardware_features`
- `kernel_types`
- `languages`
- `changed_paths`
- `artifact_dir`

## Policy

- MUST NOT treat local knowledge as evidence unless it resolves to a PR page
  and PR evidence bundle.
- The PR, source-map, and live routes are peer evidence routes. The agent may
  choose any route, or combine them.
- MUST NOT search any `index.json` repository until
  `python3 scripts/clone-index-repos.py` has cloned every referenced GitHub
  repository.
- MUST NOT rely on snippets or blogs over official docs and upstream source for
  implementation details.
- MUST NOT write kernels or pivot technical direction from cached local docs,
  wiki pages, blog notes, contests, pseudocode, or generated summaries.

## Validation

```bash
python3 scripts/validate.py
```
