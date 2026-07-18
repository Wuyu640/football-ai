from __future__ import annotations

from backend.engine.elo_engine import EloEngine
from backend.engine.history_engine import HistoryEngine


class ScheduleStrength:

    def __init__(self):
        self.history = HistoryEngine()
        self.elo = EloEngine()

    def analyse(
        self,
        team: str,
        league: str | None = None,
        season: int | None = None,
    ):

        ratings = self.elo.calculate(
            league=league,
            season=season,
        )

        matches = self.history.last_matches(
            team=team,
            amount=10,
            league=league,
            season=season,
        )

        rivals = []

        for match in matches:

            if match["homeTeam"]["name"] == team:
                rivals.append(
                    match["awayTeam"]["name"]
                )
            else:
                rivals.append(
                    match["homeTeam"]["name"]
                )

        if not rivals:
            return {
                "average_elo": 1500,
                "difficulty": "unknown",
            }

        average = round(
            sum(
                ratings.get(rival, 1500)
                for rival in rivals
            ) / len(rivals),
            1,
        )

        if average >= 1700:
            difficulty = "very_hard"
        elif average >= 1600:
            difficulty = "hard"
        elif average >= 1500:
            difficulty = "medium"
        else:
            difficulty = "easy"

        return {

            "average_elo": average,

            "difficulty": difficulty,

            "matches": len(rivals),

        }