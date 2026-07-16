from backend.training.evaluator import Evaluator

evaluator = Evaluator()

prediction = {

    "home": 0.58,

    "draw": 0.24,

    "away": 0.18

}

print(

    evaluator.evaluate(

        prediction,

        "home"

    )

)

print(

    evaluator.evaluate(

        prediction,

        "away"

    )

)