# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2902](https://github.com/flashinfer-ai/flashinfer/pull/2902)
- Source page: `sources/prs/flashinfer/PR-2902.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2902`
- Generated at: `2026-05-20T15:25:48.722543+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-27T14:45:39Z`
- Merged: `2026-04-03T04:15:03Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 10
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=9, outdated=2
- Human participants with discussion text: aleozlx, coderabbitai, johnnynunez, samuellees
- Automation comments/reviews omitted from high-signal summary: 12
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-27T14:50:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request implements MXFP8 GEMM support for SM120 (Blackwell) GPUs using CUTLASS. The changes include ... (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4021706184)
- `2026-03-27T14:57:30Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4021755645)
- `2026-03-28T03:02:50Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🧹 Nitpick comments (1) include/flashinfer/gemm/mxfp8 gemm cutlass template sm120.h (1) 106-114: Add a comment ... (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4024618674)
- `2026-03-28T03:12:32Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (1) include/flashinfer/gemm/mxfp8 gemm template sm120.h (1) 221-249: Cache workspace size once ... (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4024629412)
- `2026-03-28T03:43:28Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (1) tests/gemm/test mm mxfp8 sm120.py (1) 79-107: all tactics test name ... (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4024687690)
- `2026-03-31T15:46:43Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4038366478)
- `2026-04-01T15:20:25Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4044998206)

## Inline Comment Hotspots

- `flashinfer/gemm/gemm_base.py`: 5 inline comment(s)
- `tests/gemm/test_mm_mxfp8_sm120.py`: 2 inline comment(s)
- `csrc/mxfp8_gemm_cutlass_sm120.cu`: 1 inline comment(s)
- `docs/api/gemm.rst`: 1 inline comment(s)
- `include/flashinfer/gemm/mxfp8_gemm_template_sm120.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-27T14:57:30Z` `review` `COMMENTED` by `coderabbitai`; signals: alignment, cutlass, flashinfer, fp8, gemm, hang, layout, sm120; excerpt: "Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4021755645)
- `2026-03-31T15:46:43Z` `review` `COMMENTED` by `coderabbitai`; signals: alignment, block, cutlass, dtype, flashinfer, fp8, gemm, hang; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) flashinfer/gemm/gemm base.py ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4038366478)
- `2026-03-27T14:46:09Z` `issue` by `coderabbitai`; signals: alignment, block, cache, compile, correctness, cuda, cutlass, dtype; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#issuecomment-4143141404)
- `2026-03-28T03:02:50Z` `review` `COMMENTED` by `coderabbitai`; signals: cutlass, flashinfer, fp8, gemm, hang, sm120; excerpt: "Actionable comments posted: 3 🧹 Nitpick comments (1) include/flashinfer/gemm/mxfp8 gemm cutlass template sm120.h (1) 106-114: Add a comment explaining why exceptions are swallowed here. ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4024618674)
- `2026-03-28T03:12:32Z` `review` `COMMENTED` by `coderabbitai`; signals: cache, flashinfer, fp8, gemm, hang, sm120; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (1) include/flashinfer/gemm/mxfp8 gemm template sm120.h (1) 221-249: Cache workspace size once to avoid repeated calls. Small cleanup: ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4024629412)
- `2026-03-27T14:57:29Z` `inline` by `coderabbitai` `flashinfer/gemm/gemm_base.py`:3293; signals: cutlass, flashinfer, fp8, gemm, sm100, sm120; excerpt: "⚠️ Potential issue 🟠 Major SM120 CUTLASS is wired only into mm mxfp8(). get gemm sm120 module cutlass mxfp8() is only consumed by the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#discussion_r3001495767)
- `2026-03-27T14:57:29Z` `inline` by `coderabbitai` `tests/gemm/test_mm_mxfp8_sm120.py`:19; signals: cuda, cute, flashinfer, fp8, gemm, sm120; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 351 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#discussion_r3001495772)
- `2026-03-28T03:43:28Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, fp8, gemm, hang, sm120; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (1) tests/gemm/test mm mxfp8 sm120.py (1) 79-107: all tactics test name is misleading for current behavior. The ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#pullrequestreview-4024687690)
- `2026-03-28T03:02:49Z` `inline` by `coderabbitai` `flashinfer/gemm/gemm_base.py`:3284; signals: failing, flashinfer, gemm, hang, sm120; excerpt: "⚠️ Potential issue 🟡 Minor Fix clang-format drift in the SM120 module accessor. Pre-commit reports formatting changes in this section, so this will keep ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#discussion_r3004026007)
- `2026-03-28T03:02:49Z` `inline` by `coderabbitai` `flashinfer/gemm/gemm_base.py`:6990; signals: benchmark, cutlass, flashinfer, gemm, layout; excerpt: "⚠️ Potential issue 🟡 Minor Correct the SM12x BMM B-layout docstring. This text says callers must pass B as [b, n, k], but the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#discussion_r3004026010)
- `2026-03-28T03:02:49Z` `inline` by `coderabbitai` `include/flashinfer/gemm/mxfp8_gemm_template_sm120.h`:74; signals: block, flashinfer, fp8, gemm, sm120; excerpt: "⚠️ Potential issue 🟡 Minor Run clang-format on this new header to unblock pre-commit. CI reports formatting drift at this line range in this ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#discussion_r3004026011)
- `2026-03-28T03:12:32Z` `inline` by `coderabbitai` `flashinfer/gemm/gemm_base.py`:3435; signals: cutlass, flashinfer, gemm, kernel, layout; excerpt: "⚠️ Potential issue 🟠 Major Reject 8x4 swizzled scales on SM12x CUTLASS. This branch only gates on “1D vs 2D”, so use 8x4 sf ..." (https://github.com/flashinfer-ai/flashinfer/pull/2902#discussion_r3004036220)
