# PR Discussion Digest

- Source PR: [pytorch/pytorch#135869](https://github.com/pytorch/pytorch/pull/135869)
- Source page: `sources/prs/pytorch/PR-135869.md`
- Evidence bundle: `evidence/pull-bundles/pytorch/gh-135869`
- Generated at: `2026-05-20T15:26:54.853042+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-09-12T16:15:28Z`
- Merged: `2024-09-30T20:14:55Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 4 (approved=4)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: atalman, jithunnair-amd, kit1980, malfet, pruthvistony
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2024-09-12T17:05:51Z` `APPROVED` by `pruthvistony` - LGTM. Cherry-pick from main branch. Part of continued effort to improve AOTriton on ROCm. (https://github.com/pytorch/pytorch/pull/135869#pullrequestreview-2300933065)
- `2024-09-25T14:53:30Z` `APPROVED` by `jithunnair-amd` (https://github.com/pytorch/pytorch/pull/135869#pullrequestreview-2328545331)
- `2024-09-27T18:29:25Z` `APPROVED` by `atalman` - lgtm (https://github.com/pytorch/pytorch/pull/135869#pullrequestreview-2334379165)
- `2024-09-30T20:14:31Z` `APPROVED` by `malfet` (https://github.com/pytorch/pytorch/pull/135869#pullrequestreview-2338482200)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2024-09-26T17:44:48Z` `issue` by `jithunnair-amd`; signals: hang; excerpt: "This looks like feature work, at least EXPERIMENTAL Navi31 support. If you split out critical fixes only, we can cherry-pick that. @kit1980 If it ..." (https://github.com/pytorch/pytorch/pull/135869#issuecomment-2377574849)
- `2024-09-30T20:10:25Z` `issue` by `jithunnair-amd`; signals: hang; excerpt: "@kit1980 Can we please merge this PR? It also allows us to re-enable entire test transformers.py suite for ROCm, which was disabled due to ..." (https://github.com/pytorch/pytorch/pull/135869#issuecomment-2384059137)
- `2024-09-12T17:05:51Z` `review` `APPROVED` by `pruthvistony`; signals: triton; excerpt: "LGTM. Cherry-pick from main branch. Part of continued effort to improve AOTriton on ROCm." (https://github.com/pytorch/pytorch/pull/135869#pullrequestreview-2300933065)
- `2024-09-25T20:34:32Z` `issue` by `kit1980`; signals: general review; excerpt: "This looks like feature work, at least EXPERIMENTAL Navi31 support. If you split out critical fixes only, we can cherry-pick that." (https://github.com/pytorch/pytorch/pull/135869#issuecomment-2375203117)
