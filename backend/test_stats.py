from backend.engine.stats_engine import StatsEngine

engine = StatsEngine()

stats = engine.analyse("FC Barcelona")

print()

for key, value in stats.items():

    print(f"{key:20} {value}")