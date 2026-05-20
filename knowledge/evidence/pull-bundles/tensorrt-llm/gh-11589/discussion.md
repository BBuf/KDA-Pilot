# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11589](https://github.com/NVIDIA/TensorRT-LLM/pull/11589)
- Source page: `sources/prs/tensorrt-llm/PR-11589.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11589`
- Generated at: `2026-05-20T15:17:48.261174+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-19T23:00:55Z`
- Merged: `2026-04-27T15:46:41Z`

## Discussion Counts

- Issue comments: 155
- Review submissions: 64 (approved=7, commented=57)
- Inline review comments: 97
- Review threads observed: 46
- Resolved/outdated thread markers: resolved=46, outdated=32
- Human participants with discussion text: StanleySun639, Tabrizian, Wanli-Jiang, brb-nv, coderabbitai, hyukn, kaiyux, mikeiovine, nv-lschneider, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-19T23:14:49Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 [!NOTE] Due to the large number of review comments, Critical, Major severity comments were ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3829011623)
- `2026-02-28T03:35:14Z` `COMMENTED` by `Tabrizian` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3869969522)
- `2026-03-03T12:58:25Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3882295773)
- `2026-03-10T21:04:33Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925422909)
- `2026-03-10T21:48:01Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925626553)
- `2026-03-10T21:50:47Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925638489)
- `2026-03-10T21:54:43Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925654953)
- `2026-03-10T21:59:55Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925681371)
- `2026-03-10T22:00:45Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925685454)
- `2026-03-10T22:04:40Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925705664)
- `2026-03-10T22:08:17Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925726796)
- `2026-03-10T22:13:22Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925752104)
- `2026-03-10T23:19:21Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3925993101)
- `2026-03-10T23:23:30Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3926003859)
- `2026-03-10T23:29:18Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3926023506)
- `2026-03-10T23:31:38Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3926033082)
- `2026-03-10T23:31:39Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3926033162)
- `2026-03-10T23:31:41Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3926033292)
- `2026-03-10T23:31:42Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3926033345)
- `2026-03-10T23:31:43Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3926033424)
- `2026-04-06T18:05:41Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-4063614153)
- `2026-04-06T19:18:11Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-4064019509)
- `2026-04-06T19:18:47Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-4064022540)
- `2026-04-06T19:22:50Z` `COMMENTED` by `nv-lschneider` (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-4064042946)
- ... 40 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`: 14 inline comment(s)
- `tensorrt_llm/_torch/modules/linear_common.py`: 12 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 9 inline comment(s)
- `cpp/tensorrt_llm/thop/ncclWindowTensor.cpp`: 6 inline comment(s)
- `tensorrt_llm/_torch/modules/linear.py`: 6 inline comment(s)
- `cpp/tensorrt_llm/thop/cublasScaledMM.cpp`: 5 inline comment(s)
- `tensorrt_llm/_torch/modules/attention.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_deepseekv3.py`: 4 inline comment(s)
- `cpp/tensorrt_llm/thop/cublasScaledMM.h`: 3 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py`: 3 inline comment(s)
- `tests/microbenchmarks/all_reduce.py`: 3 inline comment(s)
- `tests/unittest/_torch/multi_gpu/test_linear.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-02-19T23:14:49Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, autotune, benchmark, cuda, fp4, fp8, gemm, hang; excerpt: "Actionable comments posted: 7 [!NOTE] Due to the large number of review comments, Critical, Major severity comments were prioritized as inline comments. [!CAUTION] Some ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-3829011623)
- `2026-04-06T18:05:41Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, autotune, benchmark, cache, cuda, cute, fp4, fp8; excerpt: "Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-4063614153)
- `2026-04-06T18:05:39Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:576; signals: bf16, cute, dtype, fp4, kernel, memory, overflow, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 34232 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#discussion_r3040885466)
- `2026-04-13T22:49:48Z` `issue` by `nv-lschneider`; signals: gemm, memory, moe, oom, perf, performance, race, register; excerpt: "This PR implements this in fused python operations (GEMM and MOE) to enable output directly in a custom buffer if NCCL SYMMETRIC is chosen. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#issuecomment-4240110601)
- `2026-04-14T00:16:27Z` `issue` by `brb-nv`; signals: gemm, memory, moe, oom, perf, performance, race, register; excerpt: "This PR implements this in fused python operations (GEMM and MOE) to enable output directly in a custom buffer if NCCL SYMMETRIC is chosen. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#issuecomment-4240428498)
- `2026-03-10T23:29:18Z` `inline` by `nv-lschneider` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:936; signals: blackwell, cute, fp4, gemm, hang, nvfp4, tensorrt; excerpt: "Good catch — this was an oversight. Updated CuteDSLNVFP4BlackwellRunner to use output buffer kind and group instead of the old to userbuffers: bool, with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#discussion_r2915041393)
- `2026-03-10T23:23:30Z` `inline` by `nv-lschneider` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1989; signals: gemm, perf, performance, register, regression, tensorrt; excerpt: "If the input is not in a registered (window) buffer, NCCL SYMMETRIC will copy it to a registered buffer before the AllReduce, which adds ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#discussion_r2915025386)
- `2026-04-06T18:05:39Z` `inline` by `coderabbitai` `tests/microbenchmarks/all_reduce.py`:267; signals: benchmark, cute, perf, performance, register, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 100 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#discussion_r3040885484)
- `2026-04-09T07:50:59Z` `review` `COMMENTED` by `hyukn`; signals: benchmark, gemm, hang, perf, pipeline; excerpt: "Thanks for the great effort. This is truly a big change and has large scope of impact. My major concern is the complexity of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#pullrequestreview-4080609661)
- `2026-03-10T22:13:22Z` `inline` by `nv-lschneider` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:427; signals: compile, hang, kernel, nan, tensorrt; excerpt: "I changed BufferKind be a nanobind enum (bound in cpp/tensorrt llm/nanobind/thop/bindings.cpp). So it changed a bit. My understanding is, that the int conversion is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#discussion_r2914779041)
- `2026-04-06T20:51:32Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:576; signals: bf16, cute, dtype, hang, tensorrt; excerpt: "@nv-lschneider, thanks for the update. I can see the fix in the current file — a zero-element scalar tensor with the correct self.output dtype ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#discussion_r3041619770)
- `2026-04-14T19:19:06Z` `inline` by `nv-lschneider` `tensorrt_llm/_torch/modules/attention.py`:252; signals: attention, hang, memory, register, tensorrt; excerpt: "The NCCL name for this is registered symmetric windows. They are backed by NCCL windows. So I don't see how we can eliminate window ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11589#discussion_r3081849586)
