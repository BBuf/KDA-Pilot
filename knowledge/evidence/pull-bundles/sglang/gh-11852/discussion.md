# PR Discussion Digest

- Source PR: [sgl-project/sglang#11852](https://github.com/sgl-project/sglang/pull/11852)
- Source page: `sources/prs/sglang/PR-11852.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11852`
- Generated at: `2026-05-20T15:27:29.902543+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-20T07:29:30Z`
- Merged: `2025-12-12T04:54:17Z`

## Discussion Counts

- Issue comments: 26
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: MichoChan, ShangmingCai, XucSh, bluecoffee8, nvpohanh, weireweire, whybeyoung, zhangxiaolei123456
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-10-20T07:31:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the pipeline parallelism (PP) logic into a new SchedulerPPMixin and adds support ... (https://github.com/sgl-project/sglang/pull/11852#pullrequestreview-3355294255)
- `2025-11-29T09:45:16Z` `COMMENTED` by `MichoChan` (https://github.com/sgl-project/sglang/pull/11852#pullrequestreview-3520616676)
- `2025-12-12T04:52:44Z` `APPROVED` by `ShangmingCai` - We think this PR is ready for public testing now. Please ping me in the comment of (or ... (https://github.com/sgl-project/sglang/pull/11852#pullrequestreview-3570284612)

## Inline Comment Hotspots

- `python/sglang/srt/managers/scheduler_pp_mixin.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-11-04T13:10:10Z` `issue` by `zhangxiaolei123456`; signals: attention, benchmark, cache, cutlass, dtype, fp8, hang, moe; excerpt: "hi @XucSh @ShangmingCai @whybeyoung you can test use this command, I think this bubble is very small SGLANG PP LAYER PARTITION="3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,3" SGLANG CUTLASS MOE=1 ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3485937871)
- `2025-11-04T13:16:52Z` `issue` by `XucSh`; signals: attention, benchmark, cache, cutlass, dtype, fp8, hang, moe; excerpt: "hi @XucSh @ShangmingCai you can test use this command SGLANG PP LAYER PARTITION="3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,3" SGLANG CUTLASS MOE=1 GLOO SOCKET IFNAME=eth0 NCCL IB HCA=mlx5 NCCL IB ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3485964713)
- `2025-11-06T11:31:57Z` `issue` by `zhangxiaolei123456`; signals: block, cache, compile, cuda, hang, kernel, latency, memory; excerpt: "@ShangmingCai @bluecoffee8 I test different sequence length use '--num-prompts 1 --random-input-len sequence length --random-output-len 1' we use chunked prefill size = 1024 Sequence length ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3496730120)
- `2025-11-10T09:30:32Z` `issue` by `zhangxiaolei123456`; signals: attention, block, cuda, hang, kernel; excerpt: "Could you run with CUDA LAUNCH BLOCKING=1 to see which cuda kernel causes the illegal mem access? I am suspecting that SGL didn't reserve ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3510424062)
- `2025-10-24T04:54:06Z` `issue` by `bluecoffee8`; signals: benchmark, cache, compile, h100; excerpt: "H100 80G 8 benchmark: model: qwen3-8b commands: python -m sglang.launch server --model-path /path/to/Qwen3-8B --disable-radix-cache --pp-size 4 --trust-remote --host 0.0.0.0 --port 8001 --mem-fraction-static 0.8 --tokenizer-worker-num ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3441061861)
- `2025-11-05T10:02:22Z` `issue` by `ShangmingCai`; signals: benchmark, hang, tile; excerpt: "python3 benchmark serving.py --backend vllm --model /data00/DeepSeek-R1-0528/ --base-url --endpoint /v1/completions --num-prompts 512 --request-rate 10 --metric percentiles '50,90,95,99' --goodput ttft:5000 tpot:50 --max-concurrency 512 --random-input-len 3500 ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3490290204)
- `2025-11-07T01:32:12Z` `issue` by `nvpohanh`; signals: block, cuda, kernel; excerpt: "Could you run with CUDA LAUNCH BLOCKING=1 to see which cuda kernel causes the illegal mem access? I am suspecting that SGL didn't reserve ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3500085446)
- `2025-11-10T09:57:34Z` `issue` by `ShangmingCai`; signals: attention, hang, memory; excerpt: "The sending and receiving of bubbles occurs because attention calculations take varying amounts of time when processing chunked data, resulting in waiting periods between ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3510557750)
- `2025-11-21T01:35:05Z` `issue` by `nvpohanh`; signals: hang, perf, performance; excerpt: "@ShangmingCai @ByronHsu @zhyncs could you review this? We found that this PR significantly improves SGLang's PP performance. Thanks!" (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3560948364)
- `2025-11-21T05:34:35Z` `issue` by `ShangmingCai`; signals: hang, perf, performance; excerpt: "@ShangmingCai @ByronHsu @zhyncs could you review this? We found that this PR significantly improves SGLang's PP performance. Thanks! @nvpohanh We are pretty close to ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3561467556)
- `2025-10-22T10:21:24Z` `issue` by `whybeyoung`; signals: cache, compile; excerpt: "here is the benmark result in a800 80G 8 model: qwen3-8b sglangserver: python -m sglang.launch server --model-path /work/models/qwen8b --disable-radix-cache --pp-size 4 --trust-remote --host 0.0.0.0 ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3431597848)
- `2025-11-04T09:41:24Z` `issue` by `ShangmingCai`; signals: hang, race; excerpt: "2025-11-03 11:53:19 TP1 PP0] Scheduler hit an exception: Traceback (most recent call last): File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 2795, in run scheduler process scheduler.event loop pp ..." (https://github.com/sgl-project/sglang/pull/11852#issuecomment-3484922606)
