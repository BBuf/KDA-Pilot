# PR Discussion Digest

- Source PR: [sgl-project/sglang#3899](https://github.com/sgl-project/sglang/pull/3899)
- Source page: `sources/prs/sglang/PR-3899.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3899`
- Generated at: `2026-05-20T15:30:02.478478+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-26T23:06:19Z`
- Merged: `2025-03-25T02:50:24Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: kaixih, kushanam, pavanimajety, trevor-m, yiakwy-xpu-ml-framework-team, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-01T19:47:16Z` `COMMENTED` by `yiakwy-xpu-ml-framework-team` (https://github.com/sgl-project/sglang/pull/3899#pullrequestreview-2652568408)
- `2025-03-11T18:30:40Z` `COMMENTED` by `kushanam` (https://github.com/sgl-project/sglang/pull/3899#pullrequestreview-2675725231)
- `2025-03-13T21:52:33Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/3899#pullrequestreview-2683443709)
- `2025-03-13T21:55:37Z` `APPROVED` by `pavanimajety` - Reviewed the integrations and tests, LGTM. (https://github.com/sgl-project/sglang/pull/3899#pullrequestreview-2683447896)
- `2025-03-14T23:59:43Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/3899#pullrequestreview-2687094881)
- `2025-03-18T01:03:41Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/3899#pullrequestreview-2692505595)

## Inline Comment Hotspots

- `sgl-kernel/src/sgl-kernel/csrc/quantization/fp4/nvfp4_scaled_mm_kernels.cu`: 3 inline comment(s)
- `sgl-kernel/src/sgl-kernel/csrc/quantization/fp4/nvfp4_quant_entry.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-03-01T19:37:49Z` `issue` by `yiakwy-xpu-ml-framework-team`; signals: b200, cuda, fp4, fp8, kernel, ptx; excerpt: "@trevor-m Great efforts! I am working on FP4 type. My suggestion is only to keep fp4 with uint4 t so that both platform (AMD/NV)can ..." (https://github.com/sgl-project/sglang/pull/3899#issuecomment-2692380913)
- `2025-03-01T19:47:16Z` `inline` by `yiakwy-xpu-ml-framework-team` `sgl-kernel/src/sgl-kernel/csrc/quantization/fp4/nvfp4_quant_entry.cu`:11; signals: b200, cuda, fp4, kernel, nvfp4; excerpt: "Only work for B200. It will be very hard for SGLang team to verify. I suggested to implement FP4 cuda kernel without NV intrinsics ..." (https://github.com/sgl-project/sglang/pull/3899#discussion_r1976481120)
- `2025-03-11T18:30:40Z` `inline` by `kushanam` `sgl-kernel/src/sgl-kernel/csrc/quantization/fp4/nvfp4_quant_entry.cu`:11; signals: blackwell, fp4, kernel, nvfp4; excerpt: "@yiakwy-xpu-ml-framework-team I believe this feature is specific to Blackwell and is being added accordingly. Creating a generic kernel is beyond the scope of this ..." (https://github.com/sgl-project/sglang/pull/3899#discussion_r1989914447)
- `2025-03-13T21:52:33Z` `inline` by `pavanimajety` `sgl-kernel/src/sgl-kernel/csrc/quantization/fp4/nvfp4_scaled_mm_kernels.cu`:250; signals: cuda, fp4, kernel, nvfp4; excerpt: "super minor/nit: When the error prints, there won't be a space. It would print as Eg: 'amust be a CUDA tensor"." (https://github.com/sgl-project/sglang/pull/3899#discussion_r1994350359)
- `2025-03-14T23:56:12Z` `inline` by `kaixih` `sgl-kernel/src/sgl-kernel/csrc/quantization/fp4/nvfp4_scaled_mm_kernels.cu`:16; signals: fp4, kernel, nvfp4; excerpt: "maybe we can use template to reduce the dups. (like [here](" (https://github.com/sgl-project/sglang/pull/3899#discussion_r1996444422)
- `2025-03-18T01:03:41Z` `inline` by `trevor-m` `sgl-kernel/src/sgl-kernel/csrc/quantization/fp4/nvfp4_scaled_mm_kernels.cu`:16; signals: fp4, kernel, nvfp4; excerpt: "Thanks, fixed" (https://github.com/sgl-project/sglang/pull/3899#discussion_r1999938901)
