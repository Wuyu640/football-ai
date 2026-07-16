from backend.engine.team_profile import TeamProfile
from backend.engine.elo_engine import EloEngine


class MatchAnalyzer:

    def __init__(self):

        self.profile = TeamProfile()
        self.elo = EloEngine()

    def analyse(self, home, away):

        home_profile = self.profile.build(home)
        away_profile = self.profile.build(away)

        ratings = self.elo.calculate()

        home_elo = ratings.get(home, 1500)
        away_elo = ratings.get(away, 1500)

        analysis = {

            "home": home,

            "away": away,

            "elo_difference": round(home_elo - away_elo, 1),

            "goal_difference":
                round(
                    home_profile["avg_gf"] -
                    away_profile["avg_gf"],
                    2
                ),

            "defense_difference":
                round(
                    away_profile["avg_ga"] -
                    home_profile["avg_ga"],
                    2
                ),

            "form_difference":
                round(
                    (
                        home_profile["wins"] / max(home_profile["played"], 1)
                    ) -
                    (
                        away_profile["wins"] / max(away_profile["played"], 1)
                    ),
                    2
                )

        }

        return analysis