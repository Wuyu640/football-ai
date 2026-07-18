class AttackIndexEngine:

    def calculate(self, profile):

        attack = (
            profile["avg_gf"] * 0.35 +
            profile["recent_avg_gf"] * 0.30 +
            profile["home_avg_gf"] * 0.15 +
            (profile["recent_points"] / 15) * 0.20
        )

        attack = max(0.0, min(100.0, attack * 20))

        return round(attack, 2)