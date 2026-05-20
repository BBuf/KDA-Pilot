# PR Discussion Digest

- Source PR: [vllm-project/vllm#31542](https://github.com/vllm-project/vllm/pull/31542)
- Source page: `sources/prs/vllm/PR-31542.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31542`
- Generated at: `2026-05-20T15:39:23.642261+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-30T18:57:51Z`
- Merged: `2026-01-05T22:52:59Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 9 (approved=2, commented=7)
- Inline review comments: 10
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=0, outdated=5
- Human participants with discussion text: AndreasKaratzas, mergify, mgoin, robertgshaw2-redhat, tjtanaa, zyongye
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-30T19:00:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the UnquantizedFusedMoEMethod to better support different MoE backends, including AITer for ROCm ... (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3619027334)
- `2025-12-30T19:23:14Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the UnquantizedFusedMoEMethod to better support different MoE kernels like AiterExperts and FlashInferExperts ... (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3619088654)
- `2026-01-02T22:25:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the ROCm AITer MoE implementation to use the new modular kernel format, ... (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3623978578)
- `2026-01-02T22:45:09Z` `COMMENTED` by `AndreasKaratzas` - Are the lm eval tests still passing with aiter? Also may I ask, is it easy/possible to also ... (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3623999080)
- `2026-01-02T22:56:49Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3624020591)
- `2026-01-04T22:32:44Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3625201657)
- `2026-01-05T05:58:52Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3625576485)
- `2026-01-05T19:24:50Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3628144109)
- `2026-01-05T22:52:37Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3628665616)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`: 10 inline comment(s)

## High-Signal Discussion

- `2026-01-02T22:56:48Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`:248; signals: cuda, cutlass, flashinfer, moe; excerpt: "Is this check useful for any other platform than ROCm? I'm genuinely curious so feel free to answer "I don't know" if you are ..." (https://github.com/vllm-project/vllm/pull/31542#discussion_r2658509958)
- `2026-01-02T22:55:48Z` `issue` by `zyongye`; signals: bf16, fp8, hang, moe; excerpt: "Are the lm eval tests still passing with aiter? Also may I ask, is it easy/possible to also eval DeepSeek on this, or this ..." (https://github.com/vllm-project/vllm/pull/31542#issuecomment-3706425279)
- `2026-01-05T05:58:52Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`:259; signals: hang, moe; excerpt: "I am not familiar with the MoEPrepareAndFinalizeNoEP abstraction, However AITER supports EP. So can you also validate this PR changes when EP is enabled?" (https://github.com/vllm-project/vllm/pull/31542#discussion_r2660370948)
- `2026-01-05T19:24:50Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`:259; signals: kernel, moe; excerpt: "This is used for TP. MoEPrepareAndFinalizeNoEP is a wrapper saying that there's no EP communication involved in this secanrio. Since ModularKernel is mainly created ..." (https://github.com/vllm-project/vllm/pull/31542#discussion_r2662565463)
- `2026-01-02T22:45:09Z` `review` `COMMENTED` by `AndreasKaratzas`; signals: hang; excerpt: "Are the lm eval tests still passing with aiter? Also may I ask, is it easy/possible to also eval DeepSeek on this, or this ..." (https://github.com/vllm-project/vllm/pull/31542#pullrequestreview-3623999080)
- `2026-01-02T18:51:20Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @zyongye, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31542#issuecomment-3706024026)
- `2026-01-04T22:28:33Z` `issue` by `AndreasKaratzas`; signals: benchmark, hang; excerpt: "Test gsm8k eval before and after the change Launch command VLLM ROCM USE AITER=1 vllm serve Qwen/Qwen3-30B-A3B -tp 1 Benchmark command Before this PR: ..." (https://github.com/vllm-project/vllm/pull/31542#issuecomment-3708483604)
- `2026-01-02T22:40:39Z` `inline` by `AndreasKaratzas` `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`:248; signals: moe; excerpt: "Is this check useful for any other platform than ROCm? I'm genuinely curious so feel free to answer "I don't know" if you are ..." (https://github.com/vllm-project/vllm/pull/31542#discussion_r2658496645)
- `2026-01-02T23:01:41Z` `issue` by `AndreasKaratzas`; signals: hang; excerpt: "I don't have AMD GPU in my hand so I kinda just use CI to see if this change breaks anything. Are there any ..." (https://github.com/vllm-project/vllm/pull/31542#issuecomment-3706435346)
- `2026-01-02T23:11:29Z` `issue` by `zyongye`; signals: hang; excerpt: "I don't have AMD GPU in my hand so I kinda just use CI to see if this change breaks anything. Are there any ..." (https://github.com/vllm-project/vllm/pull/31542#issuecomment-3706453955)
- `2026-01-02T23:45:45Z` `issue` by `AndreasKaratzas`; signals: hang; excerpt: "I don't have AMD GPU in my hand so I kinda just use CI to see if this change breaks anything. Are there any ..." (https://github.com/vllm-project/vllm/pull/31542#issuecomment-3706485673)
- `2026-01-02T22:57:43Z` `issue` by `zyongye`; signals: hang; excerpt: "I don't have AMD GPU in my hand so I kinda just use CI to see if this change breaks anything." (https://github.com/vllm-project/vllm/pull/31542#issuecomment-3706429622)
