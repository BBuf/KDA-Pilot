# Run Log — b200_ltx2_rms_adaln__bitwise

All build / correctness / benchmark / probe work runs on the matching remote B200
host. The local development host is macOS (no CUDA); only source editing happens
locally. Evidence below is from the RLCR validation run on 2026-06-29.

## Host / GPU

- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), user `sglang-omni`.
- Container: `sglang_bbuf` (image `lmsysorg/sglang:dev`), `--privileged` (NCU-capable).
- Selected GPU: `REMOTE_GPU_ID=5`, NVIDIA B200 (sm_100, CC 10.0, 192 GB HBM3e),
  pinned via `CUDA_VISIBLE_DEVICES=5` for every build/correctness/benchmark/probe
  command in this run.
- GPU 5 idle state:
  - before: `5, 0 %, 0 MiB` (no compute processes).
  - after benchmark: `5, 0 %, 4 MiB` (still idle; the 4 MiB is residual context).
  - Other GPUs (1-4) showed unrelated load from other users during the window;
    GPU 5 stayed at 0% utilization, so the isolated CUDA-event timings are valid.

## Toolchain (pinned, in-container)

- torch `2.12.1+cu130`, CUDA `13.0`, `tvm_ffi` `0.1.9`, nvcc `V13.0.88`.
- Both baseline and candidate built by `tvm_ffi.cpp.load` with identical flags
  (`-std=c++17 -O3` + device-native `-gencode=arch=compute_100,code=sm_100`,
  torch linkage); NO `--use_fast_math`.
- Note: the production workload rows were originally captured at sglang commit
  `828411e6f1`; the eager oracle `F.rms_norm` is commit/version-stable, and the
  bitwise contract is self-consistent because baseline, candidate, and oracle all
  use the same in-container torch.

## Remote workspace

- Task-owned: `/home/sglang-omni/bbuf/kda/b200_ltx2_rms_adaln__bitwise`.
- Local working tree streamed in via `tar` (excludes `.humanize/`, `.build/`,
  `__pycache__/`, `profile/`); no sglang checkout is imported at runtime.

## Commands and results

1. Build smoke (compiles both CUDA modules for sm_100):
   - `CUDA_VISIBLE_DEVICES=5 python -c "import bench.adapter ..."` -> `BUILD_OK`
     (candidate `ltx2_rms_adaln_candidate` + baseline `ltx2_rms_adaln_baseline`).
2. Correctness (bitwise; tolerance forbidden):
   - `CUDA_VISIBLE_DEVICES=5,6 python bench/correctness.py --impl both --rows all`
     (two GPUs visible so the cross-device negative row actually executes)
   - Result: `rows=85/85 failures=0` -> `PASS (bitwise)`. Covers the 6 production
     rows, the canonical grid (all 4 supported layouts + mixed, eps in {1e-6,1e-5}),
     adversarial rounding rows + the single-fp32 sensitivity guard, out-of-gate
     fail-closed + eager fallback (misaligned/non-contiguous x/scale/shift, output
     aliasing of x/scale/shift, CPU and two-GPU cross-device), and the poison
     self-test.
3. Benchmark (standard standalone harness, isolated subprocess runner):
   - `CUDA_VISIBLE_DEVICES=5 python bench/benchmark.py --workloads bench/workloads.json --out bench/results.jsonl --device cuda:0`
   - Result: 6/6 PASSED (bit-wise matched), equal-weight geomean speedup
     **1.861x** this run (min 1.610 audio, max 2.025 hq_stage2; video rows stable
     ~1.97-2.03x). A prior quieter run measured 1.974x; the audio rows are
     launch-bound and noisier under system contention. Per-shape table + audio-
     variance note in `docs/results.md`.
4. Fully-fused feasibility probe (AC-8 gate):
   - `CUDA_VISIBLE_DEVICES=5 python bench/probe_fused.py`
   - Result: **NO-GO**. 48 cases (8 shapes × 3 seeds × {randn, wide-magnitude}); the
     custom single-kernel fp32 RMS reduction DIFFERs from `at::rms_norm` on the video
     rows (D=4096 and canonical D=3072) and matches only on audio (D=2048) -> not
     bit-exact on every row -> fully-fused single kernel is a documented no-go; the
     staged path (reuse `at::rms_norm`) is the production choice. Details in
     `docs/results.md`.

## Provenance

- Upstream baseline: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (re-resolved at loop start to `bb74ed4a8da02b4f142191eedac824471cfb1ec6`; the two
  RMS-AdaLN source files are byte-identical between the two commits). Details in
  `docs/baseline_source.md`.
- Raw benchmark samples: `bench/results.jsonl` (kept local; excluded from the PR).
