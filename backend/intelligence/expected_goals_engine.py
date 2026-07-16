class ExpectedGoalsEngine:

    HOME_ADVANTAGE = 0.20

    def calculate(

        self,

        home,

        away

    ):

        home_xg = (

            home.home_attack

            +

            away.away_defense

        ) / 2

        away_xg = (

            away.away_attack

            +

            home.home_defense

        ) / 2

        home_xg += self.HOME_ADVANTAGE

        return {

            "home_xg": round(

                home_xg,

                2

            ),

            "away_xg": round(

                away_xg,

                2

            )

        }