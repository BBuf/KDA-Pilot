# PR Discussion Digest

- Source PR: [sgl-project/sglang#21710](https://github.com/sgl-project/sglang/pull/21710)
- Source page: `sources/prs/sglang/PR-21710.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21710`
- Generated at: `2026-05-20T15:29:17.039335+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T21:47:24Z`
- Merged: `2026-04-08T05:43:14Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: 1am9trash, HaiShaw
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-30T21:48:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces nightly performance benchmarks for the GLM-5 model on AMD MI30x and MI35x ... (https://github.com/sgl-project/sglang/pull/21710#pullrequestreview-4033474856)
- `2026-04-02T00:42:26Z` `APPROVED` by `1am9trash` (https://github.com/sgl-project/sglang/pull/21710#pullrequestreview-4047770714)
- `2026-04-08T05:43:01Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/21710#pullrequestreview-4072998788)

## Inline Comment Hotspots

- `test/registered/amd/perf/mi35x/test_glm5_perf_mi35x.py`: 3 inline comment(s)
- `test/registered/amd/perf/mi30x/test_glm5_perf_amd.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-01T10:59:30Z` `issue` by `1am9trash`; signals: fp8; excerpt: "Maybe we can add --reasoning-parser=glm45 --tool-call-parser=glm47 to the GLM-5-FP8 AMD test configs for consistency. These parsers are already used in NV unit tests and ..." (https://github.com/sgl-project/sglang/pull/21710#issuecomment-4169250211)
