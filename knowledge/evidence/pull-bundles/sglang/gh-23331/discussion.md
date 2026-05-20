# PR Discussion Digest

- Source PR: [sgl-project/sglang#23331](https://github.com/sgl-project/sglang/pull/23331)
- Source page: `sources/prs/sglang/PR-23331.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-23331`
- Generated at: `2026-05-20T15:29:35.680699+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-21T06:34:46Z`
- Merged: `2026-05-19T22:09:50Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: AniZpZ, EanWang211123, Qiaolin-Yu, alphabetc1
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-11T02:22:56Z` `COMMENTED` by `alphabetc1` (https://github.com/sgl-project/sglang/pull/23331#pullrequestreview-4260406501)
- `2026-05-11T06:45:17Z` `COMMENTED` by `EanWang211123` (https://github.com/sgl-project/sglang/pull/23331#pullrequestreview-4261229000)
- `2026-05-11T16:21:47Z` `APPROVED` by `alphabetc1` (https://github.com/sgl-project/sglang/pull/23331#pullrequestreview-4265430498)
- `2026-05-19T22:09:13Z` `APPROVED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/23331#pullrequestreview-4323580912)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-11T02:22:56Z` `inline` by `alphabetc1` `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`:263; signals: attention, cache, hang; excerpt: "Can we change the input cache steps at the caller? Ignoring this parameter and introducing a new cache stride steps instead feels a bit ..." (https://github.com/sgl-project/sglang/pull/23331#discussion_r3216033388)
- `2026-05-11T06:45:17Z` `inline` by `EanWang211123` `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`:263; signals: attention, hang; excerpt: "yeah I considered this approach, but I found that this function is called in too many places. Changing all of the call sites might ..." (https://github.com/sgl-project/sglang/pull/23331#discussion_r3216804633)
- `2026-05-11T07:22:34Z` `issue` by `alphabetc1`; signals: latency, throughput; excerpt: "I test it on an h20(spec v2, adaptive vs baseline): Mode Score Latency Output throughput --- ---: ---: ---: Non-adaptive spec 0.900 4.009 s ..." (https://github.com/sgl-project/sglang/pull/23331#issuecomment-4418391186)
