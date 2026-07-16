from pprint import pprint

from backend.intelligence.match_probability_engine import MatchProbabilityEngine

from backend.intelligence.market_engine import MarketEngine

probability = MatchProbabilityEngine()

market = MarketEngine()

dist = probability.calculate(

    2.2,

    1.4

)

pprint(

    market.analyse(

        dist

    )

)