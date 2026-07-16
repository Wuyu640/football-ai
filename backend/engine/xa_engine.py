class XAEngine:

    def calculate(self, attack):

        xa = (
            attack["avg_goals"] * 0.75
            + attack["score"] / 100
        )

        return round(xa, 2)