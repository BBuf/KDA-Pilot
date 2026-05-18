# KernelPilot Knowledge Schema — PR Diff Evidence Only

This directory is a PR evidence index for GPU kernel work. It deliberately does
not include local wiki pages, doc summaries, blog summaries, contest notes,
pseudocode, or generated topic indices.

## Navigation

Use one discovery command:

```bash
python3 scripts/query.py "<keywords>" --compact
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

## Data Shape

- `sources/prs/{repo}/PR-{N}.md` — one metadata page per tracked upstream PR
- `evidence/pull-bundles/{repo}/gh-{N}/review.diff` — materialized PR diff
- `evidence/pull-bundles/{repo}/gh-{N}/source-snapshot/` — changed upstream
  source files captured from the PR
- `evidence/pull-bundles/{repo}/gh-{N}/upstream.json` — upstream PR metadata
- `evidence/pull-bundles/{repo}/gh-{N}/ORIGIN.yaml` — provenance
- `candidates/*.yaml` — PR candidate ledgers
- `data/*.yaml` — PR corpus metadata, aliases, tags, schema, refresh state

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

- Local knowledge must resolve to a PR page and PR evidence bundle.
- A missing local PR match is not a failure. Do not force-fit weak evidence.
- Use live web search, official docs, related upstream source code, or fresh
  code search when the PR corpus does not cover the question.
- Do not write kernels or pivot technical direction from cached local docs,
  wiki pages, blog notes, contests, pseudocode, or generated summaries.

## Validation

```bash
python3 scripts/validate.py
```
