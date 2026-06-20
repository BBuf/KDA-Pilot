# TileRT kernel tasks

CUDA optimization tasks for the **fused kernels of TileRT** (the closed-source,
B200-only, batch=1/TP=8 low-latency DeepSeek-V3.2 inference engine). Each task
gives: the problem definition, exact shapes/dtypes, a **correct PyTorch baseline**
(a faithful port of TileRT's own `golden_forward` reference), and the **measured
TileRT latency + HBM bandwidth** (from calling the real `libtilert_dsv32.so` op,
profiled with ncu on B200). The KDA goal per task: write a CUDA kernel that
**matches TileRT's measured latency** on the decode + MTP shapes.

## Layout
- `KERNEL_REGISTRY.md` — the **full audit**: every fused kernel on the DS V3.2
  decode+MTP path, with its `(kSeqLen, KeComputeType)` set read from the SASS
  symbol table. Source of truth for shape coverage.
- `harness/` — the per-op oracle + measurement harness (runs on B200):
  - `kernel_registry.py` — machine-readable registry (drives task generation).
  - `tilert_oracle.py` — instantiates each TileRT op module, runs `golden_forward`
    vs the **real `torch.ops.tilert.*`** kernel on synthetic inputs → per-op,
    per-shape correctness oracle. **16 standalone ops PASS** (see `ORACLE_RESULTS.md`).
  - `run_once.py` / `measure_ncu.py` / `sweep_ncu.py` — ncu **≥3× median** latency
    measurement (real on-GPU kernel time). Output → `docs/tilert_reference.md`.
  - `gen_tasks.py` — generates task dirs from the registry.
- `docs/` — `tilert_design_levers.md` (the blog/SASS levers each prompt cites),
  `benchmark_method.md` (the ≥3× ncu rule), `tilert_correctness_contract.md`
  (tolerances), `tilert_reference.md` (measured latencies).
- `kernels/b200_tilert_<family>/` — one task per kernel: `prompt.md` (problem +
  shapes + design levers), `config.toml` (`[reference]` = ≥3× ncu median),
  `baseline/` (golden_forward port), `bench/` (workloads.json + correctness.py +
  adapter.py), `solution/` (the KDA agent writes the CUDA kernel here).

Reverse-engineering background: `../TileRT_讨论材料.md` (§3 taxonomy, §4
persistent-grid/warp-spec, §7 comm, §13 fusion, §16 decode profile, §20 KV cache,
§22 per-kernel shapes).

## Design facts to exploit (full list in docs/tilert_design_levers.md)
- **Persistent grid, occupancy=1**: 148 CTAs (=SM count) × 384 thr (256 Consumer +
  128 Prefetcher), ~168 reg → 1 CTA/SM.
- **Warp specialization + TMA double-buffer**: Prefetcher streams weights GMEM→SMEM
  (`UBLKCP`), Consumer runs warpgroup MMA, mbarrier (`ARRIVE.TRANS64`) handshake;
  weights read **once**, intermediates stay on-chip.
- **Comm fused** (flag-based NVLink allreduce), **bandwidth levers** (FP4 experts,
  DSA top-2048 KV), **tcgen05 only in the DSA indexer** (else warpgroup HMMA).

## Status
- **Audit + full kernel set (32 kernels)**: complete (`KERNEL_REGISTRY.md`).
- **Shape coverage (decode 1 / MTP 2,4 / prefill 8,16; per SASS)**: complete in every
  `bench/workloads.json`.
- **Correctness oracle vs real op**: 16 standalone ops PASS (bf16 <2e-2, fp8/fp4
  <5e-2); see `harness/ORACLE_RESULTS.md`. Comm ops are not 1-GPU-isolatable
  (documented); a few fused ops deferred (chained/packed ABI).
- **≥3× ncu reference latencies**: `docs/tilert_reference.md` (measured on idle B200).
- **Design levers in every prompt**: complete.
