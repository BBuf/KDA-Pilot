# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12136](https://github.com/NVIDIA/TensorRT-LLM/pull/12136)
- Source page: `sources/prs/tensorrt-llm/PR-12136.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12136`
- Generated at: `2026-05-20T15:18:04.490930+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-12T03:36:37Z`
- Merged: `2026-04-02T03:51:59Z`

## Discussion Counts

- Issue comments: 55
- Review submissions: 32 (approved=8, changes_requested=1, commented=23)
- Inline review comments: 89
- Review threads observed: 74
- Resolved/outdated thread markers: resolved=74, outdated=52
- Human participants with discussion text: JintaoPengCS, Kefeng-Duan, QiJune, Shixiaowei02, Superjomn, chuangz0, coderabbitai, hyukn, liji-nv, syuoni, tensorrt-cicd, tianyuz-nv, wanqian-nv, xinhe-nv, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T06:17:18Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3934101096)
- `2026-03-12T06:43:59Z` `COMMENTED` by `syuoni` - This is a nice feature, great to see it's going to production. Regarding the CuTeDSL MoE interface, overall ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3934108792)
- `2026-03-12T07:50:52Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3934606717)
- `2026-03-12T16:39:26Z` `COMMENTED` by `wanqian-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3933776644)
- `2026-03-13T11:31:18Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3943360089)
- `2026-03-17T02:42:01Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3957864302)
- `2026-03-17T02:49:14Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3957881430)
- `2026-03-17T02:50:07Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3957883614)
- `2026-03-17T02:50:44Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3957884899)
- `2026-03-17T02:51:17Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3957886219)
- `2026-03-24T02:47:00Z` `COMMENTED` by `wanqian-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3995896849)
- `2026-03-24T02:52:26Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 20 [!NOTE] Due to the large number of review comments, Critical, Major severity comments were ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3995908285)
- `2026-03-24T07:27:47Z` `APPROVED` by `xinhe-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3996893319)
- `2026-03-24T08:51:27Z` `COMMENTED` by `Superjomn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3997335585)
- `2026-03-25T06:31:55Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4004328210)
- `2026-03-25T06:56:15Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4004416954)
- `2026-03-25T07:33:28Z` `CHANGES_REQUESTED` by `Shixiaowei02` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4004569458)
- `2026-03-25T10:39:51Z` `APPROVED` by `hyukn` - LGTM. But be aware of the potential overhead inside the custom op forward. (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4005653772)
- `2026-03-30T02:34:50Z` `COMMENTED` by `tianyuz-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4027717573)
- `2026-03-30T05:14:39Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4027848233)
- `2026-03-30T05:15:51Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4028074801)
- `2026-03-30T06:22:55Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4028254335)
- `2026-03-30T11:00:51Z` `APPROVED` by `chuangz0` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4029746571)
- `2026-03-30T11:02:15Z` `COMMENTED` by `chuangz0` (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-4029754485)
- ... 8 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/pyexecutor/dwdp.py`: 19 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`: 11 inline comment(s)
- `tensorrt_llm/llmapi/llm_args.py`: 8 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 7 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`: 7 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`: 5 inline comment(s)
- `cpp/tensorrt_llm/thop/moeAlltoAllOp.cpp`: 5 inline comment(s)
- `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/pyexecutor/py_executor.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/interface.py`: 4 inline comment(s)
- `examples/disaggregated/slurm/benchmark/submit.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-24T02:52:26Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, b200, benchmark, blackwell, block, cute, gemm, hang; excerpt: "Actionable comments posted: 20 [!NOTE] Due to the large number of review comments, Critical, Major severity comments were prioritized as inline comments. [!CAUTION] Some ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#pullrequestreview-3995908285)
- `2026-03-24T02:52:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:812; signals: blackwell, block, cute, dtype, gemm, kernel, layout, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Validate the multi-B tuple contract before building TMA state. This path assumes b, sfb, and alpha all have exactly ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2978684919)
- `2026-03-30T02:34:49Z` `inline` by `tianyuz-nv` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2092; signals: compile, correctness, cute, gemm, kernel, moe, perf, performance; excerpt: "Thanks for the commet. We looked into the launch overhead for this path. The multi-B support adds a few extra make ptr() calls compared ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r3007231527)
- `2026-03-24T02:52:19Z` `issue` by `coderabbitai`; signals: accuracy, b200, benchmark, blackwell, block, cuda, cute, fp4; excerpt: "📝 Walkthrough Walkthrough This pull request introduces DWDP (double-weighted distributed prefetching) support for disaggregated MoE serving and extends CUTE DSL GEMM kernels to support ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#issuecomment-4115017790)
- `2026-03-12T05:46:24Z` `inline` by `syuoni` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:941; signals: blackwell, block, cute, cutlass, gemm, kernel, tensorrt; excerpt: "So currently, the kernel supports up to 4 B tensors, right? Does cutlass.range constexpr(self.num b tensors) work here?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2922436603)
- `2026-03-12T05:53:17Z` `inline` by `syuoni` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:2151; signals: blackwell, block, cute, gemm, kernel, tensorrt, vector; excerpt: "Can we make a vector that maps expert idx to B tensor index? So that we can avoid these runtime condition checks here." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2922457334)
- `2026-03-12T06:17:08Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:788; signals: block, cute, fp4, hang, moe, nvfp4, tensorrt; excerpt: "The DWDP integration adds 8 weight-related parameters to run moe nvfp4 / run moe nvfp4 impl (6 → 14 params), and the same weights ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2922525580)
- `2026-03-17T02:42:01Z` `inline` by `tianyuz-nv` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2242; signals: blackwell, cute, fp4, gemm, kernel, nvfp4, tensorrt; excerpt: "Done. The original single-B interface cute dsl nvfp4 gather grouped gemm swiglu blackwell is preserved as a thin wrapper that dispatches to the new ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2944042224)
- `2026-03-17T02:49:14Z` `inline` by `tianyuz-nv` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:686; signals: blackwell, cute, fp4, gemm, moe, nvfp4, tensorrt; excerpt: "No, cute dsl nvfp4 grouped gemm blackwell (the non-fused-finalize FC2 op) does not support multiple B weights, and it does not need to. This ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2944060200)
- `2026-03-17T02:50:07Z` `inline` by `tianyuz-nv` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:587; signals: autotune, cache, cute, fp4, moe, nvfp4, tensorrt; excerpt: "No cache key update is needed. The NvFp4WeightView dataclass in the inputs list is handled safely by AutoTuner. AutoTuner. get input sizes() checks isinstance(input, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2944062573)
- `2026-03-24T02:52:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1471; signals: block, cache, cute, gemm, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1168 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2978684914)
- `2026-03-24T02:52:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`:2967; signals: blackwell, block, cute, gemm, hang, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical wrapper crashes when b tensor l sizes is None (single-B backward-compat mode). In init , when b tensor l ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12136#discussion_r2978684927)
