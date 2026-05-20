# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#3050](https://github.com/flashinfer-ai/flashinfer/pull/3050)
- Source page: `sources/prs/flashinfer/PR-3050.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-3050`
- Generated at: `2026-05-20T15:26:13.357332+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-13T19:08:48Z`
- Merged: `2026-04-21T05:37:42Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 5 (approved=3, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: bkryu, bobboli, coderabbitai, jimmyzho, yongwww
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-13T19:12:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a warning for FP8 (e4m3) kernels known to hang on SM90 architectures ... (https://github.com/flashinfer-ai/flashinfer/pull/3050#pullrequestreview-4101275719)
- `2026-04-13T19:12:13Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) tests/attention/test fmha v2 prefill.py (1) 785-788: Prefer explicit skipped params over commented-out cases. Using ... (https://github.com/flashinfer-ai/flashinfer/pull/3050#pullrequestreview-4101276751)
- `2026-04-14T17:28:19Z` `APPROVED` by `bobboli` (https://github.com/flashinfer-ai/flashinfer/pull/3050#pullrequestreview-4107918693)
- `2026-04-15T17:26:16Z` `APPROVED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/3050#pullrequestreview-4115519800)
- `2026-04-15T17:30:20Z` `APPROVED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/3050#pullrequestreview-4115542328)

## Inline Comment Hotspots

- `tests/attention/test_fmha_v2_prefill.py`: 2 inline comment(s)
- `flashinfer/prefill.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-13T19:09:04Z` `issue` by `coderabbitai`; signals: attention, dtype, flashinfer, fp8, hang, sm90; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : ..." (https://github.com/flashinfer-ai/flashinfer/pull/3050#issuecomment-4238943023)
- `2026-04-13T19:12:13Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, flashinfer, fp8, hang; excerpt: "🧹 Nitpick comments (1) tests/attention/test fmha v2 prefill.py (1) 785-788: Prefer explicit skipped params over commented-out cases. Using pytest.param(..., marks=pytest.mark.skip(...)) keeps FP8 cases visible ..." (https://github.com/flashinfer-ai/flashinfer/pull/3050#pullrequestreview-4101276751)
- `2026-04-14T17:27:48Z` `inline` by `bobboli` `tests/attention/test_fmha_v2_prefill.py`:785; signals: attention; excerpt: "Can we add pytest.skip in the function body instead of commenting out test cases, which is easy to get ignored when re-enabling tests in ..." (https://github.com/flashinfer-ai/flashinfer/pull/3050#discussion_r3081275022)
- `2026-04-14T17:27:57Z` `inline` by `bobboli` `tests/attention/test_fmha_v2_prefill.py`:861; signals: attention; excerpt: "Same here." (https://github.com/flashinfer-ai/flashinfer/pull/3050#discussion_r3081275767)
