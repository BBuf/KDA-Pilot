# PR Discussion Digest

- Source PR: [vllm-project/vllm#19067](https://github.com/vllm-project/vllm/pull/19067)
- Source page: `sources/prs/vllm/PR-19067.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19067`
- Generated at: `2026-05-20T15:35:23.921427+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-03T08:28:52Z`
- Merged: `2025-07-01T08:12:19Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 24 (approved=2, commented=22)
- Inline review comments: 25
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=8, outdated=9
- Human participants with discussion text: DarkLight1337, ProExpertProg, houseroad, mergify, tjtanaa, tywuAMD
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-03T09:12:35Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2891433720)
- `2025-06-03T10:17:07Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2891671048)
- `2025-06-07T01:50:16Z` `COMMENTED` by `ProExpertProg` - Could you please move the Triton code into the Triton backend? (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2906558769)
- `2025-06-07T01:51:22Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2906562498)
- `2025-06-09T13:25:18Z` `COMMENTED` by `ProExpertProg` - This is a good change but I think it could be slightly cleaner! (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2910062194)
- `2025-06-10T01:06:24Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2911710679)
- `2025-06-10T01:11:12Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2911714987)
- `2025-06-10T04:26:19Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2911920175)
- `2025-06-10T04:26:57Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2911920977)
- `2025-06-10T12:27:51Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2913350978)
- `2025-06-10T12:41:29Z` `COMMENTED` by `houseroad` - Thanks for the contribution, could you rebase the PR and address the comments? (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2913396818)
- `2025-06-11T07:35:12Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2915987849)
- `2025-06-11T07:35:59Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2915990338)
- `2025-06-11T07:36:37Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2915992354)
- `2025-06-11T13:58:53Z` `COMMENTED` by `houseroad` - Overall looks fine. One question about why do we need to switch to triton flash attention for rocm ... (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2917329808)
- `2025-06-12T00:38:31Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2919040914)
- `2025-06-16T20:22:34Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2933403595)
- `2025-06-16T20:24:29Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2933408560)
- `2025-06-16T20:28:38Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2933419812)
- `2025-06-19T08:20:04Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2942059407)
- `2025-06-29T23:45:14Z` `COMMENTED` by `tywuAMD` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2969589475)
- `2025-06-30T20:49:05Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2972651230)
- `2025-06-30T20:49:16Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2972652112)
- `2025-07-01T08:12:13Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2974106434)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/triton_mla.py`: 18 inline comment(s)
- `vllm/v1/attention/backends/mla/common.py`: 7 inline comment(s)

## High-Signal Discussion

- `2025-06-12T00:38:31Z` `inline` by `tywuAMD` `vllm/v1/attention/backends/mla/triton_mla.py`:122; signals: attention, mla, perf, tma, triton; excerpt: "shall we just directly pass False to return softmax lse? Just realize return softmax lse never got used in the helper function; thus I ..." (https://github.com/vllm-project/vllm/pull/19067#discussion_r2141311071)
- `2025-06-07T01:51:22Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/mla/common.py`:666; signals: attention, mla, tma, triton; excerpt: "(if return softmax lse=True and Triton can't handle the request, super().varlen fwd(...) can be used)" (https://github.com/vllm-project/vllm/pull/19067#discussion_r2133190073)
- `2025-06-10T04:26:13Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/mla/triton_mla.py`:110; signals: attention, mla, tma, triton; excerpt: "Wait, so why can't we always use triton if it can return the softmax lse? Or is that different from encoded softmax?" (https://github.com/vllm-project/vllm/pull/19067#discussion_r2136883805)
- `2025-06-11T07:35:12Z` `inline` by `tywuAMD` `vllm/v1/attention/backends/mla/triton_mla.py`:110; signals: attention, mla, tma, triton; excerpt: "I went through Triton's implementation, and it turns out that RETURN ENCODED SOFTMAX is always False so the output encoded softmax is always None." (https://github.com/vllm-project/vllm/pull/19067#discussion_r2139424970)
- `2025-06-11T13:58:24Z` `inline` by `houseroad` `vllm/v1/attention/backends/mla/triton_mla.py`:122; signals: attention, mla, perf, triton; excerpt: "Also wondering hwy do we need to use triton flash attn in this case? Is the perf better or something else?" (https://github.com/vllm-project/vllm/pull/19067#discussion_r2140263189)
- `2025-06-16T20:22:34Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/mla/triton_mla.py`:110; signals: attention, mla, tma, triton; excerpt: "This is on V0, and I don't think you really answered my question. triton attention outputs a tuple, and the second element is the ..." (https://github.com/vllm-project/vllm/pull/19067#discussion_r2150807161)
- `2025-06-16T20:28:38Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/mla/triton_mla.py`:110; signals: attention, mla, tma, triton; excerpt: "Never mind, I see the linked op is used. Could we not modify it though so that return encoded softmax is passed through successfully?" (https://github.com/vllm-project/vllm/pull/19067#discussion_r2150818869)
- `2025-06-19T08:20:04Z` `inline` by `tywuAMD` `vllm/v1/attention/backends/mla/triton_mla.py`:110; signals: attention, mla, tma, triton; excerpt: "I kept tracing the call stack and it seems like the encoded softmax is not fully ready, and that might be the reason why ..." (https://github.com/vllm-project/vllm/pull/19067#discussion_r2156432289)
- `2025-06-29T23:45:14Z` `inline` by `tywuAMD` `vllm/v1/attention/backends/mla/triton_mla.py`:116; signals: attention, mla, tma, triton; excerpt: "Hi @ProExpertProg, not sure if you saw my if you don't have any further comments. Meanwhile I will keep investigating return softmax lse and ..." (https://github.com/vllm-project/vllm/pull/19067#discussion_r2174005972)
- `2025-06-11T13:55:33Z` `inline` by `houseroad` `vllm/v1/attention/backends/mla/triton_mla.py`:122; signals: attention, mla, tma, triton; excerpt: "shall we just directly pass False to return softmax lse?" (https://github.com/vllm-project/vllm/pull/19067#discussion_r2140251817)
- `2025-06-11T13:58:53Z` `review` `COMMENTED` by `houseroad`; signals: attention, flash attention, triton; excerpt: "Overall looks fine. One question about why do we need to switch to triton flash attention for rocm case?" (https://github.com/vllm-project/vllm/pull/19067#pullrequestreview-2917329808)
- `2025-06-16T20:24:29Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/mla/triton_mla.py`:116; signals: attention, mla, tma, triton; excerpt: "Why can't we use this path if return softmax lse is True?" (https://github.com/vllm-project/vllm/pull/19067#discussion_r2150810662)
