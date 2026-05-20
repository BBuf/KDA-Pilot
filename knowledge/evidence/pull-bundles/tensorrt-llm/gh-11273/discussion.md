# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11273](https://github.com/NVIDIA/TensorRT-LLM/pull/11273)
- Source page: `sources/prs/tensorrt-llm/PR-11273.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11273`
- Generated at: `2026-05-20T15:17:42.544535+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-04T10:06:55Z`
- Merged: `2026-02-12T14:25:31Z`

## Discussion Counts

- Issue comments: 52
- Review submissions: 21 (approved=4, commented=17)
- Inline review comments: 21
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=12, outdated=10
- Human participants with discussion text: JadoTu, Wanli-Jiang, coderabbitai, nv-guomingz, tensorrt-cicd, yizhang-nv, yuantailing, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-06T08:47:09Z` `APPROVED` by `yizhang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3761604172)
- `2026-02-06T08:49:59Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 5 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3761613738)
- `2026-02-06T09:13:55Z` `COMMENTED` by `yuantailing` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3761713674)
- `2026-02-09T05:50:18Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771318945)
- `2026-02-09T05:51:54Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771323399)
- `2026-02-09T06:01:25Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771346431)
- `2026-02-09T07:30:59Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771620911)
- `2026-02-09T08:05:32Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771763662)
- `2026-02-09T08:20:45Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771828721)
- `2026-02-09T08:27:25Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771854202)
- `2026-02-09T08:46:55Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3771947590)
- `2026-02-10T05:05:18Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3776750316)
- `2026-02-10T05:05:23Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3776750483)
- `2026-02-10T05:05:29Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3776750659)
- `2026-02-10T05:05:35Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3776750886)
- `2026-02-10T05:05:38Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3776750985)
- `2026-02-10T06:54:41Z` `APPROVED` by `yuantailing` - LGTM to the Layer-wise Benchmarks changes. (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3777055534)
- `2026-02-10T07:41:57Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3777238355)
- `2026-02-10T08:21:57Z` `APPROVED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3777407070)
- `2026-02-12T06:13:18Z` `COMMENTED` by `JadoTu` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3773825676)
- `2026-02-12T06:25:18Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3788933123)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/models/modeling_nemotron_h.py`: 7 inline comment(s)
- `tensorrt_llm/_torch/modules/mlp.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/modules/rms_norm.py`: 3 inline comment(s)
- `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/thop/fusedActivationQuant.cpp`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/mamba/ssd_bmm.py`: 2 inline comment(s)
- `tests/unittest/_torch/modules/mamba/test_causal_conv1d.py`: 1 inline comment(s)
- `tests/unittest/_torch/modules/test_fused_activation_quant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-06T08:49:59Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, block, cache, compile, cuda, epilogue, fp4, hang; excerpt: "Actionable comments posted: 5 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#pullrequestreview-3761613738)
- `2026-02-06T08:49:54Z` `issue` by `coderabbitai`; signals: autotune, benchmark, bf16, block, correctness, cuda, dtype, fp4; excerpt: "📝 Walkthrough Walkthrough This pull request introduces CUDA kernel optimizations for causal convolution, implements fused ReLU-2 activation with FP4 quantization, extends layernorm kernels with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#issuecomment-3858863295)
- `2026-02-09T15:02:39Z` `inline` by `JadoTu` `tensorrt_llm/_torch/modules/mamba/ssd_bmm.py`:45; signals: autotune, hang, perf, regression, tensorrt, triton; excerpt: "See many changes of such original triton autotune hyperparameters. Does these changes of FLA initial settings work well in most cases? Will it bring ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2783137246)
- `2026-02-06T08:49:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/models/modeling_nemotron_h.py`:258; signals: fp4, moe, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Non-tuple Fp4QuantizedTensor input would crash at .view(). When hidden states is a bare Fp4QuantizedTensor (not wrapped in a tuple), ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2772986302)
- `2026-02-06T08:49:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/mlp.py`:138; signals: bf16, dtype, hang, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Hardcoded bfloat16 cast may silently change precision for float16 models. Line 132-133 unconditionally casts to bfloat16. The C++ backend ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2772986306)
- `2026-02-06T08:49:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/rms_norm.py`:152; signals: cute, fp4, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 5303 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2772986310)
- `2026-02-12T06:25:18Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/modules/mamba/ssd_bmm.py`:45; signals: hang, tensorrt, triton; excerpt: "this file is reverted to no change since no improvment is observed. For other triton cfg updates, I have checked with ISL=1k/8k/50k, all can ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2796980653)
- `2026-02-06T09:12:56Z` `inline` by `yuantailing` `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`:461; signals: benchmark, tensorrt; excerpt: "It doesn't work for models that does not accept the residual argument. Should update the condition of running into residual fusion == True branch." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2773070487)
- `2026-02-09T08:46:56Z` `inline` by `yuxianq` `cpp/tensorrt_llm/thop/fusedActivationQuant.cpp`:34; signals: kernel, tensorrt; excerpt: "Should we define invokeFusedRelu2Quantize in cpp/tensorrt llm/kernels/fusedActivationQuant.h instead?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2781354748)
- `2026-02-09T06:01:25Z` `inline` by `Wanli-Jiang` `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`:461; signals: benchmark, tensorrt; excerpt: "updated." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2780773107)
- `2026-02-09T08:20:45Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/rms_norm.py`:141; signals: block, tensorrt; excerpt: "We can simplify this code block like:" (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2781240465)
- `2026-02-06T08:49:57Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/mamba/test_causal_conv1d.py`:47; signals: benchmark; excerpt: "⚠️ Potential issue 🟡 Minor Duplicate assertion on Line 47. assert conv weight.shape[0] == dim is already checked on Line 44. Proposed fix 📝 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11273#discussion_r2772986313)
