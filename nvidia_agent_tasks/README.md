# SGLang kernel tasks for NVIDIA's kernel agents

Six kernel optimization tasks cut from SGLang, each with the real serving workload
behind it: frozen production shapes with their real-traffic
call counts, the copied SGLang baseline, real captured tensors where they fit, and a
correctness gate.

Read [`docs/measurement_contract.md`](docs/measurement_contract.md) first - it is
the acceptance criterion, and it is stricter than "faster in isolation" for reasons
we paid for.

## The tasks

| task | model | kernel(s) | measured share | workload data |
| --- | --- | --- | --- | --- |
| [`lfm25__triton_fused_moe`](lfm25__triton_fused_moe) | LFM2.5-8B-A1B (+ GLM-4.7-Flash) | `invoke_fused_moe_kernel` and friends | **50.5%** / 30.4% | 14 rows, two expert geometries + real routing tensors |
| [`glm45__fp8_fused_moe`](glm45__fp8_fused_moe) | GLM-4.5-FP8 (355B, TP8) | the FP8 arm of `invoke_fused_moe_kernel` **and** the whole `fused_experts_impl` dispatch | **51.5%** of serving GPU time in the expert GEMM alone, **64.3%** for the dispatch | 17 rows / 2 entry points, 16 of 17 on captured tensors |
| [`kimi_k3__tgv_bf16_tiny_gemm`](kimi_k3__tgv_bf16_tiny_gemm) | Kimi-K3 (2.8T, TP8) | `cutedsl_bf16_gemm` (CuTe TGV) + the `tiny_n/k_gemm` fast paths and their dispatcher | TGV **7.69%** at cc16 / **41.2%** at batch 1; tiny_n **1.64%** | 46 rows / 5 entry points, 15 MB real tensors |
| [`qwen38_nvfp4__fp4_w4a4_skinny_gemm`](qwen38_nvfp4__fp4_w4a4_skinny_gemm) | Qwen3.8-27B NVFP4 (SM120) | flashinfer `mm_fp4` + `fp4_quantize` + fused silu-quant | **40.7%** of the DSpark verify step (50.5% of plain decode) | 16 rows / 3 ops, real M∈{1,8,9} + 4k-prefill activations |
| [`qwen38_nvfp4__fp8_verify_skinny_gemm`](qwen38_nvfp4__fp8_verify_skinny_gemm) | Qwen3.8-27B NVFP4 (SM120) | `sm120_fp8_gemv` (M=1) + `apply_fp8_linear` cuBLAS route (M=9) | **~27%** of the DSpark verify step after falling off the M=1 fast path; 34.0% of plain decode | 8 rows / 2 ops, real M=1 payload |
| [`qwen38_nvfp4__gdn_sigmoid_gating_verify`](qwen38_nvfp4__gdn_sigmoid_gating_verify) | Qwen3.8-27B NVFP4 (SM120) | `fused_sigmoid_gating_delta_rule_update` + qkvzba split + conv1d update | **~5.3%** of the verify step, sequential in draft length | 3 rows / 3 ops, T=9 exact (DSPARK block 8) |

Every one of them has a shipped SGLang kernel that a candidate has to beat, so every
task has a reference arm and a baseline number to clear.

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

**Every op and every row times and gates. On 1x B300 with SGLang main @ 43226af the
three sm_103 packages produce a CUDA-graph-timed baseline for 8 of 8 ops over 77 of 77
rows; on 1x RTX PRO 6000 Blackwell the three sm_120 packages do the same for 8 of 8 ops
over 27 of 27 rows.** The A/B path is validated by running each task's own baseline as
its candidate: geomean 1.0060x (kimi_k3), 1.0001x (glm45) and 0.9985x (lfm25), every
gate green, which is also the harness's measurement floor.

Getting there meant fixing the input repair rather than excluding rows. A row whose
integer segment arguments are allocated instead of captured used to leave part of the
output unwritten, and the harness printed `NO VALID REFERENCE` and dropped it;
`tools/derive_inputs.py` now reconstructs those arguments from the row itself - prefix
sums over the array each indptr actually segments, pool-bounded indices, distinct state
slots or an explicit refusal - and never overwrites an argument the capture shipped.

