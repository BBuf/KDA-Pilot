# PR Discussion Digest

- Source PR: [vllm-project/vllm#20833](https://github.com/vllm-project/vllm/pull/20833)
- Source page: `sources/prs/vllm/PR-20833.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20833`
- Generated at: `2026-05-20T15:36:16.611498+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-11T17:49:57Z`
- Merged: `2025-07-12T06:05:13Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: WoosukKwon, mgoin, smarterclayton, yewentao256
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-11T17:50:27Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yewentao256, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20833#pullrequestreview-3011378987)
- `2025-07-11T17:51:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a TypeError when using DeepGEMM in the expert-parallel low-latency case. It also ... (https://github.com/vllm-project/vllm/pull/20833#pullrequestreview-3011381820)
- `2025-07-11T18:02:44Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/20833#pullrequestreview-3011401510)
- `2025-07-11T18:54:52Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20833#pullrequestreview-3011547188)
- `2025-07-11T18:55:05Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20833#pullrequestreview-3011547869)
- `2025-07-11T18:58:14Z` `APPROVED` by `mgoin` - Thanks LGTM (https://github.com/vllm-project/vllm/pull/20833#pullrequestreview-3011557708)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-07-11T18:02:42Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:165; signals: gemm, hang, kernel, moe; excerpt: "Why can't you just add this as a conditional to the original kernel and pass in use e8m0 as a constant bool i.e. use ..." (https://github.com/vllm-project/vllm/pull/20833#discussion_r2201458631)
- `2025-07-11T20:32:58Z` `issue` by `yewentao256`; signals: accuracy, b200, deepgemm, gemm; excerpt: "Just curious: Isn't 6% accuracy diff in gsm8k-strict significant? Is it acceptable? There is a auccracy loss for DeepGemm on B200 currently, If you ..." (https://github.com/vllm-project/vllm/pull/20833#issuecomment-3063737043)
- `2025-07-11T20:35:29Z` `issue` by `mgoin`; signals: deepgemm, gemm, sm100; excerpt: "Yeah what Wentao said is correct. It is the unfortunate result of DeepGEMM switching from float to E8M0 scales for SM100." (https://github.com/vllm-project/vllm/pull/20833#issuecomment-3063745155)
- `2025-07-11T18:00:17Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:380; signals: gemm, moe; excerpt: "Good bot!" (https://github.com/vllm-project/vllm/pull/20833#discussion_r2201455282)
- `2025-07-11T18:54:52Z` `inline` by `yewentao256` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:380; signals: gemm, moe; excerpt: "Nice catch! Fixed" (https://github.com/vllm-project/vllm/pull/20833#discussion_r2201549404)
- `2025-07-11T18:55:05Z` `inline` by `yewentao256` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:165; signals: gemm, moe; excerpt: "Sounds great! Fixed" (https://github.com/vllm-project/vllm/pull/20833#discussion_r2201549984)
- `2025-07-11T18:12:02Z` `issue` by `smarterclayton`; signals: b200; excerpt: "This fixed the failure I was seeing in the B200 DP=16,EP=16 2 node configuration." (https://github.com/vllm-project/vllm/pull/20833#issuecomment-3063262107)
- `2025-07-11T20:21:49Z` `issue` by `WoosukKwon`; signals: accuracy; excerpt: "Just curious: Isn't 6% accuracy diff in gsm8k-strict significant? Is it acceptable?" (https://github.com/vllm-project/vllm/pull/20833#issuecomment-3063711092)
