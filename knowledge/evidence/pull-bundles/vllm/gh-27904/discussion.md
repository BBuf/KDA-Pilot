# PR Discussion Digest

- Source PR: [vllm-project/vllm#27904](https://github.com/vllm-project/vllm/pull/27904)
- Source page: `sources/prs/vllm/PR-27904.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27904`
- Generated at: `2026-05-20T15:38:23.813739+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-01T00:23:31Z`
- Merged: `2025-11-04T07:56:21Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 9 (approved=3, commented=6)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: mgoin, nvjullin, nvpohanh, varun-sundar-rabindranath, yewentao256
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-01T00:24:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request effectively resolves a crash that occurred when running MoE models in eager mode ... (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3406665929)
- `2025-11-01T00:27:49Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3406667444)
- `2025-11-01T07:21:30Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3406929204)
- `2025-11-01T07:21:36Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3406929242)
- `2025-11-01T19:09:23Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3407656485)
- `2025-11-01T19:11:22Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3407656796)
- `2025-11-03T01:29:45Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3409198558)
- `2025-11-03T02:53:28Z` `COMMENTED` by `nvjullin` (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3409258756)
- `2025-11-04T07:56:16Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/27904#pullrequestreview-3414510703)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/trtllm_moe.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-11-01T07:21:30Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:130; signals: autotune, cuda, cudagraph, moe; excerpt: "Ohh I see, very interesting. Yes I have the same question of why not use the max batch size, since we will want to ..." (https://github.com/vllm-project/vllm/pull/27904#discussion_r2483174473)
- `2025-11-03T02:53:28Z` `inline` by `nvjullin` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:130; signals: flashinfer, moe; excerpt: "It comes from [PR23608]( After a quick look in flashinfer, I believe this parameter is needed because autotuning on a dummy input won't result ..." (https://github.com/vllm-project/vllm/pull/27904#discussion_r2485199794)
- `2025-11-01T19:09:22Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:141; signals: hang, moe; excerpt: "cc @nvpohanh cc @mgoin changes since you last reviewed." (https://github.com/vllm-project/vllm/pull/27904#discussion_r2483854791)
- `2025-11-01T00:27:49Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:130; signals: moe; excerpt: "Why were we setting this to self.max capture size ? Shouldn't we set this to max num batched tokens atleast ? Just curious cc ..." (https://github.com/vllm-project/vllm/pull/27904#discussion_r2483008109)
- `2025-11-03T01:26:09Z` `inline` by `nvpohanh` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:130; signals: moe; excerpt: "@nvjullin Could you review this PR and comment on this? Thanks!" (https://github.com/vllm-project/vllm/pull/27904#discussion_r2485148577)
