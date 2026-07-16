from pprint import pprint

from backend.engine.unified_prediction_engine import UnifiedPredictionEngine

engine = UnifiedPredictionEngine()

result = engine.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

pprint(result)