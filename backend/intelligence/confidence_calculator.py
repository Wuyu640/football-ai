class ConfidenceCalculator:

    def calculate(

        self,

        comparison

    ):

        total = 0

        count = 0

        for value in comparison.values():

            total += abs(value)

            count += 1

        if count == 0:

            return 0.0

        confidence = total / count

        return round(

            min(confidence / 2, 1),

            2

        )