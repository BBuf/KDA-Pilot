# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1696](https://github.com/flashinfer-ai/flashinfer/pull/1696)
- Source page: `sources/prs/flashinfer/PR-1696.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1696`
- Generated at: `2026-05-20T15:23:17.741804+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-16T22:51:04Z`
- Merged: `2025-09-17T23:04:13Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 8 (approved=3, changes_requested=1, commented=4)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: GordonGustafson, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-16T22:51:21Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @GordonGustafson, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3231934477)
- `2025-09-16T22:53:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the MoE routing kernels to support a configurable number of experts by ... (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3231938720)
- `2025-09-16T22:54:00Z` `COMMENTED` by `GordonGustafson` (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3231939287)
- `2025-09-17T01:01:50Z` `APPROVED` by `yzh119` - LGTM (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3232128260)
- `2025-09-17T04:08:07Z` `CHANGES_REQUESTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3232587819)
- `2025-09-17T19:15:43Z` `COMMENTED` by `GordonGustafson` (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3235904387)
- `2025-09-17T19:22:47Z` `APPROVED` by `zhyncs` (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3235926789)
- `2025-09-17T23:04:11Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1696#pullrequestreview-3236515858)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_routing_renormalize.cu`: 4 inline comment(s)
- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 1 inline comment(s)
- `csrc/trtllm_fused_moe_routing_llama4.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-16T22:54:00Z` `inline` by `GordonGustafson` `csrc/trtllm_fused_moe_routing_renormalize.cu`:312; signals: compile, kernel, moe; excerpt: "I'm not familiar enough with the all the models to known which values to include here. Please let me know if you have suggestions! ..." (https://github.com/flashinfer-ai/flashinfer/pull/1696#discussion_r2353824187)
- `2025-09-17T04:08:05Z` `inline` by `yzh119` `csrc/trtllm_fused_moe_routing_renormalize.cu`:312; signals: blackwell, moe; excerpt: "Blackwell UTs failed with error: Seems we should also add number of experts for 384 experts under different TP/EP settings." (https://github.com/flashinfer-ai/flashinfer/pull/1696#discussion_r2354245744)
- `2025-09-17T19:41:51Z` `issue` by `GordonGustafson`; signals: fp4, fp8; excerpt: "Please don't merge yet, I'm still doing some testing EDIT: testing is done, tried it on Kimi-K2 and DeepSeek for both fp4 and fp8 ..." (https://github.com/flashinfer-ai/flashinfer/pull/1696#issuecomment-3304340316)
- `2025-09-17T01:01:40Z` `inline` by `yzh119` `csrc/trtllm_fused_moe_routing_renormalize.cu`:312; signals: moe; excerpt: "Let's keep this as is until we reach a case not captured here." (https://github.com/flashinfer-ai/flashinfer/pull/1696#discussion_r2353960755)
- `2025-09-17T19:15:43Z` `inline` by `GordonGustafson` `csrc/trtllm_fused_moe_routing_renormalize.cu`:312; signals: moe; excerpt: "Addressed, I added 384/{1,2,4,8,16}, 256, and 72." (https://github.com/flashinfer-ai/flashinfer/pull/1696#discussion_r2356516454)
