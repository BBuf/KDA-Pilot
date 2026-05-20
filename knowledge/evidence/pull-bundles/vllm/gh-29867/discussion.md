# PR Discussion Digest

- Source PR: [vllm-project/vllm#29867](https://github.com/vllm-project/vllm/pull/29867)
- Source page: `sources/prs/vllm/PR-29867.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29867`
- Generated at: `2026-05-20T15:38:49.169147+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-02T11:00:13Z`
- Merged: `2026-01-13T12:56:01Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 13 (approved=2, commented=11)
- Inline review comments: 11
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=3, outdated=6
- Human participants with discussion text: LucasWilkinson, chatgpt-codex-connector, cursor, mergify, mgoin, mickaelseznec, robertgshaw2-redhat, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-02T11:03:58Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3529511808)
- `2025-12-02T11:08:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a potential overflow issue when dequantizing FP8 static weights by introducing a ... (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3529527887)
- `2025-12-02T14:11:57Z` `COMMENTED` by `tlrmchlsmth` - I think there are edge cases where this approach won't work, e.g. if m and n aren't divisible ... (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3530348609)
- `2025-12-02T15:14:28Z` `COMMENTED` by `LucasWilkinson` - nit: can we use dequant weights = scaled dequantize(weight, weight scale, out type=act dtype) from vllm/model executor/layers/quantization/utils/quant utils.py ... (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3530674051)
- `2025-12-02T18:45:18Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3531661574)
- `2025-12-02T18:49:56Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3531676374)
- `2026-01-09T09:28:55Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3643103774)
- `2026-01-09T10:57:44Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3643432198)
- `2026-01-09T16:25:30Z` `APPROVED` by `mgoin` - LGTM, just a typo nit (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3644670674)
- `2026-01-09T16:35:03Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3644706872)
- `2026-01-09T16:35:34Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3644708673)
- `2026-01-09T16:40:48Z` `APPROVED` by `tlrmchlsmth` - left a suggestion, but think it should be a followup (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3644729107)
- `2026-01-13T11:27:08Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3655291235)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/quant_utils.py`: 6 inline comment(s)
- `vllm/v1/attention/backends/mla/common.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-12-02T18:45:18Z` `inline` by `tlrmchlsmth` `vllm/v1/attention/backends/mla/common.py`:1162; signals: attention, block, gemm, hang, mla; excerpt: "We should still call get and maybe dequant weights here. Inside of get and maybe dequant weights, we should selectively use scaled dequantize only ..." (https://github.com/vllm-project/vllm/pull/29867#discussion_r2582426025)
- `2025-12-02T11:03:58Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/mla/common.py`:1568; signals: attention, fp8, mla, overflow; excerpt: "still uses the old eye path. Backends such as FlashMLASparseImpl and ROCMAiterMLASparseImpl inherit directly from MLACommonBaseImpl, so static FP8 weights there will continue to ..." (https://github.com/vllm-project/vllm/pull/29867#discussion_r2580692715)
- `2026-01-09T16:35:02Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/quantization/utils/quant_utils.py`:315; signals: dtype, layout, overflow; excerpt: "What if we do something like this: ``` def get and maybe dequant weights( layer: "LinearBase", out dtype: torch.dtype = torch.float32 ): """Return layer's ..." (https://github.com/vllm-project/vllm/pull/29867#discussion_r2676851826)
- `2025-12-02T18:49:56Z` `inline` by `tlrmchlsmth` `vllm/v1/attention/backends/mla/common.py`:1162; signals: attention, mla; excerpt: "My suggestion here is a short-term fix (Good for getting 0.12.0 out the door), but we should follow-up with something better. Perhaps it's time ..." (https://github.com/vllm-project/vllm/pull/29867#discussion_r2582438354)
- `2026-01-09T09:28:55Z` `inline` by `cursor` `vllm/model_executor/layers/quantization/utils/quant_utils.py`:315; signals: fp8, kernel; excerpt: "Marlin FP8 weights incorrectly dequantized with scaled dequantize High Severity When get and maybe dequant weights is called for an FP8 layer that uses ..." (https://github.com/vllm-project/vllm/pull/29867#discussion_r2675464400)
- `2025-12-02T15:14:28Z` `review` `COMMENTED` by `LucasWilkinson`; signals: dtype; excerpt: "nit: can we use dequant weights = scaled dequantize(weight, weight scale, out type=act dtype) from vllm/model executor/layers/quantization/utils/quant utils.py (feel free to update that to ..." (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3530674051)
- `2026-01-09T10:57:44Z` `inline` by `cursor` `vllm/model_executor/layers/quantization/utils/quant_utils.py`:284; signals: fp8; excerpt: "Incorrect attribute access: layer.use marlin instead of layer.quant method.use marlin High Severity The code accesses layer.use marlin but the use marlin attribute is defined ..." (https://github.com/vllm-project/vllm/pull/29867#discussion_r2675746864)
- `2026-01-13T11:27:09Z` `inline` by `cursor` `vllm/model_executor/layers/quantization/utils/quant_utils.py`:315; signals: fp8; excerpt: "FP8 dequantization fails for 1D scale tensors Medium Severity The new get and maybe dequant weights function calls scaled dequantize with group shape=None for ..." (https://github.com/vllm-project/vllm/pull/29867#discussion_r2685989496)
- `2025-12-02T11:03:58Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3529511808)
- `2025-12-02T14:11:57Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: general review; excerpt: "I think there are edge cases where this approach won't work, e.g. if m and n aren't divisible by m scale and n scale. ..." (https://github.com/vllm-project/vllm/pull/29867#pullrequestreview-3530348609)
- `2026-01-09T16:35:34Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/quantization/utils/quant_utils.py`:315; signals: general review; excerpt: "Basically, if there's a dequant method, use it and otherwise we can fall back to the N^3 eye method" (https://github.com/vllm-project/vllm/pull/29867#discussion_r2676853431)
- `2025-12-02T16:45:53Z` `issue` by `mickaelseznec`; signals: general review; excerpt: "@tlrmchlsmth @LucasWilkinson Thanks for the review! Updated according to your comments, tested locally on DSv3 as well. Let me know what you think :)" (https://github.com/vllm-project/vllm/pull/29867#issuecomment-3602997761)
