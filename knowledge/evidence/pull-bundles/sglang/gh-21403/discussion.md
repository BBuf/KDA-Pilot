# PR Discussion Digest

- Source PR: [sgl-project/sglang#21403](https://github.com/sgl-project/sglang/pull/21403)
- Source page: `sources/prs/sglang/PR-21403.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21403`
- Generated at: `2026-05-20T15:29:13.657108+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T10:57:28Z`
- Merged: `2026-04-11T05:45:32Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 7 (approved=1, changes_requested=2, commented=4)
- Inline review comments: 12
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=7
- Human participants with discussion text: HaiShaw, Jacob0226
- Automation comments/reviews omitted from high-signal summary: 13
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-25T11:03:44Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces FP8 per-token quantization support using the aiter library for RMSNorm and linear ... (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4005802803)
- `2026-03-27T04:12:57Z` `COMMENTED` by `Jacob0226` (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4018754110)
- `2026-03-31T09:10:04Z` `CHANGES_REQUESTED` by `HaiShaw` - @Jacob0226 lint fix pls (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4035868871)
- `2026-04-04T08:25:56Z` `CHANGES_REQUESTED` by `HaiShaw` - Please double check the applicable kernels scope on gfx95 and use aiter vs. use aiter only (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4058304208)
- `2026-04-07T04:11:58Z` `COMMENTED` by `Jacob0226` (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4065679679)
- `2026-04-07T04:12:01Z` `COMMENTED` by `Jacob0226` (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4065679816)
- `2026-04-10T08:51:37Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4088465278)

## Inline Comment Hotspots

- `python/sglang/srt/layers/communicator.py`: 6 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8_utils.py`: 4 inline comment(s)
- `python/sglang/srt/models/glm4_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-04T08:25:56Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: kernel; excerpt: "Please double check the applicable kernels scope on gfx95 and use aiter vs. use aiter only" (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4058304208)
- `2026-04-10T08:34:34Z` `issue` by `Jacob0226`; signals: bf16, fp8; excerpt: "@Jacob0226 May you fix conflict? Done. Merged upstream/main and resolved the conflict in communicator.py. The conflict was between this PR's quant format == "fp8" ..." (https://github.com/sgl-project/sglang/pull/21403#issuecomment-4222256682)
- `2026-04-07T04:12:01Z` `inline` by `Jacob0226` `python/sglang/srt/layers/quantization/fp8_utils.py`:1628; signals: fp8; excerpt: "The caller in compressed tensors w8a8 fp8.py already guards with if use aiter before calling apply fp8 ptpc linear, so the tuple input path ..." (https://github.com/sgl-project/sglang/pull/21403#discussion_r3042814943)
- `2026-03-27T04:12:57Z` `inline` by `Jacob0226` `python/sglang/srt/layers/quantization/fp8_utils.py`:1277; signals: fp8; excerpt: "Fixed" (https://github.com/sgl-project/sglang/pull/21403#discussion_r2998872551)
- `2026-04-04T07:48:19Z` `inline` by `HaiShaw` `python/sglang/srt/layers/quantization/fp8_utils.py`:1628; signals: fp8; excerpt: "assumed only aiter path will call apply fp8 ptpc linear, which is error prone." (https://github.com/sgl-project/sglang/pull/21403#discussion_r3035305300)
- `2026-03-31T09:10:04Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: general review; excerpt: "@Jacob0226 lint fix pls" (https://github.com/sgl-project/sglang/pull/21403#pullrequestreview-4035868871)
- `2026-04-04T08:17:05Z` `inline` by `HaiShaw` `python/sglang/srt/layers/communicator.py`:99; signals: general review; excerpt: "please comment this method is only with aiter path" (https://github.com/sgl-project/sglang/pull/21403#discussion_r3035328804)
- `2026-04-07T04:11:58Z` `inline` by `Jacob0226` `python/sglang/srt/layers/communicator.py`:99; signals: general review; excerpt: "Added aiter-only docstring in 0f6c01d." (https://github.com/sgl-project/sglang/pull/21403#discussion_r3042814813)
