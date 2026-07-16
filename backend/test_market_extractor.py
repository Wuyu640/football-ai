from pprint import pprint

from backend.intelligence.match_probability_engine import MatchProbabilityEngine

from backend.intelligence.score_matrix_engine import ScoreMatrixEngine

from backend.intelligence.market_extractor import MarketExtractor

probability = MatchProbabilityEngine()

matrix_engine = ScoreMatrixEngine()

extractor = MarketExtractor()

dist = probability.calculate(

    2.2,

    1.3

)

matrix = matrix_engine.build(

    dist["home"],

    dist["away"]

)

pprint(

    extractor.analyse(

        matrix

    )

)