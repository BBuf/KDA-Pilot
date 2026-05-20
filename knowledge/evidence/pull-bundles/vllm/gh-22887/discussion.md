# PR Discussion Digest

- Source PR: [vllm-project/vllm#22887](https://github.com/vllm-project/vllm/pull/22887)
- Source page: `sources/prs/vllm/PR-22887.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22887`
- Generated at: `2026-05-20T15:37:14.266635+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-14T08:38:24Z`
- Merged: `2025-08-29T01:23:04Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: chaojun-zhang, jikunshang, mergify
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-14T08:39:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for offline local data parallelism on XPU devices. The changes primarily ... (https://github.com/vllm-project/vllm/pull/22887#pullrequestreview-3119597702)
- `2025-08-28T00:18:07Z` `APPROVED` by `jikunshang` - LGTM. thanks for fixing this! (https://github.com/vllm-project/vllm/pull/22887#pullrequestreview-3162389260)
- `2025-08-29T01:22:40Z` `APPROVED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/22887#pullrequestreview-3167036830)

## Inline Comment Hotspots

- `vllm/platforms/xpu.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-28T00:19:01Z` `issue` by `jikunshang`; signals: hang, moe; excerpt: "maybe we should changed title to support data parallel for MoE models on XPU" (https://github.com/vllm-project/vllm/pull/22887#issuecomment-3230330040)
- `2025-08-28T01:16:14Z` `issue` by `chaojun-zhang`; signals: hang, moe; excerpt: "maybe we should changed title to support data parallel for MoE models on XPU" (https://github.com/vllm-project/vllm/pull/22887#issuecomment-3230797337)
- `2025-08-18T05:21:35Z` `issue` by `mergify`; signals: hang; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @chaojun-zhang." (https://github.com/vllm-project/vllm/pull/22887#issuecomment-3195134630)
