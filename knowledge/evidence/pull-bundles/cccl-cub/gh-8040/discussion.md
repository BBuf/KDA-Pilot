# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8040](https://github.com/NVIDIA/cccl/pull/8040)
- Source page: `sources/prs/cccl-cub/PR-8040.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8040`
- Generated at: `2026-05-20T15:20:28.013164+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-16T04:22:12Z`
- Merged: `2026-03-18T17:08:24Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 14
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=10, outdated=7
- Human participants with discussion text: NaderAlAwar, elstehle, miscco
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-16T08:44:29Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3952189001)
- `2026-03-16T13:13:16Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3953782356)
- `2026-03-16T13:13:41Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3953784641)
- `2026-03-17T04:52:55Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3958163440)
- `2026-03-17T07:59:17Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3958816584)
- `2026-03-17T08:52:20Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3959084657)
- `2026-03-18T15:23:49Z` `APPROVED` by `NaderAlAwar` - benchmark changes are good (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3968720611)

## Inline Comment Hotspots

- `cub/cub/agent/agent_topk.cuh`: 7 inline comment(s)
- `cub/cub/device/device_topk.cuh`: 6 inline comment(s)
- `cub/cub/device/dispatch/dispatch_topk.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-17T04:52:55Z` `inline` by `elstehle` `cub/cub/agent/agent_topk.cuh`:824; signals: hang; excerpt: "This is the logic for zero'ing histogram for the next pass. We are skipping this in the last pass for fundamental types. I am ..." (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2944349821)
- `2026-03-18T15:23:49Z` `review` `APPROVED` by `NaderAlAwar`; signals: benchmark, hang; excerpt: "benchmark changes are good" (https://github.com/NVIDIA/cccl/pull/8040#pullrequestreview-3968720611)
- `2026-03-16T08:35:31Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_topk.cuh`:396; signals: hang; excerpt: "To be sure the dispatch layer is fully internal, so this breaking change is fine" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2938876088)
- `2026-03-16T08:30:56Z` `inline` by `miscco` `cub/cub/agent/agent_topk.cuh`:90; signals: general review; excerpt: "I believe this could be funnelshift l(words[i], words[i - 1], shift); Totally not nerdsniping @fbusato with" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2938856350)
- `2026-03-16T08:42:07Z` `inline` by `miscco` `cub/cub/device/device_topk.cuh`:299; signals: general review; excerpt: "Important: I believe this sould be In other files we also mention the CTK version added, should we add that as a followup?" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2938905251)
- `2026-03-16T08:31:59Z` `inline` by `miscco` `cub/cub/agent/agent_topk.cuh`:190; signals: general review; excerpt: "Nitpick: Those should all be [[nodiscard]]" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2938861008)
- `2026-03-16T08:39:13Z` `inline` by `miscco` `cub/cub/device/device_topk.cuh`:260; signals: general review; excerpt: "Important: I believe in other algorithms we use template SFINAE instead of return type SFINAE" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2938891631)
- `2026-03-16T08:40:21Z` `inline` by `miscco` `cub/cub/agent/agent_topk.cuh`:62; signals: general review; excerpt: "Nitpick: We should move is fundamental type to a variable template instead of a type" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2938896702)
- `2026-03-16T08:43:53Z` `inline` by `miscco` `cub/cub/device/device_topk.cuh`:551; signals: general review; excerpt: "Ditto:" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2938913097)
- `2026-03-16T13:13:16Z` `inline` by `elstehle` `cub/cub/device/device_topk.cuh`:299; signals: general review; excerpt: "Thanks, that was a copy/paste oversight. Added the CTK version as well." (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2940301272)
- `2026-03-16T13:13:41Z` `inline` by `elstehle` `cub/cub/agent/agent_topk.cuh`:90; signals: general review; excerpt: "Oh, that's a great idea, thanks! I've adopted the funnelshift l." (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2940303531)
- `2026-03-17T07:56:56Z` `inline` by `miscco` `cub/cub/agent/agent_topk.cuh`:23; signals: general review; excerpt: "Important: This is relying on transitive includes, we should be careful here" (https://github.com/NVIDIA/cccl/pull/8040#discussion_r2945001146)
