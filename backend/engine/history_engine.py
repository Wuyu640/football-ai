from __future__ import annotations

from backend.data_engine.cache import Cache
from backend.data_engine.league_provider import LeagueProvider


class HistoryEngine:

    def __init__(self):
        self.provider = LeagueProvider()
        self.cache = Cache()

    def last_matches(
        self,
        team: str,
        amount: int = 10,
        league: str | None = None,
        season: int | None = None,
    ):

        key = f"{league}_{season}_{team}"

        matches = self.cache.get(key)

        if matches is None:

            matches = self.provider.team_matches(
                team_name=team,
                league=league,
                season=season,
            )

            matches.sort(
                key=lambda match: match["utcDate"],
                reverse=True,
            )

            self.cache.set(key, matches)

        return matches[:amount]

    def home_matches(
        self,
        team: str,
        amount: int = 10,
        league: str | None = None,
        season: int | None = None,
    ):

        return [

            match

            for match in self.last_matches(
                team,
                50,
                league,
                season,
            )

            if match["homeTeam"]["name"] == team

        ][:amount]

    def away_matches(
        self,
        team: str,
        amount: int = 10,
        league: str | None = None,
        season: int | None = None,
    ):

        return [

            match

            for match in self.last_matches(
                team,
                50,
                league,
                season,
            )

            if match["awayTeam"]["name"] == team

        ][:amount]

    def last_n_matches(
        self,
        team: str,
        amount: int,
        league: str | None = None,
        season: int | None = None,
    ):

        return self.last_matches(
            team=team,
            amount=amount,
            league=league,
            season=season,
        )