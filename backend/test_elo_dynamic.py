from backend.engine.elo_engine import EloEngine

elo = EloEngine()

ratings = elo.calculate()

teams = sorted(
    ratings.items(),
    key=lambda x: x[1],
    reverse=True
)

for team, rating in teams[:20]:

    print(

        f"{team:35} {rating:.1f}"

    )