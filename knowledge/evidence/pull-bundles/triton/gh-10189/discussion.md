# PR Discussion Digest

- Source PR: [triton-lang/triton#10189](https://github.com/triton-lang/triton/pull/10189)
- Source page: `sources/prs/triton/PR-10189.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10189`
- Generated at: `2026-05-20T15:33:26.052896+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-30T23:55:02Z`
- Merged: `2026-05-12T20:20:03Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: Jokeren, ThomasRaoux, leijurv, peterbell10, saagarjha
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-01T00:03:31Z` `COMMENTED` by `Jokeren` - I'm not clear about this PR. Do you need to handle returned tensors in LLVM lowering? (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4209229845)
- `2026-05-04T16:00:17Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4221551097)
- `2026-05-04T17:21:28Z` `COMMENTED` by `leijurv` (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4222030967)
- `2026-05-04T17:24:32Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4222052348)
- `2026-05-06T19:40:40Z` `APPROVED` by `peterbell10` - Makes sense to me. A tensor is lowered as a vector, and llvm can return vectors just fine. ... (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4238960315)
- `2026-05-08T22:33:24Z` `APPROVED` by `ThomasRaoux` - LGTM (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4255805005)

## Inline Comment Hotspots

- `python/test/unit/language/test_core.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-05-06T19:40:40Z` `review` `APPROVED` by `peterbell10`; signals: compile, layout, perf, performance, vector; excerpt: "Makes sense to me. A tensor is lowered as a vector, and llvm can return vectors just fine. I doubt the layout choices will ..." (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4238960315)
- `2026-05-01T06:19:26Z` `issue` by `saagarjha`; signals: layout, triton; excerpt: "If you don't apply this PR then you TritonToTritonGPU will fail because the tensor that is returned will not have a layout." (https://github.com/triton-lang/triton/pull/10189#issuecomment-4358125922)
- `2026-05-01T12:50:21Z` `issue` by `Jokeren`; signals: layout, triton; excerpt: "If you don't apply this PR then you TritonToTritonGPU will fail because the tensor that is returned will not have a layout. Why do ..." (https://github.com/triton-lang/triton/pull/10189#issuecomment-4359342385)
- `2026-05-01T00:03:31Z` `review` `COMMENTED` by `Jokeren`; signals: general review; excerpt: "I'm not clear about this PR. Do you need to handle returned tensors in LLVM lowering?" (https://github.com/triton-lang/triton/pull/10189#pullrequestreview-4209229845)
- `2026-05-01T15:41:53Z` `issue` by `saagarjha`; signals: triton; excerpt: "If you make a call it's going to return a tensor? We have some code that does this and it works fine if you ..." (https://github.com/triton-lang/triton/pull/10189#issuecomment-4360121554)
- `2026-05-01T16:02:11Z` `issue` by `Jokeren`; signals: triton; excerpt: "If you make a call it's going to return a tensor? We have some code that does this and it works fine if you ..." (https://github.com/triton-lang/triton/pull/10189#issuecomment-4360220836)
- `2026-05-01T21:22:43Z` `issue` by `leijurv`; signals: layout; excerpt: "Python-level test added. Lit test improved and gave an example that layouts are converted at the return as was brought up in the previous ..." (https://github.com/triton-lang/triton/pull/10189#issuecomment-4361709211)
- `2026-05-04T16:00:17Z` `inline` by `ThomasRaoux` `python/test/unit/language/test_core.py`:1333; signals: general review; excerpt: "can we use noinline=True instead. I would expect those to be fully inlined so I don't get what this tests" (https://github.com/triton-lang/triton/pull/10189#discussion_r3182811957)
- `2026-05-04T17:21:27Z` `inline` by `leijurv` `python/test/unit/language/test_core.py`:1333; signals: general review; excerpt: "Sure. Reverted back to that. We thought that using noinline=True might be unsupported so Saagar's approach was to force a function to not inline ..." (https://github.com/triton-lang/triton/pull/10189#discussion_r3183246266)
- `2026-05-04T17:24:32Z` `inline` by `ThomasRaoux` `python/test/unit/language/test_core.py`:1333; signals: general review; excerpt: "I think supporting noinline should be the goal here" (https://github.com/triton-lang/triton/pull/10189#discussion_r3183262563)
- `2026-05-01T15:58:59Z` `issue` by `ThomasRaoux`; signals: general review; excerpt: "BTW I thought we had ran into that when calling a function returning a tensor with early return within a loop. I can't find ..." (https://github.com/triton-lang/triton/pull/10189#issuecomment-4360205451)
