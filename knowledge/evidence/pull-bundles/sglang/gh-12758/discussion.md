# PR Discussion Digest

- Source PR: [sgl-project/sglang#12758](https://github.com/sgl-project/sglang/pull/12758)
- Source page: `sources/prs/sglang/PR-12758.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12758`
- Generated at: `2026-05-20T15:27:41.370770+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-06T07:30:00Z`
- Merged: `2025-11-07T05:59:57Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 11 (approved=1, changes_requested=1, commented=9)
- Inline review comments: 10
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, elvischenv, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-11-06T08:31:36Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3426886003)
- `2025-11-06T09:11:04Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3427066937)
- `2025-11-06T09:16:26Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3427094825)
- `2025-11-06T11:24:29Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3427681655)
- `2025-11-06T15:55:28Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3429005461)
- `2025-11-06T16:03:38Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3429059979)
- `2025-11-07T01:47:27Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3431240103)
- `2025-11-07T03:45:44Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3431480808)
- `2025-11-07T04:35:22Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3431594052)
- `2025-11-07T05:58:06Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12758#pullrequestreview-3431795176)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/mxfp4.py`: 6 inline comment(s)
- `python/sglang/srt/layers/flashinfer_comm_fusion.py`: 3 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-06T11:24:29Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/mxfp4.py`:647; signals: accuracy, benchmark, fp4, memory, mxfp4; excerpt: "This fix is correct since the output tensor should be padded, the original x is unpadded, and this could fix the illegal memory access ..." (https://github.com/sgl-project/sglang/pull/12758#discussion_r2498585984)
- `2025-11-06T16:03:38Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/mxfp4.py`:647; signals: accuracy, fp4, hang, mxfp4; excerpt: "With the hanging issue fix, I can get reasonable accuracy score:" (https://github.com/sgl-project/sglang/pull/12758#discussion_r2499653994)
- `2025-11-06T08:31:33Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/mxfp4.py`:647; signals: accuracy, fp4, mxfp4; excerpt: "I just tested accuracy with this PR, and it seems incorrect (0.013 for mmlu) @elvischenv Please have a check" (https://github.com/sgl-project/sglang/pull/12758#discussion_r2497998600)
- `2025-11-06T09:11:04Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/mxfp4.py`:647; signals: flashinfer, fp4, mxfp4; excerpt: "What model are you testing? Would you try hardcoding to torch.bfloat16? related code in flashinfer:" (https://github.com/sgl-project/sglang/pull/12758#discussion_r2498134431)
- `2025-11-06T09:16:26Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/mxfp4.py`:647; signals: fp4, mxfp4; excerpt: "gpt-oss 20b with mxfp4" (https://github.com/sgl-project/sglang/pull/12758#discussion_r2498155231)
- `2025-11-06T15:55:23Z` `inline` by `elvischenv` `python/sglang/srt/layers/flashinfer_comm_fusion.py`:131; signals: flashinfer, hang; excerpt: "Hang issue WAR: Increase max token num to allocate a larger workspace" (https://github.com/sgl-project/sglang/pull/12758#discussion_r2499608303)
- `2025-11-07T01:47:23Z` `inline` by `elvischenv` `python/sglang/srt/models/deepseek_v2.py`:807; signals: hang; excerpt: "Reverted that changes and let's see if it can pass." (https://github.com/sgl-project/sglang/pull/12758#discussion_r2501414246)
- `2025-11-07T03:45:44Z` `inline` by `nvpohanh` `python/sglang/srt/layers/flashinfer_comm_fusion.py`:131; signals: flashinfer; excerpt: "add an assert: assert input tensor.shape[0] <= max token num ?" (https://github.com/sgl-project/sglang/pull/12758#discussion_r2501577278)
- `2025-11-07T04:35:21Z` `inline` by `nvpohanh` `python/sglang/srt/layers/flashinfer_comm_fusion.py`:131; signals: flashinfer; excerpt: "should be covered by the code below:" (https://github.com/sgl-project/sglang/pull/12758#discussion_r2501652658)
- `2025-11-07T05:57:49Z` `issue` by `Fridge003`; signals: b200; excerpt: "The gptoss CI test on B200 is passing here" (https://github.com/sgl-project/sglang/pull/12758#issuecomment-3500882219)
- `2025-11-07T01:24:50Z` `issue` by `elvischenv`; signals: general review; excerpt: "Failed at GPTOSS Ci test, please have a look This is DeepseekV2. This failure seems also related to 12524. cc @merrymercy" (https://github.com/sgl-project/sglang/pull/12758#issuecomment-3500067502)
