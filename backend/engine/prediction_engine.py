from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.xg_engine import XGEngine
from backend.engine.poisson_engine import PoissonEngine


class PredictionEngine:

    def __init__(self):

        self.analysis = MatchAnalyzer()
        self.xg = XGEngine()
        self.poisson = PoissonEngine()

    def predict(self, home, away):

        # Análisis del partido
        analysis = self.analysis.analyse(home, away)

        # xG
        xg = self.xg.calculate(analysis)

        # Matriz de Poisson
        matrix = self.poisson.matrix(
            xg["home_xg"],
            xg["away_xg"]
        )

        home_probability = 0.0
        draw_probability = 0.0
        away_probability = 0.0

        btts_probability = 0.0
        over25_probability = 0.0

        for (home_goals, away_goals), probability in matrix.items():

            if home_goals > away_goals:
                home_probability += probability

            elif home_goals == away_goals:
                draw_probability += probability

            else:
                away_probability += probability

            if home_goals > 0 and away_goals > 0:
                btts_probability += probability

            if home_goals + away_goals >= 3:
                over25_probability += probability

        best_scores = sorted(
            matrix.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        return {

            "analysis": analysis,

            "xg": xg,

            "probabilities": {

                "home": round(home_probability, 3),
                "draw": round(draw_probability, 3),
                "away": round(away_probability, 3)

            },

            "markets": {

                "btts": round(btts_probability, 3),
                "over25": round(over25_probability, 3)

            },

            "scores": [

                {
                    "score": f"{h}-{a}",
                    "probability": round(p, 4)
                }

                for (h, a), p in best_scores

            ]

        }