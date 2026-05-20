# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8427](https://github.com/NVIDIA/cccl/pull/8427)
- Source page: `sources/prs/cccl-cub/PR-8427.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8427`
- Generated at: `2026-05-20T15:20:43.539342+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-15T02:18:35Z`
- Merged: `2026-04-27T18:15:06Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 2 (approved=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bernhardmgruber, davebayer, edenfunf
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-27T13:56:05Z` `APPROVED` by `bernhardmgruber` - Thank you very much for this contribution! (https://github.com/NVIDIA/cccl/pull/8427#pullrequestreview-4181485937)
- `2026-04-27T17:02:23Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8427#pullrequestreview-4182793661)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-21T14:08:13Z` `issue` by `edenfunf`; signals: benchmark, cuda, hang, kernel, memory, regression, speedup; excerpt: "@bernhardmgruber Thanks for the review! Done — benchmark ported in a separate commit . It mirrors with the API swapped to thrust::is partitioned + ..." (https://github.com/NVIDIA/cccl/pull/8427#issuecomment-4289183796)
- `2026-04-16T14:07:37Z` `issue` by `edenfunf`; signals: benchmark, cuda, kernel, speedup; excerpt: "@gevtushenko Hi, could you please take a look at this PR when you have time? This PR replaces the current two-pass CUDA implementation of ..." (https://github.com/NVIDIA/cccl/pull/8427#issuecomment-4260703199)
- `2026-04-21T12:34:11Z` `issue` by `bernhardmgruber`; signals: benchmark, hang; excerpt: "Hi! Thx for the PR! Can you please also port the benchmark from libcu++ and post a benchmark diff for your change? Let me ..." (https://github.com/NVIDIA/cccl/pull/8427#issuecomment-4288553818)
- `2026-04-27T13:55:48Z` `issue` by `bernhardmgruber`; signals: general review; excerpt: "Here is a quick&dirty one on my workstation as well: The noise levels are a bit high, but good enough for this massive improvement!" (https://github.com/NVIDIA/cccl/pull/8427#issuecomment-4327549126)
