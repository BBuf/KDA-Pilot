# PR Discussion Digest

- Source PR: [vllm-project/vllm#25478](https://github.com/vllm-project/vllm/pull/25478)
- Source page: `sources/prs/vllm/PR-25478.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25478`
- Generated at: `2026-05-20T15:37:56.208707+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-23T14:07:30Z`
- Merged: `2025-09-24T01:09:43Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=2, dismissed=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: robertgshaw2-redhat, simon-mo, smarterclayton, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-23T14:09:37Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses an assertion failure in the Multi-Level Attention (MLA) implementation by replacing a ... (https://github.com/vllm-project/vllm/pull/25478#pullrequestreview-3258220081)
- `2025-09-23T15:18:37Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/25478#pullrequestreview-3258528935)
- `2025-09-23T15:27:50Z` `DISMISSED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/25478#pullrequestreview-3258578118)
- `2025-09-24T01:09:38Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/25478#pullrequestreview-3260259757)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/common.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-23T15:18:30Z` `inline` by `yewentao256` `vllm/v1/attention/backends/mla/common.py`:488; signals: attention, block, cutlass, mla, oom; excerpt: "In cutlass MLA case block size = 128, if max num seqs == 1024 it is back to 128 1024 again, so seems that ..." (https://github.com/vllm-project/vllm/pull/25478#discussion_r2372683119)
- `2025-09-23T15:20:06Z` `issue` by `smarterclayton`; signals: b200; excerpt: "This allowed me to start a vllm using deepseek v3.1 again (DP=16, B200)" (https://github.com/vllm-project/vllm/pull/25478#issuecomment-3324482117)
