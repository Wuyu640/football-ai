class ExplanationEngine:

    def explain(

        self,

        advantage

    ):

        lines = []

        if advantage["score"] > 0:

            lines.append(

                "Overall advantage for the home team."

            )

        elif advantage["score"] < 0:

            lines.append(

                "Overall advantage for the away team."

            )

        else:

            lines.append(

                "Balanced match."

            )

        lines.extend(

            advantage["reasons"]

        )

        return lines