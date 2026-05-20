# PR Discussion Digest

- Source PR: [vllm-project/vllm#23351](https://github.com/vllm-project/vllm/pull/23351)
- Source page: `sources/prs/vllm/PR-23351.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23351`
- Generated at: `2026-05-20T15:37:31.588234+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-21T15:55:57Z`
- Merged: `2025-08-22T04:01:08Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-21T15:56:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables DeepGEMM for FP8 linear layers on B200 GPUs by updating the device ... (https://github.com/vllm-project/vllm/pull/23351#pullrequestreview-3141329141)
- `2025-08-21T16:03:26Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/23351#pullrequestreview-3141352684)
- `2025-08-21T17:18:45Z` `COMMENTED` by `mgoin` - LGTM. Should we also take the opportunity to refactor the logic in fp8.py? It seems there is no ... (https://github.com/vllm-project/vllm/pull/23351#pullrequestreview-3141645604)
- `2025-08-21T19:40:24Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23351#pullrequestreview-3142042950)

## Inline Comment Hotspots

- `vllm/utils/deep_gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-21T17:18:45Z` `review` `COMMENTED` by `mgoin`; signals: deepgemm, fp8, gemm, moe; excerpt: "LGTM. Should we also take the opportunity to refactor the logic in fp8.py? It seems there is no logic about deepgemm in Fp8LinearMethod and ..." (https://github.com/vllm-project/vllm/pull/23351#pullrequestreview-3141645604)
- `2025-08-21T19:23:04Z` `issue` by `yewentao256`; signals: deepgemm, fp8, gemm, moe; excerpt: "LGTM. Should we also take the opportunity to refactor the logic in fp8.py? It seems there is no logic about deepgemm in Fp8LinearMethod and ..." (https://github.com/vllm-project/vllm/pull/23351#issuecomment-3211811103)
- `2025-08-21T16:03:26Z` `inline` by `yewentao256` `vllm/utils/deep_gemm.py`:208; signals: gemm; excerpt: "Nice bot, fixed" (https://github.com/vllm-project/vllm/pull/23351#discussion_r2291511144)
