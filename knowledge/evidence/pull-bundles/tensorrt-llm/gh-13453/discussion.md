# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13453](https://github.com/NVIDIA/TensorRT-LLM/pull/13453)
- Source page: `sources/prs/tensorrt-llm/PR-13453.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13453`
- Generated at: `2026-05-20T15:18:42.396539+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-24T23:18:26Z`
- Merged: `2026-04-30T04:46:11Z`

## Discussion Counts

- Issue comments: 31
- Review submissions: 16 (approved=2, commented=14)
- Inline review comments: 18
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: coderabbitai, hnover-nv, mikeiovine, nv-guomingz, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T23:27:26Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 🧹 Nitpick comments (2) tests/unittest/ torch/modules/mamba/test replay selective state update.py (1) 19-19: Remove unused ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4173982661)
- `2026-04-24T23:34:01Z` `COMMENTED` by `hnover-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174002086)
- `2026-04-24T23:34:40Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174004477)
- `2026-04-24T23:54:07Z` `COMMENTED` by `hnover-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174072825)
- `2026-04-24T23:54:13Z` `COMMENTED` by `hnover-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174073156)
- `2026-04-24T23:54:35Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174074361)
- `2026-04-24T23:54:38Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174074705)
- `2026-04-25T00:05:02Z` `COMMENTED` by `hnover-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174124035)
- `2026-04-25T00:05:14Z` `COMMENTED` by `hnover-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174125224)
- `2026-04-25T00:05:21Z` `COMMENTED` by `hnover-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174125905)
- `2026-04-25T00:05:29Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174126707)
- `2026-04-25T00:05:32Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174126954)
- `2026-04-25T00:05:40Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4174127625)
- `2026-04-27T18:58:00Z` `COMMENTED` by `mikeiovine` - Stamping changes under pyexecutor/ on behalf of runtime/model devs. Did not review the rest, should be done by ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4183460210)
- `2026-04-27T18:58:12Z` `APPROVED` by `mikeiovine` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4183461187)
- `2026-04-29T06:18:55Z` `APPROVED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4194590264)

## Inline Comment Hotspots

- `tests/unittest/_torch/modules/mamba/benchmark_replay_selective_state_update.py`: 9 inline comment(s)
- `tensorrt_llm/_torch/modules/mamba/causal_conv1d_triton.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/modules/mamba/selective_state_update.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-24T23:27:22Z` `issue` by `coderabbitai`; signals: accuracy, attention, benchmark, block, cache, correctness, cuda, hang; excerpt: "📝 Walkthrough Walkthrough Introduces a new replay-based optimization for Mamba2 speculative decoding with selective state replay kernels, hardware-aware gating for SM versions, dual cache ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#issuecomment-4317005576)
- `2026-04-24T23:27:26Z` `review` `COMMENTED` by `coderabbitai`; signals: benchmark, cache, hang, tensorrt, triton; excerpt: "Actionable comments posted: 6 🧹 Nitpick comments (2) tests/unittest/ torch/modules/mamba/test replay selective state update.py (1) 19-19: Remove unused import. rearrange is imported but never ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4173982661)
- `2026-04-24T23:27:25Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/mamba/causal_conv1d_triton.py`:1018; signals: cuda, cute, kernel, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major Use x.device for the SM capability check. This gate is also evaluated on the current CUDA device instead of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140770550)
- `2026-04-24T23:27:25Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`:420; signals: benchmark, block, cache, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Reset cache buf idx when a replay slot is reused. A fresh replay block zeroes prev num accepted tokens ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140770560)
- `2026-04-24T23:34:40Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`:420; signals: block, cache, kernel, tensorrt; excerpt: "@hnover-nv, that's a clear and correct explanation — thank you. With prev num accepted tokens = 0, the replay kernel treats the block as ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140787584)
- `2026-04-24T23:27:25Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/mamba/selective_state_update.py`:340; signals: benchmark, cuda, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Gate PDL against x.device, not the current CUDA device. This SM check runs before the code switches to x.device, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140770555)
- `2026-04-24T23:34:01Z` `inline` by `hnover-nv` `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`:420; signals: cache, tensorrt; excerpt: "We set prev num accepted tokens=0, so that means we won't use any of the replay data. Of course the old state isn't cleared ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140786271)
- `2026-04-24T23:54:07Z` `inline` by `hnover-nv` `tensorrt_llm/_torch/modules/mamba/causal_conv1d_triton.py`:1018; signals: tensorrt, triton; excerpt: "The get sm version() device-0 hardcoding is pervasive across the codebase, so we already only support homogenous deployments. Fixing is out of scope." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140831598)
- `2026-04-24T23:54:35Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/mamba/causal_conv1d_triton.py`:1018; signals: tensorrt, triton; excerpt: "@hnover-nv, understood — thanks for the clarification. Given that TensorRT-LLM only targets homogeneous GPU deployments, the get sm version() device-0 assumption is a valid ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140832665)
- `2026-04-27T18:58:00Z` `review` `COMMENTED` by `mikeiovine`; signals: hang; excerpt: "Stamping changes under pyexecutor/ on behalf of runtime/model devs. Did not review the rest, should be done by nemotron devs" (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#pullrequestreview-4183460210)
- `2026-04-24T23:27:25Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/mamba/benchmark_replay_selective_state_update.py`:120; signals: benchmark; excerpt: "⚠️ Potential issue 🟡 Minor Only fall back on import-related failures. Catching every Exception here will hide real breakages in the fast-load path and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140770564)
- `2026-04-24T23:27:25Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/mamba/benchmark_replay_selective_state_update.py`:572; signals: benchmark; excerpt: "⚠️ Potential issue 🟠 Major This new benchmark currently fails lint. These six inline if statements trip E701, so the file will fail Ruff/Flake8 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13453#discussion_r3140770566)
