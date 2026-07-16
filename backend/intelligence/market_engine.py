class MarketEngine:

    def analyse(

        self,

        probabilities

    ):

        home_attack = probabilities["home"]

        away_attack = probabilities["away"]

        over25 = sum(

            home_attack[2:]

        ) * sum(

            away_attack[1:]

        )

        btts = sum(

            home_attack[1:]

        ) * sum(

            away_attack[1:]

        )

        return {

            "over25": round(

                over25,

                3

            ),

            "btts": round(

                btts,

                3

            )

        }