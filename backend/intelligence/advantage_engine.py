class AdvantageEngine:

    def analyse(

        self,

        comparison

    ):

        score = 0

        reasons = []

        for feature, value in comparison.items():

            if value > 0.4:

                score += 1

                reasons.append(

                    f"{feature} favors home"

                )

            elif value < -0.4:

                score -= 1

                reasons.append(

                    f"{feature} favors away"

                )

        return {

            "score": score,

            "reasons": reasons

        }