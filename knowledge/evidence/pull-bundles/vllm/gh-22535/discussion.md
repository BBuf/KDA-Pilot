# PR Discussion Digest

- Source PR: [vllm-project/vllm#22535](https://github.com/vllm-project/vllm/pull/22535)
- Source page: `sources/prs/vllm/PR-22535.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22535`
- Generated at: `2026-05-20T15:37:06.508503+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-08T18:09:27Z`
- Merged: `2025-08-12T19:54:42Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: mgoin, zyongye
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-08T18:11:41Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes an issue where the torch version check for mxfp4 was overly broad, ... (https://github.com/vllm-project/vllm/pull/22535#pullrequestreview-3101788347)
- `2025-08-10T18:28:30Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/22535#pullrequestreview-3103710743)
- `2025-08-10T18:32:14Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/22535#pullrequestreview-3103711711)
- `2025-08-12T01:15:20Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/22535#pullrequestreview-3108224059)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-08-10T18:28:30Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:727; signals: kernel, moe, sm120, triton; excerpt: "Aren't the triton kernels also used for sm80 or sm120? I think this should be not current platform.is device capability(100) then" (https://github.com/vllm-project/vllm/pull/22535#discussion_r2265391470)
- `2025-08-10T18:32:14Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/layer.py`:727; signals: hang, moe; excerpt: "It will be used for sm80. I think we can change this in another PR when we change these two lines together" (https://github.com/vllm-project/vllm/pull/22535#discussion_r2265392728)
