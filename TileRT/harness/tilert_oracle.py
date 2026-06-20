"""TileRT per-op oracle + latency harness (DeepSeek-V3.2).

The shipped `libtilert_dsv32.so` registers every fused op as `torch.ops.tilert.*`
AND ships the Python `TileRTModule` wrappers, each of which provides:
  * `golden_forward(...)`  -> TileRT's own PyTorch reference (the correctness oracle
                              == the baseline a KDA candidate must match), and
  * `tilert_forward(...)`  -> the REAL fused kernel (correct weight swizzle handled
                              by `init_random_weights()` + `enable_tilert()`).

So for each op we instantiate the module, init random weights + vars, synthesize the
activation inputs, and compare golden vs tilert on the SAME inputs. That gives a
per-op, per-shape correctness oracle. Latency (the KDA target) is measured separately
with **ncu** (`gpu__time_duration.avg`) because eager per-op host overhead (~160us)
dwarfs the real kernel time — see `run_once.py` + `measure_ncu.py`.

Run inside container `sglang_bbuf` (py3.12, tilert 0.1.4):
    cd <task root>/harness && python tilert_oracle.py            # correctness sweep
    python tilert_oracle.py --op pure_mla --seq 1                # single op/shape
"""
from __future__ import annotations

import argparse
import math
import torch

import tilert

_INITED = False


def ensure_backend():
    global _INITED
    if _INITED:
        return
    tilert.load_backend("deepseek_v3_2")
    torch.ops.tilert.tilert_init_op()
    _INITED = True


def relerr(a: torch.Tensor, b: torch.Tensor) -> float:
    a, b = a.float(), b.float()
    return (a - b).norm().item() / (b.norm().item() + 1e-12)


def margs():
    from tilert.models.deepseek_v3_2.model_args import ModelArgs
    return ModelArgs()


# ---------------------------------------------------------------------------
# Op cases. Each builder returns dict(call=<single-launch fn for ncu>,
#   golden=<tensor>, tilert=<tensor>, compare="<name>", rel=<float>).
# Standalone (1-GPU) ops only; comm ops (allreduce/broadcast/receive) need NVLink
# peer setup and are handled separately (documented, not isolatable here).
# ---------------------------------------------------------------------------

