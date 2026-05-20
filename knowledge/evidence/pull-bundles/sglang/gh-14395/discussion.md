# PR Discussion Digest

- Source PR: [sgl-project/sglang#14395](https://github.com/sgl-project/sglang/pull/14395)
- Source page: `sources/prs/sglang/PR-14395.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14395`
- Generated at: `2026-05-20T15:28:00.668413+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-04T05:15:49Z`
- Merged: `2025-12-19T09:24:00Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 15 (approved=2, commented=13)
- Inline review comments: 17
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: Fridge003, hlu1, ishandhanani, nvpohanh, weireweire
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-04T05:20:30Z` `COMMENTED` by `ishandhanani` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3538165718)
- `2025-12-04T05:31:15Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3538197863)
- `2025-12-04T05:46:59Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3538237188)
- `2025-12-04T05:48:30Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3538242023)
- `2025-12-05T01:50:10Z` `COMMENTED` by `hlu1` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3542789751)
- `2025-12-05T08:54:33Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3543655253)
- `2025-12-15T03:21:01Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3576243026)
- `2025-12-15T03:32:25Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3576254879)
- `2025-12-15T05:54:29Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3576496333)
- `2025-12-15T05:59:13Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3576511394)
- `2025-12-15T11:44:59Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3577353855)
- `2025-12-15T12:39:59Z` `APPROVED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3577961992)
- `2025-12-16T02:10:25Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3580923786)
- `2025-12-16T02:57:26Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3581010139)
- `2025-12-18T20:18:49Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14395#pullrequestreview-3594891225)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 15 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-15T11:41:38Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:1070; signals: attention, cache, flashinfer, kernel, mla; excerpt: "Do we need to reset the data type in the forward batch.attn attend prefix cache=True branch? Since it also uses flashinfer.prefill.trtllm ragged attention deepseek ..." (https://github.com/sgl-project/sglang/pull/14395#discussion_r2619065560)
- `2025-12-05T08:45:03Z` `inline` by `nvpohanh` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:262; signals: attention, flashinfer, mla; excerpt: "Maybe we should just increase DEFAULT WORKSPACE SIZE MB instead of the magic number 1.2? Or should we ask FlashInfer if they can provide ..." (https://github.com/sgl-project/sglang/pull/14395#discussion_r2591869165)
- `2025-12-05T08:54:22Z` `inline` by `nvpohanh` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:1083; signals: attention, fp8, mla; excerpt: "currently, all the known models we have uses q scale/k scale/v scale = 1.0f. But if the models contain these scales, we should use ..." (https://github.com/sgl-project/sglang/pull/14395#discussion_r2591895796)
- `2025-12-15T03:32:25Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:1083; signals: attention, fp8, mla; excerpt: "I saw other place just use scale 1.0, like quantize and rope for fp8, it's called in decode and draft extend. But I do ..." (https://github.com/sgl-project/sglang/pull/14395#discussion_r2617832259)
- `2025-12-05T08:45:39Z` `inline` by `nvpohanh` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:1079; signals: attention, dtype, mla; excerpt: "should this be hard-coded to bfloat16 or should we just the model's dtype?" (https://github.com/sgl-project/sglang/pull/14395#discussion_r2591871164)
- `2025-12-15T10:00:00Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:1229; signals: flashinfer, moe, triton; excerpt: "This argument cannot be removed until the upgrade of flashinfer" (https://github.com/sgl-project/sglang/pull/14395#discussion_r2618746706)
- `2025-12-16T02:57:25Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:1070; signals: attention, fp8, mla; excerpt: "make sense, added fp8 support for it." (https://github.com/sgl-project/sglang/pull/14395#discussion_r2621572462)
- `2025-12-15T03:21:00Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:262; signals: attention, mla; excerpt: "Ideally we should follow to calculate the size. But for now I'll just increase the DEFAULT WORKSPACE SIZE MB" (https://github.com/sgl-project/sglang/pull/14395#discussion_r2617820480)
- `2025-12-04T05:20:30Z` `inline` by `ishandhanani` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:262; signals: attention, mla; excerpt: "Can you maybe leave a small comment why we do 1.2?" (https://github.com/sgl-project/sglang/pull/14395#discussion_r2587600470)
- `2025-12-04T05:31:15Z` `inline` by `nvpohanh` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:1081; signals: attention, mla; excerpt: "nit: add space after =" (https://github.com/sgl-project/sglang/pull/14395#discussion_r2587627946)
- `2025-12-04T05:46:58Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:262; signals: attention, mla; excerpt: "128k prefill length will run out of the workspace." (https://github.com/sgl-project/sglang/pull/14395#discussion_r2587658898)
- `2025-12-04T05:48:30Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:1081; signals: attention, mla; excerpt: "fixed." (https://github.com/sgl-project/sglang/pull/14395#discussion_r2587661943)
