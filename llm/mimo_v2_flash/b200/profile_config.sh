FOLDER="mimo_v2_flash"
MODEL="XiaomiMiMo/MiMo-V2-Flash"
CLEANUP_NAME="MiMo-V2-Flash"
COOKBOOK_PAGE="Xiaomi/MiMo-V2-Flash.md"
DOCKER_IMAGE="lmsysorg/sglang:dev-pr-15207"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}
export SGLANG_ENABLE_SPEC_V2=${SGLANG_ENABLE_SPEC_V2:-0}
export HF_HUB_ENABLE_HF_TRANSFER=${HF_HUB_ENABLE_HF_TRANSFER:-0}
export HF_HUB_CACHE=${HF_HUB_CACHE:-/root/.cache/huggingface}
WEIGHT_CACHE=${WEIGHT_CACHE:-/root/.cache/huggingface/models--XiaomiMiMo--MiMo-V2-Flash}
LOCK_CACHE=${LOCK_CACHE:-/root/.cache/huggingface/.locks/models--XiaomiMiMo--MiMo-V2-Flash}

# Cookbook NVIDIA command adapted for B200: the image's FA3 backend rejects SM100,
# flashinfer cannot handle MiMo's attention sinks argument in this image, and
# EAGLE+flashinfer draft attention asserts. Use the Triton attention fallback
# to try to keep the main TP8/DP2/DP-attention path runnable.
SERVER_ARGS=(
  sglang serve
  --model-path "${MODEL}"
  --trust-remote-code
  --tp-size 8
  --dp-size 2
  --enable-dp-attention
  --mem-fraction-static 0.75
  --max-running-requests 128
  --disable-cuda-graph
  --chunked-prefill-size 16384
  --model-loader-extra-config '{"enable_multithread_load":"true","num_threads":64}'
  --attention-backend triton
  --reasoning-parser qwen3
  --tool-call-parser mimo
  --host 0.0.0.0
  --port "${PORT}"
)
