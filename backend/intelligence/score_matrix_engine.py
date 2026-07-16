class ScoreMatrixEngine:

    def build(

        self,

        home_distribution,

        away_distribution

    ):

        matrix = []

        for home_goals, home_probability in enumerate(home_distribution):

            row = []

            for away_goals, away_probability in enumerate(away_distribution):

                row.append(

                    round(

                        home_probability *

                        away_probability,

                        6

                    )

                )

            matrix.append(row)

        return matrix