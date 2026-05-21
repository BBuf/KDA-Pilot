---
name: kernel-knowledge
description: Use when the user asks for upstream evidence about NVIDIA Blackwell/Hopper GPU kernels, CUDA/CuTe/Triton/CUTLASS implementations, FlashAttention, DeepGEMM, FlashInfer, SGLang, vLLM, PyTorch, TensorRT-LLM, CCCL, TileLang, QuACK, ThunderKittens, TileKernels, official docs, or related upstream source code.
argument-hint: "[natural-language-question] | [--repo owner/name --tag foo] | [pr-page-id]"
allowed-tools: "Bash Read Grep Glob"
---

# KernelPilot Kernel Knowledge

This skill turns kernel research questions into citable evidence through three
peer routes with non-overlapping scopes. Pick one, or combine them.

- **Route A — Local PR diffs.** Materialized merged-PR pages and review diffs
  for ~3.8k upstream GPU kernel PRs across SGLang, vLLM, TensorRT-LLM,
  PyTorch, FlashAttention, FlashInfer, CUTLASS/CuTe, CCCL, Triton, DeepGEMM,
  ThunderKittens, TileLang, QuACK, DeepSeek TileKernels. PR bundles may also
  include `discussion.md` when there was useful human review/comment signal.
- **Route B — External source map.** `index.json` lists complementary code
  repositories that have no curated PR diffs in Route A: NVIDIA developer
  code samples, Colfax research kernels, simveit micro-tutorials. The agent
  clones them locally to grep live source.
- **Route C — Live web / official / upstream.** Web search, official docs,
  GitHub PR pages, and upstream source code consulted online.

## Route A: Local PR Diffs

Use Route A to answer "has someone shipped this kernel/feature/fix upstream?"
or "what does a real PR-grade implementation look like?".

```bash
python3 scripts/query.py "<keywords>" --compact --limit 50
python3 scripts/search-pr-diffs.py <term1> <term2> [--any] [--limit 200]
python3 scripts/get_page.py pr-flash-attention-1940
less evidence/pull-bundles/flash-attention/gh-1940/review.diff
find evidence/pull-bundles/flash-attention/gh-1940/source-snapshot -type f
```

`query.py` filters by `--type`, `--tag`, `--repo`, `--language`,
`--architecture`, `--kernel-type`, `--symptom`, and `--confidence`. Combine
filters to keep results scoped to the current kernel context.

Open the bundle named by `artifact_dir` before borrowing any idea: the
implementation evidence lives in `review.diff`, `source-snapshot/`,
`upstream.json`, and `ORIGIN.yaml`; `discussion.md` is an optional plain
bullet list of useful review/comment points when such discussion exists.

## Route B: External Source Map

`index.json` lists the complementary repositories not covered by Route A's PR
corpus — NVIDIA developer samples, Colfax research kernels, simveit
micro-tutorials. Use Route B when the question is about a supporting
technique (TMA/swizzle/pipelining/stream-K/persistent kernels/transposes/
block-scaled NVFP4 plumbing) that the PR diffs alone do not fully explain.

To use it, clone the referenced repos first, then grep across the cloned
tree:

```bash
python3 scripts/clone-index-repos.py
python3 scripts/search-index-repos.py <term1> <term2> [<term3>]
```

`search-index-repos.py` exits with a clear error if any referenced repo is
still missing, so the clone step is the only gate. Keep the current kernel
context (operator, dtype, architecture, framework) in the search terms so the
match set stays meaningful.

## Route C: Live Web / Official / Upstream

Use live web search, official docs, GitHub PR pages, and current upstream
source as a peer evidence route. When implementation details matter, lean on
official docs and upstream code over blogs or snippets.

For the same example kernel, useful live searches include:

```text
FlashAttention Sm100 SplitKV PR
Dao-AILab flash-attention flash_fwd_sm100 SplitKV
CUTLASS Blackwell FMHA SplitKV Sm100
```

When external-route findings shape the kernel, record URLs, commit SHAs,
source paths, and license/notice details with the change.

## Shared Example

For `FlashAttention SM100 SplitKV` all three routes contribute different
evidence:

- **Route A:** `query.py "flash attention sm100 splitkv"` surfaces
  `pr-flash-attention-1940`; the matching `review.diff` and `source-snapshot/`
  hold the implementation.
- **Route B:** after `clone-index-repos.py`, grep the Colfax/simveit/NVIDIA
  sample repos for supporting techniques such as `tma`, `swizzle`,
  `pipeline`, `stream-k`, or `block-scaled` plumbing that the PR diff alone
  does not explain.
- **Route C:** find the upstream FlashAttention PR/page, current upstream
  source, and architecture-level docs.

## Citation Checklist

Use the same shape for every finding, regardless of route:

- Name the route(s) used.
- **Route A:** PR page ID, page path under `sources/prs/`, `artifact_dir`, and
  the specific `source-snapshot/` files that informed the kernel.
- **Route B:** confirm `clone-index-repos.py` completed, list the cloned repo
  paths searched, and the matched source files.
- **Route C:** URLs, commit SHAs or version tags, source paths, and any
  license/notice text required when the code is reused.
- If a route returns a thin or empty match, widen the search inside that route
  or cross-check against another route before treating it as a finding.

The local corpus deliberately excludes wiki, doc, blog, contest, pseudocode,
and topic-index summaries; evidence comes from PR pages, cloned upstream
source, or live upstream/official material.

## Validate

```bash
python3 scripts/validate.py
```
