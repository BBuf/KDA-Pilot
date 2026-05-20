# PR Discussion Digest

- Source PR: [vllm-project/vllm#41664](https://github.com/vllm-project/vllm/pull/41664)
- Source page: `sources/prs/vllm/PR-41664.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-41664`
- Generated at: `2026-05-20T15:40:53.636020+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-04T21:12:40Z`
- Merged: `2026-05-12T11:49:33Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 8 (approved=2, commented=5, dismissed=1)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: claude, dsikka, kylesayrs, mergify, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-04T21:14:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request renames the MXFP4 quantization scheme to CompressedTensorsW4A4Mxfp4 and introduces support for true W4A4 ... (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4223568676)
- `2026-05-05T19:32:05Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4231049986)
- `2026-05-05T20:14:52Z` `COMMENTED` by `yewentao256` - Thanks for the work! (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4231318441)
- `2026-05-07T22:19:07Z` `APPROVED` by `kylesayrs` - Support looks good, was able to verify locally (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4248079400)
- `2026-05-08T18:19:18Z` `APPROVED` by `mgoin` - LGTM, thanks! (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4254419350)
- `2026-05-11T15:05:47Z` `DISMISSED` by `yewentao256` - Sorry to block for a while, please take a look at my previous comment (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4264851931)
- `2026-05-11T15:19:11Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4264950025)
- `2026-05-11T18:23:02Z` `COMMENTED` by `yewentao256` - Thanks for the work! A small update (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4265915559)

## Inline Comment Hotspots

- `vllm/model_executor/kernels/linear/mxfp4/flashinfer.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxfp4.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-05T20:14:45Z` `inline` by `yewentao256` `vllm/model_executor/kernels/linear/mxfp4/flashinfer.py`:42; signals: flashinfer, fp4, kernel, mxfp4; excerpt: "We will pad in swizzle mxfp4 scales, but here we will reshape using the current N eg Will this cause trouble?" (https://github.com/vllm-project/vllm/pull/41664#discussion_r3191294058)
- `2026-05-11T15:19:11Z` `inline` by `dsikka` `vllm/model_executor/kernels/linear/mxfp4/flashinfer.py`:42; signals: flashinfer, fp4, kernel, mxfp4; excerpt: "Addressed." (https://github.com/vllm-project/vllm/pull/41664#discussion_r3220047642)
- `2026-05-08T18:19:58Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @dsikka, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/41664#issuecomment-4408845115)
- `2026-05-05T19:32:05Z` `review` `COMMENTED` by `claude`; signals: general review; excerpt: "Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer can comment @claude review to run ..." (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4231049986)
- `2026-05-05T20:14:52Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Thanks for the work!" (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4231318441)
- `2026-05-11T15:19:04Z` `issue` by `dsikka`; signals: block; excerpt: "Sorry to block for a while, please take a look at my previous comment Sorry to block for a while, please take a look ..." (https://github.com/vllm-project/vllm/pull/41664#issuecomment-4422050463)
- `2026-05-11T18:23:02Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Thanks for the work! A small update" (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4265915559)
- `2026-05-11T15:05:47Z` `review` `DISMISSED` by `yewentao256`; signals: block; excerpt: "Sorry to block for a while, please take a look at my previous comment" (https://github.com/vllm-project/vllm/pull/41664#pullrequestreview-4264851931)
