# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9618](https://github.com/NVIDIA/TensorRT-LLM/pull/9618)
- Source page: `sources/prs/tensorrt-llm/PR-9618.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9618`
- Generated at: `2026-05-20T15:19:24.881473+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-02T08:07:17Z`
- Merged: `2025-12-11T08:21:33Z`

## Discussion Counts

- Issue comments: 26
- Review submissions: 17 (approved=4, commented=13)
- Inline review comments: 20
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=6
- Human participants with discussion text: QiJune, coderabbitai, hyukn, kaiyux, syuoni, tensorrt-cicd, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-05T12:23:23Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (5) tensorrt llm/ torch/utils.py (1) 294-300: Unsizzled FP4 scale shape helper ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3544533290)
- `2025-12-08T02:31:56Z` `APPROVED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3549898211)
- `2025-12-08T03:25:26Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3549978330)
- `2025-12-08T06:30:30Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550263875)
- `2025-12-08T06:35:07Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550332379)
- `2025-12-08T07:34:18Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550417679)
- `2025-12-08T08:58:41Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550882391)
- `2025-12-08T08:59:47Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550889408)
- `2025-12-08T08:59:56Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550890485)
- `2025-12-08T09:00:03Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550891228)
- `2025-12-08T09:00:17Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550892469)
- `2025-12-08T09:02:31Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550904502)
- `2025-12-08T09:17:10Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3550970092)
- `2025-12-08T10:20:43Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3551258591)
- `2025-12-08T10:21:33Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3551263145)
- `2025-12-08T10:38:23Z` `APPROVED` by `QiJune` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3551347892)
- `2025-12-09T02:59:20Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3555104583)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 12 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`: 8 inline comment(s)

## High-Signal Discussion

- `2025-12-05T12:23:23Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, blackwell, block, cute, cutlass, fp4, gemm; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (5) tensorrt llm/ torch/utils.py (1) 294-300: Unsizzled FP4 scale shape helper looks correct; minor lint nit fp4 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#pullrequestreview-3544533290)
- `2025-12-05T12:23:20Z` `issue` by `coderabbitai`; signals: blackwell, block, correctness, cute, fp4, gemm, hang, kernel; excerpt: "📝 Walkthrough Walkthrough The changes introduce a gather-based fusion path for grouped GEMM operations in NVFP4, replacing an explicit two-step permutation flow with a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#issuecomment-3616681407)
- `2025-12-08T07:13:31Z` `inline` by `syuoni` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:44; signals: cute, gemm, tensorrt; excerpt: "Gather FC1 has very different inputs than other grouped GEMM operators. Could we use a dedicated helper class (maybe a subclass of GroupedGemmInputsHelper) for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597300169)
- `2025-12-08T10:21:33Z` `inline` by `zongfeijing` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1910; signals: cute, gemm, tensorrt; excerpt: "It can be done in a subsequent PR; for now, keep it consistent with other implementations of group gemm." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597984044)
- `2025-12-08T02:29:08Z` `inline` by `kaiyux` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:81; signals: cute, hang, tensorrt; excerpt: "Maybe add assertion here to avoid future breaking changes?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2596857321)
- `2025-12-08T06:17:08Z` `inline` by `hyukn` `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`:907; signals: accuracy, cute, moe; excerpt: "Can we use check accuracy method from for simplicity?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597177389)
- `2025-12-08T06:35:07Z` `inline` by `zongfeijing` `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`:724; signals: cute, kernel, moe; excerpt: "No, this is a kernel-level UT." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597211945)
- `2025-12-08T07:24:20Z` `inline` by `syuoni` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2101; signals: cute, moe, tensorrt; excerpt: "This FusedMoEInputsHelper class has been moved to the beginning of this file." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597325122)
- `2025-12-08T06:30:11Z` `inline` by `hyukn` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1910; signals: cute, tensorrt; excerpt: "Using tvm ffi might be a better way to handle the torch tensor and cute tensor, see Also cc @limin2021 for advice here." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597202747)
- `2025-12-08T03:25:25Z` `inline` by `zongfeijing` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:81; signals: cute, tensorrt; excerpt: "Okay, I add an assertion as a safeguard." (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2596919853)
- `2025-12-08T06:04:26Z` `inline` by `hyukn` `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`:724; signals: cute, moe; excerpt: "Do we need multi gpu for this test?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597155384)
- `2025-12-08T07:07:07Z` `inline` by `syuoni` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:179; signals: cute, tensorrt; excerpt: "Please unify the variable naming: token id mapping - permuted idx to expanded idx" (https://github.com/NVIDIA/TensorRT-LLM/pull/9618#discussion_r2597284877)
