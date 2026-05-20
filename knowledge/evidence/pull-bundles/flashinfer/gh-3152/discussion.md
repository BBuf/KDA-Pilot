# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#3152](https://github.com/flashinfer-ai/flashinfer/pull/3152)
- Source page: `sources/prs/flashinfer/PR-3152.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-3152`
- Generated at: `2026-05-20T15:26:20.639467+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-23T04:01:34Z`
- Merged: `2026-05-05T17:19:10Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 8
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=4
- Human participants with discussion text: aleozlx, bkryu, coderabbitai, depaulmillz
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-23T04:05:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the swap ab parameter and new tile configurations (N=32, N=64) ... (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4159581307)
- `2026-04-23T04:45:10Z` `COMMENTED` by `depaulmillz` (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4159703985)
- `2026-04-23T04:45:18Z` `COMMENTED` by `depaulmillz` (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4159704365)
- `2026-04-24T00:34:06Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4167054695)
- `2026-04-25T19:28:51Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4176035145)
- `2026-04-28T18:34:01Z` `APPROVED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4191476105)
- `2026-04-28T18:43:18Z` `APPROVED` by `aleozlx` - lgtm (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4191529246)

## Inline Comment Hotspots

- `include/flashinfer/gemm/fp4_gemm_cutlass_template_sm120.h`: 3 inline comment(s)
- `include/flashinfer/gemm/mxfp8_gemm_template_sm120.h`: 2 inline comment(s)
- `flashinfer/gemm/gemm_base.py`: 1 inline comment(s)
- `flashinfer/jit/gemm/core.py`: 1 inline comment(s)
- `tests/gemm/test_mm_mxfp8_sm120.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-24T00:34:06Z` `review` `COMMENTED` by `coderabbitai`; signals: compile, cutlass, dtype, flashinfer, fp4, fp8, gemm, hang; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4167054695)
- `2026-04-23T04:01:41Z` `issue` by `coderabbitai`; signals: block, compile, cute, cutlass, flashinfer, fp4, fp8, gemm; excerpt: "📝 Walkthrough Walkthrough Updates CUTLASS submodule pointer and extends SM120/121 GEMM support by adding a compile-time/runtime swap ab option, broadening CTA tile N from ..." (https://github.com/flashinfer-ai/flashinfer/pull/3152#issuecomment-4301646811)
- `2026-04-23T04:45:18Z` `inline` by `depaulmillz` `include/flashinfer/gemm/fp4_gemm_cutlass_template_sm120.h`:135; signals: cutlass, flashinfer, fp4, gemm, sm120; excerpt: "The newest push resolved this." (https://github.com/flashinfer-ai/flashinfer/pull/3152#discussion_r3128387284)
- `2026-04-24T00:34:05Z` `inline` by `coderabbitai` `tests/gemm/test_mm_mxfp8_sm120.py`:77; signals: benchmark, fp8, gemm, sm120; excerpt: "⚠️ Potential issue 🟡 Minor Assertion message is stale. The message says "Expected 5 tactics" but the assertion expects 10. Update the message for ..." (https://github.com/flashinfer-ai/flashinfer/pull/3152#discussion_r3134768373)
- `2026-04-23T04:45:10Z` `inline` by `depaulmillz` `include/flashinfer/gemm/mxfp8_gemm_template_sm120.h`:61; signals: flashinfer, fp8, gemm, sm120; excerpt: "The newest push resolved this." (https://github.com/flashinfer-ai/flashinfer/pull/3152#discussion_r3128386951)
- `2026-04-25T19:28:51Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, gemm, hang; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) flashinfer/gemm/gemm base.py ..." (https://github.com/flashinfer-ai/flashinfer/pull/3152#pullrequestreview-4176035145)
- `2026-04-28T18:27:25Z` `issue` by `bkryu`; signals: hang; excerpt: "Changes and internal CI LGTM. Will wait for another pair of eyes to review" (https://github.com/flashinfer-ai/flashinfer/pull/3152#issuecomment-4338039593)
