# Remote B200 Run Log

## Environment

- Host: `innomatrix-us-adc-smb200-0003` (reached via `ssh ion-b200`), user `sglang-omni`.
- Container: `sglang_bbuf_pr29315` (reused — it holds the validated stack recorded in
  `docs/benchmark_method.md` and the `workloads.json` provenance; profiler-capable).
- GPU model: NVIDIA B200 (sm_100, 183359 MiB).
- `REMOTE_GPU_ID=5` (primary, pinned via `CUDA_VISIBLE_DEVICES=5` for build, benchmark,
  and profiling). GPU 6 (also idle) used only for the multi-GPU correctness test
  (`CUDA_VISIBLE_DEVICES=5,6`).
- Toolchain: torch `2.11.0+cu130`, CUDA runtime `13.0`, nvcc `13.0.88`, tvm-ffi `0.1.9`,
  Python `3.12.3`.

## GPU idle state

- Before: GPU 5 = 0% util, 0 MiB used; GPU 6 = 0% util, 0 MiB used (no compute processes).
- After:  GPU 5 = 0% util, 0 MiB used; GPU 6 = 0% util, 0 MiB used.
- Selection rule: only GPUs with 0% utilization, no compute processes, and ~0 MiB used
  were chosen; GPUs 1–4 were busy (35–74% util) and were not used.

## Remote workspace

- Task-owned dir: `/home/sglang-omni/bbuf/kda_runs/b200_ltx2_dual_modulate__bitwise`
  (streamed from the local task folder; build/scratch/`.humanize` excluded).
- Build cache and profiler artifacts (`*/.build/`, `profile/`, `*.ncu-rep`, `results.jsonl`)
  are kept remote/local as evidence and are git-ignored (excluded from the PR).

## Commands (exact)

```bash
# build-only sanity
CUDA_VISIBLE_DEVICES=5 python -c "from solution.build import load_candidate_module; load_candidate_module()"
# bit-exact correctness gate (independent oracle), incl. multi-GPU
CUDA_VISIBLE_DEVICES=5,6 python bench/correctness.py        # -> 1819 passed, 0 failed
# per-shape A/B benchmark
CUDA_VISIBLE_DEVICES=5 python bench/benchmark.py --out bench/results.jsonl   # -> 12/12 PASSED, geomean 3.54x
# Nsight Compute (representative rows) — via the checked-in replay harness bench/ncu_run.py
CUDA_VISIBLE_DEVICES=5 ncu --set basic -k regex:affine -c 1 -o profile/ncu/video_s32640 \
  python bench/ncu_run.py --workload-id ltx23_hq_pr29392_stage2_video_explicit_s32640_d4096_bcast1 --iters 1
CUDA_VISIBLE_DEVICES=5 ncu --set basic -k regex:affine -c 1 -o profile/ncu/audio_s126 \
  python bench/ncu_run.py --workload-id ltx23_stage1_audio_explicit_s126_d2048_bcast1 --iters 1
```

## Outcome

- Correctness: 1819 passed, 0 failed (bit-exact vs independent oracle).
- Benchmark: 12/12 PASSED (bitwise), geomean 3.54×, min 2.42×, max 5.18× — no regression.
- NCU: video affine L1TEX-bound (95.5%, DRAM 22.6%); audio launch/latency-bound.
- See `docs/results.md` for per-shape numbers and the roofline/NCU analysis.
