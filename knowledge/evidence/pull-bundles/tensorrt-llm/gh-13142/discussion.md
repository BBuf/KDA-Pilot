# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13142](https://github.com/NVIDIA/TensorRT-LLM/pull/13142)
- Source page: `sources/prs/tensorrt-llm/PR-13142.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13142`
- Generated at: `2026-05-20T15:18:31.346483+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-17T05:03:11Z`
- Merged: `2026-04-17T05:53:40Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: ZhanruiSunCh, chenfeiz0326, coderabbitai, ruodil, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-17T05:10:16Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#pullrequestreview-4126213997)
- `2026-04-17T05:24:59Z` `APPROVED` by `ZhanruiSunCh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#pullrequestreview-4126293403)
- `2026-04-17T05:33:08Z` `APPROVED` by `ruodil` (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#pullrequestreview-4126331593)

## Inline Comment Hotspots

- `tests/integration/defs/perf/test_perf_sanity.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-17T05:10:12Z` `issue` by `coderabbitai`; signals: b200, benchmark, block, cache, fp4, hang, kv cache, memory; excerpt: "📝 Walkthrough Walkthrough This PR removes GPU SLURM directives from job submission, adjusts benchmark iteration logic for gen-only modes, updates benchmark configuration ratios across ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#issuecomment-4265555879)
- `2026-04-17T05:10:16Z` `review` `COMMENTED` by `coderabbitai`; signals: b200, fp4, hang, perf, tensorrt; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#pullrequestreview-4126213997)
- `2026-04-17T05:10:15Z` `inline` by `coderabbitai` `tests/integration/defs/perf/test_perf_sanity.py`:1394; signals: block, hang, perf, pipeline; excerpt: "⚠️ Potential issue 🟠 Major CI-blocking formatting issue in this changed block. ruff-format already failed on this range in pipeline; please re-run formatting and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#discussion_r3098004312)
- `2026-04-17T05:38:54Z` `issue` by `chenfeiz0326`; signals: perf, pipeline; excerpt: "/bot skip --comment "Only update perf test configs, no need to run the whole CI pipeline"" (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#issuecomment-4265709899)
- `2026-04-17T05:53:37Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 43970]( [ skip ] completed with state SUCCESS. Commit: 36b41f2 Skipping testing for commit 36b41f2 [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/13142#issuecomment-4265767803)
