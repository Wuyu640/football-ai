from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.probability_engine import ProbabilityEngine

analysis = MatchAnalyzer().analyse(
    "FC Barcelona",
    "Real Madrid CF"
)

prob = ProbabilityEngine().calculate(analysis)

print("\nProbabilidades\n")

for k, v in prob.items():
    print(f"{k:10} {v*100:.1f}%")