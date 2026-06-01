# GPU-state + command provenance -- h200_diffusion_qknorm_rope__multi_shape

- Host: ion8-h200  Container: sglang_omni_bbuf_kda  GPU id: 7
- Workdir (in container): /home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/round0-20260601-145601/cand
- sglang PYTHONPATH: /home/sglang-omni/bbuf/repos/sglang/python

This artifact has one BEFORE/AFTER `nvidia-smi` section per `benchmark.csv` run. The three
committed runs (src=04e37d1a) gave geomean 1.0965 / 1.1258 / 1.0883 (median 1.0965); across all
idle-GPU runs observed (incl. earlier src hashes) the all-9 geomean is ~1.09-1.13x. The all-9
geomean is noisy because the launch-bound tiny shapes (T<=195, ~1.0-1.1x) dominate it; the large
shapes (>=4096 tokens) are stable at ~1.14-1.16x. GPU 7 was idle (util 0%, mem ~100 MiB) before
and after every run.

## Exact benchmark command (reproducible)
```bash
ssh ion8-h200 'docker exec sglang_omni_bbuf_kda env CUDA_VISIBLE_DEVICES=7 KDA_HOST=ion8-h200 KDA_GPU_ID=7 KDA_CONTAINER=sglang_omni_bbuf_kda KDA_REMOTE_WORKDIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/round0-20260601-145601/cand PYTHONPATH=/home/sglang-omni/bbuf/repos/sglang/python bash -lc "cd /home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/round0-20260601-145601/cand && bash profile/round0_ncu/run_bench.sh"'
```

## NCU collection provenance (AC-5)
NCU `--set full` profiles were collected on the same idle GPU 7 via `profile/round0_ncu/run_full.sh`:
```bash
ncu --set full --target-processes all --kernel-name regex:fused_qknorm_rope \
    --launch-skip 60 --launch-count 1 -o profile/round0_ncu/reports/full_<bucket> -f \
    python profile/round0_ncu/harness/prof_entry.py <T> <H>
```
The 2-head production kernel is byte-identical across round-0/1/2 source hashes (only a
1-head A/B entrypoint and a Python fallback reference were added), so the metrics hold.

## Per-run nvidia-smi idleness (one BEFORE/AFTER section per benchmark.csv run)

### Run 2026-06-01T08:51:04Z -- BEFORE
index, name, util.gpu(%), mem.used(MiB), mem.total(MiB)
```
7, NVIDIA H200, 0, 100, 143771
```
### Run 2026-06-01T08:51:04Z -- AFTER (benchmark rc=0)
```
7, NVIDIA H200, 2, 100, 143771
```

### Run 2026-06-01T08:51:14Z -- BEFORE
index, name, util.gpu(%), mem.used(MiB), mem.total(MiB)
```
7, NVIDIA H200, 0, 100, 143771
```
### Run 2026-06-01T08:51:14Z -- AFTER (benchmark rc=0)
```
7, NVIDIA H200, 3, 100, 143771
```

### Run 2026-06-01T08:51:24Z -- BEFORE
index, name, util.gpu(%), mem.used(MiB), mem.total(MiB)
```
7, NVIDIA H200, 0, 100, 143771
```
### Run 2026-06-01T08:51:24Z -- AFTER (benchmark rc=0)
```
7, NVIDIA H200, 2, 100, 143771
```
