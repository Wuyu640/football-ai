from backend.database.models import Team, Match
from backend.data_engine.provider import DataProvider


class MockProvider(DataProvider):

    def get_team(self, team_name):

        return Team(
            name=team_name,
            attack=80,
            defense=80,
            elo=1800
        )

    def get_match(self, home, away):

        return Match(
            home=self.get_team(home),
            away=self.get_team(away)
        )