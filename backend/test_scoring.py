from pprint import pprint

from backend.engine.scoring_engine import ScoringEngine

engine = ScoringEngine()

result = engine.calculate(
    "FC Barcelona",
    "Real Madrid CF"
)

pprint(result)