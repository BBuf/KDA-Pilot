FOLDER="qwen35"
MODEL="nvidia/Qwen3.5-397B-A17B-NVFP4"
CLEANUP_NAME="Qwen3.5 397B-A17B NVFP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 4
  --reasoning-parser qwen3
  --tool-call-parser qwen3_coder
  --mem-fraction-static 0.85
  --attention-backend trtllm_mha
  --quantization modelopt_fp4
  --fp4-gemm-backend flashinfer_cutlass
  --kv-cache-dtype fp8_e4m3
  --moe-runner-backend flashinfer_trtllm
  --chunked-prefill-size 32768
  --max-prefill-tokens 32768
  --host 0.0.0.0
  --port "${PORT}"
)
