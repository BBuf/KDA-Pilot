# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1460](https://github.com/flashinfer-ai/flashinfer/pull/1460)
- Source page: `sources/prs/flashinfer/PR-1460.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1460`
- Generated at: `2026-05-20T15:22:42.160981+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-11T09:29:54Z`
- Merged: `2025-08-14T06:34:12Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: elvischenv, nvpohanh, weireweire, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-11T09:30:20Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @elvischenv, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3104850351)
- `2025-08-11T09:33:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly addresses an issue with shape checking for FP4 scale factor tensors when ... (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3104858444)
- `2025-08-11T09:54:26Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3104974394)
- `2025-08-12T04:41:07Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3108512353)
- `2025-08-12T04:44:05Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3108516141)
- `2025-08-12T04:54:22Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3108530108)
- `2025-08-12T09:43:10Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3109628096)
- `2025-08-12T09:43:26Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3109629637)
- `2025-08-14T01:54:58Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3118350955)
- `2025-08-14T02:15:04Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3118465564)
- `2025-08-14T05:53:43Z` `APPROVED` by `nvpohanh` (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3119118050)
- `2025-08-14T06:34:02Z` `APPROVED` by `yzh119` - LGTM, thanks @elvischenv for shape fix and @weireweire @nvpohanh 's review! (https://github.com/flashinfer-ai/flashinfer/pull/1460#pullrequestreview-3119196047)

## Inline Comment Hotspots

- `flashinfer/prefill.py`: 4 inline comment(s)
- `flashinfer/decode.py`: 2 inline comment(s)
- `tests/utils_fp4.py`: 2 inline comment(s)
- `tests/test_trtllm_gen_attention.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-12T04:41:07Z` `inline` by `weireweire` `flashinfer/prefill.py`:3230; signals: flashinfer, fp4, hang; excerpt: "please add check that o.shape + offset < scale.shape, only add in FP4Tensor.init is unsafe as user may change the tensor after init." (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2268558652)
- `2025-08-12T04:54:22Z` `inline` by `weireweire` `tests/utils_fp4.py`:89; signals: fp4, hang; excerpt: "maybe change to full m" (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2268572736)
- `2025-08-12T09:43:10Z` `inline` by `elvischenv` `flashinfer/prefill.py`:3230; signals: flashinfer, hang; excerpt: "Thanks. Please help check if current change looks good to you." (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2269299904)
- `2025-08-11T09:54:26Z` `inline` by `elvischenv` `flashinfer/decode.py`:2099; signals: flashinfer; excerpt: "Good catch. Fixed." (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2266198227)
- `2025-08-12T04:44:05Z` `inline` by `weireweire` `flashinfer/prefill.py`:3230; signals: flashinfer; excerpt: "actually, even the out is None branch need this check, so add to outside the branch." (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2268561812)
- `2025-08-12T09:43:26Z` `inline` by `elvischenv` `tests/utils_fp4.py`:89; signals: fp4; excerpt: "Fixed." (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2269300789)
- `2025-08-14T01:54:58Z` `inline` by `weireweire` `tests/test_trtllm_gen_attention.py`:167; signals: attention; excerpt: "then line 177 should use "rounded extra size" for distinguish." (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2275094201)
- `2025-08-14T02:15:04Z` `inline` by `elvischenv` `tests/test_trtllm_gen_attention.py`:167; signals: attention; excerpt: "Fixed. Thanks for the review." (https://github.com/flashinfer-ai/flashinfer/pull/1460#discussion_r2275158041)