def case_rmsnorm_quant(seq=1, dev="cuda:0", ct="general"):
    ensure_backend()
    D, block = 7168, 128
    hidden = torch.randn(1, seq, D, device=dev, dtype=torch.bfloat16)
    gamma = torch.randn(D, device=dev, dtype=torch.float32)
    hout = torch.zeros_like(hidden)
    qout = torch.zeros(1, seq, D, device=dev, dtype=torch.float8_e4m3fn)
    qscale = torch.zeros(1, seq, D // block, device=dev, dtype=torch.float32)
    pl = torch.zeros(66, 148, 16, dtype=torch.uint64, device=dev)
    tl = torch.zeros(66, 148, 16, dtype=torch.int64, device=dev)

    def call():
        torch.ops.tilert.rmsnorm_quant_op(hidden, gamma, hout, qout, qscale,
                                          "deepseek_v3_2", ct, pl, tl)
    call(); torch.cuda.synchronize()
    x = hidden.float()
    ref = (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * gamma
    return dict(call=call, golden=ref, tilert=hout, compare="hidden_out",
                rel=relerr(hout, ref))


def case_rmsnorm(seq=1, dev="cuda:0", ct="general"):
    ensure_backend()
    D = 7168
    hidden = torch.randn(1, seq, D, device=dev, dtype=torch.bfloat16)
    gamma = torch.randn(D, device=dev, dtype=torch.float32)
    hout = torch.zeros_like(hidden)
    pl = torch.zeros(66, 148, 16, dtype=torch.uint64, device=dev)

    def call():
        torch.ops.tilert.rmsnorm_op(hidden, gamma, hout, "deepseek_v3_2", ct, pl)
    call(); torch.cuda.synchronize()
    x = hidden.float()
    ref = (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * gamma
    return dict(call=call, golden=ref, tilert=hout, compare="hidden_out",
                rel=relerr(hout, ref))


def case_head_proj(seq=1, dev="cuda:0", ct="general"):
    ensure_backend()
    V, K = 16160, 7168
    h = torch.randn(1, seq, K, device=dev, dtype=torch.bfloat16) / K**0.5
    W = torch.randn(V, K, device=dev, dtype=torch.bfloat16) / K**0.5
    Wc = (W.reshape(V // 16, 16, K // 1024, 1024)
          .transpose(1, 2).reshape(V // 16 * K // 1024, 16, 1024).contiguous())
    out = torch.zeros(1, seq, V, device=dev, dtype=torch.float32)
    pl = torch.zeros(66, 148, 16, dtype=torch.uint64, device=dev)

    def call():
        torch.ops.tilert.head_proj_op(h, Wc, out, "deepseek_v3_2", ct, pl)
    call(); torch.cuda.synchronize()
    ref = h.float() @ W.float().T
    return dict(call=call, golden=ref, tilert=out, compare="logits",
                rel=relerr(out, ref))


# ---- module-class based cases (weight swizzle handled by the module) ----
# Interface facts (verified from source):
#  * call golden_forward(...) and tilert_forward(...) DIRECTLY (do NOT use
#    enable_tilert()/__call__ — __call__ is inconsistent across modules and
#    enable_tilert() calls a non-existent to_tilert_weights on some).
#  * constructor arg ORDER differs per module -> always pass kwargs.
#  * some modules have init_tilert_vars(b,seq); others allocate outputs inside
#    tilert_forward via bare torch.zeros -> wrap everything in `with torch.device`
#    so those land on the right GPU.
#  * golden/tilert may return a tuple -> pick the compared element by index.

def _run_module(make, acts_fn, seq, dev, init_vars=True, out_idx=-1, algo=None,
                post_init=None):
    ensure_backend()
    with torch.device(dev):
        m = make()
        if algo is not None:
            try:
                m.set_algorithm(algo)
            except Exception:
                pass
        m.init_random_weights()
        if post_init is not None:
            post_init(m)  # fix random-weight dtype quirks; keep golden==tilert weights
        if init_vars and hasattr(m, "init_tilert_vars"):
            try:
                m.init_tilert_vars(1, seq)
            except Exception:
                pass
        acts = acts_fn()
        golden = m.golden_forward(*acts)
        tilert = m.tilert_forward(*acts)
    torch.cuda.synchronize()
    g = golden[out_idx] if isinstance(golden, (tuple, list)) else golden
    t = tilert[out_idx] if isinstance(tilert, (tuple, list)) else tilert
    return dict(call=lambda: m.tilert_forward(*acts), golden=g, tilert=t,
                rel=relerr(t, g))


def case_rmsnorm_head_proj(seq=1, dev="cuda:0", ct="general"):
    from tilert.models.deepseek_v3_2.ops.rmsnorm_head_proj import RMSNormHeadProj
    a = margs()
    r = _run_module(
        lambda: RMSNormHeadProj(model_args=a, device_id=0, num_devices=8),
        lambda: (torch.randn(1, seq, a.dim, device=dev, dtype=torch.bfloat16) / a.dim**0.5,),
        seq, dev, init_vars=True, out_idx=-1)
    r["compare"] = "logits"
    return r


def _fix_expert_proj(m):
    # op wants bf16 gate weight; random path makes it f32. Use same bf16 weight in
    # golden (ref) and tilert so the comparison isolates kernel numerical error.
    wb = m.tilert_proj_weight.to(torch.bfloat16)
    m.tilert_proj_weight = wb
    m.ref_proj_weight = wb.float()


def case_rmsnorm_expert_proj(seq=1, dev="cuda:0", ct="bf16"):
    from tilert.models.deepseek_v3_2.ops.rmsnorm_expert_proj import RMSNormExpertProj
    a = margs()
    r = _run_module(
        lambda: RMSNormExpertProj(model_args=a, num_devices=8, device_id=0),
        lambda: (torch.randn(1, seq, a.dim, device=dev, dtype=torch.bfloat16) / a.dim**0.5,),
        seq, dev, init_vars=False, out_idx=-1, post_init=_fix_expert_proj)
    r["compare"] = "scores"
    return r


# ---- projections (clean single-activation modules) ----

def case_projx_wis(seq=1, dev="cuda:0", ct="bf16"):
    from tilert.models.deepseek_v3_2.ops.projx_wis import ProjxWis
    a = margs()
    r = _run_module(
        lambda: ProjxWis(model_args=a, num_devices=8, device_id=0),
        lambda: (torch.randn(1, seq, a.dim, device=dev, dtype=torch.bfloat16) / a.dim**0.5,),
        seq, dev, init_vars=True)
    r["compare"] = "idx_scores"
    return r


# MLA q/o projections shard 128 heads over 7 workers (GPU0 = indexer) -> 20 padded
# heads/worker (§14). Use num_devices=7 so the FP16MMA weight packer lays out 20 heads.
def case_projq_wqb(seq=1, dev="cuda:0", ct="fp16mma"):
    from tilert.models.deepseek_v3_2.ops.projq_wqb import ProjqWqb
    a = margs()
    mk = lambda: ProjqWqb(model_args=a, num_devices=7, device_id=0)
    H = mk().num_local_heads  # 20
    r = _run_module(
        mk,
        lambda: (torch.randn(1, seq, H, a.qk_nope_head_dim, device=dev, dtype=torch.bfloat16) / 8,),
        seq, dev, init_vars=True,
        post_init=lambda m: setattr(m, "ref_wkv_b", m.ref_wkv_b.to(torch.bfloat16)))
    r["compare"] = "q_kvlora"
    return r


def case_projo_wkvb(seq=1, dev="cuda:0", ct="fp16mma"):
    from tilert.models.deepseek_v3_2.ops.projo_wkvb import ProjoWKVb
    a = margs()
    mk = lambda: ProjoWKVb(model_args=a, num_devices=7, device_id=0)
    H = mk().num_local_heads  # 20
    r = _run_module(
        mk,
        lambda: (torch.randn(1, seq, H, a.kv_lora_rank, device=dev, dtype=torch.bfloat16) / 8,),
        seq, dev, init_vars=True,
        post_init=lambda m: setattr(m, "ref_wkv_b", m.ref_wkv_b.to(torch.bfloat16)))
    r["compare"] = "o_vhead"
    return r


# ---- MLA core (the #1 decode kernel, 52.8%) ----

def case_flash_sparse_mla(seq=1, dev="cuda:0", ct="bf16mma", kv_len=2048, heads=16):
    from tilert.models.deepseek_v3_2.ops.flash_sparse_mla import FlashSparseMLACombine
    a = margs()
    def acts():
        q_nope = torch.randn(1, seq, heads, a.kv_lora_rank, device=dev, dtype=torch.bfloat16) / 8
        q_pe = torch.randn(1, seq, heads, a.qk_rope_head_dim, device=dev, dtype=torch.bfloat16) / 8
        kv_cache = torch.randn(1, kv_len, a.kv_lora_rank, device=dev, dtype=torch.bfloat16) / 8
        pe_cache = torch.randn(1, kv_len, a.qk_rope_head_dim, device=dev, dtype=torch.bfloat16) / 8
        idx = torch.arange(kv_len, device=dev, dtype=torch.int32).view(1, 1, kv_len).expand(1, seq, kv_len).contiguous()
        cur_pos = torch.tensor([kv_len - seq], device=dev, dtype=torch.int32)
        return (q_nope, q_pe, kv_cache, pe_cache, idx, cur_pos)
    r = _run_module(
        lambda: FlashSparseMLACombine(model_args=a, num_devices=8),
        acts, seq, dev, init_vars=True)
    r["compare"] = "mla_out"
    return r


# ---- stateful KV-cache ops (separate golden/tilert caches) ----

_FREQS = {}

def _freqs(a, seq, dev, start=0):
    from tilert.models.utils import precompute_freqs_cis
    key = id(a)
    if key not in _FREQS:
        _FREQS[key] = precompute_freqs_cis(a)
    return _FREQS[key][start:start + seq].to(dev)


def case_rotate(seq=1, dev="cuda:0", ct="general"):
    from tilert.models.deepseek_v3_2.ops.rotate import Rotate
    a = margs()
    r = _run_module(
        lambda: Rotate(model_args=a, num_devices=1, device_id=0),
        lambda: (torch.randn(1, seq, a.index_n_heads, a.index_head_dim, device=dev, dtype=torch.bfloat16),
                 _freqs(a, seq, dev)),
        seq, dev, init_vars=True)
    r["compare"] = "rotated"
    return r


def case_qkv_rope(seq=1, dev="cuda:0", ct="general"):
    from tilert.models.deepseek_v3_2.ops.qkv_rope import QKVRoPE
    ensure_backend()
    a = margs()
    H = a.n_heads // 8
    with torch.device(dev):
        m = QKVRoPE(model_args=a, num_devices=8, device_id=0)
        m.init_random_weights(); m.init_tilert_vars(1, seq)
        q_pe = torch.randn(1, seq, H, a.qk_rope_head_dim, device=dev, dtype=torch.bfloat16)
        fc = _freqs(a, seq, dev).unsqueeze(0)  # [1, seq, 32] -> op wants rope_freqs [1,seq,64]
        pe_g = torch.randn(1, seq, a.qk_rope_head_dim, device=dev, dtype=torch.bfloat16)
        pe_t = pe_g.clone()
        g = m.golden_forward(q_pe.clone(), pe_g, 0, fc, 1, seq)
        t = m.tilert_forward(q_pe.clone(), pe_t, 0, fc, 1, seq)
    torch.cuda.synchronize()
    rel = relerr(t, g)
    rel_cache = relerr(pe_t, pe_g)
    return dict(call=lambda: m.tilert_forward(q_pe.clone(), pe_t.clone(), 0, fc, 1, seq),
                golden=g, tilert=t, compare="q_pe_rot(+cache %.1e)" % rel_cache, rel=max(rel, rel_cache))


def case_rmsnorm_kv(seq=1, dev="cuda:0", ct="general"):
    from tilert.models.deepseek_v3_2.ops.rmsnorm_kv import KVRMSNorm
    ensure_backend()
    a = margs()
    with torch.device(dev):
        m = KVRMSNorm(model_args=a, num_devices=8, device_id=0)
        m.init_random_weights(); m.init_tilert_vars(1, seq)
        kv = torch.randn(1, seq, a.kv_lora_rank, device=dev, dtype=torch.bfloat16)
        cache_g = torch.zeros(1, max(seq, 16), a.kv_lora_rank, device=dev, dtype=torch.bfloat16)
        cache_t = cache_g.clone()
        m.golden_forward(kv, cache_g, 0, 1, seq)
        m.tilert_forward(kv, cache_t, 0, 1, seq)
    torch.cuda.synchronize()
    g = cache_g[:, :seq]; t = cache_t[:, :seq]
    return dict(call=lambda: m.tilert_forward(kv, cache_t, 0, 1, seq), golden=g, tilert=t,
                compare="kv_cache", rel=relerr(t, g))


def case_rmsnorm_up_gate_silu(seq=1, dev="cuda:0", ct="fp8mma"):
    from tilert.models.deepseek_v3_2.ops.rmsnorm_up_gate_silu import RMSNormUpGateSiLU, RMSNormUpGateSiLUAlgorithm
    a = margs()
    r = _run_module(
        lambda: RMSNormUpGateSiLU(model_args=a, device_id=0, num_devices=8),
        lambda: (torch.randn(1, seq, a.dim, device=dev, dtype=torch.bfloat16) / a.dim**0.5,),
        seq, dev, init_vars=True, out_idx=-1, algo=RMSNormUpGateSiLUAlgorithm.FP8MMA)
    r["compare"] = "up_gate_silu"
    return r


def case_layernorm_rope_rotate(seq=1, dev="cuda:0", ct="general"):
    from tilert.models.deepseek_v3_2.ops.layernorm_rope_rotate import LayerNormRoPERotate
    a = margs()
    r = _run_module(
        lambda: LayerNormRoPERotate(model_args=a, num_devices=8, device_id=0),
        lambda: (torch.randn(1, seq, a.index_head_dim, device=dev, dtype=torch.bfloat16),
                 _freqs(a, seq, dev)),
        seq, dev, init_vars=True)
    r["compare"] = "k_idx_cache"
    return r


def case_rmsnorm_projq_wqb(seq=1, dev="cuda:0", ct="fp16mma"):
    from tilert.models.deepseek_v3_2.ops.rmsnorm_projq_wqb import RmsnormProjqWqb, RmsnormProjqWqbAlgorithm
    a = margs()
    r = _run_module(
        lambda: RmsnormProjqWqb(model_args=a, device_id=0, num_devices=7),
        lambda: (torch.randn(1, seq, a.q_lora_rank, device=dev, dtype=torch.bfloat16) / 8,),
        seq, dev, init_vars=True, out_idx=0, algo=RmsnormProjqWqbAlgorithm.FP16MMA,
        post_init=lambda m: setattr(m, 'ref_wq_b', m.ref_wq_b.to(torch.bfloat16)))
    r["compare"] = "q_nope"
    return r


def case_rmsnorm_projq_wqi(seq=1, dev="cuda:0", ct="fp16mma"):
    from tilert.models.deepseek_v3_2.ops.rmsnorm_projq_wqi import RmsnormProjqWqi, RmsnormProjqWqiAlgorithm
    a = margs()
    r = _run_module(
        lambda: RmsnormProjqWqi(model_args=a, device_id=0, num_devices=8),
        lambda: (torch.randn(1, seq, a.q_lora_rank, device=dev, dtype=torch.bfloat16) / 8,),
        seq, dev, init_vars=True, out_idx=-1, algo=RmsnormProjqWqiAlgorithm.FP16MMA,
        post_init=lambda m: setattr(m, 'ref_wqi', m.ref_wqi.to(torch.bfloat16)))
    r["compare"] = "iq"
    return r


CASES = {
    "rmsnorm": case_rmsnorm,
    "rmsnorm_quant": case_rmsnorm_quant,
    "head_proj": case_head_proj,
    "rmsnorm_head_proj": case_rmsnorm_head_proj,
    "rmsnorm_expert_proj": case_rmsnorm_expert_proj,
    "projx_wis": case_projx_wis,
    "projq_wqb": case_projq_wqb,
    "projo_wkvb": case_projo_wkvb,
    "flash_sparse_mla": case_flash_sparse_mla,
    "rotate": case_rotate,
    "qkv_rope": case_qkv_rope,
    "rmsnorm_kv": case_rmsnorm_kv,
    "layernorm_rope_rotate": case_layernorm_rope_rotate,
    "rmsnorm_projq_wqb": case_rmsnorm_projq_wqb,
    "rmsnorm_projq_wqi": case_rmsnorm_projq_wqi,
    "rmsnorm_up_gate_silu": case_rmsnorm_up_gate_silu,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--op", default=None)
    ap.add_argument("--seq", type=int, default=1)
    ap.add_argument("--dev", default="cuda:0")
    args = ap.parse_args()
    print("torch", torch.__version__, "|", torch.cuda.get_device_name(0))
    names = [args.op] if args.op else list(CASES)
    for name in names:
        for seq in ([args.seq] if args.op else [1, 2, 4]):
            try:
                r = CASES[name](seq=seq, dev=args.dev)
                print(f"[{name:>20} s{seq}] rel({r['compare']})={r['rel']:.2e}")
            except Exception as e:
                print(f"[{name:>20} s{seq}] ERROR {type(e).__name__}: {str(e)[:160]}")


if __name__ == "__main__":
    main()
