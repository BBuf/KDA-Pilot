# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2303](https://github.com/flashinfer-ai/flashinfer/pull/2303)
- Source page: `sources/prs/flashinfer/PR-2303.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2303`
- Generated at: `2026-05-20T15:24:33.276103+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-07T17:41:01Z`
- Merged: `2026-02-03T04:57:24Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 11 (approved=4, commented=7)
- Inline review comments: 12
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=3
- Human participants with discussion text: IwakuraRein, LopezCastroRoberto, aleozlx, bkryu, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-07T17:43:49Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces SM103-specific schedulers for NVFP4 CUTLASS kernels to enhance performance, particularly for larger ... (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3636074164)
- `2026-01-07T17:46:02Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3636084019)
- `2026-01-07T19:33:11Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) flashinfer/jit/gemm/core.py (1) 157-161: ... (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3636497383)
- `2026-01-16T23:58:13Z` `APPROVED` by `IwakuraRein` - LTGM. Thanks for the contributions! (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3673154109)
- `2026-01-20T18:32:25Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3683710889)
- `2026-01-20T19:24:25Z` `APPROVED` by `aleozlx` - LGTM as well. but wanna give some time for other comments to be resolved (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3683922440)
- `2026-01-20T19:49:23Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3684007033)
- `2026-01-21T14:26:17Z` `COMMENTED` by `LopezCastroRoberto` (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3687536814)
- `2026-01-21T14:34:37Z` `COMMENTED` by `LopezCastroRoberto` (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3687579002)
- `2026-02-02T23:08:56Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3742021495)
- `2026-02-03T04:57:11Z` `APPROVED` by `bkryu` - LGTM. Unit tests are also coming back as passing. (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3742948997)

## Inline Comment Hotspots

- `include/flashinfer/gemm/fp4_gemm_template_sm103.h`: 5 inline comment(s)
- `flashinfer/gemm/gemm_base.py`: 3 inline comment(s)
- `include/flashinfer/gemm/cutlass_gemm_configs.h`: 2 inline comment(s)
- `flashinfer/jit/gemm/core.py`: 1 inline comment(s)
- `flashinfer/jit/gemm/cutlass/cutlass_library.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-07T17:46:02Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, block, cache, cuda, cutlass, dtype, flashinfer, fp4; excerpt: "Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3636084019)
- `2026-01-07T19:33:11Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cache, cuda, cutlass, flashinfer, fp4, gemm, hang; excerpt: "Actionable comments posted: 1 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) flashinfer/jit/gemm/core.py (1) 157-161: Consider using spread operator for list ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#pullrequestreview-3636497383)
- `2026-02-02T23:08:56Z` `inline` by `IwakuraRein` `include/flashinfer/gemm/fp4_gemm_template_sm103.h`:111; signals: cutlass, flashinfer, fp4, gemm, perf, performance, regression, sm100; excerpt: "I was thinking if many sm100 dispatch policy will be disabled when arch is cutlass::arch::Sm103. But since there is no performance regression, I guess ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2756408213)
- `2026-01-07T17:41:13Z` `issue` by `coderabbitai`; signals: bf16, cuda, cutlass, flashinfer, fp4, gemm, h100, hang; excerpt: "[!NOTE] Other AI code review bot(s) detected CodeRabbit has detected other AI code review bot(s) in this pull request and will avoid duplicating their ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#issuecomment-3720001535)
- `2026-01-07T17:46:01Z` `inline` by `coderabbitai` `flashinfer/jit/gemm/cutlass/cutlass_library.py`:627; signals: benchmark, cutlass, flashinfer, gemm, kernel, tma, warp; excerpt: "🛠️ Refactor suggestion 🟠 Major Remove personal annotation and add missing suffix entry. The RLC: comment appears to be a personal annotation that should ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2669483347)
- `2026-01-16T23:35:45Z` `inline` by `IwakuraRein` `include/flashinfer/gemm/fp4_gemm_template_sm103.h`:111; signals: cute, cutlass, flashinfer, fp4, gemm, sm100; excerpt: "Could you confirm if using Arch = cutlass::arch::Sm103; works for CTA K != 768? Looks like the sm100 collective builders have this check cute::is ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2700328764)
- `2026-01-07T17:46:01Z` `inline` by `coderabbitai` `flashinfer/gemm/gemm_base.py`:532; signals: cutlass, flashinfer, fp4, gemm, sm100; excerpt: "⚠️ Potential issue 🟡 Minor Inconsistent docstring - copy-paste error. The docstring says "Get the SM100/103/110 FP4 GEMM module" but this function is specifically ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2669483339)
- `2026-01-07T17:46:01Z` `inline` by `coderabbitai` `include/flashinfer/gemm/fp4_gemm_template_sm103.h`:283; signals: benchmark, flashinfer, fp4, gemm, sm100; excerpt: "⚠️ Potential issue 🟡 Minor Error messages reference wrong architecture (sm100 instead of sm103). The error messages on lines 272 and 278 say "Failed ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2669483369)
- `2026-01-07T19:33:11Z` `inline` by `coderabbitai` `flashinfer/gemm/gemm_base.py`:519; signals: cutlass, flashinfer, fp4, gemm, sm100; excerpt: "⚠️ Potential issue 🟡 Minor Update docstring to reflect SM103 now has a separate module. The docstring still references "SM100/103/110" but SM103 is now ..." (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2669821338)
- `2026-01-21T14:34:36Z` `inline` by `LopezCastroRoberto` `include/flashinfer/gemm/cutlass_gemm_configs.h`:200; signals: cute, cutlass, flashinfer, gemm, tile; excerpt: "For configurations using the 2SM setup, the M dimension in MmaTileShape is set to 256. using MmaTileShape = cute::Shape ::Scale ," (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2712851392)
- `2026-01-20T18:32:25Z` `inline` by `IwakuraRein` `include/flashinfer/gemm/cutlass_gemm_configs.h`:200; signals: cutlass, flashinfer, gemm, tile; excerpt: "Do you know the reason why TileShape doesn't have M==256?" (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2709601609)
- `2026-01-21T14:26:17Z` `inline` by `LopezCastroRoberto` `include/flashinfer/gemm/fp4_gemm_template_sm103.h`:111; signals: cutlass, flashinfer, fp4, gemm; excerpt: "Thanks for your review. Do you mean to remove that assert inside cutlass and try if it works?" (https://github.com/flashinfer-ai/flashinfer/pull/2303#discussion_r2712816028)
