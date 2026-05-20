# PR Discussion Digest

- Source PR: [vllm-project/vllm#29339](https://github.com/vllm-project/vllm/pull/29339)
- Source page: `sources/prs/vllm/PR-29339.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29339`
- Generated at: `2026-05-20T15:38:42.713978+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-24T20:14:56Z`
- Merged: `2025-11-24T23:22:46Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: mgoin, varun-sundar-rabindranath, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-24T20:16:02Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly restricts the use of Triton kernels for MXFP4 to SM90 and SM100 ... (https://github.com/vllm-project/vllm/pull/29339#pullrequestreview-3502092835)
- `2025-11-24T20:39:27Z` `APPROVED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/29339#pullrequestreview-3502163402)
- `2025-11-24T20:42:16Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/29339#pullrequestreview-3502170388)
- `2025-11-24T21:46:47Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29339#pullrequestreview-3502347919)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/mxfp4.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-11-24T21:46:47Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/mxfp4.py`:137; signals: cuda, fp4, mxfp4; excerpt: "CUDA does, but other hardware does not. Even though this is in a CUDA branch, I think some people still build with their own ..." (https://github.com/vllm-project/vllm/pull/29339#discussion_r2557814093)
- `2025-11-24T20:42:12Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/mxfp4.py`:137; signals: fp4, mxfp4; excerpt: "I think vllm requires torch 2.9.0 now, could we remove this?" (https://github.com/vllm-project/vllm/pull/29339#discussion_r2557670062)
