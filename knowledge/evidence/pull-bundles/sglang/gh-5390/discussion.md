# PR Discussion Digest

- Source PR: [sgl-project/sglang#5390](https://github.com/sgl-project/sglang/pull/5390)
- Source page: `sources/prs/sglang/PR-5390.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5390`
- Generated at: `2026-05-20T15:30:24.731560+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-14T23:12:09Z`
- Merged: `2025-04-28T03:58:53Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 5
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: hebiao064, merrymercy, trevor-m, yessenzhar, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-04-14T23:15:10Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5390#pullrequestreview-2765995335)
- `2025-04-14T23:16:05Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/5390#pullrequestreview-2765997934)
- `2025-04-14T23:17:00Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/5390#pullrequestreview-2765999600)
- `2025-04-14T23:18:28Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5390#pullrequestreview-2766001021)
- `2025-04-14T23:23:28Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/5390#pullrequestreview-2766017624)
- `2025-04-27T02:43:05Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/5390#pullrequestreview-2796874835)
- `2025-04-28T03:58:16Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5390#pullrequestreview-2797929381)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/cutlass_mla_backend.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-04-23T00:06:12Z` `issue` by `trevor-m`; signals: accuracy, benchmark, blackwell, cutlass, flashinfer, hopper, kernel, latency; excerpt: "would you mind share some benchmark on latency and accuracy comparing with FA3 and FlashInfer? Thanks Hi @hebiao064, cutlass mla is a blackwell kernel. ..." (https://github.com/sgl-project/sglang/pull/5390#issuecomment-2822748143)
- `2025-04-14T23:15:10Z` `inline` by `zhyncs` `python/sglang/srt/layers/attention/cutlass_mla_backend.py`:6; signals: attention, blackwell, cuda, cutlass, mla; excerpt: "QQ does this cutlass mla only support on Blackwell? And is the CUDA Graph and MTP compatible? Thanks." (https://github.com/sgl-project/sglang/pull/5390#discussion_r2043136603)
- `2025-04-14T23:16:05Z` `inline` by `trevor-m` `python/sglang/srt/layers/attention/cutlass_mla_backend.py`:6; signals: attention, blackwell, cutlass, kernel, mla; excerpt: "Yes, cutlass mla decode kernel requires blackwell." (https://github.com/sgl-project/sglang/pull/5390#discussion_r2043138209)
- `2025-04-14T23:17:00Z` `inline` by `trevor-m` `python/sglang/srt/layers/attention/cutlass_mla_backend.py`:6; signals: attention, cuda, cutlass, mla; excerpt: "I think it should be cuda graph compatible, but I'm currently debugging that. It's not working right now. What is MTP?" (https://github.com/sgl-project/sglang/pull/5390#discussion_r2043139439)
- `2025-04-15T05:56:08Z` `issue` by `hebiao064`; signals: accuracy, benchmark, flashinfer, latency; excerpt: "would you mind share some benchmark on latency and accuracy comparing with FA3 and FlashInfer? Thanks" (https://github.com/sgl-project/sglang/pull/5390#issuecomment-2803892621)
- `2025-04-14T23:18:28Z` `inline` by `zhyncs` `python/sglang/srt/layers/attention/cutlass_mla_backend.py`:6; signals: attention, cutlass, mla; excerpt: "Multi-Token Prediction" (https://github.com/sgl-project/sglang/pull/5390#discussion_r2043140448)
- `2025-04-14T23:23:28Z` `inline` by `trevor-m` `python/sglang/srt/layers/attention/cutlass_mla_backend.py`:6; signals: attention, cutlass, mla; excerpt: "Ah ok, no MTP is not supported yet." (https://github.com/sgl-project/sglang/pull/5390#discussion_r2043156266)
- `2025-04-23T00:07:52Z` `issue` by `trevor-m`; signals: benchmark, cuda; excerpt: "@zhyncs I fixed the problem with cuda graphs and added some benchmark results in the description, so this should be ready now." (https://github.com/sgl-project/sglang/pull/5390#issuecomment-2822750488)
