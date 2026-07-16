from backend.data_engine.client import FootballDataClient
from backend.data_engine.local_provider import LocalProvider


class LeagueProvider:

    def __init__(self):

        self.client = FootballDataClient()

        self.local = LocalProvider()

    def matches(self, league="PD", season=2025):

        if self.local.exists(
            league,
            season
        ):

            return self.local.load(
                league,
                season
            )

        data = self.client.get(
            f"competitions/{league}/matches?season={season}"
        )

        matches = data["matches"]

        self.local.save(
            league,
            season,
            matches
        )

        return matches

    def team_matches(

        self,

        team_name,

        league="PD",

        season=2025

    ):

        matches = self.matches(
            league,
            season
        )

        result = []

        for match in matches:

            home = match["homeTeam"]["name"]
            away = match["awayTeam"]["name"]

            if (
                home == team_name
                or
                away == team_name
            ):
                result.append(match)

        return result