# PR Discussion Digest

- Source PR: [sgl-project/sglang#12491](https://github.com/sgl-project/sglang/pull/12491)
- Source page: `sources/prs/sglang/PR-12491.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12491`
- Generated at: `2026-05-20T15:27:39.738760+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-01T13:30:10Z`
- Merged: `2025-11-26T16:00:22Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 14
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: MichelleWu351, hnyls2002
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-01T13:32:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for mixed-chunk batches in the Ascend backend, which is a significant ... (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3407536722)
- `2025-11-03T02:27:02Z` `COMMENTED` by `MichelleWu351` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3409238154)
- `2025-11-12T11:39:01Z` `COMMENTED` by `hnyls2002` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3453002582)
- `2025-11-12T12:03:23Z` `COMMENTED` by `MichelleWu351` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3453087992)
- `2025-11-13T01:27:05Z` `COMMENTED` by `MichelleWu351` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3453146339)
- `2025-11-13T11:24:51Z` `COMMENTED` by `MichelleWu351` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3459321603)
- `2025-11-13T18:57:25Z` `COMMENTED` by `hnyls2002` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3461229737)
- `2025-11-13T18:57:42Z` `COMMENTED` by `hnyls2002` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3461230739)
- `2025-11-26T16:00:07Z` `APPROVED` by `hnyls2002` (https://github.com/sgl-project/sglang/pull/12491#pullrequestreview-3511662270)

## Inline Comment Hotspots

- `python/sglang/srt/mem_cache/allocator.py`: 6 inline comment(s)
- `python/sglang/srt/layers/attention/ascend_backend.py`: 3 inline comment(s)
- `python/sglang/srt/layers/attention/base_attn_backend.py`: 3 inline comment(s)
- `python/sglang/srt/managers/schedule_policy.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-12T11:38:06Z` `inline` by `hnyls2002` `python/sglang/srt/mem_cache/allocator.py`:561; signals: cache, memory; excerpt: "Why is this needed? I think our memory allocation / deallocation should promise that the pages are always unique." (https://github.com/sgl-project/sglang/pull/12491#discussion_r2517967834)
- `2025-11-12T12:03:23Z` `inline` by `MichelleWu351` `python/sglang/srt/mem_cache/allocator.py`:561; signals: cache, memory; excerpt: "I added this line of code to solve the problem that when enabling enable-mixed-chunk and enable overlap causes pages to be freed multiple times, ..." (https://github.com/sgl-project/sglang/pull/12491#discussion_r2518036073)
- `2025-11-13T01:22:39Z` `inline` by `MichelleWu351` `python/sglang/srt/layers/attention/base_attn_backend.py`:100; signals: attention, hang; excerpt: "Does this influence other backends? We previously did not have this. You are correct. When enabling enable-mixed-chunk , it can affect other backends. I ..." (https://github.com/sgl-project/sglang/pull/12491#discussion_r2520660289)
- `2025-11-13T11:24:51Z` `inline` by `MichelleWu351` `python/sglang/srt/mem_cache/allocator.py`:561; signals: cache, memory; excerpt: "Why is this needed? I think our memory allocation / deallocation should promise that the pages are always unique. After I merge the new ..." (https://github.com/sgl-project/sglang/pull/12491#discussion_r2523091126)
- `2025-11-12T12:16:21Z` `inline` by `MichelleWu351` `python/sglang/srt/managers/schedule_policy.py`:556; signals: memory; excerpt: "Line 438, extend input len = self.ceil paged tokens(extend input len), ensures that the prefill will not out of memory. However, after line 422, ..." (https://github.com/sgl-project/sglang/pull/12491#discussion_r2518081717)
- `2025-11-03T02:27:02Z` `inline` by `MichelleWu351` `python/sglang/srt/mem_cache/allocator.py`:561; signals: cache; excerpt: "I want to sort the free pages tensor before picking the unique elements." (https://github.com/sgl-project/sglang/pull/12491#discussion_r2485182913)
- `2025-11-12T11:38:40Z` `inline` by `hnyls2002` `python/sglang/srt/layers/attention/base_attn_backend.py`:100; signals: attention; excerpt: "Does this influence other backends? We previously did not have this." (https://github.com/sgl-project/sglang/pull/12491#discussion_r2517969324)
- `2025-11-13T18:57:25Z` `inline` by `hnyls2002` `python/sglang/srt/mem_cache/allocator.py`:561; signals: cache; excerpt: "Great, we really do not need it" (https://github.com/sgl-project/sglang/pull/12491#discussion_r2524592418)
- `2025-11-13T18:57:42Z` `inline` by `hnyls2002` `python/sglang/srt/layers/attention/base_attn_backend.py`:100; signals: attention; excerpt: "Great" (https://github.com/sgl-project/sglang/pull/12491#discussion_r2524593287)
- `2025-11-12T11:38:54Z` `inline` by `hnyls2002` `python/sglang/srt/managers/schedule_policy.py`:556; signals: general review; excerpt: "Why about this?" (https://github.com/sgl-project/sglang/pull/12491#discussion_r2517970082)
