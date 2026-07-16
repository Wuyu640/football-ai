from backend.data_engine.local_provider import LocalProvider

provider = LocalProvider()

matches = provider.load(
    "PD",
    2025
)

print()

print("Partidos:", len(matches))

print()

print(matches[0]["homeTeam"]["name"])