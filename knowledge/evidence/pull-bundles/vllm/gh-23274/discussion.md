# PR Discussion Digest

- Source PR: [vllm-project/vllm#23274](https://github.com/vllm-project/vllm/pull/23274)
- Source page: `sources/prs/vllm/PR-23274.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23274`
- Generated at: `2026-05-20T15:37:27.109113+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-20T17:07:12Z`
- Merged: `2025-08-25T18:47:52Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 24 (approved=2, commented=22)
- Inline review comments: 36
- Review threads observed: 20
- Resolved/outdated thread markers: resolved=12, outdated=11
- Human participants with discussion text: mgoin, xyang16, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-08-20T17:08:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a fused grouped topk kernel for MoE, which shows a nice performance ... (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3137547191)
- `2025-08-20T21:33:59Z` `COMMENTED` by `yewentao256` - Thanks for the work! Could you also test the acc for R1? lm eval --model local-completions --model args ... (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3138307317)
- `2025-08-20T22:31:55Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3138364693)
- `2025-08-22T00:28:28Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3142656660)
- `2025-08-22T00:31:29Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3142664340)
- `2025-08-22T00:33:38Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3142667260)
- `2025-08-22T00:35:27Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3142668891)
- `2025-08-22T01:17:45Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3142727521)
- `2025-08-22T18:00:17Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145367532)
- `2025-08-22T18:25:04Z` `COMMENTED` by `mgoin` - Hey @xyang16 I think everything checks out to me, thanks for working on this! One thing we must ... (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145430474)
- `2025-08-22T20:07:34Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145781972)
- `2025-08-22T20:08:08Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145783600)
- `2025-08-22T20:08:20Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145784051)
- `2025-08-22T20:10:02Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145789817)
- `2025-08-22T20:10:34Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145791461)
- `2025-08-22T20:10:48Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145791978)
- `2025-08-22T20:10:58Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145792460)
- `2025-08-22T20:23:30Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3145848295)
- `2025-08-22T22:29:54Z` `COMMENTED` by `yewentao256` - Nice work! Some additional thoughts (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3146365266)
- `2025-08-22T22:51:04Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3146458574)
- `2025-08-23T14:18:28Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3148170410)
- `2025-08-23T14:57:44Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3148279208)
- `2025-08-25T18:35:26Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3152601694)
- `2025-08-25T18:43:49Z` `APPROVED` by `mgoin` - LGTM, thanks for the iterations here. Will carefully look over CI to see if all failures are known. (https://github.com/vllm-project/vllm/pull/23274#pullrequestreview-3152626026)

## Inline Comment Hotspots

- `csrc/moe/grouped_topk_kernels.cu`: 12 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 12 inline comment(s)
- `tests/kernels/moe/test_grouped_topk.py`: 4 inline comment(s)
- `CMakeLists.txt`: 2 inline comment(s)
- `vllm/_custom_ops.py`: 2 inline comment(s)
- `csrc/moe/moe_ops.h`: 2 inline comment(s)
- `csrc/moe/torch_bindings.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-22T18:24:48Z` `inline` by `mgoin` `tests/kernels/moe/test_grouped_topk.py`:27; signals: cuda, kernel, moe; excerpt: "Add a pytest skipif not current platform.is cuda()" (https://github.com/vllm-project/vllm/pull/23274#discussion_r2294393855)
- `2025-08-20T21:49:18Z` `inline` by `mgoin` `csrc/moe/grouped_topk_kernels.cu`:481; signals: kernel, moe; excerpt: "Can you leave clear comments around the code section that is copied from TRT? I'm confused on what to review versus what to accept ..." (https://github.com/vllm-project/vllm/pull/23274#discussion_r2289378538)
- `2025-08-22T00:28:27Z` `inline` by `xyang16` `vllm/model_executor/layers/fused_moe/fused_moe.py`:964; signals: hang, moe; excerpt: "Thanks for your review! In my other PR I have added the routed scaling factor to grouped topk, which is coming from config.routed scaling ..." (https://github.com/vllm-project/vllm/pull/23274#discussion_r2292412647)
- `2025-08-22T18:00:17Z` `inline` by `xyang16` `csrc/moe/grouped_topk_kernels.cu`:481; signals: kernel, moe; excerpt: "Thanks for your review! I have added comment that the code from TRT is the invokeNoAuxTc function and the related kernels launched from invokeNoAuxTc: ..." (https://github.com/vllm-project/vllm/pull/23274#discussion_r2294340500)
- `2025-08-22T20:23:30Z` `inline` by `xyang16` `vllm/model_executor/layers/fused_moe/fused_moe.py`:954; signals: hang, moe; excerpt: "Initially I was wanting to make grouped topk and fused grouped topk separate, but rocm is only calling single grouped topk ( so I ..." (https://github.com/vllm-project/vllm/pull/23274#discussion_r2294656476)
- `2025-08-22T22:18:17Z` `inline` by `yewentao256` `csrc/moe/grouped_topk_kernels.cu`:92; signals: kernel, moe; excerpt: "is better than sometimes with ascending, sometimes with greater, which would be a little bit confused, could we uniform them?" (https://github.com/vllm-project/vllm/pull/23274#discussion_r2294847986)
- `2025-08-20T21:29:33Z` `inline` by `yewentao256` `csrc/moe/grouped_topk_kernels.cu`:159; signals: kernel, moe; excerpt: "Looks confused for the comments, if it is used for debugging, perhaps we can remove it." (https://github.com/vllm-project/vllm/pull/23274#discussion_r2289344006)
- `2025-08-20T21:30:37Z` `inline` by `yewentao256` `csrc/moe/grouped_topk_kernels.cu`:199; signals: kernel, moe; excerpt: "Same above" (https://github.com/vllm-project/vllm/pull/23274#discussion_r2289346221)
- `2025-08-20T22:29:49Z` `inline` by `mgoin` `tests/kernels/moe/test_grouped_topk.py`:27; signals: kernel, moe; excerpt: "How long does this test take? We may want to prune down configs, such as only testing bfloat16" (https://github.com/vllm-project/vllm/pull/23274#discussion_r2289439572)
- `2025-08-22T00:31:29Z` `inline` by `xyang16` `csrc/moe/grouped_topk_kernels.cu`:159; signals: kernel, moe; excerpt: "Thanks for your review! I have removed this." (https://github.com/vllm-project/vllm/pull/23274#discussion_r2292417633)
- `2025-08-22T00:33:37Z` `inline` by `xyang16` `vllm/model_executor/layers/fused_moe/fused_moe.py`:958; signals: kernel, moe; excerpt: "Thanks for your review! This is based on what is implemented, see in grouped topk kernels.cu:" (https://github.com/vllm-project/vllm/pull/23274#discussion_r2292419701)
- `2025-08-22T00:35:27Z` `inline` by `xyang16` `csrc/moe/grouped_topk_kernels.cu`:199; signals: kernel, moe; excerpt: "Thanks for your review! I have removed this." (https://github.com/vllm-project/vllm/pull/23274#discussion_r2292421029)