| task | board | ops timing today | rows timing today |
| --- | --- | --- | ---: |
| `kimi_k3__tgv_bf16_tiny_gemm` | B300 | 5 / 5 | 46 / 46 |
| `glm45__fp8_fused_moe` | B300 | 2 / 2 | 17 / 17 |
| `lfm25__triton_fused_moe` | B300 | 1 / 1 | 14 / 14 |
| `qwen38_nvfp4__fp4_w4a4_skinny_gemm` | RTX PRO 6000 | 3 / 3 | 16 / 16 |
| `qwen38_nvfp4__fp8_verify_skinny_gemm` | RTX PRO 6000 | 2 / 2 | 8 / 8 |
| `qwen38_nvfp4__gdn_sigmoid_gating_verify` | RTX PRO 6000 | 3 / 3 | 3 / 3 |

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

Every model was served with **its SGLang cookbook command** on 8x B300 SXM6 (sm_103),
then walked through the same four operating points: **real GSM8K** at 5-shot serial,
16-shot 16-way and 5-shot 32-way, plus a random 1024/256 point at concurrency 16. The
GSM8K accuracy of the very run the tensors came from is recorded per task -
DeepSeek-V4-Flash **1.000 / 1.000 / 1.000**, Qwen3-Next **1.000 / 1.000 / 0.969**,
GLM-4.5-FP8 **1.000 / 1.000 / 0.938**, GLM-4.7-Flash **1.000 / 1.000 / 0.781** - so the
shapes and the tensors are demonstrably from a correctly serving model, not from a
smoke test. MiniMax-H3 is a video model and is captured from a full generation instead.
The earlier, wider sweep (random 1k/1k at concurrency 1/16/256, a 4k/512 prefill point
and ShareGPT at concurrency 32) is what the `nemotron3_nano`, `lfm25` and `kimi_k3`
shape sets came from; each task's `docs/capture_provenance.md` lists the points that
produced its own rows.

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

## Real-tensor coverage

The workload rows are frozen production shapes; wherever we could, the **tensors are the
captured ones too**, because a verifier fed Gaussian noise can be satisfied by a shortcut
that only works on Gaussians (see `docs/anti_hack_contract.md`).

```
task                                          rows  with payload   data args real
lfm25__triton_fused_moe                       14    14 (100%)     80/98  ( 82%)
glm45__fp8_fused_moe                          17    16 ( 94%)     59/82  ( 72%)
kimi_k3__tgv_bf16_tiny_gemm                   46    35 ( 76%)     59/80  ( 74%)
qwen38_nvfp4__fp8_verify_skinny_gemm           8     4 ( 50%)     6/20  ( 30%)
qwen38_nvfp4__fp4_w4a4_skinny_gemm            16     6 ( 38%)     10/45  ( 22%)
qwen38_nvfp4__gdn_sigmoid_gating_verify        3     0 (  0%)     0/11  (  0%)
TOTAL                                        104    75 ( 72%)     214/336 ( 64%)
```

`python tools/coverage.py` recomputes it. A payload counts for a row only when the call it
was captured from agrees with that row's shapes: when the large tensors were too big to
ship, two calls of very different sequence length match equally well on their small
arguments, and a row would then silently run on another call's `cu_seqlens`. That rule
lives in `tools/payload_match.py` and is the same one the harness uses at run time.

Two categories are deliberately **not** shipped
and are excluded from the arg count: model weights (distributing them is not ours to do,
and one 6016x7168 bf16 weight alone is 86 MB) and whole state/KV pools (the rows a call
actually touches ship instead). Both are recorded as metadata with shape, dtype and
quantisation flags, so an equivalent can be allocated.

Rows without a payload run on allocated tensors. The harness says so per row, and it
refuses to judge a row whose baseline does not reproduce on them - see
`docs/measurement_contract.md`.

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
