# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11900](https://github.com/NVIDIA/TensorRT-LLM/pull/11900)
- Source page: `sources/prs/tensorrt-llm/PR-11900.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11900`
- Generated at: `2026-05-20T15:17:56.790269+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-04T08:09:21Z`
- Merged: `2026-03-09T05:36:03Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 19 (approved=2, commented=17)
- Inline review comments: 33
- Review threads observed: 20
- Resolved/outdated thread markers: resolved=20, outdated=10
- Human participants with discussion text: coderabbitai, hyukn, limin2021, longlee0622, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T08:19:09Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 8 🧹 Nitpick comments (6) tensorrt llm/ torch/custom ops/cute dsl custom ops.py (1) 3013-3016: Clean ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3887855665)
- `2026-03-04T08:28:01Z` `COMMENTED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3887895967)
- `2026-03-04T08:28:33Z` `COMMENTED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3887898270)
- `2026-03-04T08:55:38Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3888020651)
- `2026-03-04T08:58:07Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3888032837)
- `2026-03-06T04:14:15Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3901182315)
- `2026-03-06T06:53:21Z` `APPROVED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3901769007)
- `2026-03-06T10:53:49Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903004354)
- `2026-03-06T12:37:42Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903370840)
- `2026-03-06T13:38:26Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903769595)
- `2026-03-06T13:39:13Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903772988)
- `2026-03-06T13:45:51Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903802581)
- `2026-03-06T13:48:20Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903813915)
- `2026-03-06T14:07:42Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903914385)
- `2026-03-06T14:08:01Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903916453)
- `2026-03-06T14:08:06Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903917029)
- `2026-03-06T14:08:11Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903917492)
- `2026-03-06T14:08:22Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3903918480)
- `2026-03-09T02:37:06Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3912552431)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 17 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`: 11 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/__init__.py`: 2 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_indexer_topk.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_varlen_util.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-04T08:19:09Z` `review` `COMMENTED` by `coderabbitai`; signals: blackwell, block, cache, cute, dtype, hang, kernel, nan; excerpt: "Actionable comments posted: 8 🧹 Nitpick comments (6) tensorrt llm/ torch/custom ops/cute dsl custom ops.py (1) 3013-3016: Clean up the fake registration stub. Line ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#pullrequestreview-3887855665)
- `2026-03-04T08:19:03Z` `issue` by `coderabbitai`; signals: benchmark, blackwell, block, cuda, cute, dtype, hang, kernel; excerpt: "📝 Walkthrough Walkthrough This PR introduces CuTE DSL Top-K decode functionality for Blackwell GPUs, including a custom CUDA operator, kernel implementations for block prefix ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#issuecomment-3995985804)
- `2026-03-04T08:19:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:13; signals: benchmark, blackwell, cute, hang, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Update the copyright year to reflect this 2026 change. This file is introduced in a PR created on March ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882427342)
- `2026-03-04T08:19:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_varlen_util.py`:1091; signals: benchmark, blackwell, cuda, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major create random logits currently ignores its seed for CUDA RNG. Line 1090 hardcodes torch.cuda.manual seed(1111), so CUDA-generated logits are ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882427357)
- `2026-03-06T13:38:26Z` `inline` by `limin2021` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:1330; signals: accuracy, blackwell, cute, hang, kernel, tensorrt; excerpt: "I will clean up the test in the main in the kernel file in the next MR. The kernel file is copy from dsl ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2895820889)
- `2026-03-04T08:19:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2798; signals: benchmark, block, cute, cutlass, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Remove duplicate cutlass/cute imports in this scope. Line 2797 and Line 2798 re-import names already imported in the same ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882427328)
- `2026-03-04T08:19:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:33; signals: blackwell, cute, kernel, tensorrt; excerpt: "🛠️ Refactor suggestion 🟠 Major Use module-level imports instead of importing symbols directly. The direct symbol imports here violate the repo import rule and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882427348)
- `2026-03-04T08:19:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:526; signals: blackwell, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical load balance=True path passes a missing global counter to dynamic scheduling. When Line 526 enables persistent scheduling, the kernel ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882427349)
- `2026-03-04T08:19:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:588; signals: blackwell, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Guard unsupported load balance in the multi-CTA wrapper. Line 586 forces enable multi cta=True, but Lines 662/706 still forward ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882427351)
- `2026-03-04T08:19:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:975; signals: blackwell, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 154 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882427355)
- `2026-03-04T08:28:02Z` `inline` by `longlee0622` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:321; signals: cute, hang, perf, tensorrt; excerpt: "@limin2021 thanks for the PR. Any measured silicon data to show the perf gain? We do have a few DS R1/3.2 perf tests in ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2882463736)
- `2026-03-06T12:10:46Z` `inline` by `hyukn` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`:1330; signals: blackwell, cute, kernel, tensorrt; excerpt: "I highly recommend using a test to cover this part. Because the main code in the core lib might be confusing. We can use ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11900#discussion_r2895454067)
