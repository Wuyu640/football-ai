class CoachBrain:

    def analyse(self, coach):

        score = 0
        reasons = []

        experience = coach.get("experience", 0)
        adaptability = coach.get("adaptability", 0)
        mentality = coach.get("mentality", 0)

        score += experience * 4
        score += adaptability * 3
        score += mentality * 3

        return {

            "score": round(score, 2),

            "reasons": reasons

        }