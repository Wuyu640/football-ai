from collections import Counter

from backend.intelligence.match_simulator import MatchSimulator


class ScoreDistribution:

    def __init__(self):

        self.simulator = MatchSimulator()

    def analyse(

        self,

        home_attack,

        away_attack,

        simulations=5000

    ):

        scores = Counter()

        for _ in range(simulations):

            result = self.simulator.simulate_match(

                home_attack,

                away_attack

            )

            score = (

                f"{result['home']}-{result['away']}"

            )

            scores[score] += 1

        return scores.most_common(10)