# PR Discussion Digest

- Source PR: [sgl-project/sglang#10858](https://github.com/sgl-project/sglang/pull/10858)
- Source page: `sources/prs/sglang/PR-10858.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10858`
- Generated at: `2026-05-20T15:27:21.839277+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-24T07:39:02Z`
- Merged: `2026-01-30T05:53:53Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: deepvars, mingfeima, polisettyvarma
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-24T07:40:53Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to enable the deepseek model on XPU by making CUDA-specific kernel imports ... (https://github.com/sgl-project/sglang/pull/10858#pullrequestreview-3261514795)
- `2025-09-24T07:41:38Z` `COMMENTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/10858#pullrequestreview-3261518655)
- `2025-09-24T08:16:30Z` `COMMENTED` by `deepvars` (https://github.com/sgl-project/sglang/pull/10858#pullrequestreview-3261674893)
- `2025-09-24T08:36:56Z` `COMMENTED` by `polisettyvarma` (https://github.com/sgl-project/sglang/pull/10858#pullrequestreview-3261779800)
- `2025-09-25T03:08:00Z` `APPROVED` by `deepvars` (https://github.com/sgl-project/sglang/pull/10858#pullrequestreview-3265430164)
- `2025-11-06T07:42:43Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/10858#pullrequestreview-3426678048)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-09-26T04:50:24Z` `issue` by `mingfeima`; signals: cutlass, fp8, hang, kernel, moe; excerpt: "duplicated with changes in cutlass w4a8 moe.py is not needed at the moment: right now intel xpu does not really support --quantization w4afp8 recipe, ..." (https://github.com/sgl-project/sglang/pull/10858#issuecomment-3336767077)
- `2025-09-24T08:36:56Z` `inline` by `polisettyvarma` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:9; signals: cuda, cutlass, hang, moe; excerpt: "changed to is cuda alike" (https://github.com/sgl-project/sglang/pull/10858#discussion_r2374988543)
- `2025-09-24T08:15:47Z` `inline` by `deepvars` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:9; signals: cuda, cutlass, moe; excerpt: "should we use is cuda() here or is cuda alike ? Or may be just check not XPU here ?" (https://github.com/sgl-project/sglang/pull/10858#discussion_r2374904548)
- `2025-09-24T07:52:15Z` `issue` by `mingfeima`; signals: cuda, kernel, moe; excerpt: "I don't think that we have implemented w4a8 moe on intel gpus yet. Even we have done this job. We most likely don't need ..." (https://github.com/sgl-project/sglang/pull/10858#issuecomment-3327068732)
- `2025-09-24T07:41:38Z` `inline` by `polisettyvarma` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:17; signals: cutlass, moe; excerpt: "not right way to fix this" (https://github.com/sgl-project/sglang/pull/10858#discussion_r2374788643)
- `2025-09-26T05:09:06Z` `issue` by `polisettyvarma`; signals: bf16; excerpt: "i have removed duplicate code @mingfeima quantization is None by default and got this issue when running with bf16" (https://github.com/sgl-project/sglang/pull/10858#issuecomment-3336798545)
- `2025-11-06T07:43:58Z` `issue` by `mingfeima`; signals: accuracy; excerpt: "@polisettyvarma try to attach the run command lines on xpu in the Accuracy Tests part in PR description." (https://github.com/sgl-project/sglang/pull/10858#issuecomment-3495578410)
- `2025-11-06T13:25:38Z` `issue` by `polisettyvarma`; signals: accuracy; excerpt: "@polisettyvarma try to attach the run command lines on xpu in the Accuracy Tests part in PR description. @mingfeima updated, please check" (https://github.com/sgl-project/sglang/pull/10858#issuecomment-3497260281)
- `2025-09-24T07:42:28Z` `issue` by `polisettyvarma`; signals: general review; excerpt: "@Edwardf0t1 @kushanam @BBuf @ch-wan @HaiShaw @ispobock @zhyncs @Ying1123 @merrymercy @Alcanderian @mingfeima please review" (https://github.com/sgl-project/sglang/pull/10858#issuecomment-3327024815)
- `2025-11-10T07:52:17Z` `issue` by `polisettyvarma`; signals: general review; excerpt: "please review @BBuf, @Edwardf0t1, @Fridge003, @HaiShaw, @Ying1123, @ch-wan, @ispobock, @kushanam and @merrymercy previous and current failed CI tests are not related to this PR" (https://github.com/sgl-project/sglang/pull/10858#issuecomment-3509957761)
