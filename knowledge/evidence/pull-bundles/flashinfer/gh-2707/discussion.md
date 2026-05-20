# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2707](https://github.com/flashinfer-ai/flashinfer/pull/2707)
- Source page: `sources/prs/flashinfer/PR-2707.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2707`
- Generated at: `2026-05-20T15:25:25.911466+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-06T12:40:26Z`
- Merged: `2026-03-19T17:49:43Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 9
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=5
- Human participants with discussion text: aleozlx, coderabbitai, danisereb
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-06T12:49:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for non-gated MoE with ReLU2 for TRTLLM MXFP8, which is a ... (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3903553928)
- `2026-03-08T19:31:26Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3911925257)
- `2026-03-08T19:51:19Z` `COMMENTED` by `danisereb` (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3911941602)
- `2026-03-08T19:51:55Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3911941964)
- `2026-03-08T20:59:51Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3912018610)
- `2026-03-09T03:13:39Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3912642413)
- `2026-03-09T10:20:35Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3914369635)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 8 inline comment(s)
- `tests/moe/test_trtllm_gen_routed_fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-06T12:40:48Z` `issue` by `coderabbitai`; signals: autotune, block, flashinfer, fp4, fp8, hang, kernel, moe; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#issuecomment-4011528015)
- `2026-03-08T20:59:51Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cache, cute, hang, kernel, moe; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3912018610)
- `2026-03-08T19:31:25Z` `inline` by `coderabbitai` `tests/moe/test_trtllm_gen_routed_fused_moe.py`:396; signals: benchmark, fp8, gemm, kernel, layout, moe; excerpt: "⚠️ Potential issue 🟡 Minor Don't mark unshuffled FP8 weights as shuffled in this parity test. This case never runs gemm1 weights or gemm2 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#discussion_r2902306399)
- `2026-03-09T10:20:34Z` `inline` by `coderabbitai` `csrc/trtllm_fused_moe_kernel_launcher.cu`:2227; signals: fp8, gemm, kernel, layout, moe; excerpt: "⚠️ Potential issue 🟠 Major Mirror the nongated FP8-per-tensor rejection in the execution API. trtllm get valid moe configs() now rejects nongated per-tensor FP8 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#discussion_r2904505338)
- `2026-03-08T19:31:26Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel, moe; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ Run configuration Configuration used : defaults ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3911925257)
- `2026-03-08T19:51:55Z` `inline` by `coderabbitai` `csrc/trtllm_fused_moe_kernel_launcher.cu`:1153; signals: block, fp8, kernel, moe; excerpt: "@danisereb, confirmed — all three DeepSeek FP8 sites are now properly guarded: 1. Fp8BlockScaleLauncher::getValidConfigs — validateAndCastActivationType + TVM FFI ICHECK EQ(activation type, ActivationType::Swiglu) before ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#discussion_r2902329615)
- `2026-03-09T10:20:35Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, kernel, moe; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ Run configuration Configuration used : defaults ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#pullrequestreview-3914369635)
- `2026-03-08T19:31:25Z` `inline` by `coderabbitai` `csrc/trtllm_fused_moe_kernel_launcher.cu`:1153; signals: fp8, kernel, moe; excerpt: "⚠️ Potential issue 🟠 Major DeepSeek FP8 still collapses distinct gated activations onto one implementation. These checks now admit any gated act type, but ..." (https://github.com/flashinfer-ai/flashinfer/pull/2707#discussion_r2902306398)
- `2026-03-08T19:51:19Z` `inline` by `danisereb` `csrc/trtllm_fused_moe_kernel_launcher.cu`:1153; signals: kernel, moe; excerpt: "Fixed" (https://github.com/flashinfer-ai/flashinfer/pull/2707#discussion_r2902329040)
