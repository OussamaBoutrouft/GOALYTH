from ingestion import logos

print("=== TheSportsDB ===")
try:
    url = logos.TheSportsDBProvider().team_logo("Arsenal")
    print("Arsenal logo:", url)
except Exception as e:
    print("Erreur TheSportsDB :", type(e).__name__, e)

print("=== TheSportsDB joueur ===")
try:
    url = logos.TheSportsDBProvider().player_photo("Thierry Henry")
    print("Henry photo:", url)
except Exception as e:
    print("Erreur TheSportsDB joueur :", type(e).__name__, e)

print("=== OpenLigaDB ===")
try:
    url = logos.OpenLigaDBProvider().team_logo("Bayern Munich")
    print("Bayern logo:", url)
except Exception as e:
    print("Erreur OpenLigaDB :", type(e).__name__, e)

print("=== API-Football (sans cle -> None attendu) ===")
print("logo:", logos.APIFootballProvider().team_logo("Arsenal"))

print("=== Orchestrateur (fallback) ===")
try:
    orch = logos.LogoOrchestrator()   # providers gratuits uniquement
    r1 = orch.fetch_team_logo(None, 42, "Arsenal")
    print("Arsenal via orchestrateur:", r1.source, r1.url)
except Exception as e:
    print("orchestrateur:", type(e).__name__, e)

print("=== Wikimedia (fallback direct) ===")
try:
    w = logos.WikimediaCommonsProvider()
    print("Bayern logo wiki:", w.team_logo("FC Bayern Munich"))
except Exception as e:
    print("wikimedia:", type(e).__name__, e)

print("FIN")

print("FIN")
