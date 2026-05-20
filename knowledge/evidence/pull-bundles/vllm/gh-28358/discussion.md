# PR Discussion Digest

- Source PR: [vllm-project/vllm#28358](https://github.com/vllm-project/vllm/pull/28358)
- Source page: `sources/prs/vllm/PR-28358.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28358`
- Generated at: `2026-05-20T15:38:27.951380+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-09T04:59:51Z`
- Merged: `2025-11-13T18:16:55Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 26 (approved=2, commented=24)
- Inline review comments: 28
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=7, outdated=2
- Human participants with discussion text: chatgpt-codex-connector, elvircrn, heheda12345, mergify, mgoin, varun-sundar-rabindranath
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-09T05:02:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant performance optimization by fusing the scale packing for DeepGEMM directly ... (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3439405621)
- `2025-11-09T05:03:15Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3439405758)
- `2025-11-09T05:04:07Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3439405943)
- `2025-11-09T05:05:43Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3439406277)
- `2025-11-09T05:09:08Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3439407015)
- `2025-11-09T05:12:21Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3439407691)
- `2025-11-09T19:04:58Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3440259954)
- `2025-11-10T08:47:33Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3441553819)
- `2025-11-10T09:35:22Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3441946025)
- `2025-11-10T09:39:09Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3441972490)
- `2025-11-10T09:56:05Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3442080645)
- `2025-11-10T10:01:15Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3442116918)
- `2025-11-10T10:02:05Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3442123304)
- `2025-11-10T14:08:51Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443453349)
- `2025-11-10T14:11:05Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443463410)
- `2025-11-10T14:15:15Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443481645)
- `2025-11-10T14:24:24Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443523183)
- `2025-11-10T14:26:54Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443534870)
- `2025-11-10T14:37:49Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443590335)
- `2025-11-10T14:38:43Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443596187)
- `2025-11-10T14:45:13Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3443634511)
- `2025-11-10T18:03:56Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3444512261)
- `2025-11-13T04:28:01Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3457278222)
- `2025-11-13T04:28:28Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/28358#pullrequestreview-3457279815)
- ... 2 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `csrc/quantization/activation_kernels.cu`: 23 inline comment(s)
- `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`: 3 inline comment(s)
- `tests/kernels/moe/test_silu_mul_fp8_quant_deep_gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-09T05:03:15Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:358; signals: blackwell, deepgemm, dtype, fp8, gemm, hang, kernel, moe; excerpt: ", which only looks at the device capability. The previous logic consulted is deep gemm e8m0 used() so that scales were only packed to ..." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2507607727)
- `2025-11-10T14:24:23Z` `inline` by `varun-sundar-rabindranath` `csrc/quantization/activation_kernels.cu`:551; signals: hang, kernel, perf, performance, warp; excerpt: "If you have the bandwidth for this, you could perhaps comment out the global scale writes out to ballpark their impact on the overall ..." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2510769043)
- `2025-11-09T05:09:08Z` `inline` by `varun-sundar-rabindranath` `tests/kernels/moe/test_silu_mul_fp8_quant_deep_gemm.py`:279; signals: fp8, gemm, kernel, memory, moe; excerpt: "this is fine as the comparison on the contents when indexed and not raw memory contents." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2507609157)
- `2025-11-09T05:12:21Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:358; signals: deepgemm, fp8, gemm, moe; excerpt: "the scale format can be different for different calls to deepgemm - they all dont have to sync. fp8 m grouped gemm nt masked ..." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2507609945)
- `2025-11-10T09:55:59Z` `inline` by `elvircrn` `csrc/quantization/activation_kernels.cu`:551; signals: kernel, perf, performance, warp; excerpt: "If you have the bandwidth for this, you could perhaps comment out the global scale writes out to ballpark their impact on the overall ..." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2509655164)
- `2025-11-10T08:31:57Z` `inline` by `elvircrn` `csrc/quantization/activation_kernels.cu`:640; signals: benchmark, block, kernel; excerpt: "What we want here is to have sms instead of 132. Benchmarking, I found that we don't actually want to directly use the number ..." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2509279521)
- `2025-11-10T08:47:30Z` `inline` by `elvircrn` `csrc/quantization/activation_kernels.cu`:640; signals: blackwell, kernel, perf; excerpt: "If you have free time on your hands you can modify this, with possible perf improvements on Blackwell otherwise I'll get to it." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2509345551)
- `2025-11-10T09:35:16Z` `inline` by `elvircrn` `csrc/quantization/activation_kernels.cu`:731; signals: kernel, perf; excerpt: "My preference here would be that, because these values are hardcoded, that they be converted to constexpr in the kernel. This won't break anything, ..." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2509556378)
- `2025-11-10T09:39:04Z` `inline` by `elvircrn` `csrc/quantization/activation_kernels.cu`:731; signals: kernel, layout; excerpt: "The strides only make sense when they are passed from torch::Tensor when the kernel is not allowed to make layout assumptions." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2509577662)
- `2025-11-10T14:38:43Z` `inline` by `varun-sundar-rabindranath` `csrc/quantization/activation_kernels.cu`:731; signals: kernel, perf; excerpt: "My preference here would be that, because these values are hardcoded, that they be converted to constexpr in the kernel. This won't break anything, ..." (https://github.com/vllm-project/vllm/pull/28358#discussion_r2510822406)
- `2025-11-13T04:28:01Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:358; signals: gemm, moe; excerpt: "is deep gemm e8m0 used honored ! Thanks Bot !" (https://github.com/vllm-project/vllm/pull/28358#discussion_r2521363711)
- `2025-11-09T05:00:53Z` `issue` by `varun-sundar-rabindranath`; signals: hang, kernel; excerpt: "cc @elvircrn for changes to the kernel. PTAL ! Thanks 🙌" (https://github.com/vllm-project/vllm/pull/28358#issuecomment-3507530648)
