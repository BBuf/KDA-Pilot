# PR Discussion Digest

- Source PR: [sgl-project/sglang#3629](https://github.com/sgl-project/sglang/pull/3629)
- Source page: `sources/prs/sglang/PR-3629.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3629`
- Generated at: `2026-05-20T15:29:59.865865+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-17T08:50:26Z`
- Merged: `2025-02-18T07:18:31Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: Fridge003, yizhang2077, zcbenz, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-02-17T09:18:03Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/3629#pullrequestreview-2620460757)
- `2025-02-17T09:26:57Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/3629#pullrequestreview-2620483193)
- `2025-02-17T19:53:15Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3629#pullrequestreview-2621866060)
- `2025-02-18T02:54:23Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/3629#pullrequestreview-2622323113)
- `2025-02-18T05:42:17Z` `APPROVED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/3629#pullrequestreview-2622498886)

## Inline Comment Hotspots

- `sgl-kernel/src/sgl-kernel/csrc/cublas_grouped_gemm.cu`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 1 inline comment(s)
- `sgl-kernel/tests/test_cublas_grouped_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-18T02:54:07Z` `inline` by `yizhang2077` `sgl-kernel/tests/test_cublas_grouped_gemm.py`:17; signals: block, cuda, gemm, kernel; excerpt: "can you add a control here, only cuda version = 12.5 then can run this test? it seems ci blocked on this test" (https://github.com/sgl-project/sglang/pull/3629#discussion_r1958991075)
- `2025-02-17T09:17:57Z` `inline` by `yizhang2077` `sgl-kernel/src/sgl-kernel/csrc/cublas_grouped_gemm.cu`:72; signals: gemm, kernel, memory; excerpt: "I think here would cause memory leak, try to use torch::tensor to control it" (https://github.com/sgl-project/sglang/pull/3629#discussion_r1957876643)
- `2025-02-17T17:32:30Z` `issue` by `yizhang2077`; signals: cuda, gemm, hang; excerpt: "Since pytorch 2.5.1 only supports cuda12.4 in official docs, and we can not change pytorch version easily, we need to update doc to guide ..." (https://github.com/sgl-project/sglang/pull/3629#issuecomment-2663737796)
- `2025-02-17T09:26:53Z` `inline` by `yizhang2077` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:350; signals: kernel, moe; excerpt: "Can you seperate it into 2 pr? This PR can be only for sgl-kernel part" (https://github.com/sgl-project/sglang/pull/3629#discussion_r1957890303)
- `2025-02-17T19:53:15Z` `inline` by `Fridge003` `sgl-kernel/src/sgl-kernel/csrc/cublas_grouped_gemm.cu`:72; signals: gemm, kernel; excerpt: "Modified" (https://github.com/sgl-project/sglang/pull/3629#discussion_r1958724884)
