class DecisionEngine:

    def decide(self, analyses):

        total_score = 0

        explanations = []

        for name, analysis in analyses.items():

            score = analysis.get("score", 0)

            total_score += score

            explanations.append({

                "module": name,

                "score": score

            })

        if total_score >= 8:

            confidence = "VERY_HIGH"

        elif total_score >= 4:

            confidence = "HIGH"

        elif total_score >= 0:

            confidence = "MEDIUM"

        else:

            confidence = "LOW"

        return {

            "score": round(total_score, 2),

            "confidence": confidence,

            "modules": explanations

        }