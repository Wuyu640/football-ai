from backend.engine.stats_engine import StatsEngine
from backend.models.team_style import TeamStyle


class StyleDetector:

    def __init__(self):
        self.stats = StatsEngine()

    def detect(self, team):

        s = self.stats.analyse(team)

        played = max(s["played"], 1)

        if s["avg_gf"] >= 2:
            attack = "High"
        elif s["avg_gf"] >= 1.4:
            attack = "Medium"
        else:
            attack = "Low"

        if s["avg_ga"] <= 1:
            defense = "Strong"
        elif s["avg_ga"] <= 1.5:
            defense = "Balanced"
        else:
            defense = "Weak"

        return TeamStyle(

            attack=attack,

            defense=defense,

            clean_sheet_rate=round(
                s["clean_sheets"] / played,
                2
            ),

            scoring_rate=round(
                1 - s["failed_to_score"] / played,
                2
            ),

            avg_goals_for=s["avg_gf"],

            avg_goals_against=s["avg_ga"],

            win_rate=round(
                s["wins"] / played,
                2
            ),

            draw_rate=round(
                s["draws"] / played,
                2
            ),

            loss_rate=round(
                s["losses"] / played,
                2
            ),

            over25_rate=s["over25_rate"],

            btts_rate=s["btts_rate"],

            recent_points=s["recent_points"],

            recent_avg_gf=s["recent_avg_gf"],

            recent_avg_ga=s["recent_avg_ga"],

            home_avg_gf=s["home_avg_gf"],

            away_avg_gf=s["away_avg_gf"]

        )