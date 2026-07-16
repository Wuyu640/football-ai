from backend.intelligence.probability_engine import ProbabilityEngine


class MatchProbabilityEngine:

    def __init__(self):

        self.engine = ProbabilityEngine()

    def calculate(

        self,

        home_xg,

        away_xg

    ):

        return {

            "home": self.engine.distribution(

                home_xg

            ),

            "away": self.engine.distribution(

                away_xg

            )

        }