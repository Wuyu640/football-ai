class WeightedRatingEngine:

    def calculate(

        self,

        rating,

        opponent_factor

    ):

        return round(

            rating * opponent_factor,

            2

        )