---
name: kernel-knowledge
description: Use when the user asks for concrete upstream PR evidence about NVIDIA Blackwell/Hopper GPU kernels, CUDA/CuTe/Triton/CUTLASS implementations, FlashAttention, DeepGEMM, FlashInfer, SGLang, vLLM, PyTorch, TensorRT-LLM, CCCL, TileLang, QuACK, ThunderKittens, or TileKernels.
argument-hint: "[natural-language-question] | [--repo owner/name --tag foo] | [pr-page-id]"
allowed-tools: "Bash Read Grep Glob"
---

# KernelPilot Kernel Knowledge

This skill searches a PR-diff-only evidence base. It intentionally has no local
wiki, blog, doc, contest, pseudocode, or technique-guide layer.

## Rule

Use local knowledge only to find upstream PR pages and their materialized
evidence bundles. If no relevant PR evidence exists, say so and continue with
live research. Do not synthesize a kernel route from local cached docs, wiki
pages, blog notes, or pseudocode.

## Query

Run from this directory:

```bash
python3 scripts/query.py "flash attention sm100 splitkv" --compact
python3 scripts/query.py "tcgen05 tmem" --architecture B200 --compact
python3 scripts/query.py --repo Dao-AILab/flash-attention --kernel-type attention --compact
python3 scripts/query.py --tag nvfp4 --language cute-dsl --limit 20
```

Filters:

- `--repo`
- `--tag`
- `--architecture`
- `--language`
- `--kernel-type`
- `--limit`
- `--compact`
- `--paths-only`

Aliases are still supported, for example `B200 -> sm100`.

## Fetch

```bash
python3 scripts/get_page.py pr-flash-attention-1940
python3 scripts/get_page.py sources/prs/flash-attention/PR-1940.md
```

Then inspect the referenced bundle:

```bash
less evidence/pull-bundles/flash-attention/gh-1940/review.diff
find evidence/pull-bundles/flash-attention/gh-1940/source-snapshot -type f
```

## External Source Map

`index.json` is a source-map reference for live research. It is not part of the
local PR query index.

Before searching repositories listed in `index.json`, clone the full referenced
GitHub repo set:

```bash
python3 scripts/clone-index-repos.py
```

MUST NOT start searching any `index.json` repository before the full clone step
has completed. After that, search the cloned repositories one by one for code
implementations or upstream docs related to the current kernel.

## Answer Contract

When using this KB:

1. Cite PR page IDs and paths.
2. Cite the `artifact_dir` bundle.
3. Treat `review.diff` and `source-snapshot/` as the only local implementation
   evidence.
4. If the local PR corpus has no match, report that and use live web search,
   official docs, or related upstream source code search.
5. Do not quote or rely on removed local wiki/doc/blog/contest material.

## Validate

```bash
python3 scripts/validate.py
```
