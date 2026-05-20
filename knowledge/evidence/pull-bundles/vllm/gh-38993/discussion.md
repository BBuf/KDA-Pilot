# PR Discussion Digest

- Source PR: [vllm-project/vllm#38993](https://github.com/vllm-project/vllm/pull/38993)
- Source page: `sources/prs/vllm/PR-38993.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38993`
- Generated at: `2026-05-20T15:40:40.509741+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-04T19:11:02Z`
- Merged: `2026-04-05T14:54:31Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: robertgshaw2-redhat, wzhao18
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-04T19:13:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for DeepSeek FP8 block-scale weights in the FlashInfer TRT-LLM MoE kernel, ... (https://github.com/vllm-project/vllm/pull/38993#pullrequestreview-4058773394)
- `2026-04-04T19:28:26Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/38993#pullrequestreview-4058783142)
- `2026-04-04T19:32:08Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/38993#pullrequestreview-4058785561)
- `2026-04-04T20:29:00Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/38993#pullrequestreview-4058823803)
- `2026-04-04T20:29:22Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/38993#pullrequestreview-4058824009)

## Inline Comment Hotspots

- `vllm/model_executor/warmup/deep_gemm_warmup.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-04T19:32:08Z` `inline` by `wzhao18` `vllm/model_executor/warmup/deep_gemm_warmup.py`:171; signals: gemm, hang, layout, moe; excerpt: "fused moe grouped gemm may use deep gemm returns True despite trtllm MoE is used. In this warmup call, it has an assertion on ..." (https://github.com/vllm-project/vllm/pull/38993#discussion_r3035957589)
- `2026-04-04T19:29:04Z` `issue` by `robertgshaw2-redhat`; signals: deepgemm, gemm; excerpt: "nice find. why does the deepgemm warmup get touched?" (https://github.com/vllm-project/vllm/pull/38993#issuecomment-4187622798)
- `2026-04-04T19:28:26Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/warmup/deep_gemm_warmup.py`:171; signals: gemm; excerpt: "just wondering why this is touched?" (https://github.com/vllm-project/vllm/pull/38993#discussion_r3035954075)
- `2026-04-04T20:29:00Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/warmup/deep_gemm_warmup.py`:171; signals: gemm; excerpt: "nice, I wonder if we have been doing additonal warmup accidentally 🫣" (https://github.com/vllm-project/vllm/pull/38993#discussion_r3036013840)
