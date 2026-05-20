# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1025](https://github.com/Dao-AILab/flash-attention/pull/1025)
- Source page: `sources/prs/flash-attention/PR-1025.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1025`
- Generated at: `2026-05-20T15:16:26.753984+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-07-03T19:39:49Z`
- Merged: `2024-07-08T18:24:48Z`

## Discussion Counts

- Issue comments: 39
- Review submissions: 3 (commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Narsil, Oxi84, Ph0rk0z, Shreya-Pathak, foreverlms, iamsaurabhgupt, lucidrains, tridao, turboderp
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 11

## Review Decisions

- No review submissions were returned by GitHub.

## Inline Comment Hotspots

- `flash_attn/flash_attn_interface.py`: 3 inline comment(s)

## High-Signal Discussion

- `2024-07-04T06:57:37Z` `issue` by `tridao`; signals: attention, gemm, tma; excerpt: "Sorry I missed the tanh. The step should be S = gemm(Q, K), then S = tanh(softmax scale 1 / softcap), then masking, taking ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2208252644)
- `2024-07-05T15:12:10Z` `issue` by `Narsil`; signals: gemm, hang, tma; excerpt: "Hi @Shreya-Pathak, I looked at your changes. Personally I prefer the single flag (less things to know for users, and softcapping is unlikely to ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2211046942)
- `2024-07-05T17:33:30Z` `issue` by `Shreya-Pathak`; signals: failing, hang, tma; excerpt: "@Narsil I think I have also done what Tri mentioned with the softcap / softmax scale and from a brief look at your code, ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2211194117)
- `2024-07-03T19:46:36Z` `issue` by `tridao`; signals: gemm, tma; excerpt: "I think softcapping should be done before the masking. i.e. the sequence is gemm, softcapping, masking, then softmax. If you do softcapping after masking, ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2207085160)
- `2024-07-03T19:50:13Z` `issue` by `tridao`; signals: gemm, tma; excerpt: "softcapping can be fused with dividing by softmax scale. i.e. we do S = gemm(Q, K), then S = softmax scale 1 / softcap ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2207095410)
- `2024-07-04T14:18:51Z` `issue` by `Narsil`; signals: gemm, tma; excerpt: "Ok I put the template for Is softcapping, however I cannot get your idea working. I may be missing something. My understandling is that ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2209111566)
- `2024-07-04T15:15:34Z` `issue` by `Narsil`; signals: gemm, tma; excerpt: "My understanding is that scales softmax log2 is only ever used in the partial exponentiation (the log2 is to use exp2f which I assume ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2209213223)
- `2024-07-04T16:34:09Z` `issue` by `lucidrains`; signals: gemm, hang; excerpt: "@Narsil oh yea, your code looks way better than what i have lmao, let's just go with your changes so eventually you'll have to ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2209325874)
- `2024-07-04T17:58:09Z` `issue` by `lucidrains`; signals: cute, hang; excerpt: "@Narsil yea, it is really hard to contribute with these compilation times. how fast were you able to get the times down to? i'm ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2209412183)
- `2024-07-05T08:38:52Z` `issue` by `Narsil`; signals: hang, kernel; excerpt: "@lucidrains Can't see your changes anywhere, are you on a branch somewhere ? I got compilation times down to 1mn but results seems wrong ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2210451057)
- `2024-07-05T12:08:04Z` `issue` by `lucidrains`; signals: cute, hang; excerpt: "@Narsil nice, i got it to around the same ballpark! unfortunately was working off a runpod that went down before i can push the ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2210761282)
- `2024-07-05T12:39:16Z` `issue` by `Narsil`; signals: cuda, hang; excerpt: "Nice doing the backward ! You're saying this branch is supposed to work ? Can I try your branch ? (My local changes were ..." (https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2210806641)
