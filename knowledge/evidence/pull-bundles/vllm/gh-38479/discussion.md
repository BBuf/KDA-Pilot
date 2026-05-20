# PR Discussion Digest

- Source PR: [vllm-project/vllm#38479](https://github.com/vllm-project/vllm/pull/38479)
- Source page: `sources/prs/vllm/PR-38479.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38479`
- Generated at: `2026-05-20T15:40:34.879172+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-29T15:36:29Z`
- Merged: `2026-04-15T02:57:14Z`

## Discussion Counts

- Issue comments: 110
- Review submissions: 42 (approved=2, commented=40)
- Inline review comments: 78
- Review threads observed: 47
- Resolved/outdated thread markers: resolved=16, outdated=32
- Human participants with discussion text: Alberto-Codes, Cklaus1, HelloWorldU, JianDan0212, MidasMining, Sggin1, TheTom, brisker, brucechanglongxu, claude, darthsider, domvox, gaby, huangzhilin-hzl, jagmarques, lishunyang12, mgoin, naroam1, seasoncool, sweihub
- Automation comments/reviews omitted from high-signal summary: 16
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 11

## Review Decisions

- `2026-03-29T15:36:32Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4026895466)
- `2026-03-29T15:40:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request implements TurboQuant, a near-optimal KV-cache quantization scheme for vLLM, including new cache types ... (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4026898508)
- `2026-03-30T21:53:48Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4033016886)
- `2026-04-02T02:43:22Z` `COMMENTED` by `yangyang-cs95` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4048040470)
- `2026-04-02T02:46:17Z` `COMMENTED` by `yangyang-cs95` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4048046686)
- `2026-04-02T02:48:37Z` `COMMENTED` by `yangyang-cs95` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4048052152)
- `2026-04-05T11:48:58Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4059404080)
- `2026-04-05T11:49:09Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4059404208)
- `2026-04-05T11:49:30Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4059404477)
- `2026-04-05T11:49:51Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4059405427)
- `2026-04-05T11:50:22Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4059406125)
- `2026-04-05T11:51:47Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4059407507)
- `2026-04-05T11:51:55Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4059407575)
- `2026-04-07T02:55:54Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4058573496)
- `2026-04-08T12:46:24Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075164952)
- `2026-04-08T12:46:31Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075165607)
- `2026-04-08T12:47:03Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075168665)
- `2026-04-08T12:47:09Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075169279)
- `2026-04-08T14:32:32Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075893263)
- `2026-04-08T14:33:40Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075900927)
- `2026-04-08T14:34:16Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075904813)
- `2026-04-08T14:36:06Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4075917154)
- `2026-04-08T16:11:41Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4076516151)
- `2026-04-08T20:01:35Z` `COMMENTED` by `vibhavagarwal5` (https://github.com/vllm-project/vllm/pull/38479#pullrequestreview-4077901640)
- ... 18 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/v1/attention/backends/turboquant_attn.py`: 24 inline comment(s)
- `vllm/engine/arg_utils.py`: 8 inline comment(s)
- `vllm/config/cache.py`: 6 inline comment(s)
- `vllm/model_executor/layers/quantization/turboquant/centroids.py`: 4 inline comment(s)
- `vllm/v1/attention/ops/triton_turboquant_store.py`: 4 inline comment(s)
- `vllm/v1/attention/ops/csrc/tq_store_cuda.cu`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/turboquant/config.py`: 3 inline comment(s)
- `tests/quantization/test_turboquant.py`: 3 inline comment(s)
- `vllm/turboquant/__init__.py`: 2 inline comment(s)
- `vllm/v1/attention/ops/csrc/tq_decode_warp_per_head.cu`: 2 inline comment(s)
- `vllm/v1/attention/ops/triton_tq_decode.py`: 2 inline comment(s)
- `vllm/v1/attention/ops/triton_tq_store.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-31T02:40:02Z` `issue` by `Sggin1`; signals: cache, compile, cuda, dtype, flashinfer, fp4, fp8, kernel; excerpt: "Tested this on DGX Spark (GB10, SM121, 128 GB unified memory, aarch64) with Nemotron-3-Nano-30B-A3B-NVFP4. Applied the patch to vllm-node (eugr community build, vLLM 0.18.1rc1 ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4159455083)
- `2026-03-31T12:40:44Z` `issue` by `MidasMining`; signals: attention, benchmark, cache, fp8, hang, hopper, kernel, kv cache; excerpt: "Ampere (SM86) Compatibility + Quality Fix Tested this PR on 8x RTX A4000 (SM86) with Nemotron-Cascade-2-30B-A3B (hybrid Mamba+MoE+Attention, head dim=128). A few findings: FP8 ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4162361617)
- `2026-04-02T02:29:06Z` `issue` by `Cklaus1`; signals: attention, cache, fp4, fp8, kernel, kv cache, nvfp4, sm120; excerpt: "Following this with interest for RTX 5090 (SM120) + Qwen3.5-9B hybrid workloads. The 4x KV cache on hybrid attention is exactly what we need ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4174211845)
- `2026-04-03T18:14:10Z` `issue` by `Cklaus1`; signals: accuracy, attention, blackwell, cache, gemm, hang, kernel, kv cache; excerpt: "Bug Report: 3 Critical Bugs Found in TurboQuant Implementation I've been testing this patch on an RTX 5090 (Blackwell SM120) with vLLM 0.19.0 and ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4184609256)
- `2026-04-04T14:45:31Z` `issue` by `vibhavagarwal5`; signals: attention, benchmark, blackwell, cache, cuda, dtype, flash attention, fp8; excerpt: "Update: Named Presets, Bug Fixes, Quality + Performance Validation Hey all — as promised, here's the update covering the changes since my last message. ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4187218792)
- `2026-04-04T21:35:06Z` `issue` by `Alberto-Codes`; signals: attention, cache, compile, cuda, deadlock, dtype, gemm, kernel; excerpt: "Retest: transformers 5.5.0 fixes the architecture error, but tq-t4nc + Gemma 4 E4B-it hits a deeper deadlock Stood up a fresh env per @gaby's ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4187784235)
- `2026-04-05T11:16:26Z` `issue` by `wizzense`; signals: attention, benchmark, bf16, cache, compile, cuda, dtype, flashinfer; excerpt: "Benchmark Results: tq-t4nc on latest code Tested the latest commit (e724fc4) on a fresh RTX 3090 (Vast.ai, 24GB). Setup - Model : Qwen/Qwen2.5-1.5B-Instruct (BF16 ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4188726301)
- `2026-04-06T17:48:36Z` `issue` by `Alberto-Codes`; signals: attention, benchmark, cache, fp8, gemm, hang, moe, triton; excerpt: "Gemma 4 now works with TurboQuant. The fork PR (vibhavagarwal5/vllm 4) adds support for heterogeneous head dim models — Gemma 4's mix of head ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4193965595)
- `2026-04-07T05:18:05Z` `issue` by `gaby`; signals: aligned, alignment, attention, bf16, block, fp4, fp8, gemm; excerpt: "@gaby That block size error is a page-size alignment issue with hybrid Mamba+attention models. The turboquant-vllm plugin uses raw TQ4 slot bytes for page ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4196704012)
- `2026-04-08T03:49:43Z` `issue` by `Alberto-Codes`; signals: alignment, attention, block, cache, dtype, fp4, gemm, h100; excerpt: "@gaby Tested your model list on H100 with the fork branch (--kv-cache-dtype tq-t4nc): Model Gen NIAH (512-4K) Notes ------- ----- --------------- ------- Devstral-Small OK ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4203675070)
- `2026-04-10T06:32:16Z` `issue` by `vibhavagarwal5`; signals: benchmark, block, fp8, hang, kernel, perf, performance, throughput; excerpt: "Performance optimization update — follow-up work in - In-kernel FP8 cast : Moved from host-side torch.float8 e4m3fn to in-kernel tl.float8e4nv/tl.float8e4b15 - WHT rotation : ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4221602039)
- `2026-04-10T10:50:51Z` `issue` by `vipin-sa-16319`; signals: cache, cuda, dtype, hang, kv cache, latency, memory, perf; excerpt: "I tested both the baseline (v0.18.0) and this PR on a single L40S GPU (1 slot), and observed a significant performance difference. The load ..." (https://github.com/vllm-project/vllm/pull/38479#issuecomment-4222992311)
