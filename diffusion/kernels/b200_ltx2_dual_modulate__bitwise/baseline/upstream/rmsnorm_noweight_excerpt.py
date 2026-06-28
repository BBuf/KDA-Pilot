# Source-context excerpt copied verbatim from upstream SGLang.
#
# Repository : https://github.com/sgl-project/sglang
# Branch     : main
# Commit     : aaa31eb0a11e09f9511bade5e815907ec0b91fa0  (2026-06-28)
# File       : python/sglang/multimodal_gen/runtime/layers/layernorm.py
#
# Purpose: document the EXACT normalization used by the LTX2 dual-modulation
# callsite. `LTX2TransformerBlock.__init__` sets `self.rms_norm =
# RMSNormNoWeight()`, and on CUDA that resolves (via CustomOp dispatch) to
# `forward_cuda -> forward_native -> torch.nn.functional.rms_norm`. Therefore the
# production B200 normalization is bit-for-bit `F.rms_norm(x, (D,), eps)`, which
# is exactly the baseline the task prompt specifies. Matching it preserves the
# diffusion CI golden outputs.
#
# This file is reference context only. It is NOT imported at correctness or
# benchmark runtime (the standalone benchmark contract forbids importing SGLang).

# ---- RMSNormNoWeight (layernorm.py, lines 299-307 @ aaa31eb0) ----
#
# class RMSNormNoWeight(CustomOp):
#     def forward_native(self, x: torch.Tensor, eps: float) -> torch.Tensor:
#         return F.rms_norm(x, normalized_shape=(x.shape[-1],), eps=eps)
#
#     def forward_cuda(self, x: torch.Tensor, eps: float) -> torch.Tensor:
#         return self.forward_native(x, eps=eps)
#
#     def forward_npu(self, x: torch.Tensor, eps: float) -> torch.Tensor:
#         return fused_rmsnorm_without_weight(x, eps)
#
# ---- For reference: the weighted RMSNorm.forward_native (layernorm.py ~127-160)
# upcasts to fp32, computes variance = x.pow(2).mean(-1, keepdim=True),
# x = x * rsqrt(variance + eps), then casts back to the original dtype. This is
# the same math F.rms_norm performs; RMSNormNoWeight simply omits the weight.
