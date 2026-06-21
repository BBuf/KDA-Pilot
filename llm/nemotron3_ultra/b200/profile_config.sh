FOLDER="nemotron3_ultra"
MODEL="nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4"
CLEANUP_NAME="Nemotron3-Ultra 550B-A55B NVFP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --trust-remote-code
  --tp 4
  --speculative-algorithm EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --reasoning-parser nemotron_3
  --tool-call-parser qwen3_coder
  --mamba-scheduler-strategy extra_buffer
  --attention-backend trtllm_mha
  --host 0.0.0.0
  --port "${PORT}"
)
