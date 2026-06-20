# b200_tilert_rmsnorm_quant
Target GPU: NVIDIA B200 (sm_100).
## Problem
Fused **RMSNorm + per-128-block FP8(e4m3) quantization** (DeepSeek-V3.2 activation quant),
matching TileRT `RMSNormQuantExecutorImpl`.
```
y = x * rsqrt(mean(x^2)+eps) * gamma            # bf16 out
per 128-block: scale = amax(|y|)/448 ; q = (y/scale) as fp8_e4m3   # fp8 out + fp32 scale
```
Shapes (decode): hidden[1,seq,7168] bf16, gamma[7168] f32 -> hidden_out[1,seq,7168] bf16,
q_out[1,seq,7168] fp8_e4m3, q_scale[1,seq,56] f32. seq∈{1,2,4}.
## TileRT reference (measured, libtilert_dsv32.so on B200, ncu)
RMSNormQuantExecutorImpl<DefaultSchedule,4,32768,1,1,3> grid(148)×block(384) = **7.2µs**,
DRAM 0.13% (launch/fixed-cost bound for 1 token). Validated: output rel 1.62e-3 vs torch,
dequant rel 2.37e-2 (fp8). compute_kernel_type="general", gamma must be float32.
## Design levers to exploit (see ../../docs/tilert_design_levers.md)
- **L2 no-GMEM intermediates** (§13.3): single-pass fused norm→quant — the normalized
  activation never round-trips GMEM; compute the per-128 amax/scale and emit fp8 inline.
- **L1 tile overlap** (§4/§13): persistent grid (148×384), Prefetcher/Consumer split.

## Shapes (decode + MTP)
RMSNormQuant SASS kSeqLen = {1,2,4,8,16} (decode=1, MTP verify=4, prefill 8/16).
Workloads `bench/workloads.json` cover all five. Validated by
`../../harness/tilert_oracle.py case_rmsnorm_quant` (rel 1.6e-3 vs real op).

## Goal
CUDA kernel matching the baseline output (per ../../docs/tilert_correctness_contract.md) and
TileRT's latency on every seq (≥3× ncu median, see `config.toml [reference]`). This op is
launch-bound at seq=1 — the lever is minimal launch overhead + single-pass fused norm→quant.
