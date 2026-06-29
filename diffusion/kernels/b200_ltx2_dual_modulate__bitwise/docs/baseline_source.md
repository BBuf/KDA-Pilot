# Baseline Source Provenance

## Upstream resolution
- Repository URL: https://github.com/sgl-project/sglang
- Branch: `main`
- Resolved commit SHA: `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
- Commit date (UTC): 2026-06-28T14:16:38Z
- Commit subject: "feat: first-class session identity in SGLang (#29436)"
- Resolution time (UTC): 2026-06-29 (resolved at baseline-recovery time)
- Resolution method: `gh api repos/sgl-project/sglang/commits/main` to resolve the
  latest `main` SHA, then `gh api .../contents/<path>?ref=<SHA>` (raw) to fetch the
  exact source files. No SGLang checkout is imported or installed.

## Copied files (source context only — not imported at runtime)
| Local file | Upstream source @ aaa31eb0 | Notes |
|---|---|---|
| `baseline/upstream/rmsnorm_noweight_excerpt.py` | `python/sglang/multimodal_gen/runtime/layers/layernorm.py` (lines 299-307) | `RMSNormNoWeight` definition + reference to the weighted `RMSNorm.forward_native` |
| `baseline/upstream/ltx2_dual_modulation_callsite_excerpt.py` | `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` (lines ~1135, 1246-1305) | Explicit + CA dual-modulation callsite |

## Key findings (affect bitwise target)
1. **The source normalization is `torch.nn.functional.rms_norm`, executed under production autocast.**
   `LTX2TransformerBlock` uses `self.rms_norm = RMSNormNoWeight()`. On CUDA the
   CustomOp dispatch resolves to `forward_cuda -> forward_native ->
   F.rms_norm(x, normalized_shape=(x.shape[-1],), eps=eps)`. In SGLang LTX2.3
   this block runs inside the denoising loop's CUDA bf16 autocast context
   (`disable_autocast=false`, `dit_precision=bf16`). Therefore the correctness
   target is the autocast-visible production expression, whose live dual outputs
   are fp32 tensors. No separate Triton/sgl_kernel rmsnorm is on the current LTX2
   dual-modulation path.
2. **The prompt's `_ltx2_try_fused_rmsnorm_dual_modulate` /
   `_ltx2_try_fused_rmsnorm_ca_dual_modulate` helpers do NOT exist on `main`.**
   PR `sgl-project/sglang#29392` was closed (not merged). The eager modulation
   lives directly in `LTX2TransformerBlock.forward`. They are used only as
   callsite/shape context, never copied as the candidate (as the prompt requires).
3. **The block class is `LTX2TransformerBlock`** (the prompt's
   `LTX2VideoTransformerBlock` is a historical name).
4. **CA callsite scope.** The upstream CA path slices a 5-row
   `*_cross_attn_scale_shift_table` into 4 scale/shift rows + 1 gate row and adds
   a trailing `.squeeze(2)`. The per-layer **gate** rows and the squeeze belong to
   the surrounding block and are OUT OF SCOPE. The task implements exactly the
   dual-modulation sub-graph the prompt specifies (table `[4,D]` + `temb` ->
   scale0/shift0/scale1/shift1, then rms_norm + two affines).

## Itemized local edits
1. Extracted only the relevant snippets (no full-file copy) and added provenance
   headers; the excerpts are reference-only and are not imported at runtime.
2. No functional edits to upstream logic.

## Baseline / candidate exposure (to be implemented under RLCR)
- Correctness oracle: a task-local pure-PyTorch reimplementation of the
  production formulas under CUDA bf16 autocast, compared with `torch.equal`.
- Candidate ABI: destination-passing fp32 outputs for the live rows, with cheap
  preflight rejection for unsupported shapes/dtypes and no hot exception-driven
  fallback.
