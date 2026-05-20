# PR Discussion Digest

- Source PR: [sgl-project/sglang#11866](https://github.com/sgl-project/sglang/pull/11866)
- Source page: `sources/prs/sglang/PR-11866.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11866`
- Generated at: `2026-05-20T15:27:29.909051+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-20T14:33:00Z`
- Merged: `2025-10-23T09:29:02Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: FlamingoPg, ispobock, netanel-haber, yizhang2077
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-20T14:35:50Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for FP8 and NVFP4 variants of the NVIDIA-Nemotron-Nano-9B-v2 model, which is ... (https://github.com/sgl-project/sglang/pull/11866#pullrequestreview-3356728073)
- `2025-10-22T07:35:26Z` `APPROVED` by `yizhang2077` - LGTM for model/test part (https://github.com/sgl-project/sglang/pull/11866#pullrequestreview-3364059104)
- `2025-10-22T14:38:19Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/11866#pullrequestreview-3366124983)
- `2025-10-22T15:16:52Z` `COMMENTED` by `netanel-haber` (https://github.com/sgl-project/sglang/pull/11866#pullrequestreview-3366310162)
- `2025-10-23T09:14:27Z` `APPROVED` by `FlamingoPg` - LGTM for quantization (https://github.com/sgl-project/sglang/pull/11866#pullrequestreview-3368962469)
- `2025-10-23T09:28:46Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/11866#pullrequestreview-3369015457)

## Inline Comment Hotspots

- `test/srt/models/test_nvidia_nemotron_nano_v2.py`: 3 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-22T15:16:52Z` `inline` by `netanel-haber` `test/srt/models/test_nvidia_nemotron_nano_v2.py`:55; signals: blackwell, nan; excerpt: "There is only a 4-gpu blackwell setup, is it marginal to add it to that run, or is that wasteful? In case it's wasteful, ..." (https://github.com/sgl-project/sglang/pull/11866#discussion_r2452461335)
- `2025-10-23T09:28:46Z` `inline` by `ispobock` `test/srt/models/test_nvidia_nemotron_nano_v2.py`:55; signals: blackwell, nan; excerpt: "The blackwell runner seems have some environment issues recently. We will fix and then setup it later." (https://github.com/sgl-project/sglang/pull/11866#discussion_r2454495501)
- `2025-10-22T14:38:14Z` `inline` by `ispobock` `test/srt/models/test_nvidia_nemotron_nano_v2.py`:55; signals: blackwell, nan; excerpt: "Can we move this model test to blackwell gpu runner to make sure it's covered in the CI?" (https://github.com/sgl-project/sglang/pull/11866#discussion_r2452335305)
