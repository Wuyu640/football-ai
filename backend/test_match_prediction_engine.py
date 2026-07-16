from pprint import pprint

from backend.engine.match_prediction_engine import MatchPredictionEngine

engine = MatchPredictionEngine()

pprint(

    engine.analyse(

        "FC Barcelona",

        "Real Madrid CF"

    )

)