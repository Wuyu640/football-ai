class Evaluator:

    def evaluate(self, prediction, result):

        predicted = max(
            prediction,
            key=prediction.get
        )

        if predicted == result:
            return 1

        return 0