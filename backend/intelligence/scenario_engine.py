class ScenarioEngine:

    def generate(

        self,

        probabilities

    ):

        scenarios = []

        home = probabilities["home"]

        draw = probabilities["draw"]

        away = probabilities["away"]

        if home >= away:

            scenarios.append({

                "name": "Home scores first",

                "weight": round(home, 2)

            })

        if away >= home:

            scenarios.append({

                "name": "Away scores first",

                "weight": round(away, 2)

            })

        scenarios.append({

            "name": "0-0 at half-time",

            "weight": round(draw * 0.8, 2)

        })

        scenarios.append({

            "name": "Open second half",

            "weight": round(

                (home + away) / 2,

                2

            )

        })

        return scenarios