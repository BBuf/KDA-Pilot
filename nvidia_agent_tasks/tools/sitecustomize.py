"""Auto-arm the nvcap capture hook in every SGLang process (server + TP workers).

Python imports ``sitecustomize`` during interpreter start-up, so putting this
directory on PYTHONPATH is enough - no code in the serving stack changes.
"""

try:
    import nvcap  # noqa: F401  (importing installs the hook)
except Exception as _exc:  # never break the server because of the capture hook
    import sys
    print("[nvcap] sitecustomize import failed: %r" % (_exc,), file=sys.stderr)
