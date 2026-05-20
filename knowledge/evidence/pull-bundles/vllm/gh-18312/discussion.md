# PR Discussion Digest

- Source PR: [vllm-project/vllm#18312](https://github.com/vllm-project/vllm/pull/18312)
- Source page: `sources/prs/vllm/PR-18312.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-18312`
- Generated at: `2026-05-20T15:35:18.360620+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-17T23:02:37Z`
- Merged: `2025-06-08T13:05:55Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: DarkLight1337, PhzCode, codelayout, dsikka, mgoin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-05-18T00:29:55Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/18312#pullrequestreview-2848492274)
- `2025-05-18T00:41:02Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/18312#pullrequestreview-2848538428)
- `2025-05-21T19:10:53Z` `APPROVED` by `mgoin` - Okay LGTM to land emulation and coalesce with marlin later (https://github.com/vllm-project/vllm/pull/18312#pullrequestreview-2858851109)
- `2025-06-06T15:48:03Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/18312#pullrequestreview-2905331545)
- `2025-06-06T17:38:51Z` `APPROVED` by `mgoin` - LGTM, thanks! Will follow up with Marlin integration (https://github.com/vllm-project/vllm/pull/18312#pullrequestreview-2905608336)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-05-19T23:41:00Z` `issue` by `mgoin`; signals: fp8, kernel; excerpt: "I still want the default behavior to run w4a4 as w4a16 on hardware where we can support the Marlin kernel, so users have the ..." (https://github.com/vllm-project/vllm/pull/18312#issuecomment-2892518207)
- `2025-05-20T00:30:08Z` `issue` by `dsikka`; signals: fp8, kernel; excerpt: "I still want the default behavior to run w4a4 as w4a16 on hardware where we can support the Marlin kernel, so users have the ..." (https://github.com/vllm-project/vllm/pull/18312#issuecomment-2892574047)
- `2025-06-06T15:48:03Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:237; signals: fp4; excerpt: "I want to get baseline support in with this PR. I will do this in a follow-up when I combine the two fp4 schemes" (https://github.com/vllm-project/vllm/pull/18312#discussion_r2132440237)
- `2025-05-21T19:10:53Z` `review` `APPROVED` by `mgoin`; signals: coalesc; excerpt: "Okay LGTM to land emulation and coalesce with marlin later" (https://github.com/vllm-project/vllm/pull/18312#pullrequestreview-2858851109)
- `2025-05-18T00:28:44Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:235; signals: general review; excerpt: "Extra value here" (https://github.com/vllm-project/vllm/pull/18312#discussion_r2094258989)
- `2025-05-18T00:29:02Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:226; signals: general review; excerpt: "Should the input be group quant as well?" (https://github.com/vllm-project/vllm/pull/18312#discussion_r2094259473)
- `2025-05-18T00:29:22Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:237; signals: general review; excerpt: "We should check for dynamic input as well" (https://github.com/vllm-project/vllm/pull/18312#discussion_r2094260884)
- `2025-05-18T00:41:02Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:226; signals: general review; excerpt: "Technically a new strategy - “tensor group”" (https://github.com/vllm-project/vllm/pull/18312#discussion_r2094285402)
- `2025-05-23T16:54:07Z` `issue` by `dsikka`; signals: general review; excerpt: "Progress has gone fast enough that we can wait for the next ct release next week. Converting to draft until then" (https://github.com/vllm-project/vllm/pull/18312#issuecomment-2905114846)
