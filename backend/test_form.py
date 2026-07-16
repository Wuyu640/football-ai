from backend.engine.form_engine import FormEngine

engine = FormEngine()

matches = engine.recent_matches(81)

for match in matches:
    print(
        match["homeTeam"]["name"],
        "vs",
        match["awayTeam"]["name"],
        "|",
        match["status"]
    )