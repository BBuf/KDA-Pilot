# PR Discussion Digest

- Source PR: [sgl-project/sglang#5113](https://github.com/sgl-project/sglang/pull/5113)
- Source page: `sources/prs/sglang/PR-5113.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5113`
- Generated at: `2026-05-20T15:30:20.007847+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-07T05:57:55Z`
- Merged: `2025-04-16T05:01:23Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: Fridge003, qingquansong, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-11T05:04:06Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2759151197)
- `2025-04-11T05:39:51Z` `COMMENTED` by `qingquansong` - A general question, have we considered using num splits 0 see if it can chunked kv directly inside ... (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2759192971)
- `2025-04-11T05:58:16Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2759219053)
- `2025-04-13T20:14:53Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2762834025)
- `2025-04-13T20:37:30Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2762838202)
- `2025-04-16T00:20:29Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2770263889)
- `2025-04-16T01:59:53Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2770431624)
- `2025-04-16T04:19:33Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2770647497)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 4 inline comment(s)
- `python/sglang/srt/layers/attention/flashattention_backend.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-11T06:56:59Z` `issue` by `qingquansong`; signals: attention, cache, flash attention, kv cache, memory, mla, tiling, tma; excerpt: "A general question, have we considered using num splits 0 see if it can chunked kv directly inside the FA3 without doing the outer ..." (https://github.com/sgl-project/sglang/pull/5113#issuecomment-2796021343)
- `2025-04-11T07:41:56Z` `issue` by `Fridge003`; signals: attention, cache, flash attention, kv cache, memory, mla, tiling, tma; excerpt: "A general question, have we considered using num splits 0 see if it can chunked kv directly inside the FA3 without doing the outer ..." (https://github.com/sgl-project/sglang/pull/5113#issuecomment-2796107165)
- `2025-04-11T06:07:11Z` `issue` by `Fridge003`; signals: attention, cache, flash attention, kv cache, memory, mla; excerpt: "A general question, have we considered using num splits 0 see if it can chunked kv directly inside the FA3 without doing the outer ..." (https://github.com/sgl-project/sglang/pull/5113#issuecomment-2795919232)
- `2025-04-11T05:58:16Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashattention_backend.py`:606; signals: attention, cache; excerpt: "It's not feasible since this feature doesn't use the latent cache during attention. Maybe I can turn this feature into optional so it can ..." (https://github.com/sgl-project/sglang/pull/5113#discussion_r2038847467)
- `2025-04-13T20:14:53Z` `inline` by `qingquansong` `python/sglang/srt/models/deepseek_v2.py`:1066; signals: accuracy, flashinfer; excerpt: "Somehow I found the merge state implementation in flashinfer has some accuracy gap with vllm v1 ? cc @zhyncs" (https://github.com/sgl-project/sglang/pull/5113#discussion_r2041201715)
- `2025-04-11T05:04:06Z` `inline` by `qingquansong` `python/sglang/srt/layers/attention/flashattention_backend.py`:606; signals: attention; excerpt: "shall we still using kvcahe api? I vaguely remember varlen does not provide the args for page table to support page size 1 although ..." (https://github.com/sgl-project/sglang/pull/5113#discussion_r2038803993)
- `2025-04-11T05:39:51Z` `review` `COMMENTED` by `qingquansong`; signals: general review; excerpt: "A general question, have we considered using num splits 0 see if it can chunked kv directly inside the FA3 without doing the outer ..." (https://github.com/sgl-project/sglang/pull/5113#pullrequestreview-2759192971)
- `2025-04-13T20:37:30Z` `inline` by `zhyncs` `python/sglang/srt/models/deepseek_v2.py`:1066; signals: general review; excerpt: "ref" (https://github.com/sgl-project/sglang/pull/5113#discussion_r2041206152)
- `2025-04-16T00:20:29Z` `inline` by `zhyncs` `python/sglang/srt/models/deepseek_v2.py`:1057; signals: general review; excerpt: "Move to the top" (https://github.com/sgl-project/sglang/pull/5113#discussion_r2045762746)
- `2025-04-16T01:59:53Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:1057; signals: general review; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/5113#discussion_r2045860381)
