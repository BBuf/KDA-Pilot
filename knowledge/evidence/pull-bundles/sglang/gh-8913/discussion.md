# PR Discussion Digest

- Source PR: [sgl-project/sglang#8913](https://github.com/sgl-project/sglang/pull/8913)
- Source page: `sources/prs/sglang/PR-8913.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8913`
- Generated at: `2026-05-20T15:31:30.297663+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-07T13:24:03Z`
- Merged: `2025-08-14T17:55:54Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 17 (approved=1, commented=16)
- Inline review comments: 20
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=2
- Human participants with discussion text: BBuf, HydraQYH, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-07T13:24:27Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3097159088)
- `2025-08-07T13:25:59Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the FP8 blockwise GEMM for SM90 architectures by introducing a more modular ... (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3097165347)
- `2025-08-11T02:06:46Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3103861055)
- `2025-08-11T02:09:01Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3103862427)
- `2025-08-11T03:32:27Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3103918311)
- `2025-08-11T03:32:43Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3103918509)
- `2025-08-11T05:48:29Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3104114749)
- `2025-08-11T07:24:29Z` `APPROVED` by `BBuf` - LGTM. (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3104352083)
- `2025-08-11T13:47:32Z` `COMMENTED` by `HydraQYH` - Great Job. Could you please respond to the comments I made above? (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3105927814)
- `2025-08-12T01:57:27Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108305743)
- `2025-08-12T01:58:36Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108308268)
- `2025-08-12T01:59:22Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108309612)
- `2025-08-12T02:01:12Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108313043)
- `2025-08-12T04:21:23Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108488973)
- `2025-08-12T04:22:17Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108489956)
- `2025-08-12T04:28:01Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108496551)
- `2025-08-12T04:28:31Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8913#pullrequestreview-3108497085)

## Inline Comment Hotspots

- `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`: 14 inline comment(s)
- `sgl-kernel/csrc/gemm/fp8_blockwise_gemm_kernel.cu`: 3 inline comment(s)
- `sgl-kernel/csrc/cutlass_extensions/gemm/cutlass_gemm_caller.cuh`: 2 inline comment(s)
- `sgl-kernel/csrc/cutlass_extensions/common.hpp`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-11T13:44:32Z` `inline` by `HydraQYH` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:71; signals: block, cutlass, fp8, gemm, h100, h200, kernel, perf; excerpt: "Have you compared the performance of Cooperative and Pingpong on H100/H200/H800/H20? Are you considering choosing different strategies based on different GPUs in the future?" (https://github.com/sgl-project/sglang/pull/8913#discussion_r2266823766)
- `2025-08-11T03:32:27Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:30; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Yes, we'd better keep 3x intact since it is a 3x wrapper. There can be a cutlass 2x wrapper for sm89 later on." (https://github.com/sgl-project/sglang/pull/8913#discussion_r2265605811)
- `2025-08-11T02:06:46Z` `inline` by `BBuf` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:30; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Should we need 3x here ?" (https://github.com/sgl-project/sglang/pull/8913#discussion_r2265554029)
- `2025-08-11T13:36:18Z` `inline` by `HydraQYH` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:36; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Just curious. Is this for scenarios where GroupSizeM 1?" (https://github.com/sgl-project/sglang/pull/8913#discussion_r2266800222)
- `2025-08-11T13:46:28Z` `inline` by `HydraQYH` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:189; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Why use a heuristic strategy? Is there any code reference?" (https://github.com/sgl-project/sglang/pull/8913#discussion_r2266829043)
- `2025-08-12T01:58:36Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:36; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "GroupSizeM can be 1." (https://github.com/sgl-project/sglang/pull/8913#discussion_r2268393536)
- `2025-08-12T01:59:21Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:71; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Not yet, but it is on our future plan." (https://github.com/sgl-project/sglang/pull/8913#discussion_r2268394381)
- `2025-08-12T02:01:11Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:189; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "It is refer to" (https://github.com/sgl-project/sglang/pull/8913#discussion_r2268396289)
- `2025-08-12T04:21:23Z` `inline` by `HydraQYH` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:189; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Get!" (https://github.com/sgl-project/sglang/pull/8913#discussion_r2268538860)
- `2025-08-12T04:22:17Z` `inline` by `HydraQYH` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:36; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Are there scenarios where GroupSizeM 1?" (https://github.com/sgl-project/sglang/pull/8913#discussion_r2268539775)
- `2025-08-12T04:28:01Z` `inline` by `HydraQYH` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:36; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Reply: For swap AB." (https://github.com/sgl-project/sglang/pull/8913#discussion_r2268545581)
- `2025-08-12T04:28:31Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_blockwise_gemm_sm90_dispatch.cuh`:36; signals: block, cutlass, fp8, gemm, kernel, sm90; excerpt: "In case swap ab, GroupSizeM 1. In the next step, we will introduce swap ab." (https://github.com/sgl-project/sglang/pull/8913#discussion_r2268546063)
