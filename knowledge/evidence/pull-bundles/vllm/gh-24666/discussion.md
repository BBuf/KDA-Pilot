# PR Discussion Digest

- Source PR: [vllm-project/vllm#24666](https://github.com/vllm-project/vllm/pull/24666)
- Source page: `sources/prs/vllm/PR-24666.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-24666`
- Generated at: `2026-05-20T15:37:49.691310+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-11T13:39:08Z`
- Merged: `2025-09-23T19:03:10Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 39 (approved=3, commented=36)
- Inline review comments: 68
- Review threads observed: 33
- Resolved/outdated thread markers: resolved=31, outdated=24
- Human participants with discussion text: ElizaWszola, ProExpertProg, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-11T15:08:50Z` `COMMENTED` by `ProExpertProg` - A few overall notes (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3212092907)
- `2025-09-11T15:09:52Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3212252820)
- `2025-09-12T04:33:33Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3214571200)
- `2025-09-17T13:12:29Z` `COMMENTED` by `ProExpertProg` - Looks pretty good overall! A few minor notes (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3234389294)
- `2025-09-17T13:29:18Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3234480245)
- `2025-09-17T16:05:32Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3235211267)
- `2025-09-17T16:05:56Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3235212481)
- `2025-09-17T16:07:06Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3235215472)
- `2025-09-17T17:54:03Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3235606571)
- `2025-09-17T18:02:16Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3235633208)
- `2025-09-18T12:50:08Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3239481462)
- `2025-09-18T16:29:56Z` `COMMENTED` by `ProExpertProg` - Not really sure what the different block size variables/members are, could we have a separate weight block shape: ... (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3240612620)
- `2025-09-19T05:56:40Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3243225269)
- `2025-09-19T07:58:51Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3243667794)
- `2025-09-19T08:10:09Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3243705085)
- `2025-09-19T08:12:04Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3243711136)
- `2025-09-19T08:51:27Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3243858212)
- `2025-09-19T12:30:25Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3244569070)
- `2025-09-19T12:52:42Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3244729615)
- `2025-09-19T13:04:56Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3244775185)
- `2025-09-19T13:10:37Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3244794452)
- `2025-09-19T14:59:31Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3245306279)
- `2025-09-19T15:28:54Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3245469111)
- `2025-09-19T15:57:36Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3245624503)
- ... 15 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 39 inline comment(s)
- `vllm/config/__init__.py`: 8 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 7 inline comment(s)
- `vllm/model_executor/layers/quantization/input_quant_fp8.py`: 7 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`: 3 inline comment(s)
- `tests/kernels/quantization/test_fp8_quant_group.py`: 2 inline comment(s)
- `tests/quantization/test_compressed_tensors.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-17T13:29:18Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:49; signals: blackwell, block, compile, cutlass, fp8; excerpt: "This is here so we can compile this function on Blackwell (it doesn't need padding), but I could also modify Blackwell code in W8A8BlockFp8LinearOp:: ..." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2355533518)
- `2025-09-19T12:16:14Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:171; signals: cutlass, deepgemm, fp8, gemm, triton; excerpt: "Oh I see, because we don't know at init time what size the tensor will be and so we need separate quants for deepgemm ..." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2362699681)
- `2025-09-11T15:07:59Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:155; signals: cutlass, deepgemm, fp8, gemm; excerpt: "It might be worth extracting some of this dispatching logic to init - long-term we want these to be separate classes like int8 ScaledMM ..." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2341353060)
- `2025-09-12T04:33:33Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:155; signals: block, deepgemm, fp8, gemm; excerpt: "From what I'm seeing, almost all dispatching logic in this function depends on weight shapes (both should use deepgemm for fp8 linear and dispatch ..." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2342926294)
- `2025-09-17T17:54:03Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:49; signals: blackwell, compile, cutlass, fp8; excerpt: "If we simply remove it, then CUTLASS+compile won't work on Blackwell because current platform.is device capability(90) is not supported by the compiler" (https://github.com/vllm-project/vllm/pull/24666#discussion_r2356303258)
- `2025-09-19T15:57:36Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:259; signals: deepgemm, fp8, gemm, hang; excerpt: "use e8m0 should be true only when we use deepgemm, but it seems to only affect one line in per token group quant fp8: ..." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2363422361)
- `2025-09-22T11:27:24Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:212; signals: block, deepgemm, fp8, gemm; excerpt: "w8a8 deepgemm block scaled mm?" (https://github.com/vllm-project/vllm/pull/24666#discussion_r2367806332)
- `2025-09-23T15:45:38Z` `review` `COMMENTED` by `ProExpertProg`; signals: blackwell, cuda, h100; excerpt: "Gonna submit this to always use the cuda path - we can enable torch for Blackwell in a follow-up as suggested by @mgoin, he ..." (https://github.com/vllm-project/vllm/pull/24666#pullrequestreview-3258635052)
- `2025-09-17T18:02:16Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:187; signals: block, fp8, hang; excerpt: "It's not used for anything after this PR's changes (its logic has been replaced by dispatch w8a8 blockscale op()), so I'll remove it." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2356322599)
- `2025-09-18T16:22:12Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:302; signals: blackwell, fp8, kernel; excerpt: "Can we use the QuantFP8 abstraction here, and in config init we can enable the custom kernel (so that per token group quant fp8 ..." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2360153837)
- `2025-09-19T07:58:51Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:302; signals: cuda, fp8, perf; excerpt: "Is forward cuda() also undeperforming? From what I'm seeing, it's what would replace per token group quant fp8()" (https://github.com/vllm-project/vllm/pull/24666#discussion_r2362101968)
- `2025-09-19T12:09:47Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:171; signals: block, fp8, gemm; excerpt: "Why not just pass the proper use ue8m0=is deep gemm e8m0 used() to the dispatch w8a8 blockscale op method so that we can always ..." (https://github.com/vllm-project/vllm/pull/24666#discussion_r2362685086)
