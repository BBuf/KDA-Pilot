# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13410](https://github.com/NVIDIA/TensorRT-LLM/pull/13410)
- Source page: `sources/prs/tensorrt-llm/PR-13410.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13410`
- Generated at: `2026-05-20T15:18:42.381923+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-24T05:55:36Z`
- Merged: `2026-05-06T14:25:36Z`

## Discussion Counts

- Issue comments: 47
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 16
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: PerkzZheng, coderabbitai, heyuhhh, juney-nvidia, liji-nv, pengbowang-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T06:11:07Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4168269193)
- `2026-04-24T07:59:48Z` `COMMENTED` by `pengbowang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4168894708)
- `2026-04-24T08:24:40Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4169035113)
- `2026-04-24T08:25:48Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4169041893)
- `2026-04-27T03:32:51Z` `COMMENTED` by `pengbowang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4178021665)
- `2026-04-27T03:36:35Z` `COMMENTED` by `pengbowang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4178027636)
- `2026-04-27T03:37:52Z` `COMMENTED` by `pengbowang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4178029678)
- `2026-04-27T04:53:33Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4178215693)
- `2026-04-27T04:53:55Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4178217458)
- `2026-04-28T02:51:41Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4185499174)
- `2026-04-28T07:11:17Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4186564665)
- `2026-04-28T07:11:26Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4186565379)
- `2026-04-30T08:16:09Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4203521033)
- `2026-04-30T08:18:26Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4203533215)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`: 6 inline comment(s)
- `cpp/tensorrt_llm/common/attentionOp.cpp`: 5 inline comment(s)
- `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`: 5 inline comment(s)

## High-Signal Discussion

- `2026-04-24T06:11:07Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#pullrequestreview-4168269193)
- `2026-04-24T07:59:43Z` `inline` by `pengbowang-nv` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:269; signals: autotune, hang, kernel, tensorrt; excerpt: "A different issue: setting this value here will have no effect on kernel selection. We should fix it later. (Which will require change the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3136286497)
- `2026-04-27T03:37:52Z` `inline` by `pengbowang-nv` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:269; signals: autotune, hang, kernel, tensorrt; excerpt: "You don't have to change this part of code for now, since currently in autotuner we don't respect this flag." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3144761283)
- `2026-04-28T02:51:28Z` `inline` by `PerkzZheng` `cpp/tensorrt_llm/common/attentionOp.cpp`:848; signals: attention, bf16, fp8, tensorrt; excerpt: "size should be 2 since we already use bf16 for accumulation even though it is fp8 kv. Add comments here." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3151282237)
- `2026-04-24T06:11:03Z` `issue` by `coderabbitai`; signals: attention, hang, kernel, tensorrt; excerpt: "📝 Walkthrough Walkthrough Adds MultiCtasKv sparse attention support to FMHA kernels by introducing optional device pointers for scratch buffers and per-CTA counters. Extends the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#issuecomment-4311076255)
- `2026-04-24T06:11:06Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/common/attentionOp.cpp`:849; signals: attention, oom, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Gate MultiCtasKv scratch allocation by FMHA enablement. The scratch pool is allocated when useTllmGenSparseAttention() is true, but it is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3135789980)
- `2026-04-24T08:24:40Z` `inline` by `heyuhhh` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`:284; signals: hang, kernel, tensorrt; excerpt: "Maybe change it to options.mMultiCtasKvMode != tensorrt llm::kernels::MultiCtasKvMode::Disabled is better?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3136409717)
- `2026-04-27T03:36:35Z` `inline` by `pengbowang-nv` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:269; signals: hang, kernel, tensorrt; excerpt: "1. FORCE DETERMINISTIC env var may change the enable/disable of multiCtasKV mode. At least on it should be true to XQA. 2. Also you ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3144759056)
- `2026-04-24T08:25:48Z` `inline` by `heyuhhh` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:269; signals: kernel, tensorrt; excerpt: "I didn't get it. I just keep this like what did in xqaDispatcher. Could you provide more informations about here?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3136414801)
- `2026-04-27T04:53:32Z` `inline` by `heyuhhh` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:269; signals: kernel, tensorrt; excerpt: "We use generation kernels even in context phase for sparse kernels, so here just to align with generation. We only enable mMultiCtasKvMode when using ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3144936220)
- `2026-04-28T07:11:17Z` `inline` by `heyuhhh` `cpp/tensorrt_llm/common/attentionOp.cpp`:844; signals: attention, tensorrt; excerpt: "It makes sense. Thanks for pointing it out! I have fixed it. However, the generation phase has the same issues i think. Should we ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3152197046)
- `2026-04-24T07:58:15Z` `inline` by `pengbowang-nv` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`:284; signals: kernel, tensorrt; excerpt: "We also have GmemReductionWithSeparateKernel." (https://github.com/NVIDIA/TensorRT-LLM/pull/13410#discussion_r3136279689)
