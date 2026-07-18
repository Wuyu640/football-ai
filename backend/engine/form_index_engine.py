class FormIndexEngine:

    def calculate(self, profile):

        if profile["played"] == 0:
            return 50.0

        points = (profile["recent_points"] / 15) * 40

        attack = min(
            profile["recent_avg_gf"] * 15,
            30
        )

        defense = max(
            0,
            30 - profile["recent_avg_ga"] * 15
        )

        value = points + attack + defense

        value = max(
            0,
            min(
                100,
                value
            )
        )

        return round(value, 2)