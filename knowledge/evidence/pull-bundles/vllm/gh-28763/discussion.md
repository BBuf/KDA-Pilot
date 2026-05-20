# PR Discussion Digest

- Source PR: [vllm-project/vllm#28763](https://github.com/vllm-project/vllm/pull/28763)
- Source page: `sources/prs/vllm/PR-28763.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28763`
- Generated at: `2026-05-20T15:38:33.733605+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-15T00:35:07Z`
- Merged: `2025-11-19T04:06:22Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: LucasWilkinson, MatthewBonanni, MoyanZitto, chatgpt-codex-connector, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-11-15T00:38:00Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28763#pullrequestreview-3467307778)
- `2025-11-15T00:41:31Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/28763#pullrequestreview-3467312559)
- `2025-11-15T00:45:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates FlashAttention to support head sizes required for Vision Transformers (40, 72, 80). ... (https://github.com/vllm-project/vllm/pull/28763#pullrequestreview-3467324526)
- `2025-11-17T15:15:30Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/28763#pullrequestreview-3473237960)
- `2025-11-17T15:15:48Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/28763#pullrequestreview-3473240126)
- `2025-11-19T04:05:53Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28763#pullrequestreview-3480720745)

## Inline Comment Hotspots

- `vllm/platforms/cuda.py`: 2 inline comment(s)
- `cmake/external_projects/vllm_flash_attn.cmake`: 2 inline comment(s)
- `tests/kernels/attention/test_flash_attn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-15T00:38:00Z` `inline` by `chatgpt-codex-connector` `vllm/platforms/cuda.py`:276; signals: attention, compile, cuda; excerpt: "before checking compute capability or whether FlashAttention is even available. On systems where the extension is not built (e.g., CUDA < 8.0 GPUs or ..." (https://github.com/vllm-project/vllm/pull/28763#discussion_r2529328217)
- `2025-11-17T15:15:30Z` `inline` by `MatthewBonanni` `tests/kernels/attention/test_flash_attn.py`:23; signals: attention, kernel; excerpt: "The vLLM FA build has soft cap disabled" (https://github.com/vllm-project/vllm/pull/28763#discussion_r2534486998)
- `2025-11-19T01:34:45Z` `issue` by `MatthewBonanni`; signals: attention, kernel; excerpt: "@LucasWilkinson pytest tests/kernels/attention/test flash attn.py passes on A100 with FA2 👍" (https://github.com/vllm-project/vllm/pull/28763#issuecomment-3550173436)
- `2025-11-15T00:38:00Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28763#pullrequestreview-3467307778)
- `2025-11-15T00:41:31Z` `inline` by `MatthewBonanni` `vllm/platforms/cuda.py`:276; signals: cuda; excerpt: "done" (https://github.com/vllm-project/vllm/pull/28763#discussion_r2529331017)
- `2025-11-17T15:15:48Z` `inline` by `MatthewBonanni` `cmake/external_projects/vllm_flash_attn.cmake`:41; signals: hang; excerpt: "This will be changed before merge" (https://github.com/vllm-project/vllm/pull/28763#discussion_r2534488725)
