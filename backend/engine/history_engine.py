from backend.data_engine.cache import Cache
from backend.data_engine.league_provider import LeagueProvider


class HistoryEngine:

    def __init__(self):

        self.provider = LeagueProvider()
        self.cache = Cache()

    def last_matches(self, team, amount=10):

        key = f"matches_{team}"

        cached = self.cache.get(key)

        if cached is not None:
            return cached[:amount]

        matches = self.provider.team_matches(team)

        matches = sorted(
            matches,
            key=lambda m: m["utcDate"],
            reverse=True
        )

        self.cache.set(key, matches)

        return matches[:amount]

    def home_matches(self, team, amount=10):

        matches = self.last_matches(team, 50)

        return [
            m for m in matches
            if m["homeTeam"]["name"] == team
        ][:amount]

    def away_matches(self, team, amount=10):

        matches = self.last_matches(team, 50)

        return [
            m for m in matches
            if m["awayTeam"]["name"] == team
        ][:amount]

    def last_n_matches(self, team, amount):

        return self.last_matches(team, amount)