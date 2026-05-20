# PR Discussion Digest

- Source PR: [sgl-project/sglang#6545](https://github.com/sgl-project/sglang/pull/6545)
- Source page: `sources/prs/sglang/PR-6545.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6545`
- Generated at: `2026-05-20T15:30:43.502054+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-23T05:46:07Z`
- Merged: `2025-05-29T07:15:11Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 25 (approved=3, commented=22)
- Inline review comments: 22
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: Alcanderian, BBuf, ChangyiYang, Fridge003, fzyzcjy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-05-23T06:25:09Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2863330855)
- `2025-05-23T06:32:34Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2863344675)
- `2025-05-23T16:28:29Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2865014802)
- `2025-05-23T16:32:56Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2865024084)
- `2025-05-23T17:05:46Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2865129686)
- `2025-05-23T17:11:55Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2865143556)
- `2025-05-24T05:19:52Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2866150037)
- `2025-05-24T05:38:06Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2866163007)
- `2025-05-24T05:41:40Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2866165256)
- `2025-05-24T05:45:53Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2866167687)
- `2025-05-24T05:52:26Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2866169195)
- `2025-05-26T00:21:17Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2866995738)
- `2025-05-26T00:33:07Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2867003180)
- `2025-05-26T00:47:22Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2867012143)
- `2025-05-26T05:59:12Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2867304237)
- `2025-05-26T06:25:54Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2867393570)
- `2025-05-26T08:41:36Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2867705943)
- `2025-05-26T10:22:38Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2867956115)
- `2025-05-26T17:32:14Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2868934495)
- `2025-05-26T19:02:51Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2869032920)
- `2025-05-26T19:32:21Z` `COMMENTED` by `ChangyiYang` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2869076128)
- `2025-05-27T03:38:58Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2869474924)
- `2025-05-27T04:01:14Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2869500568)
- `2025-05-29T07:11:36Z` `APPROVED` by `Fridge003` - LGTM (https://github.com/sgl-project/sglang/pull/6545#pullrequestreview-2877330332)
- ... 1 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_utils.py`: 8 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8_kernel.py`: 8 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8.py`: 3 inline comment(s)
- `sgl-kernel/benchmark/bench_fp8_blockwise_gemm.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-05-24T05:45:53Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/fp8_utils.py`:147; signals: block, cutlass, deepgemm, dtype, fp8, gemm, triton; excerpt: "I see, we may have to check weight.shape[0] % 128 == 0 and weight.shape[1] % 128 == 0 in both cutlass and deepgemm(aslo C.dtype ..." (https://github.com/sgl-project/sglang/pull/6545#discussion_r2105716099)
- `2025-05-26T00:33:07Z` `inline` by `ChangyiYang` `python/sglang/srt/layers/quantization/fp8_kernel.py`:820; signals: benchmark, block, deepgemm, fp8, gemm, kernel, triton; excerpt: "Yes for example in [this test]( An alternatvie way is I can remove this branch in w8a8 block fp8 matmul, rename it to w8a8 ..." (https://github.com/sgl-project/sglang/pull/6545#discussion_r2106356766)
- `2025-05-26T08:41:35Z` `inline` by `ChangyiYang` `python/sglang/srt/layers/quantization/fp8_kernel.py`:820; signals: benchmark, block, deepgemm, fp8, gemm, kernel, triton; excerpt: "@Alcanderian so should I do the branch remove stuff I talked about now? Any more modification needed for this PR? Yes for example in ..." (https://github.com/sgl-project/sglang/pull/6545#discussion_r2106850316)
- `2025-05-26T17:32:14Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/fp8_kernel.py`:820; signals: benchmark, block, deepgemm, fp8, gemm, kernel, triton; excerpt: "@Alcanderian so should I do the branch remove stuff I talked about now? Any more modification needed for this PR? Yes for example in ..." (https://github.com/sgl-project/sglang/pull/6545#discussion_r2107684665)
- `2025-05-25T23:02:23Z` `issue` by `ChangyiYang`; signals: block, deepgemm, dtype, fp8, gemm, kernel, triton; excerpt: "Hi! I have create a new commit. Here are some bullet points Refactored dispatch logic to return only the selected matmul implementation function at ..." (https://github.com/sgl-project/sglang/pull/6545#issuecomment-2908141075)
- `2025-05-26T05:59:12Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/fp8_kernel.py`:820; signals: bf16, block, cutlass, fp8, hang, kernel; excerpt: "I think so as @ChangyiYang. But the logic here is somewhat weird, does cutlass w8a8 blockwise aslo only support bf16? or both fp16 and ..." (https://github.com/sgl-project/sglang/pull/6545#discussion_r2106570627)
- `2025-05-26T18:48:53Z` `issue` by `ChangyiYang`; signals: benchmark, block, deepgemm, fp8, gemm, triton; excerpt: "Hi ! Here are some modification for this commit split out w8a8 block fp8 matmul triton retain w8a8 block fp8 matmul only for testing ..." (https://github.com/sgl-project/sglang/pull/6545#issuecomment-2910447834)
- `2025-05-26T00:21:13Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8_kernel.py`:820; signals: block, deepgemm, fp8, gemm, kernel; excerpt: "Can this if branch be hit? Since deepgemm w8a8 block fp8 linear with fallback seems to directly call w8a8 block fp8 matmul deepgemm." (https://github.com/sgl-project/sglang/pull/6545#discussion_r2106352271)
- `2025-05-26T19:02:51Z` `inline` by `Alcanderian` `sgl-kernel/benchmark/bench_fp8_blockwise_gemm.py`:13; signals: benchmark, block, fp8, gemm, kernel; excerpt: "Is w8a8 block fp8 matmul gemm typo?" (https://github.com/sgl-project/sglang/pull/6545#discussion_r2107755555)
- `2025-05-26T19:32:21Z` `inline` by `ChangyiYang` `sgl-kernel/benchmark/bench_fp8_blockwise_gemm.py`:13; signals: benchmark, block, fp8, gemm, kernel; excerpt: "sry fix that!" (https://github.com/sgl-project/sglang/pull/6545#discussion_r2107791281)
- `2025-05-27T04:01:14Z` `inline` by `Alcanderian` `sgl-kernel/benchmark/bench_fp8_blockwise_gemm.py`:13; signals: benchmark, block, fp8, gemm, kernel; excerpt: "Ref: [this line](" (https://github.com/sgl-project/sglang/pull/6545#discussion_r2108112572)
- `2025-05-23T16:32:56Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/fp8_utils.py`:147; signals: block, cutlass, fp8, hang; excerpt: "This logic seems not right, my expection is just call return cutlass w8a8 block fp8 linear here. That means we are assgining cutlass w8a8 ..." (https://github.com/sgl-project/sglang/pull/6545#discussion_r2104993120)
