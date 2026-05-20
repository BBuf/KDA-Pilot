# PR Discussion Digest

- Source PR: [sgl-project/sglang#6821](https://github.com/sgl-project/sglang/pull/6821)
- Source page: `sources/prs/sglang/PR-6821.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6821`
- Generated at: `2026-05-20T15:30:49.029856+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-03T02:18:56Z`
- Merged: `2025-06-23T08:38:58Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 11 (approved=1, changes_requested=1, commented=9)
- Inline review comments: 17
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=8, outdated=6
- Human participants with discussion text: TianQiLin666666, ch-wan, copilot-pull-request-reviewer, fzyzcjy, zyksir
- Automation comments/reviews omitted from high-signal summary: 11
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-03T02:19:22Z` `COMMENTED` by `gemini-code-assist` - Hello @xutizhou, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2890377594)
- `2025-06-03T02:20:58Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request integrates DeepGEMM into the EPMoE layer, providing an alternative computation path. The changes ... (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2890380777)
- `2025-06-03T02:21:35Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull Request Overview This PR integrates DeepGEMM as an optional path into the EPMoE layer, introducing new Triton ... (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2890381342)
- `2025-06-03T08:16:58Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2891240191)
- `2025-06-04T15:43:05Z` `COMMENTED` by `zyksir` - @TianQiLin666666 amazing! Did you test the correctness of your implementation? like using mmlu or gsm8k using baseline and ... (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2897258400)
- `2025-06-11T08:43:52Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2916156244)
- `2025-06-16T15:13:42Z` `COMMENTED` by `TianQiLin666666` (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2932555102)
- `2025-06-16T15:13:54Z` `COMMENTED` by `TianQiLin666666` (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2932555723)
- `2025-06-16T15:14:18Z` `COMMENTED` by `TianQiLin666666` (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2932557271)
- `2025-06-22T22:24:43Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2948356573)
- `2025-06-22T22:27:43Z` `COMMENTED` by `gemini-code-assist` - Code Review The code changes integrate DeepGEMM into the EPMoE layer, providing an option to use DeepGEMM for ... (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2948357623)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 12 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-06-03T02:21:35Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: aligned, bf16, block, deepgemm, fp8, gemm, hang, kernel; excerpt: "Pull Request Overview This PR integrates DeepGEMM as an optional path into the EPMoE layer, introducing new Triton kernels and branching logic. - Add ..." (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2890381342)
- `2025-06-03T10:20:52Z` `issue` by `TianQiLin666666`; signals: deepgemm, gemm, perf, performance, triton; excerpt: "Compare performance of DeepGEMM with triton groupgemm on 8 H20-96G DeepGEMM triton groupgemm" (https://github.com/sgl-project/sglang/pull/6821#issuecomment-2934545209)
- `2025-06-04T15:43:05Z` `review` `COMMENTED` by `zyksir`; signals: correctness, deepgemm, gemm; excerpt: "@TianQiLin666666 amazing! Did you test the correctness of your implementation? like using mmlu or gsm8k using baseline and deepgemm?" (https://github.com/sgl-project/sglang/pull/6821#pullrequestreview-2897258400)
- `2025-06-03T02:21:34Z` `inline` by `copilot-pull-request-reviewer` `python/sglang/srt/layers/moe/ep_moe/layer.py`:39; signals: deepgemm, gemm, moe; excerpt: "[nitpick] The function name moe ep deepgemm preproess seems to have a typo (preproess); consider renaming it to moe ep deepgemm preprocess for clarity." (https://github.com/sgl-project/sglang/pull/6821#discussion_r2122481892)
- `2025-06-11T08:38:29Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:1242; signals: kernel, moe, triton; excerpt: "this kernel is very similar with post reorder triton kernel. Can we simply add an additional argument to post reorder triton kernel to control ..." (https://github.com/sgl-project/sglang/pull/6821#discussion_r2139550101)
- `2025-06-05T09:31:40Z` `issue` by `TianQiLin666666`; signals: correctness, deepgemm, gemm; excerpt: "@TianQiLin666666 amazing! Did you test the correctness of your implementation? like using mmlu or gsm8k using baseline and deepgemm? Yes, I have tested mmlu ..." (https://github.com/sgl-project/sglang/pull/6821#issuecomment-2943447518)
- `2025-06-11T08:29:32Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:1151; signals: kernel, moe; excerpt: "If we pre-define a tl.arange() outside this for-loop and reuse it, can this kernel be faster?" (https://github.com/sgl-project/sglang/pull/6821#discussion_r2139531834)
- `2025-06-16T15:13:54Z` `inline` by `TianQiLin666666` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:1242; signals: kernel, moe; excerpt: "Done!" (https://github.com/sgl-project/sglang/pull/6821#discussion_r2150266316)
- `2025-06-16T15:14:17Z` `inline` by `TianQiLin666666` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:1151; signals: kernel, moe; excerpt: "Done!" (https://github.com/sgl-project/sglang/pull/6821#discussion_r2150267077)
- `2025-06-03T08:16:57Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/ep_moe/layer.py`:338; signals: moe; excerpt: "this may not work b/c gateup input still has nonzero ref count" (https://github.com/sgl-project/sglang/pull/6821#discussion_r2123094128)
- `2025-06-11T08:41:11Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/layer.py`:266; signals: moe; excerpt: "we recently added num fused shared experts" (https://github.com/sgl-project/sglang/pull/6821#discussion_r2139555330)
- `2025-06-11T08:42:13Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/layer.py`:254; signals: moe; excerpt: "assert self.activation == "silu"" (https://github.com/sgl-project/sglang/pull/6821#discussion_r2139557384)
