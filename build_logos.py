"""Re-generate ingestion/logos.py from the maintained source in this script if needed.

This project now keeps ingestion/logos.py as the source of truth. This helper remains
for convenience and simply validates that the module is importable.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

mod = importlib.import_module("ingestion.logos")
print("ingestion.logos OK:", getattr(mod, "DEFAULT_PROVIDER_ORDER", None))
