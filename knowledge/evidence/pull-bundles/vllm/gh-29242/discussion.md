# PR Discussion Digest

- Source PR: [vllm-project/vllm#29242](https://github.com/vllm-project/vllm/pull/29242)
- Source page: `sources/prs/vllm/PR-29242.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29242`
- Generated at: `2026-05-20T15:38:41.034622+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-22T17:45:44Z`
- Merged: `2025-11-25T14:59:08Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: ElizaWszola, bbrowning, bnellnm, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-22T17:47:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for NVFP4 MoE kernels on SM120 architecture using CUTLASS. The changes ... (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3496870011)
- `2025-11-22T22:03:22Z` `COMMENTED` by `bbrowning` (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3496962041)
- `2025-11-25T01:22:17Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3502855014)
- `2025-11-25T01:23:23Z` `APPROVED` by `bnellnm` - LGTM. I'm not a cutlass expert but it looks close enough to the sm100 version. (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3502858782)
- `2025-11-25T06:28:53Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3503444510)
- `2025-11-25T14:58:24Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3505489640)
- `2025-11-25T14:58:49Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3505491557)

## Inline Comment Hotspots

- `csrc/quantization/fp4/nvfp4_blockwise_moe_kernel.cu`: 6 inline comment(s)

## High-Signal Discussion

- `2025-11-25T14:58:24Z` `inline` by `mgoin` `csrc/quantization/fp4/nvfp4_blockwise_moe_kernel.cu`:502; signals: bf16, block, fp4, kernel, moe, nvfp4, sm120; excerpt: "Doesn't seem to be so, the sm120 kernel is a bit unique as seen from the bf16 issue" (https://github.com/vllm-project/vllm/pull/29242#discussion_r2560316083)
- `2025-11-23T19:30:51Z` `issue` by `bbrowning`; signals: block, cutlass, fp4, hang, moe, nvfp4, sm120; excerpt: "So, after some digging around, I got this seemingly working by adjusting run fp4 blockwise scaled group mm sm120 to not be a template ..." (https://github.com/vllm-project/vllm/pull/29242#issuecomment-3568264978)
- `2025-11-25T01:22:17Z` `inline` by `bnellnm` `csrc/quantization/fp4/nvfp4_blockwise_moe_kernel.cu`:502; signals: block, fp4, kernel, moe, nvfp4, sm100; excerpt: "Does the sm100 version need beta set to 0 also?" (https://github.com/vllm-project/vllm/pull/29242#discussion_r2558211825)
- `2025-11-25T06:28:52Z` `inline` by `ElizaWszola` `csrc/quantization/fp4/nvfp4_blockwise_moe_kernel.cu`:354; signals: block, fp4, kernel, moe, nvfp4, sm100; excerpt: "nit: Would it be useful to add a similar detailed message to the SM100 kernel?" (https://github.com/vllm-project/vllm/pull/29242#discussion_r2558700362)
- `2025-11-25T14:58:49Z` `inline` by `mgoin` `csrc/quantization/fp4/nvfp4_blockwise_moe_kernel.cu`:354; signals: block, cutlass, fp4, kernel, moe, nvfp4; excerpt: "I want to improve this across the board for our cutlass kernels, so will do in a followup" (https://github.com/vllm-project/vllm/pull/29242#discussion_r2560317726)
- `2025-11-22T22:03:22Z` `inline` by `bbrowning` `csrc/quantization/fp4/nvfp4_blockwise_moe_kernel.cu`:531; signals: block, fp4, kernel, moe, nvfp4; excerpt: "The DGX Spark uses version num 121, so this may need to be a bit looser. Perhaps something like:" (https://github.com/vllm-project/vllm/pull/29242#discussion_r2553375702)
- `2025-11-23T22:57:01Z` `issue` by `bbrowning`; signals: fp4, kernel, nvfp4, perf, performance; excerpt: "I don't know what to really expect performance-wise, but this feels like it's taking advantage of the new NVFP4 kernels? The output token/s is ..." (https://github.com/vllm-project/vllm/pull/29242#issuecomment-3568429882)
- `2025-11-23T22:01:30Z` `issue` by `bbrowning`; signals: bf16, cuda, fp4, nvfp4; excerpt: "I tried explicit template instantiation and that did not work. I tried static inline template and non-templated bf16 and f16 suffixed wrappers dispatched to ..." (https://github.com/vllm-project/vllm/pull/29242#issuecomment-3568378031)
- `2025-11-24T20:52:24Z` `issue` by `bbrowning`; signals: fp4, hang, moe, nvfp4; excerpt: "I pulled the latest changes here onto my SM121 and was able to load RedHatAI/Qwen3-30B-A3B-NVFP4 and RedHatAI/Llama-4-Scout-17B-16E-Instruct-NVFP4 (both NVFP4 MoE models) successfully without having ..." (https://github.com/vllm-project/vllm/pull/29242#issuecomment-3572681155)
- `2025-11-23T14:09:35Z` `issue` by `bbrowning`; signals: cutlass, race; excerpt: "Debugging some things here locally with trace output enabled: I wonder if we're going to end up needed some of the fixes from CUTLASS ..." (https://github.com/vllm-project/vllm/pull/29242#issuecomment-3567994464)
- `2025-11-23T20:38:32Z` `issue` by `mgoin`; signals: cutlass, gemm; excerpt: "Wow, I couldn't figure out the gemm initialization failure for several hours yesterday. Even CUTLASS debug logs were giving me nothing. If that fixes ..." (https://github.com/vllm-project/vllm/pull/29242#issuecomment-3568314737)
- `2025-11-25T01:23:23Z` `review` `APPROVED` by `bnellnm`; signals: cutlass, sm100; excerpt: "LGTM. I'm not a cutlass expert but it looks close enough to the sm100 version." (https://github.com/vllm-project/vllm/pull/29242#pullrequestreview-3502858782)
