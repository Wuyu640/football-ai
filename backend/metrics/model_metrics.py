class ModelMetrics:

    def accuracy(self, predictions):

        total = len(predictions)

        if total == 0:
            return 0

        correct = 0

        for match in predictions:

            prediction = max(
                match["prediction"],
                key=match["prediction"].get
            )

            if prediction == match["result"]:
                correct += 1

        return round(
            correct / total,
            4
        )

    def summary(self, predictions):

        return {

            "matches": len(predictions),

            "accuracy": self.accuracy(predictions)

        }