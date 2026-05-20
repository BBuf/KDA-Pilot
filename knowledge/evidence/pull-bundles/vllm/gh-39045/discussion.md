# PR Discussion Digest

- Source PR: [vllm-project/vllm#39045](https://github.com/vllm-project/vllm/pull/39045)
- Source page: `sources/prs/vllm/PR-39045.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-39045`
- Generated at: `2026-05-20T15:40:40.512922+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-05T21:14:09Z`
- Merged: `2026-04-09T01:57:53Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: NebulaTurnip27, dsikka, kylesayrs, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-05T21:18:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the Gemma4 model to support per-expert 2D quantized weights and scale parameters ... (https://github.com/vllm-project/vllm/pull/39045#pullrequestreview-4059848452)
- `2026-04-06T19:17:33Z` `APPROVED` by `kylesayrs` (https://github.com/vllm-project/vllm/pull/39045#pullrequestreview-4063932167)
- `2026-04-08T02:59:54Z` `APPROVED` by `mgoin` - Seems reasonable to me, please make sure the original checkpoints aren't affected (https://github.com/vllm-project/vllm/pull/39045#pullrequestreview-4072519241)

## Inline Comment Hotspots

- `vllm/model_executor/models/gemma4.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-04-08T00:23:43Z` `issue` by `NebulaTurnip27`; signals: fp4, gemm, nvfp4; excerpt: "With this PR, the model RedHatAI/gemma-4-26B-A4B-it-NVFP4 loads correctly, but when I interact with it, it never replies. The finish reason is always length, and ..." (https://github.com/vllm-project/vllm/pull/39045#issuecomment-4202994385)
- `2026-04-06T19:17:30Z` `inline` by `kylesayrs` `vllm/model_executor/models/gemma4.py`:1281; signals: gemm, hang; excerpt: "It seems like you could also handle this by leaving the current code unchanged and just adding another mapping (with higher priority)" (https://github.com/vllm-project/vllm/pull/39045#discussion_r3041221151)
- `2026-04-06T19:01:06Z` `inline` by `kylesayrs` `vllm/model_executor/models/gemma4.py`:1520; signals: gemm; excerpt: "I don't think that saving vLLM checkpoints is a real use case" (https://github.com/vllm-project/vllm/pull/39045#discussion_r3041144119)
- `2026-04-08T02:59:38Z` `inline` by `mgoin` `vllm/model_executor/models/gemma4.py`:1281; signals: gemm; excerpt: "What is the point if this will always match first?" (https://github.com/vllm-project/vllm/pull/39045#discussion_r3048948624)
