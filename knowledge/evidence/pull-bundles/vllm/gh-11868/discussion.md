# PR Discussion Digest

- Source PR: [vllm-project/vllm#11868](https://github.com/vllm-project/vllm/pull/11868)
- Source page: `sources/prs/vllm/PR-11868.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-11868`
- Generated at: `2026-05-20T15:33:38.626220+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-08T23:38:47Z`
- Merged: `2025-01-31T02:33:00Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 19
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: Andy0422, LucasWilkinson, ProphetPeng, mergify, mgoin, tlrmchlsmth, yizhang2077
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 10

## Review Decisions

- `2025-01-13T20:00:02Z` `COMMENTED` by `mgoin` - Really nice performance! When you are ready for e2e testing lmk and we can hook these up for ... (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2547728160)
- `2025-01-15T19:23:41Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2553704686)
- `2025-01-15T19:25:07Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2553707280)
- `2025-01-20T17:33:56Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2562902592)
- `2025-01-20T18:02:23Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2562955120)
- `2025-01-20T18:03:19Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2562956140)
- `2025-01-20T18:09:43Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2562966785)
- `2025-01-20T18:16:12Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2562974762)
- `2025-01-20T18:16:46Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2562975337)
- `2025-01-27T19:18:20Z` `APPROVED` by `tlrmchlsmth` - A few minor comments, but looks good to me! (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2575794479)
- `2025-01-28T19:31:37Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2579233742)
- `2025-01-31T01:15:50Z` `APPROVED` by `mgoin` - Awesome work (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2585452446)

## Inline Comment Hotspots

- `CMakeLists.txt`: 7 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`: 4 inline comment(s)
- `csrc/cutlass_extensions/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_c3x_sm90_fp8_dispatch.cuh`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`: 2 inline comment(s)
- `benchmarks/cutlass_benchmarks/w8a8_benchmarks.py`: 1 inline comment(s)
- `tests/kernels/test_cutlass.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-01-20T18:16:12Z` `inline` by `LucasWilkinson` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_c3x_sm90_fp8_dispatch.cuh`:48; signals: alignment, block, cutlass, fp8, gemm, hang, kernel, sm90; excerpt: "we don't actually use smaller alignments in the dense cutlass GEMM kernels, we just "hardcoded" them in terms of elements, for example here for ..." (https://github.com/vllm-project/vllm/pull/11868#discussion_r1922742655)
- `2025-01-20T17:30:31Z` `inline` by `tlrmchlsmth` `csrc/cutlass_extensions/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`; signals: block, cutlass, fp8, gemm, sm90, tma, warp; excerpt: "For files that have been taken/modified from elsewhere, could you add some comments like "// Adapted from ..." with permalinks?" (https://github.com/vllm-project/vllm/pull/11868#discussion_r1922707491)
- `2025-01-20T17:32:27Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_c3x_sm90_fp8_dispatch.cuh`:48; signals: alignment, block, cutlass, fp8, gemm, kernel, sm90; excerpt: "Are these alignments right? I think these are used widely in the CUTLASS examples but we use different/smaller alignments in the vLLM dense cutlass ..." (https://github.com/vllm-project/vllm/pull/11868#discussion_r1922709214)
- `2025-01-20T18:02:22Z` `inline` by `LucasWilkinson` `csrc/cutlass_extensions/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`; signals: block, cutlass, fp8, gemm, sm90, tma, warp; excerpt: "good catch, got lost when I "rebased" the file" (https://github.com/vllm-project/vllm/pull/11868#discussion_r1922732414)
- `2025-01-27T19:14:44Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`:148; signals: block, compile, cutlass, fp8, sm90; excerpt: "Maybe it wouldn't help much, but do you think mma promotion interval should be a compile-time constant?" (https://github.com/vllm-project/vllm/pull/11868#discussion_r1931064307)
- `2025-01-27T18:49:01Z` `inline` by `tlrmchlsmth` `benchmarks/cutlass_benchmarks/w8a8_benchmarks.py`; signals: benchmark, bf16, cutlass, fp8; excerpt: "I noticed that there's an asymmetry between the int8 and fp8 benchmark functions in that bench fp8 benchmarks both fp16 and bf16 outputs and ..." (https://github.com/vllm-project/vllm/pull/11868#discussion_r1931031582)
- `2025-01-27T19:08:37Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`:60; signals: block, cutlass, fp8, sm90; excerpt: "This should likely be a template argument, since it's a tunable parameter (can wait for a subsequent PR)" (https://github.com/vllm-project/vllm/pull/11868#discussion_r1931056498)
- `2025-01-13T20:00:02Z` `review` `COMMENTED` by `mgoin`; signals: perf, performance; excerpt: "Really nice performance! When you are ready for e2e testing lmk and we can hook these up for a full dsv3 eval" (https://github.com/vllm-project/vllm/pull/11868#pullrequestreview-2547728160)
- `2025-01-15T19:25:07Z` `inline` by `LucasWilkinson` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:100; signals: block, cutlass; excerpt: "Currently for the blockwise scaling a scales and b scales must be column-major, this is something we may need to relax for a scales ..." (https://github.com/vllm-project/vllm/pull/11868#discussion_r1917226684)
- `2025-01-27T19:17:08Z` `inline` by `tlrmchlsmth` `tests/kernels/test_cutlass.py`:66; signals: cutlass, kernel; excerpt: "nit: weird dangling comma" (https://github.com/vllm-project/vllm/pull/11868#discussion_r1931067495)
- `2025-01-20T17:26:36Z` `inline` by `tlrmchlsmth` `CMakeLists.txt`:285; signals: sm90; excerpt: "nit: We could nix the c3x from the filename, especially since it's under the c3x folder and the sm90 in the filename also implies ..." (https://github.com/vllm-project/vllm/pull/11868#discussion_r1922704003)
- `2025-01-13T19:57:00Z` `inline` by `mgoin` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:93; signals: cutlass; excerpt: "This check seems fine to remove and let the subsequent function specializations handle" (https://github.com/vllm-project/vllm/pull/11868#discussion_r1913736733)
