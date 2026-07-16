from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.xg_engine import XGEngine
from backend.engine.poisson_engine import PoissonEngine


class PredictionEngine:

    def __init__(self):

        self.analysis = MatchAnalyzer()
        self.xg = XGEngine()
        self.poisson = PoissonEngine()

    def predict(self, home, away):

        analysis = self.analysis.analyse(home, away)

        xg = self.xg.calculate(analysis)

        matrix = self.poisson.matrix(
            xg["home_xg"],
            xg["away_xg"]
        )

        home = 0
        draw = 0
        away = 0

        for (hg, ag), prob in matrix.items():

            if hg > ag:
                home += prob

            elif hg == ag:
                draw += prob

            else:
                away += prob

        best_scores = sorted(
            matrix.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        return {

            "xg": xg,

            "probabilities": {

                "home": round(home, 3),

                "draw": round(draw, 3),

                "away": round(away, 3)

            },

            "scores": [

                {
                    "score": f"{h}-{a}",
                    "probability": round(p, 4)
                }

                for (h, a), p in best_scores

            ]
        }