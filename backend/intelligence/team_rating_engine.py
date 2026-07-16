from backend.engine.stats_engine import StatsEngine

from backend.models.team_rating import TeamRating


class TeamRatingEngine:

    def __init__(self):

        self.stats = StatsEngine()

    def analyse(

        self,

        team

    ):

        s = self.stats.analyse(team)

        return TeamRating(

            attack=round(

                s["avg_gf"],

                2

            ),

            defense=round(

                max(

                    0.2,

                    3 - s["avg_ga"]

                ),

                2

            ),

            form=round(

                s["recent_points"] / 15,

                2

            ),

            home_attack=s["home_avg_gf"],

            away_attack=s["away_avg_gf"],

            home_defense=round(

                max(

                    0.2,

                    3 - s["avg_ga"]

                ),

                2

            ),

            away_defense=round(

                max(

                    0.2,

                    3 - s["avg_ga"]

                ),

                2

            )

        )