# NCU Report: r0v1 — nss-b1-s11040-d5120 per-token fp32 scale/shift

- Case: `nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06` (helios), the
  bucket where candidate v1 was device-slower than baseline (benchmark
  stream-span 113.1 vs 104.8us). Profiled BOTH kernels under `ncu --set full`
  (locked clocks), ion-b200 GPU0 idle.

## Candidate v1 (vec32: 16 elems/thread, block=320)

- dur ≈ 160-164us, regs 52, **occupancy 41%** (regs/CTA 16.6K → 3 CTAs/SM),
  mem_SOL 62%, dram 4.1 TB/s, **long_scoreboard 16.4** (dominant stall),
  issue 27%.

## Baseline CuTe (8 elems/thread, block=640)

- dur ≈ 138us, regs 32, **occupancy 82%** (6+ CTAs/SM), mem_SOL 72%,
  dram 4.81 TB/s, long_scoreboard 8.6, issue 55%.

## Six analysis dimensions (candidate)

1. Occupancy: 41% — register-limited (fp32 scale+shift VecArrays are 2x32B
   chunks per operand per thread at 16 elems → 52 regs/thread).
2. Balance: mem_SOL 62% with low issue 27% — latency-bound, not
   bandwidth-saturated.
3. Stalls: long_scoreboard 16.4 dominates — global-load latency NOT hidden
   (direct consequence of the low occupancy).
4. Tensor core: n/a.
5. Timeline: stable across instances.
6. Memory: traffic 0.57+0.10 GB ≈ the 12 B/elem operand-stream model
   (scale+shift fp32 reads dominate; x read fully L2/DRAM, y write 0.10 GB...
   write = 11040*5120*2B = 0.113 GB ✓).

## Diagnosis (playbook match)

"Low occupancy + long_scoreboard dominant" → reduce per-thread register
footprint to restore latency hiding. The baseline's geometry (8 elems/thread,
2x the CTAs) is strictly better for fp32 operand streams.

## Resulting design change (applied in v2)

Per-combo vector width: any combo with an fp32 operand stream (per-token or
broadcast fp32 scale/shift, fp32 gate, fp32 weight/bias) now instantiates with
kVecBytes=16 (8 elems/thread, block=D/8), bf16-only combos keep kVecBytes=32.
Implemented in `src/wrapper.py::_combo_vec_bytes`; validated by the r1-v2
benchmark run.
