# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1013](https://github.com/flashinfer-ai/flashinfer/pull/1013)
- Source page: `sources/prs/flashinfer/PR-1013.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1013`
- Generated at: `2026-05-20T15:21:35.917282+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-10T07:21:08Z`
- Merged: `2025-04-15T14:34:33Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: dhy2000, yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-10T15:30:22Z` `APPROVED` by `yzh119` - For the lint error ( Please format your code with [pre-commit]( (https://github.com/flashinfer-ai/flashinfer/pull/1013#pullrequestreview-2757291787)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-04-13T07:22:48Z` `issue` by `dhy2000`; signals: attention, cache, kernel, mla; excerpt: "Hi @dhy2000 , we encourage using BatchMLAPagedAttentionWrapper (in which supports both decode and append attention, instead of BatchDecodeMlaWithPagedKVCacheWrapper. Thanks, so is it necessary to ..." (https://github.com/flashinfer-ai/flashinfer/pull/1013#issuecomment-2799838381)
- `2025-04-10T15:05:54Z` `issue` by `yzh119`; signals: attention, cache, mla; excerpt: "Hi @dhy2000 , we encourage using BatchMLAPagedAttentionWrapper (in which supports both decode and append attention, instead of BatchDecodeMlaWithPagedKVCacheWrapper." (https://github.com/flashinfer-ai/flashinfer/pull/1013#issuecomment-2794134395)
- `2025-04-15T14:31:28Z` `issue` by `yzh119`; signals: cache, kernel, mla; excerpt: "Thanks, so is it necessary to keep the test mla decode kernel.py which tests BatchDecodeMlaWithPagedKVCacheWrapper? We can keep it until fully deprecate this function." (https://github.com/flashinfer-ai/flashinfer/pull/1013#issuecomment-2805473431)
- `2025-04-10T08:31:07Z` `issue` by `dhy2000`; signals: failing; excerpt: "The failing jenkins check seems not caused by compilation error, the last several lines of the log: Can this check re-run?" (https://github.com/flashinfer-ai/flashinfer/pull/1013#issuecomment-2791978223)
