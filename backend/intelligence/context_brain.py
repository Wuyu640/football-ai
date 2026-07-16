class ContextBrain:

    def analyse(self, context):

        score = 0
        reasons = []

        score += context["home_advantage"] * 10

        score -= context["travel_penalty"] * 10

        score += context["motivation"] * 8

        score += context["rest_advantage"] * 6

        score += context["weather"] * 3

        score += context["altitude"] * 2

        score += context["crowd"] * 4

        score += context["pitch"] * 2

        if context["home_advantage"] > 0.15:
            reasons.append(
                "El factor campo favorece al equipo local."
            )

        if context["crowd"] > 0.05:
            reasons.append(
                "El apoyo del público puede influir en el rendimiento."
            )

        return {

            "score": round(score, 2),

            "reasons": reasons

        }