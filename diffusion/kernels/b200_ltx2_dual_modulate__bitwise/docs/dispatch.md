# Dispatch / Fallback

The candidate uses **one generic kernel pair** (one kernel for explicit dual modulation,
one templated kernel for CA-from-temb). It is NOT shape-specialized: a single
implementation wins on every production bucket (`S∈{126,1536,6144,8160,32640}`, video and
audio, explicit and CA), so there is no per-`(B,S,D)` kernel selection.

The only runtime dispatch is an **alignment-based fast-path / fallback** for the
memory-access width:

| Path | Condition | Behavior |
|---|---|---|
| Vectorized (`*_affine_kernel_vec`) | base pointers of `normed`, `y0`, `y1` are 16-byte aligned | Moves the dominant compact traffic (`normed` read, `y0`/`y1` writes) as 16-byte `int4` vectors (8 bf16/thread). |
| Scalar (`*_affine_kernel_scalar`) | otherwise | One bf16 element per thread. |

Why this is safe and bit-identical:

- `D` is validated to be a multiple of 256, so the total element count is a multiple of the
  vector width (8) and every row boundary is vector-aligned; there is no vector remainder.
- `normed` (`= at::rms_norm(...).contiguous()`) and the compact outputs are freshly
  allocated and always 16-byte aligned in practice, so the vectorized path is taken for all
  production and regression inputs. The scalar path exists only as a safety fallback for a
  hypothetical non-16-byte-aligned output buffer.
- Vectorization changes **only the load/store width**, never the arithmetic: each element
  is computed by the identical per-element fp32-opmath + bf16-rounding affine. The
  correctness gate confirms **both** paths are bit-exact (1819/0): the vector path on all
  aligned production/regression cases, and the scalar path via a dedicated check that
  forces it with a deliberately misaligned (non-16-byte) compact output.

Unsupported inputs (non-CUDA, non-bf16 `x`, non-contiguous last dim, `D` not divisible by
256 or `> 8192`, parameter-size mismatch, non-contiguous `temb`, non-compact outputs) are
**rejected** identically to the baseline via the shared `ltx2_dual_modulate_common.cuh`
validation — there is no approximate path.

No production shape falls back to exact eager: every one is bit-exact and faster, so no
"tie" rows are reported.
