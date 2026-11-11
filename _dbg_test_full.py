"""Test complet d'un match (entités + match + lineups + events)."""
import traceback
from ingestion.loaders import reference, matches, lineups as lu, events as ev_mod, matches, lineups as lu, events as ev_mod
from ingestion.db import make_engine

e = make_engine()
m = {"match_id": 7584,
     "home_team": {"home_team_id": 7, "home_team_name": "France", "country": {"id": 782, "name": "France"}},
     "away_team": {"away_team_id": 8, "away_team_name": "Australia", "country": {"id": 1611, "name": "Australia"}}}

# fake minimal structure comme matches.json
import json
real = json.load(open(r"data\open-data\open-data-master\data\matches\43\3.json", encoding="utf-8"))
m = next(x for x in real if x["match_id"] == 7584)

with e.begin() as conn:
    try:
        reference.load_static_reference(conn)
        reference.load_match_entities(conn, [m])
        players = reference.collect_players([m], {})
        reference.upsert_players(conn, players)
        matches.load_matches(conn, [m])
        print("match OK")
        lu.load_lineups(conn, 7584)
        print("lineups OK")
        cnt = ev_mod.load_events(conn, 7584)
        print("events OK :", cnt["events"])
    except Exception:
        traceback.print_exc()
