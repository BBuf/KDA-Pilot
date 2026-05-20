# PR Discussion Digest

- Source PR: [sgl-project/sglang#19003](https://github.com/sgl-project/sglang/pull/19003)
- Source page: `sources/prs/sglang/PR-19003.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19003`
- Generated at: `2026-05-20T15:28:45.336157+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-19T07:31:19Z`
- Merged: `2026-02-24T11:49:23Z`

## Discussion Counts

- Issue comments: 27
- Review submissions: 22 (approved=2, changes_requested=1, commented=19)
- Inline review comments: 22
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=9, outdated=8
- Human participants with discussion text: BBuf, JustinTong0323, mickqian, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-19T07:33:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces FlashInfer CUDNN prefill as a new backend for Vision Transformer attention, which ... (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3823941923)
- `2026-02-19T12:18:30Z` `CHANGES_REQUESTED` by `JustinTong0323` - Could you also resolve 3 bugs in devin review? They are all reasonable imo. (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3825313267)
- `2026-02-19T13:55:15Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3826077779)
- `2026-02-19T13:55:28Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3826078812)
- `2026-02-20T02:03:15Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3829462077)
- `2026-02-20T14:11:16Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3832225317)
- `2026-02-21T01:58:19Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3834807431)
- `2026-02-21T03:39:13Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3834987389)
- `2026-02-21T03:40:17Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3834989193)
- `2026-02-21T04:16:35Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835021271)
- `2026-02-21T05:03:21Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835053722)
- `2026-02-21T05:05:45Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835055005)
- `2026-02-21T05:16:10Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835061439)
- `2026-02-21T05:17:16Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835062000)
- `2026-02-21T06:13:56Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835127338)
- `2026-02-21T10:47:11Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835476432)
- `2026-02-21T10:50:31Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835477884)
- `2026-02-21T10:50:51Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835478015)
- `2026-02-21T11:13:34Z` `APPROVED` by `JustinTong0323` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835488553)
- `2026-02-21T14:32:54Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3835601954)
- `2026-02-22T00:13:30Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3836275959)
- `2026-02-22T02:06:24Z` `APPROVED` by `BBuf` - Good job. Let's run ci. (https://github.com/sgl-project/sglang/pull/19003#pullrequestreview-3836450467)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/vision.py`: 12 inline comment(s)
- `python/sglang/srt/models/qwen3_vl.py`: 10 inline comment(s)

## High-Signal Discussion

- `2026-02-19T11:45:47Z` `inline` by `JustinTong0323` `python/sglang/srt/layers/attention/vision.py`:637; signals: attention, flashinfer; excerpt: "use flashinfer as it's unified naming with --attention-backend" (https://github.com/sgl-project/sglang/pull/19003#discussion_r2827353407)
- `2026-02-19T13:55:28Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/vision.py`:637; signals: attention, hang; excerpt: "Sure, will change it." (https://github.com/sgl-project/sglang/pull/19003#discussion_r2828041155)
- `2026-02-21T05:17:16Z` `inline` by `BBuf` `python/sglang/srt/layers/attention/vision.py`:657; signals: attention, flashinfer; excerpt: "Maybe flashinfer cudnn is better?" (https://github.com/sgl-project/sglang/pull/19003#discussion_r2835847159)
- `2026-02-21T14:32:55Z` `inline` by `BBuf` `python/sglang/srt/layers/attention/vision.py`:71; signals: attention, cuda; excerpt: "cuDNN graph means CUDA Graph?" (https://github.com/sgl-project/sglang/pull/19003#discussion_r2836235435)
- `2026-02-21T10:51:13Z` `issue` by `yuan-luo`; signals: accuracy, regression; excerpt: "Could you add the mmmu accuracy before and after this PR to ensure no regression? @JustinTong0323 I updated mmmu acc in the PR description, ..." (https://github.com/sgl-project/sglang/pull/19003#issuecomment-3938598984)
- `2026-02-19T13:55:15Z` `inline` by `yuan-luo` `python/sglang/srt/models/qwen3_vl.py`:508; signals: flashinfer; excerpt: "This function only applies to qwen3 vl. For Qwen2.5-VL and some other VLMs we need to adapt it's own function as the flashinfer cudnn ..." (https://github.com/sgl-project/sglang/pull/19003#discussion_r2828040134)
- `2026-02-21T03:03:36Z` `issue` by `JustinTong0323`; signals: accuracy, regression; excerpt: "Could you add the mmmu accuracy before and after this PR to ensure no regression?" (https://github.com/sgl-project/sglang/pull/19003#issuecomment-3938029815)
- `2026-02-20T02:03:15Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/vision.py`:637; signals: attention; excerpt: "done." (https://github.com/sgl-project/sglang/pull/19003#discussion_r2831009167)
- `2026-02-21T01:58:19Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/vision.py`:486; signals: attention; excerpt: "Fixed." (https://github.com/sgl-project/sglang/pull/19003#discussion_r2835686984)
- `2026-02-21T03:39:13Z` `inline` by `BBuf` `python/sglang/srt/layers/attention/vision.py`:509; signals: attention; excerpt: "Should we try to avoid this sync?" (https://github.com/sgl-project/sglang/pull/19003#discussion_r2835777578)
- `2026-02-21T10:47:11Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/vision.py`:657; signals: attention; excerpt: "Updated." (https://github.com/sgl-project/sglang/pull/19003#discussion_r2836076371)
- `2026-02-21T10:50:50Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/vision.py`:509; signals: attention; excerpt: "Refactored and removed this sync." (https://github.com/sgl-project/sglang/pull/19003#discussion_r2836078917)
