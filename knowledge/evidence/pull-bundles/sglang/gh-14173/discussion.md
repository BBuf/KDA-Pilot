# PR Discussion Digest

- Source PR: [sgl-project/sglang#14173](https://github.com/sgl-project/sglang/pull/14173)
- Source page: `sources/prs/sglang/PR-14173.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14173`
- Generated at: `2026-05-20T15:27:58.822752+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-01T01:41:24Z`
- Merged: `2025-12-01T09:54:23Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: yuan-luo
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-01T01:43:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly fixes a buffer overflow issue with FlashInfer for Qwen3-VL models by increasing ... (https://github.com/sgl-project/sglang/pull/14173#pullrequestreview-3522918215)
- `2025-12-01T09:50:39Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/14173#pullrequestreview-3524129874)
- `2025-12-01T09:51:10Z` `APPROVED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/14173#pullrequestreview-3524132124)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashinfer_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-01T09:50:39Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/flashinfer_backend.py`:166; signals: attention, flashinfer, moe; excerpt: "Maybe add Qwen3OmniMoeForConditionalGeneration as well." (https://github.com/sgl-project/sglang/pull/14173#discussion_r2576383784)
