# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1117](https://github.com/flashinfer-ai/flashinfer/pull/1117)
- Source page: `sources/prs/flashinfer/PR-1117.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1117`
- Generated at: `2026-05-20T15:21:45.388237+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-06T01:46:46Z`
- Merged: `2025-06-10T22:02:10Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 11
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: Edenzzzz, yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-06T02:01:31Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2903552436)
- `2025-06-06T02:12:15Z` `COMMENTED` by `yzh119` - Thank you so much for doing this! Yes adding pdl support for attention kernels is a good feature ... (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2903573410)
- `2025-06-06T02:17:09Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2903587391)
- `2025-06-06T20:26:46Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2906080295)
- `2025-06-06T21:06:10Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2906145523)
- `2025-06-06T22:33:33Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2906290633)
- `2025-06-09T15:14:32Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2910397445)
- `2025-06-09T16:02:09Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2910531655)
- `2025-06-09T18:40:25Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2910966471)
- `2025-06-09T18:58:36Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2911010150)
- `2025-06-10T19:53:06Z` `APPROVED` by `yzh119` - LGTM, thanks for the contribution! (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2914874732)

## Inline Comment Hotspots

- `aot_build_utils/generate_batch_paged_decode_inst.py`: 5 inline comment(s)
- `csrc/batch_prefill.cu`: 2 inline comment(s)
- `flashinfer/decode.py`: 2 inline comment(s)
- `csrc/batch_decode_mla_config.jinja`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-06T02:12:15Z` `review` `COMMENTED` by `yzh119`; signals: attention, kernel; excerpt: "Thank you so much for doing this! Yes adding pdl support for attention kernels is a good feature to have, leave some comments for ..." (https://github.com/flashinfer-ai/flashinfer/pull/1117#pullrequestreview-2903573410)
- `2025-06-09T18:40:25Z` `inline` by `Edenzzzz` `csrc/batch_decode_mla_config.jinja`:6; signals: cutlass, layout, mla; excerpt: "Could it have been one of the Layout classes defined in cutlass?" (https://github.com/flashinfer-ai/flashinfer/pull/1117#discussion_r2136261961)
- `2025-06-09T16:02:09Z` `inline` by `yzh119` `flashinfer/decode.py`:1590; signals: flashinfer, mla; excerpt: "Firstly, this function is designed for sm80, and doesn't support pdl, actually the mla interface flashinfer exposed to user is from not from here." (https://github.com/flashinfer-ai/flashinfer/pull/1117#discussion_r2136000042)
- `2025-06-09T06:30:47Z` `issue` by `yzh119`; signals: flashinfer, layout; excerpt: "Hi @Edenzzzz , should fix the issue, but to be honest I don't understand how there could be a name conflict when we using ..." (https://github.com/flashinfer-ai/flashinfer/pull/1117#issuecomment-2954787466)
- `2025-06-09T21:32:52Z` `issue` by `Edenzzzz`; signals: cuda, hopper; excerpt: "I'm still thinking about how to expose enable pdl interface at python to user. The current idea in my mind is: 1. Making it ..." (https://github.com/flashinfer-ai/flashinfer/pull/1117#issuecomment-2957087490)
- `2025-06-09T21:40:35Z` `issue` by `yzh119`; signals: cuda, hopper; excerpt: "Sure let's do this and pass torch.cuda.current device() into device support pdl? I encourage using the input tensor's device (some user might operate tensors ..." (https://github.com/flashinfer-ai/flashinfer/pull/1117#issuecomment-2957101136)
- `2025-06-06T20:26:46Z` `inline` by `Edenzzzz` `aot_build_utils/generate_batch_paged_decode_inst.py`:43; signals: sm90; excerpt: "In this case, we will need to add the enable pdl flag for also the sm90 templates to simplify the call from wrappers?" (https://github.com/flashinfer-ai/flashinfer/pull/1117#discussion_r2132869486)
- `2025-06-06T02:01:31Z` `inline` by `Edenzzzz` `csrc/batch_prefill.cu`:39; signals: compile; excerpt: "not sure if we should remove the flag and let the compiler decide." (https://github.com/flashinfer-ai/flashinfer/pull/1117#discussion_r2131329074)
- `2025-06-09T15:14:32Z` `inline` by `Edenzzzz` `flashinfer/decode.py`:1590; signals: flashinfer; excerpt: "enable this by default?" (https://github.com/flashinfer-ai/flashinfer/pull/1117#discussion_r2135918542)
- `2025-06-09T18:58:36Z` `inline` by `yzh119` `csrc/batch_decode_mla_config.jinja`:6; signals: mla; excerpt: "hmmmm that might be possible, good point." (https://github.com/flashinfer-ai/flashinfer/pull/1117#discussion_r2136290868)
- `2025-06-06T22:39:01Z` `issue` by `Edenzzzz`; signals: mla; excerpt: "@yzh119 Precision for decode and prefill has passed. However I encountered this when running mla decode test. I didn't modify any headers. Could you ..." (https://github.com/flashinfer-ai/flashinfer/pull/1117#issuecomment-2951081164)
- `2025-06-09T19:47:01Z` `issue` by `yzh119`; signals: hopper; excerpt: "I still prefer making it None by default, then determining its value inside function, for following reasons: 1. if we are working on an ..." (https://github.com/flashinfer-ai/flashinfer/pull/1117#issuecomment-2956826438)
