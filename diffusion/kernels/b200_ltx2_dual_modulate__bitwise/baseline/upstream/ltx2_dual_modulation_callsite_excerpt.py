# Source-context excerpt copied verbatim from upstream SGLang.
#
# Repository : https://github.com/sgl-project/sglang
# Branch     : main
# Commit     : aaa31eb0a11e09f9511bade5e815907ec0b91fa0  (2026-06-28)
# File       : python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py
# Class      : LTX2TransformerBlock  (the prompt's "LTX2VideoTransformerBlock"
#              name is historical; the current block class is LTX2TransformerBlock)
#
# NOTE ON PR #29392: the prompt references helper functions
# `_ltx2_try_fused_rmsnorm_dual_modulate` and
# `_ltx2_try_fused_rmsnorm_ca_dual_modulate`. These do NOT exist on `main` at the
# resolved commit (PR #29392 "[Diffusion] Fuse LTX2 dual modulation" was closed,
# not merged). The eager modulation lives directly in LTX2TransformerBlock.forward.
#
# This file is reference context only. It is NOT imported at runtime.

# ---- EXPLICIT dual modulation (the recurring eager pattern in forward) ----
# normed scale/shift applied as, e.g. (lines ~1135, 1188, 1365):
#
#   self.rms_norm(hidden_states, self.norm_eps) * (1 + vscale_msa) + vshift_msa
#
# where (vscale_*, vshift_*) come from an ada-values split of a scale_shift_table.
# Generalized by the task prompt to the dual form:
#   normed = F.rms_norm(x, (D,), eps)
#   y0 = normed * (1 + scale0.expand_as(x)) + shift0.expand_as(x)
#   y1 = normed * (1 + scale1.expand_as(x)) + shift1.expand_as(x)

# ---- CROSS-ATTENTION dual modulation from temb (lines 1246-1305 @ aaa31eb0) ----
#
#   norm_hidden_states = self.rms_norm(hidden_states, self.norm_eps)
#   ...
#   video_per_layer_ca_scale_shift = self.video_a2v_cross_attn_scale_shift_table[:4, :]
#   video_ca_scale_shift_table = (
#       video_per_layer_ca_scale_shift[None, None, :, :].to(
#           dtype=temb_ca_scale_shift.dtype, device=temb_ca_scale_shift.device
#       )
#       + temb_ca_scale_shift.reshape(batch_size, temb_ca_scale_shift.shape[1], 4, -1)
#   ).unbind(dim=2)
#   (video_a2v_ca_scale, video_a2v_ca_shift,
#    video_v2a_ca_scale, video_v2a_ca_shift) = [t.squeeze(2) for t in video_ca_scale_shift_table]
#
# The task scope is exactly the dual-modulation (scale0/shift0/scale1/shift1)
# part. The per-layer GATE rows (video_a2v_cross_attn_scale_shift_table[4:, :])
# and the trailing `.squeeze(2)` belong to the surrounding block and are OUT OF
# SCOPE. The task prompt's compact form is the authoritative baseline:
#   scale0, shift0, scale1, shift1 = (
#       scale_shift_table.to(dtype=x.dtype).view(1, 1, 4, D)
#       + temb_scale_shift.reshape(B, temb_seq, 4, D)
#   ).unbind(dim=2)
#   normed = F.rms_norm(x, (D,), eps)
#   y0 = normed * (1 + scale0) + shift0
#   y1 = normed * (1 + scale1) + shift1
