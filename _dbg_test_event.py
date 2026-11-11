"""Test isolé d'ingestion d'un match pour tracer l'erreur exacte."""
import traceback
from ingestion.loaders import events as ev_mod
from ingestion.db import make_engine

e = make_engine()
with e.begin() as conn:
    try:
        cnt = ev_mod.load_events(conn, 8650)
        print("OK 8650 :", cnt)
    except Exception:
        traceback.print_exc()
