# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2864](https://github.com/flashinfer-ai/flashinfer/pull/2864)
- Source page: `sources/prs/flashinfer/PR-2864.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2864`
- Generated at: `2026-05-20T15:25:46.363814+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T17:24:32Z`
- Merged: `2026-04-13T19:34:13Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: aleozlx, amirkl94, amitz-nv, coderabbitai, jiahanc
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-23T17:35:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces dynamic activation function selection for BF16 Mixture-of-Experts (MoE) operations. Previously, the activation ... (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-3993449511)
- `2026-03-24T16:10:27Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4000491730)
- `2026-03-24T17:05:31Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4000845369)
- `2026-03-30T09:41:04Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4029310170)
- `2026-03-31T16:20:22Z` `COMMENTED` by `coderabbitai` - ♻️ Duplicate comments (1) csrc/trtllm fused moe kernel launcher.cu (1) 1784-1842: ⚠️ Potential issue 🟠 Major Reject non-gated ... (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4038560903)
- `2026-04-01T10:25:06Z` `COMMENTED` by `amirkl94` (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4043199213)
- `2026-04-01T10:26:48Z` `COMMENTED` by `amirkl94` (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4043208638)
- `2026-04-05T08:24:19Z` `COMMENTED` by `amitz-nv` (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4059260125)
- `2026-04-05T08:36:18Z` `COMMENTED` by `amitz-nv` (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4059268113)
- `2026-04-05T11:31:55Z` `COMMENTED` by `amitz-nv` (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4059391351)
- `2026-04-05T12:00:26Z` `APPROVED` by `jiahanc` - LGTM, thanks for contribution! (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4059413391)
- `2026-04-13T09:03:42Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4097545740)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 3 inline comment(s)
- `flashinfer/fused_moe/core.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-24T16:10:27Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cache, flashinfer, gemm, hang, kernel, moe, register; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (3) csrc/trtllm fused ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4000491730)
- `2026-03-30T09:41:04Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, bf16, cache, flashinfer, fp8, gemm, hang, kernel; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) tests/moe/test trtllm ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4029310170)
- `2026-03-24T17:05:31Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cache, flashinfer, gemm, hang, kernel, moe; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4000845369)
- `2026-03-31T16:20:22Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, fp8, gemm, hang, kernel, layout, moe; excerpt: "♻️ Duplicate comments (1) csrc/trtllm fused moe kernel launcher.cu (1) 1784-1842: ⚠️ Potential issue 🟠 Major Reject non-gated activations in the FP8 per-tensor entrypoint. ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#pullrequestreview-4038560903)
- `2026-03-23T17:24:40Z` `issue` by `coderabbitai`; signals: bf16, cuda, flashinfer, fp8, gemm, hang, kernel, moe; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#issuecomment-4112351780)
- `2026-03-24T17:05:31Z` `inline` by `coderabbitai` `csrc/trtllm_fused_moe_kernel_launcher.cu`:1761; signals: autotune, fp8, kernel, layout, moe; excerpt: "⚠️ Potential issue 🟠 Major Unify the FP8 per-tensor activation contract. trtllm fp8 per tensor scale moe() now accepts any valid activation enum, but ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#discussion_r2983053660)
- `2026-04-05T08:36:17Z` `inline` by `amitz-nv` `csrc/trtllm_fused_moe_kernel_launcher.cu`:533; signals: bf16, kernel, moe; excerpt: "IIUC in BF16 the output buffer allocations are not doubled when using a gated activation so with BF16, so it's the same with gated ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#discussion_r3036590994)
- `2026-04-01T10:26:48Z` `inline` by `amirkl94` `flashinfer/fused_moe/core.py`:2209; signals: flashinfer, hang, moe; excerpt: "Mention that relu2 is non-gated which changes the w1 shape" (https://github.com/flashinfer-ai/flashinfer/pull/2864#discussion_r3021193283)
- `2026-04-05T08:24:19Z` `inline` by `amitz-nv` `flashinfer/fused_moe/core.py`:2209; signals: flashinfer, hang, moe; excerpt: "IMO mentioning the w1 shape here is a bit too detailed, changing to - 6: Relu2 (non-gated)" (https://github.com/flashinfer-ai/flashinfer/pull/2864#discussion_r3036580495)
- `2026-04-05T11:31:55Z` `inline` by `amitz-nv` `flashinfer/fused_moe/core.py`:2209; signals: flashinfer, gemm, moe; excerpt: "I updated the gemm1 weights docstring" (https://github.com/flashinfer-ai/flashinfer/pull/2864#discussion_r3036750753)
- `2026-04-01T10:25:06Z` `inline` by `amirkl94` `csrc/trtllm_fused_moe_kernel_launcher.cu`:533; signals: kernel, moe; excerpt: "All of the relevant buffer allocations that need to be reduced (as we're non-gated), are being handled in a common path right?" (https://github.com/flashinfer-ai/flashinfer/pull/2864#discussion_r3021185118)
- `2026-04-13T09:04:39Z` `issue` by `amitz-nv`; signals: hang, moe; excerpt: "I think pre-commit was run before was merged, which changed the parameters of trtllm moe finalize allreduce fusion, so now when both are merged, ..." (https://github.com/flashinfer-ai/flashinfer/pull/2864#issuecomment-4235171000)
