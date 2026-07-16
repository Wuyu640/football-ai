class OpponentStrengthEngine:

    def calculate(

        self,

        opponent_rating

    ):

        if opponent_rating >= 8:

            return 1.25

        elif opponent_rating >= 6:

            return 1.10

        elif opponent_rating >= 4:

            return 1.00

        else:

            return 0.85