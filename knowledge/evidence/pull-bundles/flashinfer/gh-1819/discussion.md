# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1819](https://github.com/flashinfer-ai/flashinfer/pull/1819)
- Source page: `sources/prs/flashinfer/PR-1819.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1819`
- Generated at: `2026-05-20T15:23:26.770671+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T15:30:24Z`
- Merged: `2025-10-12T03:51:02Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: djmmoss, yongwww, yzh119
- Automation comments/reviews omitted from high-signal summary: 11
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-30T15:34:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for FP8 block scaling in fused Mixture-of-Experts (MoE) kernels for SM90 ... (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3285615084)
- `2025-09-30T22:40:32Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3286926596)
- `2025-09-30T22:43:34Z` `COMMENTED` by `djmmoss` (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3286934439)
- `2025-10-02T01:30:58Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3291786493)
- `2025-10-02T01:33:09Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3291789380)
- `2025-10-02T17:43:02Z` `COMMENTED` by `djmmoss` (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3295725287)
- `2025-10-02T17:59:30Z` `COMMENTED` by `djmmoss` (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3295781353)
- `2025-10-11T06:14:41Z` `APPROVED` by `yzh119` - LGTM, should be ready to merge once finishes. Thanks for the great work @djmmoss ! (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3326706567)
- `2025-10-11T20:45:25Z` `COMMENTED` by `djmmoss` (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3327578793)
- `2025-10-12T03:50:56Z` `APPROVED` by `yzh119` - The failed pipelines are irrerevant to this PR (spark & hopper), let's resolve them in a standalone PR. (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3327867894)

## Inline Comment Hotspots

- `flashinfer/jit/core.py`: 4 inline comment(s)
- `csrc/nv_internal/tensorrt_llm/deep_gemm/compiler.cuh`: 3 inline comment(s)
- `flashinfer/jit/fused_moe.py`: 2 inline comment(s)
- `csrc/nv_internal/tensorrt_llm/deep_gemm/fp8_gemm.cuh`: 1 inline comment(s)
- `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_gemm.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-02T17:43:02Z` `inline` by `djmmoss` `csrc/nv_internal/tensorrt_llm/deep_gemm/compiler.cuh`:1; signals: blackwell, compile, deepgemm, flashinfer, gemm, hopper, kernel, tensorrt; excerpt: "The tensorrt llm/deep gemm files are generated here: I checked the deepgemm kernels that have already been integrated into flashinfer, currently they only seem ..." (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2399594153)
- `2025-10-02T01:30:30Z` `inline` by `yzh119` `csrc/nv_internal/tensorrt_llm/deep_gemm/compiler.cuh`:1; signals: compile, deepgemm, gemm, hang, kernel, tensorrt; excerpt: "How are these implementations from We already have deepgemm kernels If there are not significant changes, we should unify them (maybe not in this ..." (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2396406428)
- `2025-10-02T01:33:09Z` `inline` by `yzh119` `flashinfer/jit/core.py`:270; signals: compile, cuda, flashinfer, fp4; excerpt: "Yes c++ files will be compiled with gcc instead of nvcc. Considering these file includes cuda headers, can we rename it to fp4Op.cu instead?" (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2396408849)
- `2025-10-11T06:14:09Z` `inline` by `yzh119` `flashinfer/jit/fused_moe.py`:152; signals: cuda, flashinfer, moe; excerpt: "nit: -lcuda is no longer required since" (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2422526466)
- `2025-10-02T17:59:30Z` `inline` by `djmmoss` `flashinfer/jit/core.py`:270; signals: flashinfer, hang; excerpt: "ah, this was actually fixed in different PR. I've removed this change" (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2399634679)
- `2025-10-11T20:45:24Z` `inline` by `djmmoss` `flashinfer/jit/fused_moe.py`:152; signals: flashinfer, moe; excerpt: "removed it" (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2423126338)
- `2025-10-12T03:50:56Z` `review` `APPROVED` by `yzh119`; signals: hopper, pipeline; excerpt: "The failed pipelines are irrerevant to this PR (spark & hopper), let's resolve them in a standalone PR." (https://github.com/flashinfer-ai/flashinfer/pull/1819#pullrequestreview-3327867894)
- `2025-09-30T22:43:34Z` `inline` by `djmmoss` `flashinfer/jit/core.py`:270; signals: flashinfer; excerpt: "When I was compiling, they weren't enabled in the JIT mode, I'm not sure it this was an environment issue, but I just installed ..." (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2392993202)
- `2025-09-30T22:40:32Z` `inline` by `yzh119` `flashinfer/jit/core.py`:270; signals: flashinfer; excerpt: "Why do we need this? They are nvcc native macros." (https://github.com/flashinfer-ai/flashinfer/pull/1819#discussion_r2392986609)
- `2025-10-09T21:24:00Z` `issue` by `djmmoss`; signals: block; excerpt: "@yzh119 any blockers on getting this in?" (https://github.com/flashinfer-ai/flashinfer/pull/1819#issuecomment-3387536019)
