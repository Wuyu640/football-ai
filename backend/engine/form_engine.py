from __future__ import annotations

from backend.engine.stats_engine import StatsEngine


class FormEngine:

    def __init__(self):
        self.stats = StatsEngine()

    def analyse(
        self,
        team: str,
        league: str | None = None,
        season: int | None = None,
    ):

        stats = self.stats.analyse(
            team,
            league=league,
            season=season,
        )

        points = stats["recent_points_per_game"]

        if points >= 2.4:
            trend = "excellent"
        elif points >= 2.0:
            trend = "very_good"
        elif points >= 1.5:
            trend = "good"
        elif points >= 1.0:
            trend = "average"
        elif points >= 0.5:
            trend = "poor"
        else:
            trend = "very_poor"

        return {

            "trend": trend,

            "recent_points": stats["recent_points"],

            "recent_points_per_game": stats[
                "recent_points_per_game"
            ],

            "recent_avg_gf": stats[
                "recent_avg_gf"
            ],

            "recent_avg_ga": stats[
                "recent_avg_ga"
            ],

            "goal_difference": round(
                stats["recent_avg_gf"]
                -
                stats["recent_avg_ga"],
                2
            )

        }