# PR Discussion Digest

- Source PR: [vllm-project/vllm#21340](https://github.com/vllm-project/vllm/pull/21340)
- Source page: `sources/prs/vllm/PR-21340.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21340`
- Generated at: `2026-05-20T15:36:39.900751+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-22T00:28:38Z`
- Merged: `2025-07-24T07:38:39Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: simon-mo, yaochengji
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-22T00:29:48Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/21340#pullrequestreview-3040320575)
- `2025-07-22T00:30:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a bug in the MoE layer for TPU by allowing forward tpu ... (https://github.com/vllm-project/vllm/pull/21340#pullrequestreview-3040321490)
- `2025-07-23T20:21:39Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/21340#pullrequestreview-3048898503)
- `2025-07-24T00:29:08Z` `APPROVED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/21340#pullrequestreview-3049523059)
- `2025-07-24T00:39:35Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/21340#pullrequestreview-3049543418)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-07-22T00:29:48Z` `inline` by `yaochengji` `vllm/model_executor/layers/fused_moe/layer.py`:521; signals: moe; excerpt: "This ignores all other arguments, which is the same as forward cpu." (https://github.com/vllm-project/vllm/pull/21340#discussion_r2220660370)
- `2025-07-23T20:21:39Z` `inline` by `yaochengji` `vllm/model_executor/layers/fused_moe/layer.py`:521; signals: moe; excerpt: "It's fixed." (https://github.com/vllm-project/vllm/pull/21340#discussion_r2226575862)
- `2025-07-24T00:29:04Z` `inline` by `simon-mo` `vllm/model_executor/layers/fused_moe/layer.py`:493; signals: moe; excerpt: "This code path is CPU" (https://github.com/vllm-project/vllm/pull/21340#discussion_r2227017966)
- `2025-07-24T00:39:35Z` `inline` by `yaochengji` `vllm/model_executor/layers/fused_moe/layer.py`:493; signals: moe; excerpt: "Thanks @simon-mo for catching this!" (https://github.com/vllm-project/vllm/pull/21340#discussion_r2227033000)
