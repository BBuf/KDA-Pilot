FOLDER="glm_5"
MODEL="nvidia/GLM-5-NVFP4"
CLEANUP_NAME="GLM-5 NVFP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 4
  --quantization modelopt_fp4
  --kv-cache-dtype fp8_e4m3
  --nsa-decode-backend trtllm
  --nsa-prefill-backend trtllm
  --moe-runner-backend flashinfer_trtllm
  --enable-flashinfer-allreduce-fusion
  --enable-dp-lm-head
  --disable-radix-cache
  --max-prefill-tokens 32768
  --chunked-prefill-size 32768
  --mem-fraction-static 0.85
  --scheduler-recv-interval 10
  --tokenizer-worker-num 6
  --host 0.0.0.0
  --port "${PORT}"
)
