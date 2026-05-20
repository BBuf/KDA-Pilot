# PR Discussion Digest

- Source PR: [vllm-project/vllm#17283](https://github.com/vllm-project/vllm/pull/17283)
- Source page: `sources/prs/vllm/PR-17283.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17283`
- Generated at: `2026-05-20T15:35:08.259586+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-28T05:06:01Z`
- Merged: `2025-04-28T20:55:50Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LucasWilkinson, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-28T14:12:14Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/17283#pullrequestreview-2799456954)
- `2025-04-28T14:34:25Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/17283#pullrequestreview-2799534045)
- `2025-04-28T15:30:01Z` `COMMENTED` by `mgoin` - Could you also check if v1 flashinfer has this issue? (https://github.com/vllm-project/vllm/pull/17283#pullrequestreview-2799752981)
- `2025-04-28T15:48:51Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/17283#pullrequestreview-2799819909)
- `2025-04-28T16:11:51Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17283#pullrequestreview-2799900699)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/flash_attn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-28T15:30:01Z` `review` `COMMENTED` by `mgoin`; signals: flashinfer; excerpt: "Could you also check if v1 flashinfer has this issue?" (https://github.com/vllm-project/vllm/pull/17283#pullrequestreview-2799752981)
- `2025-04-28T14:34:25Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/flash_attn.py`:375; signals: attention; excerpt: "The prefix part of cascade attention is run as a single request (since its shared), this was a copy paste bug with the scheduling ..." (https://github.com/vllm-project/vllm/pull/17283#discussion_r2063797390)
- `2025-04-28T14:12:14Z` `inline` by `tlrmchlsmth` `vllm/v1/attention/backends/flash_attn.py`:375; signals: attention; excerpt: "Could you explain what was going on here a bit more?" (https://github.com/vllm-project/vllm/pull/17283#discussion_r2063752506)
- `2025-04-28T15:33:46Z` `issue` by `LucasWilkinson`; signals: flashinfer; excerpt: "Could you also check if v1 flashinfer has this issue? FlashInfer uses the cascade wrapper which doesnt have a batch size argument" (https://github.com/vllm-project/vllm/pull/17283#issuecomment-2835656571)
