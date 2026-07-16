from backend.evaluation.evaluator import Evaluator


class Backtester:

    def __init__(self):

        self.evaluator = Evaluator()

    def evaluate_1x2(

        self,

        predictions,

        results

    ):

        accuracy = self.evaluator.accuracy(

            predictions,

            results

        )

        correct = sum(

            p == r

            for p, r in zip(

                predictions,

                results

            )

        )

        return {

            "accuracy": accuracy,

            "matches": len(results),

            "correct": correct,

            "incorrect": len(results) - correct

        }