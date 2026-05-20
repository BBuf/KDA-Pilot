# PR Discussion Digest

- Source PR: [sgl-project/sglang#25588](https://github.com/sgl-project/sglang/pull/25588)
- Source page: `sources/prs/sglang/PR-25588.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-25588`
- Generated at: `2026-05-20T15:29:51.841186+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-18T07:53:25Z`
- Merged: `2026-05-19T03:47:21Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: Abatom, ShangmingCai, liusy58
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-18T07:55:34Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces parallel video decoding for the torchcodec backend using a ThreadPoolExecutor, with the ... (https://github.com/sgl-project/sglang/pull/25588#pullrequestreview-4308272242)
- `2026-05-18T09:28:18Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/25588#pullrequestreview-4308913288)
- `2026-05-18T09:28:24Z` `APPROVED` by `ShangmingCai` - Others LGTM (https://github.com/sgl-project/sglang/pull/25588#pullrequestreview-4308914273)
- `2026-05-18T09:56:26Z` `COMMENTED` by `Abatom` (https://github.com/sgl-project/sglang/pull/25588#pullrequestreview-4309108474)
- `2026-05-18T10:40:47Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/25588#pullrequestreview-4309408769)
- `2026-05-18T12:25:41Z` `COMMENTED` by `Abatom` (https://github.com/sgl-project/sglang/pull/25588#pullrequestreview-4310100113)

## Inline Comment Hotspots

- `python/sglang/srt/utils/video_decoder.py`: 6 inline comment(s)

## High-Signal Discussion

- `2026-05-18T10:40:46Z` `inline` by `ShangmingCai` `python/sglang/srt/utils/video_decoder.py`:124; signals: benchmark, cache, perf, performance, race; excerpt: "Have you benchmarked the performance? Does it really need 32 that many here? We should choose a safer value. We find that many advanced ..." (https://github.com/sgl-project/sglang/pull/25588#discussion_r3258216593)
- `2026-05-18T09:28:18Z` `inline` by `ShangmingCai` `python/sglang/srt/utils/video_decoder.py`:124; signals: general review; excerpt: "Using os.cpu count() could be dangerous, I think using min() to limit the maximum value sounds reasonable." (https://github.com/sgl-project/sglang/pull/25588#discussion_r3257776065)
- `2026-05-18T09:56:26Z` `inline` by `Abatom` `python/sglang/srt/utils/video_decoder.py`:124; signals: general review; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/25588#discussion_r3257949983)
- `2026-05-18T12:25:41Z` `inline` by `Abatom` `python/sglang/srt/utils/video_decoder.py`:124; signals: general review; excerpt: "A one-hour video Threads E2E -- -- 128 26s 32 28s 16 32s 8 40s 4 56s 1 156s" (https://github.com/sgl-project/sglang/pull/25588#discussion_r3258854002)
