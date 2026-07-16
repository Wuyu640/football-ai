from backend.engine.tactical_engine import TacticalEngine


class StyleMatchup:

    def __init__(self):

        self.engine = TacticalEngine()

    def analyse(self, home, away):

        h = self.engine.profile(home)
        a = self.engine.profile(away)

        score = 0
        reasons = []

        if h.possession > a.possession:
            score += 5
            reasons.append("Mayor control de posesión")

        if h.pressing == "High" and a.style == "Transition":
            score -= 3
            reasons.append("El rival puede castigar la presión")

        if h.counter_attack and a.defensive_line == "High":
            score += 7
            reasons.append("Buen contraataque contra línea alta")

        if a.counter_attack and h.defensive_line == "High":
            score -= 7
            reasons.append("Riesgo ante contraataques rivales")

        return {
            "score": score,
            "reasons": reasons
        }