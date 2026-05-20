# PR Discussion Digest

- Source PR: [vllm-project/vllm#33049](https://github.com/vllm-project/vllm/pull/33049)
- Source page: `sources/prs/vllm/PR-33049.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-33049`
- Generated at: `2026-05-20T15:39:34.505816+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-26T02:29:56Z`
- Merged: `2026-03-19T19:07:45Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 18 (commented=18)
- Inline review comments: 17
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=7, outdated=5
- Human participants with discussion text: bnellnm, mergify, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-26T02:33:07Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant and beneficial refactoring of the MoE implementation. By moving the ... (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3704483941)
- `2026-01-29T22:30:08Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3725355813)
- `2026-01-29T22:41:35Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3725388555)
- `2026-01-29T22:50:42Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3725411497)
- `2026-03-05T15:57:00Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3897728695)
- `2026-03-05T15:58:42Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3897740197)
- `2026-03-05T17:59:24Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3898572847)
- `2026-03-05T17:59:36Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3898573799)
- `2026-03-05T21:02:54Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3899654153)
- `2026-03-05T21:16:47Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3899727812)
- `2026-03-18T22:58:12Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3971352938)
- `2026-03-18T23:04:02Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3971382257)
- `2026-03-18T23:11:50Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3971424702)
- `2026-03-18T23:22:28Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3971483535)
- `2026-03-18T23:23:34Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3971489436)
- `2026-03-18T23:53:58Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3971633429)
- `2026-03-19T00:05:48Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3971681556)
- `2026-03-19T16:54:12Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/33049#pullrequestreview-3976551622)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`: 17 inline comment(s)

## High-Signal Discussion

- `2026-03-19T18:46:49Z` `issue` by `robertgshaw2-redhat`; signals: b200, fp4, nvfp4, perf, performance; excerpt: "I ran some LL performance tests, B200 NVFP4 DeepSeek EP=4 - pr - main" (https://github.com/vllm-project/vllm/pull/33049#issuecomment-4092505760)
- `2026-03-18T23:23:34Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:790; signals: hang, moe; excerpt: "Yeah, I've changed all this logic in the next PR." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2956802704)
- `2026-02-05T01:05:01Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @bnellnm, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/33049#issuecomment-3850520200)
- `2026-02-12T22:02:56Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @bnellnm, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/33049#issuecomment-3893637569)
- `2026-01-29T22:41:35Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:111; signals: moe; excerpt: "Could we get rid of FusedSharedMoE and instead pass the shared expert to forward impl? Then we could get rid of the ambiguity about ..." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2743842112)
- `2026-03-05T15:58:42Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:86; signals: moe; excerpt: "I like how we have split the forward impl and forward impl chunked That being said, it seems "wrong" that we would have this ..." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2890917158)
- `2026-03-05T17:59:23Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:86; signals: moe; excerpt: "Yeah, this is in a transient state. It's all reworked in one of the later PRs. In the follow up PRs the custom ops ..." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2891434459)
- `2026-03-18T22:58:12Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:790; signals: moe; excerpt: "I think we should be able to remove this. We now do not run inplace if the model has a shared expert." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2956697515)
- `2026-03-18T23:53:58Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:124; signals: moe; excerpt: "I believe this is no longer overlapped with the shared expert because it runs before the shared expert stream syncs with the main stream. ..." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2956918227)
- `2026-03-19T00:05:48Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:87; signals: moe; excerpt: "this maybe gate() cannot be called here it needs to run after the shared expert stream setup. maybe setup shared experts stream syncs the ..." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2956954879)
- `2026-01-29T22:30:08Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:250; signals: moe; excerpt: "note, we should be able to remove the TPU stuff soon" (https://github.com/vllm-project/vllm/pull/33049#discussion_r2743812486)
- `2026-01-29T22:50:41Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`:111; signals: moe; excerpt: "Yeah, I think that is doable." (https://github.com/vllm-project/vllm/pull/33049#discussion_r2743864668)
