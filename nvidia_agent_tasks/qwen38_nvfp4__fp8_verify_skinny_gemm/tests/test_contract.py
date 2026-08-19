"""Contract test - CPU only. Checks rows parse, OPS cover every op, SOURCES exist."""
import glob, json, os, sys

TASK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_workloads_parse():
    d = json.load(open(os.path.join(TASK, "bench", "workloads.json")))
    assert d["ops"]
    for o in d["ops"]:
        assert o["rows"], o["op"]
        for r in o["rows"]:
            assert r["group"] != "warmup"
            assert r["real_calls"] > 0

def test_ops_covered():
    import importlib.util
    spec = importlib.util.spec_from_file_location("entry", os.path.join(TASK, "baseline", "entry.py"))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception:
        # baseline_loader may require torch; fall back to a textual check
        src = open(os.path.join(TASK, "baseline", "entry.py")).read()
        d = json.load(open(os.path.join(TASK, "bench", "workloads.json")))
        for o in d["ops"]:
            assert f'"{o["op"]}"' in src, o["op"]
        return
    d = json.load(open(os.path.join(TASK, "bench", "workloads.json")))
    for o in d["ops"]:
        assert o["op"] in mod.OPS, o["op"]

def test_sources_exist():
    for line in open(os.path.join(TASK, "baseline", "SOURCES.txt")):
        if "->" not in line or "not copied" in line:
            continue
        rel = line.split("->")[1].strip()
        assert os.path.exists(os.path.join(TASK, "baseline", rel)), rel

if __name__ == "__main__":
    test_workloads_parse(); test_ops_covered(); test_sources_exist(); print("contract OK")
