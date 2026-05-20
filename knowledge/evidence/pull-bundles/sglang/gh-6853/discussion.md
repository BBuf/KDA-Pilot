# PR Discussion Digest

- Source PR: [sgl-project/sglang#6853](https://github.com/sgl-project/sglang/pull/6853)
- Source page: `sources/prs/sglang/PR-6853.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6853`
- Generated at: `2026-05-20T15:30:51.944304+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-04T01:51:41Z`
- Merged: `2025-06-08T00:24:35Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 6 (approved=1, changes_requested=1, commented=4)
- Inline review comments: 6
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: Edwardf0t1, pavanimajety, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-04T01:52:08Z` `COMMENTED` by `gemini-code-assist` - Hello @pavanimajety, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6853#pullrequestreview-2894610318)
- `2025-06-04T01:53:22Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces support for FP4 quantization for Mixture of Experts (MoE) layers, specifically targeting ... (https://github.com/sgl-project/sglang/pull/6853#pullrequestreview-2894613786)
- `2025-06-04T09:21:45Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6853#pullrequestreview-2895969235)
- `2025-06-05T03:50:51Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/6853#pullrequestreview-2898777081)
- `2025-06-06T08:27:54Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/6853#pullrequestreview-2904169141)
- `2025-06-08T00:23:56Z` `APPROVED` by `zhyncs` - unblock first (https://github.com/sgl-project/sglang/pull/6853#pullrequestreview-2907932644)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/cutlass_moe.py`: 2 inline comment(s)
- `sgl-kernel/python/sgl_kernel/moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-05T03:47:53Z` `issue` by `pavanimajety`; signals: cutlass, flashinfer, fp4, moe, perf, performance; excerpt: "Please note that this PR functionally enables FP4 Checkpoints. The optimizations for cutlass fp4 moe through Flashinfer are underway and will have more configs ..." (https://github.com/sgl-project/sglang/pull/6853#issuecomment-2942646630)
- `2025-06-04T09:21:45Z` `inline` by `zhyncs` `sgl-kernel/python/sgl_kernel/moe.py`:2; signals: hang, kernel, moe; excerpt: "Can we separate the changes to sgl-kernel into a separate PR, because I need to release a new version of sgl-kernel." (https://github.com/sgl-project/sglang/pull/6853#discussion_r2126121263)
- `2025-06-05T03:50:51Z` `inline` by `pavanimajety` `python/sglang/srt/layers/moe/cutlass_moe.py`:299; signals: cutlass, hang, moe; excerpt: "This sanity check is no longer relevant because m is not passed in as an input to the function. m changes at runtime and ..." (https://github.com/sgl-project/sglang/pull/6853#discussion_r2127883779)
- `2025-06-06T08:22:58Z` `inline` by `Edwardf0t1` `python/sglang/srt/layers/quantization/modelopt_quant.py`:325; signals: fp8, moe; excerpt: "I think we can make it more robust to cover FP8 fused moe as well." (https://github.com/sgl-project/sglang/pull/6853#discussion_r2131748934)
- `2025-06-08T00:23:56Z` `review` `APPROVED` by `zhyncs`; signals: block; excerpt: "unblock first" (https://github.com/sgl-project/sglang/pull/6853#pullrequestreview-2907932644)
- `2025-06-06T08:23:49Z` `inline` by `Edwardf0t1` `python/sglang/srt/layers/quantization/modelopt_quant.py`:319; signals: general review; excerpt: "Remove the commented code." (https://github.com/sgl-project/sglang/pull/6853#discussion_r2131750319)
