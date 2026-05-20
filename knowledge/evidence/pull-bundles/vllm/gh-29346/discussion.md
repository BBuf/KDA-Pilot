# PR Discussion Digest

- Source PR: [vllm-project/vllm#29346](https://github.com/vllm-project/vllm/pull/29346)
- Source page: `sources/prs/vllm/PR-29346.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29346`
- Generated at: `2026-05-20T15:38:42.714852+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-24T21:07:02Z`
- Merged: `2025-11-25T02:01:40Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: bnellnm, yewentao256
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-24T21:08:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a performance heuristic to disable the DeepGEMM backend for FP8 Mixture-of-Experts (MoE) ... (https://github.com/vllm-project/vllm/pull/29346#pullrequestreview-3502245484)
- `2025-11-24T21:17:45Z` `COMMENTED` by `yewentao256` - LGTM, thanks for the work! Data: Triton DeepGEMM MOE (https://github.com/vllm-project/vllm/pull/29346#pullrequestreview-3502274511)
- `2025-11-24T21:18:06Z` `APPROVED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/29346#pullrequestreview-3502275338)
- `2025-11-24T22:26:03Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29346#pullrequestreview-3502463177)
- `2025-11-24T22:51:23Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29346#pullrequestreview-3502537336)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-24T21:17:45Z` `review` `COMMENTED` by `yewentao256`; signals: deepgemm, gemm, moe, triton; excerpt: "LGTM, thanks for the work! Data: Triton DeepGEMM MOE" (https://github.com/vllm-project/vllm/pull/29346#pullrequestreview-3502274511)
- `2025-11-24T22:26:03Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/fp8.py`:169; signals: fp8; excerpt: "Should we check = 8 instead of == 8?" (https://github.com/vllm-project/vllm/pull/29346#discussion_r2557902365)
