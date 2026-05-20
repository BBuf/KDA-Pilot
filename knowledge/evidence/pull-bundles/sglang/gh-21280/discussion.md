# PR Discussion Digest

- Source PR: [sgl-project/sglang#21280](https://github.com/sgl-project/sglang/pull/21280)
- Source page: `sources/prs/sglang/PR-21280.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21280`
- Generated at: `2026-05-20T15:29:12.029160+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T05:39:23Z`
- Merged: `2026-04-04T04:57:45Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: Fridge003, Kangyan-Zhou, alexnails, gzy19990617, zianglih
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-24T22:34:41Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/21280#pullrequestreview-4002781217)
- `2026-03-25T17:57:34Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/21280#pullrequestreview-4008682525)
- `2026-03-29T07:16:45Z` `COMMENTED` by `alexnails` - very tiny comments. overall LGTM! (https://github.com/sgl-project/sglang/pull/21280#pullrequestreview-4026453909)
- `2026-03-29T23:52:39Z` `APPROVED` by `alexnails` - Approved! Regarding bmm removal and reversion to bf16, this makes sense to me given attention can be sensitive ... (https://github.com/sgl-project/sglang/pull/21280#pullrequestreview-4027430437)
- `2026-04-03T20:36:59Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21280#pullrequestreview-4057210089)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 2 inline comment(s)
- `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`: 1 inline comment(s)
- `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-24T22:34:41Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`; signals: flashinfer, fp8, hang, moe; excerpt: "No functional changes in this file. The previous implementation for align mxfp8 moe weights for flashinfer trtllm takes several minutes on large models like ..." (https://github.com/sgl-project/sglang/pull/21280#discussion_r2984699405)
- `2026-03-29T07:15:07Z` `inline` by `alexnails` `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`:445; signals: attention, flashinfer, fp8, mla; excerpt: "nit: shapes here get a little messy to mental model due to how mxfp8 has to be processed. An explanation for fp8 quant utils.flashinfer ..." (https://github.com/sgl-project/sglang/pull/21280#discussion_r3005823553)
- `2026-03-29T08:57:59Z` `issue` by `zianglih`; signals: bf16, fp8, hang, mla; excerpt: "Hi @alexnails , thank you for reviewing! I just double checked and it turns out the mxfp8 bmm is now dead code. Since the ..." (https://github.com/sgl-project/sglang/pull/21280#issuecomment-4149737061)
- `2026-03-25T17:57:34Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:50; signals: flashinfer, moe; excerpt: "In the future when we refactor other mxfp/nvfp flashinfer trtllm gen moe backends we can expand the dict" (https://github.com/sgl-project/sglang/pull/21280#discussion_r2990017288)
- `2026-03-29T23:52:39Z` `review` `APPROVED` by `alexnails`; signals: attention, bf16; excerpt: "Approved! Regarding bmm removal and reversion to bf16, this makes sense to me given attention can be sensitive to precision, have pinged @yueming-yuan just ..." (https://github.com/sgl-project/sglang/pull/21280#pullrequestreview-4027430437)
- `2026-03-29T07:05:30Z` `inline` by `alexnails` `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`:487; signals: blackwell; excerpt: "should we check is blackwell here? (if we do not already do this somewhere else in the path)" (https://github.com/sgl-project/sglang/pull/21280#discussion_r3005815933)
- `2026-03-29T07:16:45Z` `review` `COMMENTED` by `alexnails`; signals: general review; excerpt: "very tiny comments. overall LGTM!" (https://github.com/sgl-project/sglang/pull/21280#pullrequestreview-4026453909)
- `2026-04-01T06:43:55Z` `issue` by `alexnails`; signals: b200; excerpt: "I think we are now up to date on CI fixes. We just need to run rerun stage stage-c-test-4-gpu-b200 (with the as a -) ..." (https://github.com/sgl-project/sglang/pull/21280#issuecomment-4167901649)
- `2026-04-02T23:00:52Z` `issue` by `zianglih`; signals: fp8; excerpt: "Miles mxfp8 RL functionality has been verified by" (https://github.com/sgl-project/sglang/pull/21280#issuecomment-4180915149)
