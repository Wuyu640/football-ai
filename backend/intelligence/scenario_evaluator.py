class ScenarioEvaluator:

    def evaluate(

        self,

        scenarios

    ):

        result = {

            "goals": 0,

            "btts": 0,

            "home": 0,

            "away": 0

        }

        for scenario in scenarios:

            name = scenario["name"]

            weight = scenario["weight"]

            if name == "Home scores first":

                result["home"] += weight

                result["goals"] += weight

            elif name == "Away scores first":

                result["away"] += weight

                result["goals"] += weight

            elif name == "0-0 at half-time":

                result["btts"] += weight * 0.3

            elif name == "Open second half":

                result["goals"] += weight * 1.5

                result["btts"] += weight

        return result