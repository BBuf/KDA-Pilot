# PR Discussion Digest

- Source PR: [sgl-project/sglang#21654](https://github.com/sgl-project/sglang/pull/21654)
- Source page: `sources/prs/sglang/PR-21654.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21654`
- Generated at: `2026-05-20T15:29:17.036040+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T03:55:12Z`
- Merged: `2026-04-01T01:04:14Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: BBuf, Johnsonms
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-30T03:56:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request optimizes the fused qknorm rope JIT kernel by reducing the number of trigonometric ... (https://github.com/sgl-project/sglang/pull/21654#pullrequestreview-4027875271)
- `2026-03-31T06:43:30Z` `COMMENTED` by `BBuf` - Should can use fused qk norm rope() be updated too? After this change,yarn is part of the JIT ... (https://github.com/sgl-project/sglang/pull/21654#pullrequestreview-4035060509)
- `2026-03-31T06:47:02Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21654#pullrequestreview-4035074857)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/csrc/elementwise/fused_qknorm_rope.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-31T19:02:43Z` `issue` by `Johnsonms`; signals: block, occupancy, oom, register, warp; excerpt: "Could you share the before/after register usage and occupancy comparison for the qwen image 1024 case? An ncu screenshot would work. Here is before ..." (https://github.com/sgl-project/sglang/pull/21654#issuecomment-4164775253)
- `2026-03-30T19:21:06Z` `issue` by `Johnsonms`; signals: kernel, latency, speedup, throughput; excerpt: "Added the real production kernel shape tests: Comparison Summary: Across all production shapes, the optimization achieves a consistent 11–12% throughput improvement (lower latency), raising ..." (https://github.com/sgl-project/sglang/pull/21654#issuecomment-4157557271)
- `2026-03-31T06:43:30Z` `review` `COMMENTED` by `BBuf`; signals: compile, hang; excerpt: "Should can use fused qk norm rope() be updated too? After this change,yarn is part of the JIT specialization key, but the probe still ..." (https://github.com/sgl-project/sglang/pull/21654#pullrequestreview-4035060509)
- `2026-03-31T06:46:33Z` `issue` by `BBuf`; signals: occupancy, register; excerpt: "Could you share the before/after register usage and occupancy comparison for the qwen image 1024 case? An ncu screenshot would work." (https://github.com/sgl-project/sglang/pull/21654#issuecomment-4160325346)
- `2026-03-31T19:03:43Z` `issue` by `Johnsonms`; signals: compile, hang; excerpt: "Should can use fused qk norm rope() be updated too? After this change,yarn is part of the JIT specialization key, but the probe still ..." (https://github.com/sgl-project/sglang/pull/21654#issuecomment-4164782155)
