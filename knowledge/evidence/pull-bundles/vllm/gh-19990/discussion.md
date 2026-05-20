# PR Discussion Digest

- Source PR: [vllm-project/vllm#19990](https://github.com/vllm-project/vllm/pull/19990)
- Source page: `sources/prs/vllm/PR-19990.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19990`
- Generated at: `2026-05-20T15:35:40.277121+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-23T16:22:00Z`
- Merged: `2025-06-29T22:05:41Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 9
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=7
- Human participants with discussion text: dsikka, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-23T16:22:28Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @dsikka, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/19990#pullrequestreview-2950717384)
- `2025-06-23T16:23:46Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request adds support for MoE models with nvfp4 compressed tensors. The changes include modifications ... (https://github.com/vllm-project/vllm/pull/19990#pullrequestreview-2950720522)
- `2025-06-25T18:27:21Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/19990#pullrequestreview-2959208543)
- `2025-06-26T13:54:51Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/19990#pullrequestreview-2962226640)
- `2025-06-26T16:54:56Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/19990#pullrequestreview-2962793484)
- `2025-06-26T16:57:40Z` `APPROVED` by `mgoin` - Thanks! We can followup with the automated testing (https://github.com/vllm-project/vllm/pull/19990#pullrequestreview-2962800341)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-06-25T18:25:52Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:333; signals: fp4, moe, nvfp4; excerpt: "These should still be enforced for fused marlin moe. Also update the mention of ModelOptNvFp4FusedMoE" (https://github.com/vllm-project/vllm/pull/19990#discussion_r2167344659)
- `2025-06-27T20:08:47Z` `issue` by `mgoin`; signals: b200, h100; excerpt: "Validated on B200 and H100 (for marlin) Command: B200: H100:" (https://github.com/vllm-project/vllm/pull/19990#issuecomment-3014246943)
- `2025-06-25T18:23:43Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:281; signals: moe; excerpt: "I think it is more clear to invert this and early exit for marlin" (https://github.com/vllm-project/vllm/pull/19990#discussion_r2167341089)
- `2025-06-25T18:27:14Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:256; signals: moe; excerpt: "Should we worry about deleting the original scales?" (https://github.com/vllm-project/vllm/pull/19990#discussion_r2167347053)
- `2025-06-26T13:54:51Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:333; signals: moe; excerpt: "Should they have been enforced in the ModelOpt integration?" (https://github.com/vllm-project/vllm/pull/19990#discussion_r2169137267)
- `2025-06-26T16:54:55Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:333; signals: moe; excerpt: "Yes, definitely there as well" (https://github.com/vllm-project/vllm/pull/19990#discussion_r2169492849)
- `2025-06-26T14:01:23Z` `issue` by `dsikka`; signals: moe; excerpt: "@mgoin I would like to add a test but I am mindful of the test time for MoEs being added to the quantization tests ..." (https://github.com/vllm-project/vllm/pull/19990#issuecomment-3008610666)
- `2025-06-25T19:16:14Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @dsikka." (https://github.com/vllm-project/vllm/pull/19990#issuecomment-3005873482)
