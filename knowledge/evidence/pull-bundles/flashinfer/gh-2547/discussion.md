# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2547](https://github.com/flashinfer-ai/flashinfer/pull/2547)
- Source page: `sources/prs/flashinfer/PR-2547.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2547`
- Generated at: `2026-05-20T15:25:02.017870+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-12T17:33:39Z`
- Merged: `2026-02-19T02:15:40Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 9
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: DomBrown, PerkzZheng, bkryu, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-12T17:45:52Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3792620218)
- `2026-02-12T17:52:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for skip-softmax attention for MLA and DeepSeek paths by adding a ... (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3792667928)
- `2026-02-12T18:00:19Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3792718112)
- `2026-02-12T18:00:57Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3792722582)
- `2026-02-13T02:38:47Z` `APPROVED` by `PerkzZheng` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3794746596)
- `2026-02-13T09:34:24Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3796115483)
- `2026-02-13T09:39:23Z` `COMMENTED` by `PerkzZheng` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3796147161)
- `2026-02-13T10:51:59Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3796611024)
- `2026-02-13T16:52:47Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3798349517)
- `2026-02-19T02:15:34Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3823161118)

## Inline Comment Hotspots

- `csrc/trtllm_fmha_kernel_launcher.cu`: 5 inline comment(s)
- `flashinfer/mla.py`: 2 inline comment(s)
- `flashinfer/prefill.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-12T17:33:50Z` `issue` by `coderabbitai`; signals: attention, benchmark, cache, cuda, dtype, flashinfer, fp8, gemm; excerpt: "📝 Walkthrough Walkthrough Adds optional skip-softmax controls (skip softmax threshold scale factor, skips softmax) and threads them from Python APIs (prefill/MLA) through TRTLLM wrappers ..." (https://github.com/flashinfer-ai/flashinfer/pull/2547#issuecomment-3892347598)
- `2026-02-12T17:45:52Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, mla, tma; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) flashinfer/mla.py (1) ..." (https://github.com/flashinfer-ai/flashinfer/pull/2547#pullrequestreview-3792620218)
- `2026-02-13T09:34:24Z` `inline` by `DomBrown` `csrc/trtllm_fmha_kernel_launcher.cu`:569; signals: hang, kernel; excerpt: "It would be a small optimisation to do that, yes. I haven't though because we are currently testing the kernel with threshold zero, and ..." (https://github.com/flashinfer-ai/flashinfer/pull/2547#discussion_r2803222047)
- `2026-02-13T10:51:58Z` `inline` by `DomBrown` `csrc/trtllm_fmha_kernel_launcher.cu`:569; signals: hang, kernel; excerpt: "I will give it a try. If the tests pass I'll push out the change (and I guess we will need to trigger CI ..." (https://github.com/flashinfer-ai/flashinfer/pull/2547#discussion_r2803599589)
- `2026-02-12T18:00:56Z` `inline` by `DomBrown` `flashinfer/mla.py`:561; signals: flashinfer, mla; excerpt: "The link is valid." (https://github.com/flashinfer-ai/flashinfer/pull/2547#discussion_r2800307755)
- `2026-02-13T09:39:23Z` `inline` by `PerkzZheng` `csrc/trtllm_fmha_kernel_launcher.cu`:569; signals: kernel; excerpt: "okay, we can probably try a extremely small value in the tests like 1e-30. or we should document it clearly. Thanks!" (https://github.com/flashinfer-ai/flashinfer/pull/2547#discussion_r2803245770)
- `2026-02-12T18:00:19Z` `inline` by `DomBrown` `flashinfer/prefill.py`:3482; signals: flashinfer; excerpt: "The link is valid." (https://github.com/flashinfer-ai/flashinfer/pull/2547#discussion_r2800304813)
- `2026-02-13T02:38:41Z` `inline` by `PerkzZheng` `csrc/trtllm_fmha_kernel_launcher.cu`:569; signals: kernel; excerpt: "should we also check whether it is zero or not ? or this has been done somewhere else." (https://github.com/flashinfer-ai/flashinfer/pull/2547#discussion_r2801991265)
- `2026-02-13T16:52:47Z` `inline` by `DomBrown` `csrc/trtllm_fmha_kernel_launcher.cu`:569; signals: kernel; excerpt: "Done. Tests look green." (https://github.com/flashinfer-ai/flashinfer/pull/2547#discussion_r2805160407)
