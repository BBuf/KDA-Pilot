# PR Discussion Digest

- Source PR: [triton-lang/triton#10099](https://github.com/triton-lang/triton/pull/10099)
- Source page: `sources/prs/triton/PR-10099.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10099`
- Generated at: `2026-05-20T15:33:20.034341+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-21T17:19:22Z`
- Merged: `2026-04-29T15:54:49Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 18
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: FrederickVu, Jokeren, antiagainst, lezcano, plognjen, yangshuxin
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-22T01:21:48Z` `COMMENTED` by `antiagainst` - The logic looks good to me but would appreicate @FrederickVu and @lezcano to review too. (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4151022344)
- `2026-04-22T09:03:40Z` `COMMENTED` by `lezcano` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4153258138)
- `2026-04-22T17:32:33Z` `COMMENTED` by `plognjen` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4156701719)
- `2026-04-22T17:36:59Z` `COMMENTED` by `plognjen` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4156725798)
- `2026-04-23T02:11:15Z` `COMMENTED` by `FrederickVu` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4159113820)
- `2026-04-23T08:13:14Z` `COMMENTED` by `lezcano` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4160759784)
- `2026-04-24T17:02:02Z` `COMMENTED` by `yangshuxin` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4172180322)
- `2026-04-24T17:18:12Z` `COMMENTED` by `lezcano` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4172261143)
- `2026-04-24T18:11:31Z` `COMMENTED` by `yangshuxin` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4172533283)
- `2026-04-24T19:11:19Z` `COMMENTED` by `lezcano` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4172844747)
- `2026-04-24T20:52:18Z` `COMMENTED` by `Jokeren` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4173331946)
- `2026-04-28T15:07:38Z` `COMMENTED` by `plognjen` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4190012210)
- `2026-04-28T17:32:00Z` `COMMENTED` by `FrederickVu` (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4191094009)
- `2026-04-29T09:33:36Z` `APPROVED` by `lezcano` - SGTM, but please address the other comments (in particular, the one about further testing) (https://github.com/triton-lang/triton/pull/10099#pullrequestreview-4195673118)

## Inline Comment Hotspots

- `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`: 16 inline comment(s)
- `python/test/gluon/test_lowerings.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-24T18:11:31Z` `inline` by `yangshuxin` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: block, layout, memory, shared memory, triton; excerpt: "@lezcano thank you very much for the quick reply. I don't see how the CGA layout of [0, 0] in your example would trigger ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3139529057)
- `2026-04-24T17:02:02Z` `inline` by `yangshuxin` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: block, cuda, layout, triton; excerpt: "So, for kBlock we disallow having a non-trivial block dimension in the verifie @lezcano could you please elaborate bit more about the contraints. I ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3139200873)
- `2026-04-22T08:59:58Z` `inline` by `lezcano` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: block, memory, triton; excerpt: "So, for kBlock we disallow having a non-trivial block dimension in the verifier. Do you really want to support having a non-trivial partition dimension? ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3122764493)
- `2026-04-22T09:03:31Z` `inline` by `lezcano` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: block, layout, triton; excerpt: "The reason why we disabled kBlocks here is because otherwise you could have a layout that broadcasts over kBlock, then you could take a ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3122788780)
- `2026-04-22T17:36:59Z` `inline` by `plognjen` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:579; signals: kernel, layout, triton; excerpt: "Yes, padded encoding was supported in the verifier and I think we use it a lot in kernel development, since gfx1250 basically uses only ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3125819766)
- `2026-04-22T17:32:33Z` `inline` by `plognjen` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: kernel, triton; excerpt: "We do seem to have use cases. I implemented this on the request of @knwng. Some of his kernels broke in the verifier when ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3125798005)
- `2026-04-23T08:13:13Z` `inline` by `lezcano` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:579; signals: layout, triton; excerpt: "ah, yes, now I remember when I run the maths for slicing a padded layout. I was also quite surprised that it worked the ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3129304914)
- `2026-04-24T17:18:12Z` `inline` by `lezcano` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: layout, triton; excerpt: "Say you have something split like This is what we don't allow, as splitting along, say, a cga layout = [[1, 0]] (splitting along ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3139274453)
- `2026-04-28T15:07:38Z` `inline` by `plognjen` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: layout, triton; excerpt: "Let's get back to this patch. @lezcano if the concern is that the layout will broadcast across partition dim, we can just add same ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3155166449)
- `2026-04-28T17:31:59Z` `inline` by `FrederickVu` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: block, triton; excerpt: "Yeah, if we can never broadcast across partitions, then I see no reason to add that to the verifier. Concerning the block dimension check ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3156064773)
- `2026-04-29T09:32:48Z` `inline` by `lezcano` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:567; signals: block, triton; excerpt: "Concerning the block dimension check in the verifier, it seems like the concern was that a user could store different data in different CTAs ..." (https://github.com/triton-lang/triton/pull/10099#discussion_r3159920061)
- `2026-04-22T08:47:34Z` `inline` by `lezcano` `lib/Conversion/TritonGPUToLLVM/ViewOpToLLVM.cpp`:579; signals: triton; excerpt: "do we only support padded encoding in this path? Isn't padded encoding supported in this path? It feels a bit asymmetric." (https://github.com/triton-lang/triton/pull/10099#discussion_r3122669488)
