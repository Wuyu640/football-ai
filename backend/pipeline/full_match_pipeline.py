from backend.intelligence.team_rating_engine import TeamRatingEngine
from backend.intelligence.expected_goals_engine import ExpectedGoalsEngine
from backend.intelligence.match_probability_engine import MatchProbabilityEngine
from backend.intelligence.score_matrix_engine import ScoreMatrixEngine
from backend.intelligence.market_extractor import MarketExtractor


class FullMatchPipeline:

    def __init__(self):

        self.rating = TeamRatingEngine()

        self.xg = ExpectedGoalsEngine()

        self.probability = MatchProbabilityEngine()

        self.matrix = ScoreMatrixEngine()

        self.market = MarketExtractor()

    def analyse(

        self,

        home,

        away

    ):

        home_rating = self.rating.analyse(home)

        away_rating = self.rating.analyse(away)

        xg = self.xg.calculate(

            home_rating,

            away_rating

        )

        distributions = self.probability.calculate(

            xg["home_xg"],

            xg["away_xg"]

        )

        matrix = self.matrix.build(

            distributions["home"],

            distributions["away"]

        )

        markets = self.market.analyse(

            matrix

        )

        return {

            "ratings": {

                "home": home_rating,

                "away": away_rating

            },

            "xg": xg,

            "markets": markets

        }