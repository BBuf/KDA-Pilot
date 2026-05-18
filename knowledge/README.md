# KernelPilot Knowledge — Kernel Evidence Acquisition

> **Knowledge cutoff: 2026-05-16.** Merged PR evidence is collected from
> **2024-01-01** through this date, recorded in
> [`data/refresh-cutoff.yaml`](data/refresh-cutoff.yaml).

This knowledge base intentionally avoids synthesized wiki pages, doc summaries,
blog summaries, contest notes, pseudocode, and technique guides. It provides
three peer evidence-acquisition routes with non-overlapping scopes: local PR
diffs for the major kernel frameworks, an external source map for
complementary code samples, and live web/official/upstream source research.

## What's Here

- **3,660 PR pages** under `sources/prs/` for the major kernel frameworks
  (SGLang, vLLM, TensorRT-LLM, PyTorch, FlashAttention, FlashInfer,
  CUTLASS/CuTe, CCCL, Triton, DeepGEMM, ThunderKittens, TileLang, QuACK,
  DeepSeek TileKernels).
- **3,660 PR evidence bundles** under `evidence/pull-bundles/`
- **14 candidate ledgers** under `candidates/`
- **External source map** in `index.json`; this is a repo/topic map for live
  research over the **complementary** code repositories that are not in the
  PR corpus (NVIDIA developer samples, Colfax research kernels, simveit
  micro-tutorials). It is not a local evidence index.
- PR ingestion, materialization, metadata sync, search, source-map clone/search,
  fetch, and validation scripts under `scripts/`
- PR corpus metadata under `data/`

Each PR page points at its evidence bundle via `artifact_dir`. Each bundle
contains `review.diff`, `upstream.json`, `ORIGIN.yaml`, and `source-snapshot/`.

## Three Peer Routes

The agent picks any route, or combines them. The three routes cover
non-overlapping evidence; none is a fallback for the others.

### Route A: Local PR Diffs

The PR route uses local PR pages and materialized PR diffs for the major
kernel frameworks.

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

`index.json` lists the complementary code repositories that Route A's PR
corpus does not cover — NVIDIA developer code samples, Colfax research
kernels, and simveit micro-tutorials. It is a repo/topic map for live
research, not a local evidence index, and is not searched by
`scripts/query.py`.

Use Route B when the question is about a supporting technique
(TMA/swizzle/pipelining/stream-K/persistent kernels/transposes/block-scaled
NVFP4 plumbing) that the PR diffs alone do not fully explain.

Two-step workflow: clone the referenced repos, then grep across the cloned
tree. `search-index-repos.py` errors out if any referenced repo is still
missing, so the clone step is the only gate.

```bash
python3 scripts/clone-index-repos.py
python3 scripts/search-index-repos.py <term1> <term2> <term3>
```

Keep the current kernel context (operator, dtype, architecture, framework) in
the search terms so the matches stay meaningful.

### Route C: Live Web / Official / Upstream

Use live web search, official docs, GitHub PR pages, and upstream repository
search as a peer evidence route. Prefer official docs and upstream source code
over blogs or snippets when implementation details matter.

## Shared Example

For `FlashAttention SM100 SplitKV`, the three routes contribute different
evidence:

```bash
python3 scripts/query.py "flash attention sm100 splitkv" --compact --limit 50
python3 scripts/search-pr-diffs.py SplitKV Sm100 --any --limit 200
python3 scripts/get_page.py pr-flash-attention-1940
```

```bash
python3 scripts/clone-index-repos.py
python3 scripts/search-index-repos.py tma swizzle transpose
python3 scripts/search-index-repos.py stream-k persistent block-scaled
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

- Local synthesized explanations (wiki, doc, blog, contest, pseudocode,
  topic-index) are deliberately excluded; evidence comes from PR pages, cloned
  upstream source, or live upstream/official material.
- Route B searches run after `clone-index-repos.py` finishes the full set; the
  script enforces this.
- Live official docs, upstream source, and web searches stay first-class
  alongside the cached PR corpus rather than being demoted to a fallback.
