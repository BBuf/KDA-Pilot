# PR Discussion Digest

- Source PR: [sgl-project/sglang#18341](https://github.com/sgl-project/sglang/pull/18341)
- Source page: `sources/prs/sglang/PR-18341.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18341`
- Generated at: `2026-05-20T15:28:36.983129+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-06T06:26:23Z`
- Merged: `2026-02-21T16:07:16Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Fridge003, mmangkad, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-21T16:03:40Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18341#pullrequestreview-3835668424)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-02-07T04:12:58Z` `issue` by `Fridge003`; signals: kernel, race; excerpt: "@mmangkad Do you have screenshot of trace files? How can you make sure you have triggered this kernel" (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3863534533)
- `2026-02-12T05:32:34Z` `issue` by `Fridge003`; signals: cuda, race; excerpt: "launch overhead from disabling cuda graphs; with graphs enabled, the timeline is fully saturated. can you please post some trace results with cuda graph ..." (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3888771838)
- `2026-02-12T06:29:55Z` `issue` by `mmangkad`; signals: cuda, race; excerpt: "launch overhead from disabling cuda graphs; with graphs enabled, the timeline is fully saturated. can you please post some trace results with cuda graph ..." (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3888929221)
- `2026-02-13T01:34:23Z` `issue` by `yuan-luo`; signals: cuda, sm90; excerpt: "I didn't find this PR previously and did the similar thing. The new Unified API doesn't support SM90, so we need to check the ..." (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3894328561)
- `2026-02-15T01:22:46Z` `issue` by `mmangkad`; signals: cuda, sm90; excerpt: "I didn't find this PR previously and did the similar thing. The new Unified API doesn't support SM90, so we need to check the ..." (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3902978376)
- `2026-02-07T05:14:05Z` `issue` by `mmangkad`; signals: race; excerpt: "@Fridge003 confirmed via logs - they're quite different, but I can share a trace screenshot in a bit too" (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3863621140)
- `2026-02-07T06:04:12Z` `issue` by `mmangkad`; signals: race; excerpt: "Logs: The old API had no backend field and used trtllm create ipc workspace for all reduce fusion() instead. Traces:" (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3863683218)
- `2026-02-11T04:26:12Z` `issue` by `mmangkad`; signals: cuda; excerpt: "It looks really slow... Is that expected? The gaps were just host launch overhead from disabling cuda graphs; with graphs enabled, the timeline is ..." (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3882048269)
- `2026-02-21T16:06:56Z` `issue` by `Fridge003`; signals: general review; excerpt: "@mmangkad Maybe we can try to tune some of the configs, and see whether it can be faster (for future PR)" (https://github.com/sgl-project/sglang/pull/18341#issuecomment-3939021790)
