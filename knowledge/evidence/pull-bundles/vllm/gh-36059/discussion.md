# PR Discussion Digest

- Source PR: [vllm-project/vllm#36059](https://github.com/vllm-project/vllm/pull/36059)
- Source page: `sources/prs/vllm/PR-36059.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36059`
- Generated at: `2026-05-20T15:40:05.338736+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-04T23:08:17Z`
- Merged: `2026-03-05T19:05:56Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: frankwang28, mergify, yewentao256
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T23:13:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a necessary fallback from FlashAttention v4 to v2 when batch invariance is ... (https://github.com/vllm-project/vllm/pull/36059#pullrequestreview-3892580896)
- `2026-03-05T15:53:11Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! Could you add more context why FA4 doesn't supprot it in PR description/comments? (https://github.com/vllm-project/vllm/pull/36059#pullrequestreview-3897698092)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-03-05T18:31:09Z` `issue` by `frankwang28`; signals: block, cute, tile; excerpt: "Could you add more context why FA4 doesn't supprot it in PR description/comments? The first place I found some invariance was the selection of ..." (https://github.com/vllm-project/vllm/pull/36059#issuecomment-4006900398)
- `2026-03-04T23:20:42Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @frankwang28, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36059#issuecomment-4000922699)
- `2026-03-05T15:53:11Z` `review` `APPROVED` by `yewentao256`; signals: general review; excerpt: "LGTM, thanks for the work! Could you add more context why FA4 doesn't supprot it in PR description/comments?" (https://github.com/vllm-project/vllm/pull/36059#pullrequestreview-3897698092)
