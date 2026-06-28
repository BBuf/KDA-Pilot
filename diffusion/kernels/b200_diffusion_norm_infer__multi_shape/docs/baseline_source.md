# Pinned baseline lineage — baseline/

Round-2 pinned copies of the two SGLang Triton baseline implementations, used as
the baseline side of the local A/B lane for NEW candidates (the installed-sglang
baseline remains the comparator for the round-1-compatible rebaseline rows).

## Upstream source

- Repo: https://github.com/sgl-project/sglang
- Pin: container-installed editable checkout `/sgl-workspace/sglang` @ `edb1b3f8f`
  (torch 2.11.0+cu130, CUDA 13.0 container `sglang_bbuf` on `ion-b200`
  = `ion-b200`)
- Drift check vs round-1 provenance commit `0b65588c1`:
  `git diff 0b65588c1 edb1b3f8f -- <both files>` → **empty** (byte-identical),
  working tree clean for both paths. Recorded 2026-06-04.

## Copied files

| Local file | Upstream path | md5 (pre-edit, == container) |
|---|---|---|
| `baseline/norm.py` | `python/sglang/jit_kernel/diffusion/triton/norm.py` | `c3f6955e842f2cb9c0a9f14f64764511` |
| `baseline/rmsnorm_onepass.py` | `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` | `4c034f804c88b90a6deb6b758791d003` |

## Local edits (the ONLY differences vs upstream)

1. Import-shim swap, one block per file, marked with a `Pinned-copy edit` comment:
   - `norm.py`: `sglang.multimodal_gen.runtime.platforms.current_platform` and
     `sglang.srt.utils.custom_op.register_custom_op` → `_sglang_shims`
   - `rmsnorm_onepass.py`: those two plus
     `sglang.kernel_api_logging.debug_kernel_api` → `_sglang_shims`
2. New files (not from upstream): `_sglang_shims.py` (passthrough
   `register_custom_op` / `debug_kernel_api`, CUDA-only `current_platform`) and
   `__init__.py` (path-based loader + provenance constants).

The Triton kernels, autotune configs, launch heuristics, and public function
bodies are untouched.

## Why the custom-op layer is stripped here

The local lane measures DEVICE kernels through identical thin Python wrappers on
both sides (candidate side = `src/register.py` plain callables). Host-layer
registration (`@register_custom_op`) is production-required but symmetric-only
comparisons of it belong to the in-SGLang shipping arbiter (isolated worktree,
both sides registered — see `docs/sglang_jit_export.md`). The one-time parity
cross-check below quantifies the host-layer delta explicitly so it can never be
mistaken for a device win.

## One-time parity cross-check (pinned copy vs installed sglang)

Recorded in `benchmark.csv` under candidate id `baseline-parity-r2` after the
remote run: outputs bitwise-equal on the six production shapes; timing deltas
attributable to the stripped custom-op host layer are reported per shape
(see the `notes` field of those rows).
