# PR Discussion Digest

- Source PR: [vllm-project/vllm#39820](https://github.com/vllm-project/vllm/pull/39820)
- Source page: `sources/prs/vllm/PR-39820.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-39820`
- Generated at: `2026-05-20T15:40:46.658629+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-14T18:56:02Z`
- Merged: `2026-04-14T21:08:17Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T18:58:57Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a batch-invariant mode for NVFP4 linear kernels to ensure deterministic execution when ... (https://github.com/vllm-project/vllm/pull/39820#pullrequestreview-4108419567)
- `2026-04-14T19:00:01Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/39820#pullrequestreview-4108424846)
- `2026-04-14T21:08:12Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/39820#pullrequestreview-4109230254)

## Inline Comment Hotspots

- `vllm/model_executor/kernels/linear/__init__.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-14T19:00:01Z` `inline` by `yewentao256` `vllm/model_executor/kernels/linear/__init__.py`:608; signals: kernel; excerpt: "It will info once by default" (https://github.com/vllm-project/vllm/pull/39820#discussion_r3081753056)
