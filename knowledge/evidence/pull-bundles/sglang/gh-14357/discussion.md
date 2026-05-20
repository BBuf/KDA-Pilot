# PR Discussion Digest

- Source PR: [sgl-project/sglang#14357](https://github.com/sgl-project/sglang/pull/14357)
- Source page: `sources/prs/sglang/PR-14357.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14357`
- Generated at: `2026-05-20T15:27:58.829820+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-03T12:01:59Z`
- Merged: `2025-12-17T07:01:39Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Fridge003, Qiaolin-Yu, b8zhong, elvischenv
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-03T12:04:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables Flashinfer autotuning by default, which is a good change for improving performance ... (https://github.com/sgl-project/sglang/pull/14357#pullrequestreview-3534733064)
- `2025-12-10T03:46:45Z` `APPROVED` by `b8zhong` - Waiting for B200 CI to pass (https://github.com/sgl-project/sglang/pull/14357#pullrequestreview-3560575208)
- `2025-12-10T19:27:44Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14357#pullrequestreview-3564165058)
- `2025-12-10T19:34:45Z` `APPROVED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/14357#pullrequestreview-3564188966)
- `2025-12-11T01:46:28Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/14357#pullrequestreview-3565276834)

## Inline Comment Hotspots

- `python/sglang/srt/server_args.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-12-12T08:04:36Z` `issue` by `elvischenv`; signals: attention, autotune, flashinfer, hang, kernel, moe, perf; excerpt: "@b8zhong I have made the following changes to improve the autotune benefits: - For all flashinfer MoE APIs, set tune max num tokens to ..." (https://github.com/sgl-project/sglang/pull/14357#issuecomment-3645376012)
- `2025-12-04T17:52:58Z` `issue` by `elvischenv`; signals: attention, autotune, cuda, flashinfer; excerpt: "From the log, the attention backend is using attention backend='fa3', so it won't do flashinfer autotune before cuda graph. The autotune will run with ..." (https://github.com/sgl-project/sglang/pull/14357#issuecomment-3613559761)
- `2025-12-10T03:46:45Z` `review` `APPROVED` by `b8zhong`; signals: b200; excerpt: "Waiting for B200 CI to pass" (https://github.com/sgl-project/sglang/pull/14357#pullrequestreview-3560575208)
- `2025-12-10T19:27:38Z` `inline` by `Fridge003` `python/sglang/srt/server_args.py`:3142; signals: general review; excerpt: "Please update this argument in the document" (https://github.com/sgl-project/sglang/pull/14357#discussion_r2607949996)
- `2025-12-11T01:46:28Z` `inline` by `elvischenv` `python/sglang/srt/server_args.py`:3142; signals: general review; excerpt: "Done. Thanks for pointing out." (https://github.com/sgl-project/sglang/pull/14357#discussion_r2608831732)
- `2025-12-04T17:44:21Z` `issue` by `b8zhong`; signals: general review; excerpt: "There is a failure of test/srt/test gpt oss 1gpu.py, I think it might be related. Can you check the result locally?" (https://github.com/sgl-project/sglang/pull/14357#issuecomment-3613514383)
- `2025-12-10T00:30:50Z` `issue` by `b8zhong`; signals: general review; excerpt: "@elvischenv Hi, do you mind merging in main? Thanks. Sorry for the delay... recently there are many CI failures" (https://github.com/sgl-project/sglang/pull/14357#issuecomment-3634853125)
