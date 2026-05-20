# PR Discussion Digest

- Source PR: [vllm-project/vllm#29354](https://github.com/vllm-project/vllm/pull/29354)
- Source page: `sources/prs/vllm/PR-29354.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29354`
- Generated at: `2026-05-20T15:38:42.718488+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-24T22:36:03Z`
- Merged: `2026-01-09T19:58:39Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 17 (approved=4, commented=13)
- Inline review comments: 14
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=0, outdated=7
- Human participants with discussion text: RunkaiTao, bnellnm, chatgpt-codex-connector, cursor, dcmaddix, heheda12345, jeejeelee, mergify, mgoin, varun-sundar-rabindranath
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-02T22:17:10Z` `COMMENTED` by `dcmaddix` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3532318123)
- `2025-12-03T17:29:19Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3536173585)
- `2025-12-03T18:20:46Z` `COMMENTED` by `varun-sundar-rabindranath` - Thanks for the optimization @RunkaiTao . IIUC, the speedup comes from the fact that we skipping the call ... (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3536202706)
- `2025-12-03T19:41:57Z` `COMMENTED` by `RunkaiTao` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3536641346)
- `2025-12-03T19:55:30Z` `COMMENTED` by `RunkaiTao` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3536687230)
- `2025-12-03T20:01:22Z` `COMMENTED` by `RunkaiTao` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3536705433)
- `2025-12-11T04:59:35Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3565637735)
- `2025-12-11T06:18:34Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3565903721)
- `2025-12-11T13:52:49Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3567551781)
- `2025-12-11T13:56:55Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3567569279)
- `2025-12-17T20:22:25Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3589498801)
- `2025-12-17T20:25:13Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3589509708)
- `2025-12-17T20:29:43Z` `APPROVED` by `varun-sundar-rabindranath` - LGTM! Thanks @RunkaiTao (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3589523459)
- `2026-01-06T22:06:11Z` `APPROVED` by `bnellnm` - Nice work! (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3632682543)
- `2026-01-08T06:45:05Z` `APPROVED` by `jeejeelee` - Considering @varun-sundar-rabindranath and @bnellnm have approved this PR, I just add my stamp to land this PR (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3637961187)
- `2026-01-09T01:50:34Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3642042837)
- `2026-01-09T19:58:20Z` `APPROVED` by `mgoin` - Interesting optimization, nice find! (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3645401851)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 12 inline comment(s)
- `tests/kernels/moe/test_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-09T01:50:34Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/fused_moe.py`:2206; signals: block, correctness, kernel, moe, triton; excerpt: "Wrong tensor used for chunk padding calculation Low Severity In the naive block assignment path, max num tokens padded is computed using topk ids.numel() ..." (https://github.com/vllm-project/vllm/pull/29354#discussion_r2674533058)
- `2025-12-03T18:20:46Z` `review` `COMMENTED` by `varun-sundar-rabindranath`; signals: block, moe, speedup; excerpt: "Thanks for the optimization @RunkaiTao . IIUC, the speedup comes from the fact that we skipping the call to moe align block size and ..." (https://github.com/vllm-project/vllm/pull/29354#pullrequestreview-3536202706)
- `2025-12-03T19:55:30Z` `inline` by `RunkaiTao` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1911; signals: benchmark, kernel, moe; excerpt: "I couldn't run into this branch and test fused moe kernel gptq awq using benchmark moe.py. So I temporally turn it off in use ..." (https://github.com/vllm-project/vllm/pull/29354#discussion_r2586424884)
- `2025-12-17T13:08:46Z` `issue` by `varun-sundar-rabindranath`; signals: block, perf, performance; excerpt: "Thank you @RunkaiTao . Nice performance boost. Can you add a unit test that exercises naive block assignment code-path." (https://github.com/vllm-project/vllm/pull/29354#issuecomment-3665282266)
- `2025-12-03T17:59:00Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1911; signals: block, moe; excerpt: "IIUC, this optimization should also benefit block quantized code path. Is there are a reason we are not enabling it for those cases ?" (https://github.com/vllm-project/vllm/pull/29354#discussion_r2586110394)
- `2025-12-11T06:18:34Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1957; signals: block, moe; excerpt: "nit : about the name use unpermute, is there a better / descriptive name that we can use. maybe, naive block assignment. If you ..." (https://github.com/vllm-project/vllm/pull/29354#discussion_r2609320969)
- `2025-12-02T22:17:10Z` `inline` by `dcmaddix` `vllm/model_executor/layers/fused_moe/fused_moe.py`:545; signals: kernel, moe; excerpt: "let's try to consolidate this into the fused moe kernel to reduce duplicate code" (https://github.com/vllm-project/vllm/pull/29354#discussion_r2582951080)
- `2025-12-17T20:22:25Z` `inline` by `varun-sundar-rabindranath` `tests/kernels/moe/test_moe.py`:366; signals: kernel, moe; excerpt: "please remove cruft" (https://github.com/vllm-project/vllm/pull/29354#discussion_r2628518472)
- `2025-12-17T20:25:13Z` `inline` by `varun-sundar-rabindranath` `tests/kernels/moe/test_moe.py`:427; signals: kernel, moe; excerpt: "is this required ?" (https://github.com/vllm-project/vllm/pull/29354#discussion_r2628525710)
- `2025-12-03T17:36:50Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1920; signals: moe; excerpt: "should these be curr topk ids instead of topk ids ? also, expert ids is a 1D tensors in the other code path, can ..." (https://github.com/vllm-project/vllm/pull/29354#discussion_r2586042211)
- `2025-12-03T19:41:57Z` `inline` by `RunkaiTao` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1908; signals: moe; excerpt: "Yes,4 is from experiment. I want to make sure num token top k num much smaller than num experts. I also disable expert map ..." (https://github.com/vllm-project/vllm/pull/29354#discussion_r2586387793)
- `2025-12-03T17:29:19Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1908; signals: moe; excerpt: "for my edification, is the 4 in tokens in chunk top k num 4 a heuristic ?" (https://github.com/vllm-project/vllm/pull/29354#discussion_r2586017668)
