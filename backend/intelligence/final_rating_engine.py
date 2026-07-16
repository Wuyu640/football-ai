class FinalRatingEngine:

    def calculate(

        self,

        attack,

        defense,

        form

    ):

        rating = (

            attack * 0.45 +

            defense * 0.35 +

            form * 0.20

        )

        return round(

            rating,

            2

        )