from backend.engine.elo_engine import EloEngine
from backend.engine.history_engine import HistoryEngine


class ScheduleStrength:

    def __init__(self):

        self.history = HistoryEngine()
        self.elo = EloEngine()

    def analyse(self, team):

        ratings = self.elo.calculate()

        matches = self.history.last_matches(team, 10)

        total = 0
        played = 0

        for match in matches:

            if match["homeTeam"]["name"] == team:
                rival = match["awayTeam"]["name"]
            else:
                rival = match["homeTeam"]["name"]

            total += ratings.get(rival, 1500)
            played += 1

        if played == 0:
            return 1500

        return round(total / played, 1)