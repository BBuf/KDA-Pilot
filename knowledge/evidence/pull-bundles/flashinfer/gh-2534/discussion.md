# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2534](https://github.com/flashinfer-ai/flashinfer/pull/2534)
- Source page: `sources/prs/flashinfer/PR-2534.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2534`
- Generated at: `2026-05-20T15:24:59.568299+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-10T12:42:04Z`
- Merged: `2026-03-30T16:07:37Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 12
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=5, outdated=6
- Human participants with discussion text: ChristinaZ, aleozlx, coderabbitai, mgoin, wenscarl, wzhao18, yweng0828
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-10T12:46:18Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request introduces support for fp32 logits in the fused MoE kernels, specifically for fp8 ... (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3778736589)
- `2026-02-11T07:54:51Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3783303894)
- `2026-02-12T07:18:42Z` `COMMENTED` by `yweng0828` (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3789090156)
- `2026-02-12T07:19:03Z` `COMMENTED` by `yweng0828` (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3789091246)
- `2026-02-12T07:24:09Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3789108533)
- `2026-02-19T23:05:36Z` `COMMENTED` by `mgoin` (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3828987686)
- `2026-02-20T19:18:05Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3833817774)
- `2026-02-20T19:19:17Z` `APPROVED` by `aleozlx` - lgtm tests clean, ready to merge (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3833821746)
- `2026-02-20T20:52:13Z` `COMMENTED` by `mgoin` (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3834162723)
- `2026-03-17T19:10:08Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3963133615)
- `2026-03-17T19:21:14Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3963210858)
- `2026-03-18T23:35:56Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (1) tests/moe/test trtllm gen fused moe.py (1) 3298-3326: Consider adding FP32 ... (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3971552338)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 4 inline comment(s)
- `include/flashinfer/trtllm/fused_moe/DevKernel.h`: 4 inline comment(s)
- `tests/moe/utils.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-17T19:10:08Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, block, cache, dtype, flashinfer, fp4, fp8, gemm; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (2) tests/moe/test trtllm ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3963133615)
- `2026-03-17T19:21:14Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cache, correctness, dtype, flashinfer, fp4, gemm, hang; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3963210858)
- `2026-02-12T07:24:09Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cache, dtype, flashinfer, fp8, kernel, moe; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3789108533)
- `2026-02-12T07:17:56Z` `issue` by `coderabbitai`; signals: bf16, block, dtype, flashinfer, fp8, hang, kernel, moe; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#issuecomment-3889080250)
- `2026-03-18T23:35:55Z` `inline` by `coderabbitai` `csrc/trtllm_fused_moe_kernel_launcher.cu`:523; signals: benchmark, cute, dtype, flashinfer, kernel, moe; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 3594 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#discussion_r2956851258)
- `2026-03-18T23:35:56Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, fp8, hang, kernel, moe; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (1) tests/moe/test trtllm gen fused moe.py (1) 3298-3326: Consider adding FP32 logits test for Llama4 routing. FP8PerTensorMoe ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#pullrequestreview-3971552338)
- `2026-03-17T19:21:13Z` `inline` by `coderabbitai` `include/flashinfer/trtllm/fused_moe/DevKernel.h`:236; signals: cute, dtype, flashinfer, kernel, moe; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 7267 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#discussion_r2949060341)
- `2026-03-06T02:02:18Z` `issue` by `yweng0828`; signals: block, fp4, fp8, hang, moe; excerpt: "@yweng0828 Does the change also apply to trtllm fp4 block scale moe? Hi @wenscarl, No, this change does not apply to trtllm fp4 block ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#issuecomment-4009042514)
- `2026-03-17T19:21:13Z` `inline` by `coderabbitai` `include/flashinfer/trtllm/fused_moe/DevKernel.h`:202; signals: cute, flashinfer, kernel, moe; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 500 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#discussion_r2949060334)
- `2026-02-11T07:52:03Z` `inline` by `ChristinaZ` `include/flashinfer/trtllm/fused_moe/DevKernel.h`:269; signals: dtype, flashinfer, kernel, moe; excerpt: "How about use this infor: Unsupported combination of mDtypeScore and mDtypeExpW" (https://github.com/flashinfer-ai/flashinfer/pull/2534#discussion_r2791874687)
- `2026-03-17T19:39:11Z` `issue` by `aleozlx`; signals: block, flashinfer, kernel, moe; excerpt: "Hi @yweng0828 we are trying to help merging it. last week we had an CI issue blocking all PRs merging. i refreshed the branch ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#issuecomment-4077549875)
- `2026-02-11T07:46:58Z` `inline` by `ChristinaZ` `csrc/trtllm_fused_moe_kernel_launcher.cu`:587; signals: fp8, kernel, moe; excerpt: "Should this piece of code be part of the FusedMoeLauncher class so that all child classes can share it? It seems that this logic ..." (https://github.com/flashinfer-ai/flashinfer/pull/2534#discussion_r2791858862)
