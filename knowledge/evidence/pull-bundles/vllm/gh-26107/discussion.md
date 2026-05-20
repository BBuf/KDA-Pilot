# PR Discussion Digest

- Source PR: [vllm-project/vllm#26107](https://github.com/vllm-project/vllm/pull/26107)
- Source page: `sources/prs/vllm/PR-26107.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26107`
- Generated at: `2026-05-20T15:38:03.876956+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-02T16:14:46Z`
- Merged: `2025-10-15T17:53:00Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 9 (approved=2, commented=7)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=5
- Human participants with discussion text: mergify, mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-02T16:16:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for cuDNN FP4 GEMM via FlashInfer, which is a great addition ... (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3295382684)
- `2025-10-06T17:27:26Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3306183099)
- `2025-10-06T17:27:50Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3306185190)
- `2025-10-06T17:28:12Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3306186931)
- `2025-10-06T18:39:02Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3306559561)
- `2025-10-06T21:57:43Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3307622682)
- `2025-10-06T22:02:22Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3307644538)
- `2025-10-15T16:15:11Z` `APPROVED` by `pavanimajety` - Thanks @kaixih and @mgoin, PR looks good to me and all the checks have passed (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3341282711)
- `2025-10-15T17:52:51Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26107#pullrequestreview-3341635888)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/modelopt.py`: 5 inline comment(s)
- `vllm/envs.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-06T17:27:26Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:855; signals: cutlass, flashinfer, fp4, gemm; excerpt: "can we simplify this to just specify VLLM FP4 GEMM BACKEND = {"flashinfer-cudnn, "trtllm", "cutlass") ?" (https://github.com/vllm-project/vllm/pull/26107#discussion_r2407589606)
- `2025-10-06T18:39:02Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:855; signals: cutlass, fp4, gemm, nvfp4; excerpt: "+1. Maybe we can be less careful with deprecation here and just switch. I vote for VLLM NVFP4 GEMM BACKEND = ("cudnn, "trtllm", "cutlass") ..." (https://github.com/vllm-project/vllm/pull/26107#discussion_r2407915768)
- `2025-10-06T22:02:22Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:1115; signals: flashinfer; excerpt: "Nit: May be also simplify this here? Since all of them just say flashinfer- ? Extract the string and call with the backend string ..." (https://github.com/vllm-project/vllm/pull/26107#discussion_r2408799277)
- `2025-10-06T17:27:50Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:855; signals: general review; excerpt: "Perhaps with a deprecation warning too, to not break earlier workflows." (https://github.com/vllm-project/vllm/pull/26107#discussion_r2407591426)
- `2025-10-06T17:28:13Z` `inline` by `pavanimajety` `vllm/envs.py`:1358; signals: general review; excerpt: "Same as above." (https://github.com/vllm-project/vllm/pull/26107#discussion_r2407592933)
- `2025-10-06T21:57:27Z` `inline` by `mgoin` `vllm/envs.py`:1269; signals: general review; excerpt: "Nit: You could use env with choices like" (https://github.com/vllm-project/vllm/pull/26107#discussion_r2408779670)
- `2025-10-06T02:54:49Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @kaixih." (https://github.com/vllm-project/vllm/pull/26107#issuecomment-3369756313)
- `2025-10-08T12:10:42Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @kaixih." (https://github.com/vllm-project/vllm/pull/26107#issuecomment-3381220694)
