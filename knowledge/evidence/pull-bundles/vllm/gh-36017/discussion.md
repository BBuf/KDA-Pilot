# PR Discussion Digest

- Source PR: [vllm-project/vllm#36017](https://github.com/vllm-project/vllm/pull/36017)
- Source page: `sources/prs/vllm/PR-36017.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36017`
- Generated at: `2026-05-20T15:40:05.332302+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-04T15:41:28Z`
- Merged: `2026-03-04T22:23:52Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: amitz-nv, benchislett
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T15:45:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug by fixing the passing of activation type to FlashInfer's fused ... (https://github.com/vllm-project/vllm/pull/36017#pullrequestreview-3890261483)
- `2026-03-04T15:47:43Z` `COMMENTED` by `amitz-nv` (https://github.com/vllm-project/vllm/pull/36017#pullrequestreview-3890276560)
- `2026-03-04T16:01:54Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/36017#pullrequestreview-3890375940)
- `2026-03-04T16:05:47Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/36017#pullrequestreview-3890401119)
- `2026-03-04T16:05:51Z` `APPROVED` by `benchislett` - LGTM (https://github.com/vllm-project/vllm/pull/36017#pullrequestreview-3890401471)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-04T15:47:43Z` `inline` by `amitz-nv` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:326; signals: fp4, moe, nvfp4; excerpt: "That's just not true, that import exists there at lines 18-20." (https://github.com/vllm-project/vllm/pull/36017#discussion_r2884557451)
- `2026-03-04T16:01:54Z` `inline` by `benchislett` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:326; signals: fp4, moe, nvfp4; excerpt: "lol" (https://github.com/vllm-project/vllm/pull/36017#discussion_r2884643155)
- `2026-03-04T16:05:47Z` `inline` by `benchislett` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:247; signals: fp8, moe; excerpt: "Seems correct, based on" (https://github.com/vllm-project/vllm/pull/36017#discussion_r2884665290)
