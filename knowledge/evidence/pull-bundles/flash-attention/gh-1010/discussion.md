# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1010](https://github.com/Dao-AILab/flash-attention/pull/1010)
- Source page: `sources/prs/flash-attention/PR-1010.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1010`
- Generated at: `2026-05-20T15:16:26.747709+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-06-26T19:00:51Z`
- Merged: `2024-07-23T04:34:37Z`

## Discussion Counts

- Issue comments: 32
- Review submissions: 0 (no states)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Bellk17, deke997, ehartford, foreverlms, hackey, larrysingh, linchen111, minzhezhou, poyenc, rocking5566, tomasikp, tridao, yiakwy-xpu-ml-framework-team
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 11

## Review Decisions

- No review submissions were returned by GitHub.

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2024-07-14T10:56:38Z` `issue` by `minzhezhou`; signals: attention, block, kernel, memory, pipeline, tile; excerpt: "I also have an error when compiling for 7900xtx (gfx1100). Write, does flash-attention support this card? They don't support it yet, native should mean ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2227302316)
- `2024-07-12T13:08:29Z` `issue` by `minzhezhou`; signals: attention, bf16, kernel, memory, tile; excerpt: "I got this error during the build fmha bwd d128 fp16 batch for gfx1100: /root/code/flash-attention/csrc/composable kernel/include/ck tile/core/arch/generic memory space atomic hip.hpp:66:19: error: static assertion ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2225557002)
- `2024-07-03T18:28:08Z` `issue` by `ehartford`; signals: attention, compile, cuda, hang; excerpt: "hi @rocking5566 I get this error when I try to install this. 1) I clone main 2) I get the remote and merge it ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2206951913)
- `2024-07-04T00:34:29Z` `issue` by `ehartford`; signals: attention, flash attention; excerpt: "Thank you, running python setup.py worked. I will run a full build tonight using flash attention and verify that it's working" (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2207669915)
- `2024-07-16T22:49:46Z` `issue` by `ehartford`; signals: attention, flash attention; excerpt: "I tried this on a known good configuration, using TRL I am able to run it without flash attention, and I am able to ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2231945727)
- `2024-07-14T09:31:46Z` `issue` by `hackey`; signals: attention; excerpt: "I also have an error when compiling for 7900xtx (gfx1100). Write, does flash-attention support this card?" (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2227280895)
- `2024-07-17T07:47:42Z` `issue` by `poyenc`; signals: block; excerpt: "@minzhezhou Thanks for your time. We only support mi200 & mi300 at this time. Thus we put gfx90a / gfx94x in the allowed archs ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2232653688)
- `2024-07-17T10:58:40Z` `issue` by `minzhezhou`; signals: block; excerpt: "@minzhezhou Thanks for your time. We only support mi200 & mi300 at this time. Thus we put gfx90a / gfx94x in the allowed archs ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2233027047)
- `2024-07-18T08:38:23Z` `issue` by `poyenc`; signals: attention; excerpt: "Hi @poyenc, thanks for the reminder. Do you mean it is technically impossible to make it work for navi or it is not on ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2235949521)
- `2024-06-28T19:17:38Z` `issue` by `ehartford`; signals: hang; excerpt: "@tridao I would be very happy to see this change!" (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2197492165)
- `2024-07-03T19:09:46Z` `issue` by `rocking5566`; signals: general review; excerpt: "@ehartford Thank for you valuable comment. About compiling the code for Rocm, You can try python setup.py install This is work for me. I ..." (https://github.com/Dao-AILab/flash-attention/pull/1010#issuecomment-2207009873)
