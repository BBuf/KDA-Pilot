# SGLang kernel tasks for NVIDIA's kernel agents

Eight kernel optimization tasks cut from SGLang and SGLang-diffusion, each with the
real serving workload behind it: frozen production shapes with their real-traffic
call counts, the copied SGLang baseline, real captured tensors where they fit, and a
correctness gate.

Read [`docs/measurement_contract.md`](docs/measurement_contract.md) first - it is
the acceptance criterion, and it is stricter than "faster in isolation" for reasons
we paid for.

## The tasks

| task | model | kernel(s) | measured share | workload data |
| --- | --- | --- | --- | --- |
| [`nemotron3_nano__mamba2_ssm`](nemotron3_nano__mamba2_ssm) | NVIDIA Nemotron-3-Nano-30B-A3B-FP8 | Triton `ssd_*` chunk pipeline + `causal_conv1d_*` | **55.8%** of serving GPU time | 123 rows / 9 ops + a verified 16-step real state chain |
| [`glm47_flash__triton_attention`](glm47_flash__triton_attention) | GLM-4.7-Flash | `decode_attention_fwd`, `extend_attention_fwd` | **75.3%** (Qwen3-Next runs the same kernels at 6.39%) | 86 rows / 3 ops, 15 MB real tensors |
| [`deepseek_v4_flash__dsa_sparse_attention`](deepseek_v4_flash__dsa_sparse_attention) | DeepSeek-V4-Flash | whole DSA chain: compress -> q-indexer -> **deep_gemm logits** -> top-k -> **flash_mla sparse core**, plus the **mHC TileLang** kernels | front end **8.46%** aggregate, sparse core **7.50%**, mHC **8.06%** of serving GPU time | 111 rows / 12 ops, 35 MB real tensors |
| [`lfm25__triton_fused_moe`](lfm25__triton_fused_moe) | LFM2.5-8B-A1B (+ GLM-4.7-Flash) | `invoke_fused_moe_kernel` and friends | **50.5%** / 30.4% | 19 rows, two expert geometries + real routing tensors |
| [`qwen3_next__gdn_chunk_prefill`](qwen3_next__gdn_chunk_prefill) | Qwen3-Next-80B-A3B | FLA chunk prefill + **`TritonGDNKernel.packed_decode`** | decode kernel **3.56%** of GPU time; GDN family 4.39% | 46 rows, **2 verified 16-step state chains** |
| [`minimax_h3__sm103_block_sparse_attention`](minimax_h3__sm103_block_sparse_attention) | MiniMax-H3 | **write a new** sm_103 sub-block block-sparse forward | the sparse arm is the only backend beating cache-only on B300 (10.37 s vs 11.16 s) | dense reference shapes + deadlock forensics |
| [`diffusion__attention_backend_fa4_vs_cudnn`](diffusion__attention_backend_fa4_vs_cudnn) | Wan2.2-TI2V-5B, MiniMax-H3 | FA4 CuTe vs cuDNN SDPA dispatch | measured tonight: FA4 **wins** 4-5% on long shapes, **loses 1.24x** at 24-26 tokens | 16 rows + 2 measured timing tables |
| [`minimax_h3__sparse_backend_fallback`](minimax_h3__sparse_backend_fallback) | MiniMax-H3 | sparse backend selection + its dense fallback | audio-tower step 44 -> 191 ms under the sparse backend eats most of the win | 8 rows, both towers |

The first five have a shipped SGLang kernel that a candidate has to beat; the last
three need a kernel designed (or a vendor kernel fixed) because there is no drop-in
baseline that wins today.

[`SHAPES.md`](SHAPES.md) lists the shape family of every op in every task in one place
(regenerate with `python tools/dump_shapes.py > SHAPES.md`).
[`docs/profiles/`](docs/profiles) holds the raw per-kernel GPU-time tables the shares
above come from.

## Running a task

```bash
python tools/check_task.py <task>        # is the package complete? (CPU only, doubles as CI)
python tools/bench_harness.py <task>     # baseline-only timing, per row
# ...write solution/entry.py with the same OPS keys...
python tools/bench_harness.py <task> --json report.json    # interleaved A/B + gates
```

`tools/bench_harness.py` implements the measurement contract so each agent does not have
to re-derive it: CUDA-graph timing, interleaved arms, preallocated outputs, `copy_` restore
for in-place kernels with the restore cost subtracted, correctness before performance, and
for state-carrying kernels the chained final-state gate. `tools/verify_state_chain.py`
proves a shipped chain actually chains; `tools/check_hacks.py` prints the statistics that
let a synthetic-Gaussian verifier be fooled.

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
concurrency 1/16/256, a prefill-heavy 4k/512 point, ShareGPT at concurrency 32, and
**real GSM8K** at 5-shot serial, 5-shot 32-way, 16-shot 16-way, plus a 100-200
question accuracy run. The accuracy of that very run is recorded per task
(DeepSeek-V4-Flash **0.980**, Qwen3-Next **1.000**, GLM-4.7-Flash **0.820**, and so
on), so the shapes are demonstrably from a correctly serving model.

Two capture-only modifiers and the reason for each, plus the
shapes-with-radix-cache-on / tensors-with-radix-cache-off split, are documented in
[`docs/workload_capture.md`](docs/workload_capture.md). The tooling in
[`tools/`](tools/) regenerates everything:

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
* **Elementwise fusion in diffusion** - we swept the ecosystem for this in August
  and concluded SGLang is already at the frontier: our elementwise kernels sit at
  70-88% of achievable bandwidth and the entire remaining residue is 1-4% of a step.
  A fused DiT gate+residual+norm+shift/scale task was drafted and cut for exactly
  this reason.
* **Video VAE decode kernels** - real target, wrong time: the fused conv3d /
  GroupNorm-SiLU kernels are not called by the model we had staged (Wan2.2 has its
  own decoder), and the models that do call them were not captured in this pass. We
  would rather hand it over with shapes than without.
* **Programmatic Dependent Launch in diffusion** - measured ceiling below 0.5% of
  step time at these kernel granularities.
* **Kernels that are dead on the recommended path.** Each task's evidence section
  names the entry points that fired **zero** times on the cookbook recipe - the DSA
  task in particular - so no cycles go to code the deployment never runs.

Everything here is reproducible from `tools/` plus the command in each task's
`docs/capture_provenance.md`. If a number looks wrong, that is the path to check it.
