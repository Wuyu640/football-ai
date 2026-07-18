from __future__ import annotations

import math


class ProbabilityEngine:

    DRAW_WEIGHT = 0.22

    def calculate(self, analysis):

        score = (

            analysis["elo_difference"] * 0.04

            + analysis["goal_difference"] * 8

            + analysis["defense_difference"] * 8

            + analysis["form_difference"] * 12

        )

        home = 1 / (
            1 + math.exp(-score / 10)
        )

        away = 1 - home

        draw = self.DRAW_WEIGHT

        total = home + away + draw

        home /= total
        draw /= total
        away /= total

        favourite = "draw"

        if home > away and home > draw:
            favourite = "home"

        elif away > home and away > draw:
            favourite = "away"

        confidence = max(
            home,
            draw,
            away
        )

        return {

            "home": round(home, 3),

            "draw": round(draw, 3),

            "away": round(away, 3),

            "favorite": favourite,

            "confidence": round(
                confidence,
                3
            )

        }