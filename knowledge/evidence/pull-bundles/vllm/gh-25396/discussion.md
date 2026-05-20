# PR Discussion Digest

- Source PR: [vllm-project/vllm#25396](https://github.com/vllm-project/vllm/pull/25396)
- Source page: `sources/prs/vllm/PR-25396.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25396`
- Generated at: `2026-05-20T15:37:56.207851+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-22T15:26:05Z`
- Merged: `2025-09-22T18:27:51Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: chatgpt-codex-connector, mgoin, simon-mo, zhuohan123
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-22T15:27:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix an issue where FlashAttention was incorrectly chosen for fp8 kv-cache ... (https://github.com/vllm-project/vllm/pull/25396#pullrequestreview-3253549582)
- `2025-09-22T15:32:09Z` `COMMENTED` by `chatgpt-codex-connector` - Codex Review: Here are some suggestions. Reply with @codex fix comments to fix any unresolved comments. About Codex ... (https://github.com/vllm-project/vllm/pull/25396#pullrequestreview-3253579643)
- `2025-09-22T15:33:21Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25396#pullrequestreview-3253587696)
- `2025-09-22T16:01:57Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25396#pullrequestreview-3253748078)
- `2025-09-22T17:39:28Z` `APPROVED` by `zhuohan123` (https://github.com/vllm-project/vllm/pull/25396#pullrequestreview-3254262168)
- `2025-09-22T17:41:47Z` `APPROVED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/25396#pullrequestreview-3254272805)

## Inline Comment Hotspots

- `vllm/platforms/cuda.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-09-22T15:32:09Z` `inline` by `chatgpt-codex-connector` `vllm/platforms/cuda.py`:344; signals: attention, blackwell, cache, cuda, flashinfer, fp8, hang, kv cache; excerpt: "[P1] Avoid forcing Triton on SM100 when only FlashInfer is missing The new branch treats any device that is not exactly SM90 as ineligible ..." (https://github.com/vllm-project/vllm/pull/25396#discussion_r2369033047)
- `2025-09-22T16:01:57Z` `inline` by `mgoin` `vllm/platforms/cuda.py`:344; signals: attention, cache, cuda, fp8, kv cache, sm100; excerpt: "fp8 kv cache is not supported for sm100 on flashattention, so I think this is right" (https://github.com/vllm-project/vllm/pull/25396#discussion_r2369175624)
- `2025-09-22T15:33:21Z` `inline` by `mgoin` `vllm/platforms/cuda.py`:341; signals: cache, cuda, dtype, kv cache; excerpt: "is kv cache dtype supported isn't used anywhere anymore :(" (https://github.com/vllm-project/vllm/pull/25396#discussion_r2369039089)
- `2025-09-22T15:32:09Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "Codex Review: Here are some suggestions. Reply with @codex fix comments to fix any unresolved comments. About Codex in GitHub [Your team has set ..." (https://github.com/vllm-project/vllm/pull/25396#pullrequestreview-3253579643)
