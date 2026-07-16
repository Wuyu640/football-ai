from pprint import pprint

from backend.intelligence.monte_carlo_engine import MonteCarloEngine

engine = MonteCarloEngine()

probabilities = {

    "home": 0.55,

    "draw": 0.25,

    "away": 0.20

}

pprint(

    engine.simulate(

        probabilities,

        10000

    )

)