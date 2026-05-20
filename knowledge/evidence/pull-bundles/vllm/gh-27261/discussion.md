# PR Discussion Digest

- Source PR: [vllm-project/vllm#27261](https://github.com/vllm-project/vllm/pull/27261)
- Source page: `sources/prs/vllm/PR-27261.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27261`
- Generated at: `2026-05-20T15:38:15.309754+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-21T11:02:40Z`
- Merged: `2025-11-16T18:39:44Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 11 (approved=2, changes_requested=1, commented=8)
- Inline review comments: 12
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=3, outdated=4
- Human participants with discussion text: amirkl94, chatgpt-codex-connector, mergify, mgoin, tlrmchlsmth, tomeras91
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-21T11:11:38Z` `COMMENTED` by `tomeras91` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3360017699)
- `2025-11-05T11:21:24Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3421367297)
- `2025-11-05T12:01:52Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3421543002)
- `2025-11-05T12:25:52Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3421677956)
- `2025-11-10T09:20:37Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3441844630)
- `2025-11-11T23:28:22Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3450522895)
- `2025-11-13T18:10:52Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3461052761)
- `2025-11-13T18:13:04Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3461059247)
- `2025-11-14T15:38:01Z` `CHANGES_REQUESTED` by `mgoin` - PTAL at the failing blackwell test (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3465501017)
- `2025-11-15T14:40:01Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3468121174)
- `2025-11-16T18:39:37Z` `APPROVED` by `mgoin` - Thank you! (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3470395822)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/modelopt.py`: 9 inline comment(s)
- `tests/kernels/moe/test_flashinfer.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-10T09:20:37Z` `inline` by `amirkl94` `vllm/model_executor/layers/quantization/modelopt.py`:575; signals: cutlass, flashinfer, fp8, hang, kernel, moe, register; excerpt: "These factors are registered into the layer during process weights after loading (line 566) . They are registered to the layer when we're using ..." (https://github.com/vllm-project/vllm/pull/27261#discussion_r2509483152)
- `2025-11-14T15:37:50Z` `inline` by `mgoin` `tests/kernels/moe/test_flashinfer.py`:86; signals: blackwell, flashinfer, fp8, kernel, moe; excerpt: "This doesn't seem right as it breaks test flashinfer per tensor moe fp8 no graph on blackwell" (https://github.com/vllm-project/vllm/pull/27261#discussion_r2527934132)
- `2025-11-15T14:40:00Z` `inline` by `amirkl94` `tests/kernels/moe/test_flashinfer.py`:86; signals: flashinfer, hang, kernel, moe; excerpt: "Yeah it should be if activation == "relu2 no mul: , I originally wrote it as a one liner but the pre-commit hook complained, ..." (https://github.com/vllm-project/vllm/pull/27261#discussion_r2529932958)
- `2025-11-05T12:01:51Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/quantization/modelopt.py`:369; signals: cutlass, flashinfer, moe; excerpt: "and runs a relu2 no mul model, apply() will hit the hard assertion activation == "silu" and abort instead of falling back to the ..." (https://github.com/vllm-project/vllm/pull/27261#discussion_r2494168731)
- `2025-11-05T12:25:52Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/quantization/modelopt.py`:575; signals: flashinfer, kernel, moe; excerpt: "It looks like output1 scales gate scalar and output2 scales scalar are only used in flashinfer trtllm moe. It's not clear from the vLLM ..." (https://github.com/vllm-project/vllm/pull/27261#discussion_r2494255653)
- `2025-10-21T11:11:26Z` `inline` by `tomeras91` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:151; signals: cutlass, flashinfer, moe; excerpt: "maybe worth asserting that activation is one of the keys in activation str to value map?" (https://github.com/vllm-project/vllm/pull/27261#discussion_r2447731381)
- `2025-11-14T15:38:01Z` `review` `CHANGES_REQUESTED` by `mgoin`; signals: blackwell, failing; excerpt: "PTAL at the failing blackwell test" (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3465501017)
- `2025-11-11T23:17:37Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:366; signals: flashinfer, moe; excerpt: "It seems you are missing the override of self.flashinfer moe backend here" (https://github.com/vllm-project/vllm/pull/27261#discussion_r2516118768)
- `2025-11-11T23:28:20Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:366; signals: flashinfer, moe; excerpt: "It looks like the self.flashinfer moe backend override was left out" (https://github.com/vllm-project/vllm/pull/27261#discussion_r2516145808)
- `2025-11-11T23:28:00Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:575; signals: kernel; excerpt: "I can remove the if else when setting the quantization and set it the same for all paths. I think I'd prefer to just ..." (https://github.com/vllm-project/vllm/pull/27261#discussion_r2516144946)
- `2025-11-05T12:01:52Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/27261#pullrequestreview-3421543002)
- `2025-10-21T11:10:37Z` `inline` by `tomeras91` `vllm/model_executor/layers/quantization/modelopt.py`:645; signals: general review; excerpt: "1. why did you remove the assert that renormalize is not True? 2. Maybe worth asserting that activation is either "silu" or "relu2"?" (https://github.com/vllm-project/vllm/pull/27261#discussion_r2447728053)
