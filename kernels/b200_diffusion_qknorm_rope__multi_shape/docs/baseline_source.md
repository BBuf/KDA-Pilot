# Baseline Source Provenance — `baseline/`

Hermetic copy of the SGLang baseline kernel used by the loop-time device-fair A/B lane,
so correctness/benchmark runs never patch or monkey-patch an SGLang checkout.

## Copied files

| Local copy | Upstream file | Verbatim |
|---|---|---|
| `baseline/qknorm_rope_baseline.cuh` | `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` | yes (byte-identical at copy time) |

- Upstream project: https://github.com/sgl-project/sglang
- Copied from local checkout: `/Users/bbuf/工作目录/Common/sglang`
- Checkout HEAD at copy time: `0689ba84b88c991684b0f99ee9b50c3ce485b483`
  (`[KDA] wire direct triton_group_norm_silu public entry to the candidate dispatcher`)
- Last upstream commit touching the copied file: `d633ab7349a8cdfe939d25745c3f647c508b8be5`
  (`[Diffusion] Add qknorm rope fuse kernel (#21440)`)
- sha256 of the copy (and of the source file at copy time):
  `86db210550d97141b932be60ec8643b3819cd893e24b57eeda192129cddf6898`
- Copy date: 2026-06-04
- Local edits: **none** (verbatim copy; the file defines the warp-per-(token,head)
  `fused_qknorm_rope_warp` kernel and its `QKNormRopeKernel<...>::run` tvm-ffi launcher).

## Loader

`baseline/loader.py` builds the copy through the same `load_jit` + `make_cpp_args` +
`cache_once` entry ABI as the candidate (`src/wrapper.py`), exporting the same
`module.qknorm_rope(...)` symbol via `QKNormRopeKernel<...>::run`. Flags follow SGLang's
jit defaults (no `--use_fast_math`); `KDA_LINEINFO=1` selects a separate `-lineinfo`
profiling build keyed by its own cache marker.

## Binding-commit rule

The benchmark-binding SGLang commit is the one inside the `sglang_bbuf` container on
`ion-b200`, recorded at baseline freeze. Before the freeze, verify the remote
`python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` sha256 equals the value above;
if it differs, re-sync this copy from the remote checkout and update this document before
any A/B numbers are recorded.
