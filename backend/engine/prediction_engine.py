from __future__ import annotations

from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.xg_engine import XGEngine
from backend.engine.poisson_engine import PoissonEngine


class PredictionEngine:

    def __init__(self):
        self.analysis = MatchAnalyzer()
        self.xg = XGEngine()
        self.poisson = PoissonEngine()

    def predict(
        self,
        home: str,
        away: str,
        league: str | None = None,
        season: int | None = None,
    ):

        analysis = self.analysis.analyse(
            home,
            away,
            league,
            season,
        )

        xg = self.xg.calculate(analysis)

        matrix = self.poisson.matrix(
            xg["home_xg"],
            xg["away_xg"],
        )

        home_probability = 0.0
        draw_probability = 0.0
        away_probability = 0.0

        btts_probability = 0.0
        over15_probability = 0.0
        over25_probability = 0.0
        over35_probability = 0.0

        for (hg, ag), probability in matrix.items():

            if hg > ag:
                home_probability += probability

            elif hg == ag:
                draw_probability += probability

            else:
                away_probability += probability

            goals = hg + ag

            if hg > 0 and ag > 0:
                btts_probability += probability

            if goals >= 2:
                over15_probability += probability

            if goals >= 3:
                over25_probability += probability

            if goals >= 4:
                over35_probability += probability

        scores = [

            {
                "score": f"{h}-{a}",
                "probability": round(p, 4),
            }

            for (h, a), p in self.poisson.most_likely_scores(
                xg["home_xg"],
                xg["away_xg"],
            )

        ]

        return {

            "analysis": analysis,

            "xg": xg,

            "probabilities": {

                "home": round(home_probability, 3),
                "draw": round(draw_probability, 3),
                "away": round(away_probability, 3),

            },

            "markets": {

                "btts": round(btts_probability, 3),

                "over15": round(over15_probability, 3),

                "over25": round(over25_probability, 3),

                "over35": round(over35_probability, 3),

            },

            "scores": scores,

            "favorite": max(

                {
                    "home": home_probability,
                    "draw": draw_probability,
                    "away": away_probability,
                },

                key=lambda x: {
                    "home": home_probability,
                    "draw": draw_probability,
                    "away": away_probability,
                }[x],

            ),

        }