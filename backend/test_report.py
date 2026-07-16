from pprint import pprint

from backend.evaluation.report import EvaluationReport

engine = EvaluationReport()

evaluation = {

    "accuracy": 0.714,

    "matches": 120,

    "correct": 86,

    "incorrect": 34

}

pprint(

    engine.build(

        evaluation

    )

)