# PR Discussion Digest

- Source PR: [vllm-project/vllm#41566](https://github.com/vllm-project/vllm/pull/41566)
- Source page: `sources/prs/vllm/PR-41566.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-41566`
- Generated at: `2026-05-20T15:40:53.632300+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-03T17:29:50Z`
- Merged: `2026-05-13T20:58:32Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 19 (approved=2, commented=17)
- Inline review comments: 19
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: BowenBao, ProExpertProg, claude, juhi10071998, mergify, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-03T17:29:53Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4216620028)
- `2026-05-03T17:35:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the online quantization configuration system, replacing the OnlineQuantScheme enum with a more ... (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4216624914)
- `2026-05-04T21:15:47Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4223575035)
- `2026-05-04T23:44:37Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4224323566)
- `2026-05-05T17:56:12Z` `COMMENTED` by `BowenBao` - Thanks @mgoin ! I added some suggestions (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4230325835)
- `2026-05-05T20:42:25Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4231480793)
- `2026-05-07T22:02:32Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4248015939)
- `2026-05-08T00:18:58Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4248500906)
- `2026-05-08T15:24:28Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4253327271)
- `2026-05-08T15:24:30Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4253327415)
- `2026-05-08T15:24:31Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4253327563)
- `2026-05-08T15:24:33Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4253327725)
- `2026-05-08T15:24:34Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4253327854)
- `2026-05-08T16:37:54Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4253756195)
- `2026-05-12T18:18:32Z` `COMMENTED` by `juhi10071998` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4275029701)
- `2026-05-13T17:25:48Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4283961475)
- `2026-05-13T17:59:13Z` `APPROVED` by `BowenBao` - LGTM, thanks! (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4284174122)
- `2026-05-13T18:09:53Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4284241830)
- `2026-05-13T18:13:34Z` `COMMENTED` by `juhi10071998` (https://github.com/vllm-project/vllm/pull/41566#pullrequestreview-4284262816)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`: 10 inline comment(s)
- `tests/compile/fusions_e2e/conftest.py`: 6 inline comment(s)
- `vllm/config/quantization.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-05-08T15:24:28Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:187; signals: bf16, cutlass, flashinfer, fp4, fp8, moe, mxfp4; excerpt: "Addressed. map mxfp4 backend now returns a list[Mxfp4MoeBackend]; flashinfer trtllm and flashinfer cutlass both expand to their BF16 + MXFP8 variants. The runner backend ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3209639758)
- `2026-05-08T15:24:31Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:377; signals: bf16, flashinfer, fp4, fp8, kernel, moe, mxfp4; excerpt: "Mostly addressed. The runner backend path now drops the manual upgrade dict and just iterates the candidate list from map mxfp4 backend, leaving variant ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3209640020)
- `2026-05-05T17:55:43Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:187; signals: dtype, flashinfer, fp4, fp8, moe, mxfp4; excerpt: "i think we should remove dtype from the str key and return a list of backends. i.e., - then we can have things like ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3190506967)
- `2026-05-12T18:18:32Z` `inline` by `juhi10071998` `vllm/config/quantization.py`:32; signals: bf16, dtype, fp4, hang, moe, nvfp4; excerpt: "hi @mgoin - for our usecase we wanted to ingest the nvfp4 ckpt (weights and activation in nvfp4- input scales in ckpt) as the ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3228779125)
- `2026-05-08T16:37:54Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:377; signals: fp4, fp8, kernel, moe, mxfp4; excerpt: "accepts both (kMxfp4Static, None) and (kMxfp4Static, kMxfp8Dynamic) for the same kernel class I ran into a similar situation in 41436 for aiter backend, where ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3210019410)
- `2026-05-04T23:44:37Z` `inline` by `mgoin` `tests/compile/fusions_e2e/conftest.py`:110; signals: blackwell, compile, fp8, hopper; excerpt: "I don't think so, we don't have mxfp8 activation support beyond Blackwell. So if this test runs on Hopper then it would fail" (https://github.com/vllm-project/vllm/pull/41566#discussion_r3185181797)
- `2026-05-08T15:24:29Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:212; signals: fp4, hang, moe, mxfp4; excerpt: "Took user override wins, raise on conflict -- see resolve activation key. The user-set quantization config.moe.activation and the caller-supplied activation key (e.g. compressed-tensors W4A8 ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3209639895)
- `2026-05-05T17:37:19Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:380; signals: fp4, moe, mxfp4; excerpt: "fyi, in 39136 I added activation key: QuantKey None = None, arg to this method, to pass info from model's quant config. should user ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3190396512)
- `2026-05-05T17:40:21Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:377; signals: fp4, moe, mxfp4; excerpt: "can we leave it to is supported config to find the matching config? as long as user overriden activation key is passed, it should ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3190413284)
- `2026-05-05T17:41:14Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:212; signals: fp4, moe, mxfp4; excerpt: "similar to feels like there's no need to filter backends explicitly as it is handled by is supported config later." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3190420476)
- `2026-05-05T17:47:34Z` `inline` by `BowenBao` `tests/compile/fusions_e2e/conftest.py`:111; signals: compile, fp8, moe; excerpt: "i think it would be helpful to add more docs in docs/features/quantization/online.md for both the nested dict structure and the shorthand arg like --quantization-config.moe.activation ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3190460130)
- `2026-05-13T17:25:48Z` `inline` by `mgoin` `vllm/config/quantization.py`:32; signals: fp4, moe, nvfp4; excerpt: "If you want to use the marlin backend with an existing NVFP4 W4A4 model, you can just use --linear-backend marlin or --moe-backend marlin. Is ..." (https://github.com/vllm-project/vllm/pull/41566#discussion_r3236227438)
