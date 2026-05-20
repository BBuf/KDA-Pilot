# PR Discussion Digest

- Source PR: [vllm-project/vllm#34302](https://github.com/vllm-project/vllm/pull/34302)
- Source page: `sources/prs/vllm/PR-34302.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34302`
- Generated at: `2026-05-20T15:39:47.265448+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-11T02:23:15Z`
- Merged: `2026-02-23T14:02:26Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 7 (approved=3, changes_requested=1, commented=3)
- Inline review comments: 9
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=1, outdated=6
- Human participants with discussion text: LucasWilkinson, eugr, mgoin, pavanimajety, robertgshaw2-redhat, stavinsky, xinli-sw
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 8

## Review Decisions

- `2026-02-11T02:25:08Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request ports an optimized router GEMM kernel for DeepSeek V3 MoE models from sglang. ... (https://github.com/vllm-project/vllm/pull/34302#pullrequestreview-3782532956)
- `2026-02-11T04:10:55Z` `APPROVED` by `LucasWilkinson` - Nice! LGTM, thanks! (https://github.com/vllm-project/vllm/pull/34302#pullrequestreview-3782732328)
- `2026-02-11T04:27:13Z` `CHANGES_REQUESTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34302#pullrequestreview-3782744509)
- `2026-02-11T05:14:48Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34302#pullrequestreview-3782852259)
- `2026-02-12T14:21:07Z` `APPROVED` by `mgoin` - LGTM if eval and perf is good (https://github.com/vllm-project/vllm/pull/34302#pullrequestreview-3791306220)
- `2026-02-17T21:34:20Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34302#pullrequestreview-3816419324)
- `2026-02-17T22:08:22Z` `APPROVED` by `mgoin` - LGTM (https://github.com/vllm-project/vllm/pull/34302#pullrequestreview-3816550312)

## Inline Comment Hotspots

- `csrc/moe/dsv3_router_gemm_utils.h`: 3 inline comment(s)
- `csrc/moe/dsv3_router_gemm.cu`: 2 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 2 inline comment(s)
- `CMakeLists.txt`: 1 inline comment(s)
- `csrc/moe/dsv3_router_gemm_entry.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-11T04:27:06Z` `inline` by `mgoin` `csrc/moe/dsv3_router_gemm_entry.cu`:128; signals: gemm, moe, sm120; excerpt: "Do you know if this would work on SM120? Better to be explicit if we don't know" (https://github.com/vllm-project/vllm/pull/34302#discussion_r2791353989)
- `2026-02-11T05:14:48Z` `inline` by `robertgshaw2-redhat` `csrc/moe/dsv3_router_gemm_utils.h`:31; signals: cuda, gemm, moe; excerpt: "any pointer? sorry im not too familiar with the cuda code" (https://github.com/vllm-project/vllm/pull/34302#discussion_r2791449904)
- `2026-02-17T21:34:20Z` `inline` by `robertgshaw2-redhat` `csrc/moe/dsv3_router_gemm_utils.h`:31; signals: cutlass, gemm, moe; excerpt: "I looked into it. Seems like its tied into cutlass, simplified it a bit" (https://github.com/vllm-project/vllm/pull/34302#discussion_r2819190581)
- `2026-02-11T04:18:30Z` `issue` by `robertgshaw2-redhat`; signals: flashinfer, gemm, sm90; excerpt: "Can we use the router gemm interface already present in flashinfer? DSV3 [[DSV3] Optimized Router Gemm flashinfer-ai/flashinfer 2019]( ML3 [[ML3] Optimized Router Gemm flashinfer-ai/flashinfer ..." (https://github.com/vllm-project/vllm/pull/34302#issuecomment-3882032885)
- `2026-02-18T19:51:21Z` `issue` by `xinli-sw`; signals: block, flashinfer, kernel; excerpt: "I think we still expect these kernels to improve and evolve(new HW arch) in FI, it would be great to consider invoking them directly ..." (https://github.com/vllm-project/vllm/pull/34302#issuecomment-3922853090)
- `2026-02-11T04:19:02Z` `inline` by `mgoin` `CMakeLists.txt`:1087; signals: blackwell, cuda; excerpt: "This isn't compatible with CUDA 13 and missing blackwell ultra, should be something like" (https://github.com/vllm-project/vllm/pull/34302#discussion_r2791340479)
- `2026-02-11T04:22:22Z` `inline` by `mgoin` `csrc/moe/dsv3_router_gemm_utils.h`:31; signals: gemm, moe; excerpt: "nit: we should already have a util for this" (https://github.com/vllm-project/vllm/pull/34302#discussion_r2791346175)
- `2026-02-18T17:02:09Z` `issue` by `pavanimajety`; signals: flashinfer, sm100; excerpt: "Hey all, FYI - there's a flashinfer PR ready that removes the restriction for non SM100 in case we want to switch to the ..." (https://github.com/vllm-project/vllm/pull/34302#issuecomment-3922001860)
- `2026-02-11T02:28:18Z` `issue` by `mgoin`; signals: flashinfer, gemm; excerpt: "Can we use the router gemm interface already present in flashinfer? DSV3 ML3" (https://github.com/vllm-project/vllm/pull/34302#issuecomment-3881759496)
- `2026-02-11T04:19:42Z` `inline` by `mgoin` `vllm/model_executor/models/deepseek_v2.py`:246; signals: sm120; excerpt: "This should be current platform.is device capability(90) and current platform.is device capability family(100) since we aren't supporting sm120" (https://github.com/vllm-project/vllm/pull/34302#discussion_r2791341660)
- `2026-02-12T19:05:11Z` `issue` by `pavanimajety`; signals: cuda, kernel; excerpt: "This is a pure cuda kernel, so it should be okay to be used on any architecture" (https://github.com/vllm-project/vllm/pull/34302#issuecomment-3892860534)
- `2026-02-11T04:25:33Z` `issue` by `robertgshaw2-redhat`; signals: bf16; excerpt: "TODO: - conditions for when to deploy [expert size, etc] - see if we should use fp32 or bf16 for non-trtllm" (https://github.com/vllm-project/vllm/pull/34302#issuecomment-3882047009)
