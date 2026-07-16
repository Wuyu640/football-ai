from backend.data_engine.client import FootballDataClient


class TeamStats:

    def __init__(self):
        self.client = FootballDataClient()

    def get_team(self, team_id):
        return self.client.get(f"teams/{team_id}")

    def get_matches(self, team_id):
        return self.client.get(
    f"teams/{team_id}/matches?status=FINISHED&limit=10"
)