# PR Discussion Digest

- Source PR: [vllm-project/vllm#28076](https://github.com/vllm-project/vllm/pull/28076)
- Source page: `sources/prs/vllm/PR-28076.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28076`
- Generated at: `2026-05-20T15:38:25.499040+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-04T23:05:49Z`
- Merged: `2025-11-20T03:39:36Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: chatgpt-codex-connector, heheda12345, mergify, mgoin, pavanimajety, shengliangxu, yewentao256
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-04T23:08:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request effectively consolidates the Nvidia ModelOpt quantization configuration handling for different methods like FP8 ... (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3418909109)
- `2025-11-04T23:08:53Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3418910861)
- `2025-11-07T13:40:18Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3434002213)
- `2025-11-07T22:31:26Z` `COMMENTED` by `yewentao256` - The idea looks good to me, could you also show lm eval metrics to make sure we don't ... (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3436729847)
- `2025-11-18T17:55:12Z` `COMMENTED` by `shengliangxu` (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3479068443)
- `2025-11-18T20:39:12Z` `COMMENTED` by `shengliangxu` (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3479710478)
- `2025-11-18T21:27:15Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3479777137)
- `2025-11-19T20:15:22Z` `COMMENTED` by `shengliangxu` (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3484573486)
- `2025-11-20T03:19:15Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3485509044)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/modelopt.py`: 8 inline comment(s)

## High-Signal Discussion

- `2025-11-04T23:08:53Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/quantization/modelopt.py`:147; signals: fp4, moe, nvfp4; excerpt: ". ModelOptNvFp4Config sets FusedMoEMethodCls to ModelOptNvFp4FusedMoE, whose init signature remains (quant config, moe: FusedMoEConfig, layer). When an NVFP4 MoE layer is processed this call ..." (https://github.com/vllm-project/vllm/pull/28076#discussion_r2492278594)
- `2025-11-07T22:31:26Z` `review` `COMMENTED` by `yewentao256`; signals: accuracy; excerpt: "The idea looks good to me, could you also show lm eval metrics to make sure we don't hurt accuracy?" (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3436729847)
- `2025-11-04T23:08:53Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28076#pullrequestreview-3418910861)
- `2025-11-19T20:38:00Z` `issue` by `shengliangxu`; signals: accuracy; excerpt: "The idea looks good to me, could you also show lm eval metrics to make sure we don't hurt accuracy? working on it, will ..." (https://github.com/vllm-project/vllm/pull/28076#issuecomment-3554541335)
- `2025-11-07T13:40:18Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:223; signals: general review; excerpt: "Can we also refactor the from config? The logic is very repetitive here as well." (https://github.com/vllm-project/vllm/pull/28076#discussion_r2503606197)
- `2025-11-18T17:55:11Z` `inline` by `shengliangxu` `vllm/model_executor/layers/quantization/modelopt.py`:223; signals: general review; excerpt: "sorry for the late reply, got swamped for some other stuff, let me check it." (https://github.com/vllm-project/vllm/pull/28076#discussion_r2539169819)
- `2025-11-18T20:39:12Z` `inline` by `shengliangxu` `vllm/model_executor/layers/quantization/modelopt.py`:223; signals: general review; excerpt: "Done" (https://github.com/vllm-project/vllm/pull/28076#discussion_r2539655349)
- `2025-11-18T21:22:59Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:163; signals: general review; excerpt: "Please put an expected version number so we know when "next" is" (https://github.com/vllm-project/vllm/pull/28076#discussion_r2539701677)
- `2025-11-19T20:15:22Z` `inline` by `shengliangxu` `vllm/model_executor/layers/quantization/modelopt.py`:163; signals: general review; excerpt: "sg, updated the version number" (https://github.com/vllm-project/vllm/pull/28076#discussion_r2543427269)
- `2025-11-07T13:40:51Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @shengliangxu." (https://github.com/vllm-project/vllm/pull/28076#issuecomment-3502633673)
