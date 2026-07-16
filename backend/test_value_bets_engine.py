from pprint import pprint

from backend.intelligence.value_bets_engine import ValueBetsEngine

engine = ValueBetsEngine()

model = {

    "home": 0.54,

    "draw": 0.24,

    "away": 0.22

}

bookmaker = {

    "home": 0.48,

    "draw": 0.27,

    "away": 0.25

}

pprint(

    engine.analyse(

        model,

        bookmaker

    )

)