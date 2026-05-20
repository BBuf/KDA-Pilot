# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12385](https://github.com/NVIDIA/TensorRT-LLM/pull/12385)
- Source page: `sources/prs/tensorrt-llm/PR-12385.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12385`
- Generated at: `2026-05-20T15:18:08.009175+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-20T05:12:29Z`
- Merged: `2026-04-03T06:03:28Z`

## Discussion Counts

- Issue comments: 91
- Review submissions: 30 (approved=1, commented=29)
- Inline review comments: 41
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=15, outdated=6
- Human participants with discussion text: HuiGao-NV, coderabbitai, juney-nvidia, kaiyux, lfr-0531, longcheng-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-20T05:45:59Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 9 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3979578206)
- `2026-03-21T07:34:09Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765041)
- `2026-03-21T07:34:14Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765078)
- `2026-03-21T07:34:18Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765113)
- `2026-03-21T07:34:22Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765140)
- `2026-03-21T07:34:28Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765205)
- `2026-03-21T07:34:35Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765268)
- `2026-03-21T07:34:42Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765337)
- `2026-03-21T07:34:48Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765407)
- `2026-03-21T07:34:51Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765436)
- `2026-03-21T07:34:52Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765444)
- `2026-03-21T07:34:55Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765469)
- `2026-03-21T07:35:09Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765630)
- `2026-03-21T07:35:09Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765640)
- `2026-03-21T07:35:15Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765717)
- `2026-03-21T07:35:16Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765729)
- `2026-03-21T07:35:17Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765732)
- `2026-03-21T07:35:35Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985765928)
- `2026-03-21T07:36:22Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3985766373)
- `2026-03-24T09:27:18Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3997486503)
- `2026-03-24T13:49:58Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3999375369)
- `2026-03-24T13:50:06Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3999376825)
- `2026-03-24T13:50:30Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3999380301)
- `2026-03-24T13:59:19Z` `COMMENTED` by `longcheng-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3999451373)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 9 inline comment(s)
- `cpp/tensorrt_llm/kernels/heuristic_topk.cuh`: 6 inline comment(s)
- `cpp/tensorrt_llm/thop/IndexerTopKOp.cpp`: 6 inline comment(s)
- `examples/longbench/eval_longbench_v1.py`: 6 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_indexer_topk.py`: 6 inline comment(s)
- `tensorrt_llm/llmapi/llm_args.py`: 5 inline comment(s)
- `cpp/tensorrt_llm/kernels/heuristicTopKDecode.cu`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-21T07:35:35Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:531; signals: attention, correctness, kernel, memory, perf, performance, race, tensorrt; excerpt: "@longcheng-nv, thanks for the update. The .zero () call at dsa.py:544 addresses the primary concern — uninitialized memory producing arbitrary hint indices is now ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r2969275713)
- `2026-04-01T09:04:00Z` `inline` by `longcheng-nv` `examples/longbench/eval_longbench_v1.py`:155; signals: accuracy, attention, blackwell, block, correctness, fp8, kernel, sm100; excerpt: "Good call. The current CI coverage for this feature is: Unit tests (kernel correctness, already in CI): - tests/unittest/ torch/thop/parallel/test indexer topk.py — tests ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r3020772153)
- `2026-03-20T05:45:05Z` `issue` by `coderabbitai`; signals: alignment, attention, cache, correctness, cuda, dtype, hang, kernel; excerpt: "📝 Walkthrough Walkthrough This PR introduces a heuristic top-K decoding mechanism that accelerates top-K selection by reusing previous step's top-K indices as hints. It ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#issuecomment-4095763031)
- `2026-03-29T14:09:57Z` `issue` by `longcheng-nv`; signals: accuracy, b200, benchmark, blackwell, dtype, failing, hang, pipeline; excerpt: "CI Status Update The latest CI runs (pipelines 31620 and 31628) both show 1 failure in an unrelated test: - DGX B200-8 GPUs-PyTorch-1.accuracy.test disaggregated ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#issuecomment-4150235003)
- `2026-03-24T13:50:30Z` `inline` by `longcheng-nv` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1739; signals: attention, b200, cuda, kernel, memory, race, tensorrt; excerpt: "Good idea in principle, but after adopting Comment 2 (passing prev topk directly as pre idx), fusing the write-back creates a data race for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r2981744348)
- `2026-03-20T05:45:57Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/heuristicTopKDecode.cu`:98; signals: cache, cuda, kernel, memory, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Make the shared-memory opt-in cache device-aware. cudaFuncSetAttribute(...MaxDynamicSharedMemorySize...) is device-scoped, but configured is a single process-wide flag. In multi-GPU runs, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r2964090784)
- `2026-03-21T07:36:22Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/heuristic_topk.cuh`:774; signals: compile, cute, hang, kernel, tensorrt; excerpt: "🧩 Analysis chain Let me verify the call chain to confirm. --- 🏁 Script executed: Length of output: 254775 --- @longcheng-nv You’re right — ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r2969276254)
- `2026-03-24T13:49:58Z` `inline` by `longcheng-nv` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:608; signals: attention, cache, cuda, hang, tensorrt; excerpt: "Good catch. Removed the duplicate allocation from create expanded buffers(). The initial allocation in post init (line 547) is now the single source of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r2981740126)
- `2026-03-20T05:45:59Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 9 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ Run configuration Configuration used : Path: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#pullrequestreview-3979578206)
- `2026-03-25T09:07:14Z` `issue` by `longcheng-nv`; signals: attention, blackwell, h100, hang, kernel; excerpt: "Updates in latest push Commit 67fad31 — Fix CI failure on H100: - Added get sm version() = 100 guard to enable heuristic topk ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#issuecomment-4124907836)
- `2026-03-20T05:45:57Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/IndexerTopKOp.cpp`:87; signals: cuda, kernel, memory, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Require pre idx to be on the same CUDA device as logits. pre idx is only checked for is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r2964090789)
- `2026-03-21T07:34:48Z` `inline` by `longcheng-nv` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:531; signals: attention, kernel, race, tensorrt; excerpt: "Fixed in commit 0648f623. heuristic prev topk is zero-initialized via .zero () at allocation time (dsa.py:544). The first decode step reads zeros (no valid ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12385#discussion_r2969274994)
