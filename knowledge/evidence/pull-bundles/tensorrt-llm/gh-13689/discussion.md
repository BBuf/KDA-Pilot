# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13689](https://github.com/NVIDIA/TensorRT-LLM/pull/13689)
- Source page: `sources/prs/tensorrt-llm/PR-13689.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13689`
- Generated at: `2026-05-20T15:18:51.741781+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-01T16:47:06Z`
- Merged: `2026-05-18T02:14:53Z`

## Discussion Counts

- Issue comments: 81
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 9
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=7
- Human participants with discussion text: HuiGao-NV, StanleySun639, ZhanruiSunCh, coderabbitai, nv-guomingz, rosenrodt, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-03T13:30:10Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#pullrequestreview-4216359487)
- `2026-05-05T01:56:09Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#pullrequestreview-4224786400)
- `2026-05-12T04:58:00Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#pullrequestreview-4269256155)
- `2026-05-12T15:37:06Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#pullrequestreview-4273868575)
- `2026-05-18T02:09:23Z` `APPROVED` by `ZhanruiSunCh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#pullrequestreview-4306842739)
- `2026-05-18T02:10:08Z` `APPROVED` by `HuiGao-NV` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#pullrequestreview-4306844106)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/quantization.py`: 2 inline comment(s)
- `tests/unittest/_torch/modules/moe/moe_test_utils.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`: 1 inline comment(s)
- `tests/integration/defs/.test_durations`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-03T13:30:10Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, b200, block, failing, hang, moe, tensorrt; excerpt: "Actionable comments posted: 7 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#pullrequestreview-4216359487)
- `2026-05-03T13:30:04Z` `issue` by `coderabbitai`; signals: accuracy, b200, bf16, block, cute, cutlass, flashinfer, fp8; excerpt: "📝 Walkthrough Walkthrough This PR introduces BF16 unquantized execution support for the TRTLLMGen fused MoE backend by integrating FlashInfer-backed operations. It refactors backend selection ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#issuecomment-4366283123)
- `2026-05-03T13:30:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:716; signals: accuracy, bf16, flashinfer, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win BF16 can still hit the direct FlashInfer router kernel. This branch accepts non-None router logits, and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3178180418)
- `2026-05-03T13:30:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:732; signals: bf16, block, layout, moe, register, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Process shared BF16 expert buffers through the same layout transform. process weights after loading() only rewrites ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3178180419)
- `2026-05-03T13:30:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:732; signals: bf16, memory, moe, oom, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Avoid duplicating the full BF16 MoE weights during post-load conversion. Both torch.stack([...]) calls allocate a second ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3178180421)
- `2026-05-03T13:30:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`:155; signals: cute, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 10521 --- Inconsistent attribute access: layer quant mode ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3178180414)
- `2026-05-03T13:30:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:340; signals: block, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Reflow this signature to clear the flake8 E125 failure. Static analysis is already flagging Line 324 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3178180415)
- `2026-05-03T13:30:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:195; signals: moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Mutates original model config when override quant config is None. When override quant config is None, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3178180413)
- `2026-05-03T13:30:07Z` `inline` by `coderabbitai` `tests/integration/defs/.test_durations`:301; signals: bf16, cutlass; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Add duration entries for the new tp2 BF16 cases. Line 298 and Line 299 add tp1 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3178180424)
- `2026-05-12T04:58:01Z` `inline` by `rosenrodt` `tests/unittest/_torch/modules/moe/moe_test_utils.py`:365; signals: moe; excerpt: "The following assignment is missing. We should put this line above line 267 because 271/292 will use it" (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3223807429)
- `2026-05-12T15:37:06Z` `inline` by `nv-guomingz` `tests/unittest/_torch/modules/moe/moe_test_utils.py`:365; signals: moe; excerpt: "Updated" (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#discussion_r3227765810)
- `2026-05-02T08:58:55Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46512]( [ run ] completed with state SUCCESS. Commit: 0cbea83 [/LLM/main/L0 MergeRequest PR pipeline 36572]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13689#issuecomment-4363456751)
