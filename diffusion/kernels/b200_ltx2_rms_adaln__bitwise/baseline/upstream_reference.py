"""Recovered upstream SGLang reference for b200_ltx2_rms_adaln__bitwise.

This is a PROVENANCE / contract-reference artifact only. It is NOT imported at
correctness or benchmark runtime (the standalone contract forbids importing
sglang). The numeric oracle is plain PyTorch eager; see bench/correctness.py.
Full provenance: docs/baseline_source.md.

  repo:   https://github.com/sgl-project/sglang
  branch: main
  commit: aaa31eb0a11e09f9511bade5e815907ec0b91fa0   (resolved 2026-06-29 UTC)
  source files (verbatim sha256 of the fetched upstream files):
    python/sglang/multimodal_gen/runtime/layers/layernorm.py
      e4389a39497f0191c02f1398dc3a6d6325263d8a326eb58b96c72fb0a8482943
    python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py
      ff3fd96e8df346a82840a18a00f2702b8b7d02bc1950fbfcebfe3d760bde0141

NOTE on entry-point names: config.toml names the entry points
`_ltx2_rms_adaln` and `_ltx2_try_fused_rms_adaln`. NEITHER symbol exists in
upstream `main` at the resolved commit (grep count 0). They were the *proposed*
fused helpers of the closed PR sgl-project/sglang#29396 (never merged). The real
upstream semantics live inline at the modulation callsites, over
`RMSNormNoWeight`. The recovered baseline is therefore the inline eager pattern
below, which is what the task must match bit-for-bit.

================================================================================
layernorm.py  (lines 298-307, verbatim)
================================================================================
    @CustomOp.register("rms_norm_no_weight")
    class RMSNormNoWeight(CustomOp):
        def forward_native(self, x: torch.Tensor, eps: float) -> torch.Tensor:
            return F.rms_norm(x, normalized_shape=(x.shape[-1],), eps=eps)

        def forward_cuda(self, x: torch.Tensor, eps: float) -> torch.Tensor:
            return self.forward_native(x, eps=eps)   # production CUDA path == eager

        def forward_npu(self, x: torch.Tensor, eps: float) -> torch.Tensor:
            return fused_rmsnorm_without_weight(x, eps)

================================================================================
ltx_2.py  (relevant lines, verbatim)
================================================================================
    norm_eps: float = 1e-6                 # default (lines 603, 932)
    self.norm_eps = float(norm_eps)        # line 619 (also 944)
    self.rms_norm = RMSNormNoWeight()      # line 945

    # video MSA callsite (lines 1134-1136); audio MSA (1156-1159), prompt-Q
    # (1188, 1215), MLP (1365, 1377) are all the same shape:
    norm_hidden_states = (
        self.rms_norm(hidden_states, self.norm_eps) * (1 + vscale_msa) + vshift_msa
    )

================================================================================
Recovered task-local eager baseline semantics (bf16 inputs, eps default 1e-6):

    normed = torch.nn.functional.rms_norm(x, normalized_shape=(D,), eps=eps)
    y = normed * (1 + scale) + shift

Operation boundaries (PyTorch eager, each rounds to bf16):
    1) normed   = rms_norm(x, (D,), eps)        # fp32 reduction, store bf16
    2) one_plus = (1 + scale)                   # bf16
    3) mul      = normed * one_plus             # bf16
    4) y        = mul + shift                   # bf16
================================================================================
"""
