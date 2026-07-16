class ExplainEngine:

    def analyse(self, analysis, prediction):

        reasons = []

        if analysis["elo_difference"] > 40:
            reasons.append(
                "El equipo local tiene una ventaja importante de nivel (ELO)."
            )

        elif analysis["elo_difference"] < -40:
            reasons.append(
                "El equipo visitante tiene una ventaja importante de nivel (ELO)."
            )

        if analysis["form_difference"] > 0.3:
            reasons.append(
                "El equipo local llega en mejor forma."
            )

        elif analysis["form_difference"] < -0.3:
            reasons.append(
                "El equipo visitante llega en mejor forma."
            )

        if analysis["goal_difference"] > 0.5:
            reasons.append(
                "El ataque local está siendo más efectivo."
            )

        elif analysis["goal_difference"] < -0.5:
            reasons.append(
                "El ataque visitante está siendo más efectivo."
            )

        if not reasons:
            reasons.append(
                "Se espera un partido muy equilibrado."
            )

        return reasons