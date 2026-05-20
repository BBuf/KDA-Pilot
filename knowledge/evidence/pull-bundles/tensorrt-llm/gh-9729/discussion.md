# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9729](https://github.com/NVIDIA/TensorRT-LLM/pull/9729)
- Source page: `sources/prs/tensorrt-llm/PR-9729.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9729`
- Generated at: `2026-05-20T15:19:26.757433+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-05T08:12:43Z`
- Merged: `2026-01-13T13:11:13Z`

## Discussion Counts

- Issue comments: 172
- Review submissions: 49 (approved=5, commented=44)
- Inline review comments: 63
- Review threads observed: 26
- Resolved/outdated thread markers: resolved=26, outdated=17
- Human participants with discussion text: 2ez4bz, benzh-2025, byshiue, coderabbitai, hyukn, juney-nvidia, liji-nv, litaotju, tensorrt-cicd, yihwang-nv, yuxianq, zhang2020
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-05T08:16:20Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (5) tests/unittest/ torch/multi gpu/test linear.py (3) 346-357: Consider reusing the existing ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3543566394)
- `2025-12-11T04:12:48Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3565533356)
- `2025-12-11T04:13:07Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3565534593)
- `2025-12-11T10:09:14Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3566680571)
- `2025-12-11T10:11:01Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3566688247)
- `2025-12-11T10:11:57Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3566692677)
- `2025-12-11T10:12:49Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3566697206)
- `2025-12-11T10:31:22Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3566768288)
- `2025-12-24T02:47:37Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609754936)
- `2025-12-24T04:10:05Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609862956)
- `2025-12-24T04:13:37Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609867009)
- `2025-12-24T04:14:06Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609867469)
- `2025-12-24T04:14:59Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609868519)
- `2025-12-24T04:15:48Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609869296)
- `2025-12-24T04:19:10Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609874796)
- `2025-12-24T04:19:39Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609875597)
- `2025-12-24T04:23:44Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609880333)
- `2025-12-24T05:01:45Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3609931789)
- `2026-01-12T06:28:51Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3649286081)
- `2026-01-12T06:31:46Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3649323587)
- `2026-01-12T06:32:15Z` `COMMENTED` by `benzh-2025` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3649324407)
- `2026-01-12T08:59:52Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3649721124)
- `2026-01-12T09:19:08Z` `COMMENTED` by `byshiue` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3649804280)
- `2026-01-12T09:21:11Z` `COMMENTED` by `byshiue` (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3649812982)
- ... 25 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/models/modeling_llama.py`: 22 inline comment(s)
- `tensorrt_llm/_torch/modules/linear.py`: 15 inline comment(s)
- `cpp/tensorrt_llm/thop/fusedGemmAllreduceOp.cpp`: 12 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`: 10 inline comment(s)
- `tests/unittest/_torch/multi_gpu/test_linear.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-12-05T08:16:20Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, block, cache, compile, correctness, dtype, fp4, gemm; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (5) tests/unittest/ torch/multi gpu/test linear.py (3) 346-357: Consider reusing the existing check accuracy utility. This function duplicates ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#pullrequestreview-3543566394)
- `2025-12-05T08:16:20Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/linear.py`:1421; signals: benchmark, fp4, fp8, mxfp4, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Remove duplicate method definition. The apply linear allreduce method is defined twice consecutively in W4A8MXFP4FP8LinearMethod. The second definition shadows ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2591794600)
- `2025-12-05T08:16:20Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/linear.py`:2133; signals: fp4, gemm, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Potential AttributeError if quant config is None. When use fused gemm allreduce=True is passed but quant config is None, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2591794609)
- `2026-01-12T09:27:43Z` `inline` by `benzh-2025` `tensorrt_llm/_torch/models/modeling_llama.py`:678; signals: accuracy, fp4, nvfp4, tensorrt; excerpt: "yes, this is verified by this: tests/integration/defs/accuracy/test llm api pytorch.py:test nvfp4 tp4" (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2681459980)
- `2026-01-12T10:14:02Z` `inline` by `litaotju` `cpp/tensorrt_llm/thop/fusedGemmAllreduceOp.cpp`:149; signals: gemm, hang, race, tensorrt; excerpt: "I think we should not make this log as info level, its soo verbose and not useful information to users. You added it for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2681616596)
- `2026-01-12T12:18:23Z` `inline` by `benzh-2025` `tensorrt_llm/_torch/modules/linear.py`:972; signals: fp4, kernel, tensorrt, tma; excerpt: "it accept stride inputs, only require stride satisfy tma requirements. In other side, this kernel only process fp4 input, fp4 is most generated internal, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2682041219)
- `2026-01-12T10:22:21Z` `inline` by `litaotju` `tensorrt_llm/_torch/models/modeling_llama.py`:678; signals: blackwell, kernel, tensorrt; excerpt: "This kernel only support Blackwell? so should we really enable it by default, what if other GPUs don't have it?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2681644377)
- `2026-01-12T12:27:52Z` `inline` by `benzh-2025` `tensorrt_llm/_torch/models/modeling_llama.py`:687; signals: blackwell, kernel, tensorrt; excerpt: "This kernel only support Blackwell? so should we really enable it by default, what if other GPUs don't have it? I have another check ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2682071114)
- `2025-12-24T04:14:59Z` `inline` by `benzh-2025` `tensorrt_llm/_torch/models/modeling_llama.py`:680; signals: fp4, nvfp4, tensorrt; excerpt: "it is because self.is nvfp4 is None." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2644748871)
- `2026-01-12T06:32:15Z` `inline` by `benzh-2025` `cpp/tensorrt_llm/thop/fusedGemmAllreduceOp.cpp`:2; signals: gemm, hang, tensorrt; excerpt: "Good point, let me change." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2681015719)
- `2026-01-12T12:20:03Z` `inline` by `benzh-2025` `cpp/tensorrt_llm/thop/fusedGemmAllreduceOp.cpp`:149; signals: gemm, hang, tensorrt; excerpt: "it used for notify whether gemm+allreduce enabled. Let me change." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2682046501)
- `2026-01-12T12:22:51Z` `inline` by `benzh-2025` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1925; signals: fp4, hang, tensorrt; excerpt: "yes, weight is also fp4. let me change." (https://github.com/NVIDIA/TensorRT-LLM/pull/9729#discussion_r2682055066)
