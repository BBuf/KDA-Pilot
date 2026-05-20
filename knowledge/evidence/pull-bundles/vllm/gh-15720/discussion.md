# PR Discussion Digest

- Source PR: [vllm-project/vllm#15720](https://github.com/vllm-project/vllm/pull/15720)
- Source page: `sources/prs/vllm/PR-15720.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-15720`
- Generated at: `2026-05-20T15:34:39.248230+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-28T19:01:41Z`
- Merged: `2025-04-03T02:48:00Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 20 (approved=2, commented=18)
- Inline review comments: 20
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: ProExpertProg, maleksan85, mgoin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-31T21:26:08Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2730542400)
- `2025-03-31T21:26:30Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2730543033)
- `2025-03-31T21:27:03Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2730543911)
- `2025-03-31T21:27:23Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2730544645)
- `2025-04-01T17:43:29Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2733565945)
- `2025-04-01T20:22:46Z` `COMMENTED` by `ProExpertProg` - So if I understand correctly, this adds support for chunked prefill to the existing ROCm custom Paged Attention, ... (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2733925850)
- `2025-04-01T22:37:30Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734182215)
- `2025-04-02T03:02:23Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734549734)
- `2025-04-02T03:19:05Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734563269)
- `2025-04-02T03:23:59Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734567235)
- `2025-04-02T03:32:29Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734574177)
- `2025-04-02T03:32:57Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734574562)
- `2025-04-02T03:35:40Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734577252)
- `2025-04-02T03:38:26Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734579474)
- `2025-04-02T04:00:30Z` `APPROVED` by `ProExpertProg` - CPP looks good to me, very contained and straightforward change 😃 (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2734598416)
- `2025-04-02T09:29:03Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2735577394)
- `2025-04-02T15:55:32Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2736818893)
- `2025-04-02T15:57:25Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2736825997)
- `2025-04-02T15:59:21Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2736832646)
- `2025-04-03T02:47:59Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2738215691)

## Inline Comment Hotspots

- `vllm/attention/ops/paged_attn.py`: 6 inline comment(s)
- `vllm/attention/ops/chunked_prefill_paged_decode.py`: 5 inline comment(s)
- `vllm/attention/backends/rocm_flash_attn.py`: 4 inline comment(s)
- `csrc/rocm/attention.cu`: 3 inline comment(s)
- `vllm/_custom_ops.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-01T17:43:29Z` `inline` by `maleksan85` `vllm/attention/ops/chunked_prefill_paged_decode.py`:39; signals: attention, block, triton; excerpt: "as per suggestion from Triton team do: offset = tl.make range(0, BLOCK M).to(tl.int64); instead, to have computation in int64/uint64" (https://github.com/vllm-project/vllm/pull/15720#discussion_r2023387261)
- `2025-04-02T03:19:05Z` `inline` by `robertgshaw2-redhat` `vllm/attention/backends/rocm_flash_attn.py`:833; signals: attention, kernel, perf; excerpt: "I think we should do query start loc = None then pass query start loc here and add a comment about how for V0 ..." (https://github.com/vllm-project/vllm/pull/15720#discussion_r2024007114)
- `2025-04-02T03:35:39Z` `inline` by `maleksan85` `vllm/attention/ops/paged_attn.py`:34; signals: attention, kernel, memory; excerpt: "I believe it is better to ask about authors :) However my guess is that this kernel allocates many partitions (as per partition size) ..." (https://github.com/vllm-project/vllm/pull/15720#discussion_r2024016498)
- `2025-04-01T20:22:46Z` `review` `COMMENTED` by `ProExpertProg`; signals: attention, kernel; excerpt: "So if I understand correctly, this adds support for chunked prefill to the existing ROCm custom Paged Attention, and then for prefill we still ..." (https://github.com/vllm-project/vllm/pull/15720#pullrequestreview-2733925850)
- `2025-04-02T03:23:59Z` `inline` by `maleksan85` `vllm/attention/backends/rocm_flash_attn.py`:833; signals: attention, perf, performance; excerpt: "This is good idea. However lets keep performance of chunked prefill in V0 in separate PR." (https://github.com/vllm-project/vllm/pull/15720#discussion_r2024009943)
- `2025-04-01T21:32:18Z` `issue` by `maleksan85`; signals: attention, kernel, triton; excerpt: "So if I understand correctly, this adds support for chunked prefill to the existing ROCm custom Paged Attention, and then for prefill we still ..." (https://github.com/vllm-project/vllm/pull/15720#issuecomment-2770734528)
- `2025-04-02T03:38:26Z` `inline` by `maleksan85` `vllm/attention/ops/paged_attn.py`:32; signals: attention, fp8; excerpt: "well, it will depend on demand. I mean there is another implementation on V0 that could also be ported to V1 and for FP8 ..." (https://github.com/vllm-project/vllm/pull/15720#discussion_r2024017943)
- `2025-03-31T21:26:08Z` `inline` by `maleksan85` `vllm/attention/ops/chunked_prefill_paged_decode.py`:39; signals: attention; excerpt: "it was done to make computation of offsets correct when seq len is like 16k. find a way to keep int64 and constexpr at ..." (https://github.com/vllm-project/vllm/pull/15720#discussion_r2021787307)
- `2025-04-02T09:28:51Z` `inline` by `mgoin` `vllm/attention/ops/paged_attn.py`:27; signals: attention; excerpt: "Could you get this information from vllm/platforms/rocm.py? Perhaps get device name() can achieve this. Either way this functionality should be kept there in the ..." (https://github.com/vllm-project/vllm/pull/15720#discussion_r2024451682)
- `2025-04-02T09:28:59Z` `inline` by `mgoin` `vllm/attention/backends/rocm_flash_attn.py`:833; signals: attention; excerpt: "+1 for the first ask. It is pretty opaque to just pass in a nameless None, at least give it a variable name or ..." (https://github.com/vllm-project/vllm/pull/15720#discussion_r2024451901)
- `2025-04-02T15:55:32Z` `inline` by `maleksan85` `csrc/rocm/attention.cu`:389; signals: attention; excerpt: "should this be conversion similar to what static cast provides? I mean when assignment happens to int64 t from int?" (https://github.com/vllm-project/vllm/pull/15720#discussion_r2025142969)
- `2025-03-31T21:26:30Z` `inline` by `maleksan85` `vllm/attention/ops/chunked_prefill_paged_decode.py`:373; signals: attention; excerpt: "share with rocm flash attn.py" (https://github.com/vllm-project/vllm/pull/15720#discussion_r2021787755)
