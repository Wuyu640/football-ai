from pprint import pprint

from backend.intelligence.match_probability_engine import MatchProbabilityEngine

engine = MatchProbabilityEngine()

pprint(

    engine.calculate(

        2.1,

        1.4

    )

)