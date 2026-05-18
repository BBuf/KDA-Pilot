# KernelPilot Knowledge — Kernel Evidence Acquisition

> **Knowledge cutoff: 2026-05-16.** Merged PR evidence is collected from
> **2024-01-01** through this date, recorded in
> [`data/refresh-cutoff.yaml`](data/refresh-cutoff.yaml).

This knowledge base intentionally avoids synthesized wiki pages, doc summaries,
blog summaries, contest notes, pseudocode, and technique guides. It provides
three equal evidence-acquisition routes: local PR diffs, external source-map
repositories, and live web/official/upstream source research.

## What's Here

- **3,660 PR pages** under `sources/prs/`
- **3,660 PR evidence bundles** under `evidence/pull-bundles/`
- **14 candidate ledgers** under `candidates/`
- **External source map** in `index.json`; this is a repo/topic map for live
  research, not a local evidence index.
- PR ingestion, materialization, metadata sync, search, source-map clone/search,
  fetch, and validation scripts under `scripts/`
- PR corpus metadata under `data/`

Each PR page points at its evidence bundle via `artifact_dir`. Each bundle
contains `review.diff`, `upstream.json`, `ORIGIN.yaml`, and `source-snapshot/`.

## Three Equal Routes

The agent may choose any route, or combine routes. None is a fallback for the
others.

### Route A: Local PR Diffs

The agent MUST NOT start by narrowing to one familiar repo. It MUST NOT treat a
PR match as sufficient until broad search across all local PR pages or all
materialized PR diffs has been attempted.

```bash
python3 scripts/query.py "<keywords>" [--repo owner/name] [--tag tag] [--architecture sm100] [--language cute-dsl] [--kernel-type attention] --compact
python3 scripts/search-pr-diffs.py <term1> <term2> [--any]
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

### Route B: External Source Map

`index.json` lists upstream repositories and topic-to-repository routing hints
that can help live research. It intentionally has no `ncu_signals` fields and is
not searched by `scripts/query.py`.

Clone command for every GitHub repository referenced by `index.json`:

```bash
python3 scripts/clone-index-repos.py
```

MUST NOT begin searching the referenced repositories until that command has
finished successfully for the full set. MUST NOT treat one cloned repository as
representative of the source-map route. MUST NOT ignore the current kernel's
operator, dtype, architecture, or framework context during source-map searches.

```bash
python3 scripts/search-index-repos.py <term1> <term2> <term3>
```

### Route C: Live Web / Official / Upstream

Use live web search, official docs, GitHub PR pages, and upstream repository
search as a peer evidence route. Prefer official docs and upstream source code
over blogs or snippets when implementation details matter.

## Shared Example

For `FlashAttention SM100 SplitKV`, all three routes are valid:

```bash
python3 scripts/query.py "flash attention sm100 splitkv" --compact --limit 50
python3 scripts/search-pr-diffs.py SplitKV Sm100 --any --limit 200
python3 scripts/get_page.py pr-flash-attention-1940
```

```bash
python3 scripts/clone-index-repos.py
python3 scripts/search-index-repos.py SplitKV Sm100 flash_fwd_sm100
```

Useful live searches:

```text
FlashAttention Sm100 SplitKV PR
Dao-AILab flash-attention flash_fwd_sm100 SplitKV
CUTLASS Blackwell FMHA SplitKV Sm100
```

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

## Layout

```text
knowledge/
|-- SKILL.md
|-- README.md
|-- CLAUDE.md
|-- requirements.txt
|-- scripts/
|   |-- query.py
|   |-- search-pr-diffs.py
|   |-- get_page.py
|   |-- validate.py
|   |-- fetch-pr-evidence.py
|   |-- generate-pr-pages.py
|   |-- materialize-source-prs.py
|   |-- expand-pr-corpus.py
|   |-- sync-pr-evidence-metadata.py
|   |-- clone-index-repos.py
|   `-- search-index-repos.py
|-- sources/
|   `-- prs/
|-- evidence/
|   `-- pull-bundles/
|-- candidates/
|-- index.json
`-- data/
```

## Scope Rules

- Local synthesized explanations are deliberately excluded.
- MUST NOT narrow PR-route research to one repo before whole-corpus PR search
  has been attempted.
- MUST NOT search source-map repositories before every referenced repo has been
  cloned.
- MUST NOT replace live official docs, related upstream source code, or web
  searches with cached local knowledge pages.
