# PR Discussion Digest

- Source PR: [vllm-project/vllm#21643](https://github.com/vllm-project/vllm/pull/21643)
- Source page: `sources/prs/vllm/PR-21643.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21643`
- Generated at: `2026-05-20T15:36:51.439891+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-26T03:05:54Z`
- Merged: `2025-08-02T14:49:08Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: DarkLight1337, jikunshang, xuechendi, yma11
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-26T03:07:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for Falcon3-MoE models on the XPU platform by adding XPU-specific logic ... (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3057390487)
- `2025-07-29T15:54:21Z` `COMMENTED` by `xuechendi` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3068198713)
- `2025-07-29T15:54:33Z` `COMMENTED` by `xuechendi` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3068199816)
- `2025-07-29T23:33:15Z` `APPROVED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3069481423)
- `2025-07-30T04:40:20Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3069862320)
- `2025-08-01T02:28:36Z` `COMMENTED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3077416285)
- `2025-08-01T02:28:49Z` `COMMENTED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3077416682)
- `2025-08-01T07:26:29Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3078067290)
- `2025-08-01T09:22:34Z` `COMMENTED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/21643#pullrequestreview-3078404338)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 9 inline comment(s)

## High-Signal Discussion

- `2025-07-29T02:17:54Z` `issue` by `yma11`; signals: hang, kernel, moe; excerpt: "can you rename the PR title? I think this change is not for falcon only. xpu should not support any MoE model before? updated. ..." (https://github.com/vllm-project/vllm/pull/21643#issuecomment-3130338703)
- `2025-08-01T09:22:34Z` `inline` by `jikunshang` `vllm/model_executor/layers/fused_moe/layer.py`:332; signals: benchmark, moe; excerpt: "for test/benchmark purpose, we may keep both. it's ok to keep it now." (https://github.com/vllm-project/vllm/pull/21643#discussion_r2247432399)
- `2025-07-28T01:28:25Z` `issue` by `jikunshang`; signals: hang, moe; excerpt: "can you rename the PR title? I think this change is not for falcon only. xpu should not support any MoE model before?" (https://github.com/vllm-project/vllm/pull/21643#issuecomment-3124920557)
- `2025-07-29T15:56:19Z` `issue` by `xuechendi`; signals: hang, moe; excerpt: "@yma11 , with this PR, we will continue the optimizations on ipex.llm.modules.GatedMLPMOE right? If this PR is ready, @jikunshang , please approve" (https://github.com/vllm-project/vllm/pull/21643#issuecomment-3133133731)
- `2025-08-01T02:28:36Z` `inline` by `jikunshang` `vllm/model_executor/layers/fused_moe/layer.py`:332; signals: moe; excerpt: "can we follow code path like cpu, add a xpu fused moe.py. I think we will also add another path in the future via ..." (https://github.com/vllm-project/vllm/pull/21643#discussion_r2246749734)
- `2025-08-01T07:26:29Z` `inline` by `yma11` `vllm/model_executor/layers/fused_moe/layer.py`:332; signals: moe; excerpt: "But we probably won't keep both paths. I am not sure what else can be put in xpu fused moe.py and for now, we ..." (https://github.com/vllm-project/vllm/pull/21643#discussion_r2247197354)
- `2025-07-29T15:54:21Z` `inline` by `xuechendi` `vllm/model_executor/layers/fused_moe/layer.py`:336; signals: moe; excerpt: "@yma11 , please resolve gemini's comments" (https://github.com/vllm-project/vllm/pull/21643#discussion_r2240291190)
- `2025-07-29T15:54:33Z` `inline` by `xuechendi` `vllm/model_executor/layers/fused_moe/layer.py`:555; signals: moe; excerpt: "@yma11 same here" (https://github.com/vllm-project/vllm/pull/21643#discussion_r2240291887)
- `2025-07-30T04:40:20Z` `inline` by `yma11` `vllm/model_executor/layers/fused_moe/layer.py`:336; signals: moe; excerpt: "This doesn't quite apply to our interface. just resolve it." (https://github.com/vllm-project/vllm/pull/21643#discussion_r2241512257)
- `2025-08-01T02:28:49Z` `inline` by `jikunshang` `vllm/model_executor/layers/fused_moe/layer.py`:545; signals: moe; excerpt: "XPU" (https://github.com/vllm-project/vllm/pull/21643#discussion_r2246750089)
