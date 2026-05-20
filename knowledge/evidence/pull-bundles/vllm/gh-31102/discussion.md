# PR Discussion Digest

- Source PR: [vllm-project/vllm#31102](https://github.com/vllm-project/vllm/pull/31102)
- Source page: `sources/prs/vllm/PR-31102.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31102`
- Generated at: `2026-05-20T15:39:14.216663+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-21T18:54:51Z`
- Merged: `2025-12-22T23:42:59Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: chatgpt-codex-connector, maleksan85, mgoin, micah-wil, robertgshaw2-redhat, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-12-21T18:56:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces changes for MoE refactoring, specifically for AITER modular kernels, and adds support ... (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3601908602)
- `2025-12-21T19:22:53Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3601919557)
- `2025-12-22T15:40:50Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3604580174)
- `2025-12-22T15:48:04Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3604605571)
- `2025-12-22T15:49:09Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3604611592)
- `2025-12-22T19:48:50Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3605509991)
- `2025-12-22T23:42:46Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3606088168)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/prepare_finalize.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-22T15:40:50Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/quantization/fp8.py`:1120; signals: correctness, fp8; excerpt: ", but that prepare class multiplies a1 by topk weights whenever apply router weight on input is true (prepare finalize.py 46-53). AiterExperts then reports ..." (https://github.com/vllm-project/vllm/pull/31102#discussion_r2640307144)
- `2025-12-21T19:22:53Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/fused_moe.py`:2135; signals: moe, triton; excerpt: "not: triton was broken on main before this for ROCM" (https://github.com/vllm-project/vllm/pull/31102#discussion_r2638046860)
- `2025-12-22T15:49:09Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/quantization/fp8.py`:193; signals: fp8; excerpt: "We can do this is a separate PR. Importing rocm aiter ops at this step is not allowed because it initializes things that are ..." (https://github.com/vllm-project/vllm/pull/31102#discussion_r2640341112)
- `2025-12-22T15:40:50Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/31102#pullrequestreview-3604580174)
- `2025-12-22T15:48:04Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/fp8.py`:193; signals: fp8; excerpt: "let's use" (https://github.com/vllm-project/vllm/pull/31102#discussion_r2640335481)
- `2025-12-22T19:48:50Z` `inline` by `maleksan85` `vllm/model_executor/layers/fused_moe/prepare_finalize.py`:58; signals: moe; excerpt: "would be easier to read and support if the names of returned parameters are provided." (https://github.com/vllm-project/vllm/pull/31102#discussion_r2641052456)
