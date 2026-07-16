from backend.engine.stats_engine import StatsEngine
from backend.data_engine.team_stats import TeamStats


class RatingEngine:

    def __init__(self):
        self.team = TeamStats()
        self.stats = StatsEngine()

    def calculate(self, home_id, away_id):

        home = self.team.get_team(home_id)
        away = self.team.get_team(away_id)

        home_stats = self.stats.analyse(home_id)
        away_stats = self.stats.analyse(away_id)

        home_strength = (
            home_stats["wins"] * 3
            + home_stats["draws"]
            + home_stats["gf"] * 0.15
        )

        away_strength = (
            away_stats["wins"] * 3
            + away_stats["draws"]
            + away_stats["gf"] * 0.15
        )

        if home_strength > away_strength:
            winner = home["name"]
        elif away_strength > home_strength:
            winner = away["name"]
        else:
            winner = "Draw"

        return {
            "home": home["name"],
            "away": away["name"],
            "home_strength": round(home_strength, 2),
            "away_strength": round(away_strength, 2),
            "winner": winner,
            "home_stats": home_stats,
            "away_stats": away_stats
        }