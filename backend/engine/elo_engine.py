from backend.data_engine.league_provider import LeagueProvider


class EloEngine:

    BASE_ELO = 1500
    K = 20
    HOME_ADVANTAGE = 75

    def __init__(self):

        self.provider = LeagueProvider()

    def expected(self, elo_a, elo_b):

        return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

    def calculate(self):

        matches = self.provider.matches()

        ratings = {}

        matches = sorted(
            matches,
            key=lambda m: m["utcDate"]
        )

        for match in matches:

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
                away_elo
            )

            expected_away = 1 - expected_home

            if hg > ag:

                score_home = 1
                score_away = 0

            elif hg == ag:

                score_home = 0.5
                score_away = 0.5

            else:

                score_home = 0
                score_away = 1

            ratings[home] += self.K * (score_home - expected_home)
            ratings[away] += self.K * (score_away - expected_away)

        return ratings