# PR Discussion Digest

- Source PR: [sgl-project/sglang#10275](https://github.com/sgl-project/sglang/pull/10275)
- Source page: `sources/prs/sglang/PR-10275.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10275`
- Generated at: `2026-05-20T15:27:16.568503+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-10T14:48:33Z`
- Merged: `2025-11-25T02:49:39Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: BBuf, FlamingoPg, ch-wan, jdemouth-nvidia, nvcastet, samuellees, trevor-m, yizhang2077, yuan-luo, zhendonghua, zhyncs
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-10T14:48:48Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @nvcastet, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3206542559)
- `2025-09-10T14:50:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for bfloat16 fused Mixture-of-Experts (MoE) layers using FlashInfer's Cutlass kernels. The ... (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3206550748)
- `2025-09-15T02:29:29Z` `COMMENTED` by `ch-wan` - Thank you for your contribution. I left some comments. Also, is Fp8 support in your plan? (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3222737209)
- `2025-09-17T04:54:41Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3232649820)
- `2025-10-24T02:41:17Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3374070473)
- `2025-10-27T18:58:14Z` `COMMENTED` by `nvcastet` (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3385022449)
- `2025-11-24T02:47:05Z` `APPROVED` by `yizhang2077` - LGTM overall. (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3498215991)
- `2025-11-24T03:02:21Z` `COMMENTED` by `zhendonghua` (https://github.com/sgl-project/sglang/pull/10275#pullrequestreview-3498244061)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/unquant.py`: 6 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-12T13:01:34Z` `issue` by `samuellees`; signals: benchmark, cutlass, flashinfer, h200, latency, perf, performance, throughput; excerpt: "Do you have any performance benchmark comparison results to report? Such as model . Yeah, it will bring e2e benefits for Qwen3-Next. I"ll post ..." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3285205610)
- `2025-09-18T10:05:36Z` `issue` by `yuan-luo`; signals: cutlass, flashinfer, fp4, hang, kernel, moe; excerpt: "This is a new feature, I think we'd better add a new file flashinfer cutlass moe.py on the python/sglang/srt/layers/moe/ directory. HI @yuan-luo we already ..." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3306610807)
- `2025-09-14T12:24:25Z` `issue` by `yuan-luo`; signals: benchmark, compile, cutlass, moe, triton; excerpt: "Could you add a benchmark test between cutlass and triton fused moe just like benchmark vllm vs sglang fused moe triton.py and benchmark torch ..." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3289500398)
- `2025-09-16T15:33:53Z` `issue` by `samuellees`; signals: accuracy, b200, perf, performance, throughput; excerpt: "Performance on B200, output throughput improves 12%: Accuracy on B200 gsm8k: Code refactoring is on the way. cc @zhyncs" (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3299316002)
- `2025-09-17T18:21:15Z` `issue` by `trevor-m`; signals: cutlass, flashinfer, fp4, hang, moe; excerpt: "This is a new feature, I think we'd better add a new file flashinfer cutlass moe.py on the python/sglang/srt/layers/moe/ directory. HI @yuan-luo we already ..." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3304099398)
- `2025-09-14T12:45:08Z` `issue` by `yuan-luo`; signals: cutlass, flashinfer, moe; excerpt: "This is a new feature, I think we'd better add a new file flashinfer cutlass moe.py on the python/sglang/srt/layers/moe/ directory." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3289516932)
- `2025-10-02T11:29:56Z` `issue` by `jdemouth-nvidia`; signals: cutlass, flashinfer, moe; excerpt: "@yuan-luo , we'd like to move forward with this PR. For that, I'd like to understand your comment better: Are you suggesting that we ..." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3360712314)
- `2025-09-12T08:34:00Z` `issue` by `BBuf`; signals: benchmark, perf, performance; excerpt: "Do you have any performance benchmark comparison results to report? Such as model ." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3284305169)
- `2025-09-17T04:54:41Z` `inline` by `samuellees` `python/sglang/srt/server_args.py`:1472; signals: bf16, moe; excerpt: "Thanks. I want to ensure the types of activation and weight of MoE are both fp16/bf16, do you have any suggestion here? @ch-wan" (https://github.com/sgl-project/sglang/pull/10275#discussion_r2354296894)
- `2025-10-24T02:35:24Z` `issue` by `yizhang2077`; signals: bf16, cutlass, flashinfer; excerpt: "sorry for late reply, could we add some ut about flashinfer cutlass bf16?" (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3440550689)
- `2025-10-27T18:58:13Z` `inline` by `nvcastet` `python/sglang/srt/layers/quantization/unquant.py`:244; signals: kernel, layout; excerpt: "Yes it is at to figure out the weight layout this kernel requires." (https://github.com/sgl-project/sglang/pull/10275#discussion_r2466758398)
- `2025-09-14T09:39:51Z` `issue` by `zhyncs`; signals: accuracy, b200; excerpt: "@samuellees Great work! Can you test it on the b200? Thanks! Also, we need to ensure the accuracy is correct." (https://github.com/sgl-project/sglang/pull/10275#issuecomment-3289396931)
