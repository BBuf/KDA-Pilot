# PR Discussion Digest

- Source PR: [vllm-project/vllm#35123](https://github.com/vllm-project/vllm/pull/35123)
- Source page: `sources/prs/vllm/PR-35123.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35123`
- Generated at: `2026-05-20T15:39:58.127110+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-23T18:01:51Z`
- Merged: `2026-02-24T01:11:27Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: robertgshaw2-redhat, stavinsky
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T18:09:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses build failures on unsupported architectures (e.g., SM121) by moving the ops.impl() registrations ... (https://github.com/vllm-project/vllm/pull/35123#pullrequestreview-3842717579)
- `2026-02-23T18:10:45Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/35123#pullrequestreview-3842722104)

## Inline Comment Hotspots

- `csrc/moe/dsv3_router_gemm_entry.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-23T20:51:48Z` `issue` by `stavinsky`; signals: cache, dtype, flashinfer, fp4, fp8, memory, moe, nvfp4; excerpt: "loads fine VLLM USE FLASHINFER MOE FP4=0 vllm serve --host 0.0.0.0 --gpu-memory-utilization 0.4 --load-format fastsafetensors --max-num-seqs 1 --kv-cache-dtype fp8 nvidia/Qwen3-Next-80B-A3B-Instruct-NVFP4 fails on load (i ..." (https://github.com/vllm-project/vllm/pull/35123#issuecomment-3947271314)
