class ProbabilityMapper:

    def convert(

        self,

        comparison

    ):

        home = max(

            comparison["home_score"],

            0

        )

        away = max(

            comparison["away_score"],

            0

        )

        draw = max(

            5 -

            abs(comparison["home_score"]),

            1

        )

        total = home + draw + away

        return {

            "home": round(home / total, 3),

            "draw": round(draw / total, 3),

            "away": round(away / total, 3)

        }