# PR Discussion Digest

- Source PR: [sgl-project/sglang#7772](https://github.com/sgl-project/sglang/pull/7772)
- Source page: `sources/prs/sglang/PR-7772.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7772`
- Generated at: `2026-05-20T15:31:21.453448+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-04T08:06:43Z`
- Merged: `2025-07-05T03:50:12Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 11
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: AniZpZ, yangsijia-celina
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-04T08:07:30Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yangsijia-serena, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7772#pullrequestreview-2986027416)
- `2025-07-04T08:09:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new CUTLASS W4A8 MoE kernel tailored for the Hopper architecture, which ... (https://github.com/sgl-project/sglang/pull/7772#pullrequestreview-2986031157)
- `2025-07-04T09:53:33Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/7772#pullrequestreview-2986317046)
- `2025-07-04T16:57:01Z` `COMMENTED` by `yangsijia-celina` (https://github.com/sgl-project/sglang/pull/7772#pullrequestreview-2987878708)
- `2025-07-05T03:44:46Z` `APPROVED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/7772#pullrequestreview-2988929965)

## Inline Comment Hotspots

- `sgl-kernel/csrc/cutlass_extensions/gemm/collective/sm90_mma_array_tma_gmma_rs_warpspecialized_mixed_input_.hpp`: 3 inline comment(s)
- `sgl-kernel/python/sgl_kernel/cutlass_moe.py`: 3 inline comment(s)
- `sgl-kernel/tests/test_cutlass_w4a8_moe_mm.py`: 2 inline comment(s)
- `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_grouped_mm_c3x.cu`: 1 inline comment(s)
- `sgl-kernel/csrc/cutlass_extensions/detail/collective/mixed_input_utils.hpp`: 1 inline comment(s)
- `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_moe_data.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-04T09:53:21Z` `inline` by `AniZpZ` `sgl-kernel/tests/test_cutlass_w4a8_moe_mm.py`:128; signals: cutlass, fp8, gemm, kernel, moe; excerpt: "consider add multi expert unittest @pytest.mark.parametrize("batch size,k,n,num experts", [ (4, 384, 768, 4), (8, 512, 1024, 8), ]) def test int4 fp8 grouped gemm ..." (https://github.com/sgl-project/sglang/pull/7772#discussion_r2184905001)
- `2025-07-04T09:35:51Z` `inline` by `AniZpZ` `sgl-kernel/python/sgl_kernel/cutlass_moe.py`:59; signals: cutlass, kernel, moe; excerpt: "consider non-zero default value or add checks here" (https://github.com/sgl-project/sglang/pull/7772#discussion_r2184867678)
- `2025-07-04T16:57:01Z` `inline` by `yangsijia-celina` `sgl-kernel/tests/test_cutlass_w4a8_moe_mm.py`:128; signals: cutlass, kernel, moe; excerpt: "fixed and added" (https://github.com/sgl-project/sglang/pull/7772#discussion_r2185784063)
