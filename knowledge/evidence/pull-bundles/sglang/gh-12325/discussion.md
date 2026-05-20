# PR Discussion Digest

- Source PR: [sgl-project/sglang#12325](https://github.com/sgl-project/sglang/pull/12325)
- Source page: `sources/prs/sglang/PR-12325.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12325`
- Generated at: `2026-05-20T15:27:38.225546+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-29T07:51:48Z`
- Merged: `2025-10-29T18:51:55Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, voipmonitor, weireweire
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-29T07:55:20Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12325#pullrequestreview-3392065182)
- `2025-10-29T07:55:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces performance optimizations for the Deepseek model on sm120 hardware by leveraging the ... (https://github.com/sgl-project/sglang/pull/12325#pullrequestreview-3392065665)
- `2025-10-29T08:02:43Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/12325#pullrequestreview-3392090858)
- `2025-10-29T08:04:59Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/12325#pullrequestreview-3392097144)
- `2025-10-29T08:10:53Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12325#pullrequestreview-3392113770)
- `2025-10-29T08:14:09Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/12325#pullrequestreview-3392126373)
- `2025-10-29T08:18:28Z` `APPROVED` by `Fridge003` - LGTM (https://github.com/sgl-project/sglang/pull/12325#pullrequestreview-3392138954)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 3 inline comment(s)
- `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-29T10:06:50Z` `issue` by `voipmonitor`; signals: attention, cutlass, flashinfer, hang, mla, sm120; excerpt: "@voipmonitor "auto" also result to "fa2" inside flashinfer, I just tested fa2 and followed the cutlass way, let me change it. Actually I think ..." (https://github.com/sgl-project/sglang/pull/12325#issuecomment-3460700857)
- `2025-10-29T09:58:19Z` `issue` by `weireweire`; signals: cutlass, flashinfer, hang, sm120; excerpt: "@voipmonitor "auto" also result to "fa2" inside flashinfer, I just tested fa2 and followed the cutlass way, let me change it. Actually I think ..." (https://github.com/sgl-project/sglang/pull/12325#issuecomment-3460669989)
- `2025-10-29T08:04:59Z` `inline` by `weireweire` `python/sglang/srt/models/deepseek_v2.py`:323; signals: flashinfer, hang, sm120; excerpt: "so the issue is sm120 don't support non-ragged and have to use the flag. change flashinfer backend can solve" (https://github.com/sgl-project/sglang/pull/12325#discussion_r2472062432)
- `2025-10-29T08:10:50Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:246; signals: attention, flashinfer, mla; excerpt: "We can move this to else branch" (https://github.com/sgl-project/sglang/pull/12325#discussion_r2472075110)
- `2025-10-29T08:14:09Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:246; signals: attention, flashinfer, mla; excerpt: "done" (https://github.com/sgl-project/sglang/pull/12325#discussion_r2472082775)
- `2025-10-29T09:31:19Z` `issue` by `voipmonitor`; signals: cutlass, fp8, sm120; excerpt: "@weireweire why not elif is sm120 supported(): self.fmha backend = "auto" ? but forcing fa2? if it is "auto" it still works - how ..." (https://github.com/sgl-project/sglang/pull/12325#issuecomment-3460571208)
- `2025-10-29T07:55:13Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:323; signals: flashinfer, mla; excerpt: "We can't modify this line, otherwise flashinfer mla disable ragged will lose control of flashinfer backend. flashinfer mla disable ragged is false by default ..." (https://github.com/sgl-project/sglang/pull/12325#discussion_r2472040288)
- `2025-10-29T08:02:43Z` `inline` by `weireweire` `python/sglang/srt/models/deepseek_v2.py`:323; signals: general review; excerpt: "uh, make sense, reverted" (https://github.com/sgl-project/sglang/pull/12325#discussion_r2472057539)
