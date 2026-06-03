# SGLang jit_kernel / tvm-ffi Export — b200_diffusion_rotary_embedding__multi_shape

## Preserved public entry points
- `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding(x, cos, sin, interleaved=False)`
- `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb(x, cos, sin)`

## Candidate source & build
- Device code: `src/csrc/rotary_embedding.cuh` (templated, header-only; `kda_diffusion_rotary::StandardRotaryKernel<head_dim, use_pdl, DType>` and `Ltx2SplitRotaryKernel<half, use_pdl, DType>`, each with a `::run(TensorView out, x, cos, sin)` launcher mirroring `csrc/diffusion/qknorm_rope.cuh`).
- Build: SGLang `jit_kernel` / tvm-ffi only — `sglang.jit_kernel.utils.load_jit` + `make_cpp_args` (NO `torch.utils.cpp_extension`). nvcc flags = SGLang defaults (`-DSGL_CUDA_ARCH`, `-std=c++20`, `-O3`, `--expt-relaxed-constexpr`); **no `--use_fast_math`**. PDL off (validated unnecessary).

### load_jit args (template arg order = `<head_dim|half, use_pdl, DType>`)
```python
# standard
args = make_cpp_args(head_dim, use_pdl, dtype)            # e.g. "128, false, bf16_t"
load_jit(f"kda_diffrope_std_{src_hash}", *args,
         cuda_files=[<rotary_embedding.cuh>],
         cuda_wrappers=[("apply_rotary",
                         f"kda_diffusion_rotary::StandardRotaryKernel<{args}>::run")],
         extra_include_paths=[<csrc dir>])
# ltx-2
args = make_cpp_args(half_dim, use_pdl, dtype)            # e.g. "64, false, bf16_t"
load_jit(f"kda_diffrope_ltx2_{src_hash}", *args,
         cuda_files=[<rotary_embedding.cuh>],
         cuda_wrappers=[("apply_ltx2",
                         f"kda_diffusion_rotary::Ltx2SplitRotaryKernel<{args}>::run")],
         extra_include_paths=[<csrc dir>])
```
`src_hash` (sha1 of the `.cuh`) is part of the jit module name so editing the source forces a rebuild (cache invalidation). `cuda_files` accepts an absolute path (pathlib lets an absolute entry override the `csrc/` join), so the workspace `.cuh` builds in place; the canonical packaged location is `python/sglang/jit_kernel/csrc/diffusion/rotary_embedding.cuh` (then `cuda_files=["diffusion/rotary_embedding.cuh"]`).

## Drop-in install / dispatch
`src/wrapper.py` exposes the two preserved-name callables. Install = point the SGLang public symbols at them (e.g. `sglang...rotary.apply_rotary_embedding = wrapper.apply_rotary_embedding`). The wrapper routes only the captured signatures to CUDA and falls back to the **original baseline object captured at import** for everything else — recursion-safe after the swap. `src/register.py` exposes `EXPORTS` + `register()`.

## In-tree export + in-SGLang drop-in test result (B200 GPU5, idle-gated, `export_intree.py`)
Performed in a **task-owned git worktree** of SGLang (`git worktree add --detach $REMOTE_KDA_DIR/sglang_export HEAD`, the `ion-b200` skill's recommended remote-experiment pattern), with `src/csrc/rotary_embedding.cuh` **physically copied** to `python/sglang/jit_kernel/csrc/diffusion/rotary_embedding.cuh` in that worktree. `import sglang` resolved to the worktree (`sglang_from=.../sglang_export/python/sglang/__init__.py`), and the candidate was built by a `cache_once` loader using the **relative** csrc path `cuda_files=["diffusion/rotary_embedding.cuh"]` — the official packaged form.
- **csrc file present in-tree**: `true` (`.../jit_kernel/csrc/diffusion/rotary_embedding.cuh`).
- **jit_kernel build**: OK via `cache_once` + `load_jit` relative csrc path (tvm-ffi; no torch cpp_extension).
- **In-SGLang correctness oracle**: public API (after symbol swap) vs the original baseline — **bit-exact on all 11 captured signatures** (`max_abs_diff = 0.0`).
- **In-SGLang smoke benchmark** (public API, candidate vs original baseline): standard `1×27030×24×128` 110.82→61.70 µs **1.80×**; LTX-2 large half64 `1×24576×4096` 92.45→92.40 µs **1.00×** (DRAM-bandwidth ceiling); LTX-2 large half32 `1×24576×2048` 59.62→49.41 µs **1.21×**.
- **Fallback**: fp16 non-captured signature via the public API → original baseline (`max_abs_diff = 0.0`, recursion-safe).
- **Restore + cleanup**: originals restored (`restored = true`); worktree removed (`git worktree remove --force`) — the shared production checkout was NOT modified.

> An earlier in-process variant (`export_test.py`, runtime symbol swap + workspace-path build) gave identical results and is retained as a quicker smoke path.

## Files / scope
- Export validated in a **task-owned worktree** (not the shared checkout). To promote permanently, the same copy of `src/csrc/rotary_embedding.cuh` → `python/sglang/jit_kernel/csrc/diffusion/rotary_embedding.cuh` is applied in the chosen editable SGLang checkout and the public-name resolution registered (install/uninstall). The KDA-workspace dispatcher (`src/wrapper.py`) and the in-tree `cache_once` loader (`export_intree.py`) build the identical kernel.
- Pinned baseline: SGLang `0b65588c180a519427867d53cc4ed6e9e2610890` (`0.5.12.dev472+g3f7e538b2`), container `sglang_bbuf` on `ion-b200`.
