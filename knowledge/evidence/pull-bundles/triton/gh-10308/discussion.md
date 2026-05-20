# PR Discussion Digest

- Source PR: [triton-lang/triton#10308](https://github.com/triton-lang/triton/pull/10308)
- Source page: `sources/prs/triton/PR-10308.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10308`
- Generated at: `2026-05-20T15:33:32.304362+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-14T00:03:54Z`
- Merged: `2026-05-15T16:59:10Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: ThomasRaoux, pawelszczerbuk, peterbell10
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-14T00:33:10Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4286323169)
- `2026-05-14T00:55:58Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4286403468)
- `2026-05-14T15:14:01Z` `COMMENTED` by `pawelszczerbuk` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4291079607)
- `2026-05-14T16:32:48Z` `COMMENTED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4291630447)
- `2026-05-14T18:52:41Z` `COMMENTED` by `pawelszczerbuk` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4292572900)
- `2026-05-14T21:56:42Z` `APPROVED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4293713761)
- `2026-05-14T22:13:11Z` `COMMENTED` by `pawelszczerbuk` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4293802332)
- `2026-05-14T22:34:17Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4293906112)
- `2026-05-15T14:00:03Z` `COMMENTED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10308#pullrequestreview-4298691552)

## Inline Comment Hotspots

- `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`: 9 inline comment(s)

## High-Signal Discussion

- `2026-05-14T22:13:11Z` `inline` by `pawelszczerbuk` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:265; signals: layout, tmem, triton, warp; excerpt: "this was added because getDistributedLayoutForTmemLdSt asserts: so we are not only limited by the HW (numWarps % 4 == 0) but also by the ..." (https://github.com/triton-lang/triton/pull/10308#discussion_r3244582645)
- `2026-05-14T15:14:01Z` `inline` by `pawelszczerbuk` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:450; signals: hang, triton; excerpt: "I wanted to exclude the barriers, but in the hindsight this doesn't really make sense. Let me remove these, will make the change much ..." (https://github.com/triton-lang/triton/pull/10308#discussion_r3242325975)
- `2026-05-14T18:52:41Z` `inline` by `pawelszczerbuk` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:188; signals: nan, triton; excerpt: "This code is only used when the allocation is of integer type - I wanted to initialize these to consistent NaN bit patterns, but ..." (https://github.com/triton-lang/triton/pull/10308#discussion_r3243568940)
- `2026-05-14T22:34:17Z` `inline` by `ThomasRaoux` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:265; signals: triton, warp; excerpt: "I see, yeah I guess we shouldn't allow non power of 2 num warps so not sure why we have this. Could just be ..." (https://github.com/triton-lang/triton/pull/10308#discussion_r3244662691)
- `2026-05-14T21:55:37Z` `inline` by `ThomasRaoux` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:265; signals: triton, warp; excerpt: "nit: technically it is numWarps % 4 == 0?" (https://github.com/triton-lang/triton/pull/10308#discussion_r3244511883)
- `2026-05-14T00:33:10Z` `inline` by `ThomasRaoux` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:455; signals: triton; excerpt: "why do we need this check?" (https://github.com/triton-lang/triton/pull/10308#discussion_r3238264351)
- `2026-05-14T00:55:58Z` `inline` by `ThomasRaoux` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:450; signals: triton; excerpt: "why can't we just walk through all the allocs?" (https://github.com/triton-lang/triton/pull/10308#discussion_r3238335947)
- `2026-05-14T16:32:48Z` `inline` by `peterbell10` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:188; signals: triton; excerpt: "What about bfloat16?" (https://github.com/triton-lang/triton/pull/10308#discussion_r3242805321)
- `2026-05-15T14:00:03Z` `inline` by `peterbell10` `lib/Dialect/TritonInstrument/Transforms/ConcurrencySanitizer.cpp`:188; signals: triton; excerpt: "Ah missed that this was only used for integer allocations. Sorry for the noise." (https://github.com/triton-lang/triton/pull/10308#discussion_r3248684208)
