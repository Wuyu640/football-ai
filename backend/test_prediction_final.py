from pprint import pprint

from backend.engine.prediction_engine import PredictionEngine

engine = PredictionEngine()

result = engine.predict(
    "FC Barcelona",
    "Real Madrid CF"
)

pprint(result)