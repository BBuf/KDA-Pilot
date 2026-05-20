# PR Discussion Digest

- Source PR: [sgl-project/sglang#21906](https://github.com/sgl-project/sglang/pull/21906)
- Source page: `sources/prs/sglang/PR-21906.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21906`
- Generated at: `2026-05-20T15:29:18.506970+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T04:36:35Z`
- Merged: `2026-04-03T21:19:13Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 5 (approved=2, changes_requested=1, commented=2)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, mmangkad
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-02T04:40:08Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21906#pullrequestreview-4048312546)
- `2026-04-02T04:53:57Z` `COMMENTED` by `mmangkad` (https://github.com/sgl-project/sglang/pull/21906#pullrequestreview-4048354123)
- `2026-04-02T05:27:49Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21906#pullrequestreview-4048441195)
- `2026-04-03T08:09:31Z` `CHANGES_REQUESTED` by `Fridge003` - Wait for CI runners pass (https://github.com/sgl-project/sglang/pull/21906#pullrequestreview-4054760732)
- `2026-04-03T21:19:03Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21906#pullrequestreview-4057335027)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa_backend.py`: 2 inline comment(s)
- `python/sglang/srt/utils/common.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-03T03:02:16Z` `issue` by `mmangkad`; signals: attention, block, flashinfer, triton; excerpt: "@mmangkad Can we set flashinfer as the default attention backend when it's on sm103 machine? @Fridge003 for most models SM103 already falls through to ..." (https://github.com/sgl-project/sglang/pull/21906#issuecomment-4181541672)
- `2026-04-02T04:40:03Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:1779; signals: attention, kernel; excerpt: "Is this kernel affected?" (https://github.com/sgl-project/sglang/pull/21906#discussion_r3025853406)
- `2026-04-02T04:53:57Z` `inline` by `mmangkad` `python/sglang/srt/layers/attention/nsa_backend.py`:1779; signals: attention, kernel; excerpt: "Likely yes. Same underlying kernel module, just a different op on it" (https://github.com/sgl-project/sglang/pull/21906#discussion_r3025888604)
- `2026-04-02T04:39:17Z` `inline` by `Fridge003` `python/sglang/srt/utils/common.py`:280; signals: sm100; excerpt: "Instead of is sm100 exact function, can we add a function is sm103 supported and skip all sm103 devices" (https://github.com/sgl-project/sglang/pull/21906#discussion_r3025851525)
- `2026-04-03T00:51:44Z` `issue` by `Fridge003`; signals: attention, flashinfer; excerpt: "@mmangkad Can we set flashinfer as the default attention backend when it's on sm103 machine?" (https://github.com/sgl-project/sglang/pull/21906#issuecomment-4181212578)
- `2026-04-03T08:09:31Z` `review` `CHANGES_REQUESTED` by `Fridge003`; signals: general review; excerpt: "Wait for CI runners pass" (https://github.com/sgl-project/sglang/pull/21906#pullrequestreview-4054760732)
- `2026-04-02T08:31:14Z` `issue` by `mmangkad`; signals: b200; excerpt: "B200 tests passed" (https://github.com/sgl-project/sglang/pull/21906#issuecomment-4175590571)
