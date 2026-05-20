# PR Discussion Digest

- Source PR: [vllm-project/vllm#38815](https://github.com/vllm-project/vllm/pull/38815)
- Source page: `sources/prs/vllm/PR-38815.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38815`
- Generated at: `2026-05-20T15:40:36.912559+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T14:41:23Z`
- Merged: `2026-04-11T23:21:36Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 16 (approved=2, commented=12, dismissed=2)
- Inline review comments: 18
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=8, outdated=7
- Human participants with discussion text: EdalatiAli, dsikka, mergify, mgoin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-02T14:46:20Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for MXFP8 (W8A8) quantization within the compressed-tensors framework, adding a new ... (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4051180730)
- `2026-04-02T21:29:19Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4053312508)
- `2026-04-02T21:57:07Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4053411221)
- `2026-04-02T22:01:29Z` `DISMISSED` by `robertgshaw2-redhat` - waiting for @dsikka and @kylesayrs (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4053424203)
- `2026-04-07T17:04:05Z` `DISMISSED` by `dsikka` - Overall LGTM. Some small nits and we should not skip the test for sm < 100 (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4069883586)
- `2026-04-07T18:51:57Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4070528352)
- `2026-04-07T18:52:12Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4070529640)
- `2026-04-07T18:52:17Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4070529979)
- `2026-04-07T18:52:22Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4070530410)
- `2026-04-07T18:52:31Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4070531108)
- `2026-04-07T18:54:59Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4070542943)
- `2026-04-09T02:16:45Z` `COMMENTED` by `mgoin` - LGTM, just concern about the test model (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4079346296)
- `2026-04-09T18:30:49Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4084602369)
- `2026-04-11T00:52:32Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4093015411)
- `2026-04-11T21:58:33Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4094275857)
- `2026-04-11T23:20:32Z` `APPROVED` by `mgoin` - LGTM, thanks Ali! (https://github.com/vllm-project/vllm/pull/38815#pullrequestreview-4094333921)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`: 10 inline comment(s)
- `tests/quantization/test_compressed_tensors.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-02T21:29:19Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:512; signals: fp8, moe; excerpt: "This method is not called during the forward pass of CompressedTensorsW8A8Mxfp8MoEMethod because [this condition]( is True." (https://github.com/vllm-project/vllm/pull/38815#discussion_r3030466955)
- `2026-04-07T17:00:02Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:62; signals: dtype, fp8; excerpt: "use MXFP8 VALUE DTYPE" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3046629733)
- `2026-04-07T17:00:48Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:74; signals: dtype, fp8; excerpt: "nit: use MXFP8 SCALE DTYPE" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3046633613)
- `2026-04-07T18:52:12Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:41; signals: fp8, hang; excerpt: "changed to 75" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3047200748)
- `2026-04-11T00:52:28Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:38; signals: fp8, hang; excerpt: "I landed a refactor in so you'll need to merge with main and change this" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3067265246)
- `2026-04-11T21:58:33Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:38; signals: fp8, kernel; excerpt: "I updated the kernel selection logic accordingly." (https://github.com/vllm-project/vllm/pull/38815#discussion_r3068650236)
- `2026-04-11T20:52:06Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @EdalatiAli, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/38815#issuecomment-4230161028)
- `2026-04-07T18:54:59Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:426; signals: fp8; excerpt: "The current format follows the other checks format like is fp8 w4a8 and is fp8 w8a16. Do you still suggest returning the asserts?" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3047214369)
- `2026-04-07T16:59:26Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:36; signals: fp8; excerpt: "nit: just use the constant directly" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3046626259)
- `2026-04-07T16:59:41Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:41; signals: fp8; excerpt: "Shouldn't marlin be 75?" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3046627761)
- `2026-04-07T17:02:38Z` `inline` by `dsikka` `tests/quantization/test_compressed_tensors.py`:640; signals: blackwell; excerpt: "We can just fall back on marlin if not on blackwell. We should update this condition" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3046642052)
- `2026-04-07T18:51:57Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`:36; signals: fp8; excerpt: "Done" (https://github.com/vllm-project/vllm/pull/38815#discussion_r3047199483)
