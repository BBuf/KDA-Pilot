# B200 Environment Snapshot — task workspace `b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`

Captured: 2026-06-04 (local); remote clock 2026-06-04 ~07:41 UTC.
All remote access via the `ion-b200` Claude Code skill (SSH alias `ion-b200`).

## Host / container

- Host: `innomatrix-us-adc-smb200-0003` (ssh alias `ion-b200`), login user `sglang-omni`
- Container: `sglang_bbuf` — running (Up 47 hours at snapshot time). Per skill contract it is created with `--privileged --cap-add=SYS_ADMIN --security-opt seccomp=unconfined` (NCU-capable); an `ncu --set basic` smoke check will be re-verified before the first profiling run.
- Remote task workspace: `REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/20260604-074122-rlcr0`

## GPU state at selection (nvidia-smi: index, name, uuid, util%, mem-used MiB / total MiB)

```text
0, NVIDIA B200, GPU-a4d97fda-2684-94c9-4291-c6b291c0eb33, 0,  0,      183359   <- SELECTED (REMOTE_GPU_ID=0)
1, NVIDIA B200, GPU-709d3f1a-3fca-36e4-22a6-e4e7e1d8c33e, 0,  0,      183359   (idle)
2, NVIDIA B200, GPU-89c9740c-e637-aa38-5d2d-77dcc8f3c75c, 0,  0,      183359   (idle)
3, NVIDIA B200, GPU-7bcee9f8-36e9-8370-5647-d6f3af9a0ab5, 0,  0,      183359   (idle)
4, NVIDIA B200, GPU-3f9e06de-1182-c110-c905-162e17af11ac, 94, 150171, 183359   (busy)
5, NVIDIA B200, GPU-8b907ca0-c8de-1118-00b6-070c288bdd6f, 94, 149311, 183359   (busy)
6, NVIDIA B200, GPU-2068bc3d-c877-5748-f9ba-3853fa3976fe, 94, 149335, 183359   (busy)
7, NVIDIA B200, GPU-932a894c-49f5-18ff-6ae0-9b6334c946b0, 94, 149345, 183359   (busy)
```

- Selected `REMOTE_GPU_ID=0` (UUID `GPU-a4d97fda-2684-94c9-4291-c6b291c0eb33`). GPUs are shared: idleness is re-checked immediately before AND after every benchmark/profile run; runs on a busy card are invalid.

## Software stack inside `sglang_bbuf`

- Active SGLang (pip editable): `/sgl-workspace/sglang` — version `0.0.0.dev1+gedb1b3f8f`, commit `edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7`, branch `main`, working tree clean (0 dirty files)
- torch `2.11.0+cu130` (CUDA 13.0)
- nvcc: CUDA 13.0, V13.0.88
- apache-tvm-ffi `0.1.9`
- nvidia-cutlass-dsl `4.5.0` (CuTe-DSL runtime for the baseline)
- cuda-python `13.2.0`
- Nsight Compute (`ncu`) present in PATH
- Note: `/home/sglang-omni/bbuf/repos/sglang` also exists but is NOT the pip-active checkout; all baseline/runtime behavior binds to `/sgl-workspace/sglang`.

## Source lineage (container vs local recovery checkout)

Local recovery checkout: `/Users/bbuf/工作目录/Common/sglang` @ `0689ba84b8` (branch `kda/group_norm_silu_export`).
Container active checkout: `/sgl-workspace/sglang` @ `edb1b3f8f` (branch `main`).

sha256 comparison of task-relevant files — IDENTICAL in both checkouts:

```text
b4a77d302827f3060a595030ef683c725e13cdb15e3d1e574680b4af09532769  python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py
4cec65996625b63f4e7d09a1d877991bec23176039f54d82f133a5b39fae4fd3  python/sglang/jit_kernel/diffusion/cutedsl/common/norm_fusion.py
90b8a0ea9a857849799ae8c17e3306271b68156082fcc4c257b28a1d051e7e2e  python/sglang/jit_kernel/diffusion/cutedsl/common/reduce.py
11439328fbc48f81547d181b049e0e662f1f308b58292b750bb2784ee39643fe  python/sglang/jit_kernel/diffusion/cutedsl/utils.py
86db210550d97141b932be60ec8643b3819cd893e24b57eeda192129cddf6898  python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh
```

DIFFERING between checkouts (container value is authoritative at runtime; differences do not affect the baseline kernel itself):

```text
python/sglang/jit_kernel/utils.py                          container=993cdf728a8184346b7cd12cae315ce454e5f3e32018df4013e8520443a72a32  local=a96739cf79e9c088cb273950ca95d33db33f26dcb27b8c873b20359c2a2846ed
python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py  container=92abe0c0683d197d41ccc5ce34c6c1af623307447f0d8dac6a96e9cf7cc4d7a8  local=fe01710f49490cbda8a10fe94fdb793bd78dd9ba974e4efd706f13c0d69f71bf
```

## Reference skills

- `external/KernelWiki` @ `faed56ce84e5700087a8aee91cc9ab2902a57625` (submodule initialized; `scripts/query.py --help` exit 0)
- `external/ncu-report-skill` @ `d1887948c7d53690cfe6605f59c1329b8a1c6bb5` (submodule initialized)
- `~/.claude/skills/ion-b200/SKILL.md` — remote host conventions (read)

## Remote execution pattern (per ion-b200 skill + task prompt, revised round 1)

Use quoted-heredoc stdin piping so every variable expands INSIDE the container, and
literal absolute paths for anything destructive (`BL-20260604-remote-shell-var-expansion`
— nested host-shell expansion of in-container variables caused the round-0 incident):

```bash
ssh ion-b200 'docker exec -i sglang_bbuf bash -s' <<'EOF'
cd /home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/<run>/workspace
REMOTE_GPU_ID=<idle-id> CUDA_VISIBLE_DEVICES=<idle-id> <command>
EOF
```

No Python/pip/nvcc/build/test/benchmark/profiling directly on the `ion-b200` host.
`benchmark.py` enforces the selection contract: it aborts unless `REMOTE_GPU_ID` is set
and matches the first `CUDA_VISIBLE_DEVICES` entry, and unless the card passes the
strict idle gate (start: no compute apps, util ≤ 5%, memory ≤ 2 GiB; end: no foreign
compute app AND memory ≤ 2 GiB — memory-only or one-app-high-memory contamination is
rejected since per-PID self-attribution is impossible in the container namespace).

## GPU selection updates during the loop

- Round 0: `REMOTE_GPU_ID=0` (state table above).
- Round 1: GPU 0 became occupied by a foreign memory-resident app (host pid 2752289,
  ~6.6 GiB, 0% util — not ours, left untouched); the strict gate correctly refused it
  twice. Final fixed-gate benchmark + dispatch-symmetric arbiter r4 ran on
  **`REMOTE_GPU_ID=1`** (`GPU-709d3f1a-3fca-36e4-22a6-e4e7e1d8c33e`, fully idle:
  0% util, 0 MiB, no compute apps).
