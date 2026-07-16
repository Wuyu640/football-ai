from pprint import pprint

from backend.intelligence.scoreline_engine import ScorelineEngine

engine = ScorelineEngine()

evaluation = {

    "home": 0.8,

    "away": 0.3,

    "goals": 2.4,

    "btts": 1.2

}

pprint(

    engine.predict(

        evaluation

    )

)