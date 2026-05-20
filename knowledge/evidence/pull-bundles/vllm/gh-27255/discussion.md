# PR Discussion Digest

- Source PR: [vllm-project/vllm#27255](https://github.com/vllm-project/vllm/pull/27255)
- Source page: `sources/prs/vllm/PR-27255.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27255`
- Generated at: `2026-05-20T15:38:15.308014+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-21T08:26:44Z`
- Merged: `2025-11-05T11:06:07Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: amirkl94, mgoin, robertgshaw2-redhat, tlrmchlsmth, wenscarl
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-10-21T08:28:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly addresses a bug in the Cutlass FP8 FusedMoE implementation by passing the ... (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3359391168)
- `2025-10-30T20:51:40Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3401602071)
- `2025-11-04T12:09:58Z` `APPROVED` by `mgoin` - LGTM, please validate @wenscarl (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3416110528)
- `2025-11-04T13:40:42Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3416508291)
- `2025-11-04T15:31:21Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3417120028)
- `2025-11-04T15:48:54Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3417214843)
- `2025-11-05T07:07:16Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3420226652)
- `2025-11-05T09:38:27Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/27255#pullrequestreview-3420858405)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/modelopt.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 2 inline comment(s)
- `tests/kernels/moe/test_flashinfer.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-04T13:36:54Z` `inline` by `wenscarl` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py`:173; signals: cutlass, flashinfer, moe; excerpt: "I suggest using a more descriptive condition, for example:" (https://github.com/vllm-project/vllm/pull/27255#discussion_r2490548291)
- `2025-11-05T07:07:15Z` `inline` by `amirkl94` `vllm/model_executor/layers/quantization/modelopt.py`:573; signals: fp8, moe; excerpt: "I'd rather not move this calculation inside the function as I'm not sure if in the future other paths will require different factors. If ..." (https://github.com/vllm-project/vllm/pull/27255#discussion_r2493261272)
- `2025-11-04T13:40:21Z` `inline` by `wenscarl` `vllm/model_executor/layers/fused_moe/config.py`:466; signals: moe; excerpt: "The additional 4 scales were not present before 27223 and no issue without them. Is it possible to deduce them from others?" (https://github.com/vllm-project/vllm/pull/27255#discussion_r2490559569)
- `2025-11-04T15:31:20Z` `inline` by `amirkl94` `vllm/model_executor/layers/fused_moe/config.py`:466; signals: moe; excerpt: "As far as I could tell, no" (https://github.com/vllm-project/vllm/pull/27255#discussion_r2490986140)
- `2025-11-04T15:48:08Z` `inline` by `wenscarl` `vllm/model_executor/layers/quantization/modelopt.py`:573; signals: flashinfer; excerpt: "The g1 alphas can be computed by w1 scale and a1 scale here, right? Same in test flashinfer.py." (https://github.com/vllm-project/vllm/pull/27255#discussion_r2491049620)
- `2025-11-02T14:15:52Z` `issue` by `amirkl94`; signals: hang; excerpt: "@wenscarl This reverts a change you made in can you please take a look?" (https://github.com/vllm-project/vllm/pull/27255#issuecomment-3477998114)
- `2025-11-05T09:38:27Z` `inline` by `wenscarl` `vllm/model_executor/layers/quantization/modelopt.py`:573; signals: general review; excerpt: "Sound reasonable. Let's leave it as it is." (https://github.com/vllm-project/vllm/pull/27255#discussion_r2493698076)
