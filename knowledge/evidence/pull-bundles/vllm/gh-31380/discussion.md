# PR Discussion Digest

- Source PR: [vllm-project/vllm#31380](https://github.com/vllm-project/vllm/pull/31380)
- Source page: `sources/prs/vllm/PR-31380.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31380`
- Generated at: `2026-05-20T15:39:17.853185+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-26T07:16:31Z`
- Merged: `2026-01-09T11:28:02Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 21
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=18, outdated=12
- Human participants with discussion text: chatgpt-codex-connector, cursor, mergify, tjtanaa, vllmellm
- Automation comments/reviews omitted from high-signal summary: 16
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-26T07:20:08Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the ROCm attention kernels to support non-power-of-two block sizes, which is required ... (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3612931338)
- `2025-12-26T07:59:44Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for non-power-of-2 block sizes in ROCm attention kernels, which is crucial ... (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3612989297)
- `2025-12-27T07:18:11Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors ROCm attention kernels to support non-power-of-2 block sizes, which is required for ... (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3614168940)
- `2025-12-27T08:14:02Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3614240696)
- `2025-12-29T02:27:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces significant refactoring to the ROCm attention kernels to support non-power-of-2 block sizes, ... (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3614941921)
- `2026-01-06T05:19:41Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3629423880)
- `2026-01-08T10:27:29Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3638774149)
- `2026-01-09T01:58:00Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3642052705)
- `2026-01-09T04:06:04Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3642250360)
- `2026-01-09T04:52:35Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3642323142)
- `2026-01-09T05:04:28Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3642340315)
- `2026-01-09T11:25:31Z` `APPROVED` by `tjtanaa` - LGTM. Amazing work. Thank you so much (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3643517949)

## Inline Comment Hotspots

- `vllm/attention/ops/prefix_prefill.py`: 11 inline comment(s)
- `vllm/attention/ops/chunked_prefill_paged_decode.py`: 6 inline comment(s)
- `tests/kernels/attention/test_prefix_prefill.py`: 3 inline comment(s)
- `vllm/attention/ops/triton_reshape_and_cache_flash.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-27T08:14:02Z` `inline` by `chatgpt-codex-connector` `vllm/attention/ops/chunked_prefill_paged_decode.py`:440; signals: attention, block, cache, fp8, kernel, triton; excerpt: "while PHYSICAL BLOCK SIZE can still be 16. When the custom ROCm kernel is disabled (e.g., alibi/sliding window/FP8), a 16-token cache block is iterated ..." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2649019215)
- `2026-01-06T05:19:40Z` `inline` by `tjtanaa` `vllm/attention/ops/prefix_prefill.py`:839; signals: attention, block, hang, perf, performance; excerpt: "@vllmellm will this affect the performance? BLOCK M has been changed from 128 to 32 and BLOCK N has been changed from 64 to ..." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2663644879)
- `2026-01-09T01:58:01Z` `inline` by `cursor` `tests/kernels/attention/test_prefix_prefill.py`:112; signals: attention, block, dtype, hang, kernel; excerpt: "Function call has wrong argument order after signature change Medium Severity The test contexted kv attention f32 function calls test contexted kv attention using ..." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2674543626)
- `2026-01-09T04:52:35Z` `inline` by `cursor` `vllm/attention/ops/prefix_prefill.py`:720; signals: attention, block, kernel, memory; excerpt: "Alibi path uses raw block table when pointer-based tables enabled Medium Severity The new is block table ptr feature is incompletely implemented across two ..." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2674815632)
- `2025-12-27T08:14:02Z` `inline` by `chatgpt-codex-connector` `vllm/attention/ops/prefix_prefill.py`:827; signals: attention, block, kernel; excerpt: ", the kernel iterates start n in 32-token chunks and derives bn logical idx from start n // PHYSICAL BLOCK SIZE, which skips every ..." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2649019216)
- `2026-01-09T01:58:00Z` `inline` by `cursor` `tests/kernels/attention/test_prefix_prefill.py`:112; signals: attention, block, kernel; excerpt: "Parametrized block size is overwritten with hardcoded value High Severity The test adds block size as a parametrized parameter (with values including 544 for ..." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2674543620)
- `2026-01-08T10:27:28Z` `inline` by `vllmellm` `vllm/attention/ops/prefix_prefill.py`:839; signals: attention, block; excerpt: "Hi @tjtanaa , I have followed the advice and restored the original logic of the standard model. The new arithmetic addressing logic will only ..." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2671791535)
- `2026-01-09T04:06:04Z` `inline` by `vllmellm` `tests/kernels/attention/test_prefix_prefill.py`:112; signals: attention, kernel; excerpt: "Waiting for new code to be pushed" (https://github.com/vllm-project/vllm/pull/31380#discussion_r2674744502)
- `2025-12-27T08:14:02Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/31380#pullrequestreview-3614240696)
- `2026-01-09T05:04:27Z` `inline` by `vllmellm` `vllm/attention/ops/prefix_prefill.py`:720; signals: attention; excerpt: "Alibi is not affected by this modification and will not be processed at this time." (https://github.com/vllm-project/vllm/pull/31380#discussion_r2674833171)
- `2025-12-29T09:00:05Z` `issue` by `tjtanaa`; signals: hang; excerpt: "@vllmellm Please check, the changes are affecting the AMD CI." (https://github.com/vllm-project/vllm/pull/31380#issuecomment-3695893599)
- `2025-12-30T04:14:46Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @vllmellm." (https://github.com/vllm-project/vllm/pull/31380#issuecomment-3698262752)
