#!/bin/bash
# Capture the MiniMax-H3 sub-block sparse arm on sm_103 (the arm that deadlocks ~25%/request).
set -u
W=/scratch/minimax_h3_nvfp4_1957/worktrees/subblock
FI=/scratch/minimax_h3_nvfp4_1957/repos/flashinfer-main
OUT=/scratch/nv_handoff/cap/diff_h3_sparse
mkdir -p $OUT
source /scratch/k3_bench/venv_sgl/bin/activate
export NVCAP_DIR=$OUT NVCAP_CONFIG=/scratch/nv_handoff/tools/targets/diffusion_focus.json
export NVCAP_GROUP_MB=150 NVCAP_MAX_TENSOR_MB=24 NVCAP_MAX_SHAPES_PER_OP=6
export PYTHONPATH=/scratch/nv_handoff/tools:$W/python:$FI
export HF_HOME=/scratch/b300_diffusion_retest_20260813/cache/hf
export SGLANG_SUBBLOCK_SM103_BSA=1
export SGLANG_DIFFUSION_CACHE_ROOT=/scratch/b300_diffusion_retest_20260813/cache/sglang_diffusion
export FLASHINFER_DISABLE_VERSION_CHECK=1 NCCL_NVLS_ENABLE=0
export CUDA_VISIBLE_DEVICES=4,5,6,7
cd $W
echo "h3_sparse_subblock_4gpu" > $OUT/GROUP
sglang generate --backend=sglang --model-path=/scratch/models/minimax_h3 \
  --model-id=MiniMaxAI/MiniMax-H3 --pipeline-class-name=MiniMaxH3Pipeline \
  --config=/scratch/b300_diffusion_retest_20260813/sglang/outputs/diffusion_benchmarks/generated_configs/minimax-h3-t2va.json \
  --prompt "At night, while their owner sleeps in a bedroom, three cats march in loudly playing tiny brass instruments, then abruptly file out." \
  --model-variant=fl2va --num-gpus=4 --tp-size=2 --ulysses-degree=2 --performance-mode=speed \
  --enable-torch-compile=false --seed=42 --save-output \
  --attention-backend subblock_sparse_attn \
  --component-attention-backends '{"text_encoder":"fa"}' \
  --attention-backend-config '{"sparsity":0.75,"n_k":4,"n_q":4,"skip_first_steps":10,"skip_first_layers":0,"min_seq_len":4096}'
rc=$?
rm -f $OUT/GROUP
echo "H3_SPARSE_DONE rc=$rc"
