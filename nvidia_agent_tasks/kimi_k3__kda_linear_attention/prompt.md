# KDA linear attention: fused decode + chunk prefill (Kimi-K3)

**Task:** `kimi_k3__kda_linear_attention`

**Model:** `moonshotai/Kimi-K3`
**Serving command this workload came from (the deployment we run in production):**

```bash
python3 -m sglang.launch_server --model-path moonshotai/Kimi-K3 \
  --trust-remote-code --tp-size 8 --mem-fraction-static 0.85 \
  --reasoning-parser kimi_k3 --tool-call-parser kimi_k3
```

**Measured share:** **3.55%** of serving GPU time as a family (decode fusion kernel 2.81%, chunk prefill 0.48%, causal conv1d 0.21%) at random 1k/256 concurrency 16

## Kernels in scope

- `k3_kda_fused_decode`
- `k3_kda_chunk_prefill`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install). Do not benchmark against a
naive PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- Kimi-K3 is 93 layers, 69 of them KDA linear attention - the decode kernel fires
  308,024 times in this capture. It is a hand-written JIT CUDA kernel
  (`kda_decode_fusion_many_heads_kernel`), so a candidate has a real implementation to
  beat, not a Triton reference.
- The prefill side is the same algorithm family your KDA_prefill CuTe kernels already
  target (we vendor them at `kernels/ops/attention/linear/kda_nvidia_prefill`, 2.3-2.9x
  over the FLA reference on B200) - this task supplies the decode half and the real
  chunked-prefill shapes from a TP8 deployment.
- Per rank the geometry is 12 KDA heads of head_dim 128 with a 128x128 state, gate lower
  bound -5.0, and `use_qk_l2norm_in_kernel=True` - i.e. a cross-channel reduction per
  token that is exactly what a synthetic-Gaussian verifier lets you skip (see the anti-
  hack contract).

## Correctness gate

- State-carrying: the chained final-state gate. `bench/tensors/kda_decode_chain8_bs1/`
  ships **8 consecutive real decode steps of one layer at batch 1**, whose state links are
  byte-identical (7/7, `tools/verify_state_chain.py`). The layer's invariant tensors live
  once in `static/`, and the conv-state pool is stored as the touched rows - see
  `CHAIN.json`.
- Prefill: output plus `final_state` against the baseline on the captured ragged
  `cu_seqlens`.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic call
counts, captured on 8x B300 (TP8) with GSM8K 5-shot serial, 16-shot 16-way and 5-shot
32-way - **accuracy 1.000 on all three**. `docs/capture_provenance.md` has the details.

## Notes

- Decode inputs are non-contiguous slices of a fused QKV buffer; gate/beta buffers are
  padded to a multiple of 16 so their sequence dim is larger than q/k/v's;
  `initial_state` is fp32 while q/k/v/g are bf16. All three are in the shipped rows.
- Chain capture required `--disable-radix-cache`: with it on, the mamba/KDA pool's
  extra_buffer strategy rewrites state rows outside the kernel call.

## Deliverable

1. Kernel source in `solution/`, exposing the same `OPS` keys as `baseline/entry.py`.
2. `python tools/bench_harness.py kimi_k3__kda_linear_attention --json report.json` output.
3. The correctness-gate result, and the Nsight Compute evidence for any bottleneck claim.
