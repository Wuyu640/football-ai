class PlayerBrain:

    def analyse(self, injuries):

        score = 0
        reasons = []

        score -= injuries["impact_home"] * 10

        score += injuries["impact_away"] * 10

        return {

            "score": round(score, 2),

            "reasons": reasons

        }