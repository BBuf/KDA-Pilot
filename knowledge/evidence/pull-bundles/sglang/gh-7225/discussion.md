# PR Discussion Digest

- Source PR: [sgl-project/sglang#7225](https://github.com/sgl-project/sglang/pull/7225)
- Source page: `sources/prs/sglang/PR-7225.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7225`
- Generated at: `2026-05-20T15:31:07.138080+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-16T04:11:46Z`
- Merged: `2025-06-27T08:10:27Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 23 (approved=2, commented=21)
- Inline review comments: 35
- Review threads observed: 24
- Resolved/outdated thread markers: resolved=23, outdated=18
- Human participants with discussion text: Qiaolin-Yu, ch-wan, fzyzcjy, hebiao064
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-16T04:13:05Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @Qiaolin-Yu, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2930581526)
- `2025-06-16T04:15:13Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for compatibility between MTP (Multi-Token Prediction, likely speculative decoding) and TBO ... (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2930583552)
- `2025-06-18T10:52:01Z` `COMMENTED` by `fzyzcjy` - some optional nits (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2938708453)
- `2025-06-18T10:55:13Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2938733300)
- `2025-06-19T03:47:21Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2941458518)
- `2025-06-19T03:58:06Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2941469276)
- `2025-06-19T07:34:28Z` `COMMENTED` by `fzyzcjy` - only optional tiny nits (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2941908691)
- `2025-06-20T02:42:48Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2944406075)
- `2025-06-20T02:56:54Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2944418969)
- `2025-06-20T02:59:03Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2944420799)
- `2025-06-20T03:02:04Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2944424958)
- `2025-06-20T03:02:37Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2944425426)
- `2025-06-20T03:06:48Z` `APPROVED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2944430783)
- `2025-06-20T03:19:34Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2944442751)
- `2025-06-24T08:20:59Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2952664552)
- `2025-06-26T23:04:54Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2963975868)
- `2025-06-26T23:05:28Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2963978107)
- `2025-06-26T23:06:32Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2963981354)
- `2025-06-27T00:55:17Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2964247295)
- `2025-06-27T00:55:23Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2964247719)
- `2025-06-27T04:16:56Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2964673515)
- `2025-06-27T07:30:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces compatibility between Multi-Token Prediction (MTP) and two-batch overlap (TBO) by adjusting how ... (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2965118502)
- `2025-06-27T08:07:35Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2965293380)

## Inline Comment Hotspots

- `python/sglang/srt/two_batch_overlap.py`: 21 inline comment(s)
- `python/sglang/srt/layers/attention/tbo_backend.py`: 5 inline comment(s)
- `python/sglang/srt/model_executor/forward_batch_info.py`: 3 inline comment(s)
- `test/srt/test_dp_attention.py`: 2 inline comment(s)
- `python/sglang/srt/operations_strategy.py`: 2 inline comment(s)
- `python/sglang/srt/model_executor/cuda_graph_runner.py`: 1 inline comment(s)
- `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-18T10:43:53Z` `inline` by `fzyzcjy` `test/srt/test_dp_attention.py`:185; signals: attention, deepgemm, gemm; excerpt: "nit: no longer need to manually enable deepgemm - it is there by default (iirc)" (https://github.com/sgl-project/sglang/pull/7225#discussion_r2154281848)
- `2025-06-18T10:53:59Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/tbo_backend.py`:155; signals: attention; excerpt: "nit: I would personally feel the following is tiny slightly more readable what's more, maybe we should use the former unconditionally, i.e. since it ..." (https://github.com/sgl-project/sglang/pull/7225#discussion_r2154299737)
- `2025-06-19T07:31:43Z` `inline` by `fzyzcjy` `python/sglang/srt/two_batch_overlap.py`:30; signals: hang; excerpt: "question: shall we call it "token num per seq" (and change everywhere related), since I personally feel like: suppose we have batch size 256, ..." (https://github.com/sgl-project/sglang/pull/7225#discussion_r2156341079)
- `2025-06-18T10:43:24Z` `inline` by `fzyzcjy` `test/srt/test_dp_attention.py`:146; signals: attention; excerpt: "nit: looks like it is SGLANG TBO DEBUG" (https://github.com/sgl-project/sglang/pull/7225#discussion_r2154280951)
- `2025-06-18T10:52:36Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/tbo_backend.py`:134; signals: attention; excerpt: "e.g. for this seems we can unify as mentioned above" (https://github.com/sgl-project/sglang/pull/7225#discussion_r2154297329)
- `2025-06-18T10:54:07Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/tbo_backend.py`:249; signals: attention; excerpt: "(same as above)" (https://github.com/sgl-project/sglang/pull/7225#discussion_r2154299944)
- `2025-06-20T02:42:48Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/two_batch_overlap.py`:53; signals: hang; excerpt: "For TARGET VERIFY mode, is extend will return true. So I think we could not change the order?" (https://github.com/sgl-project/sglang/pull/7225#discussion_r2157934871)
- `2025-06-24T08:20:59Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/tbo_backend.py`:216; signals: attention; excerpt: "maybe split spec info into two microbatches" (https://github.com/sgl-project/sglang/pull/7225#discussion_r2163272566)
- `2025-06-18T10:52:01Z` `review` `COMMENTED` by `fzyzcjy`; signals: general review; excerpt: "some optional nits" (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2938708453)
- `2025-06-19T07:34:28Z` `review` `COMMENTED` by `fzyzcjy`; signals: general review; excerpt: "only optional tiny nits" (https://github.com/sgl-project/sglang/pull/7225#pullrequestreview-2941908691)
- `2025-06-18T10:45:30Z` `inline` by `fzyzcjy` `python/sglang/srt/model_executor/forward_batch_info.py`:355; signals: general review; excerpt: "nit: shall we put this logic inside TboForwardBatchPreparer.prepare to avoid copy-paste the logic twice" (https://github.com/sgl-project/sglang/pull/7225#discussion_r2154284671)
- `2025-06-18T10:49:27Z` `inline` by `fzyzcjy` `python/sglang/srt/two_batch_overlap.py`:367; signals: general review; excerpt: "nit: a bit worried whether this is too dynamic. I would personally suggest listing all extend blahblah manually to the existing long list, probably ..." (https://github.com/sgl-project/sglang/pull/7225#discussion_r2154291529)
