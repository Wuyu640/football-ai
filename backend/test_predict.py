from pprint import pprint

from backend.api.predict import Predictor

engine = Predictor()

pprint(

    engine.predict(

        "FC Barcelona",

        "Real Madrid CF"

    )

)