# PR Discussion Digest

- Source PR: [sgl-project/sglang#13607](https://github.com/sgl-project/sglang/pull/13607)
- Source page: `sources/prs/sglang/PR-13607.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13607`
- Generated at: `2026-05-20T15:27:49.566244+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-19T22:04:57Z`
- Merged: `2025-12-05T17:54:49Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 9
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=1
- Human participants with discussion text: CatherineSue, b8zhong, copilot-pull-request-reviewer, hnyls2002, slin1237
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-19T22:09:30Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull Request Overview This PR removes usage of deprecated API endpoint calls and updates them to use the ... (https://github.com/sgl-project/sglang/pull/13607#pullrequestreview-3484931547)
- `2025-11-19T22:10:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request effectively removes calls to deprecated endpoints like /get server info, /get model info, ... (https://github.com/sgl-project/sglang/pull/13607#pullrequestreview-3484933117)
- `2025-11-19T22:13:54Z` `APPROVED` by `slin1237` (https://github.com/sgl-project/sglang/pull/13607#pullrequestreview-3484942916)
- `2025-11-19T22:19:24Z` `COMMENTED` by `slin1237` (https://github.com/sgl-project/sglang/pull/13607#pullrequestreview-3484959806)
- `2025-11-19T22:54:43Z` `APPROVED` by `CatherineSue` (https://github.com/sgl-project/sglang/pull/13607#pullrequestreview-3485045418)

## Inline Comment Hotspots

- `python/sglang/lang/backend/runtime_endpoint.py`: 3 inline comment(s)
- `test/srt/rl/test_update_weights_from_disk.py`: 3 inline comment(s)
- `test/srt/test_srt_endpoint.py`: 2 inline comment(s)
- `test/srt/test_data_parallelism.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-19T22:09:30Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: attention, benchmark, cache, flashinfer, fp4, hang, mla; excerpt: "Pull Request Overview This PR removes usage of deprecated API endpoint calls and updates them to use the new endpoint names. The changes migrate ..." (https://github.com/sgl-project/sglang/pull/13607#pullrequestreview-3484931547)
- `2025-11-19T22:19:24Z` `inline` by `slin1237` `python/sglang/lang/backend/runtime_endpoint.py`:69; signals: hang; excerpt: "changing func name has other implication and downside for no good reason resolving all of those comments" (https://github.com/sgl-project/sglang/pull/13607#discussion_r2543742900)
- `2025-11-22T17:35:42Z` `issue` by `hnyls2002`; signals: general review; excerpt: "@b8zhong Please fix the conflicts. Also, as Merge-Oncalls, @CatherineSue @slin1237 you can drive the merging process of this PR." (https://github.com/sgl-project/sglang/pull/13607#issuecomment-3566913901)
