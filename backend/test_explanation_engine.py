from pprint import pprint

from backend.intelligence.explanation_engine import ExplanationEngine

engine = ExplanationEngine()

advantage = {

    "score": 2,

    "reasons": [

        "Attack favors home",

        "Tempo favors home"

    ]

}

pprint(

    engine.explain(

        advantage

    )

)