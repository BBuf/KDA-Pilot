# PR Discussion Digest

- Source PR: [vllm-project/vllm#28878](https://github.com/vllm-project/vllm/pull/28878)
- Source page: `sources/prs/vllm/PR-28878.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28878`
- Generated at: `2026-05-20T15:38:35.358910+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-17T20:25:28Z`
- Merged: `2025-11-27T02:35:13Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 15 (approved=4, commented=11)
- Inline review comments: 14
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=5, outdated=2
- Human participants with discussion text: HDCharles, chatgpt-codex-connector, dsikka, heheda12345, kylesayrs, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-11-17T20:28:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug where models with partially quantized Mixture-of-Experts (MoE) layers would fail ... (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3474448442)
- `2025-11-17T20:28:52Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3474450623)
- `2025-11-18T01:51:47Z` `COMMENTED` by `HDCharles` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3475179104)
- `2025-11-18T02:06:12Z` `COMMENTED` by `HDCharles` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3475199236)
- `2025-11-18T02:29:52Z` `COMMENTED` by `HDCharles` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3475236500)
- `2025-11-19T17:00:52Z` `APPROVED` by `kylesayrs` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3483842730)
- `2025-11-19T17:16:30Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3479739336)
- `2025-11-19T17:31:15Z` `COMMENTED` by `HDCharles` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3483966095)
- `2025-11-19T17:36:41Z` `COMMENTED` by `HDCharles` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3483984822)
- `2025-11-19T18:18:03Z` `COMMENTED` by `HDCharles` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3484137291)
- `2025-11-20T20:58:39Z` `COMMENTED` by `HDCharles` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3489908258)
- `2025-11-20T21:49:54Z` `APPROVED` by `kylesayrs` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3490077163)
- `2025-11-20T23:38:36Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3490542067)
- `2025-11-27T01:55:56Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3513299351)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`: 4 inline comment(s)
- `tests/quantization/test_compressed_tensors.py`: 3 inline comment(s)
- `.buildkite/test-pipeline.yaml`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-18T02:29:52Z` `inline` by `HDCharles` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:121; signals: moe; excerpt: "this functionally is the same as previously where we matched based on hardcoded regex to the first layer. In practice the layers are normally ..." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2536098843)
- `2025-11-19T17:15:56Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:121; signals: moe; excerpt: "I don't understand the purpose of .0 here? Are we making an assumption of just looking at the first moe layer to define the ..." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2542914628)
- `2025-11-19T17:31:15Z` `inline` by `HDCharles` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:121; signals: moe; excerpt: "yeah that wouldn't be an issue since this is indexing experts, not layers. e.g. for model.layers.0.mlp.experts.(0.down proj).weight << we only try to match for ..." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2542963477)
- `2025-11-19T17:36:41Z` `inline` by `HDCharles` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:176; signals: moe; excerpt: "This isn't doing the filtering/matching, its just adding FusedMoE to the target scheme map as an option. i.e. before {"Linear": , " ": } ..." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2542977797)
- `2025-11-19T18:18:03Z` `inline` by `HDCharles` `tests/quantization/test_compressed_tensors.py`:787; signals: moe; excerpt: "yeah i'll make a fake model for this, i don't think there's an actual MoE that's smaler than this one." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2543095682)
- `2025-11-17T20:28:52Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28878#pullrequestreview-3474450623)
- `2025-11-18T01:51:47Z` `inline` by `HDCharles` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:126; signals: moe; excerpt: "this logic is the same as before just explicated." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2536048049)
- `2025-11-19T17:14:59Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:176; signals: moe; excerpt: "Shouldn't this be doing the filtering by looking for layer ignores that might disqualify FusedMoE?" (https://github.com/vllm-project/vllm/pull/28878#discussion_r2542911733)
- `2025-11-27T01:55:50Z` `inline` by `mgoin` `.buildkite/test-pipeline.yaml`:635; signals: pipeline; excerpt: "Why is this needed now if we didn't need this before? Is it needed for the new model somehow?" (https://github.com/vllm-project/vllm/pull/28878#discussion_r2566943562)
- `2025-11-21T03:12:00Z` `issue` by `dsikka`; signals: dtype; excerpt: "FYI - failure is because config was generated using a newer ct nightly whereas ct 12.2 is used by vLLM. We should use 12.2 ..." (https://github.com/vllm-project/vllm/pull/28878#issuecomment-3561134653)
- `2025-11-17T20:28:52Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`:699; signals: general review; excerpt: "will return None, causing callers to fall back to UnquantizedLinearMethod and silently drop sparsity acceleration. Useful? React with 👍 / 👎." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2535425395)
- `2025-11-18T20:58:47Z` `inline` by `mgoin` `tests/quantization/test_compressed_tensors.py`:787; signals: general review; excerpt: "This is a big model for CI and we don't actually need to load real weights here. Can you make this for a <1B ..." (https://github.com/vllm-project/vllm/pull/28878#discussion_r2539677166)
