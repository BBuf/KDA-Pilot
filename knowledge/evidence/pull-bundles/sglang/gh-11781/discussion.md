# PR Discussion Digest

- Source PR: [sgl-project/sglang#11781](https://github.com/sgl-project/sglang/pull/11781)
- Source page: `sources/prs/sglang/PR-11781.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11781`
- Generated at: `2026-05-20T15:27:27.066059+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-17T21:58:10Z`
- Merged: `2025-10-18T08:08:01Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (approved=1, changes_requested=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: merrymercy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-17T22:00:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the installation instructions and cleans up the pyproject.toml files. The changes include ... (https://github.com/sgl-project/sglang/pull/11781#pullrequestreview-3352262480)
- `2025-10-17T22:44:06Z` `CHANGES_REQUESTED` by `zhyncs` - nit: we need to update the Dockerfile too. We can just remove BUILD TYPE. wdyt (https://github.com/sgl-project/sglang/pull/11781#pullrequestreview-3352315334)
- `2025-10-17T23:26:45Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/11781#pullrequestreview-3352372434)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-10-17T22:44:06Z` `review` `CHANGES_REQUESTED` by `zhyncs`; signals: general review; excerpt: "nit: we need to update the Dockerfile too. We can just remove BUILD TYPE. wdyt" (https://github.com/sgl-project/sglang/pull/11781#pullrequestreview-3352315334)
- `2025-10-17T23:12:07Z` `issue` by `merrymercy`; signals: blackwell; excerpt: "@zhyncs good catch. I will keep blackwell and blackwell aarch64 in the pyproject.toml for now. We can delete them in the next PR." (https://github.com/sgl-project/sglang/pull/11781#issuecomment-3417482954)
- `2025-10-17T23:26:37Z` `issue` by `zhyncs`; signals: general review; excerpt: "BTW @mingfeima @HaiShaw May we use sglang-amx and sglang-rocm for the PyPI installation? It'll be easier for the user to install SGLang on Intel ..." (https://github.com/sgl-project/sglang/pull/11781#issuecomment-3417505175)
- `2025-10-18T01:07:55Z` `issue` by `merrymercy`; signals: general review; excerpt: "BTW @mingfeima @HaiShaw May we use sglang-amx and sglang-rocm for the PyPI installation? It'll be easier for the user to install SGLang on Intel ..." (https://github.com/sgl-project/sglang/pull/11781#issuecomment-3417656830)
