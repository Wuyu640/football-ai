class PredictionFactors:

    def analyse(

        self,

        graph

    ):

        score = {

            "home_win": 0,

            "draw": 0,

            "away_win": 0,

            "goals": 0,

            "btts": 0

        }

        for node in graph:

            effect = node["effect"]

            if effect == "High scoring potential":

                score["home_win"] += 2

                score["goals"] += 2

            elif effect == "Good attack":

                score["home_win"] += 1

                score["goals"] += 1

            elif effect == "Weak defense":

                score["goals"] += 2

                score["btts"] += 2

            elif effect == "Solid defense":

                score["draw"] += 1

            elif effect == "Open match":

                score["goals"] += 2

                score["btts"] += 1

            elif effect == "Slow match":

                score["draw"] += 2

        return score