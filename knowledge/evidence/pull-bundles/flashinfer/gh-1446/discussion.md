# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1446](https://github.com/flashinfer-ai/flashinfer/pull/1446)
- Source page: `sources/prs/flashinfer/PR-1446.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1446`
- Generated at: `2026-05-20T15:22:40.264684+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-10T17:45:11Z`
- Merged: `2025-08-13T07:24:51Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 15
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=9, outdated=14
- Human participants with discussion text: IwakuraRein, cyx-6, nvpohanh, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-08-10T17:45:39Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yongwww, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1446#pullrequestreview-3103699466)
- `2025-08-10T17:48:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the codebase to remove the dependency on the getEnvEnablePDL function, replacing it ... (https://github.com/flashinfer-ai/flashinfer/pull/1446#pullrequestreview-3103700113)
- `2025-08-10T20:29:10Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1446#pullrequestreview-3103737202)
- `2025-08-13T04:35:27Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1446#pullrequestreview-3113895517)
- `2025-08-13T05:10:35Z` `COMMENTED` by `cyx-6` (https://github.com/flashinfer-ai/flashinfer/pull/1446#pullrequestreview-3113950490)
- `2025-08-13T07:24:42Z` `APPROVED` by `yzh119` - CI is temporarily broken, run blackwell tests locally and all UT passed. Thanks for your contribution @cyx-6 @yongwww ... (https://github.com/flashinfer-ai/flashinfer/pull/1446#pullrequestreview-3114268638)

## Inline Comment Hotspots

- `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`: 13 inline comment(s)
- `include/flashinfer/trtllm/fmha/fmhaRunnerParams.h`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-13T06:09:35Z` `issue` by `yzh119`; signals: attention, flashinfer, gemm, kernel, moe; excerpt: "@nvpohanh not only moe kernels, all dependency of getEnvEnablePDL (including trtllm-gen's batched gemm and attention) have been removed. AR+Norm/activation These operators do not rely ..." (https://github.com/flashinfer-ai/flashinfer/pull/1446#issuecomment-3182314491)
- `2025-08-13T04:34:51Z` `inline` by `yzh119` `include/flashinfer/trtllm/fmha/fmhaRunnerParams.h`:279; signals: blackwell, flashinfer, hopper, kernel; excerpt: "Don't set default value here, it doesn't work, we will be memset the entire POD anyways in the constructors: and for hopper/blackwell kernels, it ..." (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2272044012)
- `2025-08-13T05:18:47Z` `issue` by `nvpohanh`; signals: gemm, hang, kernel, moe; excerpt: "@yongwww @yzh119 I see that these only changed MoE-related kernels. Do we plan to make the same change for other kernels like Attn/Gemm/AR+Norm/activation/etc.?" (https://github.com/flashinfer-ai/flashinfer/pull/1446#issuecomment-3182212415)
- `2025-08-10T20:27:34Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:263; signals: cutlass, kernel, moe; excerpt: "stream should be the last argument, and please do not set a default value for enable pdl" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428670)
- `2025-08-10T20:27:41Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:593; signals: cutlass, kernel, moe; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428696)
- `2025-08-10T20:27:51Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:709; signals: cutlass, kernel, moe; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428742)
- `2025-08-10T20:27:57Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:789; signals: cutlass, kernel, moe; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428785)
- `2025-08-10T20:28:02Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:846; signals: cutlass, kernel, moe; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428831)
- `2025-08-10T20:28:11Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:853; signals: cutlass, kernel, moe; excerpt: "fix the caller" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428862)
- `2025-08-10T20:28:15Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:858; signals: cutlass, kernel, moe; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428902)
- `2025-08-10T20:28:22Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:864; signals: cutlass, kernel, moe; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428965)
- `2025-08-10T20:28:27Z` `inline` by `yzh119` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:1628; signals: cutlass, kernel, moe; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1446#discussion_r2265428980)
