# PR Discussion Digest

- Source PR: [vllm-project/vllm#25843](https://github.com/vllm-project/vllm/pull/25843)
- Source page: `sources/prs/vllm/PR-25843.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25843`
- Generated at: `2026-05-20T15:37:58.157254+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-28T20:53:52Z`
- Merged: `2025-10-01T02:18:20Z`

## Discussion Counts

- Issue comments: 28
- Review submissions: 17 (approved=1, commented=16)
- Inline review comments: 12
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=5
- Human participants with discussion text: DrStone1971, jasl, johnnynunez, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-28T20:55:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to add support for the SM120 architecture by adjusting the maximum threads ... (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3277378813)
- `2025-09-29T15:48:08Z` `COMMENTED` by `mgoin` - LGTM, thank you. Just one nit with the comment (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3280576081)
- `2025-09-29T16:59:04Z` `COMMENTED` by `yewentao256` - Thanks for the work! Verified that SM100 (Blackwell) works with this change. (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3280838530)
- `2025-09-29T17:51:22Z` `COMMENTED` by `DrStone1971` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281032993)
- `2025-09-29T17:56:35Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281054161)
- `2025-09-29T18:37:20Z` `COMMENTED` by `DrStone1971` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281249068)
- `2025-09-29T18:55:40Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281319965)
- `2025-09-29T19:14:26Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281401057)
- `2025-09-29T19:27:49Z` `COMMENTED` by `DrStone1971` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281456200)
- `2025-09-29T19:31:38Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281470699)
- `2025-09-29T20:41:38Z` `COMMENTED` by `DrStone1971` - wrong commit with out sign (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281720747)
- `2025-09-29T20:45:48Z` `COMMENTED` by `DrStone1971` - Latest Fix (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281732044)
- `2025-09-29T20:57:32Z` `COMMENTED` by `DrStone1971` - DCO problem (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281764179)
- `2025-09-29T21:03:08Z` `COMMENTED` by `DrStone1971` - DCO Problem (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281781999)
- `2025-09-29T22:11:50Z` `APPROVED` by `mgoin` - LGTM thanks for the comments (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3281962866)
- `2025-09-30T20:26:24Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3286610985)
- `2025-09-30T20:32:33Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3286629867)

## Inline Comment Hotspots

- `csrc/launch_bounds_utils.h`: 12 inline comment(s)

## High-Signal Discussion

- `2025-09-28T21:11:46Z` `issue` by `DrStone1971`; signals: blackwell, compile, ptx, sm120; excerpt: "[compile ptxas.log]( compile correct using [[NVIDIA] Blackwell Family]( 24673 patch and SM120 Architecture" (https://github.com/vllm-project/vllm/pull/25843#issuecomment-3344259951)
- `2025-09-29T16:59:04Z` `review` `COMMENTED` by `yewentao256`; signals: blackwell, hang, sm100; excerpt: "Thanks for the work! Verified that SM100 (Blackwell) works with this change." (https://github.com/vllm-project/vllm/pull/25843#pullrequestreview-3280838530)
- `2025-09-29T18:37:11Z` `inline` by `DrStone1971` `csrc/launch_bounds_utils.h`:42; signals: blackwell, sm120; excerpt: "i have fix and insert a correct if workflow for match 2048 (Blackwell, SM101 and SM110) and 1536 for SM120 and other. Please check ..." (https://github.com/vllm-project/vllm/pull/25843#discussion_r2388894915)
- `2025-09-28T21:19:30Z` `issue` by `DrStone1971`; signals: compile, sm120; excerpt: "@simon-mo & @yewentao256 this is for correct compile on SM120. There is a little problem on [csrc/launch bounds utils.h]( fixed with this patch" (https://github.com/vllm-project/vllm/pull/25843#issuecomment-3344266200)
- `2025-09-29T10:37:06Z` `issue` by `jasl`; signals: fp4, ptx; excerpt: "off-topic: when compiling on SM110, I see warnings like ptxas warning : Value of threads per SM for entry ZN4vllm15cvt fp16 to fp4I13 nv ..." (https://github.com/vllm-project/vllm/pull/25843#issuecomment-3346230713)
- `2025-09-30T07:43:51Z` `issue` by `DrStone1971`; signals: block, compile; excerpt: "@DrStone71 Unfortunately, the problem still @yewentao256 @jasl @johnnynunez @mgoin In this already merged patch ( [Compile] Fix Compile Warning for Ignoring MIN BLOCK PER ..." (https://github.com/vllm-project/vllm/pull/25843#issuecomment-3350442073)
- `2025-09-30T08:40:15Z` `issue` by `jasl`; signals: block, compile; excerpt: "@DrStone71 Unfortunately, the problem still @yewentao256 @jasl @johnnynunez @mgoin In this already merged patch ( [Compile] Fix Compile Warning for Ignoring MIN BLOCK PER ..." (https://github.com/vllm-project/vllm/pull/25843#issuecomment-3350713775)
- `2025-09-30T20:11:03Z` `issue` by `johnnynunez`; signals: block, warp; excerpt: "@jasl @DrStone71 ouch! it is 1536 Name: NVIDIA Thor Compute Capability: 11.0 Max threads/SM: 1536 Max threads/block: 1024 Warp size: 32 johnny@johnny-thor: /Projects$" (https://github.com/vllm-project/vllm/pull/25843#issuecomment-3353641150)
- `2025-09-29T19:14:26Z` `inline` by `mgoin` `csrc/launch_bounds_utils.h`:18; signals: cuda; excerpt: "@DrStone71 for instance, you could put the comment above this define to list out the cuda arch cases considered here, explicitly" (https://github.com/vllm-project/vllm/pull/25843#discussion_r2388994772)
- `2025-09-29T19:27:49Z` `inline` by `DrStone1971` `csrc/launch_bounds_utils.h`:42; signals: compile; excerpt: "@jasl you can insert nvidia-smi output and full compile log (at startup of compile system, define found architecture." (https://github.com/vllm-project/vllm/pull/25843#discussion_r2389028094)
- `2025-09-30T20:35:37Z` `issue` by `johnnynunez`; signals: fp4, nvfp4; excerpt: "nvfp4 experts quant.cu" (https://github.com/vllm-project/vllm/pull/25843#issuecomment-3353719113)
- `2025-09-29T19:31:38Z` `inline` by `jasl` `csrc/launch_bounds_utils.h`:42; signals: compile; excerpt: "Sorry, nvidia-smi on Thor seems has trouble, all data are N/A For the compile log" (https://github.com/vllm-project/vllm/pull/25843#discussion_r2389039072)
