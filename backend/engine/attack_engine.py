from backend.engine.stats_engine import StatsEngine


class AttackEngine:

    def __init__(self):
        self.stats = StatsEngine()

    def analyse(self, team):

        data = self.stats.analyse(team)

        attack_score = (
            data["avg_gf"] * 30
            + data["wins"] * 2
            - data["failed_to_score"] * 5
        )

        return {
            "score": round(attack_score, 2),
            "avg_goals": data["avg_gf"]
        }