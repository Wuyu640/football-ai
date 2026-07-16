from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.xg_engine import XGEngine
from backend.engine.poisson_engine import PoissonEngine

analysis = MatchAnalyzer().analyse(
    "FC Barcelona",
    "Real Madrid CF"
)

xg = XGEngine().calculate(analysis)

matrix = PoissonEngine().matrix(
    xg["home_xg"],
    xg["away_xg"]
)

top = sorted(
    matrix.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nMarcadores más probables\n")

for score, prob in top[:15]:
    print(
        f"{score[0]}-{score[1]}   {prob*100:.2f}%"
    )