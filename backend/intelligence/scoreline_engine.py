class ScorelineEngine:

    def predict(

        self,

        evaluation

    ):

        home = evaluation["home"]

        away = evaluation["away"]

        goals = evaluation["goals"]

        if home > away:

            if goals >= 1.5:

                return [

                    "2-1",

                    "2-0",

                    "3-1",

                    "1-0"

                ]

            return [

                "1-0",

                "2-0"

            ]

        if away > home:

            return [

                "0-1",

                "1-2",

                "0-2"

            ]

        return [

            "1-1",

            "0-0"

        ]