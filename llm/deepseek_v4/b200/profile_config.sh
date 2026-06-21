FOLDER="deepseek_v4"
MODEL="deepseek-ai/DeepSeek-V4-Flash"
CLEANUP_NAME="DeepSeek-V4-Flash FP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 4
  --moe-runner-backend flashinfer_mxfp4
  --speculative-algorithm EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --chunked-prefill-size 4096
  --disable-flashinfer-autotune
  --swa-full-tokens-ratio 0.1
  --host 0.0.0.0
  --port "${PORT}"
)
