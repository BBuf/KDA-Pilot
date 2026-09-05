#include <torch/extension.h>

#include <c10/cuda/CUDAStream.h>

void launch_fp8_gemv(
    void* output,
    const void* input,
    const void* weight,
    const void* alpha,
    int n,
    int k,
    cudaStream_t stream);

void launch_fp8_linear(
    void* output,
    void* quantized_input,
    const void* input,
    const void* weight,
    const void* weight_scale,
    const void* input_scale,
    int n,
    int k,
    cudaStream_t stream);

void launch_fp8_quantize(
    void* quantized_input,
    const void* input,
    const void* input_scale,
    const void* weight,
    int n,
    int k,
    cudaStream_t stream);

void fp8_gemv(
    torch::Tensor output,
    torch::Tensor input,
    torch::Tensor weight,
    torch::Tensor alpha) {
  launch_fp8_gemv(
      output.data_ptr(),
      input.data_ptr(),
      weight.data_ptr(),
      alpha.data_ptr(),
      output.size(1),
      input.size(1),
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

void fp8_linear(
    torch::Tensor output,
    torch::Tensor quantized_input,
    torch::Tensor input,
    torch::Tensor weight,
    torch::Tensor weight_scale,
    torch::Tensor input_scale) {
  launch_fp8_linear(
      output.data_ptr(),
      quantized_input.data_ptr(),
      input.data_ptr(),
      weight.data_ptr(),
      weight_scale.data_ptr(),
      input_scale.data_ptr(),
      output.size(1),
      input.size(1),
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

void fp8_quantize(
    torch::Tensor quantized_input,
    torch::Tensor input,
    torch::Tensor input_scale,
    torch::Tensor weight) {
  launch_fp8_quantize(
      quantized_input.data_ptr(),
      input.data_ptr(),
      input_scale.data_ptr(),
      weight.data_ptr(),
      weight.size(1),
      input.size(1),
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, module) {
  module.def("fp8_gemv", &fp8_gemv);
  module.def("fp8_linear", &fp8_linear);
  module.def("fp8_quantize", &fp8_quantize);
}
