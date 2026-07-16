from backend.engine.history_engine import HistoryEngine

engine = HistoryEngine()

matches = engine.last_matches("FC Barcelona")

print("Últimos partidos:\n")

for match in matches:

    print(
        match["homeTeam"]["name"],
        "vs",
        match["awayTeam"]["name"],
        "|",
        match["score"]["fullTime"]
    )