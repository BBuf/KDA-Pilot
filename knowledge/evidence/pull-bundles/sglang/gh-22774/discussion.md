# PR Discussion Digest

- Source PR: [sgl-project/sglang#22774](https://github.com/sgl-project/sglang/pull/22774)
- Source page: `sources/prs/sglang/PR-22774.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22774`
- Generated at: `2026-05-20T15:29:30.803456+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-14T08:17:14Z`
- Merged: `2026-04-24T01:59:51Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 33
- Review threads observed: 25
- Resolved/outdated thread markers: resolved=25, outdated=21
- Human participants with discussion text: froststeam, popsiclexu, yeahdongcn
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T08:19:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request implements support for the MUSA (Moore Threads) architecture throughout the SGLang runtime, including ... (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4104399252)
- `2026-04-14T11:07:37Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4105335546)
- `2026-04-14T11:19:47Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4105464515)
- `2026-04-14T11:23:50Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4105486174)
- `2026-04-14T11:25:28Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4105494108)
- `2026-04-14T11:27:25Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4105503397)
- `2026-04-14T11:35:41Z` `COMMENTED` by `popsiclexu` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4105545452)
- `2026-04-14T11:36:39Z` `COMMENTED` by `popsiclexu` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4105550931)
- `2026-04-14T15:18:15Z` `COMMENTED` by `popsiclexu` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4107112095)
- `2026-04-14T15:19:00Z` `COMMENTED` by `popsiclexu` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4107117061)
- `2026-04-15T02:08:40Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4110328200)
- `2026-04-15T07:30:55Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4111611747)
- `2026-04-15T07:31:49Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4111623386)
- `2026-04-15T11:28:05Z` `APPROVED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4113093168)
- `2026-04-22T03:00:53Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22774#pullrequestreview-4151833408)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_kernel.py`: 5 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/moe_runner/triton.py`: 3 inline comment(s)
- `python/sglang/srt/model_executor/model_runner.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 3 inline comment(s)
- `python/sglang/srt/layers/activation.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`: 2 inline comment(s)
- `python/sglang/srt/speculative/eagle_info.py`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/topk.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-15T09:55:59Z` `issue` by `yeahdongcn`; signals: aligned, cache, deepgemm, gemm, hang, kernel, tma, triton; excerpt: "LGTM! I believe all changes are guarded by is musa() and should not introduce side effects on other platforms. Highlights for the SGLang core ..." (https://github.com/sgl-project/sglang/pull/22774#issuecomment-4251054878)
- `2026-04-14T11:03:36Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/quantization/fp8_kernel.py`:1118; signals: bf16, fp8, gemm, kernel; excerpt: "Maybe we can add a comment here to clarify that deep gemm fp8 fp8 bf16 nt on MUSA requires contiguous tensors." (https://github.com/sgl-project/sglang/pull/22774#discussion_r3078965518)
- `2026-04-22T03:00:52Z` `inline` by `froststeam` `python/sglang/srt/layers/quantization/fp8_kernel.py`:1118; signals: aligned, fp8, kernel, tma; excerpt: "Here, we actually need to avoid setting column major scales=True and scale tma aligned=True during sglang per token group quant fp8." (https://github.com/sgl-project/sglang/pull/22774#discussion_r3121338631)
- `2026-04-14T11:35:41Z` `inline` by `popsiclexu` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:697; signals: kernel, moe, triton; excerpt: "The judgment of is musa cannot be placed in the Triton kernel. ATOMIC ADD SEM is passed as a parameter." (https://github.com/sgl-project/sglang/pull/22774#discussion_r3079124496)
- `2026-04-14T10:56:18Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`:171; signals: deepgemm, gemm, moe; excerpt: "Can we merge this condition to deep gemm wrapper.DEEPGEMM SCALE UE8M0? I noticed that:" (https://github.com/sgl-project/sglang/pull/22774#discussion_r3078928312)
- `2026-04-15T02:02:30Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`:337; signals: compile, gemm; excerpt: "I think it would be clear to do something like: From the context, I think MUSA doesn't need to use this hook." (https://github.com/sgl-project/sglang/pull/22774#discussion_r3083519465)
- `2026-04-14T11:00:16Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/quantization/fp8_kernel.py`:65; signals: fp8, kernel; excerpt: "Could you double-check this with:" (https://github.com/sgl-project/sglang/pull/22774#discussion_r3078948838)
- `2026-04-14T11:02:28Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/quantization/fp8_kernel.py`:520; signals: fp8, kernel; excerpt: "Chance to merge the condition into enable v2?" (https://github.com/sgl-project/sglang/pull/22774#discussion_r3078960239)
- `2026-04-14T11:19:24Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:697; signals: kernel, moe; excerpt: "Is it correct to use tl.constexpr for ATOMIC ADD SEM?" (https://github.com/sgl-project/sglang/pull/22774#discussion_r3079045547)
- `2026-04-14T15:18:15Z` `inline` by `popsiclexu` `python/sglang/srt/layers/quantization/fp8_kernel.py`:65; signals: fp8, kernel; excerpt: "sgl per tensor quant fp8 was removed" (https://github.com/sgl-project/sglang/pull/22774#discussion_r3080540906)
- `2026-04-15T02:08:05Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`:171; signals: gemm, moe; excerpt: "Do we still need this? We can discuss it offline." (https://github.com/sgl-project/sglang/pull/22774#discussion_r3083545872)
- `2026-04-15T07:31:37Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:670; signals: kernel, moe; excerpt: "atomic-add should be atomic add?" (https://github.com/sgl-project/sglang/pull/22774#discussion_r3084724891)
