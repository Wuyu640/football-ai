import random

from backend.engine.xg_engine import XGEngine
from backend.engine.poisson_engine import PoissonEngine


class SimulationEngine:

    def __init__(self):

        self.xg = XGEngine()
        self.poisson = PoissonEngine()

    def simulate(self, analysis, simulations=10000):

        xg = self.xg.calculate(analysis)

        matrix = self.poisson.matrix(
            xg["home_xg"],
            xg["away_xg"]
        )

        home = 0
        draw = 0
        away = 0

        probabilities = list(matrix.items())

        for _ in range(simulations):

            r = random.random()

            total = 0

            for (hg, ag), p in probabilities:

                total += p

                if r <= total:

                    if hg > ag:
                        home += 1

                    elif hg == ag:
                        draw += 1

                    else:
                        away += 1

                    break

        return {

            "home": round(home / simulations, 3),

            "draw": round(draw / simulations, 3),

            "away": round(away / simulations, 3)

        }