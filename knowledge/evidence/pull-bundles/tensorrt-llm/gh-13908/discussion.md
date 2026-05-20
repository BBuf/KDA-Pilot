# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13908](https://github.com/NVIDIA/TensorRT-LLM/pull/13908)
- Source page: `sources/prs/tensorrt-llm/PR-13908.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13908`
- Generated at: `2026-05-20T15:18:58.003940+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-08T13:01:09Z`
- Merged: `2026-05-11T01:10:36Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 5 (approved=4, commented=1)
- Inline review comments: 10
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=10
- Human participants with discussion text: Barry-Delaney, QiJune, coderabbitai, leslie-fang25, lfr-0531, tensorrt-cicd, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-08T13:11:11Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#pullrequestreview-4252457598)
- `2026-05-09T03:16:05Z` `APPROVED` by `leslie-fang25` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#pullrequestreview-4256552945)
- `2026-05-09T05:30:50Z` `APPROVED` by `Barry-Delaney` (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#pullrequestreview-4256930400)
- `2026-05-09T10:08:26Z` `APPROVED` by `lfr-0531` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#pullrequestreview-4257570936)
- `2026-05-11T01:10:33Z` `APPROVED` by `QiJune` (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#pullrequestreview-4260220465)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/mega_moe/mega_moe_deepgemm.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/moe_scheduler.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/quantization.py`: 2 inline comment(s)
- `tests/unittest/_torch/modules/moe/test_moe_module.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/MOE_DEVELOPER_GUIDE.md`: 1 inline comment(s)
- `tests/integration/test_lists/test-db/l0_dgx_b300.yml`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-08T13:11:05Z` `issue` by `coderabbitai`; signals: alignment, autotune, b200, bf16, compile, cute, deepgemm, dtype; excerpt: "[ Summary --- --- Interface & Scheduler Contracts tensorrt llm/ torch/modules/fused moe/interface.py Introduces MoESchedulerKind enum with EXTERNAL COMM and FUSED COMM values, adds scheduler ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#issuecomment-4406666135)
- `2026-05-08T13:11:11Z` `review` `COMMENTED` by `coderabbitai`; signals: b200, deepgemm, gemm, hang, moe, tensorrt; excerpt: "Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#pullrequestreview-4252457598)
- `2026-05-08T13:11:08Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/mega_moe/mega_moe_deepgemm.py`:178; signals: cutlass, deepgemm, gemm, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Reject non-distributed environments in can implement(). create moe.get moe cls() now relies on can implement() for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860921)
- `2026-05-08T13:11:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/moe_scheduler.py`:257; signals: deepgemm, gemm, latency, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Mirror the DeepEPLowLatency workspace formula in the multi-chunk DeepGemm path. prepare workspace deepgemm() sizes single-chunk workspaces ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860943)
- `2026-05-08T13:11:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:4916; signals: cache, fp4, moe, mxfp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🏗️ Heavy lift Invalidate or replace the one-shot t l1 / t l2 cache. transform main weights() becomes a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860960)
- `2026-05-08T13:11:08Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/mega_moe/mega_moe_deepgemm.py`:204; signals: deepgemm, gemm, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Don't silently ignore activation type. create moe backend() passes activation type, but this backend never maps ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860929)
- `2026-05-08T13:11:08Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/MOE_DEVELOPER_GUIDE.md`:67; signals: kernel, moe, perf, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Document the fused-comm EPLB AllReduce path the same way the code implements it. These sections currently ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860934)
- `2026-05-08T13:11:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:4725; signals: block, hang, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Fix the hanging indents here before Flake8 blocks the PR. These copy () calls currently trip ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860951)
- `2026-05-08T13:11:09Z` `inline` by `coderabbitai` `tests/integration/test_lists/test-db/l0_dgx_b300.yml`:44; signals: deepgemm, gemm, hang, moe; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Add the MegaMoE EPLB selector to the B300 post-merge matrix. These entries only exercise the new ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860964)
- `2026-05-08T13:11:09Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/moe/test_moe_module.py`:125; signals: cute, moe, race, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🏗️ Heavy lift 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1230 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860968)
- `2026-05-08T13:11:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/moe_scheduler.py`:94; signals: failing, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Rewrite the abstract forward() declaration so lint passes. Flake8 is already flagging this one-line abstractmethod body ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860939)
- `2026-05-08T13:11:09Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/moe/test_moe_module.py`:142; signals: cute, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 2213 --- Destroy the default ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13908#discussion_r3208860974)
