---
name: kernel-knowledge
description: Use when the user asks for upstream evidence about NVIDIA Blackwell/Hopper GPU kernels, CUDA/CuTe/Triton/CUTLASS implementations, FlashAttention, DeepGEMM, FlashInfer, SGLang, vLLM, PyTorch, TensorRT-LLM, CCCL, TileLang, QuACK, ThunderKittens, TileKernels, official docs, or related upstream source code.
argument-hint: "[natural-language-question] | [--repo owner/name --tag foo] | [pr-page-id]"
allowed-tools: "Bash Read Grep Glob"
---

# KernelPilot Kernel Knowledge

This skill provides three equal evidence-acquisition routes:

1. Local PR diff corpus.
2. External source-map repositories from `index.json`.
3. Live web search, official docs, and related upstream source code.

The agent may choose any route, or combine them. None of the three routes is a
fallback for the others. Whichever route is chosen, search comprehensively before
drawing a conclusion.

## Route A: Local PR Diffs

The PR route searches the whole local PR corpus. Do not start by narrowing to a
single familiar repo. First run a corpus-wide search across all PR pages and/or
all materialized `review.diff` files.

```bash
python3 scripts/query.py "flash attention sm100 splitkv" --compact --limit 50
python3 scripts/search-pr-diffs.py SplitKV Sm100 --any --limit 200
```

Then fetch and inspect relevant PR pages and bundles:

```bash
python3 scripts/get_page.py pr-flash-attention-1940
less evidence/pull-bundles/flash-attention/gh-1940/review.diff
find evidence/pull-bundles/flash-attention/gh-1940/source-snapshot -type f
```

## Route B: External Source Map

`index.json` is a source-map reference for live source research. It is not a
local summary index. It contains repositories, kernel paths, tags, and topic
routing hints.

Before searching repositories listed in `index.json`, clone the full referenced
GitHub repo set:

```bash
python3 scripts/clone-index-repos.py
```

MUST NOT start searching any `index.json` repository before the full clone step
has completed. After that, search the cloned repositories one by one. Use the
current kernel's operator, dtype, architecture, and framework context.

```bash
python3 scripts/search-index-repos.py SplitKV Sm100 flash_fwd_sm100
```

## Route C: Live Web / Official / Upstream

Use live web search, official docs, GitHub PR pages, and upstream repository
search as a peer evidence route. Prefer official docs and upstream code over
blogs or snippets when implementation details matter.

For the same example kernel, useful live searches include:

```text
FlashAttention Sm100 SplitKV PR
Dao-AILab flash-attention flash_fwd_sm100 SplitKV
CUTLASS Blackwell FMHA SplitKV Sm100
```

Record URLs, commit SHAs, source paths, and license/notice details when the
source directly affects code.

## Shared Example

For `FlashAttention SM100 SplitKV`, all three routes are valid:

- PR route: `query.py "flash attention sm100 splitkv"` should surface
  `pr-flash-attention-1940`; inspect its `review.diff` and
  `source-snapshot/`.
- Source route: clone the full `index.json` repo set, then search all cloned
  repositories for `SplitKV`, `Sm100`, and `flash_fwd_sm100`.
- Web route: search GitHub/web for the upstream FlashAttention PR, current
  upstream source, and any official docs needed to understand architecture
  constraints.

## Answer Contract

When using this skill:

1. State which route or routes were used.
2. For PR evidence, cite PR page IDs, paths, and `artifact_dir` bundles.
3. For source-map evidence, confirm the full clone step completed before repo
   search, then cite repo paths and source files.
4. For web/upstream evidence, cite URLs, commits, source paths, or doc pages.
5. Do not quote or rely on removed local wiki/doc/blog/contest material.
6. If a route finds no relevant evidence, say so explicitly; do not turn a weak
   match into a technical route.

## Validate

```bash
python3 scripts/validate.py
```
