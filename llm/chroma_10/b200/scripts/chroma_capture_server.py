#!/usr/bin/env python3
"""Launch Chroma with runtime SGLang kernel interface capture enabled."""

from __future__ import annotations

import os

import api_server
import uvicorn
from chroma_kernel_capture_patch import install


def main() -> None:
    install()
    uvicorn.run(
        api_server.app,
        host="0.0.0.0",
        port=int(os.environ.get("CHROMA_PORT", "8000")),
        workers=1,
        log_level="info",
    )


if __name__ == "__main__":
    main()
