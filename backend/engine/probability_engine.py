import math


class ProbabilityEngine:

    def calculate(self, analysis):

        score = (
            analysis["elo_difference"] * 0.04
            + analysis["goal_difference"] * 8
            + analysis["defense_difference"] * 8
            + analysis["form_difference"] * 12
        )

        home = 1 / (1 + math.exp(-score / 10))
        away = 1 - home

        draw = 0.22

        total = home + away + draw

        return {
            "home": round(home / total, 3),
            "draw": round(draw / total, 3),
            "away": round(away / total, 3),
        }