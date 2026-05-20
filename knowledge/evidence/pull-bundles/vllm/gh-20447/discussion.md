# PR Discussion Digest

- Source PR: [vllm-project/vllm#20447](https://github.com/vllm-project/vllm/pull/20447)
- Source page: `sources/prs/vllm/PR-20447.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20447`
- Generated at: `2026-05-20T15:36:06.819952+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-03T17:32:15Z`
- Merged: `2025-07-22T14:27:12Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 12 (approved=2, changes_requested=1, commented=9)
- Inline review comments: 12
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=3, outdated=5
- Human participants with discussion text: LucasWilkinson, djmmoss, jiahanc, mergify, mgoin, shixianc, yewentao256
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-03T17:32:47Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @djmmoss, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2984040257)
- `2025-07-03T17:34:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for SM100 (Blackwell) architecture for CUTLASS grouped GEMM operations, which is ... (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2984049384)
- `2025-07-03T18:35:53Z` `COMMENTED` by `yewentao256` - Thanks for the work! Could you also add some benchmark comparison with Triton? (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2984262155)
- `2025-07-03T19:56:20Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2984498550)
- `2025-07-07T17:49:32Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2994827382)
- `2025-07-07T17:51:01Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2994831924)
- `2025-07-07T20:41:15Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2995224510)
- `2025-07-08T17:10:08Z` `CHANGES_REQUESTED` by `mgoin` - we are planning to add the tuned configs to this PR, please hold off on merging until they ... (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2998477671)
- `2025-07-08T19:59:48Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2998952035)
- `2025-07-18T18:13:20Z` `APPROVED` by `mgoin` - LGTM nice work, just one request for documentation (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-3034397964)
- `2025-07-18T19:07:35Z` `COMMENTED` by `jiahanc` (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-3034585500)
- `2025-07-18T21:24:04Z` `APPROVED` by `mgoin` - LGTM, thank you for the support! (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-3034855584)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`: 1 inline comment(s)
- `csrc/quantization/cutlass_w8a8/moe/grouped_mm_c3x_sm100.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-17T05:19:33Z` `issue` by `jiahanc`; signals: benchmark, cuda, gemm, kernel, moe, perf, triton; excerpt: "Kernel perf benchmark Model Configuration triton moe triton moe cuda graphs grouped gemm moe grouped gemm moe cuda graphs --------------------- ---------- ---------- ---------- ---------- ..." (https://github.com/vllm-project/vllm/pull/20447#issuecomment-3082567551)
- `2025-07-17T05:24:14Z` `issue` by `jiahanc`; signals: cutlass, gemm, kernel, latency, moe, perf, triton; excerpt: "@mgoin the PR is read to go. The cutlass perf has been tuned. We implemented a fallback logic to triton MOE in small batch ..." (https://github.com/vllm-project/vllm/pull/20447#issuecomment-3082575585)
- `2025-07-04T00:03:20Z` `issue` by `mgoin`; signals: benchmark, kernel, perf, performance, triton; excerpt: "Could you also add some benchmark comparison with Triton? Since there are no tuned configs in this PR, I expect this will give poor ..." (https://github.com/vllm-project/vllm/pull/20447#issuecomment-3033974234)
- `2025-07-03T18:34:51Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:87; signals: fp8, moe, sm100, sm90; excerpt: "In this case we don't need to have complicated logic in is fp8 w8a8 sm90 or sm100, and may be better for the future ..." (https://github.com/vllm-project/vllm/pull/20447#discussion_r2183496374)
- `2025-07-03T18:33:55Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:87; signals: fp8, moe, sm100, sm90; excerpt: "Could this be divided to is fp8 w8a8 sm90 and is fp8 w8a8 sm100 two branchs?" (https://github.com/vllm-project/vllm/pull/20447#discussion_r2183494749)
- `2025-07-03T18:35:53Z` `review` `COMMENTED` by `yewentao256`; signals: benchmark, triton; excerpt: "Thanks for the work! Could you also add some benchmark comparison with Triton?" (https://github.com/vllm-project/vllm/pull/20447#pullrequestreview-2984262155)
- `2025-07-07T17:49:32Z` `inline` by `LucasWilkinson` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:158; signals: cuda, cutlass; excerpt: "nit: can we just move this above if (cuda device capability = 90) so we dont have to add fall through cases as newer ..." (https://github.com/vllm-project/vllm/pull/20447#discussion_r2190721195)
- `2025-07-18T19:07:35Z` `inline` by `jiahanc` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:957; signals: moe, sm100; excerpt: "done and also fix the fallback logic only on SM100" (https://github.com/vllm-project/vllm/pull/20447#discussion_r2216754539)
- `2025-07-17T18:31:32Z` `issue` by `shixianc`; signals: hang, moe; excerpt: "@jiahanc I made a swap ab change last week the current implementation looks exactly the same especially on handing the problem sizes in moe ..." (https://github.com/vllm-project/vllm/pull/20447#issuecomment-3085041884)
- `2025-07-17T18:47:40Z` `issue` by `jiahanc`; signals: hang, moe; excerpt: "@jiahanc I made a swap ab change last week the current implementation looks exactly the same especially on handing the problem sizes in moe ..." (https://github.com/vllm-project/vllm/pull/20447#issuecomment-3085081280)
- `2025-07-03T19:56:20Z` `inline` by `djmmoss` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:87; signals: moe; excerpt: "fixed 👍" (https://github.com/vllm-project/vllm/pull/20447#discussion_r2183654145)
- `2025-07-07T17:51:00Z` `inline` by `LucasWilkinson` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:257; signals: cutlass; excerpt: "@djmmoss I think Gemini is actually correct here; we should also add runtime switches" (https://github.com/vllm-project/vllm/pull/20447#discussion_r2190723841)
