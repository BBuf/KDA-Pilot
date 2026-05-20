# PR Discussion Digest

- Source PR: [vllm-project/vllm#12528](https://github.com/vllm-project/vllm/pull/12528)
- Source page: `sources/prs/vllm/PR-12528.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12528`
- Generated at: `2026-05-20T15:33:43.578241+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-28T21:13:21Z`
- Merged: `2025-01-31T07:49:37Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 27
- Review threads observed: 19
- Resolved/outdated thread markers: resolved=12, outdated=13
- Human participants with discussion text: LucasWilkinson, WoosukKwon, mergify, mgoin, simon-mo, tlrmchlsmth, zhuohan123
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-01-28T21:23:35Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2579440098)
- `2025-01-30T03:45:13Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2582843810)
- `2025-01-30T03:48:54Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2582859639)
- `2025-01-30T03:53:40Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2582862593)
- `2025-01-30T05:36:32Z` `APPROVED` by `zhuohan123` - Thanks for the work! Left some comments on API aesthetics. I haven't look too details into the kernel ... (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2582877566)
- `2025-01-30T05:48:17Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2582966394)
- `2025-01-30T07:01:48Z` `COMMENTED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2583062725)
- `2025-01-30T13:57:09Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2583983213)
- `2025-01-30T14:09:13Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2584015247)
- `2025-01-30T14:14:38Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2584030149)
- `2025-01-30T15:24:24Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2584228584)
- `2025-01-30T19:38:47Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2584862065)

## Inline Comment Hotspots

- `vllm/attention/backends/mla/utils.py`: 6 inline comment(s)
- `vllm/config.py`: 4 inline comment(s)
- `vllm/engine/arg_utils.py`: 4 inline comment(s)
- `vllm/envs.py`: 3 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 2 inline comment(s)
- `vllm/attention/ops/triton_decode_attention.py`: 2 inline comment(s)
- `vllm/attention/selector.py`: 2 inline comment(s)
- `vllm/attention/layer.py`: 2 inline comment(s)
- `vllm/platforms/rocm.py`: 1 inline comment(s)
- `vllm/attention/backends/abstract.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-01-30T03:32:30Z` `inline` by `mgoin` `vllm/envs.py`:307; signals: hang, mla, perf; excerpt: "Could we remove the environment variable if we have it defined in arg utils.py? nit: change this to VLLM MLA DISABLE and move it ..." (https://github.com/vllm-project/vllm/pull/12528#discussion_r1934960691)
- `2025-01-30T14:09:12Z` `inline` by `LucasWilkinson` `vllm/attention/layer.py`:47; signals: attention, compile, mla; excerpt: "this forwards extra args to the attention impl since for MLA we need to pass in things like q proj, kv b proj, rotary ..." (https://github.com/vllm-project/vllm/pull/12528#discussion_r1935675993)
- `2025-01-30T03:53:39Z` `inline` by `LucasWilkinson` `vllm/attention/backends/mla/utils.py`:240; signals: attention, fp8, mla; excerpt: "don't we have to for V3? since its FP8?" (https://github.com/vllm-project/vllm/pull/12528#discussion_r1934971039)
- `2025-01-31T07:47:40Z` `issue` by `simon-mo`; signals: attention, failing, hang; excerpt: "@LucasWilkinson the following test is failing and I skipped it Error This is might be that when the model quantized, attention process weight is ..." (https://github.com/vllm-project/vllm/pull/12528#issuecomment-2626505625)
- `2025-01-30T03:43:24Z` `inline` by `mgoin` `vllm/attention/backends/mla/utils.py`:240; signals: attention, mla; excerpt: "I think we can't deal with kv b proj being quantized, so we might just want to enforce no quantization here. Need to understand ..." (https://github.com/vllm-project/vllm/pull/12528#discussion_r1934966323)
- `2025-01-30T05:48:17Z` `inline` by `WoosukKwon` `vllm/attention/ops/triton_decode_attention.py`:426; signals: attention, triton; excerpt: "I think it's OK to keep it? I wanted to minimize the diff from the original file, so that we can update it easily ..." (https://github.com/vllm-project/vllm/pull/12528#discussion_r1935037292)
- `2025-01-30T13:57:09Z` `inline` by `LucasWilkinson` `vllm/attention/selector.py`:86; signals: attention, mla; excerpt: "hmmm what would that look like? We turn this on when we detect it's a Deepseek model automatically, so are you purposing the code ..." (https://github.com/vllm-project/vllm/pull/12528#discussion_r1935657179)
- `2025-01-30T03:30:51Z` `inline` by `mgoin` `vllm/platforms/rocm.py`:80; signals: kernel, triton; excerpt: "The triton kernel in theory should work on rocm too, but we should leave this as a follow-up item" (https://github.com/vllm-project/vllm/pull/12528#discussion_r1934959652)
- `2025-01-30T04:13:36Z` `inline` by `zhuohan123` `vllm/attention/ops/triton_decode_attention.py`:426; signals: attention, triton; excerpt: "Do we wanna keep these AMD flags @WoosukKwon?" (https://github.com/vllm-project/vllm/pull/12528#discussion_r1934980621)
- `2025-01-30T05:14:01Z` `inline` by `zhuohan123` `vllm/attention/backends/abstract.py`:273; signals: attention, mla; excerpt: "Should we have a class MLAAttentionImpl(AttentionImpl)?" (https://github.com/vllm-project/vllm/pull/12528#discussion_r1935014982)
- `2025-01-30T05:14:49Z` `inline` by `zhuohan123` `vllm/attention/backends/mla/utils.py`:21; signals: attention, mla; excerpt: "This comment is incomplete" (https://github.com/vllm-project/vllm/pull/12528#discussion_r1935015389)
- `2025-01-30T05:36:32Z` `review` `APPROVED` by `zhuohan123`; signals: kernel, mla; excerpt: "Thanks for the work! Left some comments on API aesthetics. I haven't look too details into the kernel and the exact mla implementation. Will ..." (https://github.com/vllm-project/vllm/pull/12528#pullrequestreview-2582877566)
