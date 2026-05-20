# PR Discussion Digest

- Source PR: [vllm-project/vllm#37695](https://github.com/vllm-project/vllm/pull/37695)
- Source page: `sources/prs/vllm/PR-37695.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37695`
- Generated at: `2026-05-20T15:40:24.592622+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-20T15:21:34Z`
- Merged: `2026-03-27T23:30:46Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 14 (approved=3, commented=11)
- Inline review comments: 10
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: mgoin, robertgshaw2-redhat, vadiklyutiy, wzhao18, zou3519
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-20T15:24:11Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3982261315)
- `2026-03-20T15:26:34Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3982275311)
- `2026-03-20T15:27:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a performance optimization for Mixture-of-Experts layers by using torch.compile to fuse the ... (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3982280215)
- `2026-03-20T20:11:23Z` `APPROVED` by `mgoin` - LGTM! (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3983837945)
- `2026-03-20T20:37:54Z` `APPROVED` by `zou3519` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3983951196)
- `2026-03-20T23:23:35Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3984545606)
- `2026-03-21T00:14:35Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3984689125)
- `2026-03-21T18:35:58Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3986397729)
- `2026-03-21T20:42:27Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3986784120)
- `2026-03-22T08:46:41Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3987913966)
- `2026-03-22T09:36:44Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3987952657)
- `2026-03-22T18:45:17Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-3988444182)
- `2026-03-26T00:58:24Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-4010790955)
- `2026-03-27T23:30:39Z` `APPROVED` by `mgoin` - Thanks, LGTM! (https://github.com/vllm-project/vllm/pull/37695#pullrequestreview-4024152498)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/utils.py`: 10 inline comment(s)

## High-Signal Discussion

- `2026-03-22T09:36:43Z` `inline` by `vadiklyutiy` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: compile, hang, moe, perf, performance; excerpt: "I removed "dynamic=True", will leave it to torch.compile to figure out the compile strategy. unfortunately it is not the same as set only specific ..." (https://github.com/vllm-project/vllm/pull/37695#discussion_r2971308934)
- `2026-03-21T20:42:27Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: compile, moe, perf; excerpt: "Thanks for sharing the resources. I removed "dynamic=True", will leave it to torch.compile to figure out the compile strategy. I experimented using torch. dynamo.mark ..." (https://github.com/vllm-project/vllm/pull/37695#discussion_r2970206775)
- `2026-03-21T18:35:58Z` `inline` by `vadiklyutiy` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: compile, moe; excerpt: "you can look on example how it was done for custom ops in 34900 Implementation in 34900 was inspired how it done for model ..." (https://github.com/vllm-project/vllm/pull/37695#discussion_r2969951420)
- `2026-03-22T08:46:41Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: compile, moe; excerpt: "I don't think you want to entirely remove the dynamic argument. IIUC this will make it specialize and potentially compile on each new shape" (https://github.com/vllm-project/vllm/pull/37695#discussion_r2971263722)
- `2026-03-22T18:45:17Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: compile, moe; excerpt: "From so we don’t have to worry about unexpected recompilation. Would something like this look reasonable? This can be cleaned up if we have ..." (https://github.com/vllm-project/vllm/pull/37695#discussion_r2971907118)
- `2026-03-26T00:58:24Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: moe; excerpt: "I added dynamic=True back. Let's go with this safe approach and improve if needed in the future. @mgoin It would be good to merge ..." (https://github.com/vllm-project/vllm/pull/37695#discussion_r2991888221)
- `2026-03-20T15:24:11Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/utils.py`:350; signals: moe; excerpt: "can this have a better function name that makes it clear it is for trtllm routed moe?" (https://github.com/vllm-project/vllm/pull/37695#discussion_r2966412697)
- `2026-03-20T15:26:34Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/utils.py`:350; signals: moe; excerpt: "Was thinking about it just now. Can you check the updated?" (https://github.com/vllm-project/vllm/pull/37695#discussion_r2966425293)
- `2026-03-20T23:23:23Z` `inline` by `vadiklyutiy` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: moe; excerpt: "I'd recommend to mark as dynamic only really dynamic variables." (https://github.com/vllm-project/vllm/pull/37695#discussion_r2968365242)
- `2026-03-21T00:14:35Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/utils.py`:328; signals: moe; excerpt: "@zou3519 I am not an expert on this. Could you comment on the best practice?" (https://github.com/vllm-project/vllm/pull/37695#discussion_r2968480363)
- `2026-03-26T18:29:53Z` `issue` by `vadiklyutiy`; signals: compile; excerpt: "I was thinking why thes ops do not capture by @support torch compile Found 31985 where it is planned to remove high level custom ..." (https://github.com/vllm-project/vllm/pull/37695#issuecomment-4137287321)
