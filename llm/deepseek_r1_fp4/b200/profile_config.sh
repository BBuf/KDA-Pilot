FOLDER="deepseek_r1_fp4"
MODEL="nvidia/DeepSeek-R1-0528-FP4-v2"
CLEANUP_NAME="DeepSeek-R1-0528 FP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 8
  --moe-runner-backend flashinfer_cutlass
  --speculative-algorithm EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --host 0.0.0.0
  --port "${PORT}"
)
