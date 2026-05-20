# PR Discussion Digest

- Source PR: [sgl-project/sglang#3730](https://github.com/sgl-project/sglang/pull/3730)
- Source page: `sources/prs/sglang/PR-3730.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3730`
- Generated at: `2026-05-20T15:30:02.469740+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-20T10:48:04Z`
- Merged: `2025-02-24T13:43:36Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 15 (approved=2, changes_requested=1, commented=12)
- Inline review comments: 17
- Review threads observed: 17
- Resolved/outdated thread markers: resolved=17, outdated=16
- Human participants with discussion text: HandH1998, JeffRody, KimmyGLM, brisker, coolhok, ispobock, laixinn, lambert0312, noob-ctrl
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 15

## Review Decisions

- `2025-02-21T09:59:14Z` `CHANGES_REQUESTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2632545170)
- `2025-02-24T08:07:57Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636231250)
- `2025-02-24T08:10:58Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636236601)
- `2025-02-24T08:11:50Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636238243)
- `2025-02-24T08:20:10Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636255215)
- `2025-02-24T08:36:03Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636289377)
- `2025-02-24T08:37:42Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636292915)
- `2025-02-24T08:38:40Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636294884)
- `2025-02-24T08:40:09Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636297899)
- `2025-02-24T08:43:05Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636305870)
- `2025-02-24T08:43:40Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636307701)
- `2025-02-24T08:45:45Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636312195)
- `2025-02-24T08:47:41Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636316275)
- `2025-02-24T10:37:54Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636637103)
- `2025-02-24T10:39:18Z` `APPROVED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3730#pullrequestreview-2636640464)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/blockwise_int8.py`: 9 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`: 3 inline comment(s)
- `python/sglang/test/test_block_int8.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/blockwise_int8_utils.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/blockwise_int8_kernel.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/int8_utils.py`: 1 inline comment(s)
- `test/srt/test_block_int8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-24T08:07:57Z` `inline` by `HandH1998` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:220; signals: fp8, moe, triton; excerpt: "The code of elif use int8 w8a8 is same with elif use fp8 w8a8. Maybe can merge them to elif use fp8 w8a8 or ..." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1967172075)
- `2025-02-24T08:36:03Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/blockwise_int8.py`:445; signals: block, cache, kv cache; excerpt: "delete it, as int8 kv cache is not supported" (https://github.com/sgl-project/sglang/pull/3730#discussion_r1967203323)
- `2025-02-21T09:52:44Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/blockwise_int8_kernel.py`:1; signals: block, kernel; excerpt: "move to int8 kernels.py." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1965191335)
- `2025-02-24T08:10:57Z` `inline` by `HandH1998` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:510; signals: moe, triton; excerpt: "Same as above." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1967175187)
- `2025-02-24T08:11:50Z` `inline` by `HandH1998` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:795; signals: moe, triton; excerpt: "Default value should be False?" (https://github.com/sgl-project/sglang/pull/3730#discussion_r1967176066)
- `2025-02-24T08:38:40Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/blockwise_int8.py`:102; signals: attention, block; excerpt: "delete from vllm.attention.layer import Attention" (https://github.com/sgl-project/sglang/pull/3730#discussion_r1967206452)
- `2025-02-24T08:40:08Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/blockwise_int8.py`:71; signals: block, hang; excerpt: "change to return "blockwise int8"" (https://github.com/sgl-project/sglang/pull/3730#discussion_r1967208239)
- `2025-02-21T09:50:16Z` `inline` by `ispobock` `python/sglang/test/test_block_int8.py`:1; signals: block; excerpt: "Add to run suite.py." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1965187780)
- `2025-02-21T09:50:39Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/blockwise_int8_utils.py`:12; signals: block; excerpt: "clean the comments." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1965188323)
- `2025-02-21T09:53:28Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/blockwise_int8.py`:144; signals: block; excerpt: "Update or clean comments." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1965192600)
- `2025-02-21T09:59:07Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/blockwise_int8.py`:15; signals: block; excerpt: "If this quantization is only for block-wise int8. The common int8 w8a8 logic can be removed." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1965201645)
- `2025-02-24T08:20:10Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/blockwise_int8.py`:34; signals: block; excerpt: "I think BlockInt8Config will be more understandable." (https://github.com/sgl-project/sglang/pull/3730#discussion_r1967185247)
