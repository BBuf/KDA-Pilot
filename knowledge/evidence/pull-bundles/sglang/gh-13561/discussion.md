# PR Discussion Digest

- Source PR: [sgl-project/sglang#13561](https://github.com/sgl-project/sglang/pull/13561)
- Source page: `sources/prs/sglang/PR-13561.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13561`
- Generated at: `2026-05-20T15:27:48.091422+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-19T06:37:23Z`
- Merged: `2026-02-05T07:09:59Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 32 (approved=3, changes_requested=5, commented=24)
- Inline review comments: 45
- Review threads observed: 26
- Resolved/outdated thread markers: resolved=6, outdated=23
- Human participants with discussion text: Guobing-Chen, SKRohit, ZailiWang, airMeng, ck-intel, mingfeima, msinnha1, polisettyvarma
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-02T05:32:16Z` `COMMENTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3528192019)
- `2025-12-02T09:59:11Z` `CHANGES_REQUESTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3529236448)
- `2025-12-08T06:09:52Z` `CHANGES_REQUESTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550205331)
- `2025-12-08T06:56:37Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550382113)
- `2025-12-08T06:57:07Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550383234)
- `2025-12-08T06:57:13Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550383476)
- `2025-12-08T06:59:53Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550392759)
- `2025-12-08T07:02:11Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550400806)
- `2025-12-08T07:07:03Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550417511)
- `2025-12-08T07:10:39Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550428619)
- `2025-12-08T07:15:55Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3550445829)
- `2025-12-09T05:44:08Z` `APPROVED` by `mingfeima` - fix CI error if not flaky mark TODOs in our spreadsheet (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3555562147)
- `2025-12-17T05:29:52Z` `COMMENTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3586076035)
- `2025-12-19T02:50:06Z` `COMMENTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3596504270)
- `2025-12-22T07:36:05Z` `COMMENTED` by `msinnha1` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3602936009)
- `2025-12-22T11:19:20Z` `COMMENTED` by `ck-intel` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3603670950)
- `2025-12-24T02:15:06Z` `COMMENTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3609746191)
- `2026-01-19T06:31:23Z` `COMMENTED` by `msinnha1` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3676464117)
- `2026-01-20T02:34:04Z` `CHANGES_REQUESTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3677147227)
- `2026-01-22T04:07:14Z` `COMMENTED` by `SKRohit` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3690512264)
- `2026-01-23T03:31:53Z` `CHANGES_REQUESTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3695514190)
- `2026-01-23T05:04:14Z` `COMMENTED` by `SKRohit` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3695701378)
- `2026-01-23T07:00:30Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3695984359)
- `2026-01-23T07:00:40Z` `COMMENTED` by `airMeng` (https://github.com/sgl-project/sglang/pull/13561#pullrequestreview-3695984811)
- ... 8 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/unquant.py`: 19 inline comment(s)
- `python/sglang/srt/layers/attention/xpu_backend.py`: 12 inline comment(s)
- `test/srt/xpu/test_deepseek_ocr.py`: 5 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`: 5 inline comment(s)
- `python/sglang/srt/layers/moe/moe_runner/triton.py`: 2 inline comment(s)
- `docker/xpu.Dockerfile`: 1 inline comment(s)
- `python/sglang/srt/utils/common.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-08T06:14:44Z` `issue` by `mingfeima`; signals: attention, kernel, moe, perf, performance, triton; excerpt: "@airMeng update the PR descriptions to add more details: updates attention backend scripts to reduce overhead (and how to achieve that?) enable MoE implementations ..." (https://github.com/sgl-project/sglang/pull/13561#issuecomment-3625168401)
- `2025-12-08T05:59:28Z` `inline` by `mingfeima` `python/sglang/srt/layers/attention/xpu_backend.py`:576; signals: attention, cache, dtype, fp8; excerpt: "i prefer removing to(q.dtype) here and just report an error in C++ when q and kv have different dtypes. also i suppose we haven't ..." (https://github.com/sgl-project/sglang/pull/13561#discussion_r2597147188)
- `2026-01-23T05:04:14Z` `inline` by `SKRohit` `python/sglang/srt/layers/quantization/unquant.py`:481; signals: cuda, kernel, moe, triton; excerpt: "TritonMoeQuantInfo does not have w13 bias and w2 bias atrributes. Those are present in TritonKernelsQuantInfo: Also, as per forward cuda implementation b13 and b2 ..." (https://github.com/sgl-project/sglang/pull/13561#discussion_r2719618381)
- `2025-12-22T07:35:13Z` `inline` by `msinnha1` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:668; signals: cuda, moe, triton; excerpt: "In DeepSeek V3 routed scaling factor is 2.5 then why are we calling moe sum and not moe sum reduce? or till the time ..." (https://github.com/sgl-project/sglang/pull/13561#discussion_r2638944985)
- `2025-12-08T06:00:19Z` `inline` by `mingfeima` `python/sglang/srt/layers/attention/xpu_backend.py`:584; signals: attention, perf, performance; excerpt: "these will be performance downgrade for sure. mark a TODO to move them into C++." (https://github.com/sgl-project/sglang/pull/13561#discussion_r2597148598)
- `2026-01-23T03:24:46Z` `inline` by `polisettyvarma` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:690; signals: hang, moe, triton; excerpt: "seems you have changed the order, please check" (https://github.com/sgl-project/sglang/pull/13561#discussion_r2719441097)
- `2026-01-23T03:31:42Z` `inline` by `polisettyvarma` `python/sglang/srt/layers/moe/moe_runner/triton.py`:320; signals: cuda, moe, triton; excerpt: "query, cuda does reduce also for xpu where do we do this sum/reduce then ?" (https://github.com/sgl-project/sglang/pull/13561#discussion_r2719452010)
- `2026-01-23T07:00:40Z` `inline` by `airMeng` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:690; signals: hang, moe, triton; excerpt: "change back" (https://github.com/sgl-project/sglang/pull/13561#discussion_r2719871007)
- `2026-01-23T07:00:51Z` `inline` by `airMeng` `python/sglang/srt/layers/moe/moe_runner/triton.py`:320; signals: aligned, moe, triton; excerpt: "aligned" (https://github.com/sgl-project/sglang/pull/13561#discussion_r2719871563)
- `2025-12-08T07:07:03Z` `inline` by `airMeng` `python/sglang/srt/layers/attention/xpu_backend.py`:589; signals: attention, kernel; excerpt: "for sink support, we test at sgl-kernel-xpu side. For model level verification, we haven't enabled models with sink on our current CI machine" (https://github.com/sgl-project/sglang/pull/13561#discussion_r2597284645)
- `2025-12-08T07:15:55Z` `inline` by `airMeng` `python/sglang/srt/layers/attention/xpu_backend.py`:607; signals: attention, mla; excerpt: "This is another optimization that now accepts non-cumsum cu seqlens k to avoid host overhead. And since MLA hasn't been optimized, I update here ..." (https://github.com/sgl-project/sglang/pull/13561#discussion_r2597306109)
- `2025-12-22T11:18:10Z` `inline` by `ck-intel` `python/sglang/srt/layers/attention/xpu_backend.py`:526; signals: attention, hang; excerpt: "@airMeng "sinks" info is already passed as part of "kwargs", is this change required? referring code lines 470-472:" (https://github.com/sgl-project/sglang/pull/13561#discussion_r2639542541)
