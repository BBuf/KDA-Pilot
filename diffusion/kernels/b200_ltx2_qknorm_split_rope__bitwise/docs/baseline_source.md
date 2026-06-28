# Baseline Source Provenance & Extracted Semantics

## Upstream source

- Repository: https://github.com/sgl-project/sglang
- Branch: `main`
- Resolved commit SHA: `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
- Resolution time: 2026-06-29 (resolved via `git ls-remote ... refs/heads/main` + blobless clone)
- Source file: `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`
  - Upstream file sha256: `ff3fd96e8df346a82840a18a00f2702b8b7d02bc1950fbfcebfe3d760bde0141`

## Copied files

| Local file | Copied from (upstream) | Notes |
|------------|------------------------|-------|
| `baseline/ltx2_split_rope.py` | `ltx_2.py` `apply_interleaved_rotary_emb` (lines 177-183) + `apply_split_rotary_emb` (lines 186-239) | `apply_interleaved_rotary_emb` verbatim. `apply_split_rotary_emb_eager` = upstream eager fallback (lines 208-239) verbatim with the fast-path dispatch removed (see Local edits). |
| `baseline/reference.py` | LTX2Attention forward order (lines 751-773) + `self.q_norm/k_norm = torch.nn.RMSNorm(inner_dim, eps)` (lines 677-678) | Task-local oracle adapter; mirrors the eager attention path. Not a verbatim file copy (it is the task adapter that composes the copied functions). |

## Local edits (intentional)

1. **Fast-path dispatch removed to force the eager reference.** Upstream
   `apply_split_rotary_emb` (lines 190-206) dispatches to a bf16 Triton kernel
   `sglang.jit_kernel.diffusion.triton.ltx2_rotary.apply_ltx2_split_rotary_emb`
   for the production input shape (x 3-D, cos/sin 4-D, all bf16, cuda, x
   contiguous). That Triton fast path is exactly the optimized kernel this task
   is **replacing**, and the source prompt requires bit-equality to the **eager**
   reference. `apply_split_rotary_emb_eager()` keeps the eager fallback math
   (lines 208-239) verbatim and removes the dispatch branch, so the oracle never
   enters the fast path and never imports sglang. Verified by `split_rope_support_status`.

## Note on the config entry point

`config.toml [task].entry_points` lists
`sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_qknorm_split_rope`.
That symbol **does not exist** in upstream `main` at `aaa31eb0…` — it was part of
the closed PR #29399 and was never merged. The bit-exact reference is therefore
the eager path (`torch.nn.RMSNorm` + `apply_split_rotary_emb` eager fallback),
which the source prompt designates as the baseline. `apply_split_rotary_emb` IS
present upstream and is copied.

## Extracted exact semantics (the candidate must match these bit-for-bit)

### Operation order (LTX2Attention forward, TP world size = 1)

```
q = to_q(x); k = to_k(context)          # [B, S, H], bf16, H = num_heads * head_dim
q = q_norm(q); k = k_norm(k)            # torch.nn.RMSNorm(H, eps) over full H, bf16 weights
# cos is 4-D in production -> split variant:
q_out = apply_split_rotary_emb(q, (q_cos, q_sin))
k_out = apply_split_rotary_emb(k, (k_cos, k_sin))
```

### RMSNorm

- `torch.nn.RMSNorm(H, eps=eps)` with `elementwise_affine=True`, bf16 weight,
  normalizing over the **full hidden dim H** (NOT per-head). `eps = 1e-6` for all
  production rows.
- PyTorch upcasts to fp32 for the statistics and casts back to bf16; the exact
  rounding points (where the bf16 cast happens relative to the weight multiply,
  and whether the path is `rsqrt(mean+eps)` vs `sqrt`+reciprocal) MUST be
  characterized empirically on the B200 when authoring the candidate. The oracle
  calls `torch.nn.RMSNorm` directly, so it is correct by construction.
- For reference only, the TP>1 variant `LTX2TPRMSNormAcrossHeads` (lines 560-593)
  computes `var = x.float().pow(2).mean(-1)`, `inv = rsqrt(var + eps)`,
  `y = (x.float() * inv).to(bf16)`, `return y * weight.to(bf16)`. This is a
  DIFFERENT module and is NOT used (the task rejects TP != 1).

### Split RoPE (`apply_split_rotary_emb` eager fallback)

- Split is **half/half** along `head_dim` (first `head_dim/2` = `first_x`, second
  `head_dim/2` = `second_x`); **NOT interleaved**.
- cos/sin are `[B, num_heads, S, head_dim/2]`; broadcast over the 2-way split via
  `unsqueeze(-2)`.
- Exact arithmetic (bf16 tensors):
  - `out = split_x * cos_u` — bf16 elementwise multiply; `first_x*cos` and
    `second_x*cos` are **rounded to bf16 here**.
  - `first_out.addcmul_(-sin_u, second_x)` -> `first_x*cos - sin*second_x`.
  - `second_out.addcmul_(sin_u, first_x)` -> `second_x*cos + sin*first_x`.
- The first product is rounded to bf16 BEFORE the sine term is added; the
  `addcmul_` internal accumulation dtype (fp32 opmath vs bf16) MUST be confirmed
  empirically on the B200 — it dictates whether the candidate accumulates the
  sine term in fp32 then rounds once, or rounds in bf16. **Do not** contract
  `x*cos +/- y*sin` into one FMA; that can change the output bits.

### Non-contiguous cos/sin layout (production)

- Production cos/sin are stored physically as `[B, S, num_heads, head_dim/2]` and
  viewed transposed to `[B, num_heads, S, head_dim/2]`, so the head/seq dims have
  swapped strides while the last dim stays contiguous (stride 1). Example:
  `q_cos [2,32,1536,64]` has stride `[3145728, 64, 2048, 1]`.
- The candidate must index cos/sin via their real strides; assuming contiguous
  `[B, num_heads, S, head_dim/2]` is wrong. Last-dim stride != 1 is a reject case.

### Reject / fallback list (from the source prompt)

TP world size != 1; non-`torch.nn.RMSNorm`; `eps` mismatch; fp32 norm weights;
interleaved/non-split RoPE tensors; non-contiguous Q/K or cos/sin last dim; dtype
other than bf16. Encoded in `baseline/ltx2_split_rope.py:split_rope_support_status`
and (for norm inputs) validated by the adapter.

## Drift audit (DEC-2)

- Workloads were captured at SGLang commit `828411e6f1` (container
  `sglang_bbuf_pr29315`). The baseline is copied from the latest `main`
  (`aaa31eb0…`) per the diffusion-kernel rule.
- Status: DONE (best-effort). `828411e6f1` is not reachable on the public
  `sgl-project/sglang` remote (`git fetch origin 828411e6f1` → "couldn't find
  remote ref"); it is a PR-era container commit absent from public `main` history,
  so a direct function diff is not possible. This is acceptable because: (a) the
  bit-exactness gate compares candidate vs the eager oracle, **both** built from
  current `main` (`aaa31eb0…`), which is the integration target per the
  latest-`main` rule; (b) the captured workloads supply tensor **shapes** only —
  values are regenerated from seeds in `make_case` — so capture-time numeric
  semantics do not enter the comparison; (c) the eager `apply_split_rotary_emb`
  expression (`split_x*cos` then two `addcmul_`) is simple and stable. Residual
  risk is low. If a future integration pins a specific commit, re-run the diff
  against that commit.

## Pending user decisions in effect (defaults applied; see refined-plan.md)

- DEC-1: benchmark baseline = PyTorch eager fallback through a matched adapter.
- DEC-2: copy from latest `main` + drift audit vs `828411e6f1` (above).
- DEC-3: require production grid (num_heads=32, head_dim in {64,128}); treat
  head_dim=256 / num_heads in {8,16,24} as optional with clean reject.
