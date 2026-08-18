# SGLang kernel tasks for NVIDIA's kernel agents (KDA 1.5 / CAKE)

Ten kernel optimization tasks cut from SGLang and SGLang-diffusion, each with the
real serving workload behind it. Two folders, split by what the agent is being
asked to do:

* [`kda15/`](kda15/) - **there is a shipped kernel and we want it beaten.** Frozen
  production shapes, the copied SGLang baseline, real captured tensors, a
  correctness gate. Five tasks (A1-A5).
* [`cake/`](cake/) - **there is no drop-in baseline.** A kernel has to be designed
  (or a vendor kernel is losing and needs to be fixed). Five tasks (C1-C4, B2).

Read [`docs/measurement_contract.md`](docs/measurement_contract.md) first - it is
the acceptance criterion, and it is stricter than "faster in isolation" for
reasons we paid for.

## The tasks

| id | task | model | kernel(s) | measured share | workload data |
| --- | --- | --- | --- | --- | --- |
| A1 | [Mamba-2 SSM chunk scan + causal conv1d](kda15/A1_nemotron3_nano__mamba2_ssm) | NVIDIA Nemotron-3-Nano-30B-A3B-FP8 | Triton `ssd_*` + `causal_conv1d_*` | **55.8%** of serving GPU time | 123 rows, 9 ops, 16-step real state chain |
| A2 | [Triton unified attention](kda15/A2_glm47_flash__triton_attention) | GLM-4.7-Flash | `decode_attention_fwd`, `extend_attention_fwd` | **75.3%** | 58 rows, 4 ops |
| A3 | [DSA sparse attention](kda15/A3_dsv4_flash__dsa_sparse_attention) | DeepSeek-V4-Flash | indexer quant / top-k / compress | 576k+195k+189k real calls | 59 rows, 6 ops |
| A4 | [Triton fused MoE](kda15/A4_triton_fused_moe) | LFM2.5-8B-A1B (+ GLM-4.7-Flash) | `invoke_fused_moe_kernel` | **50.5%** / 30.4% | 11 rows + real routing tensors |
| A5 | [GDN chunk prefill + recurrent decode](kda15/A5_qwen3_next__gdn_prefill) | Qwen3-Next-80B-A3B | FLA `chunk_*`, `fused_recurrent_*`, `kda.*` | 1152 real calls/group on the chunk path | see task |
| C1 | [New sm_103 sub-block BSA kernel](cake/C1_sm103_subblock_bsa) | MiniMax-H3 | block-sparse attention forward | sparse arm is the only backend beating cache-only on B300 (10.37 s vs 11.16 s) | dense reference shapes + deadlock forensics |
| C2 | [FA4 CuTe loses to cuDNN on diffusion shapes](cake/C2_diffusion_attention_fa4_vs_cudnn) | Wan2.2-TI2V-5B, MiniMax-H3 | FA4 CuTe forward | attention is 48-70% of a denoise step; cuDNN wins 1.24-1.98x on 11 real shapes | captured shapes from both models |
| C3 | [Video VAE conv3d + GroupNorm/SiLU](cake/C3_video_vae_conv3d_groupnorm) | Qwen-Image / FLUX.2 / Hunyuan VAEs | `causal_conv3d_cat_pad`, `group_norm_silu` | our fused kernels are already 2.06x / 2.31x; layout change is worth ~3x more | entry points identified, shapes to capture (see task) |
| C4 | [Sol-Attn on sm_103 + sparse dense-fallback](cake/C4_solattn_sm103_and_sparse_fallback) | MiniMax-H3 | sparse backend + fallback path | audio-tower step 44 -> 191 ms under the sparse backend eats most of the win | captured audio/video tower shapes |
| B2 | [Fused DiT gate+residual+norm+shift/scale](cake/B2_dit_gate_resid_norm_modulate) | Wan2.2, Qwen-Image, Z-Image, H3 | `fused_ln_modulate` family | 1-4% of a step - **lowest priority, say so if you skip it** | 4 rows, real shapes |

