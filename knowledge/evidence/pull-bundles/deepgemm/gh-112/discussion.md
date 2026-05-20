# PR Discussion Digest

- Source PR: [deepseek-ai/DeepGEMM#112](https://github.com/deepseek-ai/DeepGEMM/pull/112)
- Source page: `sources/prs/deepgemm/PR-112.md`
- Evidence bundle: `evidence/pull-bundles/deepgemm/gh-112`
- Generated at: `2026-05-20T15:21:28.701085+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-12T02:03:59Z`
- Merged: `2025-07-18T03:32:22Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 23 (approved=1, commented=22)
- Inline review comments: 23
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: LyricZhao, RayWang96, fzyzcjy, lucifer1004, simple86, yewentao256, youkaichao, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-12T02:10:50Z` `APPROVED` by `zhyncs` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2919197803)
- `2025-06-12T05:10:14Z` `COMMENTED` by `lucifer1004` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2919562623)
- `2025-06-12T05:19:31Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2919576117)
- `2025-06-12T06:33:51Z` `COMMENTED` by `fzyzcjy` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2919707022)
- `2025-06-12T08:13:13Z` `COMMENTED` by `fzyzcjy` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2920017961)
- `2025-06-12T09:11:00Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2920193815)
- `2025-06-12T09:31:27Z` `COMMENTED` by `fzyzcjy` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2920283868)
- `2025-06-16T19:13:38Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2933220021)
- `2025-06-17T06:36:15Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2934313529)
- `2025-06-17T13:24:03Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2935671359)
- `2025-06-17T23:19:33Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2937305172)
- `2025-06-18T01:13:32Z` `COMMENTED` by `youkaichao` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2937449670)
- `2025-06-18T01:51:10Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2937491410)
- `2025-06-18T02:23:55Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2937543895)
- `2025-06-18T14:13:57Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2939420427)
- `2025-07-03T20:19:52Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2984546758)
- `2025-07-07T02:40:49Z` `COMMENTED` by `simple86` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2992003175)
- `2025-07-07T15:07:41Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2994282713)
- `2025-07-07T15:16:58Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2994313211)
- `2025-07-07T18:05:06Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2994864136)
- `2025-07-07T18:05:53Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-2994865950)
- `2025-07-09T14:15:25Z` `COMMENTED` by `RayWang96` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-3001757418)
- `2025-07-09T23:10:22Z` `COMMENTED` by `yewentao256` (https://github.com/deepseek-ai/DeepGEMM/pull/112#pullrequestreview-3003358449)

## Inline Comment Hotspots

- `deep_gemm/__init__.py`: 7 inline comment(s)
- `tests/test_core.py`: 5 inline comment(s)
- `deep_gemm/utils/layout.py`: 4 inline comment(s)
- `deep_gemm/utils/math.py`: 3 inline comment(s)
- `CMakeLists.txt`: 2 inline comment(s)
- `setup.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-07-02T13:27:11Z` `issue` by `yewentao256`; signals: b200, benchmark, bf16, blackwell, correctness, deepgemm, fp8, gemm; excerpt: "@yewentao256 I read and tried to debug the unit test of VLLM, and I think the problem is that the scale is not being ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#issuecomment-3027890132)
- `2025-07-02T14:03:10Z` `issue` by `RayWang96`; signals: accuracy, b200, bf16, blackwell, correctness, deepgemm, gemm, h100; excerpt: "So the correctness of DeepGemm narrow down to a smaller scope? I am thinking since this is supported on H100, to make sure the ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#issuecomment-3028006591)
- `2025-06-17T06:36:15Z` `inline` by `RayWang96` `deep_gemm/__init__.py`:12; signals: aligned, deepgemm, gemm, layout, sm100, sm90, tma; excerpt: "get col major tma aligned tensor is this function deprecated? Not used in SM100, will be added to utils/layout.py in SM90 support. Is this ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2151437748)
- `2025-07-02T10:28:46Z` `issue` by `RayWang96`; signals: benchmark, bf16, blackwell, deepgemm, fp8, gemm, triton; excerpt: "@yewentao256 I read and tried to debug the unit test of VLLM, and I think the problem is that the scale is not being ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#issuecomment-3027324053)
- `2025-06-25T18:27:31Z` `issue` by `yewentao256`; signals: accuracy, b200, deepgemm, gemm, h100; excerpt: "Added unit test in vllm that may be helpful. This unit test can pass on H100. But for B200 of your integration, it can ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#issuecomment-3005746833)
- `2025-06-18T02:23:55Z` `inline` by `RayWang96` `deep_gemm/__init__.py`:12; signals: fp8, gemm, kernel, layout; excerpt: "fp8 gemm nt can implicitly handle the transformation, or this step can be skipped to only validate the layout. It's recommended to use a ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2153503399)
- `2025-07-07T15:07:41Z` `inline` by `RayWang96` `deep_gemm/utils/math.py`:15; signals: gemm, kernel, perf, performance; excerpt: "Thanks, this function is primarily intended for testing purposes. For performance optimization, a custom implementation should be considered, potentially fused into other kernels." (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2190361732)
- `2025-06-12T06:33:48Z` `inline` by `fzyzcjy` `deep_gemm/utils/layout.py`:136; signals: gemm, kernel, layout; excerpt: "would be great to allow skipping (INT, 128, 128) case where the data is already pre-transformed by other fused kernels. For example, my patch:" (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2141824027)
- `2025-06-18T14:13:53Z` `inline` by `yewentao256` `deep_gemm/__init__.py`:12; signals: aligned, gemm, tma; excerpt: "So do you mean it is recommended that we call this get col major tma aligned tensor each time before we call any gemm ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2154724678)
- `2025-06-16T19:12:12Z` `inline` by `yewentao256` `deep_gemm/__init__.py`:12; signals: aligned, gemm, tma; excerpt: "get col major tma aligned tensor is this function deprecated?" (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2150681938)
- `2025-06-12T09:11:00Z` `inline` by `RayWang96` `deep_gemm/utils/layout.py`:136; signals: gemm, layout; excerpt: "That makes sense. I'm thinking about how to skip transform in the most appropriate way, but for now, let me merge your patch as ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2142132407)
- `2025-06-17T23:19:32Z` `inline` by `yewentao256` `deep_gemm/__init__.py`:12; signals: gemm, sm100; excerpt: "@RayWang96 When you said not used in SM100, does this mean it will be automatically handled in SM100 and we don't need the code ..." (https://github.com/deepseek-ai/DeepGEMM/pull/112#discussion_r2153317583)
