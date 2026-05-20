# PR Discussion Digest

- Source PR: [vllm-project/vllm#27224](https://github.com/vllm-project/vllm/pull/27224)
- Source page: `sources/prs/vllm/PR-27224.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27224`
- Generated at: `2026-05-20T15:38:13.573793+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-20T20:30:40Z`
- Merged: `2025-11-05T15:43:02Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 5 (approved=3, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: HAIAI, chatgpt-codex-connector, ganyi1996ppo, gshtras, mergify, simon-mo, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-20T20:32:14Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables support for block sizes greater than 1 for the AITER MLA backend ... (https://github.com/vllm-project/vllm/pull/27224#pullrequestreview-3357841797)
- `2025-10-20T20:34:54Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/27224#pullrequestreview-3357849254)
- `2025-10-24T10:09:07Z` `APPROVED` by `HAIAI` - LGTM (https://github.com/vllm-project/vllm/pull/27224#pullrequestreview-3375549832)
- `2025-10-24T18:24:27Z` `APPROVED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/27224#pullrequestreview-3378256765)
- `2025-11-03T21:50:42Z` `APPROVED` by `gshtras` (https://github.com/vllm-project/vllm/pull/27224#pullrequestreview-3413057454)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-22T05:25:38Z` `issue` by `tjtanaa`; signals: benchmark, block, fp8, latency, perf, performance, throughput; excerpt: "Just a sharing of the performance metric of this amazing optimization PR. There is improvement even in the original support block-size=1. 🚀 Here's a ..." (https://github.com/vllm-project/vllm/pull/27224#issuecomment-3430555436)
- `2025-10-20T20:34:54Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:149; signals: attention, block, kernel, mla; excerpt: ". Once the remapping is done, each entry represents a single token, so the last-page length for any non-empty request should always be 1. ..." (https://github.com/vllm-project/vllm/pull/27224#discussion_r2446061603)
- `2025-10-22T07:08:07Z` `issue` by `ganyi1996ppo`; signals: benchmark, block, perf, performance; excerpt: "Just a sharing of the performance metric of this amazing optimization PR. There is improvement even in the original support block-size=1. 🚀 @tjtanaa Thanks ..." (https://github.com/vllm-project/vllm/pull/27224#issuecomment-3430773176)
- `2025-10-23T06:13:38Z` `issue` by `ganyi1996ppo`; signals: block, cache, perf, performance; excerpt: "hi @tjtanaa, We tested the performance with 8k/1k and 32/1k configure for different scenario, the block-size=128 seems always get better perf compared with block-size=1 ..." (https://github.com/vllm-project/vllm/pull/27224#issuecomment-3435334633)
- `2025-10-22T07:50:59Z` `issue` by `tjtanaa`; signals: block, perf, performance; excerpt: "@ganyi1996ppo can you share the performance value of your experiment for block-size=128 vs block-size=1?" (https://github.com/vllm-project/vllm/pull/27224#issuecomment-3430893772)
- `2025-10-25T01:47:20Z` `issue` by `ganyi1996ppo`; signals: block, hang, mla; excerpt: "Does this change require any particular AITER version or branch? @gshtras No specific aiter version is required, it just maps block-size 1 block table ..." (https://github.com/vllm-project/vllm/pull/27224#issuecomment-3445451529)
- `2025-10-20T20:34:54Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/27224#pullrequestreview-3357849254)
- `2025-10-24T14:53:39Z` `issue` by `gshtras`; signals: hang; excerpt: "Does this change require any particular AITER version or branch?" (https://github.com/vllm-project/vllm/pull/27224#issuecomment-3443588424)
- `2025-11-03T21:51:19Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @ganyi1996ppo." (https://github.com/vllm-project/vllm/pull/27224#issuecomment-3482738928)
