# PR Discussion Digest

- Source PR: [sgl-project/sglang#6509](https://github.com/sgl-project/sglang/pull/6509)
- Source page: `sources/prs/sglang/PR-6509.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6509`
- Generated at: `2026-05-20T15:30:43.499780+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-21T23:17:20Z`
- Merged: `2025-05-30T08:11:53Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: Alcanderian, Fridge003, NorthmanPKU
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-22T19:21:31Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2862331100)
- `2025-05-22T21:30:45Z` `COMMENTED` by `NorthmanPKU` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2862611952)
- `2025-05-22T21:30:57Z` `COMMENTED` by `NorthmanPKU` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2862612244)
- `2025-05-24T05:04:16Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2866135918)
- `2025-05-24T06:40:32Z` `COMMENTED` by `NorthmanPKU` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2866186976)
- `2025-05-26T05:10:22Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2867191201)
- `2025-05-26T21:40:10Z` `COMMENTED` by `NorthmanPKU` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2869181221)
- `2025-05-26T21:40:26Z` `COMMENTED` by `NorthmanPKU` (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2869181412)
- `2025-05-27T01:29:17Z` `APPROVED` by `Fridge003` - LGTM (https://github.com/sgl-project/sglang/pull/6509#pullrequestreview-2869326087)

## Inline Comment Hotspots

- `test/srt/test_triton_sliding_window.py`: 4 inline comment(s)
- `python/sglang/srt/layers/attention/triton_backend.py`: 2 inline comment(s)
- `python/sglang/srt/models/gemma3_causal.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-22T19:18:15Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/triton_backend.py`:239; signals: attention, cuda, flashinfer, triton; excerpt: "These procedures of initializing kv lens and kv indices seem to be similar acorss init forward metadata, init forward metadata capture cuda graph and ..." (https://github.com/sgl-project/sglang/pull/6509#discussion_r2103247001)
- `2025-05-26T21:40:26Z` `inline` by `NorthmanPKU` `test/srt/test_triton_sliding_window.py`:36; signals: gemm, hang, triton; excerpt: "Changed it to gemma-3-4b-it." (https://github.com/sgl-project/sglang/pull/6509#discussion_r2107871058)
- `2025-05-24T06:40:32Z` `inline` by `NorthmanPKU` `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`:56; signals: attention, triton; excerpt: "For now there could at most be 2 values, one for window size and one for -1 (global attention). So yes I shall define ..." (https://github.com/sgl-project/sglang/pull/6509#discussion_r2105728786)
- `2025-05-26T04:53:46Z` `inline` by `Fridge003` `test/srt/test_triton_sliding_window.py`:36; signals: gemm, triton; excerpt: "Is tp=8 necessary for launching gemma-3-27b-it? For ci test we had better use a smaller model that can be launched on a single gpu" (https://github.com/sgl-project/sglang/pull/6509#discussion_r2106506919)
- `2025-05-22T19:21:22Z` `inline` by `Fridge003` `python/sglang/srt/models/gemma3_causal.py`:281; signals: gemm, triton; excerpt: "Can you add a test for a sliding window model with triton backend? It should be put under test/srt" (https://github.com/sgl-project/sglang/pull/6509#discussion_r2103251497)
- `2025-05-22T21:30:45Z` `inline` by `NorthmanPKU` `python/sglang/srt/layers/attention/triton_backend.py`:239; signals: attention, triton; excerpt: "Make sense!" (https://github.com/sgl-project/sglang/pull/6509#discussion_r2103426806)
- `2025-05-24T05:04:16Z` `inline` by `Alcanderian` `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`:56; signals: attention, triton; excerpt: "Is this const for each model?" (https://github.com/sgl-project/sglang/pull/6509#discussion_r2105707491)
- `2025-05-22T21:30:57Z` `inline` by `NorthmanPKU` `python/sglang/srt/models/gemma3_causal.py`:281; signals: gemm; excerpt: "ok" (https://github.com/sgl-project/sglang/pull/6509#discussion_r2103427003)
- `2025-05-26T04:34:25Z` `inline` by `Fridge003` `test/srt/test_triton_sliding_window.py`:1; signals: triton; excerpt: "This test can be added to test/srt/run suite.py to trigger CI." (https://github.com/sgl-project/sglang/pull/6509#discussion_r2106490688)
- `2025-05-26T21:40:09Z` `inline` by `NorthmanPKU` `test/srt/test_triton_sliding_window.py`:1; signals: triton; excerpt: "OK👌" (https://github.com/sgl-project/sglang/pull/6509#discussion_r2107870843)
