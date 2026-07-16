from backend.engine.elo_engine import EloEngine

elo = EloEngine()

print()

print(
    elo.winner_probability(
        1900,
        1880
    )
)