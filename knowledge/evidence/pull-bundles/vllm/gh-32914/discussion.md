# PR Discussion Digest

- Source PR: [vllm-project/vllm#32914](https://github.com/vllm-project/vllm/pull/32914)
- Source page: `sources/prs/vllm/PR-32914.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-32914`
- Generated at: `2026-05-20T15:39:32.758879+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-23T06:37:25Z`
- Merged: `2026-04-01T03:30:19Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 16 (approved=1, commented=15)
- Inline review comments: 17
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=5
- Human participants with discussion text: Rohan138, mergify, samutamm, tjtanaa, tuukkjs
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2026-01-23T06:39:58Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request updates the AITER branch in the Dockerfile and integrates aiter.paged attention common for ... (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3695921154)
- `2026-02-13T08:25:14Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3795700084)
- `2026-02-13T08:28:36Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3795712597)
- `2026-02-16T07:51:33Z` `COMMENTED` by `samutamm` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3807100416)
- `2026-02-27T09:46:06Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3865988420)
- `2026-02-27T10:33:22Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3866195745)
- `2026-02-27T12:59:14Z` `COMMENTED` by `samutamm` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3866828280)
- `2026-03-04T08:33:38Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3887921417)
- `2026-03-10T18:55:42Z` `COMMENTED` by `Rohan138` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3924684204)
- `2026-03-12T11:46:21Z` `COMMENTED` by `tuukkjs` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3935928865)
- `2026-03-12T11:49:14Z` `COMMENTED` by `tuukkjs` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3935943388)
- `2026-03-12T11:50:36Z` `COMMENTED` by `tuukkjs` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3935951096)
- `2026-03-13T04:56:35Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3941615854)
- `2026-03-13T04:57:45Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3941619647)
- `2026-03-17T12:39:47Z` `COMMENTED` by `tuukkjs` (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-3960454492)
- `2026-03-31T12:50:51Z` `APPROVED` by `tjtanaa` - LGTM. However, the paged attention common code path is not producing correct output for hybrid models like Qwen3.5. ... (https://github.com/vllm-project/vllm/pull/32914#pullrequestreview-4037150244)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/rocm_aiter_fa.py`: 17 inline comment(s)

## High-Signal Discussion

- `2026-03-31T04:37:37Z` `issue` by `tuukkjs`; signals: accuracy, attention, benchmark, bf16, cache, fp8, kernel, kv cache; excerpt: "MI300X pa common kernel routing paged attention common dynamically selects HIP (paged attention rocm/ll4mi) or ASM (pa bf16 pertokenFp8 gqa8 ) based on batch ..." (https://github.com/vllm-project/vllm/pull/32914#issuecomment-4159823893)
- `2026-02-27T12:59:14Z` `inline` by `samutamm` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, bf16, cache, fp8, kv cache, layout; excerpt: "So far VLLM ROCM SHUFFLE KV CACHE LAYOUT seems useful in cases we've seen. For Qwen/Qwen3-235B-A22B-Instruct-2507 (bf16) VLLM ROCM SHUFFLE KV CACHE LAYOUT=1 brought ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2864231686)
- `2026-03-12T11:46:21Z` `inline` by `tuukkjs` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, fp8, kernel, kv cache, layout; excerpt: "Hey, I am taking a look at this PR since Samu is away. We found out that VLLM ROCM SHUFFLE KV CACHE LAYOUT=1 (the ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2924066172)
- `2026-03-17T12:39:47Z` `inline` by `tuukkjs` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, benchmark, correctness, fp8, kernel, perf; excerpt: "Short update. Fix to restrict the pa fwd asm kernel to head size 128 in aiter has been merged. I’ve been running lm eval ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2946490403)
- `2026-03-10T18:55:42Z` `inline` by `Rohan138` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, kv cache, layout, perf; excerpt: "JFYI @tjtanaa if you turn VLLM ROCM USE SHUFFLE KVCACHE LAYOUT on by default, it'll break the rope+kvcache fusion unit test for ROCM AITER ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2913799056)
- `2026-03-31T04:37:46Z` `issue` by `tuukkjs`; signals: accuracy, attention, kernel, oom, throughput; excerpt: "MI355X pa common kernel routing Model TP Heads/GPU MI355X (thr=512) ------- ---- ----------- ------------------ Llama 3.3 70B 1 64 HIP ≤8, ASM ≥9 Llama ..." (https://github.com/vllm-project/vllm/pull/32914#issuecomment-4159824314)
- `2026-02-13T08:28:36Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, kv cache, layout; excerpt: "@samutamm are you confident that we can remove this is shuffle kv cache enabled and envs.VLLM ROCM SHUFFLE KV CACHE LAYOUT condition and always ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2802917902)
- `2026-02-16T07:51:33Z` `inline` by `samutamm` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, kv cache, layout; excerpt: "So far VLLM ROCM SHUFFLE KV CACHE LAYOUT seems useful in cases we've seen. Right, paged attention common does not have sliding windows, conserving ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2811079661)
- `2026-02-27T10:33:21Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, dtype, fp8; excerpt: "I just found one that we might need to keep the flag for now, when trying to run Qwen/Qwen3.5-397B-A17B-FP8 with kv-cache-dtype=fp8" (https://github.com/vllm-project/vllm/pull/32914#discussion_r2863656777)
- `2026-03-12T11:50:35Z` `inline` by `tuukkjs` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, layout, perf; excerpt: "@Rohan138 your ? AFAIU, for some models (e.g., llama 3s – I think) one would benefit from both (the shuffled layout and rope+kvcache fusion) ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2924087010)
- `2026-03-13T04:57:45Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, kv cache, layout; excerpt: "@Rohan138 ok. Then in this case, we still need to preserve the environment variable flag VLLM ROCM SHUFFLE KV CACHE LAYOUT. But we will ..." (https://github.com/vllm-project/vllm/pull/32914#discussion_r2929040560)
- `2026-02-27T09:46:06Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:1111; signals: attention, cache, kv cache, layout; excerpt: "So far VLLM ROCM SHUFFLE KV CACHE LAYOUT seems useful in cases we've seen. When is it useful?" (https://github.com/vllm-project/vllm/pull/32914#discussion_r2863462085)
