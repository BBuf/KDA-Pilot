# KernelPilot Knowledge — PR Diff Evidence Only

> **Knowledge cutoff: 2026-05-16.** Merged PR evidence is collected from
> **2024-01-01** through this date, recorded in
> [`data/refresh-cutoff.yaml`](data/refresh-cutoff.yaml).

This knowledge base is intentionally narrow: it contains upstream PR evidence
and the local tooling needed to search, fetch, refresh, and validate that
evidence. It does not contain synthesized wiki pages, doc summaries, blog
summaries, contest notes, pseudocode, or technique guides.

## What's Here

- **3,660 PR pages** under `sources/prs/`
- **3,660 PR evidence bundles** under `evidence/pull-bundles/`
- **14 candidate ledgers** under `candidates/`
- PR ingestion, materialization, metadata sync, search, fetch, and validation
  scripts under `scripts/`
- PR corpus metadata under `data/`

Each PR page points at its evidence bundle via `artifact_dir`. Each bundle
contains `review.diff`, `upstream.json`, `ORIGIN.yaml`, and `source-snapshot/`.

## Query Rule

There is one local discovery path:

```bash
python3 scripts/query.py "<keywords>" [--repo owner/name] [--tag tag] [--architecture sm100] [--language cute-dsl] [--kernel-type attention] --compact
```

Then fetch a result:

```bash
python3 scripts/get_page.py pr-flash-attention-1940
```

Open the bundle named by `artifact_dir` when implementation details matter:

```bash
less evidence/pull-bundles/flash-attention/gh-1940/review.diff
find evidence/pull-bundles/flash-attention/gh-1940/source-snapshot -type f
```

If no relevant local PR evidence exists, say that plainly. Do not infer from a
local wiki/doc/blog fallback. Use live web search, official docs, related
upstream source code, or fresh code search as needed.

## Maintenance

```bash
pip install -r requirements.txt
python3 scripts/validate.py
```

Useful PR-corpus tooling:

- `scripts/expand-pr-corpus.py`
- `scripts/generate-pr-pages.py`
- `scripts/fetch-pr-evidence.py`
- `scripts/materialize-source-prs.py`
- `scripts/sync-pr-evidence-metadata.py`
- `scripts/refresh_candidate_ledger.py`

## Layout

```text
knowledge/
|-- SKILL.md
|-- README.md
|-- CLAUDE.md
|-- requirements.txt
|-- scripts/
|   |-- query.py
|   |-- get_page.py
|   |-- validate.py
|   |-- fetch-pr-evidence.py
|   |-- generate-pr-pages.py
|   |-- materialize-source-prs.py
|   |-- expand-pr-corpus.py
|   |-- refresh_candidate_ledger.py
|   `-- sync-pr-evidence-metadata.py
|-- sources/
|   `-- prs/
|-- evidence/
|   `-- pull-bundles/
|-- candidates/
`-- data/
```

## Scope Rules

- PR diff and materialized source snapshots are the only local knowledge
  evidence.
- Local synthesized explanations are deliberately excluded.
- A missing local PR match is acceptable; do not force a weak match.
- Official docs, related upstream source code, and web searches should be
  fetched live when needed instead of cached locally as knowledge pages.
