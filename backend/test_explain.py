from pprint import pprint

from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.prediction_engine import PredictionEngine
from backend.engine.explain_engine import ExplainEngine

analysis = MatchAnalyzer().analyse(
    "FC Barcelona",
    "Real Madrid CF"
)

prediction = PredictionEngine().predict(
    "FC Barcelona",
    "Real Madrid CF"
)

result = ExplainEngine().analyse(
    analysis,
    prediction
)

pprint(result)