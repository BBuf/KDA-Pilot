# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2865](https://github.com/flashinfer-ai/flashinfer/pull/2865)
- Source page: `sources/prs/flashinfer/PR-2865.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2865`
- Generated at: `2026-05-20T15:25:46.371031+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T17:32:53Z`
- Merged: `2026-04-04T04:05:50Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 19
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=7
- Human participants with discussion text: aleozlx, coderabbitai, ishovkun, yongwww, yzh119
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-23T17:43:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces new vertical and horizontal MTP (Multi-Token Processing) kernels for selective state update ... (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3993509905)
- `2026-03-23T17:54:51Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3993571964)
- `2026-03-23T18:05:54Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3993635100)
- `2026-03-23T18:14:01Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3993676546)
- `2026-03-23T18:17:10Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3993695977)
- `2026-03-23T18:19:31Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3993710869)
- `2026-03-23T20:53:35Z` `COMMENTED` by `coderabbitai` - ♻️ Duplicate comments (1) include/flashinfer/mamba/kernel selective state update mtp vertical.cuh (1) 343-365: ⚠️ Potential issue 🟠 Major Use ... (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994640081)
- `2026-03-23T20:58:49Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994669957)
- `2026-03-23T21:01:30Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994681272)
- `2026-03-23T21:02:23Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994684853)
- `2026-03-23T21:04:32Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994693661)
- `2026-03-23T21:05:01Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994695670)
- `2026-03-23T21:06:30Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994703639)
- `2026-03-25T20:48:45Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-4009791401)
- `2026-03-25T21:12:16Z` `APPROVED` by `yzh119` - LGTM overall, thanks for the PR! (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-4009905204)

## Inline Comment Hotspots

- `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`: 7 inline comment(s)
- `include/flashinfer/mamba/kernel_selective_state_update_mtp_horizontal.cuh`: 5 inline comment(s)
- `include/flashinfer/mamba/invoke_selective_state_update_mtp.cuh`: 4 inline comment(s)
- `benchmarks/bench_ssu_sweep_mtp.py`: 2 inline comment(s)
- `3rdparty/cutlass`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-23T21:01:30Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`:214; signals: b200, benchmark, bf16, cute, dtype, flashinfer, hang, kernel; excerpt: "🧩 Analysis chain The PR description image shows three side-by-side bar charts titled "Selective State Update Benchmark (MTP=6) [NVIDIA B200]". Each subplot compares speedup ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2977578953)
- `2026-03-23T21:04:32Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`:366; signals: b200, benchmark, bf16, epilogue, flashinfer, kernel, layout, speedup; excerpt: "The PR description image shows three side-by-side bar charts titled “Selective State Update Benchmark (MTP=6) [NVIDIA B200]”. Each panel compares speedup vs Triton for ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2977590985)
- `2026-03-23T21:06:30Z` `inline` by `coderabbitai` `include/flashinfer/mamba/invoke_selective_state_update_mtp.cuh`:50; signals: alignment, b200, benchmark, bf16, compile, flashinfer, perf, performance; excerpt: "The PR description image shows three performance bar charts titled “Selective State Update Benchmark (MTP=6) [NVIDIA B200]” with bf16, f16-philox-5, and f32 panels. Across ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2977600059)
- `2026-03-23T17:33:16Z` `issue` by `coderabbitai`; signals: aligned, alignment, benchmark, blackwell, cuda, cutlass, dtype, flashinfer; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#issuecomment-4112431612)
- `2026-03-23T20:53:35Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, epilogue, flashinfer, hang, kernel, tile; excerpt: "♻️ Duplicate comments (1) include/flashinfer/mamba/kernel selective state update mtp vertical.cuh (1) 343-365: ⚠️ Potential issue 🟠 Major Use z's strides for gate loads. The ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3994640081)
- `2026-03-23T17:54:51Z` `review` `COMMENTED` by `coderabbitai`; signals: benchmark, cutlass, flashinfer, hang, kernel; excerpt: "Actionable comments posted: 7 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ Run configuration Configuration used : defaults ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#pullrequestreview-3993571964)
- `2026-03-23T18:17:10Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_horizontal.cuh`:77; signals: bf16, flashinfer, hang, kernel, speedup; excerpt: "The PR description image shows three side-by-side bar charts of speedup vs batch size for bf16, f16‑philox‑5, and f32. “horizontal” and “auto” variants lead, ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2976759490)
- `2026-03-23T17:54:49Z` `inline` by `coderabbitai` `include/flashinfer/mamba/invoke_selective_state_update_mtp.cuh`:83; signals: benchmark, epilogue, flashinfer, warp; excerpt: "⚠️ Potential issue 🟠 Major The vertical precondition needs DIM % 32 == 0 today. The current % 16 guard lets shapes like DIM=80 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2976645072)
- `2026-03-23T17:54:49Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_horizontal.cuh`:77; signals: flashinfer, hang, kernel, layout; excerpt: "⚠️ Potential issue 🔴 Critical Do not collapse dt/dt bias/A/D across the dim axis. Line 81 only stores dt as [head][token], Lines 264-268 load ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2976645089)
- `2026-03-23T17:54:49Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`:103; signals: flashinfer, kernel, tile, tma; excerpt: "⚠️ Potential issue 🔴 Critical Don't TMA-load state for padded slots. is pad is computed in the kernel entry, but role load() still uses ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2976645108)
- `2026-03-23T17:54:50Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_vertical.cuh`:366; signals: epilogue, flashinfer, kernel, layout; excerpt: "⚠️ Potential issue 🟠 Major Use z's strides for gate loads. The epilogue derives base offset from out stride and then reuses it for ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2976645112)
- `2026-03-23T17:54:49Z` `inline` by `coderabbitai` `include/flashinfer/mamba/kernel_selective_state_update_mtp_horizontal.cuh`:107; signals: benchmark, flashinfer, kernel; excerpt: "⚠️ Potential issue 🔴 Critical rand ints is uninitialized on every e == 2 mod 4 call. Because rand ints is stack-local, Line 104 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2865#discussion_r2976645091)
