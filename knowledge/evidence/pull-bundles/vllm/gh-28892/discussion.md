# PR Discussion Digest

- Source PR: [vllm-project/vllm#28892](https://github.com/vllm-project/vllm/pull/28892)
- Source page: `sources/prs/vllm/PR-28892.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28892`
- Generated at: `2026-05-20T15:38:35.361799+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-18T00:17:22Z`
- Merged: `2025-11-21T16:54:11Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 11
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: Victor49152, chatgpt-codex-connector, jiahanc, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-18T00:18:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the Flashinfer TRT-LLM FP4 kernel for MoE layers and refactors ... (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3475010909)
- `2025-11-18T00:23:09Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review . The shared kernel expects the same scale layout as the ModelOpt path (see modelopt.py ... (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3475028083)
- `2025-11-19T21:31:58Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3484790640)
- `2025-11-19T21:33:03Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3484828106)
- `2025-11-19T23:06:08Z` `COMMENTED` by `Victor49152` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3485067500)
- `2025-11-19T23:17:13Z` `COMMENTED` by `jiahanc` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3485094089)
- `2025-11-19T23:18:34Z` `COMMENTED` by `Victor49152` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3485097228)
- `2025-11-19T23:19:05Z` `COMMENTED` by `Victor49152` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3485098074)
- `2025-11-20T02:31:27Z` `COMMENTED` by `Victor49152` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3485439463)
- `2025-11-20T02:33:08Z` `COMMENTED` by `Victor49152` (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3485442433)
- `2025-11-20T23:32:13Z` `APPROVED` by `mgoin` - Great work @Victor49152 ! I appreciate the careful testing and reporting (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3490523173)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 10 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-18T00:23:09Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: kernel, layout, moe; excerpt: "💡 Codex Review . The shared kernel expects the same scale layout as the ModelOpt path (see modelopt.py lines 1496–1507), which multiplies by the ..." (https://github.com/vllm-project/vllm/pull/28892#pullrequestreview-3475028083)
- `2025-11-19T23:06:08Z` `inline` by `Victor49152` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:395; signals: hang, kernel, moe; excerpt: "From what I inspect from the both quantized checkpoint for Qwen, this w13 input global scale contains identical values for all elements, and the ..." (https://github.com/vllm-project/vllm/pull/28892#discussion_r2543831931)
- `2025-11-18T00:25:48Z` `issue` by `Victor49152`; signals: kernel, layout, moe; excerpt: "💡 Codex Review . The shared kernel expects the same scale layout as the ModelOpt path (see modelopt.py lines 1496–1507), which multiplies by the ..." (https://github.com/vllm-project/vllm/pull/28892#issuecomment-3544484094)
- `2025-11-20T02:33:08Z` `inline` by `Victor49152` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:395; signals: accuracy, moe; excerpt: "I added the same processing to w13 input global scale, and re-run all the accuracy check on 235B models, results are updated in the ..." (https://github.com/vllm-project/vllm/pull/28892#discussion_r2544144105)
- `2025-11-19T23:18:34Z` `inline` by `Victor49152` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:395; signals: hang, moe; excerpt: "I see, I will add the change and retest the results shortly. Thanks" (https://github.com/vllm-project/vllm/pull/28892#discussion_r2543853803)
- `2025-11-19T21:20:47Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:395; signals: moe; excerpt: "Why don't we need to do the same processing for w13 input global scale? I see that modelopt seems to do both" (https://github.com/vllm-project/vllm/pull/28892#discussion_r2543604784)
- `2025-11-19T23:17:12Z` `inline` by `jiahanc` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:395; signals: moe; excerpt: "Not sure about compressed tensor, but in modelopt checkpoint, the values can vary in w13 input global scale, so we need to do the ..." (https://github.com/vllm-project/vllm/pull/28892#discussion_r2543851643)
- `2025-11-19T21:32:57Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:321; signals: moe; excerpt: "nit: we should generalize this as well between ct and modelopt" (https://github.com/vllm-project/vllm/pull/28892#discussion_r2543634934)
- `2025-11-19T23:19:05Z` `inline` by `Victor49152` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:321; signals: moe; excerpt: "SGTM, on it" (https://github.com/vllm-project/vllm/pull/28892#discussion_r2543854559)
- `2025-11-20T02:31:27Z` `inline` by `Victor49152` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:321; signals: moe; excerpt: "It's moved to utils too" (https://github.com/vllm-project/vllm/pull/28892#discussion_r2544141779)
- `2025-11-20T03:48:50Z` `issue` by `Victor49152`; signals: hang; excerpt: "@mgoin Hi Michael, I cleaned up this PR and re-tested everything, also catched a small breaking change from main branch into modelopt path. I ..." (https://github.com/vllm-project/vllm/pull/28892#issuecomment-3555644738)
- `2025-11-19T18:26:04Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @Victor49152." (https://github.com/vllm-project/vllm/pull/28892#issuecomment-3554090225)
