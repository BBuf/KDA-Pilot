# PR Discussion Digest

- Source PR: [sgl-project/sglang#18871](https://github.com/sgl-project/sglang/pull/18871)
- Source page: `sources/prs/sglang/PR-18871.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18871`
- Generated at: `2026-05-20T15:28:42.866848+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-15T22:01:28Z`
- Merged: `2026-03-10T06:56:07Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: BBuf, Johnsonms, b8zhong
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-15T22:03:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request is a great improvement, migrating the norm kernels from custom C++ implementations to ... (https://github.com/sgl-project/sglang/pull/18871#pullrequestreview-3805636593)
- `2026-03-07T08:22:08Z` `APPROVED` by `BBuf` - Looks good. (https://github.com/sgl-project/sglang/pull/18871#pullrequestreview-3908151680)
- `2026-03-10T05:56:48Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/18871#pullrequestreview-3919962365)
- `2026-03-10T06:18:18Z` `COMMENTED` by `Johnsonms` (https://github.com/sgl-project/sglang/pull/18871#pullrequestreview-3920044242)
- `2026-03-10T06:55:40Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/18871#pullrequestreview-3920190241)

## Inline Comment Hotspots

- `sgl-kernel/python/sgl_kernel/elementwise.py`: 2 inline comment(s)
- `sgl-kernel/benchmark/bench_norm_jit.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-10T06:18:18Z` `inline` by `Johnsonms` `sgl-kernel/python/sgl_kernel/elementwise.py`:162; signals: compile, flashinfer, kernel, race, register; excerpt: "We need this check because some FlashInfer norm paths are not safe under torch.compile(..., fullgraph=True). Dynamo traces into FlashInfer’s JIT module loading path, which ..." (https://github.com/sgl-project/sglang/pull/18871#discussion_r2909586231)
- `2026-03-10T05:56:48Z` `inline` by `BBuf` `sgl-kernel/python/sgl_kernel/elementwise.py`:162; signals: compile, kernel; excerpt: "Why we need to check torch.compile mode?" (https://github.com/sgl-project/sglang/pull/18871#discussion_r2909518026)
- `2026-03-07T00:51:47Z` `issue` by `Johnsonms`; signals: flashinfer, hang; excerpt: "Hi @Johnsonms , why could we not directly call the Flashinfer python API for this? Just like how it was done for sampling. Yes, ..." (https://github.com/sgl-project/sglang/pull/18871#issuecomment-4015040817)
- `2026-03-01T13:56:32Z` `issue` by `b8zhong`; signals: flashinfer; excerpt: "Hi @Johnsonms , why could we not directly call the Flashinfer python API for this? Just like how it was done for sampling." (https://github.com/sgl-project/sglang/pull/18871#issuecomment-3980018984)
