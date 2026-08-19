"""Baseline wrapper for `qwen38_nvfp4__gdn_sigmoid_gating_verify`."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {
    "sglang.kernels.ops.attention.fla.fused_sigmoid_gating_recurrent": "kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py",
    "sglang.kernels.ops.attention.triton_gdn_fused_proj": "kernels/ops/attention/triton_gdn_fused_proj.py",
    "sglang.kernels.ops.mamba.causal_conv1d_triton": "kernels/ops/mamba/causal_conv1d_triton.py",
}

def _sym(module, attr):
    return load(module, attr, __file__, COPIED.get(module, ""))

OPS = {
    "qwen38_gdn_gating_update": lambda **kw: _sym("sglang.kernels.ops.attention.fla.fused_sigmoid_gating_recurrent", "fused_sigmoid_gating_delta_rule_update")(**kw),
    "qwen38_qkvzba_split": lambda **kw: _sym("sglang.kernels.ops.attention.triton_gdn_fused_proj", "fused_qkvzba_split_reshape_cat_contiguous")(**kw),
    "qwen38_conv1d_update": lambda **kw: _sym("sglang.kernels.ops.mamba.causal_conv1d_triton", "causal_conv1d_update")(**kw),
}
RECONSTRUCT: dict = {}
