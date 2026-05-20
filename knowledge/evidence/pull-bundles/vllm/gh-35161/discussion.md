# PR Discussion Digest

- Source PR: [vllm-project/vllm#35161](https://github.com/vllm-project/vllm/pull/35161)
- Source page: `sources/prs/vllm/PR-35161.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35161`
- Generated at: `2026-05-20T15:39:59.963378+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-24T01:32:21Z`
- Merged: `2026-02-25T01:14:24Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: mgoin, xyang16, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-24T01:34:07Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly fixes a bug in the moe align block size kernel where expert ... (https://github.com/vllm-project/vllm/pull/35161#pullrequestreview-3844476111)
- `2026-02-24T15:33:33Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! Just curious why it doesn't affect accuracy in main? (https://github.com/vllm-project/vllm/pull/35161#pullrequestreview-3848722269)
- `2026-02-25T01:13:59Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/35161#pullrequestreview-3851313635)

## Inline Comment Hotspots

- `tests/kernels/moe/test_moe_align_block_size.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-24T17:46:22Z` `issue` by `xyang16`; signals: accuracy, block, hang; excerpt: "LGTM, thanks for the work! Just curious why it doesn't affect accuracy in main? @yewentao256 Thanks for view! I think it's because there's another ..." (https://github.com/vllm-project/vllm/pull/35161#issuecomment-3953728772)
- `2026-02-24T15:33:33Z` `review` `APPROVED` by `yewentao256`; signals: accuracy; excerpt: "LGTM, thanks for the work! Just curious why it doesn't affect accuracy in main?" (https://github.com/vllm-project/vllm/pull/35161#pullrequestreview-3848722269)
