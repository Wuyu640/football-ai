from backend.training.evaluator import Evaluator


class Backtester:

    def __init__(self):

        self.evaluator = Evaluator()

    def run(self, predictions):

        total = len(predictions)

        if total == 0:
            return {
                "accuracy": 0,
                "correct": 0,
                "total": 0
            }

        correct = 0

        for item in predictions:

            correct += self.evaluator.evaluate(
                item["prediction"],
                item["result"]
            )

        return {

            "accuracy": round(
                correct / total,
                3
            ),

            "correct": correct,

            "total": total

        }