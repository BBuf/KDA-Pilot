# PR Discussion Digest

- Source PR: [vllm-project/vllm#35088](https://github.com/vllm-project/vllm/pull/35088)
- Source page: `sources/prs/vllm/PR-35088.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35088`
- Generated at: `2026-05-20T15:39:58.118562+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-23T08:49:02Z`
- Merged: `2026-02-24T15:25:45Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: danisereb, mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T08:51:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly addresses a performance issue with the flashinfer MoE kernels. The original code ... (https://github.com/vllm-project/vllm/pull/35088#pullrequestreview-3839794987)
- `2026-02-23T15:33:38Z` `APPROVED` by `mgoin` - Makes sense, LGTM (https://github.com/vllm-project/vllm/pull/35088#pullrequestreview-3841796568)
- `2026-02-23T15:39:24Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/35088#pullrequestreview-3841832274)
- `2026-02-23T20:06:48Z` `APPROVED` by `pavanimajety` - Seems like the test failures are unrelated (model architectures in the failing tests likely won't invoke trtllm FP4 ... (https://github.com/vllm-project/vllm/pull/35088#pullrequestreview-3843251331)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-23T20:06:48Z` `review` `APPROVED` by `pavanimajety`; signals: failing, flashinfer, fp4, kernel, latency, moe, perf, performance; excerpt: "Seems like the test failures are unrelated (model architectures in the failing tests likely won't invoke trtllm FP4 moe kernels) There's still a bug ..." (https://github.com/vllm-project/vllm/pull/35088#pullrequestreview-3843251331)
- `2026-02-23T15:39:24Z` `inline` by `danisereb` `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`:351; signals: flashinfer, fp4, moe, mxfp4; excerpt: "Like I mentioned in the PR description, I followed the reshape from Mxfp4MoEMethod.apply monolithic. As far as I understand, reshape() uses a view when ..." (https://github.com/vllm-project/vllm/pull/35088#discussion_r2841551332)
- `2026-02-23T15:33:27Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`:351; signals: flashinfer, fp4, moe; excerpt: "Is reshape required or could we use view here? I just ask so we avoid the implicit .contiguous() that reshape has" (https://github.com/vllm-project/vllm/pull/35088#discussion_r2841520302)
- `2026-02-23T17:11:17Z` `issue` by `danisereb`; signals: flashinfer, hang; excerpt: "Rebased to get this change: seems to be related to the CI failures I see. There's still a bug in certain cases (num tokens ..." (https://github.com/vllm-project/vllm/pull/35088#issuecomment-3946082882)
