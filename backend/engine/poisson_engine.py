from __future__ import annotations

import math


class PoissonEngine:

    MAX_GOALS = 6

    @staticmethod
    def probability(
        goals: int,
        xg: float,
    ) -> float:

        if xg <= 0:
            return 0.0

        return (
            math.exp(-xg)
            * (xg ** goals)
            / math.factorial(goals)
        )

    def matrix(
        self,
        home_xg: float,
        away_xg: float,
    ):

        matrix = {}

        total = 0.0

        for home in range(self.MAX_GOALS + 1):

            home_probability = self.probability(
                home,
                home_xg,
            )

            for away in range(self.MAX_GOALS + 1):

                away_probability = self.probability(
                    away,
                    away_xg,
                )

                probability = (
                    home_probability
                    * away_probability
                )

                matrix[(home, away)] = probability

                total += probability

        if total > 0:

            for score in matrix:
                matrix[score] /= total

        return matrix

    def most_likely_scores(
        self,
        home_xg: float,
        away_xg: float,
        limit: int = 10,
    ):

        matrix = self.matrix(
            home_xg,
            away_xg,
        )

        return sorted(
            matrix.items(),
            key=lambda item: item[1],
            reverse=True,
        )[:limit]