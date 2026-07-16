class MatchAdjustmentEngine:

    def adjust(

        self,

        home_xg,

        away_xg,

        home_rating,

        away_rating

    ):

        tempo = (

            home_rating.attack +

            away_rating.attack

        ) / 2

        defensive_balance = (

            home_rating.defense +

            away_rating.defense

        ) / 2

        if tempo > 2:

            home_xg += 0.15

            away_xg += 0.10

        if defensive_balance > 2:

            home_xg -= 0.10

            away_xg -= 0.10

        return {

            "home_xg": round(home_xg, 2),

            "away_xg": round(away_xg, 2)

        }