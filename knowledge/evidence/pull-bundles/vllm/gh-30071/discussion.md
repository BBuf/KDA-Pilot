# PR Discussion Digest

- Source PR: [vllm-project/vllm#30071](https://github.com/vllm-project/vllm/pull/30071)
- Source page: `sources/prs/vllm/PR-30071.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-30071`
- Generated at: `2026-05-20T15:38:53.429096+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-04T17:08:36Z`
- Merged: `2025-12-18T04:20:42Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: BowenBao, LucasWilkinson, chatgpt-codex-connector, mergify, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-04T17:11:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for int4-fp8 w4a8 quantization for Mixture of Experts (MoE) layers using ... (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3541107898)
- `2025-12-04T23:19:34Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3542525996)
- `2025-12-04T23:50:24Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3542579503)
- `2025-12-06T14:46:36Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3547724949)
- `2025-12-11T16:41:12Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3568350935)
- `2025-12-17T13:02:05Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3587644604)
- `2025-12-17T13:02:19Z` `APPROVED` by `tjtanaa` - LGTM. Just one part about the type hinting seems offed. (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3587645551)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/quark/quark_moe.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-12-04T23:19:34Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:524; signals: dtype, fp8, kernel, moe; excerpt: ", but get fused moe quant config still builds an fp8 w8a8 moe quant config (lines 536‑540). That quant config tags the weights as ..." (https://github.com/vllm-project/vllm/pull/30071#discussion_r2590916546)
- `2025-12-11T16:41:12Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:524; signals: kernel, moe; excerpt: "hi @tjtanaa, the current AITER commit supports this, it does not require new AITER commit, because the kernel is actually not new. The quantized ..." (https://github.com/vllm-project/vllm/pull/30071#discussion_r2611305152)
- `2025-12-04T23:50:24Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:524; signals: kernel, moe; excerpt: "this is handled by the kernel" (https://github.com/vllm-project/vllm/pull/30071#discussion_r2590962988)
- `2025-12-17T13:11:19Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @BowenBao, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/30071#issuecomment-3665292121)
- `2025-12-17T22:06:45Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @BowenBao, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/30071#issuecomment-3667397066)
- `2025-12-06T14:46:36Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:524; signals: moe; excerpt: "@BowenBao May I know which AITER commits is required to support this feature? Does the AITER commit used in the docker/Dockerfile.rocm base support this? ..." (https://github.com/vllm-project/vllm/pull/30071#discussion_r2594973649)
- `2025-12-04T23:19:34Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/30071#pullrequestreview-3542525996)
- `2025-12-17T13:02:05Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:545; signals: moe; excerpt: "@BowenBao NITS: I think should this be layer: FusedMoE like the other class." (https://github.com/vllm-project/vllm/pull/30071#discussion_r2626988129)
