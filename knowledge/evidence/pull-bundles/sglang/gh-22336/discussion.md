# PR Discussion Digest

- Source PR: [sgl-project/sglang#22336](https://github.com/sgl-project/sglang/pull/22336)
- Source page: `sources/prs/sglang/PR-22336.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22336`
- Generated at: `2026-05-20T15:29:23.472534+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T07:16:16Z`
- Merged: `2026-04-09T05:57:43Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: 1am9trash, HaiShaw, michaelzhang-ai
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-04-08T07:17:48Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces accuracy and performance evaluation tests for the GLM-5.1 model on AMD MI30x ... (https://github.com/sgl-project/sglang/pull/22336#pullrequestreview-4073374834)
- `2026-04-09T04:30:51Z` `APPROVED` by `1am9trash` - LGTM (https://github.com/sgl-project/sglang/pull/22336#pullrequestreview-4079693597)
- `2026-04-09T05:57:33Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/22336#pullrequestreview-4079975240)

## Inline Comment Hotspots

- `test/registered/amd/accuracy/mi35x/test_glm51_eval_mi35x.py`: 2 inline comment(s)
- `test/registered/amd/perf/mi35x/test_glm51_perf_mi35x.py`: 2 inline comment(s)
- `test/registered/amd/perf/mi30x/test_glm51_perf_amd.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-09T00:41:29Z` `issue` by `michaelzhang-ai`; signals: perf, performance; excerpt: "CI Validation - All 4 GLM-5.1 jobs passed ✅ Nightly Test (AMD) — — and performance tests (bench one batch) passed on both MI30x ..." (https://github.com/sgl-project/sglang/pull/22336#issuecomment-4210681792)
- `2026-04-09T01:53:55Z` `issue` by `1am9trash`; signals: benchmark, moe; excerpt: "Followed the model configs for and are both MoE models (256 routed experts, top-8). Why does GLM-5.1 add --ep-size 8 while GLM-5 runs with ..." (https://github.com/sgl-project/sglang/pull/22336#issuecomment-4210927760)
- `2026-04-09T04:04:15Z` `issue` by `michaelzhang-ai`; signals: benchmark, moe; excerpt: "Followed the model configs for and are both MoE models (256 routed experts, top-8). Why does GLM-5.1 add --ep-size 8 while GLM-5 runs with ..." (https://github.com/sgl-project/sglang/pull/22336#issuecomment-4211377491)
