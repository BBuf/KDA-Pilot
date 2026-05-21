# KernelPilot Knowledge Schema — Evidence Routes

This directory supports three peer evidence-acquisition routes for GPU kernel
work with non-overlapping scopes:

- Route A: local PR diffs for the major kernel frameworks (SGLang, vLLM,
  TensorRT-LLM, PyTorch, FlashAttention, FlashInfer, CUTLASS/CuTe, CCCL,
  Triton, DeepGEMM, ThunderKittens, TileLang, QuACK, DeepSeek TileKernels).
- Route B: cloned complementary repositories not covered by Route A's PR
  corpus (NVIDIA developer samples, Colfax research kernels, simveit
  micro-tutorials).
- Route C: live web/official/upstream source research.

It deliberately does not include local wiki pages, doc summaries, blog
summaries, contest notes, pseudocode, or generated topic indices.

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
- `evidence/pull-bundles/{repo}/gh-{N}/discussion.md` — optional plain
  bullet list of useful human review/comment points from the submission-to-merge
  window
- `evidence/pull-bundles/{repo}/gh-{N}/source-snapshot/` — changed upstream
  source files captured from the PR
- `evidence/pull-bundles/{repo}/gh-{N}/upstream.json` — upstream PR metadata
- `evidence/pull-bundles/{repo}/gh-{N}/ORIGIN.yaml` — provenance
- `candidates/*.yaml` — PR candidate ledgers
- `data/*.yaml` — PR corpus metadata, aliases, tags, schema, refresh state
- `index.json` — external source map for live repository research over the
  complementary code repositories not in the PR corpus; not indexed by the
  local PR query path

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

## Working Rules

- Treat the PR, source-map, and live routes as peer evidence routes; pick one
  or combine them.
- Local evidence counts only when it resolves to a PR page and the matching
  evidence bundle.
- Route B searches run after `clone-index-repos.py` finishes the full set; the
  script enforces this.
- For implementation details, prefer official docs and upstream source over
  blog snippets.
- Kernel writes and direction changes rest on the three live routes, not on
  cached wiki/doc/blog/contest/pseudocode/topic-index material.

## Validation

```bash
python3 scripts/validate.py
```
