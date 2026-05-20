# PR Discussion Digest

- Source PR: [vllm-project/vllm#26545](https://github.com/vllm-project/vllm/pull/26545)
- Source page: `sources/prs/vllm/PR-26545.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26545`
- Generated at: `2026-05-20T15:38:08.230724+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-09T23:48:02Z`
- Merged: `2025-10-17T18:06:33Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 19 (approved=3, commented=16)
- Inline review comments: 18
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: BowenBao, SageMoore, fxmarty-amd, maleksan85, mawong-amd, mergify, mgoin, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-13T18:26:34Z` `COMMENTED` by `mawong-amd` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3332629289)
- `2025-10-13T22:24:22Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3333173687)
- `2025-10-14T01:44:38Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3333609819)
- `2025-10-14T01:50:34Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3333617765)
- `2025-10-14T02:23:31Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3333674868)
- `2025-10-14T12:23:59Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3335332060)
- `2025-10-14T22:11:17Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3337681812)
- `2025-10-14T22:12:31Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3337684340)
- `2025-10-14T22:58:21Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3337804445)
- `2025-10-14T23:29:55Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3337867228)
- `2025-10-15T09:32:25Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3339372689)
- `2025-10-15T18:15:14Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3341710007)
- `2025-10-15T21:49:14Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3342473595)
- `2025-10-16T00:28:05Z` `APPROVED` by `BowenBao` - Thanks for updates, LGTM on quark side. (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3342710776)
- `2025-10-16T00:38:35Z` `APPROVED` by `mgoin` - LGTM, thanks! (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3342722426)
- `2025-10-16T11:55:05Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3344402647)
- `2025-10-16T11:56:10Z` `APPROVED` by `fxmarty-amd` - cc @mgoin if you have an opinion on the above. Otherwise LGTM, think we should use mxfp4 instead ... (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3344442369)
- `2025-10-16T17:05:57Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3345973161)
- `2025-10-16T17:19:55Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3346046772)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/quark/quark_moe.py`: 14 inline comment(s)
- `vllm/envs.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-15T18:15:14Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:571; signals: bf16, block, fp4, kernel, moe, mxfp4, perf; excerpt: "Hi @maleksan85, emulation is already supported. when self.emulate = True it simulates in bf16 matmul, with mxfp4 weight dequant and performs qdq over activation. ..." (https://github.com/vllm-project/vllm/pull/26545#discussion_r2433535128)
- `2025-10-14T01:44:38Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:571; signals: fp4, moe, mxfp4; excerpt: "Is it possible to infer the datatype from the quark config if VLLM ROCM USE CK MXFP4 MOE is always set to true so ..." (https://github.com/vllm-project/vllm/pull/26545#discussion_r2427697321)
- `2025-10-14T12:23:59Z` `inline` by `tjtanaa` `vllm/envs.py`:932; signals: fp4, moe, mxfp4; excerpt: "If this is enabled by default, is it possible to infer the datatype from the quark config if VLLM ROCM USE CK MXFP4 MOE ..." (https://github.com/vllm-project/vllm/pull/26545#discussion_r2428965493)
- `2025-10-16T11:55:01Z` `inline` by `fxmarty-amd` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:660; signals: fp4, moe, mxfp4; excerpt: "Why are we not using torch.ops.vllm.rocm aiter fused moe or vllm.model executor.layers.fused moe.rocm aiter fused moe.rocm aiter fused experts like done in or in ..." (https://github.com/vllm-project/vllm/pull/26545#discussion_r2435621481)
- `2025-10-16T11:56:10Z` `review` `APPROVED` by `fxmarty-amd`; signals: fp4, mxfp4, nvfp4; excerpt: "cc @mgoin if you have an opinion on the above. Otherwise LGTM, think we should use mxfp4 instead of fp4 to clarify against nvfp4." (https://github.com/vllm-project/vllm/pull/26545#pullrequestreview-3344442369)
- `2025-10-13T22:22:40Z` `inline` by `SageMoore` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:571; signals: fp4, moe; excerpt: "What's the expected behavior on a machine that doesn't support fp4? Will we crash if the environment variable is set?" (https://github.com/vllm-project/vllm/pull/26545#discussion_r2427426051)
- `2025-10-14T01:50:34Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:650; signals: moe, register; excerpt: "Does it require new AITER version? I remember that the AITER commit in the docker/Dockerfile.rocm base still requires the op to be wrapped in ..." (https://github.com/vllm-project/vllm/pull/26545#discussion_r2427703539)
- `2025-10-16T11:46:21Z` `inline` by `fxmarty-amd` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:479; signals: fp4, moe; excerpt: "We can add current platform.supports mx(), use fp4 aiter moe(), self.ocp mx scheme values in the log" (https://github.com/vllm-project/vllm/pull/26545#discussion_r2435597308)
- `2025-10-16T17:19:55Z` `inline` by `maleksan85` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:660; signals: fp4, moe; excerpt: "not sure I got your message but mentioned MoEs are a8w8 MoEs, not fp4." (https://github.com/vllm-project/vllm/pull/26545#discussion_r2436805927)
- `2025-10-14T22:11:17Z` `inline` by `maleksan85` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:571; signals: moe; excerpt: "well, to my knowledge there should be emulation. However deeper look showed that emulation is not yet implemented: cc @fxmarty-amd @BowenBao please comment if ..." (https://github.com/vllm-project/vllm/pull/26545#discussion_r2430607807)
- `2025-10-14T22:12:31Z` `inline` by `maleksan85` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:650; signals: moe; excerpt: "I'm running on pretty old version from rocm/aiter/355 wip: Name: aiter Version: 0.1.5.dev128+g2d33708e2" (https://github.com/vllm-project/vllm/pull/26545#discussion_r2430609457)
- `2025-10-14T02:23:25Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:658; signals: moe; excerpt: "Could you assert the activation instead of assuming else gelu?" (https://github.com/vllm-project/vllm/pull/26545#discussion_r2427747337)
