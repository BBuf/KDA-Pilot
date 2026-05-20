# PR Discussion Digest

- Source PR: [sgl-project/sglang#22955](https://github.com/sgl-project/sglang/pull/22955)
- Source page: `sources/prs/sglang/PR-22955.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22955`
- Generated at: `2026-05-20T15:29:34.194951+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-16T09:19:02Z`
- Merged: `2026-04-17T15:33:42Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: BBuf, mickqian
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-16T09:21:23Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the FLUX.2 NVFP4 quantization workflow to use the --transformer-path flag, allowing the ... (https://github.com/sgl-project/sglang/pull/22955#pullrequestreview-4119724946)
- `2026-04-17T13:19:18Z` `APPROVED` by `mickqian` (https://github.com/sgl-project/sglang/pull/22955#pullrequestreview-4129107842)

## Inline Comment Hotspots

- `python/sglang/multimodal_gen/test/server/testcase_configs.py`: 2 inline comment(s)
- `python/sglang/multimodal_gen/runtime/pipelines/flux_2_nvfp4.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-17T12:46:33Z` `issue` by `BBuf`; signals: b200, fp4, nvfp4; excerpt: "Debug note for the FLUX.2 NVFP4 B200 CI failure: The latest failure is different from the earlier class name / missing config.json issue. The ..." (https://github.com/sgl-project/sglang/pull/22955#issuecomment-4268084745)
- `2026-04-16T09:27:21Z` `issue` by `BBuf`; signals: b200, bf16, hang, register; excerpt: "/tag-and-rerun-ci Updated after local validation: - Removed changes from python/sglang/multimodal gen/test/server/test server common.py, python/sglang/multimodal gen/test/server/test server utils.py, and python/sglang/multimodal gen/test/unit/test transformer quant.py. - Moved ..." (https://github.com/sgl-project/sglang/pull/22955#issuecomment-4258892655)
