# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13222](https://github.com/NVIDIA/TensorRT-LLM/pull/13222)
- Source page: `sources/prs/tensorrt-llm/PR-13222.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13222`
- Generated at: `2026-05-20T15:18:34.859191+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-20T13:15:27Z`
- Merged: `2026-04-30T08:38:05Z`

## Discussion Counts

- Issue comments: 28
- Review submissions: 11 (approved=3, commented=8)
- Inline review comments: 26
- Review threads observed: 22
- Resolved/outdated thread markers: resolved=22, outdated=17
- Human participants with discussion text: MrGeva, StanleySun639, coderabbitai, galagam, lucaslie, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-21T04:15:21Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4141366605)
- `2026-04-23T15:12:33Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4163624234)
- `2026-04-23T15:45:08Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 🧹 Nitpick comments (2) cpp/tensorrt llm/common/attentionOp.h (1) 146-147: Include v stride in bytes in ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4163880797)
- `2026-04-23T16:54:48Z` `APPROVED` by `lucaslie` - lgtm. still not a fan of the rope+attention fusion but I think it's the best we can do ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4164280094)
- `2026-04-23T18:21:03Z` `COMMENTED` by `galagam` - Left some comments, mostly nitpicking. The only blocker for me is the integration test. See (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4164681016)
- `2026-04-26T11:45:15Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4176876599)
- `2026-04-26T11:50:52Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4176881333)
- `2026-04-26T11:58:33Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4176887905)
- `2026-04-26T12:38:46Z` `COMMENTED` by `galagam` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4176924568)
- `2026-04-26T15:52:24Z` `APPROVED` by `galagam` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4177122236)
- `2026-04-27T22:54:36Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4184634144)

## Inline Comment Hotspots

- `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`: 7 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_rope_mla.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/trtllm_mla.py`: 3 inline comment(s)
- `tests/integration/test_lists/test-db/l0_b200.yml`: 2 inline comment(s)
- `tests/integration/test_lists/test-db/l0_dgx_b200.yml`: 2 inline comment(s)
- `tests/integration/defs/accuracy/references/mmlu.yaml`: 2 inline comment(s)
- `examples/auto_deploy/model_registry/configs/deepseek-r1.yaml`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/kvcache.py`: 1 inline comment(s)
- `tests/integration/test_lists/test-db/l0_h100.yml`: 1 inline comment(s)
- `examples/auto_deploy/model_registry/configs/dashboard_default.yaml`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-23T15:45:08Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, b200, compile, flashinfer, hang, kernel, mla; excerpt: "Actionable comments posted: 6 🧹 Nitpick comments (2) cpp/tensorrt llm/common/attentionOp.h (1) 146-147: Include v stride in bytes in the context params debug string. Now ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#pullrequestreview-4163880797)
- `2026-04-23T15:30:00Z` `issue` by `coderabbitai`; signals: accuracy, attention, b200, cache, compile, dtype, flashinfer, fp8; excerpt: "📝 Walkthrough Walkthrough Adds explicit V-tensor stride support for attention enqueue, introduces a complete TRT‑LLM MLA backend with prefill/decode and planner-managed paged KV cache, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#issuecomment-4305699532)
- `2026-04-23T15:45:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/trtllm_mla.py`:276; signals: block, cuda, hang, mla, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major Reallocate planner state when capacity or device changes. reset() becomes a no-op after the first forward, but this planner ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132033829)
- `2026-04-23T15:45:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/trtllm_mla.py`:1158; signals: benchmark, cache, dtype, fp8, mla, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Key the decode weight cache by compute dtype too. For FP8 checkpoints, kv b proj weight is cast to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132033847)
- `2026-04-23T15:45:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_rope_mla.py`:481; signals: cache, mla, race, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Only tag MLA nodes that were actually rewired. This loop marks every torch mla node as fused-RoPE even when ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132033876)
- `2026-04-23T15:45:07Z` `inline` by `coderabbitai` `tests/integration/test_lists/test-db/l0_dgx_b200.yml`:373; signals: b200, cute, mla, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 321 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132033881)
- `2026-04-23T17:58:40Z` `inline` by `galagam` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:1110; signals: accuracy, correctness, flashinfer, mla; excerpt: "This is a dashboard-based integration test, it is meant to verify the accuracy for the model with the up-to-date config in the model registry. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132790287)
- `2026-04-26T11:58:33Z` `inline` by `MrGeva` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:1110; signals: accuracy, attention, hang, mla; excerpt: "you are right that both tests are actually testing trtllm mla (due to recent change I made to enable it in the deepseek-r1.yaml). I ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3143438132)
- `2026-04-23T15:45:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/trtllm_mla.py`:464; signals: attention, mla, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Don't treat RoPE tables as one-time global state. ensure rope tables() only checks rope initialized, so the first qk ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132033843)
- `2026-04-26T12:38:46Z` `inline` by `galagam` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:1110; signals: accuracy, attention, flashinfer; excerpt: "@MrGeva We can't test every variant using e2e integration tests, it's just not a scaleable approach. We can set up a unit test for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3143485085)
- `2026-04-23T18:15:46Z` `inline` by `galagam` `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_rope_mla.py`:155; signals: mla, race, tensorrt; excerpt: "maybe keep this a local helper function inside trace to buffer?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132876493)
- `2026-04-23T15:45:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_rope_mla.py`:327; signals: mla, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Fail the fusion if weight re-interleave cannot be completed. undo rope deinterleave() currently logs and continues when config lookup ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13222#discussion_r3132033863)
