# KDA Prompt: memory_bound__unrolled_elementwise_kernel__64bf90af3d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`memory_bound` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.5-1T`
- Model folder: `llm/ring_25_1t/b200`
- Kernel category: `memory_bound`
- Max observed GPU share: `4.96%`
- Kernel name: `void at::native::unrolled_elementwise_kernel<at::native::direct_copy_kernel_cuda(at::TensorIteratorBase&)::{lambda()#3}::operator()() const::{lambda()#7}::operator()() const::{lambda(float)#1}, std::array<char*, 2ul>, 4, TrivialOffsetCalculator<1, unsigned int>, TrivialOffsetCalculator<1, unsigned int>, at::native::memory::LoadWithCast<1>, at::native::memory::StoreWithCast<1> >(int, at::native::direct_copy_kernel_cuda(at::TensorIteratorBase&)::{lambda()#3}::operator()() const::{lambda()#7}::operator()() const::{lambda(float)#1}, std::array<char*, 2ul>, TrivialOffsetCalculator<1, unsigned int>, TrivialOffsetCalculator<1, unsigned int>, at::native::memory::LoadWithCast<1>, at::native::memory::StoreWithCast<1>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 4.96% GPU, calls=16056, mean=42.62 us
- `sharegpt_mid`: 4.01% GPU, calls=16056, mean=20.69 us

## Promoted Shape Samples

1. `aten::copy_` via `external_id=80667`: `{"Concrete Inputs":["","","False"],"Input Dims":[[16384,8192],[16384,8192],[]],"Input Strides":[[8192,1],[8192,1],[]],"Input type":["float","c10::BFloat16","Scalar"]}`
2. `sglang::_run_activation_inplace` via `external_id=80653`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[16384,512],[16384,256]],"Input Strides":[[],[512,1],[256,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`
3. `aten::copy_` via `external_id=163062`: `{"Concrete Inputs":["","","False"],"Input Dims":[[14375,8192],[14375,8192],[]],"Input Strides":[[8192,1],[8192,1],[]],"Input type":["float","c10::BFloat16","Scalar"]}`
4. `sglang::inplace_all_reduce` via `external_id=176352`: `{"Concrete Inputs":["",""],"Input Dims":[[14375,8192],[]],"Input Strides":[[8192,1],[]],"Input type":["c10::BFloat16",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
