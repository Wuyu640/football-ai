from backend.engine.stats_engine import StatsEngine


class TeamProfile:

    def __init__(self):

        self.stats = StatsEngine()

    def build(self, team):

        stats = self.stats.analyse(team)

        profile = {

            "team": team,

            "played": stats["played"],

            "wins": stats["wins"],

            "draws": stats["draws"],

            "losses": stats["losses"],

            "gf": stats["gf"],

            "ga": stats["ga"],

            "avg_gf": stats["avg_gf"],

            "avg_ga": stats["avg_ga"],

            "clean_sheets": stats["clean_sheets"],

            "failed_to_score": stats["failed_to_score"]

        }

        return profile