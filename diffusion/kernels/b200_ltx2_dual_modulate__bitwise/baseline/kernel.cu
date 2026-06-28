// Task-local PyTorch eager baseline for LTX2 dual modulation, exposed through the
// same destination-passing TVM-FFI CUDA ABI as the candidate (inputs first,
// scalar `double eps`, output tensors last; runs on torch's current CUDA stream).
//
// The upstream LTX2 path is pure PyTorch eager (RMSNormNoWeight -> F.rms_norm; see
// docs/baseline_source.md). This wrapper runs that exact eager sequence via ATen
// (`at::rms_norm` + the dual affine), so it is bit-identical to the independent
// oracle while sharing the candidate's ABI, build path, and validation.

#include "../ltx2_dual_modulate_common.cuh"

namespace {

using ltx2::as_tensor;
using ltx2::check_explicit_param;
using ltx2::check_output;
using ltx2::check_table;
using ltx2::check_temb;
using ltx2::check_x;
using ltx2::Dims;
using tvm::ffi::TensorView;

// [B, D] params broadcast over the sequence axis; insert it so broadcasting with
// x = [B, S, D] is valid for all three supported layouts.
inline at::Tensor bcast(const at::Tensor& p) {
  return p.dim() == 2 ? p.unsqueeze(1) : p;
}

void ltx2_dual_modulate_baseline(TensorView x, TensorView scale0, TensorView shift0,
                                 TensorView scale1, TensorView shift1, double eps,
                                 TensorView y0, TensorView y1) {
  Dims dm = check_x(x);
  check_explicit_param(scale0, dm, "scale0");
  check_explicit_param(shift0, dm, "shift0");
  check_explicit_param(scale1, dm, "scale1");
  check_explicit_param(shift1, dm, "shift1");
  check_output(y0, dm, "y0");
  check_output(y1, dm, "y1");

  at::Tensor xt = as_tensor(x);
  at::Tensor normed =
      at::rms_norm(xt, {dm.D}, c10::optional<at::Tensor>{}, c10::optional<double>(eps));
  at::Tensor o0 = as_tensor(y0), o1 = as_tensor(y1);
  o0.copy_(normed * (1 + bcast(as_tensor(scale0))) + bcast(as_tensor(shift0)));
  o1.copy_(normed * (1 + bcast(as_tensor(scale1))) + bcast(as_tensor(shift1)));
}

void ltx2_ca_dual_modulate_from_temb_baseline(TensorView x,
                                              TensorView temb_scale_shift,
                                              TensorView scale_shift_table,
                                              double eps, TensorView y0,
                                              TensorView y1) {
  Dims dm = check_x(x);
  int64_t temb_seq = check_temb(temb_scale_shift, dm);
  check_table(scale_shift_table, dm);
  check_output(y0, dm, "y0");
  check_output(y1, dm, "y1");

  at::Tensor xt = as_tensor(x);
  at::Tensor tb = as_tensor(temb_scale_shift);
  at::Tensor table = as_tensor(scale_shift_table);
  // scale_shift_table.to(x.dtype) -> [1,1,4,D] + temb -> [B,temb_seq,4,D].
  // reshape (not view) so a last-dim-contiguous but non-compact table row stride is
  // handled by an explicit copy, matching the candidate's row-stride indexing.
  at::Tensor combined = table.to(xt.scalar_type()).reshape({1, 1, 4, dm.D}) +
                        tb.reshape({dm.B, temb_seq, 4, dm.D});
  std::vector<at::Tensor> parts = combined.unbind(2);  // scale0, shift0, scale1, shift1
  at::Tensor normed =
      at::rms_norm(xt, {dm.D}, c10::optional<at::Tensor>{}, c10::optional<double>(eps));
  at::Tensor o0 = as_tensor(y0), o1 = as_tensor(y1);
  o0.copy_(normed * (1 + parts[0]) + parts[1]);
  o1.copy_(normed * (1 + parts[2]) + parts[3]);
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_dual_modulate_baseline,
                              ltx2_dual_modulate_baseline);
TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_ca_dual_modulate_from_temb_baseline,
                              ltx2_ca_dual_modulate_from_temb_baseline);
