class Evaluator:

    def accuracy(

        self,

        predictions,

        real_results

    ):

        correct = 0

        total = len(real_results)

        for predicted, real in zip(

            predictions,

            real_results

        ):

            if predicted == real:

                correct += 1

        if total == 0:

            return 0

        return round(

            correct / total,

            3

        )