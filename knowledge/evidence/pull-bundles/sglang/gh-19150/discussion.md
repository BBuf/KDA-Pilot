# PR Discussion Digest

- Source PR: [sgl-project/sglang#19150](https://github.com/sgl-project/sglang/pull/19150)
- Source page: `sources/prs/sglang/PR-19150.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19150`
- Generated at: `2026-05-20T15:28:47.227326+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-22T09:55:13Z`
- Merged: `2026-03-18T05:11:18Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: ispobock, kaixih, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-22T10:00:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates FlashInfer's gated delta rule decode pretranspose kernel as an optional backend for ... (https://github.com/sgl-project/sglang/pull/19150#pullrequestreview-3837181140)
- `2026-03-02T07:24:43Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19150#pullrequestreview-3874488152)
- `2026-03-12T03:38:40Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/19150#pullrequestreview-3933708660)
- `2026-03-18T05:10:32Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/19150#pullrequestreview-3965090539)

## Inline Comment Hotspots

- `python/sglang/srt/server_args.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-27T22:00:23Z` `issue` by `kaixih`; signals: attention, flashinfer, kernel, triton; excerpt: "Rebased to main to follow the new argument structure introduced by 18622 (linear attention backend refactor). The old --gdn-backend flag has been replaced by ..." (https://github.com/sgl-project/sglang/pull/19150#issuecomment-3975319771)
- `2026-03-02T07:24:43Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`:11; signals: attention, flashinfer, kernel; excerpt: "This is not necessarily for decode, it can be prefill in the future. Maybe revise the comment." (https://github.com/sgl-project/sglang/pull/19150#discussion_r2870907276)
- `2026-03-16T19:25:08Z` `issue` by `kaixih`; signals: b200, hang; excerpt: "@ispobock thx for the pointer. the tests pass on my b200 machine after I do this patch: this patch is needed even without my ..." (https://github.com/sgl-project/sglang/pull/19150#issuecomment-4070041940)
- `2026-03-09T13:36:42Z` `issue` by `kaixih`; signals: hopper; excerpt: "Also, cc. @xutizhou who has done the same thing for the hopper." (https://github.com/sgl-project/sglang/pull/19150#issuecomment-4023850343)
- `2026-03-16T16:13:02Z` `issue` by `kaixih`; signals: block; excerpt: "@ispobock any thing blocking the merge?" (https://github.com/sgl-project/sglang/pull/19150#issuecomment-4068869297)
- `2026-03-17T16:57:28Z` `issue` by `kaixih`; signals: flashinfer; excerpt: "Rebased and added one test for the flashinfer decode backend: To test: Results: @ispobock PTAL" (https://github.com/sgl-project/sglang/pull/19150#issuecomment-4076502300)
