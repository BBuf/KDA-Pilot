# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2376](https://github.com/flashinfer-ai/flashinfer/pull/2376)
- Source page: `sources/prs/flashinfer/PR-2376.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2376`
- Generated at: `2026-05-20T15:24:41.143382+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-20T00:18:26Z`
- Merged: `2026-01-27T19:01:00Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 17
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=9, outdated=3
- Human participants with discussion text: aleozlx, coderabbitai, jimmyzho, raayandhar, sricketts
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-20T00:20:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds a cuDNN backend for BF16 batched GEMM, which is a great feature. ... (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3679914829)
- `2026-01-20T00:30:21Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3679929041)
- `2026-01-23T02:49:15Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) flashinfer/gemm/gemm base.py (1) ... (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3695442485)
- `2026-01-23T03:09:11Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Fix all issues with AI agents (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3695483119)
- `2026-01-23T03:14:07Z` `COMMENTED` by `raayandhar` (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3695483972)
- `2026-01-23T03:20:30Z` `COMMENTED` by `raayandhar` (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3695506407)
- `2026-01-26T17:26:55Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3707137448)
- `2026-01-26T17:29:23Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3707146265)
- `2026-01-26T17:31:46Z` `APPROVED` by `aleozlx` - lgtm (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3707154503)
- `2026-01-26T17:31:52Z` `COMMENTED` by `raayandhar` (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3707154821)
- `2026-01-26T17:37:34Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3707177928)
- `2026-01-27T00:13:30Z` `APPROVED` by `jimmyzho` - lgtm! (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3708587928)

## Inline Comment Hotspots

- `flashinfer/gemm/gemm_base.py`: 9 inline comment(s)
- `tests/gemm/test_bmm_bf16.py`: 7 inline comment(s)
- `tests/gemm/test_mm_bf16.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-23T03:20:27Z` `inline` by `raayandhar` `tests/gemm/test_bmm_bf16.py`:25; signals: b200, bf16, dtype, failing, gemm, hang, sm100; excerpt: "I don't know why, but for some reason on SM103 this test was failing (when we had fp16 out dtype). This was with my ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#discussion_r2719434376)
- `2026-01-20T00:18:37Z` `issue` by `coderabbitai`; signals: autotune, bf16, cute, cutlass, flashinfer, gemm, hang; excerpt: "📝 Walkthrough Walkthrough Adds cuDNN-backed bfloat16 MM/BMM execution paths and runners, integrates "cudnn" and "auto" into backend selection and heuristics, validates optional outputs and ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#issuecomment-3770515849)
- `2026-01-23T02:49:15Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cutlass, flashinfer, gemm, hang; excerpt: "Actionable comments posted: 1 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) flashinfer/gemm/gemm base.py (1) 185-186: Remove duplicate compute-capability decorator. Two ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3695442485)
- `2026-01-20T00:30:20Z` `inline` by `coderabbitai` `tests/gemm/test_bmm_bf16.py`:39; signals: benchmark, bf16, cute, flashinfer, gemm; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 972 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#discussion_r2706382297)
- `2026-01-20T00:30:21Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, flashinfer, fp8, gemm; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#pullrequestreview-3679929041)
- `2026-01-23T02:49:14Z` `inline` by `coderabbitai` `tests/gemm/test_mm_bf16.py`:38; signals: bf16, cute, flashinfer, gemm; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 96 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#discussion_r2719383271)
- `2026-01-20T00:21:26Z` `issue` by `raayandhar`; signals: benchmark, bf16, fp8, gemm; excerpt: "I tried getting cuDNN to work with mm bf16 but it seems like it wasn't able to find a valid plan? I'm looking into ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#issuecomment-3770520810)
- `2026-01-23T03:09:11Z` `inline` by `coderabbitai` `flashinfer/gemm/gemm_base.py`:186; signals: benchmark, flashinfer, gemm; excerpt: "⚠️ Potential issue 🟡 Minor Duplicate decorator detected. The @supported compute capability([100, 103]) decorator is applied twice. Remove one instance. Proposed fix 📝 Committable ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#discussion_r2719417296)
- `2026-01-23T03:17:39Z` `issue` by `raayandhar`; signals: b200, hang, sm100; excerpt: "SM103 results: BMM: MM: Have not tested on B200 (SM100) yet with most recent changes. The prices to rent are super high today." (https://github.com/flashinfer-ai/flashinfer/pull/2376#issuecomment-3787960103)
- `2026-01-26T17:29:23Z` `inline` by `aleozlx` `tests/gemm/test_bmm_bf16.py`:25; signals: bf16, gemm; excerpt: "did you get a not supported error or result mismatch error? then can we file this as an github issue and mention in the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#discussion_r2728553180)
- `2026-01-26T17:31:51Z` `inline` by `raayandhar` `tests/gemm/test_bmm_bf16.py`:25; signals: bf16, gemm; excerpt: "iirc it was a cuDNN can't find an execution plan error but I can re-test later today and find out, it's possible it has ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#discussion_r2728560976)
- `2026-01-26T17:37:34Z` `inline` by `aleozlx` `tests/gemm/test_bmm_bf16.py`:25; signals: bf16, gemm; excerpt: "i see try exporting env vars CUDNN LOGLEVEL DBG=2 CUDNN LOGDEST DBG=somefile.log this may capture more detailed error reason if it's not able to ..." (https://github.com/flashinfer-ai/flashinfer/pull/2376#discussion_r2728581199)
