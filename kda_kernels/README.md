        # kda_kernels

        Python package that mirrors `sglang.jit_kernel.diffusion.*` with
        KDA-optimized kernel implementations. Importing `kda_kernels` and
        calling `install()` replaces a configurable subset of sglang's
        diffusion kernel functions with the optimized ones produced by the
        kernel-pilot KDA tasks under `kernels/`.

        ## Quick start

        ### Option A: explicit activate

        ```python
        import sglang  # baseline diffusion kernels are loaded but not yet active
        import kda_kernels
        kda_kernels.install()             # swap in every promoted KDA kernel
        # ... your sglang code runs with the optimized kernels ...
        kda_kernels.uninstall()           # restore baseline (rarely needed)
        ```

        ### Option B: implicit activate (recommended)

        Apply the patch at `patches/sglang_kda_kernels.patch` to your sglang
        checkout. The patch adds a small `try: import kda_kernels;
        kda_kernels.install()` block to the end of `sglang/__init__.py`, so
        any program that does `import sglang` automatically picks up every
        promoted KDA kernel.

        ```bash
        cd /path/to/sglang
        git apply /path/to/kernel-pilot/patches/sglang_kda_kernels.patch
        ```

        Make sure `kda_kernels/` is on `PYTHONPATH` before importing sglang,
        e.g.:

        ```bash
        export PYTHONPATH=/path/to/kernel-pilot:$PYTHONPATH
        ```

        ### Inspect what is currently swapped

        ```python
        import kda_kernels
        for sglang_path, kda_path, status in kda_kernels.install():
            print(f"{status:>30s}  {sglang_path}  ->  {kda_path}")
        ```

        ## Layout

        ```text
        kda_kernels/
          __init__.py                       # exposes install / status / uninstall
          _install.py                       # the monkey-patch driver
          _registry.py                      # KERNEL_REGISTRY: sglang_path -> kda_path mapping
          diffusion/
            qknorm_rope/                    # one directory per kernel family
              __init__.py                   # exposes the swap functions
              # after promotion these land alongside:
              # *.cu / *.cuh / *.cpp / *.h  — CUDA source copied from kernels/<task>/src/
              # wrapper.py                  — Python JIT loader for the CUDA module
              # KDA_STATUS.md               — task / commit / date / speedup stamps
            norm_infer/__init__.py          # owns norm_infer + triton_one_pass_rms_norm
            group_norm_silu/__init__.py     # owns triton_group_norm_silu + apply_group_norm_silu
            rotary_embedding/__init__.py    # owns apply_rotary_embedding + apply_ltx2_split_rotary_emb
            fuse_scale_shift/__init__.py    # owns 3 fuse_*_scale_shift_* functions
            cutedsl_norm_tanh_mul_add/__init__.py  # Z-Image residual modulation
            cutedsl_norm_scale_shift/__init__.py   # Qwen / Wan / HunyuanVideo / Helios modulation
        ```

        Every kernel family is its own Python package. `__init__.py` either
        re-exports the SGLang baseline (stub with `KDA_OPTIMIZED_<fn> = False`)
        or imports the swap functions from `<family>/wrapper.py` after the
        family has been promoted via
        `scripts/export_kda_kernels/export.py <task-slug>`. CUDA sources for
        each family live alongside the wrapper, so the shippable overlay is
        self-contained per kernel.

        All KDA-optimized kernels are native CUDA C++ (`.cu` / `.cuh` /
        `.cpp` / `.h`); Triton and CuTe-DSL appear only as baselines or
        porting references inside `kernels/<task>/src/`. The previous
        `kda_kernels/diffusion/{triton,cutedsl}/` namespaces have been
        collapsed.

        ## Swap table

| sglang entry point | kda mirror | owning KDA task family |
|---|---|---|
| `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope` | `kda_kernels.diffusion.qknorm_rope:fused_inplace_qknorm_rope` | `qknorm_rope` |
| `sglang.jit_kernel.diffusion.triton.norm:norm_infer` | `kda_kernels.diffusion.triton.norm:norm_infer` | `norm_infer` |
| `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm` | `kda_kernels.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm` | `norm_infer` |
| `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu` | `kda_kernels.diffusion.triton.group_norm_silu:triton_group_norm_silu` | `group_norm_silu` |
| `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu` | `kda_kernels.diffusion.group_norm_silu:apply_group_norm_silu` | `group_norm_silu` |
| `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding` | `kda_kernels.diffusion.triton.rotary:apply_rotary_embedding` | `rotary_embedding` |
| `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb` | `kda_kernels.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb` | `rotary_embedding` |
| `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_scale_shift_kernel` | `kda_kernels.diffusion.triton.scale_shift:fuse_scale_shift_kernel` | `fuse_scale_shift` |
| `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_layernorm_scale_shift_gate_select01_kernel` | `kda_kernels.diffusion.triton.scale_shift:fuse_layernorm_scale_shift_gate_select01_kernel` | `fuse_scale_shift` |
| `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_residual_layernorm_scale_shift_gate_select01_kernel` | `kda_kernels.diffusion.triton.scale_shift:fuse_residual_layernorm_scale_shift_gate_select01_kernel` | `fuse_scale_shift` |
| `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add` | `kda_kernels.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add` | `cutedsl_norm_tanh_mul_add` |
| `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale` | `kda_kernels.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale` | `cutedsl_norm_tanh_mul_add` |
| `sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_norm_scale_shift` | `kda_kernels.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_norm_scale_shift` | `cutedsl_norm_scale_shift` |
| `sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_scale_residual_norm_scale_shift` | `kda_kernels.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_scale_residual_norm_scale_shift` | `cutedsl_norm_scale_shift` |

        ## When `install()` skips a function

        - `skipped: not optimized` — kda_kernels still re-exports the sglang
          baseline for that function. This is the default until a KDA task is
          promoted.
        - `skipped: already installed` — call `kda_kernels.install(force=True)`
          to re-swap, or `kda_kernels.uninstall()` first.
        - `skipped: <exception>` — either side could not be imported or the
          attribute is missing; pass `strict=True` to `install()` to raise.

        ## Versioning

        `kda_kernels.__version__` follows the kernel-pilot tag. Each promoted
        function's module also carries:

        - `KDA_TASK`: which kernel-pilot task produced it
        - `KDA_COMMIT`: kernel-pilot commit sha at promotion time
        - `KDA_SPEEDUP`: claimed geomean speedup at promotion time
        - `KDA_DATE`: ISO date of promotion

        These show up in `kda_kernels.install()`'s log messages.
