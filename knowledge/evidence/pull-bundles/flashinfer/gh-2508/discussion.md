# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2508](https://github.com/flashinfer-ai/flashinfer/pull/2508)
- Source page: `sources/prs/flashinfer/PR-2508.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2508`
- Generated at: `2026-05-20T15:24:57.134654+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-06T10:27:57Z`
- Merged: `2026-02-14T17:26:35Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: IwakuraRein, aleozlx, coderabbitai, dbari, yzh119
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-06T10:30:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a type mismatch issue in the trtllm fp8 per tensor scale moe ... (https://github.com/flashinfer-ai/flashinfer/pull/2508#pullrequestreview-3762206212)
- `2026-02-09T18:58:17Z` `APPROVED` by `aleozlx` - lgtm (https://github.com/flashinfer-ai/flashinfer/pull/2508#pullrequestreview-3774849823)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-02-06T10:28:32Z` `issue` by `coderabbitai`; signals: attention, autotune, benchmark, block, cute, flashinfer, fp8, gemm; excerpt: "📝 Walkthrough Walkthrough Replaced enum-typed ActivationType parameters with integer activation type (using .value) across fused MoE public APIs and call sites in flashinfer/fused moe/core.py, ..." (https://github.com/flashinfer-ai/flashinfer/pull/2508#issuecomment-3859496242)
- `2026-02-12T17:59:30Z` `issue` by `IwakuraRein`; signals: block, fp4, fp8, moe; excerpt: "trtllm fp4 block scale moe op has activation type: int = ActivationType.Swiglu.value,. Maybe it's better to unify trtllm fp4 block scale moe op and ..." (https://github.com/flashinfer-ai/flashinfer/pull/2508#issuecomment-3892517244)
- `2026-02-13T21:05:22Z` `issue` by `yzh119`; signals: block, fp4, fp8, moe; excerpt: "Hi @dbari I have merged your commits. Maybe it's better to unify trtllm fp4 block scale moe op and trtllm fp8 per tensor scale ..." (https://github.com/flashinfer-ai/flashinfer/pull/2508#issuecomment-3899457926)
- `2026-02-06T12:01:50Z` `issue` by `dbari`; signals: fp4; excerpt: "I adapted the tests to match the function signature and made it consistent with the fp4 functions here: Feel free to include it in ..." (https://github.com/flashinfer-ai/flashinfer/pull/2508#issuecomment-3860045996)
