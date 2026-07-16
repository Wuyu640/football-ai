class TacticalMatchup:

    def analyse(self, home_style, away_style):

        score = 0
        reasons = []

        if (
            home_style.attack == "High"
            and
            away_style.defense == "Weak"
        ):
            score += 2
            reasons.append("Ataque local muy favorable")

        if (
            away_style.attack == "High"
            and
            home_style.defense == "Weak"
        ):
            score -= 2
            reasons.append("Ataque visitante muy favorable")

        if home_style.defense == "Strong":
            score += 0.5

        if away_style.defense == "Strong":
            score -= 0.5

        return {
            "tactical_score": round(score, 2),
            "reasons": reasons
        }