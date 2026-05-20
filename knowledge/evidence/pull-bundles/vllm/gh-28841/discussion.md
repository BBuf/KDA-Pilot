# PR Discussion Digest

- Source PR: [vllm-project/vllm#28841](https://github.com/vllm-project/vllm/pull/28841)
- Source page: `sources/prs/vllm/PR-28841.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28841`
- Generated at: `2026-05-20T15:38:35.355764+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-17T07:23:18Z`
- Merged: `2025-11-25T07:59:40Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 15 (approved=5, changes_requested=1, commented=9)
- Inline review comments: 7
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: DarkLight1337, ProExpertProg, ZJY0516, bnellnm, elvischenv, mgoin, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-17T07:24:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the Mixture-of-Experts layer to enable an important fusion optimization (all reduce + ... (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3471328939)
- `2025-11-17T21:37:47Z` `APPROVED` by `ProExpertProg` - Nice, this should also reduce the size of the reduction in general! cc @ilmarkov @varun-sundar-rabindranath @bnellnm can you ... (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3474648366)
- `2025-11-18T06:49:31Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3475777836)
- `2025-11-18T14:09:04Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3478034654)
- `2025-11-18T15:44:59Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3478475859)
- `2025-11-18T15:51:54Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3478508981)
- `2025-11-18T16:04:32Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3478577684)
- `2025-11-18T16:46:05Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3478763171)
- `2025-11-18T16:51:35Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3478787682)
- `2025-11-18T17:50:01Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3479046199)
- `2025-11-18T22:24:04Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3479908888)
- `2025-11-18T22:25:30Z` `CHANGES_REQUESTED` by `ProExpertProg` - It seems like the "Blackwell Compile and Fusion tests" did not get triggered in CI. Could you add ... (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3479912378)
- `2025-11-19T17:23:18Z` `COMMENTED` by `elvischenv` - Resolved merge conflict. (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3483933767)
- `2025-11-21T03:27:49Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3491040193)
- `2025-11-21T14:52:46Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3493091881)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 6 inline comment(s)
- `tests/compile/distributed/test_fusions_e2e.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-18T22:25:30Z` `review` `CHANGES_REQUESTED` by `ProExpertProg`; signals: blackwell, compile, moe; excerpt: "It seems like the "Blackwell Compile and Fusion tests" did not get triggered in CI. Could you add fused moe/layer.py to the list of ..." (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3479912378)
- `2025-11-18T15:44:55Z` `inline` by `elvischenv` `vllm/model_executor/layers/fused_moe/layer.py`:1492; signals: kernel, memory, moe; excerpt: "Please see the above few lines. og hidden states is just used by padding before the MoE kernel. trtllm ar kernel just raise error ..." (https://github.com/vllm-project/vllm/pull/28841#discussion_r2538709483)
- `2025-11-18T16:04:32Z` `inline` by `elvischenv` `vllm/model_executor/layers/fused_moe/layer.py`:1492; signals: kernel, memory, moe; excerpt: "Sure. Does that mean other all reduce kernels support non-continuous memory?" (https://github.com/vllm-project/vllm/pull/28841#discussion_r2538790987)
- `2025-11-18T15:51:53Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1492; signals: kernel, moe; excerpt: "Can we move the contiguous call so that it only applies for the trtllm kernel?" (https://github.com/vllm-project/vllm/pull/28841#discussion_r2538735636)
- `2025-11-18T14:09:03Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1492; signals: moe; excerpt: "Is og hidden states going to be the same across all ranks? Also, is the call to contiguous necessary?" (https://github.com/vllm-project/vllm/pull/28841#discussion_r2538360856)
- `2025-11-18T16:51:35Z` `inline` by `elvischenv` `vllm/model_executor/layers/fused_moe/layer.py`:1492; signals: moe; excerpt: "Sorry, I just thought the issue may not a trtllm specific issue, but a general issue with symm mem: Just pushed a fix with ..." (https://github.com/vllm-project/vllm/pull/28841#discussion_r2538957750)
- `2025-11-25T05:30:52Z` `issue` by `nvpohanh`; signals: failing, pipeline; excerpt: "@mgoin could you help us to trigger the failing pipelines? I can't see the pipeline logs. thanks!" (https://github.com/vllm-project/vllm/pull/28841#issuecomment-3573843273)
- `2025-11-18T06:49:27Z` `inline` by `elvischenv` `tests/compile/distributed/test_fusions_e2e.py`:124; signals: compile; excerpt: "@ProExpertProg @mgoin Added the 20b e2e fusion test. Also tested on main and got expected failure:" (https://github.com/vllm-project/vllm/pull/28841#discussion_r2536538389)
- `2025-11-18T16:46:05Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1492; signals: moe; excerpt: "Not sure but there didn't seem to be a call to contiguous before?" (https://github.com/vllm-project/vllm/pull/28841#discussion_r2538937890)
- `2025-11-19T17:23:18Z` `review` `COMMENTED` by `elvischenv`; signals: general review; excerpt: "Resolved merge conflict." (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3483933767)
- `2025-11-17T21:37:47Z` `review` `APPROVED` by `ProExpertProg`; signals: general review; excerpt: "Nice, this should also reduce the size of the reduction in general! cc @ilmarkov @varun-sundar-rabindranath @bnellnm can you take a look please" (https://github.com/vllm-project/vllm/pull/28841#pullrequestreview-3474648366)
