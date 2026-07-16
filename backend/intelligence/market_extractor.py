class MarketExtractor:

    def analyse(

        self,

        matrix

    ):

        home = 0

        draw = 0

        away = 0

        btts = 0

        over25 = 0

        exact_scores = {}

        for i, row in enumerate(matrix):

            for j, probability in enumerate(row):

                exact_scores[f"{i}-{j}"] = probability

                if i > j:

                    home += probability

                elif i == j:

                    draw += probability

                else:

                    away += probability

                if i > 0 and j > 0:

                    btts += probability

                if i + j >= 3:

                    over25 += probability

        exact_scores = dict(

            sorted(

                exact_scores.items(),

                key=lambda item: item[1],

                reverse=True

            )

        )

        return {

            "home": round(home, 3),

            "draw": round(draw, 3),

            "away": round(away, 3),

            "btts": round(btts, 3),

            "over25": round(over25, 3),

            "top_scores": list(

                exact_scores.items()

            )[:10]

        }