# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1233](https://github.com/Dao-AILab/flash-attention/pull/1233)
- Source page: `sources/prs/flash-attention/PR-1233.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1233`
- Generated at: `2026-05-20T15:16:29.271603+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-09-16T23:00:34Z`
- Merged: `2024-09-20T06:14:45Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 4 (commented=4)
- Inline review comments: 9
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=0, outdated=4
- Human participants with discussion text: ipiszy, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2024-09-19T07:43:05Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1233#pullrequestreview-2314646762)
- `2024-09-20T05:07:44Z` `COMMENTED` by `ipiszy` - Thanks @tridao ! (https://github.com/Dao-AILab/flash-attention/pull/1233#pullrequestreview-2317252125)
- `2024-09-20T05:23:22Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1233#pullrequestreview-2317290319)
- `2024-09-20T05:33:32Z` `COMMENTED` by `ipiszy` (https://github.com/Dao-AILab/flash-attention/pull/1233#pullrequestreview-2317300123)

## Inline Comment Hotspots

- `hopper/mainloop_bwd_sm90_tma_gmma_ws.hpp`: 4 inline comment(s)
- `hopper/flash_bwd_kernel.h`: 2 inline comment(s)
- `hopper/flash_bwd_launch_template.h`: 2 inline comment(s)
- `hopper/flash_fwd_launch_template.h`: 1 inline comment(s)

## High-Signal Discussion

- `2024-09-19T07:30:35Z` `inline` by `tridao` `hopper/flash_bwd_kernel.h`:255; signals: block, hang, hopper, kernel; excerpt: "We'd need the same change to m block max here?" (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1766309525)
- `2024-09-19T07:36:00Z` `inline` by `tridao` `hopper/mainloop_bwd_sm90_tma_gmma_ws.hpp`:616; signals: hopper, sm90, tma; excerpt: "Let's condition on Is local here" (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1766317073)
- `2024-09-20T04:55:55Z` `inline` by `ipiszy` `hopper/mainloop_bwd_sm90_tma_gmma_ws.hpp`:616; signals: hopper, sm90, tma; excerpt: "Why is it necessary to condition on Is local? I think Deterministic is also applied to local?" (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1767981986)
- `2024-09-20T05:23:22Z` `inline` by `tridao` `hopper/mainloop_bwd_sm90_tma_gmma_ws.hpp`:616; signals: hopper, sm90, tma; excerpt: "Yes but without local we wound't need additional calls to Barrier::arrive inc right?" (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1767998815)
- `2024-09-20T05:33:32Z` `inline` by `ipiszy` `hopper/mainloop_bwd_sm90_tma_gmma_ws.hpp`:616; signals: hopper, sm90, tma; excerpt: "Ah right, my brain is broken lol." (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1768005416)
- `2024-09-19T07:32:45Z` `inline` by `tridao` `hopper/flash_bwd_launch_template.h`:177; signals: hopper, kernel; excerpt: "Let's template with Is local && !Is causal to reduce the number of kernels. And add an static assert(!(Is causal && Is local)) inside ..." (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1766312563)
- `2024-09-20T04:41:29Z` `inline` by `ipiszy` `hopper/flash_bwd_kernel.h`:255; signals: hopper, kernel; excerpt: "Good catch! Missed this." (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1767973849)
- `2024-09-19T07:33:08Z` `inline` by `tridao` `hopper/flash_bwd_launch_template.h`:191; signals: hopper; excerpt: "Same templating Is local && !Is causal here and below" (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1766313059)
- `2024-09-19T07:40:16Z` `inline` by `tridao` `hopper/flash_fwd_launch_template.h`:124; signals: hopper; excerpt: "same here, let's template with Is local && !Is causal" (https://github.com/Dao-AILab/flash-attention/pull/1233#discussion_r1766322822)
- `2024-09-20T05:07:44Z` `review` `COMMENTED` by `ipiszy`; signals: general review; excerpt: "Thanks @tridao !" (https://github.com/Dao-AILab/flash-attention/pull/1233#pullrequestreview-2317252125)
