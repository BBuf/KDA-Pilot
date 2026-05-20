# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#764](https://github.com/flashinfer-ai/flashinfer/pull/764)
- Source page: `sources/prs/flashinfer/PR-764.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-764`
- Generated at: `2026-05-20T15:26:35.523019+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-29T14:28:33Z`
- Merged: `2025-02-13T08:33:11Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 13
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=7
- Human participants with discussion text: abmfy, youkaichao, yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-08T03:11:40Z` `COMMENTED` by `youkaichao` - thanks for the great efforts! (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603211310)
- `2025-02-08T13:26:23Z` `COMMENTED` by `yzh119` - Hi @youkaichao @abmfy thanks so much for your contributions! I have some concern about compilation time for JIT, ... (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603799913)
- `2025-02-08T13:27:16Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603808885)
- `2025-02-08T13:34:29Z` `COMMENTED` by `youkaichao` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603827855)
- `2025-02-08T14:04:06Z` `COMMENTED` by `abmfy` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603854072)
- `2025-02-08T14:27:19Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603858632)
- `2025-02-08T20:21:16Z` `COMMENTED` by `yzh119` - Thanks @abmfy @youkaichao for this contribution! Overall look good to me, but I request some changes on scheduler.cuh ... (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604018965)
- `2025-02-09T08:05:16Z` `COMMENTED` by `youkaichao` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604145204)
- `2025-02-09T08:05:56Z` `COMMENTED` by `youkaichao` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604145307)
- `2025-02-09T08:07:05Z` `COMMENTED` by `youkaichao` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604145498)
- `2025-02-09T08:07:53Z` `COMMENTED` by `youkaichao` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604145663)
- `2025-02-09T08:14:25Z` `COMMENTED` by `abmfy` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604146723)
- `2025-02-09T08:16:03Z` `COMMENTED` by `abmfy` (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604146967)
- `2025-02-13T08:32:59Z` `APPROVED` by `yzh119` - Thank you so much for this refactor, let merge this first :) (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2614223285)

## Inline Comment Hotspots

- `csrc/pytorch_conversion_utils.h`: 6 inline comment(s)
- `csrc/pytorch_extension_utils.h`: 5 inline comment(s)
- `include/flashinfer/attention/scheduler.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-02-08T20:16:56Z` `inline` by `yzh119` `include/flashinfer/attention/scheduler.cuh`:27; signals: attention, cuda, cutlass, flashinfer; excerpt: "We tend not to have a torch dependency in include folder (the header-only library should only depend on cuda/cutlass/stl etc, because some of the ..." (https://github.com/flashinfer-ai/flashinfer/pull/764#discussion_r1947940808)
- `2025-02-08T20:19:34Z` `inline` by `yzh119` `include/flashinfer/attention/scheduler.cuh`:318; signals: attention, flashinfer, hang, vector; excerpt: "still using std::vector here, but change the logic in source files (csrc/ .cu)." (https://github.com/flashinfer-ai/flashinfer/pull/764#discussion_r1947941207)
- `2025-02-09T18:52:35Z` `issue` by `yzh119`; signals: cuda, flashinfer, kernel, sm90; excerpt: "I'm using torch 2.6-cu126 (and CUDA 12.8) and I tried installing the AOT wheel in this PR, when I import flashinfer.flashinfer kernels and flashinfer.flashinfer ..." (https://github.com/flashinfer-ai/flashinfer/pull/764#issuecomment-2646478959)
- `2025-02-12T08:47:42Z` `issue` by `yzh119`; signals: hang, mla, nan; excerpt: "Rebased with latest main branch and changes the mla interface to pytorch library. @abmfy @youkaichao Regarding the build error, I tried a new environment ..." (https://github.com/flashinfer-ai/flashinfer/pull/764#issuecomment-2653019156)
- `2025-02-13T03:30:16Z` `issue` by `youkaichao`; signals: hang, mla, nan; excerpt: "Rebased with latest main branch and changes the mla interface to pytorch library. @abmfy @youkaichao Regarding the build error, I tried a new environment ..." (https://github.com/flashinfer-ai/flashinfer/pull/764#issuecomment-2655374697)
- `2025-02-08T20:21:16Z` `review` `COMMENTED` by `yzh119`; signals: hang; excerpt: "Thanks @abmfy @youkaichao for this contribution! Overall look good to me, but I request some changes on scheduler.cuh because we don't want to introduce ..." (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2604018965)
- `2025-01-29T14:58:51Z` `issue` by `youkaichao`; signals: hang, vector; excerpt: "looks more involved than I think. we need to change the usage of std::vector" (https://github.com/flashinfer-ai/flashinfer/pull/764#issuecomment-2621893650)
- `2025-02-09T08:14:24Z` `inline` by `abmfy` `csrc/pytorch_conversion_utils.h`:24; signals: dtype; excerpt: "I've checked that with vec being int64 t, at::tensor will automatically have a dtype of int64; but for explicitness I'll add that" (https://github.com/flashinfer-ai/flashinfer/pull/764#discussion_r1948033557)
- `2025-02-08T13:26:23Z` `review` `COMMENTED` by `yzh119`; signals: general review; excerpt: "Hi @youkaichao @abmfy thanks so much for your contributions! I have some concern about compilation time for JIT, I wonder do you think it's ..." (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603799913)
- `2025-02-09T08:05:16Z` `inline` by `youkaichao` `csrc/pytorch_conversion_utils.h`:24; signals: dtype; excerpt: "add torch::dtype?" (https://github.com/flashinfer-ai/flashinfer/pull/764#discussion_r1948032214)
- `2025-02-09T08:07:05Z` `inline` by `youkaichao` `csrc/pytorch_conversion_utils.h`:28; signals: dtype; excerpt: "we can remove this check, if we add dtype in vec to tensor" (https://github.com/flashinfer-ai/flashinfer/pull/764#discussion_r1948032446)
- `2025-02-08T03:11:40Z` `review` `COMMENTED` by `youkaichao`; signals: general review; excerpt: "thanks for the great efforts!" (https://github.com/flashinfer-ai/flashinfer/pull/764#pullrequestreview-2603211310)
