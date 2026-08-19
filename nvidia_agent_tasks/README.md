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
| [`glm47_flash__triton_attention`](glm47_flash__triton_attention) | GLM-4.7-Flash | `decode_attention_fwd`, `extend_attention_fwd` | **75.3%**; the same kernels are **50.8%** of Qwen3-Next at 32k input | 86 rows / 3 ops, 4.7 MB real tensors |
| [`deepseek_v4_flash__dsa_sparse_attention`](deepseek_v4_flash__dsa_sparse_attention) | DeepSeek-V4-Flash | whole DSA chain: compress -> q-indexer -> **deep_gemm logits** -> top-k -> **flash_mla sparse core**, plus the **mHC TileLang** kernels | front end **8.46%** aggregate, sparse core **7.50%**, mHC **8.06%** of serving GPU time | 111 rows / 12 ops, 35 MB real tensors |
| [`lfm25__triton_fused_moe`](lfm25__triton_fused_moe) | LFM2.5-8B-A1B (+ GLM-4.7-Flash) | `invoke_fused_moe_kernel` and friends | **50.5%** / 30.4% | 19 rows, two expert geometries + real routing tensors |
| [`qwen3_next__gdn_chunk_prefill`](qwen3_next__gdn_chunk_prefill) | Qwen3-Next-80B-A3B | FLA chunk prefill + **`TritonGDNKernel.packed_decode`** | GDN family **2.8-5.3%** across four operating points (decode kernel 2.0-3.6%, chunk prefill peaks 2.5% at 8k in) | 46 rows, **2 verified 16-step state chains** |
| [`kimi_k3__tgv_bf16_tiny_gemm`](kimi_k3__tgv_bf16_tiny_gemm) | Kimi-K3 (2.8T, TP8) | `cutedsl_bf16_gemm` (CuTe TGV) + the `tiny_n/k_gemm` fast paths and their dispatcher | TGV **7.69%** at cc16 / **41.2%** at batch 1; tiny_n **1.64%** | 53 rows / 5 entry points, 15 MB real tensors |
| [`kimi_k3__kda_linear_attention`](kimi_k3__kda_linear_attention) | Kimi-K3 (2.8T, TP8) | `kda_fused_decode` (JIT CUDA) + KDA chunk prefill | **3.55%** family (decode kernel 2.81%) | 19 rows, 308k decode calls + a verified state chain |
| [`minimax_h3__sm103_block_sparse_attention`](minimax_h3__sm103_block_sparse_attention) | MiniMax-H3 | **write a new** sm_103 sub-block block-sparse forward | the sparse arm is the only backend beating cache-only on B300 (10.37 s vs 11.16 s) | dense reference shapes + deadlock forensics |

Seven of them have a shipped SGLang kernel that a candidate has to beat. The eighth,
`minimax_h3__sm103_block_sparse_attention`, is a new-kernel task: the existing sub-block
BSA implementation deadlocks on sm_103, so there is nothing to beat, only something to
replace.

[`SHAPES.md`](SHAPES.md) lists the shape family of every op in every task in one place
(regenerate with `python tools/dump_shapes.py > SHAPES.md`).
[`docs/profiles/`](docs/profiles) holds the raw per-kernel GPU-time tables the shares
above come from.

## Running a task

```bash
python tools/check_task.py <task>          # package complete? (CPU only, doubles as CI)
python <task>/tests/test_contract.py       # rows, OPS coverage, sources, chains (CPU only)
python tools/bench_harness.py <task>       # baseline timing per row (GPU)
# ...write solution/entry.py with the same OPS keys...
python tools/bench_harness.py <task> --json report.json    # interleaved A/B + gates
```

**Verified on 1x B300 with SGLang main @ 43226af: 37 of the 45 op-rows produce a
CUDA-graph-timed baseline straight from the recorded workload, and the whole A/B path was
validated with an identity candidate - 1.002x geomean with every gate green, which is also
the harness's measurement floor.** The remaining 8 need a
few lines in that task's `RECONSTRUCT` hook, because the capture can record an argument's
contents but not the object around it (a plan namedtuple, a bound method's instance);
each task's `bench/README.md` names exactly which ones and why, and the harness reports
them as `NOT RUNNABLE` with the missing argument named instead of aborting the run.

| task | ops timing today |
| --- | --- |
| `nemotron3_nano__mamba2_ssm` | 9 / 9 |
| `glm47_flash__triton_attention` | 6 / 6 |
| `kimi_k3__tgv_bf16_tiny_gemm` | 5 / 5 |
| `kimi_k3__kda_linear_attention` | 2 / 2 |
| `lfm25__triton_fused_moe` | 2 / 2 |
| `qwen3_next__gdn_chunk_prefill` | 5 / 6 |
| `deepseek_v4_flash__dsa_sparse_attention` | 8 / 12 |
| `minimax_h3__sm103_block_sparse_attention` | 0 / 3 (backend impls need an instance) |

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

Each task also carries `solution/entry.py.template` (the OPS skeleton to fill in),
`tests/test_contract.py` (package integrity, CPU-only) and `tests/test_solution.py` (the
correctness gate for a candidate, including the chained final-state gate where the task
ships a chain).

| doc | what it fixes |
| --- | --- |
| [`docs/measurement_contract.md`](docs/measurement_contract.md) | how a win is measured: CUDA-graph timing, interleaved A/B, ncu inflation, the microbenchmark traps that produced wrong answers here, noise floors |
| [`docs/anti_hack_contract.md`](docs/anti_hack_contract.md) | why synthetic Gaussian inputs let three specific shortcuts pass, and the chained final-state gate that catches them |
| [`docs/baseline_policy.md`](docs/baseline_policy.md) | baseline = the shipped SGLang kernel at a pinned commit, never a naive PyTorch reference |
| [`docs/workload_capture.md`](docs/workload_capture.md) | provenance of every shape, and warmup vs real traffic |

## Out of scope, and why

* **Communication kernels and the TRT-LLM fused-MoE path.** Your ground; our profiles
  exclude them by construction.
* **Elementwise fusion in diffusion.** SGLang's elementwise kernels already run at 70-88%
  of achievable bandwidth and the entire remaining residue is 1-4% of a denoise step, so
  the ceiling is a pass-count saving, not a kernel win.
* **The diffusion attention backend.** On sm_103 the vendored FA4 CuTe kernel is 4-5%
  *faster* than cuDNN SDPA on every large shape with the fused-QKV layout the DiT
  actually uses; cuDNN only wins below ~26 tokens. What is left is a dispatch predicate on
  our side. The measured tables and captured shapes are in
  [`docs/profiles/`](docs/profiles) if they are useful to you.
* **Programmatic Dependent Launch in diffusion.** Measured ceiling below 0.5% of step time
  at these kernel granularities.
* **Kernels that are dead on the recommended path.** Each task's evidence section names the
  entry points that fired **zero** times on the cookbook recipe - the DSA task in
  particular - so no cycles go to code the deployment never runs. The same rule kept a few
  MoE-adjacent kernels out of this set entirely: on the recommended Blackwell fp8 path
  they are fused into trtllm routing.

Everything here is reproducible from `tools/` plus the command in each task's
`docs/capture_provenance.md`. If a number looks wrong, that is the path to check it.
