# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12354](https://github.com/NVIDIA/TensorRT-LLM/pull/12354)
- Source page: `sources/prs/tensorrt-llm/PR-12354.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12354`
- Generated at: `2026-05-20T15:18:08.004982+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-19T13:15:48Z`
- Merged: `2026-03-23T09:03:23Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 13 (approved=2, commented=11)
- Inline review comments: 12
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=6, outdated=3
- Human participants with discussion text: coderabbitai, hyukn, limin2021, tensorrt-cicd, yiakwy-xpu-ml-framework-team, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2026-03-19T13:28:50Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (1) tensorrt llm/ torch/cute dsl kernels/blackwell/top k/single pass multi cta radix ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3975132526)
- `2026-03-20T02:14:58Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3978961868)
- `2026-03-20T02:16:49Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3978967075)
- `2026-03-20T02:32:24Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3979013163)
- `2026-03-20T02:38:08Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3979027758)
- `2026-03-20T05:46:31Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3979579920)
- `2026-03-20T05:46:37Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3979580098)
- `2026-03-20T05:46:43Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3979580306)
- `2026-03-20T05:46:48Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3979580463)
- `2026-03-23T06:21:51Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3989591712)
- `2026-03-23T08:57:17Z` `APPROVED` by `hyukn` - LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3990222283)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`: 9 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-19T13:28:50Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, blackwell, cuda, cute, hang, kernel, moe, tensorrt; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (1) tensorrt llm/ torch/cute dsl kernels/blackwell/top k/single pass multi cta radix topk cluster.py (1) 28-30: Consider whether ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#pullrequestreview-3975132526)
- `2026-03-19T13:28:46Z` `issue` by `coderabbitai`; signals: benchmark, blackwell, cuda, cute, dtype, hang, kernel, moe; excerpt: "📝 Walkthrough Walkthrough Added a cluster-accelerated single-pass multi-CTA top-k kernel with DSMEM-based histogram merging and cluster synchronization. Refactored existing runner to use class attributes, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#issuecomment-4090138491)
- `2026-03-19T13:28:49Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`:74; signals: blackwell, cache, cuda, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Key the cluster-size cache by CUDA device. query max cluster size() is device-specific, but lru cache(maxsize=1) memoizes the first ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2960061605)
- `2026-03-20T02:14:58Z` `inline` by `yuxianq` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`:187; signals: blackwell, cute, kernel, tensorrt; excerpt: "Can we move build local histogram to single pass multi cta radix topk.py and reuse it in build and merge histogram?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2963623312)
- `2026-03-20T02:32:24Z` `inline` by `yuxianq` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`:267; signals: blackwell, cute, kernel, tensorrt; excerpt: "The pass 0 (Reuse local histogram for counters), pass 1 and pass 2 of collect output cluster and collect output are identical, should we ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2963664856)
- `2026-03-20T02:16:50Z` `inline` by `yuxianq` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`:257; signals: blackwell, cute, kernel, tensorrt; excerpt: "Can we share the prefix mask part between radix round cluster/ radix round/ radix round single cta?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2963626830)
- `2026-03-20T05:46:36Z` `inline` by `limin2021` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`:267; signals: blackwell, cute, kernel, tensorrt; excerpt: "done." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2964092254)
- `2026-03-20T05:46:43Z` `inline` by `limin2021` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`:257; signals: blackwell, cute, kernel, tensorrt; excerpt: "done." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2964092460)
- `2026-03-20T05:46:48Z` `inline` by `limin2021` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/single_pass_multi_cta_radix_topk_cluster.py`:187; signals: blackwell, cute, kernel, tensorrt; excerpt: "done." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2964092613)
- `2026-03-19T13:28:49Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:3987; signals: cute, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Handle the cluster runner fallback before returning. CuteDSLTopKDecodeSinglePassMultiCTAClusterRunner.forward() is explicitly allowed to return (None, None) for unsupported shapes, but ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2960061596)
- `2026-03-20T02:38:08Z` `inline` by `yuxianq` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:3973; signals: cute, tensorrt; excerpt: "Should we fallback to CuteDSLTopKDecodeSinglePassMultiCTARunner when its result[0] is None?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2963675365)
- `2026-03-20T05:46:31Z` `inline` by `limin2021` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:3973; signals: cute, tensorrt; excerpt: "done." (https://github.com/NVIDIA/TensorRT-LLM/pull/12354#discussion_r2964092091)
