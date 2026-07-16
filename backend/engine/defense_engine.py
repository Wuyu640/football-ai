from backend.engine.stats_engine import StatsEngine


class DefenseEngine:

    def __init__(self):
        self.stats = StatsEngine()

    def analyse(self, team):

        data = self.stats.analyse(team)

        defense_score = (
            100
            - data["avg_ga"] * 25
            + data["clean_sheets"] * 3
        )

        return {
            "score": round(defense_score, 2),
            "avg_conceded": data["avg_ga"]
        }