#include <torch/extension.h>

#include <c10/cuda/CUDAStream.h>

void launch_fused_quant(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    const void* mask,
    int rows,
    int columns,
    int grid_size,
    int block_size,
    cudaStream_t stream);

void launch_small_quant(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    int rows,
    int grid_size,
    int block_size,
    cudaStream_t stream);

void launch_silu_small(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    int rows,
    int grid_size,
    int block_size,
    cudaStream_t stream);

void launch_silu_swizzled_4096(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    cudaStream_t stream);

void launch_silu_swizzled_half8_4096(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    cudaStream_t stream);

void launch_silu_swizzled_4369(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    cudaStream_t stream);

void launch_reduce_down_split(
    void* output,
    const void* partials,
    int rows,
    int splits,
    cudaStream_t stream);

void reduce_down_split(torch::Tensor output, torch::Tensor partials) {
  launch_reduce_down_split(
      output.data_ptr(),
      partials.data_ptr(),
      output.size(0),
      partials.size(0),
      c10::cuda::getCurrentCUDAStream(output.get_device()));
}

void small_quant(
    torch::Tensor output,
    torch::Tensor output_scales,
    torch::Tensor input,
    torch::Tensor global_scale,
    int grid_size,
    int block_size) {
  launch_small_quant(
      output.data_ptr(),
      output_scales.data_ptr(),
      input.data_ptr(),
      global_scale.data_ptr(),
      input.size(0),
      grid_size,
      block_size,
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

void fused_quant(
    torch::Tensor output,
    torch::Tensor output_scales,
    torch::Tensor input,
    torch::Tensor global_scale,
    torch::Tensor mask,
    int grid_size,
    int block_size) {
  launch_fused_quant(
      output.data_ptr(),
      output_scales.data_ptr(),
      input.data_ptr(),
      global_scale.data_ptr(),
      mask.data_ptr(),
      input.size(1),
      input.size(2) / 2,
      grid_size,
      block_size,
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

void silu_small(
    torch::Tensor output,
    torch::Tensor output_scales,
    torch::Tensor input,
    torch::Tensor global_scale,
    int grid_size,
    int block_size) {
  launch_silu_small(
      output.data_ptr(),
      output_scales.data_ptr(),
      input.data_ptr(),
      global_scale.data_ptr(),
      input.size(1),
      grid_size,
      block_size,
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

void silu_swizzled_4096(
    torch::Tensor output,
    torch::Tensor output_scales,
    torch::Tensor input,
    torch::Tensor global_scale) {
  launch_silu_swizzled_4096(
      output.data_ptr(),
      output_scales.data_ptr(),
      input.data_ptr(),
      global_scale.data_ptr(),
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

void silu_swizzled_half8_4096(
    torch::Tensor output,
    torch::Tensor output_scales,
    torch::Tensor input,
    torch::Tensor global_scale) {
  launch_silu_swizzled_half8_4096(
      output.data_ptr(),
      output_scales.data_ptr(),
      input.data_ptr(),
      global_scale.data_ptr(),
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

void silu_swizzled_4369(
    torch::Tensor output,
    torch::Tensor output_scales,
    torch::Tensor input,
    torch::Tensor global_scale) {
  launch_silu_swizzled_4369(
      output.data_ptr(),
      output_scales.data_ptr(),
      input.data_ptr(),
      global_scale.data_ptr(),
      c10::cuda::getCurrentCUDAStream(input.get_device()));
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, module) {
  module.def("fused_quant", &fused_quant);
  module.def("small_quant", &small_quant);
  module.def("silu_small", &silu_small);
  module.def("silu_swizzled_4096", &silu_swizzled_4096);
  module.def("silu_swizzled_half8_4096", &silu_swizzled_half8_4096);
  module.def("silu_swizzled_4369", &silu_swizzled_4369);
  module.def("reduce_down_split", &reduce_down_split);
}
