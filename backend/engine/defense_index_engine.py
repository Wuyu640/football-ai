class DefenseIndexEngine:

    def calculate(self, profile):

        defense = (
            (1 / max(profile["avg_ga"], 0.1)) * 0.40 +
            (1 / max(profile["recent_avg_ga"], 0.1)) * 0.35 +
            ((profile["clean_sheets"] / max(profile["played"], 1)) * 10) * 0.25
        )

        defense = max(0.0, min(100.0, defense * 10))

        return round(defense, 2)