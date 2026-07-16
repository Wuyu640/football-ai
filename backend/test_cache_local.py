from time import perf_counter

from backend.data_engine.league_provider import LeagueProvider

provider = LeagueProvider()

t1 = perf_counter()

provider.matches("PD", 2025)

t2 = perf_counter()

print()

print(f"{t2-t1:.4f} segundos")