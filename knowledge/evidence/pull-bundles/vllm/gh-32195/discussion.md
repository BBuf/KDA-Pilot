# PR Discussion Digest

- Source PR: [vllm-project/vllm#32195](https://github.com/vllm-project/vllm/pull/32195)
- Source page: `sources/prs/vllm/PR-32195.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-32195`
- Generated at: `2026-05-20T15:39:26.192424+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-12T17:23:12Z`
- Merged: `2026-03-01T02:55:25Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 36 (approved=1, commented=35)
- Inline review comments: 46
- Review threads observed: 17
- Resolved/outdated thread markers: resolved=11, outdated=9
- Human participants with discussion text: RunkaiTao, cursor, dcmaddix, gnovack, jeejeelee, mergify, varun-sundar-rabindranath, xyang16
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-12T17:24:43Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for TMA (Tensor Memory Accelerator) descriptors in the fused moe lora ... (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3651879380)
- `2026-01-12T17:53:17Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3651986075)
- `2026-01-12T17:54:18Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3651989188)
- `2026-01-12T20:16:09Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3652594592)
- `2026-01-13T18:46:59Z` `COMMENTED` by `dcmaddix` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3657303983)
- `2026-01-13T18:47:26Z` `COMMENTED` by `dcmaddix` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3657306001)
- `2026-01-20T18:22:32Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3683673279)
- `2026-01-20T18:23:11Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3683676855)
- `2026-01-20T18:23:41Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3683678764)
- `2026-01-20T18:25:05Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3683683498)
- `2026-01-23T19:40:44Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3699285815)
- `2026-01-27T00:50:11Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3708653819)
- `2026-01-31T03:30:55Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3731353378)
- `2026-02-03T05:46:46Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3743092879)
- `2026-02-03T05:54:42Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3743124080)
- `2026-02-11T17:06:39Z` `COMMENTED` by `RunkaiTao` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3786127439)
- `2026-02-18T21:32:46Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3822345359)
- `2026-02-21T05:08:39Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3835056705)
- `2026-02-21T22:57:40Z` `COMMENTED` by `varun-sundar-rabindranath` - Thanks for the work @gnovack - Nice speed up 🙌 . Left some comments - PTAL! (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3835058048)
- `2026-02-23T05:55:26Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3839264868)
- `2026-02-23T14:25:03Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3841351713)
- `2026-02-23T20:21:43Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3843325760)
- `2026-02-23T22:01:27Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3843753020)
- `2026-02-23T23:55:16Z` `COMMENTED` by `gnovack` (https://github.com/vllm-project/vllm/pull/32195#pullrequestreview-3844186625)
- ... 12 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`: 43 inline comment(s)
- `tests/lora/test_olmoe_tp.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-02-21T22:34:27Z` `inline` by `varun-sundar-rabindranath` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:767; signals: block, cache, kernel, moe, tma, triton; excerpt: "Question about intermediate cache shape. Focusing on the use tma and sorted tokens ids != None case IIUC, this is an intermediate tensor to ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2836751137)
- `2026-01-12T20:16:10Z` `inline` by `cursor` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:555; signals: memory, moe, perf, tma, triton; excerpt: "Buffer size mismatch when EM not divisible by top k num Medium Severity When EM is not perfectly divisible by top k num, there's ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2683774574)
- `2026-02-03T05:46:46Z` `inline` by `gnovack` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:295; signals: cuda, kernel, moe, tma, triton; excerpt: "Main currently has 2 calls to tl.extra.cuda.gdc wait() (one within the loop over k and one before the loop). I don't think we need ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2757309433)
- `2026-02-24T16:56:03Z` `inline` by `gnovack` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:380; signals: block, hang, moe, tma, triton; excerpt: "I took a quick stab at this, but it ended up looking a bit messier when these were factored out. Mostly because different sets ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2848381526)
- `2026-01-12T20:16:10Z` `inline` by `cursor` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:857; signals: moe, register, tma, triton; excerpt: "Fake implementations missing new use tma parameter High Severity The fused moe lora shrink fake and fused moe lora expand fake functions are missing ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2683774573)
- `2026-02-03T05:54:42Z` `inline` by `gnovack` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:587; signals: kernel, moe, tma, triton; excerpt: "We could implement this as a pre-run hook, but I think that might be a bit messier / more fragile, since it would require ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2757328893)
- `2026-02-21T05:50:39Z` `inline` by `varun-sundar-rabindranath` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:726; signals: memory, moe, tma, triton; excerpt: "why isn't this no longer M ? I think it should still be M for the non-tma case so we don't allocate extra memory ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2835874035)
- `2026-02-21T22:44:36Z` `inline` by `varun-sundar-rabindranath` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:767; signals: kernel, moe, tma, triton; excerpt: "I was a bit confused by the cdiv and top k num but I believe this is to play well with how the strides ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2836762475)
- `2026-02-21T22:56:18Z` `inline` by `varun-sundar-rabindranath` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:226; signals: kernel, moe, tma, triton; excerpt: "can you add a comment describing the various combinations possible with use tma - IIUC, a desc b desc sort c comment -- -- ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2836782611)
- `2026-02-23T22:01:27Z` `inline` by `gnovack` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:120; signals: kernel, moe, tma, triton; excerpt: "Yes, technically it would be possible to implement this as more of a temporary override within a context manager; however, this would require reaching ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2843300377)
- `2026-02-23T23:55:16Z` `inline` by `gnovack` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:767; signals: cache, moe, tma, triton; excerpt: "Great point. Originally, I was trying to just use one consistent cache shape (regardless of whether TMA was enabled or not). To address [the ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2843690598)
- `2026-02-25T03:30:07Z` `inline` by `varun-sundar-rabindranath` `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`:120; signals: kernel, moe, tma, triton; excerpt: "Thanks for researching this @gnovack . I was generally worried that it'd affect another kernel in the same forward pass. It looks like everytime ..." (https://github.com/vllm-project/vllm/pull/32195#discussion_r2850619138)
