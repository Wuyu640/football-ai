class DecisionBrain:

    WEIGHTS = {

        "tactical": 0.35,

        "context": 0.15,

        "player": 0.20,

        "coach": 0.10,

        "market": 0.20

    }

    def analyse(self, brains):

        total = 0

        details = {}

        for name, result in brains.items():

            score = result.get("score", 0)

            weight = self.WEIGHTS.get(name, 0)

            weighted = score * weight

            details[name] = {

                "score": round(score, 2),

                "weight": weight,

                "weighted_score": round(weighted, 2)

            }

            total += weighted

        return {

            "score": round(total, 2),

            "details": details

        }