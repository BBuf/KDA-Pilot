# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#6538](https://github.com/NVIDIA/TensorRT-LLM/pull/6538)
- Source page: `sources/prs/tensorrt-llm/PR-6538.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-6538`
- Generated at: `2026-05-20T15:19:11.434855+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-01T04:42:05Z`
- Merged: `2025-08-19T14:04:48Z`

## Discussion Counts

- Issue comments: 37
- Review submissions: 28 (approved=6, commented=22)
- Inline review comments: 35
- Review threads observed: 30
- Resolved/outdated thread markers: resolved=30, outdated=11
- Human participants with discussion text: PerkzZheng, brb-nv, coderabbitai, jdebache, jmydurant, juney-nvidia, kaiyux, lancelly, litaotju, tensorrt-cicd, yuxianq, zhhuang-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-01T04:49:43Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🔭 Outside diff range comments (1) cpp/tensorrt llm/kernels/mlaKernels.cu (1) 1-3: Update copyright year to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3077629857)
- `2025-08-01T09:30:33Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🔭 Outside diff range comments (1) cpp/tensorrt llm/kernels/mlaKernels.cu (1) 1-15: Update copyright year to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3078429085)
- `2025-08-01T09:42:23Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (1) tensorrt llm/ torch/attention backend/trtllm.py (1) 201-201: Line exceeds maximum length ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3078464734)
- `2025-08-01T09:48:38Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (2) tensorrt llm/ torch/attention backend/trtllm.py (1) 201-201: Consider breaking long documentation ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3078490132)
- `2025-08-04T03:31:22Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (3) tensorrt llm/ torch/attention backend/trtllm.py (2) 70-70: Consider using Optional typing ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3082579553)
- `2025-08-04T03:40:08Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🔭 Outside diff range comments (1) cpp/tests/unit tests/kernels/mlaPreprocessTest.cu (1) 2-2: Update copyright header to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3082586494)
- `2025-08-05T04:45:43Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3086492472)
- `2025-08-08T06:38:30Z` `COMMENTED` by `jdebache` - Looks good overall. For my understanding and curiosity, could you confirm: before the changes, we needed to 'fake' ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3099630932)
- `2025-08-14T16:11:32Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 🔭 Outside diff range comments (2) cpp/tensorrt llm/kernels/mlaKernels.cu (1) 187-282: Fix k-buffer index — ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3121198108)
- `2025-08-15T03:35:01Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122729213)
- `2025-08-15T03:40:28Z` `COMMENTED` by `zhhuang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122736606)
- `2025-08-15T03:46:17Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🔭 Outside diff range comments (3) cpp/tensorrt llm/kernels/mlaChunkedPrefill.cu (1) 340-355: Add bfloat16 include to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122743175)
- `2025-08-15T03:53:23Z` `COMMENTED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122752988)
- `2025-08-15T04:54:03Z` `COMMENTED` by `zhhuang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122845595)
- `2025-08-15T05:05:50Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🔭 Outside diff range comments (5) cpp/tensorrt llm/kernels/fmhaDispatcher.cpp (2) 141-159: Unify QKV layout mapping ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122867432)
- `2025-08-15T06:30:54Z` `APPROVED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3123071441)
- `2025-08-17T16:36:56Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 ♻️ Duplicate comments (7) cpp/kernels/fmha v2/fmha test.py (2) 168-169: Include SM121 in FP8 MLA ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3126400542)
- `2025-08-18T07:54:33Z` `APPROVED` by `litaotju` - I approve for the DS modeling file. We need perf data before merge. (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127209832)
- `2025-08-18T08:06:26Z` `APPROVED` by `lancelly` - Changes for bindings and attention op looks good to me. (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127245516)
- `2025-08-18T08:40:05Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 🔭 Outside diff range comments (2) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/kernelParams.h (1) 356-371: Non-FP8 separate V: strideHeads ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127371960)
- `2025-08-18T08:45:44Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127391932)
- `2025-08-18T09:11:32Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127504279)
- `2025-08-18T09:12:29Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127507259)
- `2025-08-18T09:24:59Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127554809)
- ... 4 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/cubin/fmha_cubin.h`: 7 inline comment(s)
- `cpp/tensorrt_llm/thop/attentionOp.cpp`: 5 inline comment(s)
- `examples/models/core/deepseek_v3/README.md`: 4 inline comment(s)
- `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`: 4 inline comment(s)
- `cpp/tensorrt_llm/common/attentionOp.cpp`: 2 inline comment(s)
- `cpp/kernels/fmha_v2/fmha_test.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/kernelParams.h`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/attention.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/trtllm.py`: 1 inline comment(s)
- `cpp/kernels/fmha_v2/setup.py`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fmhaRunner.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/mlaKernels.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-01T04:49:43Z` `review` `COMMENTED` by `coderabbitai`; signals: alignment, attention, block, cache, compile, hang, kernel, kv cache; excerpt: "Actionable comments posted: 2 🔭 Outside diff range comments (1) cpp/tensorrt llm/kernels/mlaKernels.cu (1) 1-3: Update copyright year to 2025 The copyright header should include ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3077629857)
- `2025-08-01T09:30:33Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, compile, hang, kernel, kv cache, layout; excerpt: "Actionable comments posted: 0 🔭 Outside diff range comments (1) cpp/tensorrt llm/kernels/mlaKernels.cu (1) 1-15: Update copyright year to 2025. According to the coding guidelines, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3078429085)
- `2025-08-01T09:42:23Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, compile, hang, kernel, kv cache, layout; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (1) tensorrt llm/ torch/attention backend/trtllm.py (1) 201-201: Line exceeds maximum length limit. Line 201 is 148 characters ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3078464734)
- `2025-08-01T09:48:38Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, compile, dtype, hang, kernel, kv cache; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (2) tensorrt llm/ torch/attention backend/trtllm.py (1) 201-201: Consider breaking long documentation line for better readability. The documentation ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3078490132)
- `2025-08-04T03:31:22Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, compile, fp8, hang, kernel, kv cache; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (3) tensorrt llm/ torch/attention backend/trtllm.py (2) 70-70: Consider using Optional typing for consistency. The softmax stats tensor ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3082579553)
- `2025-08-04T03:40:08Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, compile, cuda, hang, kernel, kv cache; excerpt: "Actionable comments posted: 0 🔭 Outside diff range comments (1) cpp/tests/unit tests/kernels/mlaPreprocessTest.cu (1) 2-2: Update copyright header to include current year. The copyright header ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3082586494)
- `2025-08-14T16:11:32Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, bf16, block, cache, compile, correctness, flash attention, fp8; excerpt: "Actionable comments posted: 7 🔭 Outside diff range comments (2) cpp/tensorrt llm/kernels/mlaKernels.cu (1) 187-282: Fix k-buffer index — dst k idx uses the wrong ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3121198108)
- `2025-08-15T03:46:17Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, cache, cuda, fp8, hang, kernel, kv cache, layout; excerpt: "Actionable comments posted: 3 🔭 Outside diff range comments (3) cpp/tensorrt llm/kernels/mlaChunkedPrefill.cu (1) 340-355: Add bfloat16 include to support the new nv bfloat16 instantiation ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122743175)
- `2025-08-15T05:05:50Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, attention, bf16, block, cache, dtype, fp8, hang; excerpt: "Actionable comments posted: 1 🔭 Outside diff range comments (5) cpp/tensorrt llm/kernels/fmhaDispatcher.cpp (2) 141-159: Unify QKV layout mapping in run(): use AttentionInputLayoutToQkvLayout() The run ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3122867432)
- `2025-08-17T16:36:56Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, attention, bf16, cache, compile, correctness, cuda; excerpt: "Actionable comments posted: 3 ♻️ Duplicate comments (7) cpp/kernels/fmha v2/fmha test.py (2) 168-169: Include SM121 in FP8 MLA gating Allow both SM120 and SM121; ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3126400542)
- `2025-08-18T08:40:05Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, attention, b200, bf16, blackwell, block, cache; excerpt: "Actionable comments posted: 4 🔭 Outside diff range comments (2) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/kernelParams.h (1) 356-371: Non-FP8 separate V: strideHeads likely needs adjustment to include KNoPE ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3127371960)
- `2025-08-18T16:25:17Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, bf16, block, cache, dtype, flash attention, fp8, hang; excerpt: "Actionable comments posted: 4 🔭 Outside diff range comments (6) cpp/tensorrt llm/common/attentionOp.cpp (2) 770-772: Under-allocation: include mFP8ContextMLA in BMM scale workspace sizes fmha bmm1 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6538#pullrequestreview-3129086107)
