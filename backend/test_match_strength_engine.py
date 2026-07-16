from pprint import pprint

from backend.intelligence.match_strength_engine import MatchStrengthEngine

engine = MatchStrengthEngine()

home = {

    "attack": 2.3,

    "defense": 1.8,

    "form": 0.8

}

away = {

    "attack": 1.7,

    "defense": 1.6,

    "form": 0.6

}

pprint(

    engine.compare(

        home,

        away

    )

)