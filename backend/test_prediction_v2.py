from pprint import pprint

from backend.engine.prediction_engine_v2 import PredictionEngineV2

engine = PredictionEngineV2()

result = engine.analyse(

    "FC Barcelona"

)

pprint(result)