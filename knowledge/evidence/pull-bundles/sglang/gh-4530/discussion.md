# PR Discussion Digest

- Source PR: [sgl-project/sglang#4530](https://github.com/sgl-project/sglang/pull/4530)
- Source page: `sources/prs/sglang/PR-4530.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4530`
- Generated at: `2026-05-20T15:30:11.272529+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-18T03:07:28Z`
- Merged: `2025-03-29T18:51:46Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 4 (commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: kgosal03, lambert0312, qingquansong, wuxun-zhang, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-03-18T06:39:18Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/4530#pullrequestreview-2693177643)
- `2025-03-25T05:37:56Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4530#pullrequestreview-2712435479)
- `2025-03-25T06:04:54Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/4530#pullrequestreview-2712477484)

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/moe_fused_gate.cu`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/topk.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-03-18T06:39:18Z` `inline` by `qingquansong` `sgl-kernel/csrc/moe/moe_fused_gate.cu`:58; signals: cutlass, dtype, hang, kernel, moe; excerpt: "@yiakwy-xpu-ml-framework-team I temporarily put this here to differentiate between cutlass one and native array with torch dtype. Feel free to let me know what ..." (https://github.com/sgl-project/sglang/pull/4530#discussion_r2000311909)
- `2025-03-25T05:37:56Z` `inline` by `zhyncs` `python/sglang/srt/layers/moe/topk.py`:132; signals: kernel, moe; excerpt: "I think the Python-related part should be updated after sgl-kernel releases a new version. Can you split it into two PRs? Thank you." (https://github.com/sgl-project/sglang/pull/4530#discussion_r2011345211)
- `2025-03-18T21:10:34Z` `issue` by `qingquansong`; signals: flashinfer, kernel; excerpt: "It seems that it is not compatible with Flashinfer, and is still under experimentation. When using Flashinfer, the following error is reported: Hey @lambert0312 ..." (https://github.com/sgl-project/sglang/pull/4530#issuecomment-2734738872)
- `2025-03-18T23:44:57Z` `issue` by `lambert0312`; signals: flashinfer, kernel; excerpt: "Hey @lambert0312 👀 is this error related to this kernel specifically and does not show up with the original torch kernel? Do you happen ..." (https://github.com/sgl-project/sglang/pull/4530#issuecomment-2734965762)
- `2025-03-19T00:15:38Z` `issue` by `qingquansong`; signals: flashinfer, kernel; excerpt: "Hey @lambert0312 👀 is this error related to this kernel specifically and does not show up with the original torch kernel? Do you happen ..." (https://github.com/sgl-project/sglang/pull/4530#issuecomment-2734998092)
- `2025-03-25T06:04:54Z` `inline` by `qingquansong` `python/sglang/srt/layers/moe/topk.py`:132; signals: moe; excerpt: "Of course! 🫡" (https://github.com/sgl-project/sglang/pull/4530#discussion_r2011372214)
- `2025-03-18T11:32:06Z` `issue` by `lambert0312`; signals: flashinfer; excerpt: "It seems that it is not compatible with Flashinfer, and is still under experimentation. When using Flashinfer, the following error is reported:" (https://github.com/sgl-project/sglang/pull/4530#issuecomment-2732869267)
