# PR Discussion Digest

- Source PR: [sgl-project/sglang#21921](https://github.com/sgl-project/sglang/pull/21921)
- Source page: `sources/prs/sglang/PR-21921.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21921`
- Generated at: `2026-05-20T15:29:18.508510+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T07:05:11Z`
- Merged: `2026-04-06T06:00:21Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 4 (commented=4)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: ShangmingCai, YAMY1234
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-02T07:06:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds documentation and tests for the Heterogeneous TP with GPU Staging Buffer feature, ... (https://github.com/sgl-project/sglang/pull/21921#pullrequestreview-4048772575)
- `2026-04-02T07:10:56Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/21921#pullrequestreview-4048790164)
- `2026-04-04T06:53:20Z` `COMMENTED` by `ShangmingCai` - Is it possible that we put these tests in the different tp test file, instead of creating another ... (https://github.com/sgl-project/sglang/pull/21921#pullrequestreview-4058222380)
- `2026-04-04T06:54:12Z` `COMMENTED` by `ShangmingCai` - Others LGTM. (https://github.com/sgl-project/sglang/pull/21921#pullrequestreview-4058222891)

## Inline Comment Hotspots

- `docs/advanced_features/pd_disaggregation.md`: 2 inline comment(s)
- `test/registered/distributed/test_disaggregation_different_tp_staging.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-05T16:04:00Z` `issue` by `ShangmingCai`; signals: b200, hopper; excerpt: "CI has passed. But the warning message might need improvement. It almost looks like a failure or a fallback, but I think it should ..." (https://github.com/sgl-project/sglang/pull/21921#issuecomment-4189113181)
- `2026-04-04T06:53:20Z` `review` `COMMENTED` by `ShangmingCai`; signals: general review; excerpt: "Is it possible that we put these tests in the different tp test file, instead of creating another file? I mean, they are testing ..." (https://github.com/sgl-project/sglang/pull/21921#pullrequestreview-4058222380)
- `2026-04-04T06:54:12Z` `review` `COMMENTED` by `ShangmingCai`; signals: general review; excerpt: "Others LGTM." (https://github.com/sgl-project/sglang/pull/21921#pullrequestreview-4058222891)
- `2026-04-02T07:10:56Z` `inline` by `YAMY1234` `docs/advanced_features/pd_disaggregation.md`:202; signals: general review; excerpt: "This is incorrect" (https://github.com/sgl-project/sglang/pull/21921#discussion_r3026313546)
- `2026-04-05T03:45:16Z` `issue` by `YAMY1234`; signals: general review; excerpt: "Is it possible that we put these tests in the different tp test file, instead of creating another file? I mean, they are testing ..." (https://github.com/sgl-project/sglang/pull/21921#issuecomment-4188206763)
