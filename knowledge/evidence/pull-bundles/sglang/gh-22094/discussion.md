# PR Discussion Digest

- Source PR: [sgl-project/sglang#22094](https://github.com/sgl-project/sglang/pull/22094)
- Source page: `sources/prs/sglang/PR-22094.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22094`
- Generated at: `2026-05-20T15:29:21.826124+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-04T04:39:01Z`
- Merged: `2026-04-25T06:00:29Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: BBuf, DarkSharpness, ch-wan
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-13T12:49:29Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/22094#pullrequestreview-4098780295)
- `2026-04-21T22:14:24Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/22094#pullrequestreview-4151029299)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/activation.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-20T07:55:05Z` `issue` by `DarkSharpness`; signals: benchmark, perf, performance; excerpt: "Could you resolve the conflicts and add some benchmark results? Hi. I've just rebased to main. Performance results are the same as the old ..." (https://github.com/sgl-project/sglang/pull/22094#issuecomment-4278808651)
- `2026-04-21T22:10:12Z` `inline` by `ch-wan` `python/sglang/jit_kernel/activation.py`:26; signals: kernel, sm100; excerpt: "In the original implementation, --use fast math is disabled for SM100+ or ROCM. Could you confirm if adding this flag ubiquitously is expected?" (https://github.com/sgl-project/sglang/pull/22094#discussion_r3120560742)
- `2026-04-19T21:43:13Z` `issue` by `ch-wan`; signals: benchmark; excerpt: "Could you resolve the conflicts and add some benchmark results?" (https://github.com/sgl-project/sglang/pull/22094#issuecomment-4276881955)
- `2026-04-24T00:31:44Z` `issue` by `ch-wan`; signals: hang; excerpt: "@DarkSharpness I fixed some numerical issues. Could you check my changes?" (https://github.com/sgl-project/sglang/pull/22094#issuecomment-4309564294)
