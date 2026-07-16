class DynamicWeightEngine:

    def calculate(self, context):

        weights = {

            "style": 1.0,

            "matchup": 1.0,

            "context": 1.0,

            "coach": 1.0,

            "player": 1.0

        }

        if context.get("knockout"):

            weights["coach"] += 0.3
            weights["context"] += 0.3

        if context.get("derby"):

            weights["player"] += 0.2
            weights["context"] += 0.2

        if context.get("bad_weather"):

            weights["style"] -= 0.2

        return weights