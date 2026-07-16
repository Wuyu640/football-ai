from backend.data_engine.team_stats import TeamStats


class FormEngine:

    def __init__(self):
        self.team = TeamStats()

    def recent_matches(self, team_id):

        data = self.team.get_matches(team_id)

        return data["matches"][:10]