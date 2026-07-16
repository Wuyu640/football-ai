from pprint import pprint

from backend.evaluation.season_validator import SeasonValidator

engine = SeasonValidator()

predictions = [

    "H",
    "A",
    "D",
    "H",
    "H",
    "A",
    "D",
    "H"

]

results = [

    "H",
    "A",
    "H",
    "H",
    "D",
    "A",
    "D",
    "H"

]

pprint(

    engine.validate(

        predictions,

        results

    )

)