from __future__ import annotations

from backend.data_engine.league_provider import LeagueProvider


class EloEngine:

    BASE_ELO = 1500
    K = 20
    HOME_ADVANTAGE = 75

    def __init__(self):
        self.provider = LeagueProvider()

    @staticmethod
    def expected(elo_a: float, elo_b: float) -> float:
        return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

    def calculate(
        self,
        league: str | None = None,
        season: int | None = None,
    ):

        ratings = {}

        matches = self.provider.matches(
            league=league,
            season=season,
        )

        for match in sorted(
            matches,
            key=lambda m: m["utcDate"],
        ):

            if match["status"] != "FINISHED":
                continue

            home = match["homeTeam"]["name"]
            away = match["awayTeam"]["name"]

            hg = match["score"]["fullTime"]["home"]
            ag = match["score"]["fullTime"]["away"]

            ratings.setdefault(home, self.BASE_ELO)
            ratings.setdefault(away, self.BASE_ELO)

            home_elo = ratings[home]
            away_elo = ratings[away]

            expected_home = self.expected(
                home_elo + self.HOME_ADVANTAGE,
                away_elo,
            )

            expected_away = 1 - expected_home

            if hg > ag:
                score_home = 1.0
                score_away = 0.0
            elif hg < ag:
                score_home = 0.0
                score_away = 1.0
            else:
                score_home = 0.5
                score_away = 0.5

            margin = max(abs(hg - ag), 1)

            k = self.K * (
                1 + (margin - 1) * 0.25
            )

            ratings[home] += k * (
                score_home - expected_home
            )

            ratings[away] += k * (
                score_away - expected_away
            )

        return dict(
            sorted(
                ratings.items(),
                key=lambda x: x[1],
                reverse=True,
            )
        )