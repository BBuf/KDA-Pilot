# PR Discussion Digest

- Source PR: [vllm-project/vllm#25935](https://github.com/vllm-project/vllm/pull/25935)
- Source page: `sources/prs/vllm/PR-25935.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25935`
- Generated at: `2026-05-20T15:37:58.160531+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T08:11:04Z`
- Merged: `2025-10-01T02:19:54Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: certainly-param, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-30T08:12:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly addresses a runtime error when using INT8 quantization on Blackwell (SM100+) GPUs ... (https://github.com/vllm-project/vllm/pull/25935#pullrequestreview-3283158936)
- `2025-09-30T16:54:45Z` `COMMENTED` by `yewentao256` - This gives better log for int8, but not actually fix the problem, is there any chance you can ... (https://github.com/vllm-project/vllm/pull/25935#pullrequestreview-3285914726)
- `2025-09-30T19:30:13Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/25935#pullrequestreview-3286434646)
- `2025-09-30T19:32:42Z` `APPROVED` by `mgoin` - Thanks for the improvement (https://github.com/vllm-project/vllm/pull/25935#pullrequestreview-3286441533)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/kernels/scaled_mm/cutlass.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-30T17:07:26Z` `issue` by `certainly-param`; signals: accuracy, blackwell, fp8, perf, performance; excerpt: "throughly Yeah, I think the best approach is to auto-convert INT8 to FP8 on Blackwell GPUs. The hardware doesn't have INT8 tensor cores anyway ..." (https://github.com/vllm-project/vllm/pull/25935#issuecomment-3353082793)
- `2025-09-30T19:06:41Z` `issue` by `certainly-param`; signals: blackwell, fp8, hang, kernel; excerpt: "Thanks for the work! I am thinking "auto-convert INT8 to FP8" is not a ideal way to realize it, perhaps we can have another ..." (https://github.com/vllm-project/vllm/pull/25935#issuecomment-3353451747)
- `2025-09-30T19:00:19Z` `issue` by `yewentao256`; signals: fp8, hang; excerpt: "Thanks for the work! I am thinking "auto-convert INT8 to FP8" is not a ideal way to realize it, perhaps we can have another ..." (https://github.com/vllm-project/vllm/pull/25935#issuecomment-3353429963)
- `2025-09-30T16:54:45Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "This gives better log for int8, but not actually fix the problem, is there any chance you can throughly fix it?" (https://github.com/vllm-project/vllm/pull/25935#pullrequestreview-3285914726)
