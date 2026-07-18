from __future__ import annotations

from backend.data_engine.client import FootballDataClient
from backend.data_engine.local_provider import LocalProvider


class LeagueProvider:

    DEFAULT_LEAGUE = "PD"
    DEFAULT_SEASON = 2025

    def __init__(self):
        self.client = FootballDataClient()
        self.local = LocalProvider()

    def matches(
        self,
        league: str | None = None,
        season: int | None = None,
        force_update: bool = False
    ):

        league = league or self.DEFAULT_LEAGUE
        season = season or self.DEFAULT_SEASON

        if (
            not force_update
            and self.local.exists(league, season)
        ):
            return self.local.load(league, season)

        data = self.client.get(
            f"competitions/{league}/matches?season={season}"
        )

        matches = data.get("matches", [])

        matches = sorted(
            matches,
            key=lambda match: match["utcDate"]
        )

        self.local.save(
            league,
            season,
            matches
        )

        return matches

    def team_matches(
        self,
        team_name: str,
        league: str | None = None,
        season: int | None = None
    ):

        matches = self.matches(
            league=league,
            season=season
        )

        return [

            match

            for match in matches

            if (
                match["homeTeam"]["name"] == team_name
                or
                match["awayTeam"]["name"] == team_name
            )

        ]