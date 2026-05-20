# PR Discussion Digest

- Source PR: [sgl-project/sglang#24933](https://github.com/sgl-project/sglang/pull/24933)
- Source page: `sources/prs/sglang/PR-24933.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-24933`
- Generated at: `2026-05-20T15:29:45.682905+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-11T03:38:06Z`
- Merged: `2026-05-18T16:15:08Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: DarkSharpness, HaiShaw, kkHuang-amd
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-15T09:02:49Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/24933#pullrequestreview-4296783976)
- `2026-05-15T09:04:02Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/24933#pullrequestreview-4296841084)
- `2026-05-15T09:23:01Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/24933#pullrequestreview-4296974549)
- `2026-05-18T16:05:07Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/24933#pullrequestreview-4311801296)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/deepseek_v4.py`: 3 inline comment(s)
- `python/sglang/srt/layers/attention/hip_flash_mla.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/dsv4/compressor.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-15T08:57:42Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/deepseek_v4.py`:1059; signals: bf16, kernel; excerpt: "dsv4 requires bf16 in and fp32 out (fp32 acc). I'm not sure whether bf16 in bf16 out then cast to fp32 might cause some ..." (https://github.com/sgl-project/sglang/pull/24933#discussion_r3247040991)
- `2026-05-15T09:00:08Z` `inline` by `DarkSharpness` `python/sglang/srt/layers/attention/hip_flash_mla.py`; signals: attention, mla; excerpt: "Do we still need this? It seems to be mainly for debug purpose (or maybe rename this file to be more descriptive. e.g. hip ..." (https://github.com/sgl-project/sglang/pull/24933#discussion_r3247056168)
- `2026-05-15T09:04:01Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/attention/hip_flash_mla.py`; signals: attention, mla; excerpt: "Yes, I can fix it with dedicated to run on ROCm" (https://github.com/sgl-project/sglang/pull/24933#discussion_r3247077886)
- `2026-05-15T08:59:14Z` `inline` by `DarkSharpness` `python/sglang/srt/layers/attention/dsv4/compressor.py`; signals: attention; excerpt: "This diff seems to be too large. Should we move this to another file (e.g. compress hip.py) following the same interface, and import this ..." (https://github.com/sgl-project/sglang/pull/24933#discussion_r3247050675)
- `2026-05-15T08:55:58Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/deepseek_v4.py`:665; signals: kernel; excerpt: "maybe move this to the beginning of this file?" (https://github.com/sgl-project/sglang/pull/24933#discussion_r3247031438)
- `2026-05-15T09:23:01Z` `inline` by `kkHuang-amd` `python/sglang/jit_kernel/deepseek_v4.py`:1059; signals: kernel; excerpt: "From our testing, not see precision degradation issue" (https://github.com/sgl-project/sglang/pull/24933#discussion_r3247182047)
