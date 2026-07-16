from backend.engine.prediction_engine_v2 import PredictionEngineV2
from backend.intelligence.probability_mapper import ProbabilityMapper


class MatchPredictionEngine:

    def __init__(self):

        self.engine = PredictionEngineV2()

        self.mapper = ProbabilityMapper()

    def analyse(

        self,

        home,

        away

    ):

        home_result = self.engine.analyse(home)

        away_result = self.engine.analyse(away)

        home_score = (

            home_result["prediction"]["home_win"]

            -

            away_result["prediction"]["home_win"]

        )

        draw_score = abs(home_score)

        away_score = -home_score

        comparison = {

            "home_score": home_score,

            "draw_score": draw_score,

            "away_score": away_score

        }

        probabilities = self.mapper.convert(

            comparison

        )

        return {

            "home": home_result,

            "away": away_result,

            "comparison": comparison,

            "probabilities": probabilities

        }