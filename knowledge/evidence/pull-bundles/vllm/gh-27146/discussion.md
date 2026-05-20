# PR Discussion Digest

- Source PR: [vllm-project/vllm#27146](https://github.com/vllm-project/vllm/pull/27146)
- Source page: `sources/prs/vllm/PR-27146.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27146`
- Generated at: `2026-05-20T15:38:13.565013+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-18T08:00:21Z`
- Merged: `2025-10-22T04:22:39Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 8 (approved=3, commented=5)
- Inline review comments: 11
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=6
- Human participants with discussion text: ProExpertProg, ZJY0516
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-10-18T08:02:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables the silu mul fp8 quant fusion pass to work even when the ... (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3352752108)
- `2025-10-18T23:02:33Z` `COMMENTED` by `ProExpertProg` - Looks great! For tests, could you only generate relevant tests, and then skip based on support (right now ... (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3353853543)
- `2025-10-19T02:22:48Z` `COMMENTED` by `ZJY0516` (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3353923197)
- `2025-10-19T04:00:46Z` `COMMENTED` by `ZJY0516` (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3353939712)
- `2025-10-19T06:23:00Z` `COMMENTED` by `ZJY0516` (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3353970510)
- `2025-10-20T15:50:33Z` `APPROVED` by `ProExpertProg` - Great work! Could you post some E2E perf and accuracy numbers? And would you be interested in adding ... (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3356995210)
- `2025-10-20T22:05:08Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3358080146)
- `2025-10-21T22:58:38Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3363020848)

## Inline Comment Hotspots

- `tests/compile/test_silu_mul_quant_fusion.py`: 7 inline comment(s)
- `vllm/compilation/matcher_utils.py`: 2 inline comment(s)
- `vllm/compilation/activation_quant_fusion.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-20T16:08:24Z` `issue` by `ZJY0516`; signals: accuracy, fp8, perf; excerpt: "Great work! Could you post some E2E perf and accuracy numbers? Do you know which model use silu mul and fp8 quant? And would ..." (https://github.com/vllm-project/vllm/pull/27146#issuecomment-3422762995)
- `2025-10-20T15:50:33Z` `review` `APPROVED` by `ProExpertProg`; signals: accuracy, perf; excerpt: "Great work! Could you post some E2E perf and accuracy numbers? And would you be interested in adding dynamic quant support as a follow-up?" (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3356995210)
- `2025-10-18T22:55:19Z` `inline` by `ProExpertProg` `tests/compile/test_silu_mul_quant_fusion.py`:162; signals: compile; excerpt: "Nit: can you skip generation of these tests? Better not to skip tests that shouldn't exist at all" (https://github.com/vllm-project/vllm/pull/27146#discussion_r2442670309)
- `2025-10-18T23:02:33Z` `review` `COMMENTED` by `ProExpertProg`; signals: general review; excerpt: "Looks great! For tests, could you only generate relevant tests, and then skip based on support (right now it's a little bit mixed up)" (https://github.com/vllm-project/vllm/pull/27146#pullrequestreview-3353853543)
- `2025-10-19T06:23:00Z` `inline` by `ZJY0516` `tests/compile/test_silu_mul_quant_fusion.py`:162; signals: compile; excerpt: "I have updated the test generation" (https://github.com/vllm-project/vllm/pull/27146#discussion_r2442783549)
- `2025-10-20T15:47:56Z` `inline` by `ProExpertProg` `tests/compile/test_silu_mul_quant_fusion.py`:125; signals: compile; excerpt: "Nit: I would inline these into the @pytest.mark.parametrize call" (https://github.com/vllm-project/vllm/pull/27146#discussion_r2445410654)
- `2025-10-20T15:48:11Z` `inline` by `ProExpertProg` `tests/compile/test_silu_mul_quant_fusion.py`:155; signals: compile; excerpt: "Nit:" (https://github.com/vllm-project/vllm/pull/27146#discussion_r2445411287)
- `2025-10-20T22:07:45Z` `issue` by `ProExpertProg`; signals: fp8; excerpt: "Do you know which model use silu mul and fp8 quant? silu mul is used by basically all models. fp8 quant is used by ..." (https://github.com/vllm-project/vllm/pull/27146#issuecomment-3423903639)
- `2025-10-21T15:53:18Z` `issue` by `ZJY0516`; signals: blackwell; excerpt: "The error message is very strange. I don't have blackwell machine. Would you be able to help resolve the blackwell-fusion-tests? @ProExpertProg" (https://github.com/vllm-project/vllm/pull/27146#issuecomment-3427374984)
- `2025-10-18T22:45:41Z` `inline` by `ProExpertProg` `vllm/compilation/matcher_utils.py`:35; signals: general review; excerpt: "Nit: we don't need this constant, it's just used in one place right? I want to start cleaning up these constants that we no ..." (https://github.com/vllm-project/vllm/pull/27146#discussion_r2442653981)
- `2025-10-18T22:47:45Z` `inline` by `ProExpertProg` `vllm/compilation/activation_quant_fusion.py`:113; signals: general review; excerpt: "This should be just input, no?" (https://github.com/vllm-project/vllm/pull/27146#discussion_r2442657686)
- `2025-10-19T02:22:48Z` `inline` by `ZJY0516` `vllm/compilation/matcher_utils.py`:35; signals: general review; excerpt: "It will be used in test file too." (https://github.com/vllm-project/vllm/pull/27146#discussion_r2442724678)
