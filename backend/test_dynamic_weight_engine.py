from pprint import pprint

from backend.intelligence.dynamic_weight_engine import DynamicWeightEngine

engine = DynamicWeightEngine()

context = {

    "knockout": True,

    "derby": False,

    "bad_weather": True

}

pprint(

    engine.calculate(

        context

    )

)