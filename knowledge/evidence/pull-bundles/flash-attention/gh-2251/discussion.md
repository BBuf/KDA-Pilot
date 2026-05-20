# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2251](https://github.com/Dao-AILab/flash-attention/pull/2251)
- Source page: `sources/prs/flash-attention/PR-2251.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2251`
- Generated at: `2026-05-20T15:16:48.366365+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-11T22:37:02Z`
- Merged: `2026-02-23T21:27:04Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: henrylhtsang, jayhshah, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T21:25:58Z` `APPROVED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2251#pullrequestreview-3843618472)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-02-12T02:27:58Z` `issue` by `tridao`; signals: hang; excerpt: "Yeah i realized that sometimes people use negative window size. In FA3 that wouldn't work at all. In FA4 it would work. But now ..." (https://github.com/Dao-AILab/flash-attention/pull/2251#issuecomment-3888321772)
- `2026-02-12T04:15:00Z` `issue` by `henrylhtsang`; signals: general review; excerpt: "@tridao Thanks for the response! I modified the PR to do that and remove local enum from the tests. Running the tests overnight so ..." (https://github.com/Dao-AILab/flash-attention/pull/2251#issuecomment-3888581788)
- `2026-02-12T06:20:53Z` `issue` by `jayhshah`; signals: general review; excerpt: "Is there a need to remove support for negative window sizes? I had added and checked that due to a request." (https://github.com/Dao-AILab/flash-attention/pull/2251#issuecomment-3888904494)
- `2026-02-12T06:35:57Z` `issue` by `jayhshah`; signals: general review; excerpt: "How about if window size[0] and window size[1] are both provided, we check that the inequality is satisfied, and if it is not, set ..." (https://github.com/Dao-AILab/flash-attention/pull/2251#issuecomment-3888948286)
- `2026-02-12T17:57:32Z` `issue` by `henrylhtsang`; signals: general review; excerpt: "How about if window size[0] and window size[1] are both provided, we check that the inequality is satisfied, and if it is not, set ..." (https://github.com/Dao-AILab/flash-attention/pull/2251#issuecomment-3892505236)
- `2026-02-12T17:57:52Z` `issue` by `henrylhtsang`; signals: general review; excerpt: "Is there a need to remove support for negative window sizes? I had added and checked that due to a request. I think people ..." (https://github.com/Dao-AILab/flash-attention/pull/2251#issuecomment-3892507378)
