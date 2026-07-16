from pprint import pprint

from backend.metrics.model_metrics import ModelMetrics

metrics = ModelMetrics()

matches = [

    {

        "prediction": {

            "home": 0.60,

            "draw": 0.20,

            "away": 0.20

        },

        "result": "home"

    },

    {

        "prediction": {

            "home": 0.40,

            "draw": 0.30,

            "away": 0.30

        },

        "result": "draw"

    },

    {

        "prediction": {

            "home": 0.20,

            "draw": 0.25,

            "away": 0.55

        },

        "result": "away"

    }

]

pprint(

    metrics.summary(

        matches

    )

)