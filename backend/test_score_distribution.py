from pprint import pprint

from backend.intelligence.score_distribution import ScoreDistribution

engine = ScoreDistribution()

pprint(

    engine.analyse(

        2.2,

        1.4,

        5000

    )

)