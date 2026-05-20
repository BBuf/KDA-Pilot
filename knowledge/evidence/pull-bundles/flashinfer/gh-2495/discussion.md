# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2495](https://github.com/flashinfer-ai/flashinfer/pull/2495)
- Source page: `sources/prs/flashinfer/PR-2495.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2495`
- Generated at: `2026-05-20T15:24:54.416269+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-04T21:39:11Z`
- Merged: `2026-02-05T20:25:33Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 9 (approved=4, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: aleozlx, coderabbitai, djns99, nv-yunzheq, yzh119
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-04T21:41:21Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds necessary support checks for GEMM configurations in CUTLASS MoE kernels, specifically for ... (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3753440174)
- `2026-02-04T22:01:47Z` `COMMENTED` by `djns99` (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3753511367)
- `2026-02-04T22:02:42Z` `APPROVED` by `djns99` (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3753514060)
- `2026-02-04T23:36:04Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3753799739)
- `2026-02-05T00:25:05Z` `COMMENTED` by `nv-yunzheq` (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3753912473)
- `2026-02-05T00:28:18Z` `COMMENTED` by `djns99` (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3753919255)
- `2026-02-05T00:42:23Z` `COMMENTED` by `nv-yunzheq` (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3753945285)
- `2026-02-05T16:35:50Z` `APPROVED` by `aleozlx` - tests clean approved again (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3758206708)
- `2026-02-05T20:25:24Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2495#pullrequestreview-3759272633)

## Inline Comment Hotspots

- `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`: 6 inline comment(s)

## High-Signal Discussion

- `2026-02-04T21:39:30Z` `issue` by `coderabbitai`; signals: aligned, alignment, cutlass, epilogue, gemm, hang, kernel, memory; excerpt: "📝 Walkthrough Walkthrough Added runtime validation in MOE GEMM dispatch to enforce NO SMEM epilogue constraints: require output N alignment based on OutputType bit-width ..." (https://github.com/flashinfer-ai/flashinfer/pull/2495#issuecomment-3849876839)
- `2026-02-04T22:01:47Z` `inline` by `djns99` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`:986; signals: cutlass, gemm, kernel, moe, sm90, tensorrt; excerpt: "If we put this in runGemm/dispatchToArch we don't need to have two copies of this check. Maybe [here]( since this is only relevant for ..." (https://github.com/flashinfer-ai/flashinfer/pull/2495#discussion_r2766167802)
- `2026-02-05T00:25:05Z` `inline` by `nv-yunzheq` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`:986; signals: cutlass, gemm, kernel, moe, tensorrt; excerpt: "dispatchToArch doesn't work as we could not know if the activation is gated or not in the function. runGemm works, but to align with ..." (https://github.com/flashinfer-ai/flashinfer/pull/2495#discussion_r2766518604)
- `2026-02-05T00:28:18Z` `inline` by `djns99` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`:986; signals: cutlass, gemm, kernel, moe, tensorrt; excerpt: "We dont need to check isGatedActivation here This line sets the value of N correctly. The original check is only working with inter size ..." (https://github.com/flashinfer-ai/flashinfer/pull/2495#discussion_r2766525784)
- `2026-02-05T00:42:23Z` `inline` by `nv-yunzheq` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`:986; signals: cutlass, gemm, kernel, moe, tensorrt; excerpt: "Thanks. Updated to dispatchToArch" (https://github.com/flashinfer-ai/flashinfer/pull/2495#discussion_r2766550774)
