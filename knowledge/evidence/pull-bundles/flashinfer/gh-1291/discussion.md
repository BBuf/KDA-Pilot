# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1291](https://github.com/flashinfer-ai/flashinfer/pull/1291)
- Source page: `sources/prs/flashinfer/PR-1291.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1291`
- Generated at: `2026-05-20T15:22:10.145165+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-19T03:17:14Z`
- Merged: `2025-07-22T17:26:26Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: wenscarl, yzh119
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-19T03:17:31Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @wenscarl, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1291#pullrequestreview-3035102905)
- `2025-07-19T03:18:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request removes the FAST BUILD flag for the MoE kernels, which will enable a ... (https://github.com/flashinfer-ai/flashinfer/pull/1291#pullrequestreview-3035103198)
- `2025-07-19T19:22:49Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1291#pullrequestreview-3035513595)
- `2025-07-21T18:03:48Z` `COMMENTED` by `wenscarl` (https://github.com/flashinfer-ai/flashinfer/pull/1291#pullrequestreview-3039170179)
- `2025-07-21T19:22:00Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1291#pullrequestreview-3039398472)
- `2025-07-22T17:26:16Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1291#pullrequestreview-3044086968)

## Inline Comment Hotspots

- `csrc/nv_internal/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/gemm_configs.h`: 2 inline comment(s)
- `flashinfer/fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-19T19:22:49Z` `inline` by `yzh119` `csrc/nv_internal/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/gemm_configs.h`:103; signals: cutlass, gemm, hang, tensorrt, tile; excerpt: "From my understanding this changes cta tile size from (256, 128) to (256, 256), what motivates this change, and why not keeping both?" (https://github.com/flashinfer-ai/flashinfer/pull/1291#discussion_r2217425359)
- `2025-07-21T18:03:47Z` `inline` by `wenscarl` `csrc/nv_internal/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/gemm_configs.h`:103; signals: cutlass, gemm, tensorrt; excerpt: "Yes, I think it's just the old comment was wrong. Both of them kept." (https://github.com/flashinfer-ai/flashinfer/pull/1291#discussion_r2219898328)
- `2025-07-21T19:22:00Z` `inline` by `yzh119` `flashinfer/fused_moe.py`:281; signals: flashinfer, moe, sm100; excerpt: "could it be an argument in gen fused moe sm100 module:" (https://github.com/flashinfer-ai/flashinfer/pull/1291#discussion_r2220052435)