## What every task carries

```
prompt.md                    the task card: target, evidence, gate, deliverable
config.json                  model, ops, environment, benchmark defaults
baseline/                    the shipped SGLang implementation, copied verbatim
                             (SOURCES.txt lists the files and the commit)
bench/workloads.json         frozen call signatures + real-traffic call counts
bench/tensors/               real inputs / outputs / state chains (where shipped)
docs/profile_evidence.md     what fired, how often, at which shapes
docs/capture_provenance.md   exact serving command, capture matrix, GSM8K accuracy
solution/                    empty - the candidate goes here
```

## How the workloads were produced

Every model was served with **its SGLang cookbook command** on 8x B300 SXM6
(sm_103), then walked through a fixed matrix of operating points - random 1k/1k at
concurrency 1/16/256, a prefill-heavy 4k/512 point, ShareGPT at concurrency 32,
and **real GSM8K** at 5-shot serial, 5-shot 32-way, 16-shot 16-way, plus a
100-200 question accuracy run. The accuracy of that very run is recorded per task
(e.g. DeepSeek-V4-Flash **0.980**, GLM-4.7-Flash **0.820**, Nemotron-3-Nano and
LFM2.5 in their provenance files), so the shapes are demonstrably from a
correctly serving model.

Two capture-only modifiers and the reason for each, plus the
shapes-with-radix-cache-on / tensors-with-radix-cache-off split, are documented in
[`docs/workload_capture.md`](docs/workload_capture.md). The capture tooling is in
[`tools/`](tools/) and regenerates everything:

```bash
# 1. serve with the cookbook command + the capture hook
PYTHONPATH=tools NVCAP_DIR=cap/<slug> NVCAP_CONFIG=tools/targets/<task>.json \
    python -m sglang.launch_server <cookbook args> --disable-cuda-graph
# 2. walk the operating-point matrix (labels the capture groups)
bash workloads.sh cfg_<slug>.sh shapes
# 3. merge per-process manifests and select the workload rows
python tools/merge_manifests.py cap/<slug>
python tools/build_workloads.py --manifest cap/<slug>/shape_manifest.json \
    --out <task>/bench/workloads.json --top 10
```

## Contracts

| doc | what it fixes |
| --- | --- |
| [`docs/measurement_contract.md`](docs/measurement_contract.md) | how a win is measured: CUDA-graph timing, interleaved A/B, ncu inflation, the microbenchmark traps that produced wrong answers here, noise floors |
| [`docs/anti_hack_contract.md`](docs/anti_hack_contract.md) | why synthetic Gaussian inputs let three specific shortcuts pass, and the chained final-state gate that catches them |
| [`docs/baseline_policy.md`](docs/baseline_policy.md) | baseline = the shipped SGLang kernel at a pinned commit, never a naive PyTorch reference |
| [`docs/workload_capture.md`](docs/workload_capture.md) | provenance of every shape, and warmup vs real traffic |

## What we deliberately did not ask for

* **Communication kernels and the TRT-LLM fused-MoE path** - your ground, and our
  profiles exclude them by construction.
* **More elementwise fusion in diffusion** - we swept the ecosystem for this in
  August and concluded SGLang is already at the frontier; our elementwise kernels
  sit at 70-88% of achievable bandwidth, and the whole remaining elementwise
  residue is 1-4% of a step. B2 is the one exception, and it is explicitly the
  lowest-priority task here.
* **Programmatic Dependent Launch in diffusion** - measured ceiling below 0.5% of
  step time at these kernel granularities.
* **Kernels that are dead on the recommended path.** A3's evidence section names
  the DSA entry points that fired 0 times on the cookbook B300 recipe; please do
  not spend cycles there.

Everything in here is reproducible from the tooling in `tools/` plus the command
in each task's `docs/capture_provenance.md`. If a number looks wrong, that is the
path to check it.
