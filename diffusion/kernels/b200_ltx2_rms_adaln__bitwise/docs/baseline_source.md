# Baseline Source Provenance — b200_ltx2_rms_adaln__bitwise

## Upstream resolution

- Repository: https://github.com/sgl-project/sglang
- Branch: `main`
- Resolved commit: `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
- Resolution method: `git ls-remote https://github.com/sgl-project/sglang.git refs/heads/main` and the GitHub trees/raw API.
- Resolution time: 2026-06-29 (UTC).
- Production-capture cross-reference: `bench/workloads.json` rows were captured at sglang commit `828411e6f1` (host `ion-b200`, container `sglang_bbuf_pr29315`, `Lightricks/LTX-2.3`). The eager oracle (`F.rms_norm`) is commit-stable, so the slightly newer `main` commit used for recovery does not change the numeric target.

## Files fetched (verbatim upstream)

| Upstream path | sha256 |
|---------------|--------|
| `python/sglang/multimodal_gen/runtime/layers/layernorm.py` | `e4389a39497f0191c02f1398dc3a6d6325263d8a326eb58b96c72fb0a8482943` |
| `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` | `ff3fd96e8df346a82840a18a00f2702b8b7d02bc1950fbfcebfe3d760bde0141` |

## Copied into `baseline/`

- `baseline/upstream_reference.py` — the RMS-AdaLN-relevant verbatim extract (the `RMSNormNoWeight` class and the modulation callsite expression) plus this provenance header. This is a reference artifact only; it is **not** imported at correctness/benchmark runtime (standalone contract). No local edits to the upstream lines (verbatim quote); the only added content is the provenance header and the operation-boundary annotation.

## Recovered callsite contract (K)

- `RMSNormNoWeight` (`layernorm.py:298-307`): `forward_native(x, eps) = F.rms_norm(x, (x.shape[-1],), eps=eps)`; `forward_cuda` delegates to `forward_native`, so the production CUDA path is **plain eager** `F.rms_norm`.
- DiT (`ltx_2.py`): `self.rms_norm = RMSNormNoWeight()` (line 945); `self.norm_eps` defaults to `1e-6` (lines 603/619/932/944).
- Modulation callsites (lines 1135 / 1157 / 1188 / 1215 / 1365 / 1377), all of the form:
  ```python
  norm_hidden_states = self.rms_norm(hidden_states, self.norm_eps) * (1 + scale) + shift
  ```
  covering video & audio self-attention (MSA), prompt-Q, and MLP, across the two pipeline stages — matching the six per-stage `sites` in `bench/workloads.json`.

### Finding: named entry points are absent from `main`
`config.toml` lists entry points `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_rms_adaln` and `:_ltx2_try_fused_rms_adaln`. **Neither symbol exists in upstream `main`** at the resolved commit (`grep` count 0). They were the proposed fused helpers of the **closed** PR `sgl-project/sglang#29396` (never merged). The recovered, authoritative baseline is therefore the inline eager pattern above. This matches the source prompt, which specifies the target pattern as "every PyTorch fallback callsite of the form `rms_norm_layer(x, eps) * (1 + scale) + shift`".

## Task-local baseline semantics (R)

```python
normed = torch.nn.functional.rms_norm(x, normalized_shape=(D,), eps=eps)
y = normed * (1 + scale) + shift
```

Per-operation bf16 rounding boundaries (eager): (1) `rms_norm` (fp32 reduction, bf16 store) → (2) `1 + scale` (bf16) → (3) `normed * (1+scale)` (bf16) → (4) `+ shift` (bf16). The candidate must preserve all four.

### Broadcast convention for compressed scale/shift layouts
Supported scale/shift layouts are `[D]`, `[B,D]`, `[B,1,D]`, `[B,S,D]`. PyTorch right-aligns shapes for broadcasting, so a **bare 2D `[B,D]`** does NOT broadcast against `[B,S,D]` (it would collide on the sequence dim unless `S==B`). In AdaLN a `[B,D]` modulation is per-(batch,channel) applied over the sequence, i.e. semantically `[B,1,D]`. The task-local oracle, the ATen baseline (`baseline/kernel.cu`), and the candidate's PERBATCH mode therefore all treat a 2D `[B,D]` scale/shift as `[B,1,D]` (unsqueeze at dim -2). `[D]`, `[B,1,D]`, and `[B,S,D]` broadcast directly. (Production rows are full `[B,S,D]`.)
