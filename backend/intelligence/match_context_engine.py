class MatchContextEngine:

    def analyse(self, context):

        score = 0

        reasons = []

        if context.get("must_win"):

            score += 3

            reasons.append(
                "Uno de los equipos necesita ganar."
            )

        if context.get("knockout"):

            score -= 1

            reasons.append(
                "Las eliminatorias suelen ser más conservadoras."
            )

        if context.get("second_leg"):

            reasons.append(
                "El resultado de la ida puede condicionar el partido."
            )

        if context.get("derby"):

            score += 2

            reasons.append(
                "Los derbis suelen aumentar la intensidad."
            )

        if context.get("bad_weather"):

            score -= 2

            reasons.append(
                "El clima puede reducir el ritmo de juego."
            )

        return {

            "score": score,

            "reasons": reasons

        }