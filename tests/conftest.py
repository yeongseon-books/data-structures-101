from __future__ import annotations

import importlib.util
from pathlib import Path


def load_module(rel_path: str):
    root = Path(__file__).resolve().parents[1]
    path = root / rel_path
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
