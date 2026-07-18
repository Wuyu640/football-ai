from __future__ import annotations

from backend.engine.stats_engine import StatsEngine


class AttackEngine:

    def __init__(self):
        self.stats = StatsEngine()

    def analyse(
        self,
        team: str,
        league: str | None = None,
        season: int | None = None,
    ):

        data = self.stats.analyse(
            team_name=team,
            league=league,
            season=season,
        )

        avg_goals = data["avg_gf"]
        recent_goals = data["recent_avg_gf"]

        score = (

            avg_goals * 35

            + recent_goals * 30

            + data["win_rate"] * 20

            - data["failed_to_score_rate"] * 25

            + data["home_points_per_game"] * 5

            + data["away_points_per_game"] * 5

        )

        score = max(0, min(round(score, 2), 100))

        if score >= 80:
            strength = "elite"
        elif score >= 65:
            strength = "strong"
        elif score >= 50:
            strength = "average"
        elif score >= 35:
            strength = "weak"
        else:
            strength = "very_weak"

        return {

            "score": score,

            "strength": strength,

            "avg_goals": avg_goals,

            "recent_avg_goals": recent_goals,

            "win_rate": data["win_rate"],

            "failed_to_score_rate": data[
                "failed_to_score_rate"
            ]

        }