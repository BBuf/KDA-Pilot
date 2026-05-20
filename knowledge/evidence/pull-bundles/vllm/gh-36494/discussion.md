# PR Discussion Digest

- Source PR: [vllm-project/vllm#36494](https://github.com/vllm-project/vllm/pull/36494)
- Source page: `sources/prs/vllm/PR-36494.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36494`
- Generated at: `2026-05-20T15:40:13.276428+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T12:39:21Z`
- Merged: `2026-03-10T06:11:27Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: amirkl94, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-09T12:43:36Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request removes a NotImplementedError to enable Expert Parallelism (EP) for the TensorRT-LLM Mixture of ... (https://github.com/vllm-project/vllm/pull/36494#pullrequestreview-3915145221)
- `2026-03-09T14:16:07Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/36494#pullrequestreview-3915728055)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-03-09T15:09:25Z` `issue` by `mgoin`; signals: b200, block, flashinfer, fp8, moe, triton; excerpt: "@amirkl94 Can we add a test case to the moe refactor? Like we should be able to add a case similar to tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml with ..." (https://github.com/vllm-project/vllm/pull/36494#issuecomment-4024457166)
- `2026-03-09T17:43:07Z` `issue` by `amirkl94`; signals: b200, block, flashinfer, fp8, moe, triton; excerpt: "@amirkl94 Can we add a test case to the moe refactor? Like we should be able to add a case similar to tests/evals/gsm8k/configs/moe-refactor-dp-ep/Llama-4-Scout-Fp8-ModelOpt-triton.yaml with ..." (https://github.com/vllm-project/vllm/pull/36494#issuecomment-4025612459)
- `2026-03-09T12:59:52Z` `issue` by `amirkl94`; signals: general review; excerpt: "@robertgshaw2-redhat Can you review as well? Just want to make sure there isn't a different reason this was disabled." (https://github.com/vllm-project/vllm/pull/36494#issuecomment-4023585481)
