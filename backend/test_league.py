from backend.data_engine.league_provider import LeagueProvider

provider = LeagueProvider()

data = provider.matches()

print("Partidos:", len(data["matches"]))

for match in data["matches"][:10]:
    print(
        match["homeTeam"]["name"],
        "vs",
        match["awayTeam"]["name"],
        "|",
        match["status"]
    )