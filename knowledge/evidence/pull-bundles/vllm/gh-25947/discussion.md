# PR Discussion Digest

- Source PR: [vllm-project/vllm#25947](https://github.com/vllm-project/vllm/pull/25947)
- Source page: `sources/prs/vllm/PR-25947.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25947`
- Generated at: `2026-05-20T15:38:00.360419+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T10:31:26Z`
- Merged: `2025-10-09T17:59:42Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: mgoin, pavanimajety, roikoren755
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-30T10:32:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a critical bug in padded FP4 quantization by ensuring that allocated tensors ... (https://github.com/vllm-project/vllm/pull/25947#pullrequestreview-3283875502)
- `2025-10-06T16:25:30Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/25947#pullrequestreview-3305834387)
- `2025-10-08T07:52:45Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/25947#pullrequestreview-3313464676)
- `2025-10-08T15:45:26Z` `APPROVED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/25947#pullrequestreview-3315483886)
- `2025-10-09T13:56:45Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25947#pullrequestreview-3319127166)

## Inline Comment Hotspots

- `vllm/_custom_ops.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-09T13:56:35Z` `issue` by `mgoin`; signals: fp4, gemm, kernel, tensorrt; excerpt: "Note that this specific model doesn't work with TP 2, and this PR doesn't solve issues that come up in those scenarios. For TP4 ..." (https://github.com/vllm-project/vllm/pull/25947#issuecomment-3386002939)
- `2025-10-08T08:41:04Z` `issue` by `roikoren755`; signals: fp4, hang, nvfp4; excerpt: "Thanks for the PR! Could you also post lm eval results for any other FP4 model to ensure that previous paths don't break? Ran ..." (https://github.com/vllm-project/vllm/pull/25947#issuecomment-3380415627)
- `2025-10-06T16:26:13Z` `issue` by `pavanimajety`; signals: fp4; excerpt: "Thanks for the PR! Could you also post lm eval results for any other FP4 model to ensure that previous paths don't break?" (https://github.com/vllm-project/vllm/pull/25947#issuecomment-3372647359)
- `2025-10-06T16:25:30Z` `inline` by `pavanimajety` `vllm/_custom_ops.py`:1377; signals: general review; excerpt: "When a tensor of required out shape is allocated, why do we also need to initialize it with zeros? The divisibility check is only ..." (https://github.com/vllm-project/vllm/pull/25947#discussion_r2407309216)
- `2025-10-08T07:52:45Z` `inline` by `roikoren755` `vllm/_custom_ops.py`:1377; signals: general review; excerpt: "Did it for consistency's sake, but you are correct, this allocation can stay as torch.empty. I'll revert this line." (https://github.com/vllm-project/vllm/pull/25947#discussion_r2412923929)
