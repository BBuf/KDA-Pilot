# PR Discussion Digest

- Source PR: [vllm-project/vllm#21465](https://github.com/vllm-project/vllm/pull/21465)
- Source page: `sources/prs/vllm/PR-21465.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21465`
- Generated at: `2026-05-20T15:36:42.999162+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-23T15:01:56Z`
- Merged: `2025-07-24T15:13:24Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: ElizaWszola, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-23T15:04:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a critical "illegal memory access" bug in the NVFP4 MoE kernel. The ... (https://github.com/vllm-project/vllm/pull/21465#pullrequestreview-3047863649)
- `2025-07-23T15:07:31Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/21465#pullrequestreview-3047875902)
- `2025-07-23T20:12:41Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/21465#pullrequestreview-3048869318)
- `2025-07-24T04:25:16Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/21465#pullrequestreview-3049927051)
- `2025-07-24T14:22:24Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21465#pullrequestreview-3051901785)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`: 3 inline comment(s)

## High-Signal Discussion

- `2025-07-23T15:07:31Z` `inline` by `ElizaWszola` `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`:122; signals: block, cutlass, fp8, moe; excerpt: "Would it make sense to rather add a boolean argument to get cutlass moe mm data() that forces no swap? Looks like disabling swap ..." (https://github.com/vllm-project/vllm/pull/21465#discussion_r2225899496)
- `2025-07-23T20:12:41Z` `inline` by `yewentao256` `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`:122; signals: block, cutlass, fp8, moe; excerpt: "run cutlass moe fp8 run cutlass block scaled fused experts which path are you taking about? I don't have enough context so I am ..." (https://github.com/vllm-project/vllm/pull/21465#discussion_r2226556307)
- `2025-07-24T04:25:15Z` `inline` by `ElizaWszola` `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`:122; signals: block, cutlass, hang, moe; excerpt: "I mean a get cutlass moe mm data() call in run cutlass block scaled fused experts() :) But I can add that change to ..." (https://github.com/vllm-project/vllm/pull/21465#discussion_r2227300222)
- `2025-07-23T21:00:14Z` `issue` by `yewentao256`; signals: fp4, kernel; excerpt: "Can you check if this fails with modelopt fp4 as well since it should use the same kernel? nvidia/DeepSeek-R1-0528-FP4 This one will not cause ..." (https://github.com/vllm-project/vllm/pull/21465#issuecomment-3110158591)
- `2025-07-23T15:53:44Z` `issue` by `mgoin`; signals: fp4, kernel; excerpt: "Can you check if this fails with modelopt fp4 as well since it should use the same kernel?" (https://github.com/vllm-project/vllm/pull/21465#issuecomment-3109215391)
