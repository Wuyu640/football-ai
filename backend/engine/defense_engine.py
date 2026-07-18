from __future__ import annotations

from backend.engine.stats_engine import StatsEngine


class DefenseEngine:

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

        score = (

            100

            - data["avg_ga"] * 35

            - data["recent_avg_ga"] * 25

            + data["clean_sheet_rate"] * 30

            + data["win_rate"] * 10

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

            "avg_conceded": data["avg_ga"],

            "recent_avg_conceded": data["recent_avg_ga"],

            "clean_sheet_rate": data["clean_sheet_rate"]

        }