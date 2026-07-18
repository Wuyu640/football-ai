from backend.engine.stats_engine import StatsEngine
from backend.data_engine.team_stats import TeamStats


class RatingEngine:

    def __init__(self):

        self.team = TeamStats()
        self.stats = StatsEngine()

    def calculate(self, home_id, away_id):

        home = self.team.get_team(home_id)
        away = self.team.get_team(away_id)

        home_stats = self.stats.analyse(home["name"])
        away_stats = self.stats.analyse(away["name"])

        home_attack = (
            home_stats["avg_gf"] * 0.45 +
            home_stats["recent_avg_gf"] * 0.35 +
            home_stats["home_avg_gf"] * 0.20
        )

        away_attack = (
            away_stats["avg_gf"] * 0.45 +
            away_stats["recent_avg_gf"] * 0.35 +
            away_stats["away_avg_gf"] * 0.20
        )

        home_defense = (
            (1 / max(home_stats["avg_ga"], 0.1)) * 0.60 +
            (1 / max(home_stats["recent_avg_ga"], 0.1)) * 0.40
        )

        away_defense = (
            (1 / max(away_stats["avg_ga"], 0.1)) * 0.60 +
            (1 / max(away_stats["recent_avg_ga"], 0.1)) * 0.40
        )

        home_form = (
            (home_stats["recent_points"] / 15) * 100
        )

        away_form = (
            (away_stats["recent_points"] / 15) * 100
        )

        home_rating = (
            home_attack * 0.40 +
            home_defense * 10 * 0.35 +
            home_form * 0.25
        )

        away_rating = (
            away_attack * 0.40 +
            away_defense * 10 * 0.35 +
            away_form * 0.25
        )

        if home_rating > away_rating:
            winner = home["name"]
        elif away_rating > home_rating:
            winner = away["name"]
        else:
            winner = "Draw"

        return {

            "home": home["name"],
            "away": away["name"],

            "home_rating": round(home_rating, 2),
            "away_rating": round(away_rating, 2),

            "home_attack": round(home_attack, 2),
            "away_attack": round(away_attack, 2),

            "home_defense": round(home_defense, 2),
            "away_defense": round(away_defense, 2),

            "home_form": round(home_form, 2),
            "away_form": round(away_form, 2),

            "winner": winner,

            "home_stats": home_stats,
            "away_stats": away_stats

        }