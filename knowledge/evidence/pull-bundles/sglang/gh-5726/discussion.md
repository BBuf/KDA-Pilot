# PR Discussion Digest

- Source PR: [sgl-project/sglang#5726](https://github.com/sgl-project/sglang/pull/5726)
- Source page: `sources/prs/sglang/PR-5726.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5726`
- Generated at: `2026-05-20T15:30:29.963211+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-25T00:35:33Z`
- Merged: `2025-04-28T16:33:21Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: ByronHsu, whybeyoung
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-26T21:15:03Z` `COMMENTED` by `ByronHsu` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2796441953)
- `2025-04-27T05:39:45Z` `COMMENTED` by `whybeyoung` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2797325520)
- `2025-04-27T06:01:20Z` `COMMENTED` by `ByronHsu` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2797348137)
- `2025-04-27T06:01:56Z` `COMMENTED` by `ByronHsu` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2797349130)
- `2025-04-27T06:02:37Z` `COMMENTED` by `whybeyoung` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2797350072)
- `2025-04-27T06:12:46Z` `COMMENTED` by `whybeyoung` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2797368680)
- `2025-04-27T06:15:10Z` `COMMENTED` by `whybeyoung` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2797369503)
- `2025-04-28T16:30:31Z` `APPROVED` by `ByronHsu` (https://github.com/sgl-project/sglang/pull/5726#pullrequestreview-2799952040)

## Inline Comment Hotspots

- `python/sglang/srt/entrypoints/http_server.py`: 4 inline comment(s)
- `python/sglang/srt/disaggregation/decode.py`: 2 inline comment(s)
- `python/sglang/srt/disaggregation/prefill.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-27T06:12:46Z` `inline` by `whybeyoung` `python/sglang/srt/entrypoints/http_server.py`:829; signals: cache, cuda, deepgemm, gemm, perf; excerpt: "I want to use it to trigger the DeepGEMM precache operation under each DP (Data Parallel) rank, because the precache mechanism mentioned earlier ( ..." (https://github.com/sgl-project/sglang/pull/5726#discussion_r2062383032)
- `2025-04-26T21:14:49Z` `inline` by `ByronHsu` `python/sglang/srt/disaggregation/prefill.py`:121; signals: oom; excerpt: "we can just use bootstrap room to determine warmup request because LB always gives non negative room id" (https://github.com/sgl-project/sglang/pull/5726#discussion_r2061618639)
- `2025-04-27T05:39:45Z` `inline` by `whybeyoung` `python/sglang/srt/disaggregation/prefill.py`:121; signals: oom; excerpt: "as we talked in slac. this bootstrap room can't be fake , we should use fake bootstrap host only" (https://github.com/sgl-project/sglang/pull/5726#discussion_r2062349158)
- `2025-04-27T06:15:10Z` `inline` by `whybeyoung` `python/sglang/srt/entrypoints/http_server.py`:845; signals: general review; excerpt: "We can do it this way, but I'm not entirely sure if it's absolutely necessary. If it is, I can add it." (https://github.com/sgl-project/sglang/pull/5726#discussion_r2062383858)
- `2025-04-26T21:13:25Z` `inline` by `ByronHsu` `python/sglang/srt/disaggregation/decode.py`:140; signals: general review; excerpt: "can we just have a "fake" transfer backend and get rid of fake transfer?" (https://github.com/sgl-project/sglang/pull/5726#discussion_r2061617484)
- `2025-04-27T06:01:17Z` `inline` by `ByronHsu` `python/sglang/srt/entrypoints/http_server.py`:845; signals: general review; excerpt: "why not warmup on decode?" (https://github.com/sgl-project/sglang/pull/5726#discussion_r2062366904)
- `2025-04-27T06:01:53Z` `inline` by `ByronHsu` `python/sglang/srt/entrypoints/http_server.py`:829; signals: general review; excerpt: "why does it matter if we are using fake sender?" (https://github.com/sgl-project/sglang/pull/5726#discussion_r2062367713)
- `2025-04-27T06:02:36Z` `inline` by `whybeyoung` `python/sglang/srt/disaggregation/decode.py`:140; signals: general review; excerpt: "good point ." (https://github.com/sgl-project/sglang/pull/5726#discussion_r2062368369)
