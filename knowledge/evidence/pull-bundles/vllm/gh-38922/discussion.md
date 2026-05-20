# PR Discussion Digest

- Source PR: [vllm-project/vllm#38922](https://github.com/vllm-project/vllm/pull/38922)
- Source page: `sources/prs/vllm/PR-38922.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38922`
- Generated at: `2026-05-20T15:40:38.437316+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-03T16:22:21Z`
- Merged: `2026-04-10T05:27:54Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: Isotr0py, mergify, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-03T16:25:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the DISPATCH BY KV CACHE DTYPE macro in both AMD and NVIDIA ... (https://github.com/vllm-project/vllm/pull/38922#pullrequestreview-4056340224)
- `2026-04-06T13:38:37Z` `COMMENTED` by `yewentao256` - Thanks for the work! Could we make a Enum for this? (https://github.com/vllm-project/vllm/pull/38922#pullrequestreview-4062277797)
- `2026-04-07T15:15:22Z` `COMMENTED` by `yewentao256` - The change looks good, could you add acc metrics report using lm eval for different kv cache dtype ... (https://github.com/vllm-project/vllm/pull/38922#pullrequestreview-4069221524)
- `2026-04-08T19:40:37Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/38922#pullrequestreview-4077784321)

## Inline Comment Hotspots

- `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh`: 1 inline comment(s)
- `csrc/quantization/w8a8/fp8/nvidia/quant_utils.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-07T15:15:22Z` `review` `COMMENTED` by `yewentao256`; signals: cache, dtype, hang, kv cache; excerpt: "The change looks good, could you add acc metrics report using lm eval for different kv cache dtype to make sure we won't break ..." (https://github.com/vllm-project/vllm/pull/38922#pullrequestreview-4069221524)
- `2026-04-08T16:14:17Z` `issue` by `Isotr0py`; signals: cache, dtype, kv cache; excerpt: "Seems lm-eval has issues about answer extraction for Qwen3.5, but at least the scores are consistent for different kv cache dtype. Auto Tasks Version ..." (https://github.com/vllm-project/vllm/pull/38922#issuecomment-4207734829)
- `2026-04-06T13:38:37Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Thanks for the work! Could we make a Enum for this?" (https://github.com/vllm-project/vllm/pull/38922#pullrequestreview-4062277797)
- `2026-04-09T16:01:03Z` `issue` by `mergify`; signals: general review; excerpt: "Deprecation notice: This pull request comes from a fork and was rebased using bot account impersonation. This capability will be removed on July 1, ..." (https://github.com/vllm-project/vllm/pull/38922#issuecomment-4215646290)
