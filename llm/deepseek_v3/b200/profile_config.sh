FOLDER="deepseek_v3"
MODEL="deepseek-ai/DeepSeek-V3"
CLEANUP_NAME="DeepSeek-V3 FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 8
  --speculative-algorithm EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --host 0.0.0.0
  --port "${PORT}"
)
