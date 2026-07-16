import random


class MonteCarloEngine:

    def simulate(

        self,

        probabilities,

        simulations=1000

    ):

        results = {

            "home": 0,

            "draw": 0,

            "away": 0

        }

        for _ in range(simulations):

            r = random.random()

            if r < probabilities["home"]:

                results["home"] += 1

            elif r < (

                probabilities["home"]

                +

                probabilities["draw"]

            ):

                results["draw"] += 1

            else:

                results["away"] += 1

        return {

            "home": round(

                results["home"] / simulations,

                3

            ),

            "draw": round(

                results["draw"] / simulations,

                3

            ),

            "away": round(

                results["away"] / simulations,

                3

            )

        }