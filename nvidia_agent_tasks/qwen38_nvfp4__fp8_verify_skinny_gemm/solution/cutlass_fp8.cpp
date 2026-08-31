#include <torch/extension.h>

#include <c10/cuda/CUDAStream.h>

void launch_cutlass_fp8_m9(
    void* output,
    const void* activation,
    const void* weight,
    const void* input_scale,
    const void* weight_scale,
    int n,
    int k,
    cudaStream_t stream);

void launch_cutlass_fp8_m1(
    void* output,
    const void* activation,
    const void* weight,
    const void* alpha,
    int n,
    int k,
    cudaStream_t stream);

void cutlass_fp8_m9(
    torch::Tensor output,
    torch::Tensor activation,
    torch::Tensor weight,
    torch::Tensor input_scale,
    torch::Tensor weight_scale) {
  launch_cutlass_fp8_m9(
      output.data_ptr(),
      activation.data_ptr(),
      weight.data_ptr(),
      input_scale.data_ptr(),
      weight_scale.data_ptr(),
      output.size(1),
      activation.size(1),
      c10::cuda::getCurrentCUDAStream(activation.get_device()));
}

void cutlass_fp8_m1(
    torch::Tensor output,
    torch::Tensor activation,
    torch::Tensor weight,
    torch::Tensor alpha) {
  launch_cutlass_fp8_m1(
      output.data_ptr(),
      activation.data_ptr(),
      weight.data_ptr(),
      alpha.data_ptr(),
      output.size(1),
      activation.size(1),
      c10::cuda::getCurrentCUDAStream(activation.get_device()));
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, module) {
  module.def("fp8_m1", &cutlass_fp8_m1);
  module.def("fp8_m9", &cutlass_fp8_m9);
}
