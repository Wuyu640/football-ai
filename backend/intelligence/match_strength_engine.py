class MatchStrengthEngine:

    def compare(

        self,

        home,

        away

    ):

        home_strength = (

            home["attack"]

            +

            home["defense"]

            +

            home["form"]

        )

        away_strength = (

            away["attack"]

            +

            away["defense"]

            +

            away["form"]

        )

        difference = round(

            home_strength

            -

            away_strength,

            2

        )

        return {

            "home_strength": round(home_strength, 2),

            "away_strength": round(away_strength, 2),

            "difference": difference

        }