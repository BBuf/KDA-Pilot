# PR Discussion Digest

- Source PR: [vllm-project/vllm#14383](https://github.com/vllm-project/vllm/pull/14383)
- Source page: `sources/prs/vllm/PR-14383.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14383`
- Generated at: `2026-05-20T15:34:23.993366+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-06T20:37:28Z`
- Merged: `2025-05-08T22:09:55Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 12
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=8
- Human participants with discussion text: LucasWilkinson, WoosukKwon, kushanam, mergify, pathorn, thakkarV, tlrmchlsmth, wenscarl
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-26T02:07:57Z` `COMMENTED` by `tlrmchlsmth` - Thanks for the contribution! A couple of comments but looks good overall (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2715701918)
- `2025-03-28T16:23:35Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2726069167)
- `2025-03-28T16:25:13Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2726073484)
- `2025-04-04T20:48:55Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2744078607)
- `2025-04-04T20:54:00Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2744086816)
- `2025-04-04T21:08:56Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2744107180)
- `2025-04-04T21:14:44Z` `COMMENTED` by `thakkarV` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2744116270)
- `2025-04-25T19:48:11Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2795144732)
- `2025-04-25T19:50:35Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2795149048)
- `2025-05-05T13:56:23Z` `APPROVED` by `LucasWilkinson` - LGTM now, thanks! (https://github.com/vllm-project/vllm/pull/14383#pullrequestreview-2814906779)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`: 6 inline comment(s)
- `csrc/cutlass_extensions/common.hpp`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_c3x_sm100.cu`: 1 inline comment(s)
- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-26T02:00:22Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8.cu`:39; signals: alignment, block, cutlass, fp8, perf, performance, sm100; excerpt: "This dynamic padding could cause subtle performance issues that could be hard to debug. I think it would be best to add a TORCH ..." (https://github.com/vllm-project/vllm/pull/14383#discussion_r2013274139)
- `2025-03-06T21:58:43Z` `issue` by `pathorn`; signals: blackwell, block, fp8, hang, kernel, sm100; excerpt: "It looks like scaled mm blockwise sm100 fp8.cu and scaled mm blockwise sm100 fp8 dispatch.cuh were committed only as symlinks. When the change is ..." (https://github.com/vllm-project/vllm/pull/14383#issuecomment-2705035012)
- `2025-03-26T02:03:24Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`:71; signals: block, cutlass, fp8, sm100; excerpt: "nit: delete commented-out code" (https://github.com/vllm-project/vllm/pull/14383#discussion_r2013276016)
- `2025-03-26T02:04:39Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`:102; signals: block, cutlass, fp8, sm100; excerpt: "light suggestion to turn off clang format for these blocks and manually do the whitespace" (https://github.com/vllm-project/vllm/pull/14383#discussion_r2013276696)
- `2025-03-28T16:23:35Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`:71; signals: block, cutlass, fp8, sm100; excerpt: "@wenscarl just checking since I see you marked this as resolved: did you forget to push?" (https://github.com/vllm-project/vllm/pull/14383#discussion_r2018975701)
- `2025-03-28T16:25:13Z` `inline` by `wenscarl` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`:71; signals: block, cutlass, fp8, sm100; excerpt: "Thanks for the reminder. I am working on the push, please expect it within next few hours." (https://github.com/vllm-project/vllm/pull/14383#discussion_r2018978874)
- `2025-04-04T21:14:08Z` `inline` by `thakkarV` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`:98; signals: block, cutlass, fp8, sm100; excerpt: "Use 2Sm for compute bound cases" (https://github.com/vllm-project/vllm/pull/14383#discussion_r2029442413)
- `2025-04-04T21:14:41Z` `inline` by `thakkarV` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`:192; signals: block, cutlass, fp8, sm100; excerpt: "Have you tried auto tuning for these?" (https://github.com/vllm-project/vllm/pull/14383#discussion_r2029444068)
- `2025-03-26T01:52:44Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/scaled_mm_c3x_sm100.cu`:54; signals: cutlass, sm100, sm90; excerpt: "This code is duplicated from scaled mm c3x sm90.cu. Could you please factor it out?" (https://github.com/vllm-project/vllm/pull/14383#discussion_r2013269293)
- `2025-03-10T21:05:32Z` `issue` by `kushanam`; signals: block, cutlass, fp8; excerpt: "Thank you @wenscarl! Please correct thecutlass scaled mm supports block fp8() function in scaled mm entry.cu to allow 100 arch as well." (https://github.com/vllm-project/vllm/pull/14383#issuecomment-2711832745)
- `2025-04-04T20:48:54Z` `inline` by `tlrmchlsmth` `csrc/cutlass_extensions/common.hpp`:70; signals: cutlass, kernel; excerpt: "Should we do this instead? If I understand correctly, these kernels won't be forward-compatible" (https://github.com/vllm-project/vllm/pull/14383#discussion_r2029418379)
- `2025-04-04T20:54:00Z` `inline` by `wenscarl` `csrc/cutlass_extensions/common.hpp`:70; signals: cutlass, sm100; excerpt: "Yes, it's sm100a." (https://github.com/vllm-project/vllm/pull/14383#discussion_r2029423231)
