# PR Discussion Digest

- Source PR: [sgl-project/sglang#22918](https://github.com/sgl-project/sglang/pull/22918)
- Source page: `sources/prs/sglang/PR-22918.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22918`
- Generated at: `2026-05-20T15:29:32.576636+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-16T01:46:43Z`
- Merged: `2026-05-19T08:04:49Z`

## Discussion Counts

- Issue comments: 24
- Review submissions: 13 (approved=1, commented=11, dismissed=1)
- Inline review comments: 15
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=2, outdated=4
- Human participants with discussion text: Fridge003, b8zhong, zianglih, zijiexia
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-13T02:06:05Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4277675777)
- `2026-05-13T02:08:38Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4277684362)
- `2026-05-13T02:11:33Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4277696874)
- `2026-05-13T02:25:18Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4277747338)
- `2026-05-13T02:33:59Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4277779543)
- `2026-05-13T12:11:49Z` `APPROVED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4281396255)
- `2026-05-16T18:11:56Z` `DISMISSED` by `zijiexia` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4304061071)
- `2026-05-16T18:30:59Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4304077824)
- `2026-05-18T22:25:15Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4314280734)
- `2026-05-18T22:30:27Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4314425505)
- `2026-05-18T22:48:10Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4314496705)
- `2026-05-18T22:51:01Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4314506093)
- `2026-05-18T23:04:09Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22918#pullrequestreview-4314557763)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 6 inline comment(s)
- `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`: 5 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `docs/references/environment_variables.md`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-13T02:33:59Z` `inline` by `zianglih` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:229; signals: bf16, flashinfer, fp4, fp8, moe, nvfp4, register; excerpt: "Now only the following: - Fused (inference serving): - FP8, NVFP4 - Routed (RL): - MXFP8, BF16, per-token NVFP4" (https://github.com/sgl-project/sglang/pull/22918#discussion_r3231108889)
- `2026-05-18T22:24:12Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:832; signals: flashinfer, fp4, moe, nvfp4; excerpt: "Just curious: what's the difference between nvfp4 quantize and fp4 quantzie. Looks like they are the same (except the per token activation parameter)" (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262547849)
- `2026-05-13T02:08:39Z` `inline` by `b8zhong` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:229; signals: flashinfer, moe, register; excerpt: "Do you know: 1. How long this extras test will take. Since this file has a lot of tests now (maybe we can move ..." (https://github.com/sgl-project/sglang/pull/22918#discussion_r3231033461)
- `2026-05-18T22:25:13Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:819; signals: flashinfer, fp4, moe; excerpt: "Instead of adding conditions in quantize hidden states fp4 inplace. We might open a new function for the per-token quantization, since their usage is ..." (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262551996)
- `2026-05-18T22:48:10Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:832; signals: flashinfer, fp4, moe; excerpt: "fp4 quantzie is from this code, not a flashinfer api: It eventually maps to flashinfer.fp4 quantzie, which is intended to support both ue8m0 and ..." (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262638195)
- `2026-05-18T23:04:09Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:819; signals: flashinfer, fp4, moe; excerpt: "Unfolded in . There is only one caller for quantize hidden states fp4 so directly move the per-token specific code there without defining new ..." (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262690839)
- `2026-05-13T02:11:33Z` `inline` by `zianglih` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:229; signals: flashinfer, moe, register; excerpt: "We can drop all the fused tests and only keep the routed tests." (https://github.com/sgl-project/sglang/pull/22918#discussion_r3231041606)
- `2026-05-18T21:59:35Z` `inline` by `Fridge003` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:207; signals: flashinfer, moe, register; excerpt: "Why are we removing these tests" (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262446822)
- `2026-05-18T22:30:26Z` `inline` by `zianglih` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:207; signals: flashinfer, moe, register; excerpt: "See ." (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262573283)
- `2026-05-13T02:25:18Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1761; signals: flashinfer, moe; excerpt: "it is guarded by enable flashinfer trtllm moe, which means flashinfer trtllm and flashinfer trtllm routed. Both backends support this." (https://github.com/sgl-project/sglang/pull/22918#discussion_r3231083919)
- `2026-05-18T22:09:11Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:818; signals: flashinfer, moe; excerpt: "Can we remove the here, which might cause some ambiguity" (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262482323)
- `2026-05-18T22:51:01Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:818; signals: flashinfer, moe; excerpt: "Done by" (https://github.com/sgl-project/sglang/pull/22918#discussion_r3262647166)
