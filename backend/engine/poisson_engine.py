import math


class PoissonEngine:

    def probability(self, goals, xg):

        return (
            math.exp(-xg)
            * (xg ** goals)
            / math.factorial(goals)
        )

    def matrix(self, home_xg, away_xg):

        result = {}

        for home in range(6):
            for away in range(6):

                result[(home, away)] = (
                    self.probability(home, home_xg)
                    *
                    self.probability(away, away_xg)
                )

        return result