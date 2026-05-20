# PR Discussion Digest

- Source PR: [sgl-project/sglang#5318](https://github.com/sgl-project/sglang/pull/5318)
- Source page: `sources/prs/sglang/PR-5318.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5318`
- Generated at: `2026-05-20T15:30:23.001165+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-12T06:45:43Z`
- Merged: `2025-04-21T05:58:28Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 21 (approved=2, commented=19)
- Inline review comments: 22
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=7
- Human participants with discussion text: Swipe4057, Ying1123, hebiao064, merrymercy, qingquansong, zcnrex, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-04-13T00:02:29Z` `COMMENTED` by `zcnrex` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2762363381)
- `2025-04-13T00:15:40Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2762386244)
- `2025-04-13T21:33:08Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2762848392)
- `2025-04-14T02:18:29Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2762975058)
- `2025-04-17T19:37:59Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2776725237)
- `2025-04-18T05:44:40Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2777637182)
- `2025-04-18T06:43:13Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2777778805)
- `2025-04-18T22:33:20Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2779546185)
- `2025-04-18T22:34:06Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2779548668)
- `2025-04-19T21:58:39Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780099765)
- `2025-04-20T09:03:03Z` `COMMENTED` by `Ying1123` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780191428)
- `2025-04-20T09:17:49Z` `APPROVED` by `Ying1123` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780192292)
- `2025-04-20T21:00:51Z` `APPROVED` by `merrymercy` - Please add a test case and we can merge this soon! (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780331190)
- `2025-04-20T22:22:02Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780348824)
- `2025-04-20T22:41:27Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780351903)
- `2025-04-20T22:43:40Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780352256)
- `2025-04-20T23:09:22Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780356107)
- `2025-04-20T23:12:04Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780356535)
- `2025-04-21T02:11:16Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780422800)
- `2025-04-21T02:15:26Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780425339)
- `2025-04-21T03:14:37Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/5318#pullrequestreview-2780462791)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashattention_backend.py`: 14 inline comment(s)
- `python/sglang/srt/model_executor/model_runner.py`: 3 inline comment(s)
- `test/srt/run_suite.py`: 3 inline comment(s)
- `test/srt/test_fa3.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-17T19:37:56Z` `inline` by `zhyncs` `python/sglang/srt/layers/attention/flashattention_backend.py`:729; signals: attention, cache, tma; excerpt: "Do we always need to set return softmax lse to true? I think it may introduce overhead. Can we only use it for top ..." (https://github.com/sgl-project/sglang/pull/5318#discussion_r2049538315)
- `2025-04-20T23:12:03Z` `inline` by `hebiao064` `python/sglang/srt/model_executor/model_runner.py`:246; signals: flashinfer, mla; excerpt: "After we optimized the speed of TopK 1, we can remove it. The reason why we enable fa3 for MLA's spec decoding topk 1 ..." (https://github.com/sgl-project/sglang/pull/5318#discussion_r2051829633)
- `2025-04-13T00:02:29Z` `inline` by `zcnrex` `python/sglang/srt/layers/attention/flashattention_backend.py`:778; signals: attention, flashinfer; excerpt: "Do we need to check is flashinfer available here before using merge state" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2040800963)
- `2025-04-13T00:15:40Z` `inline` by `zhyncs` `python/sglang/srt/layers/attention/flashattention_backend.py`:778; signals: attention, kernel; excerpt: "Let’s migrate it to sgl-kernel" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2040810886)
- `2025-04-18T05:44:40Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/flashattention_backend.py`:272; signals: attention, compile; excerpt: "we need to disable torch compile to make it work" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2050084771)
- `2025-04-13T21:33:08Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/flashattention_backend.py`:1610; signals: attention; excerpt: "this is still needed for MM" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2041216949)
- `2025-04-14T02:18:29Z` `inline` by `qingquansong` `python/sglang/srt/layers/attention/flashattention_backend.py`:1610; signals: attention; excerpt: "yep yep, let me revert it. Thanks!" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2041308272)
- `2025-04-17T19:33:29Z` `inline` by `zhyncs` `python/sglang/srt/layers/attention/flashattention_backend.py`:272; signals: attention; excerpt: "@DefTruth" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2049532452)
- `2025-04-18T22:33:19Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/flashattention_backend.py`:272; signals: attention; excerpt: "added a todo for this line, will address it later" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2051193127)
- `2025-04-18T22:34:06Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/flashattention_backend.py`:729; signals: attention; excerpt: "make sense, addressed" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2051195216)
- `2025-04-19T21:58:39Z` `inline` by `zhyncs` `python/sglang/srt/model_executor/model_runner.py`:235; signals: mla; excerpt: "typo: MHA - MLA" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2051588486)
- `2025-04-20T22:41:27Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/flashattention_backend.py`:326; signals: attention; excerpt: "resolved, thanks. I didn't accepted your commit since I don't want to dismiss your approval :)" (https://github.com/sgl-project/sglang/pull/5318#discussion_r2051825102)
