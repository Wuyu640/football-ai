from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.xg_engine import XGEngine

analysis = MatchAnalyzer().analyse(
    "FC Barcelona",
    "Real Madrid CF"
)

xg = XGEngine().calculate(analysis)

print()

for k, v in xg.items():
    print(f"{k:12} {v}")