FOLDER="step_37_flash"
MODEL="stepfun-ai/Step-3.7-Flash-NVFP4"
CLEANUP_NAME="Step-3.7-Flash NVFP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  sglang serve
  --model-path "${MODEL}"
  --tp 8
  --ep 8
  --moe-runner-backend flashinfer_trtllm
  --kv-cache-dtype fp8_e4m3
  --quantization modelopt_fp4
  --attention-backend trtllm_mha
  --trust-remote-code
  --reasoning-parser step3p5
  --host 0.0.0.0
  --port "${PORT}"
)

