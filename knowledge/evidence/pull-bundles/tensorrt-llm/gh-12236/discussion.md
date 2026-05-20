# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12236](https://github.com/NVIDIA/TensorRT-LLM/pull/12236)
- Source page: `sources/prs/tensorrt-llm/PR-12236.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12236`
- Generated at: `2026-05-20T15:18:04.516379+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-16T05:29:44Z`
- Merged: `2026-03-19T04:05:36Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 53 (approved=3, commented=50)
- Inline review comments: 64
- Review threads observed: 33
- Resolved/outdated thread markers: resolved=33, outdated=22
- Human participants with discussion text: Superjomn, coderabbitai, hyukn, limin2021, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-16T05:41:06Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 9 🧹 Nitpick comments (7) tensorrt llm/ torch/cute dsl kernels/blackwell/top k/filtered top k decode varlen.py ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3951558138)
- `2026-03-17T07:07:14Z` `APPROVED` by `Superjomn` - LGTM on the llm api (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3958614462)
- `2026-03-17T08:24:24Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3958892023)
- `2026-03-17T10:00:55Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3959520330)
- `2026-03-17T14:48:10Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3961373310)
- `2026-03-17T14:48:33Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3961377143)
- `2026-03-17T14:50:54Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3961401298)
- `2026-03-17T14:55:52Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3961451864)
- `2026-03-18T01:21:46Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3964511616)
- `2026-03-18T01:27:39Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3964525169)
- `2026-03-18T01:51:59Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3964575386)
- `2026-03-18T07:52:37Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965748960)
- `2026-03-18T08:00:49Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965781775)
- `2026-03-18T08:06:47Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965806167)
- `2026-03-18T08:10:19Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965826351)
- `2026-03-18T08:11:53Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965835076)
- `2026-03-18T08:14:10Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965846593)
- `2026-03-18T08:17:09Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965863708)
- `2026-03-18T08:18:20Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965871452)
- `2026-03-18T08:19:19Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965877713)
- `2026-03-18T08:22:28Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3965896331)
- `2026-03-18T09:35:29Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3966381254)
- `2026-03-18T09:37:06Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3966390603)
- `2026-03-18T09:37:09Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3966390950)
- ... 29 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 40 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 11 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_indexer_topk.py`: 7 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`: 2 inline comment(s)
- `tensorrt_llm/llmapi/llm_args.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/block_scan.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_varlen_util.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-16T05:41:06Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, blackwell, block, compile, cute, hang, kernel, pipeline; excerpt: "Actionable comments posted: 9 🧹 Nitpick comments (7) tensorrt llm/ torch/cute dsl kernels/blackwell/top k/filtered top k decode varlen.py (5) 244-244: Avoid shadowing Python builtin ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#pullrequestreview-3951558138)
- `2026-03-16T05:41:01Z` `issue` by `coderabbitai`; signals: attention, benchmark, blackwell, block, compile, cute, dtype, hang; excerpt: "📝 Walkthrough Walkthrough Introduces CuTE DSL-based Top-K decode kernels for Blackwell GPUs with distributed multi-CTA support. Adds configuration flag to enable CuTE DSL top-k ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#issuecomment-4065180643)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/block_scan.py`:79; signals: blackwell, block, cute, kernel, tensorrt, tile, warp; excerpt: "⚠️ Potential issue 🟠 Major Validate the supported shape contract up front. This helper only works when min(num bins, num threads per block) // ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273045)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:654; signals: benchmark, blackwell, cute, cutlass, dtype, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Variable torch dtype shadows the imported function. Line 651 assigns torch dtype = input values.dtype, but torch dtype is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273047)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2822; signals: cache, compile, cuda, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Scope the CuTE DSL caches by CUDA device. get num sms() memoizes the first GPU's SM count, and none ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273039)
- `2026-03-18T09:46:34Z` `inline` by `limin2021` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2831; signals: cache, cuda, cute, kernel, memory, tensorrt; excerpt: "The top-k buffers are only used within each kernel invocation and fully overwritten each call — there's no cross-module sharing opportunity. The current per-Runner ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2952164470)
- `2026-03-18T08:06:45Z` `inline` by `yuxianq` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2831; signals: cute, deepgemm, gemm, memory, moe, tensorrt; excerpt: "Canwe reuse get memory buffers in like DeepGemmFusedMoE in" (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2951602512)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:914; signals: attention, compile, cuda, cute, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Warmup coverage is incomplete for non-default execution paths. tensorrt llm/ torch/custom ops/cute dsl custom ops.py::warmup cute dsl indexer topk() ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273036)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:3010; signals: cache, cute, hang, race, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Don't return shared cached storage from the value-returning APIs. When output indices/output values is omitted, these paths hand back ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273040)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:3925; signals: cute, dtype, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Validate output indices and the seq lens contract before dispatch. This public op currently trusts the caller. A wrong ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273044)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:1387; signals: blackwell, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor CLI argument --use cold l2 has ineffective configuration. Using action="store true" with default=True means the flag has no effect—the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273054)
- `2026-03-16T05:41:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_varlen_util.py`:1117; signals: blackwell, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Convert reference indices back to row-relative offsets. torch.topk returns absolute column indices, but this helper masks them as if ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12236#discussion_r2938273055)
