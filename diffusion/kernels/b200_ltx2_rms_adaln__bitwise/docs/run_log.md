# Run Log — b200_ltx2_rms_adaln__bitwise

## Remote environment
- Host: `ion-b200` (login banner host `innomatrix-us-adc-smb200-0003`), user `sglang-omni`.
- Container: `sglang_bbuf` (image `lmsysorg/sglang:dev`).
- Remote task workspace: `/home/sglang-omni/bbuf/kda_tasks/b200_ltx2_rms_adaln__bitwise` (mounted into the container).
- Toolchain (in container): torch 2.12.1+cu130, CUDA 13.0, tvm_ffi 0.1.9, nvcc CUDA 13.0, cc (gcc) 13.3.0. Device gencode `sm_100`.

## GPU selection (Round 1)
`nvidia-smi` at selection time (index, util%, mem_used MiB):
```
0:82% 124880   1:0% 151085   2:0% 150343   3:92% 151071
4:92% 150329   5:0% 2230     6:0% 0        7:81% 124860
```
Selected **GPU id 6** (0% utilization, 0 MiB used — no active compute, no meaningful memory). All validation/benchmark commands pinned with `CUDA_VISIBLE_DEVICES=6` → `REMOTE_GPU_ID=6`.

- GPU 6 before benchmark: `6, 0 %, 0 MiB` (host `nvidia-smi -i 6`); benchmark `nvidia_smi_before` recorded `6, NVIDIA B200, 0 %, 4 MiB` (≈0, our own context).
- GPU 6 after benchmark: `6, 0 %, 0 MiB` (host); benchmark `nvidia_smi_after` recorded `6, NVIDIA B200, 0 %, 4 MiB`. Idle before and after → measurement valid.

## Exact commands (Round 1)
Sync (local → remote; `;` not `&&` because container-owned `.build`/`__pycache__` are root-owned and `rm` is non-fatal):
```bash
COPYFILE_DISABLE=1 tar --exclude=.git --exclude=.humanize --exclude=.build \
  --exclude=__pycache__ --exclude='*.pyc' --exclude='*.so' -cf - . | \
  ssh ion-b200 'D=/home/sglang-omni/bbuf/kda_tasks/b200_ltx2_rms_adaln__bitwise; \
  rm -rf "$D"; mkdir -p "$D"; tar -xf - -C "$D"'
```
Clean rebuild (container runs as root; clears stale root-owned build artifacts):
```bash
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && rm -rf */.build */__pycache__ bench/__pycache__"'
```
Correctness (build on first import, then run):
```bash
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && \
  CUDA_VISIBLE_DEVICES=6 python3 bench/correctness.py --impl both --report /tmp/corr_full.json"'
# -> [correctness] impl=both rows=55/55 failures=0 gpu=NVIDIA B200 ; PASS (bitwise)
# (--quick subset earlier: 27/27 PASS)
```
Benchmark:
```bash
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && \
  CUDA_VISIBLE_DEVICES=6 python3 bench/benchmark.py --out /tmp/bench_results.json"'
# -> 4/4 PASSED ; geomean_speedup=2.009 (see docs/results.md)
```

## Artifacts (kept local for audit; NOT staged in the PR)
- `/tmp/corr_full.json` (container): correctness report, 55/55 PASS.
- `/tmp/bench_results.json` (container): full per-row stats + samples + provenance.extended. Copied to the local scratchpad evidence dir.
- `.build/` (container, root-owned): compiled `.so` for baseline + candidate.

## Round 2 (same host/container; GPU id 6 re-verified idle: before/after `6, 0%, 0 MiB`)
After the device-gate fix, canonical-grid + BF1D + device correctness rows, and the task10/task12 work:
```bash
# task10 bounded fused attempt (probe: custom single-kernel RMS reduction vs at::rms_norm)
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && CUDA_VISIBLE_DEVICES=6 python3 bench/probe_fused.py"'
#  -> DIFFER on large rows (43-248/row, ~0.0002%, 1 ULP); EQUAL on small audio rows
#  -> fully-fused single kernel NO-GO (see docs/dispatch.md)

# full correctness (canonical adapted grid + BF1D rejection + device fail-closed)
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && CUDA_VISIBLE_DEVICES=6 python3 bench/correctness.py --impl both --report /tmp/corr_full.json"'
#  -> rows=69/69 failures=0 ; PASS (bitwise)

# task12 NCU (staged candidate modulation kernel), privileged container, CAP_SYS_ADMIN
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && CUDA_VISIBLE_DEVICES=6 ncu -k regex:rms_adaln_modulation -s 5 -c 1 -o profile/staged_20260629/<video|audio> --metrics <set> python3 bench/profile_one.py B S D"'
#  -> profile/staged_20260629/{video,audio}.ncu-rep (local); metrics in profile/staged_20260629/REPORT.md

# benchmark rerun (current candidate sha 39e243ed...)
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && CUDA_VISIBLE_DEVICES=6 python3 bench/benchmark.py --out /tmp/bench_results2.json"'
#  -> 4/4 PASSED ; geomean_speedup=1.964
```
Raw artifacts kept local (gitignored): `/tmp/*.json` (container), `profile/staged_20260629/*.ncu-rep`, `*/.build*`. Only `profile/staged_20260629/REPORT.md` is tracked (curated).

## Round 3 (review fix — 16-byte alignment gate; GPU 6 re-verified idle: before/after `6, 0%, ~0 MiB`)
Added a 16-byte alignment gate on the vectorized pointers (kernel `CAND_CHECK` + `adapter.in_gate`/`call_candidate`) so contiguous-but-offset (bf16-aligned) views fall back instead of doing misaligned `uint4` accesses. Re-validated:
```bash
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && CUDA_VISIBLE_DEVICES=6 python3 bench/correctness.py --impl both"'
#  -> rows=69/69 failures=0 ; PASS (bitwise) (incl. new misaligned-scale + misaligned-output rows)
ssh ion-b200 'docker exec sglang_bbuf bash -lc "cd <task> && CUDA_VISIBLE_DEVICES=6 python3 bench/benchmark.py --out /tmp/bench3.json"'
#  -> 4/4 PASSED ; geomean 1.931 ; candidate sha 6d4ac255...
```
The alignment check is host-side only (before launch); the profiled modulation kernel is unchanged, so `profile/staged_20260629/REPORT.md` remains valid.

## Notes
- The login MOTD banner prints on every `ssh ion-b200 '...'`; filter it when capturing structured output.
- A second container `sglang_bbuf_pr29315` (the 2026-06-28 LTX2.3 shape-capture container) is also running on this host; it was not used for this task.
