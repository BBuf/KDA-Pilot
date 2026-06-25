# Baseline Source Lineage

## Upstream provenance

- Repository: `https://github.com/sgl-project/sglang`
- Branch: `main`
- Resolved commit SHA: `8314247d9de0fa2c58e34756b3e1dbc6cf815dfd`
- Resolution method: `git ls-remote https://github.com/sgl-project/sglang.git refs/heads/main`
- Resolution time: 2026-06-25 (UTC), at baseline-recovery time for this task.
- Fetch method: raw file fetch at the resolved commit
  (`https://raw.githubusercontent.com/sgl-project/sglang/8314247d9de0fa2c58e34756b3e1dbc6cf815dfd/python/sglang/multimodal_gen/runtime/models/dits/<file>.py`).
- Pin note: an earlier resolution during this task returned
  `67b2a9ed0cfba8ec625d3f26548e502646fd914d`; upstream `main` advanced to
  `8314247d…` shortly after. The residual-gate (`residual + update*gate`) and the
  LTX 4D broadcast-add expressions in `ltx_2.py` / `ideogram.py` / `flux_2.py`
  are byte-identical between the two commits (verified by diffing the relevant
  lines), so the recovered semantics are unaffected. This task pins to
  `8314247d…` as the baseline-recovery commit.

## Copied / referenced upstream files (at the resolved commit)

| Upstream path | Role | Relevant lines |
|---|---|---|
| `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` | LTX-2 DiT blocks: residual-gate updates and the 4D cross-attn-gate broadcast add | `residual+update*gate` at 1031, 1048, 1073, 1097, 1198, 1222; 4D broadcast at 1126-1140 |
| `python/sglang/multimodal_gen/runtime/models/dits/ideogram.py` | Ideogram4 DiT block: `x = x + gate * norm(sublayer(x))` | 327-337 |
| `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py` | FLUX.2 single/double-stream blocks: modulation residual gate | 755, 873, 880, 883, 892 |

The verbatim relevant excerpts (with line numbers) are preserved in
`baseline/upstream_residual_gate_snippets.md` for provenance/evidence. These full
model files are NOT copied wholesale into `baseline/` because they contain large
amounts of unrelated model code; the standalone baseline is the elementwise
expression itself (see "Baseline implementation" below).

## K — Kernel semantics and callsite contract (recovered)

Two elementwise operator families, all bf16 in production:

- `residual_gate_add`: `out = residual + update * gate` (the multiply is commutative;
  upstream writes both `residual + update * gate` and `residual + gate * update`).
  - LTX-2: `hidden_states = hidden_states + attn_hidden_states * vgate_msa` (gate is `[B,1,D]` or `[B,L,D]`).
  - Ideogram4: `x = x + gate_msa * self.attention_norm2(attn_out)` and `x = x + gate_mlp * self.ffn_norm2(...)` (gate `[B,1,D]`, tanh-gated upstream; the gate tensor is passed in already-computed).
  - FLUX.2: `hidden_states = hidden_states + mod_gate * attn_output`, `+ gate_mlp * ff_output`, `+ c_gate_mlp * context_ff_output` (gate `[B,1,D]`).
  - `gate` appears in two shapes: full `[B,L,D]` (equal to `residual`) and row-broadcast `[B,1,D]`.
- `broadcast_add_4d`: LTX-2 cross-attn gate/scale-shift table construction,
  `out = per_layer_table[None, None, :, :] + temb.reshape(B, S, P, D)`, i.e.
  `a=[1,1,P,D]` broadcasts over the sequence dim against `b=[1,S,P,D]`.
  Production row: `a=[1,1,3,2048]`, `b=[1,126,3,2048]`, `out=[1,126,3,2048]`;
  `out[0,s,p,d] = a[0,0,p,d] + b[0,s,p,d]`.

### Supported shape contract: batch size 1 (B=1)

Every frozen production row is B=1, so the standalone kernel ABI deliberately
supports only B=1: `residual_gate_add` accepts a full gate `[1,L,D]` or a
row-broadcast gate `[1,1,D]`; `broadcast_add_4d` accepts `a=[1,1,P,D]`,
`b=[1,S,P,D]`. A true batched broadcast (B>1 — e.g. gate `[B,1,D]` or
`b=[B,S,P,D]` with B>1, which eager PyTorch would broadcast per batch) is OUT OF
SCOPE and is rejected on BOTH sides: the candidate via its CUDA host checks, and
the eager baseline via the shared `bench/adapter.py::_validate` (which runs before
either implementation). This keeps the ABI symmetric and reward-hack-resistant;
the `rga-gate-leaddim-not1` and `bcast-batch-gt1` rejection tests cover it.
Supporting B>1 would add per-vector batch index arithmetic to the
bandwidth-critical path for a shape absent from the frozen workload, so it is
documented as out-of-scope rather than implemented.

These callsites are PyTorch-eager elementwise ops. The torch profiler (see
`../../docs/sglang_recent_diffusion_b200_profile_audit_2026-06-24.md`) shows them
as separate `aten::mul` then `aten::add` launches plus a hot 4D broadcast add.

## R — Correctness oracle and baseline path

- Oracle (fp32, one-round): `residual_gate_add` -> `(residual.float() + update.float() * gate.float()).to(out_dtype)`;
  `broadcast_add_4d` -> `(a.float() + b.float()).to(out_dtype)` with `a` broadcast over the seq dim.
- Baseline implementation (faithful eager): `baseline/binding.py` reproduces the
  profiled two-op eager path (`update*gate` into a cached preallocated scratch buffer,
  then `+residual` into the output) for `residual_gate_add`, and a single eager broadcast
  add for `broadcast_add_4d`. Exposed through a destination-passing ABI identical to the
  candidate (output passed last, current CUDA stream, no allocation in the timed steady
  state). No `sglang` import at correctness/benchmark runtime.

## W — Workload shape set and benchmark methodology

- The 8 frozen production rows are in `bench/workloads.json`, matching the
  `diffusion_residual_gate_add__multi_shape` section of
  `../../docs/diffusion_benchmark_shape_coverage.md` (source of truth).
- Benchmark methodology follows `../../docs/standalone_diffusion_benchmark.md`
  and starts `bench/benchmark.py` from `../../docs/standalone_diffusion_benchmark_template.py`.

## Local edits

- None to upstream source (the relevant expressions are reproduced in `baseline/binding.py`
  as the local baseline; upstream excerpts are preserved verbatim for provenance only).
