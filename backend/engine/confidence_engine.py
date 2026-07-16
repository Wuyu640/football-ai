class ConfidenceEngine:

    def analyse(self, prediction):

        probabilities = prediction["probabilities"]

        confidence = max(
            probabilities["home"],
            probabilities["draw"],
            probabilities["away"]
        )

        confidence *= 100

        reasons = []

        if confidence >= 70:
            reasons.append("Predicción muy consistente.")

        elif confidence >= 55:
            reasons.append("Existe un favorito claro.")

        else:
            reasons.append("Partido muy igualado.")

        return {

            "confidence": round(confidence, 2),

            "reasons": reasons

        }