# SGLang Diffusion Kernel Shape Capture Tooling

These scripts produce the shape ledgers that back every
`kernels/*_diffusion_*__multi_shape/` task. They were used to populate
`kernels/diffusion_shapes_ledger.md`, the per-task
`docs/captured_shapes_<arch>.{jsonl,md}` files, and the
`kernels/diffusion_kernel_coverage.md` matrix.

Run them only when you need to refresh the shape ledger (for example, after a
new preset is added to the SGLang diffusion benchmark skill, after a CuTe-DSL
kernel signature changes, or after a new model goes into the diffusion preset
list).

## Components

| File | Purpose |
|---|---|
| `kernel_shape_capture.py` | Monkey-patches every non-gemm/non-attention diffusion kernel entry point and writes one JSONL record per call to `$DIFFUSION_SHAPE_LOG`. |
| `sitecustomize.py` | Auto-loads `kernel_shape_capture.py` when Python starts. Place its parent directory on `PYTHONPATH` to activate. |
| `sweep_models.sh` | Drives `sglang generate` once per preset via the diffusion-benchmark skill's `bench_diffusion_denoise.py`, with shape capture active and a per-preset timeout. |
| `generate_tasks.py` | Generates the 16 `kernels/<arch>_diffusion_<family>__multi_shape/` folders (prompt.md, interface.md, benchmark.py, README.md, src/register.py, tests/test_correctness.py, etc.). |
| `generate_launchers.py` | Generates the matching `scripts/launch_kernels/kNN_<task>.sh` launchers. |
| `aggregate_shapes.py` | Merges the per-host JSONL files into `/tmp/shapes_summary.{json,md}`. |
| `distribute_shapes.py` | Copies accepted live captures into each task's `docs/captured_shapes_<arch>.{jsonl,md}`, rewrites prompt workload sections, and writes the cross-task `kernels/diffusion_shapes_ledger.md`. |
| `patch_prompts.py` | Retired compatibility stub. Prompt refresh is owned by `distribute_shapes.py`. |
| `clean_prompts.py` | Strips inconsistent leading whitespace from the generated `prompt.md` / `interface.md` / `README.md`. |

## End-to-end replay

1. Pick the remote GPU box and copy these scripts into the container that
   already has SGLang installed:

```bash
ssh <host> 'docker cp scripts/diffusion_shape_capture sglang_bbuf:/root/diffusion_shape_capture'
ssh <host> 'docker cp ~/.codex/skills/sglang-diffusion-benchmark-profile/scripts/bench_diffusion_denoise.py sglang_bbuf:/root/bench_diffusion_denoise.py'
ssh <host> 'docker cp ~/.codex/skills/sglang-diffusion-benchmark-profile/scripts/diffusion_skill_env.py    sglang_bbuf:/root/diffusion_skill_env.py'
```

2. Verify the diffusion benchmark presets the bench script knows about:

```bash
ssh <host> 'docker exec sglang_bbuf bash -lc "python3 /root/bench_diffusion_denoise.py --list-models"'
```

3. Run the sweep against an idle set of GPUs (use `kill-idle` first if needed).
The shape log lands at `$DIFFUSION_SHAPE_LOG`:

```bash
ssh <host> 'docker exec sglang_bbuf bash -lc "
  HOST_LABEL=<host> ARCH_LABEL=<b200|h200> \
  GPU_LIST_1GPU=<idle-gpu-ids> GPU_LIST_4GPU=<idle-gpu-ids> \
  HF_TOKEN=<hf-token-with-gated-access-if-running-flux> \
  /root/diffusion_shape_capture/sweep_models.sh \
  all \
  /tmp/shapes_<host>.jsonl
"'
```

Cat.png is required for image-conditioned presets (`qwen-edit`, `wan-ti2v`,
`wan-i2v`); copy it into the container at
`/home/sglang-omni/bbuf/repos/sglang/inputs/diffusion_benchmark/figs/cat.png`
before the sweep starts. `mova-720p` also needs `mova_single_person.jpg` at the
same path. Both are linked from the SGLang diffusion benchmark skill.

4. Pull the per-host JSONL files and sweep logs locally, then refresh the task
   folders from successful native benchmark runs only:

```bash
scp <host>:<container-mount>/tmp/shapes_<host>.jsonl /tmp/shapes_<host>.jsonl
scp <host>:<container-mount>/tmp/sweep_<host>.log /tmp/sweep_<host>.log
python3 scripts/diffusion_shape_capture/aggregate_shapes.py
python3 scripts/diffusion_shape_capture/distribute_shapes.py \
  --input /tmp/shapes_<host>.jsonl \
  --sweep-log /tmp/sweep_<host>.log
python3 scripts/diffusion_shape_capture/clean_prompts.py
```

5. Commit the refreshed `kernels/` content and the cross-task ledgers.

## Notes

- Shape capture only fires for entry points listed in
  `kernel_shape_capture._TARGETS`. To watch a new kernel, add the
  `(module-path, name)` tuple there and re-deploy.
- The capture wrapper emits every newly observed kernel-call signature, plus the
  first few calls and periodic samples, so the workload table is not filled from
  inferred/model-config-only shapes.
- `kernel_shape_capture.py` skips `@triton.jit` kernels because Triton's
  `JITFunction` objects must remain subscriptable.
- Tensor shapes are typically arch-independent for the kernels in this folder;
  B200 vs H200 captures usually match. Architecturally divergent captures
  should still be recorded, since they indicate per-arch code-path differences
  in SGLang.
