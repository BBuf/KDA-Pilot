# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2505](https://github.com/flashinfer-ai/flashinfer/pull/2505)
- Source page: `sources/prs/flashinfer/PR-2505.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2505`
- Generated at: `2026-05-20T15:24:57.125762+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-06T01:45:45Z`
- Merged: `2026-02-17T19:11:27Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 19 (approved=2, commented=17)
- Inline review comments: 22
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=11, outdated=6
- Human participants with discussion text: IwakuraRein, aleozlx, coderabbitai, danisereb, vincentzed, vipulSharma18, yzh119
- Automation comments/reviews omitted from high-signal summary: 14
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-06T01:47:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates mxfp8 support into the trtllm fused MoE kernels. The changes are extensive, ... (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3760299353)
- `2026-02-06T23:56:04Z` `COMMENTED` by `vipulSharma18` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3765627231)
- `2026-02-07T00:15:52Z` `COMMENTED` by `vipulSharma18` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3765660166)
- `2026-02-07T02:41:39Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3765980083)
- `2026-02-07T03:05:52Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3766042724)
- `2026-02-07T03:08:35Z` `COMMENTED` by `vipulSharma18` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3766055949)
- `2026-02-12T17:58:23Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3792705584)
- `2026-02-13T02:24:45Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3794722223)
- `2026-02-13T02:26:32Z` `COMMENTED` by `aleozlx` - looks good overall. posted a comment about GatedActType (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3794725468)
- `2026-02-13T19:43:34Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799171947)
- `2026-02-13T19:49:09Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799199582)
- `2026-02-13T19:51:20Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799208397)
- `2026-02-13T19:55:56Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799227944)
- `2026-02-13T20:59:36Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799493401)
- `2026-02-13T21:03:32Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799513860)
- `2026-02-13T21:06:22Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799527090)
- `2026-02-17T19:07:44Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3815793493)
- `2026-02-17T19:08:14Z` `APPROVED` by `aleozlx` - lgtm (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3815795184)
- `2026-02-17T19:11:25Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3815806257)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 13 inline comment(s)
- `flashinfer/fused_moe/core.py`: 5 inline comment(s)
- `benchmarks/bench_trtllm_gen_fused_moe_autotuner.py`: 3 inline comment(s)
- `flashinfer/fused_moe/__init__.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-13T19:55:56Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, dtype, fp8, gemm, kernel, layout, moe, tile; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799227944)
- `2026-02-12T17:58:23Z` `review` `COMMENTED` by `coderabbitai`; signals: block, dtype, flashinfer, fp8, gemm, kernel, moe; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3792705584)
- `2026-02-13T19:49:09Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, benchmark, block, flashinfer, fp8, kernel, moe; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) csrc/trtllm fused ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799199582)
- `2026-02-06T01:45:51Z` `issue` by `coderabbitai`; signals: autotune, benchmark, block, cuda, dtype, flashinfer, fp8, gemm; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#issuecomment-3857385399)
- `2026-02-13T19:55:54Z` `inline` by `coderabbitai` `csrc/trtllm_fused_moe_kernel_launcher.cu`:992; signals: benchmark, cute, flashinfer, fp8, gemm, kernel, moe; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 113 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#discussion_r2805859824)
- `2026-02-13T21:03:32Z` `inline` by `coderabbitai` `csrc/trtllm_fused_moe_kernel_launcher.cu`:992; signals: cute, epilogue, fp8, gemm, kernel, moe; excerpt: "🧩 Analysis chain 🏁 Script executed: Length of output: 17272 --- 🏁 Script executed: Length of output: 0 --- 🏁 Script executed: Length of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#discussion_r2806082288)
- `2026-02-13T21:06:22Z` `review` `COMMENTED` by `coderabbitai`; signals: dtype, fp8, gemm, kernel, moe; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) csrc/trtllm fused ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#pullrequestreview-3799527090)
- `2026-02-07T00:15:52Z` `inline` by `vipulSharma18` `csrc/trtllm_fused_moe_kernel_launcher.cu`:909; signals: block, fp8, kernel, layout, moe; excerpt: "since mxfp8 seems to be hardcoding the weight layout to be blockmajorK, it will be nice to get a device side assert for that ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#discussion_r2776505219)
- `2026-02-07T02:41:39Z` `inline` by `IwakuraRein` `csrc/trtllm_fused_moe_kernel_launcher.cu`:909; signals: block, fp8, kernel, layout, moe; excerpt: "since mxfp8 seems to be hardcoding the weight layout to be blockmajorK I think mxfp8 also supports K major? Will double check." (https://github.com/flashinfer-ai/flashinfer/pull/2505#discussion_r2776783520)
- `2026-02-07T03:08:35Z` `inline` by `vipulSharma18` `csrc/trtllm_fused_moe_kernel_launcher.cu`:909; signals: bf16, block, kernel, layout, moe; excerpt: "Thanks, my bad! I spent a lot of time debugging block major k layout for bf16 trtllm kernel, it will really help to have ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#discussion_r2776852141)
- `2026-02-13T19:43:34Z` `inline` by `IwakuraRein` `flashinfer/fused_moe/core.py`:178; signals: block, flashinfer, fp8, hang, moe; excerpt: "Thanks. However, the only API change in this PR is adding a fp8 quantization type to the trtllm fp8 block scale routed moe. It ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#discussion_r2805817074)
- `2026-02-09T18:20:35Z` `issue` by `IwakuraRein`; signals: cache, compile, flashinfer, fp8, tile; excerpt: "@vincentzed Hi. There are tile size 64 cubins for mxfp8. I tried your problem shape and cannot reproduce the error. Could you try pull ..." (https://github.com/flashinfer-ai/flashinfer/pull/2505#issuecomment-3873225501)
