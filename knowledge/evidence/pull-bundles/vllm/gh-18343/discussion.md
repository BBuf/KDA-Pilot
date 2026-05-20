# PR Discussion Digest

- Source PR: [vllm-project/vllm#18343](https://github.com/vllm-project/vllm/pull/18343)
- Source page: `sources/prs/vllm/PR-18343.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-18343`
- Generated at: `2026-05-20T15:35:18.367458+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-19T09:26:42Z`
- Merged: `2025-06-26T22:30:22Z`

## Discussion Counts

- Issue comments: 26
- Review submissions: 16 (approved=1, commented=15)
- Inline review comments: 17
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=6
- Human participants with discussion text: Bounty-hunter, Gongzq5, Lichunyan3, SoonyangZhang, WoosukKwon, abmfy, irenemizus, jiangshibiao, lhsjohn, ljfh001, mergify, wpc, y-null, youkaichao, ztxdcyy
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-05-20T08:01:14Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2853112301)
- `2025-05-20T08:02:33Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2853116823)
- `2025-05-20T16:46:28Z` `COMMENTED` by `abmfy` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2854932589)
- `2025-05-20T16:48:03Z` `COMMENTED` by `abmfy` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2854936186)
- `2025-05-20T16:49:22Z` `COMMENTED` by `abmfy` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2854939387)
- `2025-05-21T23:17:02Z` `COMMENTED` by `wpc` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2859366929)
- `2025-05-21T23:17:58Z` `COMMENTED` by `wpc` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2859368354)
- `2025-05-22T00:13:42Z` `COMMENTED` by `abmfy` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2859430534)
- `2025-05-23T08:28:05Z` `COMMENTED` by `y-null` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2863642431)
- `2025-05-23T18:03:30Z` `COMMENTED` by `abmfy` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2865312916)
- `2025-05-30T06:06:43Z` `COMMENTED` by `jiangshibiao` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2880099741)
- `2025-05-30T16:19:48Z` `COMMENTED` by `abmfy` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2881825254)
- `2025-06-11T01:50:43Z` `COMMENTED` by `Gongzq5` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2915414155)
- `2025-06-12T21:13:31Z` `COMMENTED` by `abmfy` (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2922671539)
- `2025-06-22T22:46:35Z` `COMMENTED` by `WoosukKwon` - @abmfy Great work on the PR! I find it clean and well-organized. I also appreciate the thoughtful handling ... (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2948359000)
- `2025-06-24T17:40:06Z` `APPROVED` by `WoosukKwon` - LGTM! Thanks for the amazing work and let's follow up with more optimizations! (https://github.com/vllm-project/vllm/pull/18343#pullrequestreview-2954754943)

## Inline Comment Hotspots

- `vllm/model_executor/models/deepseek.py`: 6 inline comment(s)
- `vllm/distributed/eplb/rebalance_execute.py`: 6 inline comment(s)
- `vllm/distributed/eplb/states.py`: 2 inline comment(s)
- `vllm/distributed/eplb/eplb_state.py`: 2 inline comment(s)
- `vllm/config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-05-21T23:16:41Z` `inline` by `wpc` `vllm/model_executor/models/deepseek.py`:225; signals: cuda, cudagraph, perf, performance; excerpt: "I think this will introduce gpu to cpu sync and hurt performance? Also do we use cuda graph in vllm? If so local mask.any ..." (https://github.com/vllm-project/vllm/pull/18343#discussion_r2101341772)
- `2025-06-20T09:16:49Z` `issue` by `abmfy`; signals: hang, latency, perf, performance; excerpt: "In my test, it takes seconds to run eplb algorithm. When each GPUModelRunner runns into EplbState.rearrange, why not let each to compute several layers ..." (https://github.com/vllm-project/vllm/pull/18343#issuecomment-2990421681)
- `2025-05-30T03:36:26Z` `inline` by `jiangshibiao` `vllm/distributed/eplb/rebalance_execute.py`:225; signals: block, cute, moe; excerpt: "During this copy stage, what's happening with the ongoing moe forward()? In the same process with automatic blocking, or between different processes with data ..." (https://github.com/vllm-project/vllm/pull/18343#discussion_r2115083369)
- `2025-05-29T16:53:50Z` `issue` by `abmfy`; signals: kernel, perf, performance; excerpt: "Will the load statistics here bring additional performance consumption? Is there a better optimization method? I tested the PyTorch implementation, and the overhead is ..." (https://github.com/vllm-project/vllm/pull/18343#issuecomment-2919999696)
- `2025-06-21T07:50:55Z` `issue` by `abmfy`; signals: accuracy, cute, hang; excerpt: "As for running several layers of eplb on each rank, your implementation is already very well. In my test, eplb algorithm indeed generate duplicate ..." (https://github.com/vllm-project/vllm/pull/18343#issuecomment-2993444720)
- `2025-05-22T00:13:42Z` `inline` by `abmfy` `vllm/model_executor/models/deepseek.py`:225; signals: kernel, moe; excerpt: "Yes, I’ve been transitioning to a new design where the expert load metrics are recorded inFusedMoEModularKernel, since the expert counts are already calculated in" (https://github.com/vllm-project/vllm/pull/18343#discussion_r2101385809)
- `2025-05-30T16:19:48Z` `inline` by `abmfy` `vllm/distributed/eplb/rebalance_execute.py`:225; signals: block, cute; excerpt: "The communications in rearrangement happen in the same process. Ranks in the EP group step the EPLB state synchronously, which blocks forward passes. However, ..." (https://github.com/vllm-project/vllm/pull/18343#discussion_r2116214619)
- `2025-05-20T08:01:14Z` `inline` by `youkaichao` `vllm/distributed/eplb/states.py`:31; signals: perf, performance; excerpt: "can we run the algorithm per-layer? what's the performance impact?" (https://github.com/vllm-project/vllm/pull/18343#discussion_r2097262058)
- `2025-05-21T23:17:58Z` `inline` by `wpc` `vllm/model_executor/models/deepseek.py`:225; signals: kernel, moe; excerpt: "Probably better to passing down and record in fused moe kernel" (https://github.com/vllm-project/vllm/pull/18343#discussion_r2101342700)
- `2025-05-29T08:48:45Z` `issue` by `lhsjohn`; signals: perf, performance; excerpt: "Will the load statistics here bring additional performance consumption? Is there a better optimization method?" (https://github.com/vllm-project/vllm/pull/18343#issuecomment-2918743008)
- `2025-06-17T00:32:56Z` `issue` by `abmfy`; signals: moe, perf; excerpt: "Hi @abmfy 👋, First, thank you for your clever algorithm design and continuous contributions! 🙌 I have two questions about the implementation: 1️⃣ EPLB ..." (https://github.com/vllm-project/vllm/pull/18343#issuecomment-2978557392)
- `2025-06-21T03:30:04Z` `issue` by `abmfy`; signals: hang, latency; excerpt: "In my test, it takes seconds to run eplb algorithm. When each GPUModelRunner runns into EplbState.rearrange, why not let each to compute several layers ..." (https://github.com/vllm-project/vllm/pull/18343#issuecomment-2993290127)
