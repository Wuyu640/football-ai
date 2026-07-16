from pprint import pprint

from backend.intelligence.scenario_engine import ScenarioEngine

engine = ScenarioEngine()

probabilities = {

    "home": 0.55,

    "draw": 0.25,

    "away": 0.20

}

pprint(

    engine.generate(

        probabilities

    )

)