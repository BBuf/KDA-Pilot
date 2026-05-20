# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2412](https://github.com/Dao-AILab/flash-attention/pull/2412)
- Source page: `sources/prs/flash-attention/PR-2412.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2412`
- Generated at: `2026-05-20T15:16:57.926157+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T09:16:54Z`
- Merged: `2026-04-23T18:22:11Z`

## Discussion Counts

- Issue comments: 33
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 12
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=0
- Human participants with discussion text: 777ki, Johnsonms, cherichy, copilot-pull-request-reviewer, dishengbin, tridao, umiswing, wangsiyu
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 20

## Review Decisions

- `2026-04-23T18:21:26Z` `APPROVED` by `Johnsonms` - Hi @wangsiyu @cherichy @dishengbin, this PR is approved and will be merged with the following follow-up items: 1. ... (https://github.com/Dao-AILab/flash-attention/pull/2412#pullrequestreview-4164837107)

## Inline Comment Hotspots

- `flash_attn/cute/mask.py`: 4 inline comment(s)
- `flash_attn/cute/interface.py`: 2 inline comment(s)
- `flash_attn/cute/utils.py`: 2 inline comment(s)
- `flash_attn/cute/tile_scheduler.py`: 2 inline comment(s)
- `tests/cute/test_flash_attn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-31T09:20:27Z` `issue` by `cherichy`; signals: block, gemm, layout, memory, pipeline, shared memory, throughput, tile; excerpt: "Thanks for the contribution! Can you say more about the new pipeline for fwd? The main differences in the pipeline are: - Two CTAs ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4161153769)
- `2026-04-02T11:37:23Z` `issue` by `cherichy`; signals: b200, benchmark, h200, oom, perf, performance, speedup, throughput; excerpt: "@Johnsonms Thanks for the updated benchmark! Here are our latest numbers comparing FA3 on H200 vs FA4 hd256 on B200 (head dim=256, batch=1, seqlen ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4176934825)
- `2026-04-02T14:42:52Z` `issue` by `Johnsonms`; signals: alignment, b200, benchmark, h200, oom, perf, performance, speedup; excerpt: "@Johnsonms Thanks for the updated benchmark! Here are our latest numbers comparing FA3 on H200 vs FA4 hd256 on B200 (head dim=256, batch=1, seqlen ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4178401705)
- `2026-04-02T22:23:28Z` `issue` by `Johnsonms`; signals: b200, benchmark, bf16, h100, h200, kernel, occupancy, oom; excerpt: "@Johnsonms Thanks for the updated benchmark! Here are our latest numbers comparing FA3 on H200 vs FA4 hd256 on B200 (head dim=256, batch=1, seqlen ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4180800388)
- `2026-03-31T19:20:07Z` `issue` by `Johnsonms`; signals: attention, b200, benchmark, kernel, memory, perf, performance; excerpt: "@wangsiyu Here are the performance benchmark results on our side for commit c784c2b. Please check whether they align with what your team observed. I ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4164897155)
- `2026-04-03T08:14:22Z` `issue` by `dishengbin`; signals: benchmark, cuda, cute, kernel, perf, performance, throughput; excerpt: "One case (16K fwd, non-causal) needs further investigation, with the contributor reaching higher peak throughput ( 1800 TFLOPS vs. 1300–1500). @Johnsonms It’s probably because ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4182463490)
- `2026-04-23T18:21:26Z` `review` `APPROVED` by `Johnsonms`; signals: attention, cute, perf, performance, sm100; excerpt: "Hi @wangsiyu @cherichy @dishengbin, this PR is approved and will be merged with the following follow-up items: 1. The current implementation follows a CuTe ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#pullrequestreview-4164837107)
- `2026-04-08T01:24:52Z` `issue` by `dishengbin`; signals: benchmark, bf16, perf, performance; excerpt: "Hi @Johnsonms , thanks for providing the benchmarking scripts. I checked the script and found that the performance differences come from how the tensors ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4203200775)
- `2026-04-23T18:00:58Z` `issue` by `Johnsonms`; signals: b200, benchmark, bf16, speedup; excerpt: "04.23 final Benchmark: Legend: TFLOPS (MFU%) where peak BF16 on B200 = 2250 TFLOPS. fwd× = FA4/cuDNN forward speedup. cuDNN bwd not available at ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4306650048)
- `2026-03-31T14:49:11Z` `issue` by `wangsiyu`; signals: benchmark, kernel, perf, performance; excerpt: "Forward kernel performance is improved via STG trick. The benchmark is ready to refresh." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4163227828)
- `2026-04-13T06:19:49Z` `issue` by `Johnsonms`; signals: hang, perf, performance; excerpt: "Hi @wangsiyu, from commit : Key takeaways (average performance under stable clocks): FWD non-causal: consistent +5–9% improvement across all sequence lengths FWD causal, 1K: ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4234256084)
- `2026-04-13T07:26:36Z` `issue` by `wangsiyu`; signals: hang, perf, performance; excerpt: "Hi @wangsiyu, from commit : Key takeaways (average performance under stable clocks): FWD non-causal: consistent +5–9% improvement across all sequence lengths FWD causal, 1K: ..." (https://github.com/Dao-AILab/flash-attention/pull/2412#issuecomment-4234572721)
