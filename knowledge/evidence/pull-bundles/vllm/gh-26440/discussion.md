# PR Discussion Digest

- Source PR: [vllm-project/vllm#26440](https://github.com/vllm-project/vllm/pull/26440)
- Source page: `sources/prs/vllm/PR-26440.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26440`
- Generated at: `2026-05-20T15:38:06.395264+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-08T19:46:58Z`
- Merged: `2025-10-21T21:38:29Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 21 (approved=1, commented=20)
- Inline review comments: 27
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=1, outdated=8
- Human participants with discussion text: LucasWilkinson, ZJY0516, alexm-redhat, chatgpt-codex-connector, mergify, mgoin, nvpohanh, pavanimajety, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 8

## Review Decisions

- `2025-10-08T19:49:01Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3316286613)
- `2025-10-08T19:50:18Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a performance optimization by executing the shared experts computation on a separate ... (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3316292777)
- `2025-10-20T20:22:04Z` `APPROVED` by `LucasWilkinson` - Nice optimization! Overall looks pretty good to me assuming DBO works; left a few comments (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3357776986)
- `2025-10-20T20:28:17Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3357817991)
- `2025-10-21T06:58:19Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3359002022)
- `2025-10-21T14:12:16Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361031075)
- `2025-10-21T15:53:36Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361505242)
- `2025-10-21T15:55:32Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361513433)
- `2025-10-21T15:56:47Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361519937)
- `2025-10-21T15:58:18Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361528008)
- `2025-10-21T15:59:09Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361532207)
- `2025-10-21T16:01:16Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361543562)
- `2025-10-21T17:12:57Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361848286)
- `2025-10-21T17:24:22Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361891839)
- `2025-10-21T17:24:47Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3361893739)
- `2025-10-21T17:55:36Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3362018495)
- `2025-10-21T17:59:53Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3362037313)
- `2025-10-21T19:39:58Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/26440#pullrequestreview-3362451051)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 22 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 4 inline comment(s)
- `vllm/model_executor/layers/shared_fused_moe/shared_fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-21T16:01:16Z` `inline` by `alexm-redhat` `vllm/model_executor/models/deepseek_v2.py`:268; signals: cuda, hang, moe, perf; excerpt: "It is a bit complicated, since there are 2 improvements: (1) the use of the cuda stream for shared experts and (2) the moving ..." (https://github.com/vllm-project/vllm/pull/26440#discussion_r2448881286)
- `2025-10-08T19:49:01Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/layer.py`:2235; signals: block, cute, moe; excerpt: "and discards the router logits argument. FusedMoE does not define a gate module by default (the base property returns None), and most existing callers ..." (https://github.com/vllm-project/vllm/pull/26440#discussion_r2414870325)
- `2025-10-20T20:16:30Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:2383; signals: compile, moe, perf; excerpt: "do we know if moving this out of the torch.compile region affects perf if we are not using multi-stream?" (https://github.com/vllm-project/vllm/pull/26440#discussion_r2446019184)
- `2025-10-08T19:49:01Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/shared_fused_moe/shared_fused_moe.py`:41; signals: hang, moe; excerpt: "pass this parameter. Instantiating those models will now raise a TypeError at import time because the additional positional argument has no default. Unless every ..." (https://github.com/vllm-project/vllm/pull/26440#discussion_r2414870331)
- `2025-10-20T20:13:50Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:2399; signals: cuda, moe; excerpt: "nit: could we fuse this and with torch.cuda.stream(self.shared experts stream): into a context manager; maybe something like with maybe stream(self.shared experts stream):" (https://github.com/vllm-project/vllm/pull/26440#discussion_r2446011865)
- `2025-10-21T15:53:35Z` `inline` by `alexm-redhat` `vllm/model_executor/layers/fused_moe/layer.py`:2399; signals: cuda, moe; excerpt: "This is a bit tricky since the codepaths are not identical for cuda-stream or non-cuda-stream. Maybe we can look into this later if the ..." (https://github.com/vllm-project/vllm/pull/26440#discussion_r2448852381)
- `2025-10-21T15:55:32Z` `inline` by `alexm-redhat` `vllm/model_executor/layers/fused_moe/layer.py`:2383; signals: compile, moe; excerpt: "This won't run when multi-stream is disabled. As I understand, gate is always inside a torch compiled region, no?" (https://github.com/vllm-project/vllm/pull/26440#discussion_r2448857580)
- `2025-10-20T20:25:18Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:1091; signals: hang, moe; excerpt: "Change the var from None by default to False and just do a regular bool check" (https://github.com/vllm-project/vllm/pull/26440#discussion_r2446039949)
- `2025-10-21T15:58:18Z` `inline` by `alexm-redhat` `vllm/model_executor/layers/fused_moe/layer.py`:2228; signals: hang, moe; excerpt: "Changed" (https://github.com/vllm-project/vllm/pull/26440#discussion_r2448868695)
- `2025-10-13T20:30:01Z` `issue` by `chatgpt-codex-connector`; signals: cuda, moe; excerpt: "💡 Codex Review whenever self.experts is a SharedFusedMoE, but FusedMoE.forward native (the GPU path used by super().forward) still expects router logits to already contain ..." (https://github.com/vllm-project/vllm/pull/26440#issuecomment-3398964224)
- `2025-10-20T20:18:53Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:2358; signals: moe; excerpt: "nit: use from vllm.utils.torch utils import current stream self.shared experts stream.wait stream(current stream())" (https://github.com/vllm-project/vllm/pull/26440#discussion_r2446025084)
- `2025-10-20T20:21:07Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:2228; signals: moe; excerpt: "nit: use from vllm.utils.torch utils import current stream ( self.shared experts stream.wait stream(current stream())" (https://github.com/vllm-project/vllm/pull/26440#discussion_r2446030159)
