# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1675](https://github.com/flashinfer-ai/flashinfer/pull/1675)
- Source page: `sources/prs/flashinfer/PR-1675.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1675`
- Generated at: `2026-05-20T15:23:12.616642+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-11T20:26:49Z`
- Merged: `2025-09-15T06:40:42Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 11
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=2, outdated=5
- Human participants with discussion text: Edenzzzz, Fridge003, MasterJH5574, happierpig, yzh119
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-09-11T20:27:13Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @Edenzzzz, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3213526385)
- `2025-09-11T20:28:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a fixed split size parameter to enable batch-invariant attention computation in prefill ... (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3213532905)
- `2025-09-11T20:31:02Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3213539348)
- `2025-09-11T22:50:10Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3213846529)
- `2025-09-12T00:30:21Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3214088202)
- `2025-09-14T04:35:57Z` `COMMENTED` by `yzh119` - LGTM in general, left some minor suggestions. (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3221733827)
- `2025-09-14T15:38:34Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3222184000)
- `2025-09-15T06:40:36Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1675#pullrequestreview-3223110072)

## Inline Comment Hotspots

- `tests/test_invariant_batch_decode.py`: 4 inline comment(s)
- `tvm_binding/batch_prefill.cu`: 3 inline comment(s)
- `csrc/batch_prefill.cu`: 2 inline comment(s)
- `flashinfer/decode.py`: 1 inline comment(s)
- `flashinfer/prefill.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-13T13:20:13Z` `issue` by `Edenzzzz`; signals: attention, cache, hang, kernel, kv cache; excerpt: "I'm worried about the use cases where we manually merge attention outputs from different KV components (e.g. in chunked-prefill, speculative decoding), it's okay to ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3288352715)
- `2025-09-11T22:50:22Z` `issue` by `yzh119`; signals: attention, hang, kernel; excerpt: "One minor note, the attention merge kernel ( uses parallel reduction, I'm not sure if we need to change it to sequential reduction to ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3282870180)
- `2025-09-13T19:09:14Z` `issue` by `Fridge003`; signals: attention, cache, hang; excerpt: "I'm worried about the use cases where we manually merge attention outputs from different KV components (e.g. in chunked-prefill, speculative decoding), it's okay to ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3288744561)
- `2025-09-11T22:15:58Z` `issue` by `yzh119`; signals: flashinfer, hang; excerpt: "The easiest way to turn off split-k in flashinfer is to change these two lines to std::numeric limits ::max(): 1. 2." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3282799163)
- `2025-09-12T00:43:24Z` `issue` by `Edenzzzz`; signals: block, hang; excerpt: "Though I thought the threads in a block just collectively reduce along the head dim, one position & head at a time in threadblock ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3283101745)
- `2025-09-12T03:41:46Z` `issue` by `Edenzzzz`; signals: hang, kernel; excerpt: "It matters if you want to guarantee the reproducibility across prefill and decode, my question is what kind of reproducibility do you want to ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3283537966)
- `2025-09-12T17:18:05Z` `issue` by `happierpig`; signals: attention, hang; excerpt: "the order might change for different kv-length. I think the current merge states should be fine for the batch-invariant reproducibility (which IMO means a ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3286216249)
- `2025-09-11T22:25:08Z` `issue` by `Edenzzzz`; signals: perf, performance; excerpt: "Yes, but simply turning it off would hurt performance" (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3282823611)
- `2025-09-12T03:34:38Z` `issue` by `yzh119`; signals: hang; excerpt: "@happierpig has done some work on changing the reduction order before. As long as changing one request's kv len doesn't affect other requests, it ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3283527611)
- `2025-09-12T20:48:28Z` `issue` by `Edenzzzz`; signals: cuda; excerpt: "One more note, in the case of CUDA graph, we can binary-search a split size that just launches below max batch size if split ..." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3286782456)
- `2025-09-12T22:10:18Z` `issue` by `Fridge003`; signals: cuda; excerpt: "Do we need to add a flag for disabling split-kv? Since finally we want to use cuda graph for decoding." (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3286977582)
- `2025-09-12T22:55:32Z` `issue` by `Edenzzzz`; signals: cuda; excerpt: "Do we need to add a flag for disabling split-kv? Since finally we want to use cuda graph for decoding. It should work now" (https://github.com/flashinfer-ai/flashinfer/pull/1675#issuecomment-3287046666)
