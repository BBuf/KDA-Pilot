# PR Discussion Digest

- Source PR: [vllm-project/vllm#14578](https://github.com/vllm-project/vllm/pull/14578)
- Source page: `sources/prs/vllm/PR-14578.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14578`
- Generated at: `2026-05-20T15:34:28.845625+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-10T21:15:20Z`
- Merged: `2025-03-28T02:58:16Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 10
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: ProExpertProg, gshtras, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-12T22:09:49Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2679983150)
- `2025-03-12T22:24:24Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2680006486)
- `2025-03-18T22:34:14Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2696462685)
- `2025-03-18T22:35:01Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2696463614)
- `2025-03-20T16:27:56Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2703403322)
- `2025-03-20T18:23:17Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2703709176)
- `2025-03-21T20:55:31Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2707242753)
- `2025-03-24T20:41:14Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2711631446)
- `2025-03-24T20:57:09Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2711663044)
- `2025-03-24T21:14:07Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2711695400)
- `2025-03-28T01:20:48Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/14578#pullrequestreview-2724040817)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-03-20T16:27:55Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`:26; signals: dtype, fp8, throughput; excerpt: "@ProExpertProg - are you use this is okay? I know that throughput the models, we pipe the dtype through." (https://github.com/vllm-project/vllm/pull/14578#discussion_r2006029071)
- `2025-03-24T20:41:14Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`:26; signals: attention, dtype, fp8; excerpt: "I looked and we use the default dtype in many places (attention, RMSNorm, etc.). So I think this is fine @robertgshaw2-redhat" (https://github.com/vllm-project/vllm/pull/14578#discussion_r2010896007)
- `2025-03-12T22:24:24Z` `inline` by `gshtras` `vllm/model_executor/layers/quantization/fp8.py`:119; signals: fp8, hang; excerpt: "For models with additional scales such as amd/Llama-3.1-8B-Instruct-FP8-QKV-Proj Been broken since this change" (https://github.com/vllm-project/vllm/pull/14578#discussion_r1992378497)
- `2025-03-20T18:23:16Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`:26; signals: dtype, fp8; excerpt: "I didn't know we did that - I thought it the default dtype was used for unquantized" (https://github.com/vllm-project/vllm/pull/14578#discussion_r2006215711)
- `2025-03-21T20:55:31Z` `inline` by `gshtras` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`:26; signals: dtype, fp8; excerpt: "That's the unquantized dtype by design here, to do fp8 x fp8 - half instead of half x fp8 - half" (https://github.com/vllm-project/vllm/pull/14578#discussion_r2008319770)
- `2025-03-12T22:08:25Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`:183; signals: cutlass; excerpt: "Either add an assert here or use the same logic as the non-cutlass case" (https://github.com/vllm-project/vllm/pull/14578#discussion_r1992363861)
- `2025-03-12T22:09:35Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/fp8.py`:119; signals: fp8; excerpt: "Where is this method used?" (https://github.com/vllm-project/vllm/pull/14578#discussion_r1992364901)
- `2025-03-18T22:35:01Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/fp8.py`:119; signals: fp8; excerpt: "Could we add a test for this? Or does it already exist in CI" (https://github.com/vllm-project/vllm/pull/14578#discussion_r2002119601)
- `2025-03-24T20:57:09Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`:182; signals: general review; excerpt: "Just want to make it clear this isn't an inherent limitation:" (https://github.com/vllm-project/vllm/pull/14578#discussion_r2010915537)
- `2025-03-24T21:14:07Z` `inline` by `gshtras` `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`:182; signals: general review; excerpt: "Sorry about the force push, accepting suggestions from the github UI breaks DCO..." (https://github.com/vllm-project/vllm/pull/14578#discussion_r2010935545)
