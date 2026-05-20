# PR Discussion Digest

- Source PR: [vllm-project/vllm#28624](https://github.com/vllm-project/vllm/pull/28624)
- Source page: `sources/prs/vllm/PR-28624.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28624`
- Generated at: `2026-05-20T15:38:31.999137+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-13T07:35:48Z`
- Merged: `2025-12-16T14:10:26Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: chatgpt-codex-connector, ganyi1996ppo, mergify, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-19T07:20:19Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28624#pullrequestreview-3481179470)
- `2025-11-19T08:02:15Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/28624#pullrequestreview-3481324176)
- `2025-11-19T08:03:33Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/28624#pullrequestreview-3481330129)
- `2025-12-16T11:53:41Z` `APPROVED` by `tjtanaa` - LGTM. Thanks for reminding me to review this amazing PR. I don't know how I have missed this. (https://github.com/vllm-project/vllm/pull/28624#pullrequestreview-3582708205)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-12-16T11:57:33Z` `issue` by `tjtanaa`; signals: benchmark, hang, latency, perf, performance, throughput; excerpt: "Adding some more details to make this PR complete. These are the perf improvement on MI300x, under the workload Server command Performance Comparison: No ..." (https://github.com/vllm-project/vllm/pull/28624#issuecomment-3660162974)
- `2025-11-19T07:20:19Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:68; signals: attention, cuda, cudagraph, mla; excerpt: "still reads cudagraph support. As a result this backend reports AttentionCGSupport.NEVER instead of the intended UNIFORM BATCH, so CUDA graph capture is effectively disabled ..." (https://github.com/vllm-project/vllm/pull/28624#discussion_r2540833685)
- `2025-11-19T07:20:19Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:186; signals: attention, memory, mla; excerpt: ". This makes the metadata length equal to max num reqs + 1 while paged kv indptr, paged kv indices, and paged kv last ..." (https://github.com/vllm-project/vllm/pull/28624#discussion_r2540833693)
- `2025-11-19T08:02:15Z` `inline` by `ganyi1996ppo` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:68; signals: attention, mla; excerpt: "Done" (https://github.com/vllm-project/vllm/pull/28624#discussion_r2540942713)
- `2025-11-19T08:03:33Z` `inline` by `ganyi1996ppo` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:186; signals: attention, mla; excerpt: "Thanks for reminding, done." (https://github.com/vllm-project/vllm/pull/28624#discussion_r2540947411)
- `2025-11-19T07:20:19Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28624#pullrequestreview-3481179470)
- `2025-11-20T17:31:38Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @ganyi1996ppo." (https://github.com/vllm-project/vllm/pull/28624#issuecomment-3559246822)
