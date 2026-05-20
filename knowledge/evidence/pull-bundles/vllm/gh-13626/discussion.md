# PR Discussion Digest

- Source PR: [vllm-project/vllm#13626](https://github.com/vllm-project/vllm/pull/13626)
- Source page: `sources/prs/vllm/PR-13626.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13626`
- Generated at: `2026-05-20T15:34:01.268360+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-20T19:02:24Z`
- Merged: `2025-02-27T23:28:08Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 22 (approved=1, commented=21)
- Inline review comments: 22
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: LiuXiaoxuanPKU, Neo9061, TianTengya, benchislett, luccafong, luyuzhe111, mergify, pyc96
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-02-24T02:33:03Z` `COMMENTED` by `luyuzhe111` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2635926969)
- `2025-02-24T02:35:47Z` `COMMENTED` by `luyuzhe111` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2635928434)
- `2025-02-24T02:47:02Z` `COMMENTED` by `luyuzhe111` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2635934400)
- `2025-02-24T16:37:14Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2637762283)
- `2025-02-24T16:37:16Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2637762633)
- `2025-02-24T18:46:24Z` `COMMENTED` by `luyuzhe111` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2638112014)
- `2025-02-24T19:32:58Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2638256773)
- `2025-02-24T22:17:13Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2638571156)
- `2025-02-25T05:58:23Z` `COMMENTED` by `luyuzhe111` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2639480855)
- `2025-02-25T17:52:55Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2641982565)
- `2025-02-25T19:34:38Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2642232279)
- `2025-02-25T19:50:31Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2642297148)
- `2025-02-25T19:54:22Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2642316202)
- `2025-02-25T20:38:06Z` `COMMENTED` by `luyuzhe111` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2642406646)
- `2025-02-25T22:04:39Z` `COMMENTED` by `pyc96` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2642572387)
- `2025-02-25T23:26:58Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2642687836)
- `2025-02-26T06:28:43Z` `COMMENTED` by `luyuzhe111` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2643229362)
- `2025-02-26T16:39:39Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2645146011)
- `2025-02-26T18:42:51Z` `APPROVED` by `LiuXiaoxuanPKU` - LGTM! Let's get this PR in first since it already brings some performance improvement. (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2641837385)
- `2025-02-27T06:48:38Z` `COMMENTED` by `pyc96` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2646773089)
- `2025-02-27T14:57:55Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2648069066)
- `2025-02-27T16:02:14Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/13626#pullrequestreview-2648299632)

## Inline Comment Hotspots

- `vllm/spec_decode/spec_decode_worker.py`: 11 inline comment(s)
- `vllm/spec_decode/multi_step_worker.py`: 9 inline comment(s)
- `vllm/config.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-02-26T16:39:39Z` `inline` by `benchislett` `vllm/spec_decode/spec_decode_worker.py`:187; signals: attention, flash attention, hang, mla; excerpt: "@pyc96 Yes, there is some special handling there and in a few other places. Right now multi-step is hard-coded in several ways to be ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1971953387)
- `2025-02-24T02:47:02Z` `inline` by `luyuzhe111` `vllm/spec_decode/multi_step_worker.py`; signals: attention, flash attention, mla; excerpt: "@benchislett another issue here is regarding a specific setting: draft tp = 1, and attention backend is not flash attention (mla, xformer). In this ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1966992500)
- `2025-02-24T16:37:16Z` `inline` by `benchislett` `vllm/spec_decode/multi_step_worker.py`; signals: attention, correctness, mla; excerpt: "I have refactored the snippet to the outside of the loop. As for the attention backend, there are a few solutions I see to ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1968014348)
- `2025-02-27T16:02:13Z` `inline` by `benchislett` `vllm/spec_decode/spec_decode_worker.py`:187; signals: block, hang, mla; excerpt: "@pyc96 I can confirm that it does seem to work with multi-step now. Even vllm/worker/multi step model runner.py seems to be successful with the ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1973891477)
- `2025-02-25T22:55:21Z` `issue` by `LiuXiaoxuanPKU`; signals: aligned, cache, kv cache; excerpt: "Hi @benchislett, sorry for the delay here. I was thinking through the implementation on a more high level. I list my understanding below and ..." (https://github.com/vllm-project/vllm/pull/13626#issuecomment-2683476289)
- `2025-02-25T23:28:05Z` `issue` by `luccafong`; signals: aligned, cache, kv cache; excerpt: "Hi @benchislett, sorry for the delay here. I was thinking through the implementation on a more high level. I list my understanding below and ..." (https://github.com/vllm-project/vllm/pull/13626#issuecomment-2683519895)
- `2025-02-24T18:46:24Z` `inline` by `luyuzhe111` `vllm/spec_decode/multi_step_worker.py`; signals: cuda, cute; excerpt: "Thanks again for your great work! Regarding returning the hidden states, I think we might be able to simplify it a bit more? Do ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1968225647)
- `2025-02-25T19:34:38Z` `inline` by `benchislett` `vllm/spec_decode/spec_decode_worker.py`:187; signals: hang, mla; excerpt: "@luccafong I don't think that TP1DraftModelRunner should be used at all for MTP. Since the advance-step is not compatible with the MLA backend, it ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1970416161)
- `2025-02-25T22:04:39Z` `inline` by `pyc96` `vllm/spec_decode/spec_decode_worker.py`:187; signals: hang, mla; excerpt: "Since the advance-step is not compatible with the MLA backend, it isn't going to work for k 1 without some significant changes. Hi @benchislett ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1970607884)
- `2025-02-25T23:26:57Z` `inline` by `luccafong` `vllm/spec_decode/spec_decode_worker.py`:187; signals: benchmark, memory; excerpt: "@luccafong QQ: does TP1DraftModelRunner work when the draft model has TP=8? If not, then this PR also has the benefit of greatly relieving the ..." (https://github.com/vllm-project/vllm/pull/13626#discussion_r1970681841)
- `2025-02-26T15:20:08Z` `issue` by `benchislett`; signals: cache, kv cache; excerpt: "That's right. This PR is just to reuse the same module for k 1, so the KV cache is handled the same as an ..." (https://github.com/vllm-project/vllm/pull/13626#issuecomment-2685388015)
- `2025-02-26T20:28:25Z` `issue` by `luyuzhe111`; signals: attention, tma; excerpt: "@LiuXiaoxuanPKU since you were sharing the diagrams, I want to use this thread to point out that the current handling of the first token ..." (https://github.com/vllm-project/vllm/pull/13626#issuecomment-2686119694)
