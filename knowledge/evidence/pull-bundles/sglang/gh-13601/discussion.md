# PR Discussion Digest

- Source PR: [sgl-project/sglang#13601](https://github.com/sgl-project/sglang/pull/13601)
- Source page: `sources/prs/sglang/PR-13601.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13601`
- Generated at: `2026-05-20T15:27:49.562894+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-19T19:42:50Z`
- Merged: `2025-11-24T00:07:56Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 6 (commented=6)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: Fridge003, fzyzcjy, kaixih
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-20T07:29:55Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/13601#pullrequestreview-3486015598)
- `2025-11-22T21:13:28Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13601#pullrequestreview-3496947889)
- `2025-11-23T09:52:00Z` `COMMENTED` by `fzyzcjy` - only some nits and LGTM as long as test pass (https://github.com/sgl-project/sglang/pull/13601#pullrequestreview-3497574975)
- `2025-11-23T20:12:12Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13601#pullrequestreview-3497972339)
- `2025-11-23T21:07:04Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13601#pullrequestreview-3498000697)
- `2025-11-23T21:07:12Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13601#pullrequestreview-3498000755)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8.py`: 4 inline comment(s)
- `python/sglang/srt/model_loader/utils.py`: 2 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-20T07:05:00Z` `inline` by `kaixih` `python/sglang/srt/layers/quantization/fp8.py`:371; signals: deepgemm, fp8, gemm; excerpt: "can we make the should deepgemm weight requant ue8m0 more reliable like: then we can confidently use this in the corresponding process weights after ..." (https://github.com/sgl-project/sglang/pull/13601#discussion_r2544601095)
- `2025-11-23T09:46:34Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/quantization/fp8.py`:361; signals: cute, fp8; excerpt: "nit: I personally prefer setting layer. executed weight requant ue8m0=False at initialization stage, s.t. we do not need getattr. b/c if we use getattr ..." (https://github.com/sgl-project/sglang/pull/13601#discussion_r2553936684)
- `2025-11-22T21:13:24Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8.py`:371; signals: fp8, hang; excerpt: "Good suggestion, just changed in this way" (https://github.com/sgl-project/sglang/pull/13601#discussion_r2553356601)
- `2025-11-23T21:07:04Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8.py`:361; signals: fp8, hang; excerpt: "Changed to another way avoiding getattr" (https://github.com/sgl-project/sglang/pull/13601#discussion_r2554324113)
- `2025-11-23T09:52:00Z` `review` `COMMENTED` by `fzyzcjy`; signals: general review; excerpt: "only some nits and LGTM as long as test pass" (https://github.com/sgl-project/sglang/pull/13601#pullrequestreview-3497574975)
- `2025-11-23T09:47:06Z` `inline` by `fzyzcjy` `python/sglang/srt/model_loader/utils.py`:133; signals: general review; excerpt: "miles/slime will call this function w/ layer=None, thus not only backward compatibility is it possible we somehow do not require pass in a layer ..." (https://github.com/sgl-project/sglang/pull/13601#discussion_r2553937055)
- `2025-11-23T09:49:26Z` `inline` by `fzyzcjy` `python/sglang/srt/models/deepseek_v2.py`:3724; signals: general review; excerpt: "nit: will we completely remove this logic later (since it seems you already remove some in this pr)" (https://github.com/sgl-project/sglang/pull/13601#discussion_r2553938757)
- `2025-11-23T20:12:12Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:3724; signals: general review; excerpt: "Yes I will remove it in the next PR" (https://github.com/sgl-project/sglang/pull/13601#discussion_r2554296075)
- `2025-11-23T21:07:12Z` `inline` by `Fridge003` `python/sglang/srt/model_loader/utils.py`:133; signals: general review; excerpt: "Sure, just removed layer from arguments" (https://github.com/sgl-project/sglang/pull/13601#discussion_r2554324188)
