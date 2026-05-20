# PR Discussion Digest

- Source PR: [sgl-project/sglang#6081](https://github.com/sgl-project/sglang/pull/6081)
- Source page: `sources/prs/sglang/PR-6081.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6081`
- Generated at: `2026-05-20T15:30:36.116924+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-07T08:40:09Z`
- Merged: `2025-06-17T07:33:28Z`

## Discussion Counts

- Issue comments: 71
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 12
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=4
- Human participants with discussion text: DeepTecher, GaoYusong, LiHao217, Qiaolin-Yu, TianQiLin666666, UnlceYang, Xuweijia-buaa, ZhenweiCao, ch-wan, hebiao064, lambert0312, miter6, pengchengneo, u4lr451, whybeyoung, yudian0504, zhangxiaolei123456, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-05-08T03:27:07Z` `COMMENTED` by `DeepTecher` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2823704824)
- `2025-05-08T17:01:33Z` `COMMENTED` by `u4lr451` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2825804380)
- `2025-05-09T01:39:46Z` `COMMENTED` by `DeepTecher` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2826748162)
- `2025-05-09T16:58:54Z` `COMMENTED` by `u4lr451` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2829084198)
- `2025-05-31T17:41:10Z` `COMMENTED` by `yudian0504` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2884378866)
- `2025-06-11T09:08:08Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2916248654)
- `2025-06-11T12:47:11Z` `COMMENTED` by `u4lr451` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2916994949)
- `2025-06-15T06:09:55Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2928995867)
- `2025-06-15T06:26:37Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2928998626)
- `2025-06-17T03:46:06Z` `COMMENTED` by `u4lr451` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2934046367)
- `2025-06-17T03:46:32Z` `COMMENTED` by `u4lr451` (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2934046798)
- `2025-06-17T06:38:03Z` `APPROVED` by `ch-wan` - Thank you for this excellent contribution. It represents a major optimization for boosting the throughput of DeepSeek-V3/R1, with ... (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2934318682)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_nextn.py`: 2 inline comment(s)
- `python/sglang/srt/speculative/eagle_utils.py`: 2 inline comment(s)
- `python/sglang/srt/layers/communicator.py`: 2 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 2 inline comment(s)
- `python/sglang/srt/model_executor/cuda_graph_runner.py`: 2 inline comment(s)
- `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/aiter_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-05-14T02:23:59Z` `issue` by `zhangxiaolei123456`; signals: attention, benchmark, cache, cuda, deepgemm, gemm, moe, tile; excerpt: "launch command Node1 GLOO SOCKET IFNAME=eth0 NCCL IB HCA=mlx5 NCCL IB DISABLE=0 NCCL SOCKET IFNAME=eth0 NCCL IB GID INDEX=3 MODEL LENGTH=131072 NCCL MIN NCHANNELS=24 ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2878446310)
- `2025-05-14T14:46:40Z` `issue` by `u4lr451`; signals: attention, benchmark, cache, cuda, deepgemm, gemm, hang, moe; excerpt: "launch command Node1 GLOO SOCKET IFNAME=eth0 NCCL IB HCA=mlx5 NCCL IB DISABLE=0 NCCL SOCKET IFNAME=eth0 NCCL IB GID INDEX=3 MODEL LENGTH=131072 NCCL MIN NCHANNELS=24 ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2880526072)
- `2025-05-08T17:08:09Z` `issue` by `u4lr451`; signals: block, compile, cuda, kernel, memory, race; excerpt: "After testing, the error is as follows: `` Scheduler hit an exception: Traceback (most recent call last): File "/sgl-workspace/sglang/python/sglang/srt/model executor/cuda graph runner.py", line 314, ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2863733944)
- `2025-05-13T18:21:45Z` `issue` by `u4lr451`; signals: attention, cuda, hang, perf, performance, throughput; excerpt: "Open DP attention, MTP, cuda graph found that the performance dropped very much, analyzed and found that it was because the reception rate dropped ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2877536400)
- `2025-06-17T06:38:03Z` `review` `APPROVED` by `ch-wan`; signals: attention, block, correctness, cuda, memory, throughput; excerpt: "Thank you for this excellent contribution. It represents a major optimization for boosting the throughput of DeepSeek-V3/R1, with its correctness and effectiveness verified by ..." (https://github.com/sgl-project/sglang/pull/6081#pullrequestreview-2934318682)
- `2025-05-13T02:41:04Z` `issue` by `zhangxiaolei123456`; signals: attention, cuda, perf, performance, throughput; excerpt: "Open DP attention, MTP, cuda graph found that the performance dropped very much, analyzed and found that it was because the reception rate dropped ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2874900998)
- `2025-05-13T17:35:56Z` `issue` by `hebiao064`; signals: attention, cuda, perf, performance, throughput; excerpt: "Open DP attention, MTP, cuda graph found that the performance dropped very much, analyzed and found that it was because the reception rate dropped ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2877421740)
- `2025-05-27T08:57:52Z` `issue` by `ZhenweiCao`; signals: attention, cuda, flashinfer, moe; excerpt: "Hi @u4lr451 , I test sglang with the command python3 -m sglang.launch server --cuda-graph-bs 1 2 3 4 5 6 7 8 9 10 ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2911733211)
- `2025-05-29T04:53:54Z` `issue` by `u4lr451`; signals: attention, cuda, flashinfer, moe; excerpt: "Hi @u4lr451 , I test sglang with the command python3 -m sglang.launch server --cuda-graph-bs 1 2 3 4 5 6 7 8 9 10 ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2918291389)
- `2025-05-31T17:31:01Z` `issue` by `u4lr451`; signals: attention, correctness, cuda, hang; excerpt: "@zhyncs @ch-wan @zhaochenyang20 Updates: The MTP now supports dp-attention, and both acceptance rates and correctness are functioning properly regardless of whether CUDA Graph is ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2925483715)
- `2025-05-31T18:36:02Z` `issue` by `GaoYusong`; signals: attention, correctness, cuda, hang; excerpt: "@zhyncs @ch-wan @zhaochenyang20 Updates: The MTP now supports dp-attention, and both acceptance rates and correctness are functioning properly regardless of whether CUDA Graph is ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2925550938)
- `2025-06-04T19:47:10Z` `issue` by `ZhenweiCao`; signals: attention, cuda, cute, flashinfer; excerpt: "Thanks for your work on this—I’m excited to try out this feature! However, I ran into a problem while testing it. When I executed ..." (https://github.com/sgl-project/sglang/pull/6081#issuecomment-2941268896)
