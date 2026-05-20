# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12320](https://github.com/NVIDIA/TensorRT-LLM/pull/12320)
- Source page: `sources/prs/tensorrt-llm/PR-12320.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12320`
- Generated at: `2026-05-20T15:18:07.987690+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-18T15:45:30Z`
- Merged: `2026-05-02T15:15:28Z`

## Discussion Counts

- Issue comments: 47
- Review submissions: 13 (approved=4, changes_requested=1, commented=8)
- Inline review comments: 22
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=16, outdated=6
- Human participants with discussion text: HuiGao-NV, brb-nv, coderabbitai, hchings, liji-nv, pengbowang-nv, shuyixiong, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-22T05:41:05Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 12 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4152286641)
- `2026-04-22T08:42:09Z` `CHANGES_REQUESTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4153213113)
- `2026-04-22T08:52:25Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4153303899)
- `2026-04-24T02:01:39Z` `APPROVED` by `brb-nv` - Approving changes under tensorrt llm/ torch/models/. Please let @pengbowang-nv review the Attention part. (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4167385721)
- `2026-04-24T02:31:05Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4167473675)
- `2026-04-24T02:40:59Z` `APPROVED` by `HuiGao-NV` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4167498587)
- `2026-04-24T02:54:46Z` `COMMENTED` by `pengbowang-nv` - Attention part tensorrt llm/ torch/modules/attention.py LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4167546990)
- `2026-04-28T05:35:32Z` `COMMENTED` by `hchings` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4186033493)
- `2026-04-28T14:23:23Z` `COMMENTED` by `shuyixiong` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4189645499)
- `2026-04-28T14:29:02Z` `COMMENTED` by `shuyixiong` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4189697940)
- `2026-04-28T14:29:23Z` `COMMENTED` by `shuyixiong` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4189700707)
- `2026-04-28T14:30:20Z` `COMMENTED` by `shuyixiong` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4189708895)
- `2026-04-30T04:31:07Z` `APPROVED` by `hchings` (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4202444202)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/linear.py`: 6 inline comment(s)
- `tensorrt_llm/_torch/model_config.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/modules/attention.py`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`: 2 inline comment(s)
- `tensorrt_llm/llmapi/llm_utils.py`: 2 inline comment(s)
- `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/thop/moeOp.cpp`: 1 inline comment(s)
- `tensorrt_llm/_torch/models/checkpoints/hf/weight_mapper.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-22T05:41:05Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, bf16, block, cutlass, gemm, hang, kernel, moe; excerpt: "Actionable comments posted: 12 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#pullrequestreview-4152286641)
- `2026-04-22T05:41:02Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:4227; signals: cutlass, fp4, gemm, kernel, moe, tensorrt, tma, warp; excerpt: "⚠️ Potential issue 🟠 Major Don't switch GEMM2 to the dynamic alpha buffer under a looser predicate than the producer path. computeStridesTmaWarpSpecialized() runs before ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793355)
- `2026-04-22T05:40:59Z` `issue` by `coderabbitai`; signals: attention, cache, cutlass, fp4, fp8, gemm, hang, kernel; excerpt: "📝 Walkthrough Walkthrough This PR introduces dynamic runtime scaling support for FP4 quantization in MoE layers, adding new kernel implementations and control flow for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#issuecomment-4293829683)
- `2026-04-22T05:41:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/attention.py`:747; signals: attention, bf16, compile, fp4, fp8, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Keep the torch.compile output allocation in sync with this BF16 path. These lines stop passing out scale/out scale sf, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793381)
- `2026-04-22T08:52:24Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/attention.py`:747; signals: attention, bf16, compile, fp4, fp8, nvfp4, tensorrt; excerpt: "@liji-nv, happy to help fix this. The issue is that create output() allocates the output buffer using only self. use quantize output(), but attn ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3122707452)
- `2026-04-22T05:41:02Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2704; signals: cutlass, fp4, gemm, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Handle the full activation set here, or gate dynamic FC2 before dispatch. The normal doActivation() path supports Identity, Gelu, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793347)
- `2026-04-22T05:41:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/model_config.py`:450; signals: benchmark, cute, fp4, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 102 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793365)
- `2026-04-22T05:41:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:640; signals: cutlass, fp4, moe, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Gate use dynamic fc2 scale with the same predicate as the extra scale tensor. quant scales only includes fc2 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793386)
- `2026-04-22T05:41:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:489; signals: cutlass, fp4, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Guard the dynamic scale computation against all-zero inputs. If x is all zeros, amax input becomes 0 and dyn ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793384)
- `2026-04-28T05:17:25Z` `inline` by `hchings` `tensorrt_llm/_torch/modules/linear.py`:2823; signals: fp4, fp8, nvfp4, tensorrt; excerpt: "Should we widen the allowlist here (e.g., if not isinstance(self.quant method, (UnquantizedLinearMethod, FP8QDQLinearMethod, NVFP4LinearMethod)):) instead of deleting this assertion entirely?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3151730642)
- `2026-04-22T05:41:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/linear.py`:1614; signals: fp4, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Keep the non-partial fused NVFP4 load path independent of fused weight shard indices mapping. Both fused NVFP4 loaders now ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793391)
- `2026-04-22T05:41:03Z` `inline` by `coderabbitai` `tensorrt_llm/llmapi/llm_utils.py`:504; signals: cache, cute, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1124 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12320#discussion_r3121793399)
