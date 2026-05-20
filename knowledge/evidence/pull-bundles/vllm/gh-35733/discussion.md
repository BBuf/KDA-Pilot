# PR Discussion Digest

- Source PR: [vllm-project/vllm#35733](https://github.com/vllm-project/vllm/pull/35733)
- Source page: `sources/prs/vllm/PR-35733.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35733`
- Generated at: `2026-05-20T15:40:03.418701+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-02T11:13:02Z`
- Merged: `2026-04-06T22:18:27Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 23 (approved=7, changes_requested=1, commented=15)
- Inline review comments: 25
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=12, outdated=12
- Human participants with discussion text: BowenBao, fxmarty-amd, kylesayrs, mergify, mgoin, vkuzo
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-02T11:15:25Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request introduces support for NVFP4 models on hardware without native support through an emulation ... (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3875537996)
- `2026-03-02T11:18:49Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3875552030)
- `2026-03-02T11:18:55Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3875552498)
- `2026-03-04T15:05:42Z` `COMMENTED` by `vkuzo` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3890016776)
- `2026-03-04T15:07:56Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3890030178)
- `2026-03-04T16:15:23Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3890460731)
- `2026-03-04T16:16:15Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3890466107)
- `2026-03-05T18:14:43Z` `APPROVED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3898635497)
- `2026-03-06T14:13:34Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3903946030)
- `2026-03-06T14:13:39Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3903946409)
- `2026-03-06T14:14:38Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-3903953056)
- `2026-03-24T21:42:21Z` `COMMENTED` by `mgoin` - LGTM, just some notes to cleanup on before landing. Thanks! (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4002274469)
- `2026-03-26T12:42:27Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4013830053)
- `2026-03-26T12:42:37Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4013831374)
- `2026-03-26T12:42:45Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4013832115)
- `2026-03-26T12:42:50Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4013832841)
- `2026-03-30T20:42:26Z` `APPROVED` by `mgoin` - LGTM! Just need to fix the conflict (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4033204015)
- `2026-03-30T22:47:56Z` `APPROVED` by `kylesayrs` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4033437128)
- `2026-04-01T18:12:26Z` `APPROVED` by `kylesayrs` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4046080311)
- `2026-04-01T18:13:38Z` `APPROVED` by `kylesayrs` - Fail first test pass. (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4046086292)
- `2026-04-01T18:15:04Z` `CHANGES_REQUESTED` by `kylesayrs` - Got a local failure on second test, test nvfp4[emulation-False-nvidia/Llama-3.1-8B-Instruct-NVFP4] on an A100. It seems like the nvfp4 kernel ... (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4046093138)
- `2026-04-02T18:00:24Z` `APPROVED` by `kylesayrs` (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4052272928)
- `2026-04-06T22:18:12Z` `APPROVED` by `mgoin` - Great work @fxmarty-amd ! (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4064822218)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`: 6 inline comment(s)
- `vllm/model_executor/layers/quantization/modelopt.py`: 5 inline comment(s)
- `tests/models/quantization/test_nvfp4.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`: 3 inline comment(s)
- `vllm/envs.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-02T14:03:59Z` `issue` by `fxmarty-amd`; signals: cuda, fp4, h100, nvfp4, triton; excerpt: "@kylesayrs Unfortunately I do not have access to A100, but I could run successfully the tests on H100 in the following environment: - Docker ..." (https://github.com/vllm-project/vllm/pull/35733#issuecomment-4178125222)
- `2026-04-02T18:14:48Z` `issue` by `fxmarty-amd`; signals: fp4, fp8, nvfp4, regression, triton; excerpt: "@kylesayrs Happy to submit this commit as a standalone PR to support Ampere and lower, MI250 and lower for NVFP4 emulation. I think we ..." (https://github.com/vllm-project/vllm/pull/35733#issuecomment-4179601578)
- `2026-04-01T18:15:04Z` `review` `CHANGES_REQUESTED` by `kylesayrs`; signals: fp4, kernel, nvfp4; excerpt: "Got a local failure on second test, test nvfp4[emulation-False-nvidia/Llama-3.1-8B-Instruct-NVFP4] on an A100. It seems like the nvfp4 kernel is still being selected." (https://github.com/vllm-project/vllm/pull/35733#pullrequestreview-4046093138)
- `2026-04-02T16:19:33Z` `issue` by `fxmarty-amd`; signals: failing, fp8, h100, triton; excerpt: "@kylesayrs please see my updated comment: Checking offline with @kylesayrs , the dispatch is correct, but probably something like gets transpiled to triton, which ..." (https://github.com/vllm-project/vllm/pull/35733#issuecomment-4178980147)
- `2026-03-04T15:05:42Z` `inline` by `vkuzo` `vllm/model_executor/layers/quantization/modelopt.py`:1164; signals: fp4, hang, nvfp4; excerpt: "this is unintuitive, can we change NvFp4LinearBackend.EMULATION to take in weight global scale the same way the production backends do instead?" (https://github.com/vllm-project/vllm/pull/35733#discussion_r2884318703)
- `2026-03-05T18:13:28Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`:66; signals: fp4, kernel, nvfp4; excerpt: "should we put the current platform.is rocm() check as elif branch here instead of up there? that way potentially users can still pick other ..." (https://github.com/vllm-project/vllm/pull/35733#discussion_r2891488343)
- `2026-03-24T21:38:09Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:37; signals: fp4, fp8, nvfp4; excerpt: "We should move this and a lot of the other utils into a proper class like Mxfp8LinearOp in It is okay to do this ..." (https://github.com/vllm-project/vllm/pull/35733#discussion_r2984425874)
- `2026-03-24T21:02:57Z` `inline` by `mgoin` `tests/models/quantization/test_nvfp4.py`:101; signals: fp4, nvfp4; excerpt: "Can we keep the list as one and handle skip filtering inside of the test nvfp4 function? That way we have the same test ..." (https://github.com/vllm-project/vllm/pull/35733#discussion_r2984252309)
- `2026-03-24T21:41:20Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`:36; signals: fp4, nvfp4; excerpt: "We should avoid actually importing and try-except. See vllm/utils/import utils.py and the has module function" (https://github.com/vllm-project/vllm/pull/35733#discussion_r2984438235)
- `2026-03-02T11:18:55Z` `inline` by `fxmarty-amd` `tests/models/quantization/test_nvfp4.py`:97; signals: fp4, nvfp4; excerpt: "bc6ff397f2e7b20a8c8517c2133e46d6ff87c282" (https://github.com/vllm-project/vllm/pull/35733#discussion_r2871870554)
- `2026-03-04T16:16:15Z` `inline` by `fxmarty-amd` `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`:72; signals: fp4, nvfp4; excerpt: "This aligns emulation behavior with other backends." (https://github.com/vllm-project/vllm/pull/35733#discussion_r2884723165)
- `2026-03-06T14:13:39Z` `inline` by `fxmarty-amd` `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`:66; signals: fp4, nvfp4; excerpt: "addressed in e7d72f5e2725803f60c74e104653da6d5db9b394" (https://github.com/vllm-project/vllm/pull/35733#discussion_r2896005992)
