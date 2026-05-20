# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8164](https://github.com/NVIDIA/cccl/pull/8164)
- Source page: `sources/prs/cccl-cub/PR-8164.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8164`
- Generated at: `2026-05-20T15:20:30.190441+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T03:07:12Z`
- Merged: `2026-04-15T10:05:37Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 22
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=18, outdated=15
- Human participants with discussion text: bernhardmgruber, griwes, miscco
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-26T10:19:43Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4005525637)
- `2026-03-30T06:59:22Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4028437642)
- `2026-04-14T06:19:38Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4103708003)
- `2026-04-14T21:23:37Z` `COMMENTED` by `bernhardmgruber` - Looks mostly good! (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4108866896)
- `2026-04-14T21:24:36Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4109301817)
- `2026-04-14T21:25:12Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4109304783)
- `2026-04-15T09:32:25Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4112425008)
- `2026-04-15T10:05:34Z` `APPROVED` by `bernhardmgruber` - I did a verification of the generated SASS again and saw no problems (updated PR description). (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4112622489)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_scan_by_key.cuh`: 12 inline comment(s)
- `cub/cub/device/dispatch/dispatch_scan_by_key.cuh`: 9 inline comment(s)
- `cub/benchmarks/bench/scan/exclusive/by_key.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-14T21:06:33Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_scan_by_key.cuh`:280; signals: hang, kernel; excerpt: "Important: This is a breaking change, since a user passing a custom PolicyHub will now only influence the host code but the custom policy ..." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r3082520682)
- `2026-03-26T10:03:41Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/scan/exclusive/by_key.cu`:11; signals: benchmark; excerpt: "I don't think the policy selector there handles scan by key, since it returns a scan policy and not a scan by key policy. ..." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r2993710296)
- `2026-03-26T10:11:57Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan_by_key.cuh`:1732; signals: hang; excerpt: "Important: I think it's very confusing if we change the arch argument during this already very long function. Let's try to avoid that." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r2993756313)
- `2026-03-26T10:17:30Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_scan_by_key.cuh`:711; signals: compile; excerpt: "Suggestion: IIUC, the active tuning policy is never needed as a compile-time value, so we can just omit using dispatch arch and just query ..." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r2993787247)
- `2026-04-14T21:23:37Z` `review` `COMMENTED` by `bernhardmgruber`; signals: general review; excerpt: "Looks mostly good!" (https://github.com/NVIDIA/cccl/pull/8164#pullrequestreview-4108866896)
- `2026-03-25T06:42:00Z` `issue` by `griwes`; signals: alignment; excerpt: "After the above policy realignment, there's no more SASS differences." (https://github.com/NVIDIA/cccl/pull/8164#issuecomment-4124175030)
- `2026-03-25T10:16:35Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_scan_by_key.cuh`:158; signals: general review; excerpt: "Important: This 1 was not there before and could impact SASS. Maybe stick to the old arguments and remove it." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r2987187853)
- `2026-03-30T06:58:51Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_scan_by_key.cuh`:1127; signals: general review; excerpt: "I believe we could shorten the whole function here if we had the if (primitive value t == primitive accum::yes) higher up so that ..." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r3007916278)
- `2026-04-14T06:19:38Z` `inline` by `griwes` `cub/cub/device/dispatch/tuning/tuning_scan_by_key.cuh`:1128; signals: general review; excerpt: "I'll make the structure a bit tidier by hoisting the common conditions out, but I definitely prefer the switch form for readability." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r3077470390)
- `2026-03-25T10:15:54Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_scan_by_key.cuh`:127; signals: general review; excerpt: "Important: those parameters are unused, let's remove them." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r2987184518)
- `2026-03-25T10:21:20Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_scan_by_key.cuh`:448; signals: general review; excerpt: "Important: I think PolicySelectorT is unused, so it can be removed again." (https://github.com/NVIDIA/cccl/pull/8164#discussion_r2987213841)
- `2026-03-26T10:11:07Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan_by_key.cuh`:1128; signals: general review; excerpt: "Suggestion: can we simplify this? Maybe it would be more readable if we did if/else clauses like:" (https://github.com/NVIDIA/cccl/pull/8164#discussion_r2993750640)
