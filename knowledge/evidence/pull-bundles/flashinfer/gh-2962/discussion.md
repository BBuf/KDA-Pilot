# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2962](https://github.com/flashinfer-ai/flashinfer/pull/2962)
- Source page: `sources/prs/flashinfer/PR-2962.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2962`
- Generated at: `2026-05-20T15:26:00.016333+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T17:14:07Z`
- Merged: `2026-05-13T00:09:14Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 16 (approved=1, commented=15)
- Inline review comments: 19
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: aleozlx, bkryu, coderabbitai, ishovkun, yzh119
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2026-04-02T17:18:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for NVIDIA Blackwell (SM100) architectures in the Mamba selective state update ... (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052040151)
- `2026-04-02T17:31:26Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052111208)
- `2026-04-02T17:47:04Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (2) include/flashinfer/mamba/invoke selective state update mtp.cuh (2) 6-8: Consider removing unused include. The header is ... (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052201694)
- `2026-04-02T17:53:55Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052235742)
- `2026-04-02T17:54:41Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052240517)
- `2026-04-02T18:10:17Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) include/flashinfer/mamba/invoke selective state update mtp.cuh (1) 263-263: Use std::max instead of unqualified max in ... (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052320193)
- `2026-04-02T18:42:47Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052497463)
- `2026-04-02T18:43:20Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052500918)
- `2026-04-02T18:44:59Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052511970)
- `2026-04-02T18:45:40Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052516236)
- `2026-04-02T18:46:30Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052521564)
- `2026-04-02T18:48:21Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052535256)
- `2026-04-02T18:48:49Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052538747)
- `2026-05-13T00:09:04Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4277099851)

## Inline Comment Hotspots

- `benchmarks/bench_ssu_sweep_sol.py`: 4 inline comment(s)
- `include/flashinfer/mamba/kernel_selective_state_update_mtp_horizontal.cuh`: 4 inline comment(s)
- `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`: 4 inline comment(s)
- `include/flashinfer/mamba/kernel_selective_state_update_mtp_simple.cuh`: 3 inline comment(s)
- `include/flashinfer/mamba/invoke_selective_state_update_mtp.cuh`: 2 inline comment(s)
- `benchmarks/bench_ssu_sweep_mtp.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-02T17:31:26Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, benchmark, compile, failing, flashinfer, hang, kernel, regression; excerpt: "Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052111208)
- `2026-04-02T17:14:26Z` `issue` by `coderabbitai`; signals: aligned, alignment, benchmark, bf16, block, flashinfer, hang, kernel; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#issuecomment-4179271809)
- `2026-04-02T17:31:24Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_horizontal.cuh`:148; signals: epilogue, flashinfer, kernel, memory, shared memory, tma; excerpt: "⚠️ Potential issue 🟠 Major Pad mode can't skip the B/C/x transactions. IS PAD only zeroes the incoming state. The compute path still consumes ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029373955)
- `2026-04-02T17:31:24Z` `inline` by `coderabbitai` `benchmarks/bench_ssu_sweep_mtp.py`:359; signals: benchmark, bf16, dtype, flashinfer; excerpt: "⚠️ Potential issue 🟠 Major Reject non-f16-philox- specs here. parse dtype spec() currently accepts bf16-philox- and f32-philox- , but the MTP path only supports ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029373926)
- `2026-04-02T17:31:24Z` `inline` by `coderabbitai` `include/flashinfer/mamba/invoke_selective_state_update_mtp.cuh`:163; signals: benchmark, flashinfer, kernel, tma; excerpt: "⚠️ Potential issue 🟠 Major Validate DIM against TMA STATE ROWS, not 16. The horizontal launcher currently admits any DIM multiple of 16, but ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029373949)
- `2026-04-02T17:31:24Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_simple.cuh`:262; signals: cache, flashinfer, hang, kernel; excerpt: "⚠️ Potential issue 🔴 Critical The unified dst slot path changed update state semantics. Two cases break here: dst state batch indices still produces ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029373960)
- `2026-04-02T18:48:49Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`:198; signals: compile, flashinfer, kernel, warp; excerpt: "@ishovkun, thanks for adding the guard! The explicit static assert(DSTATE % warpSize == 0, ...) ensures misconfigurations are caught at compile time rather than ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029743511)
- `2026-04-02T18:10:17Z` `review` `COMMENTED` by `coderabbitai`; signals: cuda, flashinfer, hang; excerpt: "🧹 Nitpick comments (1) include/flashinfer/mamba/invoke selective state update mtp.cuh (1) 263-263: Use std::max instead of unqualified max in host code. The unqualified max call ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052320193)
- `2026-04-02T18:46:30Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#pullrequestreview-4052521564)
- `2026-04-02T17:31:24Z` `inline` by `coderabbitai` `benchmarks/bench_ssu_sweep_sol.py`:269; signals: benchmark, kernel, sm100; excerpt: "⚠️ Potential issue 🟡 Minor --ncu mode currently aborts on unsupported kernels. The timed path catches RuntimeError and keeps the sweep going, but the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029373943)
- `2026-04-02T17:31:24Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`:198; signals: flashinfer, kernel, warp; excerpt: "⚠️ Potential issue 🟠 Major Make the DSTATE % 32 requirement explicit. stateValuesPerThread uses integer division, and every load/store loop assumes that quotient covers ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029373963)
- `2026-04-02T18:44:59Z` `inline` by `ishovkun` `include/flashinfer/mamba/kernel_selective_state_update_mtp_simple.cuh`:262; signals: cache, flashinfer, kernel; excerpt: "The reviewer's finding is wrong: 1. intermediate states buffer and dst state batch indices are mutually exclusive — enforced by the Python-side ValueError at ..." (https://github.com/flashinfer-ai/flashinfer/pull/2962#discussion_r3029723578)
