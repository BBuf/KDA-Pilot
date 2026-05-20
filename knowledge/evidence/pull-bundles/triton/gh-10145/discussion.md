# PR Discussion Digest

- Source PR: [triton-lang/triton#10145](https://github.com/triton-lang/triton/pull/10145)
- Source page: `sources/prs/triton/PR-10145.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10145`
- Generated at: `2026-05-20T15:33:23.458804+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-27T19:33:51Z`
- Merged: `2026-04-29T15:50:17Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, changes_requested=1, commented=2)
- Inline review comments: 14
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=11, outdated=13
- Human participants with discussion text: antiagainst, peterbell10, plognjen
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-28T01:18:01Z` `CHANGES_REQUESTED` by `antiagainst` - Nice. Overall looks good; just few nits. (https://github.com/triton-lang/triton/pull/10145#pullrequestreview-4184837223)
- `2026-04-29T10:07:14Z` `COMMENTED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10145#pullrequestreview-4195928975)
- `2026-04-29T13:15:32Z` `COMMENTED` by `plognjen` (https://github.com/triton-lang/triton/pull/10145#pullrequestreview-4197258054)
- `2026-04-29T15:44:59Z` `APPROVED` by `antiagainst` (https://github.com/triton-lang/triton/pull/10145#pullrequestreview-4198522002)

## Inline Comment Hotspots

- `python/triton/experimental/gluon/language/_layouts.py`: 12 inline comment(s)
- `python/triton/experimental/gluon/language/__init__.py`: 1 inline comment(s)
- `third_party/amd/lib/TritonAMDGPUToLLVM/DotOpToLLVM.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-27T23:58:01Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:747; signals: gemm, layout, triton; excerpt: "I don't think we want to anchor on gemm, which is a particular problem, that much? What about make partitioned dot layouts given it's ..." (https://github.com/triton-lang/triton/pull/10145#discussion_r3150801172)
- `2026-04-28T00:09:51Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:709; signals: block, layout, triton; excerpt: "Nit: I'd suggest to order parameters as .., partition dim, num partitions, block dim size, ... to be more logically grouped." (https://github.com/triton-lang/triton/pull/10145#discussion_r3150835588)
- `2026-04-28T00:10:27Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:714; signals: block, layout, triton; excerpt: "Nit: further explain that block dim size is the M/N dim for A/B operand. Or maybe name it as block mn dim size or ..." (https://github.com/triton-lang/triton/pull/10145#discussion_r3150837304)
- `2026-04-27T23:44:51Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/__init__.py`:104; signals: layout, triton; excerpt: "PartitionedSharedLayout is not exposed into common paths. So we should scope these to be under amd/ paths too." (https://github.com/triton-lang/triton/pull/10145#discussion_r3150764841)
- `2026-04-27T23:56:54Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:759; signals: layout, triton; excerpt: "I don't understand why naming it as sublayout, which indicates a slice of something. This is more original layout or unpartitioned layout or something?" (https://github.com/triton-lang/triton/pull/10145#discussion_r3150798047)
- `2026-04-28T00:01:01Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:739; signals: layout, triton; excerpt: "Not sure we want this: it doesn't provide more value than a simple tuple, but the cost is we introduce a core language construct ..." (https://github.com/triton-lang/triton/pull/10145#discussion_r3150812413)
- `2026-04-29T13:15:32Z` `inline` by `plognjen` `python/triton/experimental/gluon/language/_layouts.py`:759; signals: layout, triton; excerpt: "hmm, I used to call it sublayout or inner-layout throughout the codebase since it's a layout within single partition (similar to slice). However I ..." (https://github.com/triton-lang/triton/pull/10145#discussion_r3161256012)
- `2026-04-27T23:50:40Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:709; signals: layout, triton; excerpt: "This and the following should be placed under amd.gfx1250." (https://github.com/triton-lang/triton/pull/10145#discussion_r3150782138)
- `2026-04-27T23:56:15Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:755; signals: layout, triton; excerpt: "What does "cycle" mean here? Typo or something?" (https://github.com/triton-lang/triton/pull/10145#discussion_r3150796626)
- `2026-04-28T00:07:49Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:784; signals: layout, triton; excerpt: "Nice doc and clean impl below; thanks!" (https://github.com/triton-lang/triton/pull/10145#discussion_r3150830453)
- `2026-04-28T00:08:36Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:709; signals: layout, triton; excerpt: "make partitioned dot operand layout to be clear?" (https://github.com/triton-lang/triton/pull/10145#discussion_r3150832332)
- `2026-04-28T01:05:19Z` `inline` by `antiagainst` `python/triton/experimental/gluon/language/_layouts.py`:849; signals: layout, triton; excerpt: "We might want to add some test frontend.py tests given the non-trivial logic here." (https://github.com/triton-lang/triton/pull/10145#discussion_r3150990777)
