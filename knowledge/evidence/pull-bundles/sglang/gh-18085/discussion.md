# PR Discussion Digest

- Source PR: [sgl-project/sglang#18085](https://github.com/sgl-project/sglang/pull/18085)
- Source page: `sources/prs/sglang/PR-18085.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18085`
- Generated at: `2026-05-20T15:28:35.169220+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-02T01:17:46Z`
- Merged: `2026-02-27T22:55:08Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 9
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: Fridge003, b8zhong, guapisolo, zhaochenyang20, zianglih
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-02T01:19:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request effectively addresses the issue with updating nvfp4 weights. The introduction of the copy ... (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3736955278)
- `2026-02-12T21:17:24Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3793702093)
- `2026-02-12T21:32:10Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3793783003)
- `2026-02-12T22:55:08Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3794124324)
- `2026-02-13T00:46:09Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3793787543)
- `2026-02-17T21:33:41Z` `APPROVED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3816416918)
- `2026-02-25T01:57:59Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3851414364)
- `2026-02-27T22:54:46Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18085#pullrequestreview-3869464151)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 5 inline comment(s)
- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-02-13T00:53:12Z` `issue` by `b8zhong`; signals: cutlass, flashinfer, kernel, perf, performance; excerpt: "Thanks for data. Btw, flashinfer cutlass and cutlass are actually the same original kernel, cutlass one is just ported before existence in flashinfer I ..." (https://github.com/sgl-project/sglang/pull/18085#issuecomment-3894208752)
- `2026-02-25T01:57:59Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:186; signals: flashinfer, fp4, hang, moe; excerpt: "I made a mistake here. This clean up is for temp buffers consumed by prepare static weights for trtllm fp4 moe, not for the ..." (https://github.com/sgl-project/sglang/pull/18085#discussion_r2850407405)
- `2026-02-13T00:28:49Z` `issue` by `zianglih`; signals: cutlass, flashinfer, fp4, moe; excerpt: "Explicitly testing --moe-runner-backend cutlass and --moe-runner-backend flashinfer trtllm --quantization modelopt fp4 as requested: - CUTLASS, WITH this PR: - trtllm-gen, WITHOUT this PR: - ..." (https://github.com/sgl-project/sglang/pull/18085#issuecomment-3894143023)
- `2026-02-12T21:13:12Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1679; signals: cutlass, moe; excerpt: "QQ: did you test both CUTLASS MoE and trtllm-gen MoE? Since I think, the default right now may be trtllm, but I'm not sure ..." (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801086476)
- `2026-02-12T21:32:10Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:186; signals: flashinfer, moe; excerpt: "I think in previous normal mode implementation, extra buffers are allocated by Parameter(...) and that's why we need to del old buffers. In this ..." (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801155900)
- `2026-02-12T21:16:41Z` `inline` by `b8zhong` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:186; signals: flashinfer, moe; excerpt: "Can you wrap this in a conditional somehow? (we still want to delete it when in normal mode right..)" (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801098856)
- `2026-02-12T22:55:08Z` `inline` by `b8zhong` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:186; signals: flashinfer, moe; excerpt: "I see. Then it's alright" (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801439524)
- `2026-02-25T10:31:32Z` `issue` by `zianglih`; signals: fp4, oom; excerpt: "@Fridge003 previous OOM fp4 ci is fixed by ( Thanks!" (https://github.com/sgl-project/sglang/pull/18085#issuecomment-3958296747)
- `2026-02-12T21:33:12Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/modelopt_quant.py`:110; signals: fp8; excerpt: "Similar pattern also exists in my previous mxfp8 PR Let me sse if I can refactor this." (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801159601)
- `2026-02-13T00:45:05Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/modelopt_quant.py`:110; signals: fp8; excerpt: "Finished by . For the MXFP8 one we can make it in a small further PR." (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801734499)
- `2026-02-12T21:14:31Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/modelopt_quant.py`:110; signals: general review; excerpt: "If we need this wrappers for all online weight updates (not really too familiar with this features), we can move it to maybe a ..." (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801091079)
- `2026-02-13T00:29:31Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1679; signals: general review; excerpt: "Post the logs here Both work." (https://github.com/sgl-project/sglang/pull/18085#discussion_r2801700445)
