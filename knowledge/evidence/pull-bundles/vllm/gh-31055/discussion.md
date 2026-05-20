# PR Discussion Digest

- Source PR: [vllm-project/vllm#31055](https://github.com/vllm-project/vllm/pull/31055)
- Source page: `sources/prs/vllm/PR-31055.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31055`
- Generated at: `2026-05-20T15:39:14.209740+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-20T02:18:47Z`
- Merged: `2026-01-06T17:57:57Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: ReinforcedKnowledge, chatgpt-codex-connector, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-20T02:21:47Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/31055#pullrequestreview-3600627502)
- `2025-12-20T02:21:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a critical dtype mismatch issue that occurs when running GLM-4 MoE models ... (https://github.com/vllm-project/vllm/pull/31055#pullrequestreview-3600628286)
- `2025-12-22T15:03:53Z` `COMMENTED` by `yewentao256` - Thanks for the work! Is there any other way to fix this? I am worried changing dtype during ... (https://github.com/vllm-project/vllm/pull/31055#pullrequestreview-3604415631)
- `2026-01-05T16:25:31Z` `APPROVED` by `yewentao256` - Sorry for the late response. LGTM, thanks for the work! Could you also test the E2E accuracy using ... (https://github.com/vllm-project/vllm/pull/31055#pullrequestreview-3627545532)

## Inline Comment Hotspots

- `vllm/model_executor/models/glm4_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-06T00:58:21Z` `issue` by `ReinforcedKnowledge`; signals: accuracy, failing, h100, hang, perf, performance, throughput; excerpt: "Hey! No worries at all! I've ran some E2E accuracy and performance testing, please let me know if they're not enough, or if you ..." (https://github.com/vllm-project/vllm/pull/31055#issuecomment-3712643066)
- `2025-12-20T02:21:47Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/models/glm4_moe.py`:209; signals: bf16, dtype, hang, moe, tma; excerpt: "path GLM-4 MoE now runs softmax/top-k on bf16/fp16 instead of the float32 logits it previously produced by explicitly casting the input and keeping the ..." (https://github.com/vllm-project/vllm/pull/31055#discussion_r2636711677)
- `2025-12-22T15:03:53Z` `review` `COMMENTED` by `yewentao256`; signals: dtype, hang, perf, performance; excerpt: "Thanks for the work! Is there any other way to fix this? I am worried changing dtype during forward, which may reduce performance" (https://github.com/vllm-project/vllm/pull/31055#pullrequestreview-3604415631)
- `2025-12-22T23:27:30Z` `issue` by `ReinforcedKnowledge`; signals: dtype, fp4, hang, memory, moe; excerpt: "Thanks for the feedback! I totally agree, I'm not comfortable with that change either. Here's how I see it, the issue is the assert ..." (https://github.com/vllm-project/vllm/pull/31055#issuecomment-3684536998)
- `2026-01-05T16:25:31Z` `review` `APPROVED` by `yewentao256`; signals: accuracy, perf, performance; excerpt: "Sorry for the late response. LGTM, thanks for the work! Could you also test the E2E accuracy using lm eval ... and performance using ..." (https://github.com/vllm-project/vllm/pull/31055#pullrequestreview-3627545532)
- `2026-01-04T20:45:39Z` `issue` by `ReinforcedKnowledge`; signals: dtype, moe; excerpt: "Hey! I've updated the PR to use a configurable router logits dtype parameter instead of casting during forward pass. This allows model writers to ..." (https://github.com/vllm-project/vllm/pull/31055#issuecomment-3708411601)
- `2025-12-20T02:21:47Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/31055#pullrequestreview-3600627502)
