# PR Discussion Digest

- Source PR: [vllm-project/vllm#36458](https://github.com/vllm-project/vllm/pull/36458)
- Source page: `sources/prs/vllm/PR-36458.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36458`
- Generated at: `2026-05-20T15:40:10.781308+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T06:19:14Z`
- Merged: `2026-03-11T04:54:09Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=5, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: DarkLight1337, jikunshang, wuxun-zhang, xinyu-intel, xuechendi, yma11
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-09T06:22:11Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for block FP8 MoE on XPU devices by enabling a fallback ... (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3913130810)
- `2026-03-09T06:36:09Z` `APPROVED` by `wuxun-zhang` (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3913173086)
- `2026-03-09T08:55:59Z` `APPROVED` by `xinyu-intel` (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3913843728)
- `2026-03-09T14:03:26Z` `APPROVED` by `xuechendi` - LGTM (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3915638539)
- `2026-03-10T01:12:49Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3919107502)
- `2026-03-10T01:32:48Z` `COMMENTED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3919160627)
- `2026-03-10T01:35:47Z` `APPROVED` by `yma11` - LGTM. (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3919167543)
- `2026-03-11T04:21:11Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/36458#pullrequestreview-3926818702)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/oracle/fp8.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-10T01:12:50Z` `inline` by `yma11` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:98; signals: fp8, moe; excerpt: "better to reword this comment." (https://github.com/vllm-project/vllm/pull/36458#discussion_r2908741145)
- `2026-03-10T01:32:47Z` `inline` by `jikunshang` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:98; signals: fp8, moe; excerpt: "updated." (https://github.com/vllm-project/vllm/pull/36458#discussion_r2908789067)
- `2026-03-10T01:31:30Z` `issue` by `jikunshang`; signals: moe, triton; excerpt: "Is there some place to add a log telling user Triton MoE is used or such log already exists? right. with debug log level:" (https://github.com/vllm-project/vllm/pull/36458#issuecomment-4027996812)
- `2026-03-10T01:26:10Z` `issue` by `yma11`; signals: moe, triton; excerpt: "Is there some place to add a log telling user Triton MoE is used or such log already exists?" (https://github.com/vllm-project/vllm/pull/36458#issuecomment-4027981665)
