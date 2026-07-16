from pprint import pprint

from backend.intelligence.scenario_engine import ScenarioEngine

from backend.intelligence.scenario_evaluator import ScenarioEvaluator

engine = ScenarioEngine()

evaluator = ScenarioEvaluator()

probabilities = {

    "home": 0.55,

    "draw": 0.25,

    "away": 0.20

}

scenarios = engine.generate(

    probabilities

)

pprint(

    evaluator.evaluate(

        scenarios

    )

)