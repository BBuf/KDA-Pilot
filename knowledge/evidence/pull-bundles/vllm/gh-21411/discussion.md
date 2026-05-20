# PR Discussion Digest

- Source PR: [vllm-project/vllm#21411](https://github.com/vllm-project/vllm/pull/21411)
- Source page: `sources/prs/vllm/PR-21411.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21411`
- Generated at: `2026-05-20T15:36:39.915598+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-22T21:47:43Z`
- Merged: `2025-07-26T14:10:36Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: kaixih, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-22T21:48:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to restore previous behavior for FlashInfer MoE kernels by explicitly disabling a ... (https://github.com/vllm-project/vllm/pull/21411#pullrequestreview-3044976152)
- `2025-07-25T22:46:40Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21411#pullrequestreview-3056954840)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-24T17:57:44Z` `issue` by `kaixih`; signals: flashinfer; excerpt: "@mgoin the flashinfer has released the [0.2.9rc1]( I took a quick look at the vLLM codebase and noticed that only the Dockerfile explicitly references ..." (https://github.com/vllm-project/vllm/pull/21411#issuecomment-3114354490)
- `2025-07-24T18:11:26Z` `issue` by `mgoin`; signals: cuda; excerpt: "@kaixih Let's wait on landing this PR until after then, as it already updates the dockerfile. We will enforce the version in the future ..." (https://github.com/vllm-project/vllm/pull/21411#issuecomment-3114391094)
- `2025-07-25T22:05:10Z` `issue` by `kaixih`; signals: flashinfer; excerpt: "@mgoin can we merge this PR since the flashinfer 0.2.9rc1 is in." (https://github.com/vllm-project/vllm/pull/21411#issuecomment-3120514610)
