# PR Discussion Digest

- Source PR: [vllm-project/vllm#14071](https://github.com/vllm-project/vllm/pull/14071)
- Source page: `sources/prs/vllm/PR-14071.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14071`
- Generated at: `2026-05-20T15:34:17.028171+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-01T03:10:27Z`
- Merged: `2025-03-21T03:14:20Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 9 (approved=4, changes_requested=1, commented=4)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Isotr0py, ProExpertProg, SageMoore, WoosukKwon, hongxiayang, mergify, robertgshaw2-redhat, taoluo, tdoublep, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-02T00:15:51Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2652602459)
- `2025-03-02T00:16:03Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2652602482)
- `2025-03-03T02:48:08Z` `CHANGES_REQUESTED` by `WoosukKwon` - Hi @Isotr0py, thanks for the PR! Does Triton actually support T4? I think the support is discontinued: (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2652957377)
- `2025-03-05T05:33:21Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2659972808)
- `2025-03-18T18:04:18Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2695718041)
- `2025-03-18T22:12:30Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2696436737)
- `2025-03-18T22:34:04Z` `COMMENTED` by `WoosukKwon` - Ok.. I'm fine with this PR then. (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2696458050)
- `2025-03-20T19:47:45Z` `APPROVED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2703931734)
- `2025-03-20T20:45:27Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2704067835)

## Inline Comment Hotspots

- `vllm/platforms/cuda.py`: 3 inline comment(s)
- `vllm/platforms/rocm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-03-05T05:33:20Z` `inline` by `Isotr0py` `vllm/platforms/cuda.py`:201; signals: attention, benchmark, cuda, kernel, perf, performance, triton; excerpt: "but it would be really nice to have the option to ask vLLM to enable the TritonAttentionBackend when running even on newer NVIDIA GPUs. ..." (https://github.com/vllm-project/vllm/pull/14071#discussion_r1980724800)
- `2025-03-04T22:29:23Z` `issue` by `tdoublep`; signals: attention, benchmark, kernel, perf, performance, triton; excerpt: "I don't really have an opinion regarding how to handle older hardware, but it would be really nice to have the option to ask ..." (https://github.com/vllm-project/vllm/pull/14071#issuecomment-2699109025)
- `2025-03-03T18:46:50Z` `issue` by `Isotr0py`; signals: attention, kernel, perf, performance, triton; excerpt: "@WoosukKwon According to triton team's response ( old platform with FMA support code path is still maintained on main branch, though the MMA support ..." (https://github.com/vllm-project/vllm/pull/14071#issuecomment-2695262670)
- `2025-03-04T07:26:17Z` `issue` by `WoosukKwon`; signals: attention, blackwell, hopper, triton; excerpt: "Hi @Isotr0py, thanks for sharing the information. I think a compromise about this deprecation is only allowing user to specify VLLM ATTENTION BACKEND to ..." (https://github.com/vllm-project/vllm/pull/14071#issuecomment-2696462129)
- `2025-03-03T02:48:08Z` `review` `CHANGES_REQUESTED` by `WoosukKwon`; signals: triton; excerpt: "Hi @Isotr0py, thanks for the PR! Does Triton actually support T4? I think the support is discontinued:" (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2652957377)
- `2025-03-06T15:53:51Z` `issue` by `hongxiayang`; signals: attention, triton; excerpt: "Glad to see that ROCm's triton attention backend implementation is adopted to be used on NV GPUs. This PR looks ok to me. cc ..." (https://github.com/vllm-project/vllm/pull/14071#issuecomment-2704249408)
- `2025-03-13T14:48:16Z` `issue` by `SageMoore`; signals: kernel, triton; excerpt: "I also don't have an opinion on old hardware support but I do think it would be good to enable this backend on Nvidia ..." (https://github.com/vllm-project/vllm/pull/14071#issuecomment-2721531559)
- `2025-03-20T16:23:22Z` `issue` by `taoluo`; signals: dtype, memory; excerpt: "Hi, I tried this PR on V100, seems it can only support --dtype float32. The original --dtype half gives following errors. Given that V100 ..." (https://github.com/vllm-project/vllm/pull/14071#issuecomment-2741021887)
- `2025-03-18T22:31:59Z` `inline` by `WoosukKwon` `vllm/platforms/cuda.py`:219; signals: cuda; excerpt: "Why should we? I think people care about this log (although I really want to provide only one option per hardware)." (https://github.com/vllm-project/vllm/pull/14071#discussion_r2002117263)
- `2025-03-02T00:15:51Z` `inline` by `robertgshaw2-redhat` `vllm/platforms/cuda.py`:219; signals: cuda; excerpt: "I think we should move these logs to debug" (https://github.com/vllm-project/vllm/pull/14071#discussion_r1976512951)
- `2025-03-03T03:36:21Z` `issue` by `Isotr0py`; signals: triton; excerpt: "Hmm, at least they still kept the FMA fallback when deprecating MMAv1 on pre-Ampere GPUs. ( I also ran the prefix prefill tests and ..." (https://github.com/vllm-project/vllm/pull/14071#issuecomment-2693200604)
- `2025-03-18T22:34:04Z` `review` `COMMENTED` by `WoosukKwon`; signals: general review; excerpt: "Ok.. I'm fine with this PR then." (https://github.com/vllm-project/vllm/pull/14071#pullrequestreview-2696458050)
