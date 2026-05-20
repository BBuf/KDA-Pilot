# PR Discussion Digest

- Source PR: [vllm-project/vllm#21309](https://github.com/vllm-project/vllm/pull/21309)
- Source page: `sources/prs/vllm/PR-21309.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21309`
- Generated at: `2026-05-20T15:36:37.243336+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-21T14:33:53Z`
- Merged: `2025-08-03T07:54:23Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: LopezCastroRoberto, aabbccddwasd, fernandaspets, kabachuha, mgoin
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-07-21T14:36:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for NVFP4 on Blackwell SM120 GPUs. There are two critical issues ... (https://github.com/vllm-project/vllm/pull/21309#pullrequestreview-3038435044)
- `2025-07-24T19:09:58Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21309#pullrequestreview-3052813724)
- `2025-07-25T08:45:32Z` `COMMENTED` by `LopezCastroRoberto` (https://github.com/vllm-project/vllm/pull/21309#pullrequestreview-3054620488)
- `2025-07-28T13:56:56Z` `APPROVED` by `mgoin` - LGTM, thanks! (https://github.com/vllm-project/vllm/pull/21309#pullrequestreview-3062900978)

## Inline Comment Hotspots

- `csrc/quantization/fp4/nvfp4_scaled_mm_entry.cu`: 2 inline comment(s)
- `csrc/quantization/fp4/nvfp4_scaled_mm_sm120_kernels.cu`: 2 inline comment(s)
- `CMakeLists.txt`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-24T18:44:12Z` `inline` by `mgoin` `csrc/quantization/fp4/nvfp4_scaled_mm_sm120_kernels.cu`:300; signals: dtype, fp4, kernel, nvfp4, sm120; excerpt: "It seems these dtypes are swapped?" (https://github.com/vllm-project/vllm/pull/21309#discussion_r2229287395)
- `2025-07-25T08:45:32Z` `inline` by `LopezCastroRoberto` `csrc/quantization/fp4/nvfp4_scaled_mm_sm120_kernels.cu`:300; signals: fp4, kernel, nvfp4, sm120; excerpt: "Good catch" (https://github.com/vllm-project/vllm/pull/21309#discussion_r2230535222)
- `2025-08-02T21:50:34Z` `issue` by `fernandaspets`; signals: blackwell, fp4, nvfp4; excerpt: "Hi will this pull request work for NVFP4/Qwen3-235B-A22B-Thinking-2507-FP4? I can't load it with 0.10.1.dev235+g055bd3978.d20250731.cu129 i built the other day (did NOT use this pull ..." (https://github.com/vllm-project/vllm/pull/21309#issuecomment-3146746311)
- `2025-08-02T22:00:05Z` `issue` by `mgoin`; signals: gemm, kernel, moe; excerpt: "Not yet, this PR is only for dense GEMMs. We need separate work to add a group GEMM kernel for MoEs" (https://github.com/vllm-project/vllm/pull/21309#issuecomment-3146753663)
- `2025-07-24T18:45:17Z` `inline` by `mgoin` `csrc/quantization/fp4/nvfp4_scaled_mm_entry.cu`:43; signals: fp4, nvfp4; excerpt: "This is probably good practice to do" (https://github.com/vllm-project/vllm/pull/21309#discussion_r2229289988)
