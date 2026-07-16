import math


class ProbabilityEngine:

    def poisson(

        self,

        goals,

        expected

    ):

        return (

            math.exp(-expected)

            * (expected ** goals)

            / math.factorial(goals)

        )

    def distribution(

        self,

        expected,

        max_goals=6

    ):

        return [

            round(

                self.poisson(

                    g,

                    expected

                ),

                4

            )

            for g in range(

                max_goals + 1

            )

        ]