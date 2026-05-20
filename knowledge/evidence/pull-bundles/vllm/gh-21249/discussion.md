# PR Discussion Digest

- Source PR: [vllm-project/vllm#21249](https://github.com/vllm-project/vllm/pull/21249)
- Source page: `sources/prs/vllm/PR-21249.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21249`
- Generated at: `2026-05-20T15:36:37.238922+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-20T10:08:42Z`
- Merged: `2025-08-07T00:03:43Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 32 (approved=2, commented=30)
- Inline review comments: 56
- Review threads observed: 25
- Resolved/outdated thread markers: resolved=22, outdated=20
- Human participants with discussion text: Josephasafg, adamscarlat, heheda12345, mergify, tdoublep, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-20T10:09:53Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces v1-style attention metadata support for Mamba-1 models and refactors the Mamba state ... (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3035957381)
- `2025-07-21T23:41:19Z` `COMMENTED` by `heheda12345` - Thanks for the great job. Some questions: 1. Do we need enforce-eager to run mamba1? I'm OK with ... (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3039964296)
- `2025-07-22T09:55:27Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3042184581)
- `2025-07-22T10:17:27Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3042296977)
- `2025-07-22T10:41:11Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3042423288)
- `2025-07-23T06:21:22Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3045830363)
- `2025-07-23T06:53:52Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3045842123)
- `2025-07-23T07:01:42Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3045942062)
- `2025-07-23T11:27:10Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3046912718)
- `2025-07-23T15:30:29Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3047984237)
- `2025-07-23T15:41:32Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3048035844)
- `2025-07-23T15:42:22Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3048038450)
- `2025-07-23T16:06:39Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3048139750)
- `2025-07-24T15:45:07Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3052212440)
- `2025-07-24T17:22:45Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3052559485)
- `2025-07-24T19:30:33Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3053009772)
- `2025-07-24T19:38:29Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3053037565)
- `2025-07-24T20:48:26Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3053241210)
- `2025-07-25T07:43:13Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3054375514)
- `2025-07-25T07:46:42Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3054455225)
- `2025-08-03T16:27:17Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3082241369)
- `2025-08-03T16:34:25Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3082243851)
- `2025-08-03T16:35:53Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3082245541)
- `2025-08-05T22:00:33Z` `COMMENTED` by `tdoublep` - I have a few (mostly minor) comments but this look nearly ready to go in my view. Great ... (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3089828629)
- ... 8 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/mamba/mamba_mixer.py`: 14 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 9 inline comment(s)
- `vllm/model_executor/layers/mamba/mamba_utils.py`: 9 inline comment(s)
- `vllm/v1/attention/backends/mamba1_attn.py`: 8 inline comment(s)
- `tests/models/language/generation/test_hybrid.py`: 7 inline comment(s)
- `vllm/v1/kv_cache_interface.py`: 4 inline comment(s)
- `docs/usage/v1_guide.md`: 2 inline comment(s)
- `vllm/attention/mamba_selectors.py`: 1 inline comment(s)
- `vllm/model_executor/models/mamba.py`: 1 inline comment(s)
- `csrc/mamba/mamba_ssm/selective_scan_fwd.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-23T06:44:53Z` `inline` by `heheda12345` `vllm/model_executor/layers/mamba/mamba_mixer.py`:214; signals: kernel, perf, performance; excerpt: "Seems that we'll always use the prefill kernel in v1. Is my understanding correct? @tlrmchlsmth Will there be any performance issue if we don't ..." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2224568033)
- `2025-07-24T20:48:25Z` `inline` by `Josephasafg` `vllm/v1/attention/backends/mamba1_attn.py`:38; signals: attention, kernel, triton; excerpt: "Good question. I think we should keep both since Mamba2AttentionMetadata contains fields that aren't relevant for mamba1 like chunk indices, chunk offsets and triton ..." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2229544047)
- `2025-07-21T21:57:56Z` `inline` by `heheda12345` `vllm/v1/kv_cache_interface.py`:209; signals: cache, hang; excerpt: "Will it be better to make mamba type a plain string? There are many different state space model implementations. I hope the new models ..." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2220445396)
- `2025-07-22T09:55:26Z` `inline` by `Josephasafg` `vllm/v1/kv_cache_interface.py`:209; signals: cache, hang; excerpt: "Model vendors don't need to add their model name (e.g. Jamba). The mamba type is the type mamba the model is based on and ..." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2221954703)
- `2025-07-23T06:21:22Z` `inline` by `heheda12345` `vllm/v1/kv_cache_interface.py`:209; signals: attention, cache; excerpt: "Seems that many models are customizing the mamba layer, e.g., minimax linear attention, phi-4's modified mamba attention." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2224519788)
- `2025-07-23T11:27:10Z` `inline` by `Josephasafg` `vllm/model_executor/layers/mamba/mamba_mixer.py`:182; signals: cache, kv cache; excerpt: "Yes. I can move it to reshape kv cache tensors in GPUModelRunner to the part where we allocate the conv and ssm tensors" (https://github.com/vllm-project/vllm/pull/21249#discussion_r2225248686)
- `2025-07-23T15:30:28Z` `inline` by `heheda12345` `vllm/model_executor/layers/mamba/mamba_mixer.py`:182; signals: attention, layout; excerpt: "OK but we are doing padding for mamba layers to align page size of attention layers and the state size of mamba layers. It ..." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2225966827)
- `2025-07-25T07:36:35Z` `inline` by `heheda12345` `vllm/v1/attention/backends/mamba1_attn.py`:77; signals: attention, kernel; excerpt: "Seems that you are still using one kernel for prefill and decode. Why are you computing these things? Can you either only keep necessary ..." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2230391613)
- `2025-07-21T23:41:19Z` `review` `COMMENTED` by `heheda12345`; signals: cuda; excerpt: "Thanks for the great job. Some questions: 1. Do we need enforce-eager to run mamba1? I'm OK with supporting cuda graph in a future ..." (https://github.com/vllm-project/vllm/pull/21249#pullrequestreview-3039964296)
- `2025-07-24T15:40:02Z` `inline` by `tdoublep` `vllm/model_executor/layers/mamba/mamba_mixer.py`:214; signals: perf, performance; excerpt: "We saw very bad performance for Mamba2 until we split prefill and decode iirc" (https://github.com/vllm-project/vllm/pull/21249#discussion_r2228885197)
- `2025-07-21T21:45:25Z` `inline` by `heheda12345` `vllm/v1/worker/gpu_model_runner.py`:48; signals: attention; excerpt: "Can we avoid importing all mamba attention backends here? There will be more and more mamba-related backends." (https://github.com/vllm-project/vllm/pull/21249#discussion_r2220426561)
- `2025-07-24T15:44:00Z` `inline` by `tdoublep` `vllm/v1/attention/backends/mamba1_attn.py`:38; signals: attention; excerpt: "How different is the Mamba1AttentionMetdata to the Mamba2AttentionMetadata? Do we really need two separate classes?" (https://github.com/vllm-project/vllm/pull/21249#discussion_r2228894512)
