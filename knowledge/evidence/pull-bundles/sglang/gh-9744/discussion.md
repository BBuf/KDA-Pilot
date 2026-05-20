# PR Discussion Digest

- Source PR: [sgl-project/sglang#9744](https://github.com/sgl-project/sglang/pull/9744)
- Source page: `sources/prs/sglang/PR-9744.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9744`
- Generated at: `2026-05-20T15:31:39.826677+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-28T07:34:21Z`
- Merged: `2026-03-19T05:19:48Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 4 (approved=1, changes_requested=1, commented=2)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: blzheng, mingfeima
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-11T08:07:34Z` `CHANGES_REQUESTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/9744#pullrequestreview-3209666329)
- `2025-09-23T02:16:02Z` `COMMENTED` by `blzheng` (https://github.com/sgl-project/sglang/pull/9744#pullrequestreview-3255820575)
- `2025-09-23T02:51:58Z` `COMMENTED` by `blzheng` (https://github.com/sgl-project/sglang/pull/9744#pullrequestreview-3255865260)
- `2025-10-11T02:02:19Z` `APPROVED` by `mingfeima` - generally LGTM, just some minor issues to address. (https://github.com/sgl-project/sglang/pull/9744#pullrequestreview-3326439401)

## Inline Comment Hotspots

- `sgl-kernel/csrc/cpu/bmm.cpp`: 3 inline comment(s)
- `sgl-kernel/csrc/cpu/gemm_fp8.cpp`: 2 inline comment(s)
- `sgl-kernel/csrc/cpu/gemm.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-23T02:16:01Z` `inline` by `blzheng` `sgl-kernel/csrc/cpu/gemm_fp8.cpp`:540; signals: block, fp8, gemm, kernel; excerpt: "The main difference between tinygemm kernel and tinygemm kernel2 lies in scale. - tinygemm kernel: block-wise scale - tinygemm kernel2: a single scale" (https://github.com/sgl-project/sglang/pull/9744#discussion_r2370828737)
- `2025-09-11T08:07:07Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/gemm_fp8.cpp`:540; signals: fp8, gemm, kernel; excerpt: "what's the difference with tinygemm kernel" (https://github.com/sgl-project/sglang/pull/9744#discussion_r2339311053)
- `2025-10-11T02:00:05Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/gemm.h`:269; signals: block, gemm, kernel; excerpt: "add a comment this one is for per tensor quantization, and the last one is for block quantization" (https://github.com/sgl-project/sglang/pull/9744#discussion_r2422370220)
- `2025-09-11T08:04:22Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/bmm.cpp`:98; signals: hang, kernel; excerpt: "change this to parallel 2d" (https://github.com/sgl-project/sglang/pull/9744#discussion_r2339296735)
- `2025-09-23T02:51:57Z` `inline` by `blzheng` `sgl-kernel/csrc/cpu/bmm.cpp`:98; signals: kernel; excerpt: "Done." (https://github.com/sgl-project/sglang/pull/9744#discussion_r2370860446)
- `2025-10-11T01:55:48Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/bmm.cpp`:107; signals: kernel; excerpt: "use int64 t, since all the rest are int64 t" (https://github.com/sgl-project/sglang/pull/9744#discussion_r2422368989)
