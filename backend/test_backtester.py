from pprint import pprint

from backend.evaluation.backtester import Backtester

engine = Backtester()

predictions = [

    "H",

    "H",

    "D",

    "A",

    "H",

    "D",

    "A"

]

results = [

    "H",

    "A",

    "D",

    "A",

    "H",

    "H",

    "A"

]

pprint(

    engine.evaluate_1x2(

        predictions,

        results

    )

)