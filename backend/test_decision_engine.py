from pprint import pprint

from backend.intelligence.decision_engine import DecisionEngine

engine = DecisionEngine()

analyses = {

    "tactical": {

        "score": 3.4

    },

    "context": {

        "score": 1.2

    },

    "coach": {

        "score": 0.8

    },

    "player": {

        "score": -0.6

    },

    "market": {

        "score": 0.4

    }

}

pprint(

    engine.decide(

        analyses

    )

)