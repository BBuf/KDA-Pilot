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
fallback for the others. The agent MUST NOT draw conclusions from a chosen
route before broad search evidence for that route exists.

## Route A: Local PR Diffs

The PR route searches the whole local PR corpus. The agent MUST NOT treat a PR
match as sufficient until corpus-wide search across all PR pages and/or all
materialized `review.diff` files has been attempted.

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

Clone command for the full referenced GitHub repo set:

```bash
python3 scripts/clone-index-repos.py
```

MUST NOT start searching any `index.json` repository before the full clone step
has completed. MUST NOT ignore the current kernel's operator, dtype,
architecture, or framework context during source-map searches.

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

MUST NOT let external-source-influenced code lack URLs, commit SHAs, source
paths, and license/notice details.

## Shared Example

For `FlashAttention SM100 SplitKV`, all three routes are valid:

- PR route example: `query.py "flash attention sm100 splitkv"` surfaces
  `pr-flash-attention-1940`; its `review.diff` and `source-snapshot/` contain
  the implementation evidence.
- Source route example: after the full `index.json` clone step, search terms
  such as `SplitKV`, `Sm100`, and `flash_fwd_sm100` apply across the cloned
  repo set.
- Web route example: GitHub/web searches can find the upstream FlashAttention
  PR/page, current upstream source, and official docs for architecture
  constraints.

## Answer Contract

When using this skill:

1. MUST NOT leave route selection ambiguous; name which route or routes were
   used.
2. MUST NOT cite PR evidence without PR page IDs, paths, and `artifact_dir`
   bundles.
3. MUST NOT cite source-map evidence without recording that the full clone step
   completed before repo search, plus repo paths and source files.
4. MUST NOT cite web/upstream evidence without URLs, commits, source paths, or
   doc pages.
5. MUST NOT quote or rely on removed local wiki/doc/blog/contest material.
6. MUST NOT turn a weak match or no-match result into a technical route.

## Validate

```bash
python3 scripts/validate.py
```
