# PR Discussion Digest

- Source PR: [vllm-project/vllm#25201](https://github.com/vllm-project/vllm/pull/25201)
- Source page: `sources/prs/vllm/PR-25201.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25201`
- Generated at: `2026-05-20T15:37:54.713979+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-18T20:14:23Z`
- Merged: `2025-09-23T23:39:50Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: SageMoore, jpvillam-amd, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-18T20:16:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces functional changes to support GPT-OSS on ROCm gfx950 hardware. The changes include ... (https://github.com/vllm-project/vllm/pull/25201#pullrequestreview-3241935627)
- `2025-09-23T16:23:51Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/25201#pullrequestreview-3258782705)
- `2025-09-23T19:53:57Z` `COMMENTED` by `jpvillam-amd` (https://github.com/vllm-project/vllm/pull/25201#pullrequestreview-3259399350)
- `2025-09-23T19:56:21Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25201#pullrequestreview-3259405134)
- `2025-09-23T19:59:39Z` `COMMENTED` by `jpvillam-amd` (https://github.com/vllm-project/vllm/pull/25201#pullrequestreview-3259413566)
- `2025-09-23T22:02:19Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25201#pullrequestreview-3259718681)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`: 3 inline comment(s)
- `vllm/envs.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/mxfp4.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-23T19:56:13Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:10; signals: block, fp4, mxfp4; excerpt: "Can you move this import into the elif current platform.is rocm(): block?" (https://github.com/vllm-project/vllm/pull/25201#discussion_r2373314273)
- `2025-09-23T19:59:39Z` `inline` by `jpvillam-amd` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:10; signals: fp4, mxfp4; excerpt: "Sure thing" (https://github.com/vllm-project/vllm/pull/25201#discussion_r2373320804)
- `2025-09-23T16:23:18Z` `inline` by `SageMoore` `vllm/envs.py`:894; signals: general review; excerpt: "It's not obvious to me why you need this environment variable. Just looking at the code, it looks like this is really a GFX950 ..." (https://github.com/vllm-project/vllm/pull/25201#discussion_r2372859907)
- `2025-09-23T19:53:57Z` `inline` by `jpvillam-amd` `vllm/envs.py`:894; signals: general review; excerpt: "You are right, we were thinking to allow for non-preshuffled scales but after some debate we don't think its necessary we are going with ..." (https://github.com/vllm-project/vllm/pull/25201#discussion_r2373309903)
