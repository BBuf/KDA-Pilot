# PR Discussion Digest

- Source PR: [vllm-project/vllm#12093](https://github.com/vllm-project/vllm/pull/12093)
- Source page: `sources/prs/vllm/PR-12093.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12093`
- Generated at: `2026-05-20T15:33:40.769905+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-15T18:34:19Z`
- Merged: `2025-01-23T14:45:48Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: LucasWilkinson, WoosukKwon, houseroad, mergify, mgoin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-01-22T05:11:51Z` `APPROVED` by `WoosukKwon` - LGTM. Amazing work! This resolves the performance issue in V1! 🚀 Really appreciate it! (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2566204447)
- `2025-01-22T16:34:57Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2567725446)
- `2025-01-22T17:16:34Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2567826781)
- `2025-01-23T12:29:17Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2569736568)
- `2025-01-23T13:57:37Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2569939102)
- `2025-01-23T14:24:57Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2570013487)
- `2025-01-23T14:40:25Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2570056849)

## Inline Comment Hotspots

- `vllm/attention/backends/flash_attn.py`: 4 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-01-23T13:57:37Z` `inline` by `LucasWilkinson` `vllm/attention/backends/flash_attn.py`:646; signals: attention, failing, memory, shared memory; excerpt: "ya, the CI picked up some shapes that were failing because of not enough shared memory; FA3 doesn't seem to work for all shapes ..." (https://github.com/vllm-project/vllm/pull/12093#discussion_r1927022220)
- `2025-01-23T14:24:57Z` `inline` by `WoosukKwon` `vllm/attention/backends/flash_attn.py`:646; signals: attention, perf, performance; excerpt: "Got it. Thanks for the explanation! Do we know which shapes are not supported? Since FA3 could be very important for our performance, I'm ..." (https://github.com/vllm-project/vllm/pull/12093#discussion_r1927065481)
- `2025-01-22T17:16:33Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu_model_runner.py`:202; signals: attention, flash attention; excerpt: "v1 only has the flash attention backend for now, this PR moves flash attn varlen func to using seqlens from start locs (v0 uses ..." (https://github.com/vllm-project/vllm/pull/12093#discussion_r1925689718)
- `2025-01-22T05:11:51Z` `review` `APPROVED` by `WoosukKwon`; signals: perf, performance; excerpt: "LGTM. Amazing work! This resolves the performance issue in V1! 🚀 Really appreciate it!" (https://github.com/vllm-project/vllm/pull/12093#pullrequestreview-2566204447)
- `2025-01-23T14:40:24Z` `inline` by `WoosukKwon` `vllm/attention/backends/flash_attn.py`:646; signals: attention; excerpt: "@LucasWilkinson A small concern on this is that most of our CI wouldn't test FA3 actually since it uses L4 (if I remember correctly)." (https://github.com/vllm-project/vllm/pull/12093#discussion_r1927090493)
- `2025-01-23T12:29:16Z` `inline` by `WoosukKwon` `vllm/attention/backends/flash_attn.py`:646; signals: attention; excerpt: "Just to confirm: Lovelace GPUs will also use FA2 by default, right?" (https://github.com/vllm-project/vllm/pull/12093#discussion_r1926900949)
- `2025-01-22T16:34:53Z` `inline` by `mgoin` `vllm/v1/worker/gpu_model_runner.py`:202; signals: general review; excerpt: "In more places than this, you remove the padding either at the start or the end - why is this okay for existing attn ..." (https://github.com/vllm-project/vllm/pull/12093#discussion_r1925629685)
- `2025-01-22T06:40:41Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @LucasWilkinson." (https://github.com/vllm-project/vllm/pull/12093#issuecomment-2606417080)
