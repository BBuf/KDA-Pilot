# PR Discussion Digest

- Source PR: [sgl-project/sglang#7689](https://github.com/sgl-project/sglang/pull/7689)
- Source page: `sources/prs/sglang/PR-7689.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7689`
- Generated at: `2026-05-20T15:31:18.597188+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-01T08:40:20Z`
- Merged: `2025-07-07T03:05:49Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 20 (approved=3, commented=17)
- Inline review comments: 31
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=18, outdated=12
- Human participants with discussion text: Alcanderian, dongyibo, hlu1, ispobock, merrymercy, xutizhou, yuan-luo, zhyncs
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-07-01T08:40:53Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2974250463)
- `2025-07-01T08:42:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates a new Triton kernel for Mixture-of-Experts (MoE) to improve performance. The changes ... (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2974259283)
- `2025-07-01T10:34:38Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2974752559)
- `2025-07-01T21:32:04Z` `COMMENTED` by `hlu1` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977011898)
- `2025-07-02T03:05:58Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977486264)
- `2025-07-02T03:50:05Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977532068)
- `2025-07-02T03:50:12Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977532168)
- `2025-07-02T04:21:19Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977605402)
- `2025-07-02T04:27:32Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977621026)
- `2025-07-02T06:16:30Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977873759)
- `2025-07-02T06:19:56Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2977880717)
- `2025-07-02T08:41:45Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2978276539)
- `2025-07-02T10:21:56Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2978592900)
- `2025-07-04T06:56:10Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2985816045)
- `2025-07-04T08:43:09Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2986124442)
- `2025-07-04T15:20:59Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2987655055)
- `2025-07-04T16:58:15Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2987880554)
- `2025-07-04T16:58:23Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2987881315)
- `2025-07-04T17:18:56Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2987925192)
- `2025-07-06T03:48:10Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/7689#pullrequestreview-2990949641)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`: 19 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 10 inline comment(s)
- `benchmark/kernels/fused_moe_triton/benchmark_sglang_fused_moe_triton.py`: 1 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-02T03:50:05Z` `inline` by `yuan-luo` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:33; signals: kernel, moe, tma, triton; excerpt: "If renormalize=True, the host side will not do softmax, it will leave the Triton kernel inside to to softmax. In triton kernel routing(), if ..." (https://github.com/sgl-project/sglang/pull/7689#discussion_r2178939950)
- `2025-07-01T21:29:47Z` `inline` by `hlu1` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:132; signals: kernel, moe, triton; excerpt: "Are you using the sglang activations kernels because of the weight shuffling required by the openai kernels?" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2178568519)
- `2025-07-01T10:28:38Z` `inline` by `ispobock` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:165; signals: kernel, moe, triton; excerpt: "remove this comment" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2177157582)
- `2025-07-01T10:29:25Z` `inline` by `ispobock` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:97; signals: kernel, moe, triton; excerpt: "why comment this assert?" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2177161010)
- `2025-07-01T10:29:49Z` `inline` by `ispobock` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:33; signals: kernel, moe, triton; excerpt: "How to handle renormalize case?" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2177162756)
- `2025-07-01T10:30:03Z` `inline` by `ispobock` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:10; signals: kernel, moe, triton; excerpt: "remove this line" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2177163530)
- `2025-07-01T10:30:18Z` `inline` by `ispobock` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:1; signals: kernel, moe, triton; excerpt: "Add source reference" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2177164562)
- `2025-07-01T10:34:30Z` `inline` by `ispobock` `python/sglang/srt/server_args.py`:1558; signals: kernel, moe, triton; excerpt: "--enable-triton-kernel-moe?" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2177181710)
- `2025-07-01T21:28:03Z` `inline` by `hlu1` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:30; signals: kernel, moe, triton; excerpt: "Please add assertions for unused input args" (https://github.com/sgl-project/sglang/pull/7689#discussion_r2178565673)
- `2025-07-02T03:05:58Z` `inline` by `yuan-luo` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:165; signals: kernel, moe, triton; excerpt: "Removed." (https://github.com/sgl-project/sglang/pull/7689#discussion_r2178907280)
- `2025-07-02T03:50:12Z` `inline` by `yuan-luo` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:10; signals: kernel, moe, triton; excerpt: "Done." (https://github.com/sgl-project/sglang/pull/7689#discussion_r2178940088)
- `2025-07-02T04:21:19Z` `inline` by `yuan-luo` `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`:132; signals: kernel, moe, triton; excerpt: "Here need to invoke activation kernels, I just pick sglang version." (https://github.com/sgl-project/sglang/pull/7689#discussion_r2179001132)
