# PR Discussion Digest

- Source PR: [vllm-project/vllm#20781](https://github.com/vllm-project/vllm/pull/20781)
- Source page: `sources/prs/vllm/PR-20781.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20781`
- Generated at: `2026-05-20T15:36:14.675068+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-10T19:26:28Z`
- Merged: `2025-07-11T02:39:18Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: luccafong, mgoin
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-07-10T19:26:50Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @djmmoss, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20781#pullrequestreview-3007040347)
- `2025-07-10T19:27:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly fixes a device-side assertion by disabling the cutlass block scaled grouped gemm ... (https://github.com/vllm-project/vllm/pull/20781#pullrequestreview-3007042728)
- `2025-07-10T19:53:43Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/20781#pullrequestreview-3007144716)
- `2025-07-10T21:36:52Z` `APPROVED` by `mgoin` - Thanks, LGTM! (https://github.com/vllm-project/vllm/pull/20781#pullrequestreview-3007476310)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-10T19:53:43Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1193; signals: moe; excerpt: "I think this function should check a few extra things actually: activation, apply router weight on input, expert map and probably inplace" (https://github.com/vllm-project/vllm/pull/20781#discussion_r2198595899)
