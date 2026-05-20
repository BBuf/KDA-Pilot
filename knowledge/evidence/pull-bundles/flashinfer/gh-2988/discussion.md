# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2988](https://github.com/flashinfer-ai/flashinfer/pull/2988)
- Source page: `sources/prs/flashinfer/PR-2988.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2988`
- Generated at: `2026-05-20T15:26:02.012806+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-06T04:46:57Z`
- Merged: `2026-04-08T16:27:16Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 5 (approved=2, changes_requested=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: PerkzZheng, bkryu, coderabbitai, johnnynunez, qsang-nv, saltyminty
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-06T04:52:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the FMHA kernels to ensure at least one token per CTA during ... (https://github.com/flashinfer-ai/flashinfer/pull/2988#pullrequestreview-4060377175)
- `2026-04-07T20:33:36Z` `APPROVED` by `saltyminty` (https://github.com/flashinfer-ai/flashinfer/pull/2988#pullrequestreview-4071121965)
- `2026-04-08T03:13:18Z` `CHANGES_REQUESTED` by `bkryu` - @PerkzZheng, please check the internal CI failures on SM120 cards on tests/attention/test trtllm gen attention.py I suspect it ... (https://github.com/flashinfer-ai/flashinfer/pull/2988#pullrequestreview-4072548163)
- `2026-04-08T09:05:57Z` `COMMENTED` by `qsang-nv` (https://github.com/flashinfer-ai/flashinfer/pull/2988#pullrequestreview-4074001210)
- `2026-04-08T16:27:06Z` `APPROVED` by `bkryu` - CI now LGTM. (https://github.com/flashinfer-ai/flashinfer/pull/2988#pullrequestreview-4076642940)

## Inline Comment Hotspots

- `tests/attention/test_trtllm_gen_attention.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-06T04:47:14Z` `issue` by `coderabbitai`; signals: attention, benchmark, dtype, flashinfer, fp4, hang, kernel, nvfp4; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : ..." (https://github.com/flashinfer-ai/flashinfer/pull/2988#issuecomment-4190391532)
- `2026-04-08T03:13:18Z` `review` `CHANGES_REQUESTED` by `bkryu`; signals: attention, sm120; excerpt: "@PerkzZheng, please check the internal CI failures on SM120 cards on tests/attention/test trtllm gen attention.py I suspect it has to do with XQA on ..." (https://github.com/flashinfer-ai/flashinfer/pull/2988#pullrequestreview-4072548163)
- `2026-04-08T09:05:57Z` `inline` by `qsang-nv` `tests/attention/test_trtllm_gen_attention.py`:1282; signals: attention, sm120; excerpt: "Verified head dim 256 has precision issues on main with sm120, will work on that later. Others LGTM." (https://github.com/flashinfer-ai/flashinfer/pull/2988#discussion_r3050296073)
- `2026-04-08T03:17:25Z` `issue` by `PerkzZheng`; signals: attention, sm120; excerpt: "@PerkzZheng, please check the internal CI failures on SM120 cards on tests/attention/test trtllm gen attention.py I suspect it has to do with XQA on ..." (https://github.com/flashinfer-ai/flashinfer/pull/2988#issuecomment-4203556130)
- `2026-04-06T09:50:11Z` `issue` by `PerkzZheng`; signals: general review; excerpt: "@saltyminty sorry for asking you again. it seems that all related tests have been passed ( Feel free to merge if everything looks good. ..." (https://github.com/flashinfer-ai/flashinfer/pull/2988#issuecomment-4191486190)
