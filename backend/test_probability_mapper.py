from pprint import pprint

from backend.intelligence.probability_mapper import ProbabilityMapper

mapper = ProbabilityMapper()

comparison = {

    "home_score": 4,

    "draw_score": 1,

    "away_score": 0

}

pprint(

    mapper.convert(

        comparison

    )

)