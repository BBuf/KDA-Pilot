# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2581](https://github.com/flashinfer-ai/flashinfer/pull/2581)
- Source page: `sources/prs/flashinfer/PR-2581.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2581`
- Generated at: `2026-05-20T15:25:06.815497+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-18T09:05:05Z`
- Merged: `2026-03-07T07:42:52Z`

## Discussion Counts

- Issue comments: 26
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 10
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: IwakuraRein, aleozlx, coderabbitai, siddharth9820, sidsingh-nvidia, yzh119, zianglih
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-18T09:16:14Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for mxfp8 x mxfp8 quantization in the cutlass fused moe kernel. ... (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3818667165)
- `2026-02-22T06:23:56Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (2) tests/moe/test trtllm cutlass fused moe.py (1) 1389-1392: GPU architecture skip ... (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3836829602)
- `2026-02-24T07:21:51Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 ♻️ Duplicate comments (2) csrc/fused moe/cutlass backend/cutlass fused moe kernels.cuh (1) 3595-3602: ⚠️ Potential ... (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3845674736)
- `2026-02-27T21:48:46Z` `APPROVED` by `aleozlx` - lgtm (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3869232453)
- `2026-03-03T19:14:46Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3884564992)
- `2026-03-03T22:40:38Z` `COMMENTED` by `coderabbitai` - ♻️ Duplicate comments (1) tests/moe/test trtllm cutlass fused moe.py (1) 1389-1392: ⚠️ Potential issue 🟠 Major Use flashinfer.utils ... (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3885450352)
- `2026-03-06T20:41:09Z` `COMMENTED` by `sidsingh-nvidia` (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3903366871)
- `2026-03-06T23:06:50Z` `COMMENTED` by `zianglih` (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3906511211)
- `2026-03-07T01:13:18Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3906850674)
- `2026-03-07T03:45:14Z` `COMMENTED` by `siddharth9820` (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3907230455)

## Inline Comment Hotspots

- `csrc/fused_moe/cutlass_backend/flashinfer_cutlass_fused_moe_binding.cu`: 4 inline comment(s)
- `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`: 3 inline comment(s)
- `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch_tma_ws.h`: 2 inline comment(s)
- `tests/moe/test_trtllm_cutlass_fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-22T06:23:56Z` `review` `COMMENTED` by `coderabbitai`; signals: block, cuda, cutlass, flashinfer, fp4, fp8, moe, nvfp4; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (2) tests/moe/test trtllm cutlass fused moe.py (1) 1389-1392: GPU architecture skip should use flashinfer.utils functions per coding ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3836829602)
- `2026-02-24T07:21:51Z` `review` `COMMENTED` by `coderabbitai`; signals: block, cuda, cutlass, flashinfer, fp4, fp8, gemm, hang; excerpt: "Actionable comments posted: 1 ♻️ Duplicate comments (2) csrc/fused moe/cutlass backend/cutlass fused moe kernels.cuh (1) 3595-3602: ⚠️ Potential issue 🟠 Major Require FC2 MXFP8 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3845674736)
- `2026-03-03T22:40:38Z` `review` `COMMENTED` by `coderabbitai`; signals: block, cuda, cutlass, flashinfer, fp4, gemm, hang, kernel; excerpt: "♻️ Duplicate comments (1) tests/moe/test trtllm cutlass fused moe.py (1) 1389-1392: ⚠️ Potential issue 🟠 Major Use flashinfer.utils helpers for architecture skip gating (Line ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3885450352)
- `2026-03-07T01:13:18Z` `review` `COMMENTED` by `coderabbitai`; signals: cutlass, epilogue, fp8, gemm, hang, kernel, moe, sm100; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#pullrequestreview-3906850674)
- `2026-03-07T01:13:17Z` `inline` by `coderabbitai` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch_tma_ws.h`:504; signals: benchmark, cutlass, gemm, kernel, moe, sm120, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major Throw on invalid SM120 specialisations instead of silently falling through. If isValidSM120MOESpecialisation () is false, this branch currently exits ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#discussion_r2898597482)
- `2026-02-22T06:17:25Z` `issue` by `coderabbitai`; signals: block, cutlass, flashinfer, fp4, fp8, gemm, hang, kernel; excerpt: "📝 Walkthrough Walkthrough Adds MXFPX/MXFP8 activation-scaling and block-scaling support across the Cutlass MoE backend: new template parameter IsMXFPX, a use mxfp8 act scaling flag, ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#issuecomment-3940267485)
- `2026-02-22T06:23:55Z` `inline` by `coderabbitai` `tests/moe/test_trtllm_cutlass_fused_moe.py`:1462; signals: cuda, cute, cutlass, flashinfer, fp8, moe, sm90; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 9685 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#discussion_r2837208588)
- `2026-02-22T06:23:55Z` `inline` by `coderabbitai` `csrc/fused_moe/cutlass_backend/cutlass_fused_moe_kernels.cuh`:3586; signals: benchmark, block, cutlass, fp8, kernel, moe; excerpt: "⚠️ Potential issue 🟠 Major Validate MXFP8 block‑scale inputs consistently. use mxfp8 weight block scales is enabled when only fc1.weight block scale is set ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#discussion_r2837208586)
- `2026-02-24T07:21:50Z` `inline` by `coderabbitai` `csrc/fused_moe/cutlass_backend/flashinfer_cutlass_fused_moe_binding.cu`:404; signals: cutlass, flashinfer, fp8, latency, moe; excerpt: "⚠️ Potential issue 🟠 Major Add MXFP8 input sf validation to the non‑min‑latency path. runMoeMinLatency enforces input sf when use mxfp8 act scaling=True, but ..." (https://github.com/flashinfer-ai/flashinfer/pull/2581#discussion_r2845018912)
- `2026-03-06T12:09:57Z` `inline` by `sidsingh-nvidia` `csrc/fused_moe/cutlass_backend/flashinfer_cutlass_fused_moe_binding.cu`:897; signals: bf16, cutlass, flashinfer, kernel, moe; excerpt: "Is this only supposed to work with gated activations? The bf16 variant of this kernel supports both gated and non-gated activations." (https://github.com/flashinfer-ai/flashinfer/pull/2581#discussion_r2895450592)
- `2026-03-05T05:17:16Z` `issue` by `zianglih`; signals: blackwell, cutlass, failing, hopper, moe; excerpt: "Hopper still failing. Can confirm test trtllm cutlass fused moe passes on Blackwell:" (https://github.com/flashinfer-ai/flashinfer/pull/2581#issuecomment-4002270921)
- `2026-03-06T23:06:50Z` `inline` by `zianglih` `csrc/fused_moe/cutlass_backend/flashinfer_cutlass_fused_moe_binding.cu`:897; signals: cutlass, flashinfer, kernel, moe; excerpt: "It works with gating, reference the unit test here: Also I have tried this kernel in SGLang and can run Qwen3-30B-A3B without problems." (https://github.com/flashinfer-ai/flashinfer/pull/2581#discussion_r2898303788)
