# PR Discussion Digest

- Source PR: [vllm-project/vllm#16457](https://github.com/vllm-project/vllm/pull/16457)
- Source page: `sources/prs/vllm/PR-16457.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16457`
- Generated at: `2026-05-20T15:34:54.599516+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-11T06:15:11Z`
- Merged: `2025-04-25T06:52:28Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 14 (approved=1, commented=12, dismissed=1)
- Inline review comments: 16
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=5, outdated=6
- Human participants with discussion text: Isotr0py, cynthieye, jeejeelee, mergify, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-04-18T12:05:13Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2778403157)
- `2025-04-18T13:28:35Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2778584884)
- `2025-04-19T04:58:38Z` `DISMISSED` by `Isotr0py` - Overall LGTM now, just leave some nits. PTAL! (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2779857567)
- `2025-04-19T09:03:03Z` `COMMENTED` by `cynthieye` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2779918263)
- `2025-04-19T09:06:07Z` `COMMENTED` by `cynthieye` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2779918712)
- `2025-04-19T12:53:16Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2779956629)
- `2025-04-19T15:57:20Z` `COMMENTED` by `cynthieye` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2780013891)
- `2025-04-19T16:22:47Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2780024581)
- `2025-04-19T21:04:27Z` `COMMENTED` by `cynthieye` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2780092196)
- `2025-04-20T03:07:56Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2780134656)
- `2025-04-20T13:58:06Z` `COMMENTED` by `cynthieye` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2780252476)
- `2025-04-20T15:06:31Z` `COMMENTED` by `cynthieye` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2780266597)
- `2025-04-25T06:48:53Z` `COMMENTED` by `cynthieye` (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2793151145)
- `2025-04-25T06:51:58Z` `APPROVED` by `Isotr0py` - LGTM now, thanks for your patience! (https://github.com/vllm-project/vllm/pull/16457#pullrequestreview-2793156750)

## Inline Comment Hotspots

- `vllm/model_executor/layers/rotary_embedding.py`: 16 inline comment(s)

## High-Signal Discussion

- `2025-04-18T12:31:37Z` `issue` by `cynthieye`; signals: kernel, perf, performance, triton; excerpt: "apply rotary pos emb vision qwen2 vl.py qwen2.py @Isotr0py In qwen2-vl, the Qwen2Model of qwen2 will be called, and the rotary-embedding in Qwen2Model does ..." (https://github.com/vllm-project/vllm/pull/16457#issuecomment-2815356792)
- `2025-04-20T13:58:06Z` `inline` by `cynthieye` `vllm/model_executor/layers/rotary_embedding.py`:85; signals: attention, flash attention, triton; excerpt: "The file I want to copy/flash attention/flash attn/layers/rotary.py contains the following code from flash attn.ops.triton.rotary import apply rotary If I copy /flash-attention/flash-attn/layers/rotary.py to the ..." (https://github.com/vllm-project/vllm/pull/16457#discussion_r2051730937)
- `2025-04-18T11:58:44Z` `inline` by `Isotr0py` `vllm/model_executor/layers/rotary_embedding.py`:166; signals: kernel, triton; excerpt: "Why use triton kernel for forward native?" (https://github.com/vllm-project/vllm/pull/16457#discussion_r2050530085)
- `2025-04-18T11:57:01Z` `issue` by `Isotr0py`; signals: kernel, triton; excerpt: "Shouldn't this triton kernel have been used for Qwen2-VL?" (https://github.com/vllm-project/vllm/pull/16457#issuecomment-2815314369)
- `2025-04-19T16:22:47Z` `inline` by `Isotr0py` `vllm/model_executor/layers/rotary_embedding.py`:85; signals: kernel; excerpt: "Hmmm, seems vllm flash attn only ports the FA interface ( we might need to update the fork to include the rotary kernel... (But ..." (https://github.com/vllm-project/vllm/pull/16457#discussion_r2051520265)
- `2025-04-25T06:48:53Z` `inline` by `cynthieye` `vllm/model_executor/layers/rotary_embedding.py`:85; signals: hang; excerpt: "@Isotr0py hi，I have merged the changes to the flash attn repository. Can you help me review and merge this PR again" (https://github.com/vllm-project/vllm/pull/16457#discussion_r2059658574)
- `2025-04-18T12:02:08Z` `inline` by `Isotr0py` `vllm/model_executor/layers/rotary_embedding.py`:37; signals: kernel; excerpt: "Can't we use kernel from vllm flash attn?" (https://github.com/vllm-project/vllm/pull/16457#discussion_r2050532128)
- `2025-04-18T13:28:35Z` `inline` by `Isotr0py` `vllm/model_executor/layers/rotary_embedding.py`:85; signals: triton; excerpt: "Since triton is only available for Nvidia and ROCm GPUs, we can simplify the implementation here." (https://github.com/vllm-project/vllm/pull/16457#discussion_r2050630107)
- `2025-04-19T04:56:55Z` `inline` by `Isotr0py` `vllm/model_executor/layers/rotary_embedding.py`:325; signals: hang; excerpt: "This change is unnecessary for neuron now." (https://github.com/vllm-project/vllm/pull/16457#discussion_r2051388262)
- `2025-04-11T07:28:48Z` `issue` by `jeejeelee`; signals: kernel; excerpt: "Perhaps using kernel from would be more reasonable" (https://github.com/vllm-project/vllm/pull/16457#issuecomment-2796081279)
- `2025-04-19T09:03:03Z` `inline` by `cynthieye` `vllm/model_executor/layers/rotary_embedding.py`:85; signals: general review; excerpt: "hi，isotr0py，if I replace to Running the CI test will result in an error： [2025-04-19T08:53:45Z] ERROR 04-19 01:53:45 [core.py:386] File "/usr/local/lib/python3.12/dist-packages/vllm/model executor/models/qwen2.py", line 243, in ..." (https://github.com/vllm-project/vllm/pull/16457#discussion_r2051436128)
- `2025-04-19T12:53:16Z` `inline` by `Isotr0py` `vllm/model_executor/layers/rotary_embedding.py`:85; signals: general review; excerpt: "Oh, the import code should be vllm.vllm flash attn.layers.rotary import apply rotary emb, otherwise it won't work outside the repo folder. Qwen2-vl use original ..." (https://github.com/vllm-project/vllm/pull/16457#discussion_r2051470376)
