# NCU Report — CTA-per-token cos/sin staging candidate vs baseline (B200)

Run: `staged_b200` | host `innomatrix-us-adc-smb200-0003` | physical GPU 4 (B200, sm_100)
| commit `e2b54594a`. Candidate kernel:
`fused_qknorm_rope_cta_token<128,128,is_neox=0,use_pdl=1,bf16,int64>` — one CTA per
token, cos/sin row staged once into shared memory and reused across the token's q+k
heads. Method: `ncu --set full -k regex:cta_token -s 5 -c 1` on `optimized_wrapper`
(KDA_CAND_VARIANT=staged). Reports: `reports/large_full.ncu-rep` (remote); metrics in
`analysis/large_raw.csv`.

## Large shape `qwen-edit B8424/H24` — before/after

| metric | baseline warp (baseline_b200) | staged (this run) | Δ |
|---|---|---|---|
| device time `gpu__time_duration.sum` | 109.6 µs | **88.1 µs** | **−20% (≈1.24x)** |
| top stall `long_scoreboard` (ratio) | 11.9 | **9.29** | −22% |
| compute SOL `sm__throughput…elapsed` | 60.3 % | 59.0 % | ~same |
| memory SOL | 50.2 % | 47.4 % | ~same |
| DRAM read %peak | 12.8 % | 16.0 % | higher (same bytes, less time) |
| L2 hit `lts__t_sector_hit_rate` | 50.0 % | 48.4 % | ~same |
| achieved occupancy | 88.9 % | 84.6 % | −4 pts (smem + sync) |
| grid / static smem | 1184 / 0 | 1184 / **512 B** | cos/sin staged |
| registers/thread | 32 | 32 | same |
| new stall | — | `barrier` 2.04 | from the `__syncthreads` (outweighed) |

## Named active bound + verdict
The large kernel was memory-latency-bound (`long_scoreboard` dominant). Staging the
float32 cos/sin row once per token into shared memory and reusing it across the token's
heads **cuts `long_scoreboard` 11.9 → 9.29**, lowering device time **109.6 → 88.1 µs**.
The added `__syncthreads` introduces a small `barrier` stall (2.04) that is more than
offset. This is a **real, NCU-validated device win** on the large bucket, consistent
with the device-fair interleaved benchmark (large 1.10–1.26x; warp-sanity 0.9994x
confirms the comparison is fair).

## Small shapes
Staging does not help small shapes (device-fair ~0.86–1.0x): the grid is tiny
(num_tokens CTAs ≪ 148 SMs), and the small-shape bottleneck is host dispatch, not the
device kernel. → A per-bucket dispatcher (large → staged, small → warp/baseline) is now
evidence-justified (AC-6, next round).

## Cross-references
- Device-fair interleaved: `devfair_staged.log` (geomean 1.0787x), `devfair_warp.log`
  (0.9994x sanity) in `REMOTE_KDA_DIR`.
- Decomposition: `profile/decompose.py` + `decompose.log` (custom-op overhead ~4–5 µs;
  device-fair large 1.15x, small 0.86x).
- Build flags: `build_flags.log` — `-DSGL_CUDA_ARCH=1000 -std=c++20 -O3
  --expt-relaxed-constexpr`, no `--use_fast_math` (AC-2 flag parity).
