# PR Discussion Digest

- Source PR: [triton-lang/triton#10234](https://github.com/triton-lang/triton/pull/10234)
- Source page: `sources/prs/triton/PR-10234.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10234`
- Generated at: `2026-05-20T15:33:29.628338+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-05T19:44:37Z`
- Merged: `2026-05-13T17:36:08Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 27 (approved=1, commented=26)
- Inline review comments: 28
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=1, outdated=6
- Human participants with discussion text: Jokeren, ThomasRaoux, mwichro
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-05T20:10:54Z` `COMMENTED` by `Jokeren` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4231297561)
- `2026-05-05T20:28:36Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4231397297)
- `2026-05-05T21:23:09Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4231693702)
- `2026-05-05T21:24:39Z` `COMMENTED` by `Jokeren` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4231701194)
- `2026-05-05T21:47:17Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4231824920)
- `2026-05-05T22:16:30Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4231946542)
- `2026-05-05T23:34:15Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4232222708)
- `2026-05-05T23:34:30Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4232223456)
- `2026-05-06T00:46:06Z` `COMMENTED` by `Jokeren` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4232469958)
- `2026-05-06T00:47:21Z` `COMMENTED` by `Jokeren` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4232473895)
- `2026-05-06T02:52:35Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4232847502)
- `2026-05-06T02:53:22Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4232852965)
- `2026-05-06T03:07:32Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4232904569)
- `2026-05-06T13:52:58Z` `COMMENTED` by `Jokeren` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4236647248)
- `2026-05-06T17:25:28Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4238188413)
- `2026-05-06T19:44:42Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4238987634)
- `2026-05-06T20:55:20Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239502963)
- `2026-05-06T20:55:54Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239506056)
- `2026-05-06T20:56:15Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239508234)
- `2026-05-06T21:00:54Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239534831)
- `2026-05-06T21:02:26Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239544295)
- `2026-05-06T21:42:18Z` `COMMENTED` by `mwichro` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239779614)
- `2026-05-06T21:46:51Z` `COMMENTED` by `Jokeren` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239813747)
- `2026-05-06T21:48:12Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10234#pullrequestreview-4239819266)
- ... 3 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `python/test/unit/language/test_core.py`: 18 inline comment(s)
- `third_party/nvidia/backend/compiler.py`: 8 inline comment(s)
- `lib/Analysis/Utility.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-05T20:10:50Z` `inline` by `Jokeren` `third_party/nvidia/backend/compiler.py`:30; signals: compile, sm90; excerpt: "This is more general than sm90+. Likely you need more code updates to support a smaller dot shape across archs. I'll defer it to ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3191273960)
- `2026-05-05T22:16:30Z` `inline` by `mwichro` `third_party/nvidia/backend/compiler.py`:30; signals: compile, fp8; excerpt: "Ah, btw, on review, Claude is suggesting: So min dot size is reinventing the same formula with a hardcoded if/elif chain, ignoring the target ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3191894976)
- `2026-05-06T21:42:18Z` `inline` by `mwichro` `python/test/unit/language/test_core.py`:3600; signals: triton, vector; excerpt: "Line 3520 in python/test/unit/language/test core.py: With runtime strides, Triton can only prove contiguity along the inner dim when it is at least 16 elements ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3197679369)
- `2026-05-05T20:28:36Z` `inline` by `ThomasRaoux` `third_party/nvidia/backend/compiler.py`:30; signals: blackwell, compile; excerpt: "Yes I think it would be good to update Blackwell as well the same way." (https://github.com/triton-lang/triton/pull/10234#discussion_r3191370560)
- `2026-05-05T21:23:09Z` `inline` by `mwichro` `third_party/nvidia/backend/compiler.py`:30; signals: blackwell, compile; excerpt: "I don't have access to Blackwell GPUs to test it directly, but I've updated MMAv5" (https://github.com/triton-lang/triton/pull/10234#discussion_r3191657175)
- `2026-05-11T21:54:54Z` `issue` by `mwichro`; signals: cuda, hang; excerpt: "Thanks for your patience and approval! The tests failure do not look related to the changes RuntimeError: Cannot re-initialize CUDA in forked subprocess. To ..." (https://github.com/triton-lang/triton/pull/10234#issuecomment-4425489217)
- `2026-05-05T21:47:17Z` `inline` by `mwichro` `third_party/nvidia/backend/compiler.py`:30; signals: compile; excerpt: "A100 is sm80, so MMAv3 is not available, so it should have no effect anyway. I have A100, this one I can test: Looks ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3191777634)
- `2026-05-06T00:45:59Z` `inline` by `Jokeren` `python/test/unit/language/test_core.py`:3594; signals: tile; excerpt: "I still think there's something missing. What if you run this test on ampere by removing this constraint? My point is, the current code ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3192366760)
- `2026-05-06T00:47:21Z` `inline` by `Jokeren` `third_party/nvidia/backend/compiler.py`:30; signals: compile; excerpt: "python -m pytest python/test/unit/language/test core.py -k "dot" -q --no-header 736 passed, 1882 skipped, 6728 deselected in 286.06s (0:04:46) We don't have very small dot ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3192370390)
- `2026-05-06T19:44:42Z` `inline` by `mwichro` `python/test/unit/language/test_core.py`:3584; signals: wgmma; excerpt: "I just tried that: it turns out K has to be constexpr for this to properly emit wgmma instruction. So the less invasive way ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3197025133)
- `2026-05-06T21:00:54Z` `inline` by `mwichro` `python/test/unit/language/test_core.py`:3600; signals: wgmma; excerpt: "K must be constexpr, otherwise trition is not able to emit wgmma for K=8 (I tried). I think assuming that K is constexpr is ..." (https://github.com/triton-lang/triton/pull/10234#discussion_r3197468350)
- `2026-05-05T21:24:39Z` `inline` by `Jokeren` `third_party/nvidia/backend/compiler.py`:30; signals: compile; excerpt: "What about sm80 with TF32, are you able to use (1,1,8) to pass all tests?" (https://github.com/triton-lang/triton/pull/10234#discussion_r3191664343)
